#!/usr/bin/env python3
"""Landmark-pair fingerprinting vs MinHash/SimHash for near-duplicate detection on GLUE MRPC."""

import sys
import os
import json
import gc
import hashlib
import math
import time
import random
import resource
import multiprocessing as mp
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed

import psutil
import numpy as np
from loguru import logger
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import average_precision_score, precision_recall_curve
from datasketch import MinHash
from scipy.stats import norm as scipy_norm

# ── paths ──────────────────────────────────────────────────────────────────────
WS = Path(__file__).parent
DATA_PATH = Path("/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json")
LOGS_DIR = WS / "logs"
LOGS_DIR.mkdir(exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add(str(LOGS_DIR / "run.log"), rotation="30 MB", level="DEBUG")

# ── resource limits ─────────────────────────────────────────────────────────
_cgroup_limit = int(Path("/sys/fs/cgroup/memory.max").read_text().strip())
RAM_LIMIT = min(_cgroup_limit, 26 * 1024**3)  # 26 GB cap
resource.setrlimit(resource.RLIMIT_AS, (RAM_LIMIT, RAM_LIMIT))
logger.info(f"RAM limit set to {RAM_LIMIT/1e9:.1f} GB")

# ── hardware ────────────────────────────────────────────────────────────────
def _detect_cpus() -> int:
    try:
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except Exception:
        pass
    try:
        return len(os.sched_getaffinity(0))
    except Exception:
        return os.cpu_count() or 1

NUM_CPUS = _detect_cpus()
logger.info(f"CPUs: {NUM_CPUS}")

# ══════════════════════════════════════════════════════════════════════════════
# DATA LOADING
# ══════════════════════════════════════════════════════════════════════════════

def load_mrpc(path: Path, max_examples: int = None):
    """Load GLUE MRPC pairs from full_data_out.json."""
    logger.info(f"Loading data from {path}")
    data = json.loads(path.read_text())
    examples = data["datasets"][0]["examples"]
    if max_examples:
        examples = examples[:max_examples]
    pairs = []
    for ex in examples:
        inp = json.loads(ex["input"])
        label = int(ex["output"])
        pairs.append({
            "id": ex["metadata_row_index"],
            "sentence1": inp["sentence1"],
            "sentence2": inp["sentence2"],
            "label": label,
            "raw": ex,
        })
    logger.info(f"Loaded {len(pairs)} pairs, positive rate={sum(p['label'] for p in pairs)/len(pairs):.3f}")
    return pairs


# ══════════════════════════════════════════════════════════════════════════════
# SYNTHETIC STRUCTURAL EDITS
# ══════════════════════════════════════════════════════════════════════════════

_FILLER_SENTENCES = [
    "The organization announced its plans last week.",
    "Officials declined to comment on the matter.",
    "Experts say the situation remains uncertain.",
    "The report was released on Monday morning.",
    "Sources familiar with the matter confirmed.",
    "The meeting took place in Washington D.C.",
    "According to a spokesperson for the company.",
    "The decision was made after months of talks.",
    "Analysts believe the trend will continue.",
    "The proposal was met with mixed reactions.",
    "Several stakeholders were involved in the process.",
    "The committee approved the measure unanimously.",
    "Negotiations are expected to resume this week.",
    "A statement was issued by the press office.",
    "The figures reflect data from the previous year.",
    "The agency confirmed the details on Friday.",
    "Results are expected to be announced soon.",
    "The bill was signed into law last Thursday.",
    "Residents expressed concerns about the project.",
    "The market responded positively to the news.",
]

def _filler(n_tokens: int) -> str:
    """Return roughly n_tokens worth of filler text."""
    words = []
    while len(words) < n_tokens:
        s = random.choice(_FILLER_SENTENCES)
        words.extend(s.split())
    return " ".join(words[:n_tokens])


def make_structural_edits(pairs, seed: int = 42) -> list[dict]:
    """Create structural-edit synthetic test set from MRPC pairs."""
    rng = random.Random(seed)
    edited = []
    # Use first 300 positive pairs for edits
    pos_pairs = [p for p in pairs if p["label"] == 1][:300]

    for p in pos_pairs:
        s1, s2 = p["sentence1"], p["sentence2"]
        pair_id = p["id"]

        # prepend 50 tokens
        filler = _filler(50)
        edited.append({
            "id": f"syn_{pair_id}_prepend50",
            "sentence1": filler + " " + s1,
            "sentence2": filler + " " + s2,
            "label": 1,
            "edit_type": "prepend",
            "original_pair_id": pair_id,
        })

        # append 100 tokens
        filler = _filler(100)
        edited.append({
            "id": f"syn_{pair_id}_append100",
            "sentence1": s1 + " " + filler,
            "sentence2": s2 + " " + filler,
            "label": 1,
            "edit_type": "append",
            "original_pair_id": pair_id,
        })

        # insert mid
        words1 = s1.split()
        mid = len(words1) // 2
        ins = _filler(30)
        edited.append({
            "id": f"syn_{pair_id}_insert",
            "sentence1": " ".join(words1[:mid]) + " " + ins + " " + " ".join(words1[mid:]),
            "sentence2": s2,
            "label": 1,
            "edit_type": "insert",
            "original_pair_id": pair_id,
        })

    # Negative pairs for synthetic set (different originals paired)
    neg_sample = rng.sample(pos_pairs, min(len(pos_pairs), 300))
    for i in range(min(len(neg_sample) - 1, 200)):
        edited.append({
            "id": f"syn_neg_{i}",
            "sentence1": neg_sample[i]["sentence1"],
            "sentence2": neg_sample[i + 1]["sentence2"],
            "label": 0,
            "edit_type": "none",
            "original_pair_id": -1,
        })

    logger.info(f"Generated {len(edited)} synthetic pairs "
                f"(pos={sum(e['label'] for e in edited)}, neg={sum(1-e['label'] for e in edited)})")
    return edited


# ══════════════════════════════════════════════════════════════════════════════
# LANDMARK EXTRACTION
# ══════════════════════════════════════════════════════════════════════════════

def build_tfidf(corpus: list[str]) -> TfidfVectorizer:
    """Fit TF-IDF vectorizer on corpus."""
    vec = TfidfVectorizer(analyzer="word", token_pattern=r"\b\w+\b", lowercase=True,
                          max_features=50000, sublinear_tf=True)
    vec.fit(corpus)
    return vec


def extract_landmarks(text: str, vec: TfidfVectorizer, top_k: int = 15) -> list[tuple[int, str, float]]:
    """
    Return top-k (position, token, tfidf_score) landmarks from text.
    Sliding-window: each token scored by its global IDF × local TF within a 10-word window.
    """
    vocab = vec.vocabulary_
    idf = vec.idf_
    words = text.lower().split()
    if not words:
        return []

    window = 10
    scores = []
    for i, w in enumerate(words):
        if w not in vocab:
            continue
        # local TF in window
        lo, hi = max(0, i - window // 2), min(len(words), i + window // 2 + 1)
        local_count = words[lo:hi].count(w)
        local_tf = 1 + math.log(local_count) if local_count > 0 else 0
        score = local_tf * idf[vocab[w]]
        scores.append((i, w, score))

    if not scores:
        return []

    # Non-maximum suppression: within every 3-position window keep best
    scores.sort(key=lambda x: -x[2])
    selected = []
    covered = set()
    for pos, tok, sc in scores:
        # check if position already covered
        if any(abs(pos - c) < 3 for c in covered):
            continue
        selected.append((pos, tok, sc))
        covered.add(pos)
        if len(selected) >= top_k:
            break

    selected.sort(key=lambda x: x[0])  # sort by position
    return selected


# ══════════════════════════════════════════════════════════════════════════════
# LANDMARK-PAIR FINGERPRINTING
# ══════════════════════════════════════════════════════════════════════════════

DELTA_QUANT = 5  # quantize offset to nearest 5 tokens

def _quantize(delta: int) -> int:
    return (delta + DELTA_QUANT // 2) // DELTA_QUANT * DELTA_QUANT


def compute_fingerprint(landmarks: list, lookahead: int = 20,
                        use_delta: bool = True) -> frozenset[int]:
    """Shazam-inspired: hash pairs of (anchor, target) landmarks within lookahead window."""
    fp = []
    for i, (pos_a, tok_a, _) in enumerate(landmarks):
        for j in range(i + 1, len(landmarks)):
            pos_t, tok_t, _ = landmarks[j]
            if pos_t - pos_a > lookahead:
                break
            delta = _quantize(pos_t - pos_a) if use_delta else 0
            # Deterministic hash using token strings + delta
            key = f"{tok_a}|{tok_t}|{delta}"
            h = int(hashlib.sha256(key.encode()).hexdigest()[:8], 16)
            fp.append(h)
    return frozenset(fp)


def fingerprint_similarity(fp1: frozenset, fp2: frozenset) -> float:
    """Jaccard over fingerprint hash sets."""
    if not fp1 and not fp2:
        return 1.0
    inter = len(fp1 & fp2)
    union = len(fp1 | fp2)
    return inter / union if union else 0.0


# ══════════════════════════════════════════════════════════════════════════════
# MINHASH JACCARD
# ══════════════════════════════════════════════════════════════════════════════

NUM_PERM = 128

def shingle(text: str, k: int = 5) -> set[str]:
    """Character k-shingles."""
    text = text.lower().replace(" ", "_")
    return {text[i:i+k] for i in range(len(text) - k + 1)} if len(text) >= k else {text}


def make_minhash(text: str, num_perm: int = NUM_PERM) -> MinHash:
    m = MinHash(num_perm=num_perm)
    for s in shingle(text):
        m.update(s.encode("utf-8"))
    return m


def minhash_jaccard(m1: MinHash, m2: MinHash) -> float:
    return m1.jaccard(m2)


# ══════════════════════════════════════════════════════════════════════════════
# MINHASH CONTAINMENT
# ══════════════════════════════════════════════════════════════════════════════

def minhash_containment(m1: MinHash, m2: MinHash, size1: int, size2: int) -> float:
    """Estimate containment as min(|A|,|B|)/max(|A|,|B|) × jaccard estimate."""
    j = m1.jaccard(m2)
    if size1 == 0 or size2 == 0:
        return 0.0
    min_sz = min(size1, size2)
    max_sz = max(size1, size2)
    # Containment = |A∩B|/|A| ≈ J × (|A|+|B|) / |A| — use smaller as query
    union_est = max_sz + min_sz - j * (max_sz + min_sz) / (1 + j) if (1 + j) > 0 else max_sz
    inter_est = j * union_est
    return min(inter_est / min_sz, 1.0) if min_sz > 0 else 0.0


# ══════════════════════════════════════════════════════════════════════════════
# SIMHASH
# ══════════════════════════════════════════════════════════════════════════════

_RNG_SIMHASH = np.random.RandomState(1234)
SIMHASH_BITS = 64


def _init_simhash_projections(n_features: int) -> np.ndarray:
    return _RNG_SIMHASH.randn(SIMHASH_BITS, n_features).astype(np.float32)


def compute_simhash(tfidf_vec: np.ndarray, projections: np.ndarray) -> int:
    """Compute 64-bit SimHash from dense TF-IDF vector."""
    dots = projections @ tfidf_vec
    bits = (dots > 0).astype(np.uint8)
    result = 0
    for b in bits:
        result = (result << 1) | int(b)
    return result


def simhash_similarity(h1: int, h2: int) -> float:
    """Normalized hamming similarity (1 - hamming_distance/64)."""
    xor = h1 ^ h2
    hamming = bin(xor).count("1")
    return 1.0 - hamming / SIMHASH_BITS


# ══════════════════════════════════════════════════════════════════════════════
# METRICS
# ══════════════════════════════════════════════════════════════════════════════

def compute_metrics(scores: list[float], labels: list[int]) -> dict:
    """Compute PR curve, AP, F1, recall@prec90."""
    scores_arr = np.array(scores)
    labels_arr = np.array(labels)

    ap = float(average_precision_score(labels_arr, scores_arr))

    prec, rec, thresholds = precision_recall_curve(labels_arr, scores_arr)
    # prec/rec are (n+1,) with last point prec=1,rec=0

    # recall@prec>=0.90
    recall_at_prec90 = 0.0
    threshold_at_prec90 = float(thresholds[-1]) if len(thresholds) else 1.0
    for p, r, t in zip(prec, rec, thresholds):
        if p >= 0.90 and r > recall_at_prec90:
            recall_at_prec90 = float(r)
            threshold_at_prec90 = float(t)

    # F1 optimal
    f1_vals = 2 * prec[:-1] * rec[:-1] / (prec[:-1] + rec[:-1] + 1e-10)
    best_f1_idx = int(np.argmax(f1_vals))
    f1_optimal = float(f1_vals[best_f1_idx])
    threshold_f1 = float(thresholds[best_f1_idx]) if best_f1_idx < len(thresholds) else 1.0

    # PR curve as list of [threshold, precision, recall]
    pr_curve = []
    step = max(1, len(thresholds) // 50)
    for i in range(0, len(thresholds), step):
        pr_curve.append([round(float(thresholds[i]), 4),
                         round(float(prec[i]), 4),
                         round(float(rec[i]), 4)])

    return {
        "auc_pr": round(ap, 4),
        "recall_at_prec90": round(recall_at_prec90, 4),
        "threshold_at_prec90": round(threshold_at_prec90, 4),
        "f1_optimal": round(f1_optimal, 4),
        "threshold_at_f1_optimal": round(threshold_f1, 4),
        "precision_recall_curve": pr_curve,
    }


# ══════════════════════════════════════════════════════════════════════════════
# MAIN PIPELINE
# ══════════════════════════════════════════════════════════════════════════════

def process_pairs(pairs: list[dict], vec: TfidfVectorizer,
                  projections: np.ndarray, top_k: int = 15,
                  lookahead: int = 20) -> dict:
    """
    Run all 4 methods on a list of pairs. Returns scores per method.
    """
    n = len(pairs)
    lm_scores = []
    lm_no_delta_scores = []
    mhj_scores = []
    mhc_scores = []
    sh_scores = []

    # Build TF-IDF sparse matrix for SimHash
    all_texts = []
    for p in pairs:
        all_texts.append(p["sentence1"])
        all_texts.append(p["sentence2"])

    logger.info(f"  Transforming {len(all_texts)} texts for TF-IDF/SimHash")
    tfidf_matrix = vec.transform(all_texts)

    logger.info(f"  Computing fingerprints for {n} pairs")
    for i, p in enumerate(pairs):
        if i % 500 == 0:
            logger.info(f"    pair {i}/{n}")

        s1 = p["sentence1"]
        s2 = p["sentence2"]
        idx1 = 2 * i
        idx2 = 2 * i + 1

        # Landmark-pair
        lm1 = extract_landmarks(s1, vec, top_k=top_k)
        lm2 = extract_landmarks(s2, vec, top_k=top_k)
        fp1 = compute_fingerprint(lm1, lookahead=lookahead, use_delta=True)
        fp2 = compute_fingerprint(lm2, lookahead=lookahead, use_delta=True)
        fp1_nd = compute_fingerprint(lm1, lookahead=lookahead, use_delta=False)
        fp2_nd = compute_fingerprint(lm2, lookahead=lookahead, use_delta=False)

        lm_scores.append(fingerprint_similarity(fp1, fp2))
        lm_no_delta_scores.append(fingerprint_similarity(fp1_nd, fp2_nd))

        # MinHash
        mh1 = make_minhash(s1)
        mh2 = make_minhash(s2)
        mhj_scores.append(minhash_jaccard(mh1, mh2))
        sh1 = shingle(s1)
        sh2 = shingle(s2)
        mhc_scores.append(minhash_containment(mh1, mh2, len(sh1), len(sh2)))

        # SimHash
        v1 = tfidf_matrix[idx1].toarray()[0].astype(np.float32)
        v2 = tfidf_matrix[idx2].toarray()[0].astype(np.float32)
        norm1, norm2 = np.linalg.norm(v1), np.linalg.norm(v2)
        if norm1 > 0: v1 /= norm1
        if norm2 > 0: v2 /= norm2
        h1 = compute_simhash(v1, projections)
        h2 = compute_simhash(v2, projections)
        sh_scores.append(simhash_similarity(h1, h2))

    labels = [p["label"] for p in pairs]
    return {
        "landmark_pair": lm_scores,
        "landmark_pair_no_delta": lm_no_delta_scores,
        "minhash_jaccard": mhj_scores,
        "minhash_containment": mhc_scores,
        "simhash": sh_scores,
        "labels": labels,
    }


def run_ablation_k(pairs: list[dict], vec: TfidfVectorizer, k_values: list[int]) -> dict:
    """Ablation: vary landmark density K."""
    results = {}
    for k in k_values:
        logger.info(f"  Ablation K={k}")
        lm_scores = []
        labels = [p["label"] for p in pairs]
        for p in pairs:
            lm1 = extract_landmarks(p["sentence1"], vec, top_k=k)
            lm2 = extract_landmarks(p["sentence2"], vec, top_k=k)
            fp1 = compute_fingerprint(lm1, lookahead=20, use_delta=True)
            fp2 = compute_fingerprint(lm2, lookahead=20, use_delta=True)
            lm_scores.append(fingerprint_similarity(fp1, fp2))
        m = compute_metrics(lm_scores, labels)
        avg_lm = sum(len(extract_landmarks(p["sentence1"], vec, top_k=k)) for p in pairs[:50]) / 50
        results[f"k={k}"] = {
            "recall_at_prec90": m["recall_at_prec90"],
            "auc_pr": m["auc_pr"],
            "avg_landmarks_per_passage": round(avg_lm, 1),
        }
    return results


def run_ablation_w(pairs: list[dict], vec: TfidfVectorizer, w_values: list[int]) -> dict:
    """Ablation: vary lookahead window W."""
    results = {}
    labels = [p["label"] for p in pairs]
    for w in w_values:
        logger.info(f"  Ablation W={w}")
        lm_scores = []
        fp_sizes = []
        for p in pairs:
            lm1 = extract_landmarks(p["sentence1"], vec, top_k=15)
            lm2 = extract_landmarks(p["sentence2"], vec, top_k=15)
            fp1 = compute_fingerprint(lm1, lookahead=w, use_delta=True)
            fp2 = compute_fingerprint(lm2, lookahead=w, use_delta=True)
            lm_scores.append(fingerprint_similarity(fp1, fp2))
            fp_sizes.append((len(fp1) + len(fp2)) / 2)
        m = compute_metrics(lm_scores, labels)
        results[f"w={w}"] = {
            "recall_at_prec90": m["recall_at_prec90"],
            "auc_pr": m["auc_pr"],
            "avg_fp_size": round(sum(fp_sizes) / len(fp_sizes), 1) if fp_sizes else 0,
        }
    return results


def two_prop_z_test(p1: float, p2: float, n1: int, n2: int) -> tuple[float, float, list[float]]:
    """Two-proportion z-test for significance of delta in ablation."""
    p_pool = (p1 * n1 + p2 * n2) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2)) if p_pool * (1 - p_pool) > 0 else 1e-10
    z = (p1 - p2) / se
    p_val = 2 * (1 - scipy_norm.cdf(abs(z)))
    diff = p1 - p2
    se_diff = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    ci = [round(diff - 1.96 * se_diff, 4), round(diff + 1.96 * se_diff, 4)]
    return round(z, 4), round(p_val, 4), ci


def timing_benchmark(vec: TfidfVectorizer, projections: np.ndarray, n_corpus: int = 10000) -> dict:
    """Benchmark indexing and query latency on synthetic corpus."""
    logger.info(f"Timing benchmark on {n_corpus} synthetic passages")
    rng = random.Random(99)
    # Generate synthetic passages
    passages = [" ".join(rng.choices([w for w in vec.vocabulary_], k=50)) for _ in range(n_corpus)]

    methods_timing = {}

    # Landmark-pair indexing
    t0 = time.perf_counter()
    lm_index = []
    for txt in passages[:n_corpus]:
        lm = extract_landmarks(txt, vec, top_k=15)
        fp = compute_fingerprint(lm, lookahead=20, use_delta=True)
        lm_index.append(fp)
    lm_index_time = time.perf_counter() - t0

    # Query latency for landmark-pair
    q_passages = passages[:100]
    t0 = time.perf_counter()
    for txt in q_passages:
        lm = extract_landmarks(txt, vec, top_k=15)
        fp = compute_fingerprint(lm, lookahead=20, use_delta=True)
        _ = [fingerprint_similarity(fp, fp2) for fp2 in lm_index[:1000]]
    lm_query_time = (time.perf_counter() - t0) / len(q_passages) * 1000  # ms

    methods_timing["landmark_pair"] = {
        "indexing_time_seconds": round(lm_index_time, 2),
        "corpus_size": n_corpus,
        "median_query_latency_ms": round(lm_query_time, 2),
    }
    del lm_index; gc.collect()

    # MinHash Jaccard indexing
    t0 = time.perf_counter()
    mh_index = [make_minhash(txt) for txt in passages[:n_corpus]]
    mhj_index_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    for txt in q_passages:
        mq = make_minhash(txt)
        _ = [minhash_jaccard(mq, m) for m in mh_index[:1000]]
    mhj_query_time = (time.perf_counter() - t0) / len(q_passages) * 1000

    methods_timing["minhash_jaccard"] = {
        "indexing_time_seconds": round(mhj_index_time, 2),
        "corpus_size": n_corpus,
        "median_query_latency_ms": round(mhj_query_time, 2),
    }

    # SimHash indexing
    tfidf_sparse = vec.transform(passages[:n_corpus])
    t0 = time.perf_counter()
    sh_index = []
    for i in range(n_corpus):
        v = tfidf_sparse[i].toarray()[0].astype(np.float32)
        norm = np.linalg.norm(v)
        if norm > 0: v /= norm
        sh_index.append(compute_simhash(v, projections))
    sh_index_time = time.perf_counter() - t0

    tfidf_q = vec.transform(q_passages)
    t0 = time.perf_counter()
    for i in range(len(q_passages)):
        v = tfidf_q[i].toarray()[0].astype(np.float32)
        norm = np.linalg.norm(v)
        if norm > 0: v /= norm
        h = compute_simhash(v, projections)
        _ = [simhash_similarity(h, h2) for h2 in sh_index[:1000]]
    sh_query_time = (time.perf_counter() - t0) / len(q_passages) * 1000

    methods_timing["simhash"] = {
        "indexing_time_seconds": round(sh_index_time, 2),
        "corpus_size": n_corpus,
        "median_query_latency_ms": round(sh_query_time, 2),
    }
    del mh_index, sh_index; gc.collect()

    return methods_timing


@logger.catch(reraise=True)
def main():
    t_start = time.perf_counter()

    # ── LOAD DATA ────────────────────────────────────────────────────────────
    pairs = load_mrpc(DATA_PATH)
    synthetic_pairs = make_structural_edits(pairs)

    # ── BUILD TF-IDF CORPUS ─────────────────────────────────────────────────
    logger.info("Building TF-IDF corpus")
    all_texts = [p["sentence1"] for p in pairs] + [p["sentence2"] for p in pairs]
    vec = build_tfidf(all_texts)
    n_features = len(vec.vocabulary_)
    logger.info(f"Vocab size: {n_features}")

    # SimHash projections
    projections = _init_simhash_projections(n_features)

    # ── MRPC MAIN EVAL ──────────────────────────────────────────────────────
    logger.info("Processing MRPC pairs")
    mrpc_scores = process_pairs(pairs, vec, projections, top_k=15, lookahead=20)

    mrpc_labels = mrpc_scores["labels"]
    mrpc_results = {}
    for method in ["landmark_pair", "landmark_pair_no_delta", "minhash_jaccard", "minhash_containment", "simhash"]:
        logger.info(f"  Computing metrics for {method}")
        mrpc_results[method] = compute_metrics(mrpc_scores[method], mrpc_labels)

    # ── SYNTHETIC EVAL ──────────────────────────────────────────────────────
    logger.info("Processing Synthetic pairs")
    syn_scores = process_pairs(synthetic_pairs, vec, projections, top_k=15, lookahead=20)

    syn_labels = syn_scores["labels"]
    syn_results = {}
    for method in ["landmark_pair", "landmark_pair_no_delta", "minhash_jaccard", "minhash_containment", "simhash"]:
        syn_results[method] = compute_metrics(syn_scores[method], syn_labels)

    # ── ABLATIONS ───────────────────────────────────────────────────────────
    # Use a subset of 500 MRPC pairs for ablations to save time
    ablation_pairs = pairs[:500]

    logger.info("Ablation: landmark density (K)")
    abl_k = run_ablation_k(ablation_pairs, vec, k_values=[5, 10, 15, 20, 30])

    logger.info("Ablation: lookahead window (W)")
    abl_w = run_ablation_w(ablation_pairs, vec, w_values=[10, 20, 50, 100])

    # Positional offset significance test
    lm_with = mrpc_results["landmark_pair"]["recall_at_prec90"]
    lm_no = mrpc_results["landmark_pair_no_delta"]["recall_at_prec90"]
    n_pos = sum(mrpc_labels)
    z, p_val, ci = two_prop_z_test(lm_with, lm_no, n_pos, n_pos)
    logger.info(f"Positional offset z={z}, p={p_val}")
    offset_verdict = "SIGNIFICANT" if p_val < 0.05 else "NOT_SIGNIFICANT"

    # ── TIMING ──────────────────────────────────────────────────────────────
    logger.info("Timing benchmark")
    timing = timing_benchmark(vec, projections, n_corpus=5000)

    # ── BUILD EXAMPLES LIST (exp_gen_sol_out schema) ─────────────────────────
    logger.info("Building output JSON")

    mrpc_examples = []
    for i, p in enumerate(pairs):
        ex = dict(p["raw"])
        ex["predict_landmark_pair"] = str(round(mrpc_scores["landmark_pair"][i], 4))
        ex["predict_minhash_jaccard"] = str(round(mrpc_scores["minhash_jaccard"][i], 4))
        ex["predict_minhash_containment"] = str(round(mrpc_scores["minhash_containment"][i], 4))
        ex["predict_simhash"] = str(round(mrpc_scores["simhash"][i], 4))
        ex["predict_landmark_pair_no_delta"] = str(round(mrpc_scores["landmark_pair_no_delta"][i], 4))
        mrpc_examples.append(ex)

    syn_examples = []
    for i, sp in enumerate(synthetic_pairs):
        ex = {
            "input": json.dumps({"sentence1": sp["sentence1"], "sentence2": sp["sentence2"]}),
            "output": str(sp["label"]),
            "metadata_edit_type": sp["edit_type"],
            "metadata_original_pair_id": str(sp["original_pair_id"]),
            "metadata_label_meaning": "1=paraphrase(near-duplicate) 0=non-paraphrase",
            "metadata_source": "synthetic_structural_edits",
            "predict_landmark_pair": str(round(syn_scores["landmark_pair"][i], 4)),
            "predict_minhash_jaccard": str(round(syn_scores["minhash_jaccard"][i], 4)),
            "predict_minhash_containment": str(round(syn_scores["minhash_containment"][i], 4)),
            "predict_simhash": str(round(syn_scores["simhash"][i], 4)),
            "predict_landmark_pair_no_delta": str(round(syn_scores["landmark_pair_no_delta"][i], 4)),
        }
        syn_examples.append(ex)

    # Key findings
    lm_mrpc = mrpc_results["landmark_pair"]["recall_at_prec90"]
    cont_mrpc = mrpc_results["minhash_containment"]["recall_at_prec90"]
    lm_syn = syn_results["landmark_pair"]["recall_at_prec90"]
    cont_syn = syn_results["minhash_containment"]["recall_at_prec90"]

    lm_beats = lm_syn > cont_syn + 0.05
    delta_pp = round((lm_syn - cont_syn) * 100, 2)

    if lm_syn >= cont_syn + 0.10 and offset_verdict == "SIGNIFICANT":
        verdict = "CONFIRM"
    elif lm_syn >= cont_syn - 0.02:
        verdict = "PARTIAL"
    else:
        verdict = "DISCONFIRM"

    best_k = max(abl_k.items(), key=lambda x: x[1]["recall_at_prec90"])[0]
    best_w = max(abl_w.items(), key=lambda x: x[1]["recall_at_prec90"])[0]

    elapsed = round(time.perf_counter() - t_start, 1)
    logger.info(f"Total elapsed: {elapsed}s")

    output = {
        "metadata": {
            "objective": "Benchmark landmark-pair fingerprinting vs MinHash/SimHash for near-duplicate detection",
            "elapsed_seconds": elapsed,
            "num_cpus": NUM_CPUS,
            "datasets_evaluated": ["GLUE_MRPC", "Synthetic_Structural_Edits"],
            "mrpc_results": {
                "num_pairs": len(pairs),
                "num_positive": sum(mrpc_labels),
                "num_negative": len(mrpc_labels) - sum(mrpc_labels),
                "landmark_pair": mrpc_results["landmark_pair"],
                "minhash_jaccard": mrpc_results["minhash_jaccard"],
                "minhash_containment": mrpc_results["minhash_containment"],
                "simhash": mrpc_results["simhash"],
                "landmark_pair_no_delta": mrpc_results["landmark_pair_no_delta"],
            },
            "synthetic_results": {
                "num_pairs": len(synthetic_pairs),
                "num_positive": sum(syn_labels),
                "num_negative": len(syn_labels) - sum(syn_labels),
                "edit_types": ["prepend", "append", "insert", "none"],
                "landmark_pair": syn_results["landmark_pair"],
                "minhash_jaccard": syn_results["minhash_jaccard"],
                "minhash_containment": syn_results["minhash_containment"],
                "simhash": syn_results["simhash"],
                "landmark_pair_no_delta": syn_results["landmark_pair_no_delta"],
            },
            "ablations": {
                "positional_offset": {
                    "with_delta_recall_prec90": lm_with,
                    "without_delta_recall_prec90": lm_no,
                    "z_statistic": z,
                    "p_value": p_val,
                    "ci_95_difference": ci,
                    "verdict": offset_verdict,
                },
                "landmark_density": {"by_k": abl_k},
                "lookahead_window": {"by_w": abl_w},
            },
            "timing": timing,
            "implementation_details": {
                "landmark_extraction": {
                    "method": "Sliding-window TF-IDF local scoring + non-maximum suppression",
                    "window_size": 10,
                    "nms_radius": 3,
                    "default_top_k": 15,
                },
                "landmark_pair_hashing": {
                    "hash_function": "SHA-256 truncated to 32 bits",
                    "default_lookahead_window": 20,
                    "delta_quantization": f"nearest {DELTA_QUANT} tokens",
                },
                "baselines": {
                    "minhash_jaccard": {"library": "datasketch", "num_perm": NUM_PERM, "shingle_size": 5},
                    "minhash_containment": {"library": "datasketch", "num_perm": NUM_PERM},
                    "simhash": {"bits": SIMHASH_BITS, "vectorizer": "sklearn TfidfVectorizer"},
                },
            },
            "key_findings": {
                "landmark_pair_beats_containment_synthetic": lm_beats,
                "recall_delta_vs_containment_pp_synthetic": delta_pp,
                "positional_offset_is_load_bearing": offset_verdict == "SIGNIFICANT",
                "best_landmark_density_k": best_k,
                "best_lookahead_window_w": best_w,
                "verdict": verdict,
                "mrpc_landmark_pair_recall_at_prec90": lm_mrpc,
                "mrpc_minhash_containment_recall_at_prec90": cont_mrpc,
                "synthetic_landmark_pair_recall_at_prec90": lm_syn,
                "synthetic_minhash_containment_recall_at_prec90": cont_syn,
            },
        },
        "datasets": [
            {
                "dataset": "glue_mrpc",
                "examples": mrpc_examples,
            },
            {
                "dataset": "synthetic_structural_edits",
                "examples": syn_examples,
            },
        ],
    }

    out_path = WS / "method_out.json"
    out_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Wrote {out_path} ({out_path.stat().st_size / 1e6:.1f} MB)")

    # Print summary
    logger.info("=" * 60)
    logger.info("RESULTS SUMMARY")
    logger.info(f"MRPC: landmark_pair recall@prec90={lm_mrpc:.3f}  containment={cont_mrpc:.3f}")
    logger.info(f"Synthetic: landmark_pair recall@prec90={lm_syn:.3f}  containment={cont_syn:.3f}")
    logger.info(f"Positional offset: z={z} p={p_val} → {offset_verdict}")
    logger.info(f"Best K={best_k}, Best W={best_w}")
    logger.info(f"VERDICT: {verdict}")
    logger.info("=" * 60)

    return output


if __name__ == "__main__":
    main()
