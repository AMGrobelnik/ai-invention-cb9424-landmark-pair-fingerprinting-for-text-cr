#!/usr/bin/env python3
"""
Build near-duplicate detection benchmark from:
  1) Wikipedia (synthetic structural edits: insertion, deletion, embedding, reorder, control + negatives)
  2) Quora Duplicate Questions (real-world labeled pairs)
Outputs: full_data_out.json conforming to exp_sel_data_out.json schema.
"""

from loguru import logger
from pathlib import Path
import json
import sys
import random

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

WORKSPACE = Path("/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_art/gen_art_dataset_1")
DATASETS_DIR = WORKSPACE / "temp" / "datasets"
OUTPUT = WORKSPACE / "full_data_out.json"

WIKI_PATH = DATASETS_DIR / "wikipedia_en_5000.json"
QUORA_PATH = DATASETS_DIR / "full_sentence-transformers_quora-duplicates_pair-class_train.json"

random.seed(42)

MAX_WORDS = 400  # Truncate texts to this many words to keep file size ≤100MB

# ── helpers ──────────────────────────────────────────────────────────────────

def jaccard(a: str, b: str) -> float:
    sa = set(a.lower().split())
    sb = set(b.lower().split())
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / len(sa | sb)


def split_paragraphs(text: str) -> list[str]:
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paras


def clean_wiki(text: str) -> str:
    """Basic Wikipedia text cleaning: strip references sections, truncate to MAX_WORDS."""
    lines = []
    in_refs = False
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped.lower().startswith("== references") or stripped.lower().startswith("== see also"):
            in_refs = True
        if in_refs:
            continue
        lines.append(line)
    cleaned = "\n".join(lines).strip()
    # Truncate to MAX_WORDS
    words = cleaned.split()
    if len(words) > MAX_WORDS:
        cleaned = " ".join(words[:MAX_WORDS])
    return cleaned


# ── boilerplate corpus (built from Wikipedia snippets) ──────────────────────

def build_boilerplate_corpus(articles: list[dict], n: int = 300) -> list[str]:
    """Extract short snippets (100-250 words) from article intros to use as boilerplate."""
    snippets = []
    for art in articles[:n]:
        text = art["text"]
        paras = split_paragraphs(text)
        if paras:
            words = paras[0].split()
            if 40 <= len(words) <= 100:
                snippets.append(paras[0])
            elif len(words) > 100:
                snippets.append(" ".join(words[:80]))
    logger.info(f"Built boilerplate corpus: {len(snippets)} snippets")
    return snippets


# ── edit generators ─────────────────────────────────────────────────────────

def edit_insertion(text: str, boilerplate: list[str]) -> str:
    bp = random.choice(boilerplate)
    return bp + "\n\n" + text


def edit_deletion(text: str) -> str | None:
    paras = split_paragraphs(text)
    if len(paras) < 3:
        return None
    mid_start = max(1, len(paras) // 4)
    mid_end = min(len(paras) - 1, 3 * len(paras) // 4)
    n_del = random.randint(1, max(1, (mid_end - mid_start)))
    start_del = random.randint(mid_start, max(mid_start, mid_end - n_del))
    kept = paras[:start_del] + paras[start_del + n_del:]
    if not kept:
        return None
    return "\n\n".join(kept)


def edit_embedding(text: str, boilerplate: list[str]) -> str:
    bp1 = random.choice(boilerplate)
    bp2 = random.choice(boilerplate)
    return bp1 + "\n\n" + text + "\n\n" + bp2


def edit_reorder(text: str) -> str | None:
    paras = split_paragraphs(text)
    if len(paras) < 4:
        return None
    # Swap two random adjacent pairs in the middle
    mid = len(paras) // 2
    if mid < 1:
        return None
    i = random.randint(1, len(paras) - 2)
    paras[i], paras[i + 1] = paras[i + 1], paras[i]
    return "\n\n".join(paras)


def edit_control(text: str) -> str:
    return text


# ── Wikipedia synthetic dataset ──────────────────────────────────────────────

def build_wiki_examples(articles: list[dict], boilerplate: list[str]) -> list[dict]:
    examples = []
    source_count = 0

    # Use first 2000 articles as source passages (with enough words)
    sources = [a for a in articles if a.get("word_count", 0) >= 300][:2000]
    # Remaining articles as negative pool
    neg_pool = [a for a in articles if a.get("word_count", 0) >= 200]
    logger.info(f"Source passages: {len(sources)}, Negative pool: {len(neg_pool)}")

    EDITS = ["insertion", "deletion", "embedding", "reorder", "control"]
    NEGS_PER_SOURCE = 5  # 5 negatives per source → 10K + 10K = 20K total

    for idx, art in enumerate(sources):
        pid = f"wiki-{art['id']}"
        orig = clean_wiki(art["text"])
        orig_words = len(orig.split())

        # 1. Positive variants
        edit_funcs = {
            "insertion": lambda t: edit_insertion(t, boilerplate),
            "deletion": edit_deletion,
            "embedding": lambda t: edit_embedding(t, boilerplate),
            "reorder": edit_reorder,
            "control": edit_control,
        }

        for etype in EDITS:
            variant = edit_funcs[etype](orig)
            if variant is None:
                # fallback: use control
                variant = orig
                actual_etype = "control"
            else:
                actual_etype = etype

            var_words = len(variant.split())
            jac = jaccard(orig, variant)

            ex = {
                "input": json.dumps({
                    "passage_id": pid,
                    "original_text": orig,
                    "variant_text": variant,
                }, ensure_ascii=False),
                "output": "true",
                "metadata_edit_type": actual_etype,
                "metadata_source": "wikipedia-synthetic",
                "metadata_domain": "encyclopedia",
                "metadata_passage_id": pid,
                "metadata_original_length_words": orig_words,
                "metadata_variant_length_words": var_words,
                "metadata_edit_distance_jaccard": round(jac, 4),
                "metadata_is_near_duplicate": "true",
            }
            examples.append(ex)

        # 2. Negative pairs (random unrelated passages)
        neg_candidates = [
            a for a in neg_pool
            if a["id"] != art["id"]
        ]
        neg_sample = random.sample(neg_candidates, min(NEGS_PER_SOURCE, len(neg_candidates)))

        for neg_art in neg_sample:
            neg_text = clean_wiki(neg_art["text"])
            neg_words = len(neg_text.split())
            jac = jaccard(orig, neg_text)
            ex = {
                "input": json.dumps({
                    "passage_id": pid,
                    "original_text": orig,
                    "variant_text": neg_text,
                }, ensure_ascii=False),
                "output": "false",
                "metadata_edit_type": "negative",
                "metadata_source": "wikipedia-synthetic",
                "metadata_domain": "encyclopedia",
                "metadata_passage_id": pid,
                "metadata_original_length_words": orig_words,
                "metadata_variant_length_words": neg_words,
                "metadata_edit_distance_jaccard": round(jac, 4),
                "metadata_is_near_duplicate": "false",
            }
            examples.append(ex)

        source_count += 1
        if source_count % 200 == 0:
            logger.info(f"Processed {source_count}/{len(sources)} source passages → {len(examples)} examples so far")

    logger.info(f"Wikipedia dataset: {len(examples)} examples from {source_count} sources")
    return examples


# ── Quora duplicate questions dataset ────────────────────────────────────────

def build_quora_examples(quora_path: Path, max_rows: int = 10000) -> list[dict]:
    data = json.loads(quora_path.read_text())
    examples = []

    rows = data if isinstance(data, list) else data.get("examples", data)
    rows = rows[:max_rows]

    for row in rows:
        s1 = row.get("sentence1", "")
        s2 = row.get("sentence2", "")
        label = row.get("label", 0)
        is_dup = bool(label == 1)

        if not s1 or not s2:
            continue

        jac = jaccard(s1, s2)
        ex = {
            "input": json.dumps({
                "sentence1": s1,
                "sentence2": s2,
            }, ensure_ascii=False),
            "output": "true" if is_dup else "false",
            "metadata_edit_type": "paraphrase" if is_dup else "negative",
            "metadata_source": "quora-duplicates",
            "metadata_domain": "questions",
            "metadata_original_length_words": len(s1.split()),
            "metadata_variant_length_words": len(s2.split()),
            "metadata_edit_distance_jaccard": round(jac, 4),
            "metadata_is_near_duplicate": "true" if is_dup else "false",
            "metadata_quora_label": label,
        }
        examples.append(ex)

    logger.info(f"Quora dataset: {len(examples)} examples (dup={sum(1 for e in examples if e['output']=='true')})")
    return examples


# ── main ─────────────────────────────────────────────────────────────────────

@logger.catch(reraise=True)
def main():
    Path("logs").mkdir(exist_ok=True)

    logger.info("Loading Wikipedia articles...")
    articles = json.loads(WIKI_PATH.read_text())
    logger.info(f"Loaded {len(articles)} Wikipedia articles")

    logger.info("Building boilerplate corpus...")
    boilerplate = build_boilerplate_corpus(articles, n=500)

    logger.info("Generating Wikipedia synthetic examples...")
    wiki_examples = build_wiki_examples(articles, boilerplate)

    logger.info("Loading Quora duplicates...")
    quora_examples = build_quora_examples(QUORA_PATH, max_rows=10000)

    out = {
        "metadata": {
            "description": "Near-duplicate text passage detection benchmark",
            "sources": ["wikipedia-synthetic", "quora-duplicates"],
            "edit_types": ["insertion", "deletion", "embedding", "reorder", "control", "paraphrase", "negative"],
            "schema_fields": {
                "input": "JSON string with original_text and variant_text (or sentence1/sentence2)",
                "output": "'true' if near-duplicate, 'false' otherwise",
                "metadata_edit_type": "type of structural edit applied",
                "metadata_edit_distance_jaccard": "token-level Jaccard similarity between texts",
            }
        },
        "datasets": [
            {
                "dataset": "wikipedia-synthetic",
                "examples": wiki_examples,
            },
            {
                "dataset": "quora-duplicates",
                "examples": quora_examples,
            }
        ]
    }

    OUTPUT.write_text(json.dumps(out, ensure_ascii=False))
    size_mb = OUTPUT.stat().st_size / 1e6
    logger.info(f"Saved full_data_out.json: {size_mb:.1f} MB")
    logger.info(f"  Wikipedia: {len(wiki_examples)} examples")
    logger.info(f"  Quora:     {len(quora_examples)} examples")
    logger.info(f"  Total:     {len(wiki_examples) + len(quora_examples)} examples")


if __name__ == "__main__":
    main()
