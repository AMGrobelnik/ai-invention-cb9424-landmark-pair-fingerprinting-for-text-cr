# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_Bd0c_4hy9OC-` — Near Duplicate Detection
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-03 18:50:15 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Landmark-Pair Text Fingerprinting Beyond Containment MinHash
hypothesis: >-
  Near-duplicate text passages can be detected more robustly than both standard Jaccard MinHash AND MinHash Containment (|A∩B|/|A|,
  the well-known fix for document-length sensitivity) by fingerprinting pairs of locally-salient n-gram landmarks together
  with their relative positional offset — directly analogous to how Shazam identifies audio by hashing (anchor-frequency,
  target-frequency, time-delta) pairs. The hypothesis is: a fingerprint built from (ngram_A, ngram_B, position_delta) hashes,
  where ngram_A and ngram_B are locally-maximal TF-IDF n-grams within the passage, will achieve higher recall than MinHash
  Containment at equivalent precision ≥0.90 on near-duplicates involving paragraph-scale reordering or partial-overlap embedding
  — because containment MinHash is still sensitive to within-document reorderings that alter shingle co-occurrence, while
  the relative distance between co-occurring salient n-grams is preserved under structural edits even when absolute positions
  shift. The improvement over containment MinHash is expected to be modest (5-15pp) rather than the 33-39pp claimed over Jaccard
  MinHash (which was an unfair comparison), and the contribution is most clearly demonstrated on paragraph-reorder and partial-overlap
  cases that neither Jaccard nor containment MinHash handles well.
motivation: >-
  MinHash, the dominant scalable near-duplicate detector, estimates global Jaccard overlap of k-gram shingles. This works
  well for near-exact copies but degrades when passages are embedded in larger documents, have surrounding boilerplate added,
  or have paragraphs inserted/removed — because every added token dilutes the Jaccard score. These structural near-duplicates
  are common in web crawls (article syndication), legal corpora (contract reuse), and LLM pretraining data (dataset contamination).
  A fingerprint mechanism borrowed from audio recognition that is inherently local and position-offset-aware would fill this
  gap without requiring neural embeddings or increased compute.
assumptions:
- >-
  Text passages contain at least a handful of locally-distinctive n-grams (high local TF-IDF) that survive minor edits and
  serve as stable landmarks.
- >-
  The relative positional distance between co-occurring salient n-grams within a passage is approximately preserved under
  the structural edits (insertion/deletion) that MinHash handles poorly.
- >-
  A sparse set of landmark pairs (O(k^2) per document for k landmarks) is sufficient to discriminate near-duplicate from unrelated
  passages, similar to Shazam needing only a few dozen landmark pairs per audio snippet.
- >-
  An inverted index over landmark-pair hashes enables sub-linear candidate retrieval, maintaining scalability comparable to
  MinHash LSH.
investigation_approach: >-
  1. LANDMARK EXTRACTION: For each passage, compute sliding-window TF-IDF scores for all k-grams (k=5..8 characters or words).
  Find local maxima in the resulting position×n-gram saliency surface using scipy.ndimage.maximum_filter, yielding a sparse
  set of (position, n-gram) landmark pairs. 2. FINGERPRINT GENERATION: For each anchor landmark (p1, g1), enumerate all target
  landmarks (p2, g2) within a lookahead window W. Emit hash(g1, g2, p2-p1) as a fingerprint hash. The full fingerprint is
  the set of all such hashes. 3. INVERTED INDEX: Build an inverted index mapping each hash to the passages that contain it.
  Two passages are candidate near-duplicates if they share >= T hashes. 4. BENCHMARK: Evaluate on (a) the PAN-PC-11 plagiarism
  corpus with copy, paraphrase, and simulated-paraphrase cases; (b) a synthetic corpus where 500 Wikipedia passages are each
  embedded in 5 variants with prepended/appended/inserted text of varying lengths. Compare precision-recall curves against
  MinHash (with varying band/row settings) and SimHash. 5. ABLATIONS: Test with/without positional offset in the hash (to
  isolate whether the offset is the key ingredient vs. simple co-occurrence), and vary landmark density k and window W.
success_criteria: >-
  CONFIRM: Landmark-pair fingerprinting achieves at least 10 percentage points higher recall than MinHash at precision >=
  0.90 on the structural-edit near-duplicate benchmark (passages with surrounding text added). The positional-offset ablation
  (removing delta from the hash) shows a statistically significant drop in precision (demonstrating the offset is load-bearing,
  not just co-occurrence). DISCONFIRM: If landmark-pair fingerprinting recall is within 5pp of MinHash on structural edits,
  or if the inverted-index lookup time is >10x slower than MinHash at equal candidate set size, the hypothesis is refuted.
  PARTIAL: Higher recall only on insertion/deletion cases but not paraphrases would suggest the mechanism is complementary
  to MinHash rather than superior.
related_works:
- >-
  Winnowing (Schleimer et al., SIGMOD 2003): Selects a subset of k-gram hashes using a sliding-window minimum, guaranteeing
  at least one fingerprint in every window of length w. Key difference: selects INDIVIDUAL hash landmarks — no pairing, no
  positional offset between pairs. The new method hashes PAIRS of landmarks with their relative offset, creating a 2D structural
  code instead of a 1D sequence of isolated hashes.
- >-
  MinHash / LSH (Broder 1997, Manku et al. WWW 2007): Estimates Jaccard similarity of k-gram shingle sets via random hash
  minima. Key difference: global statistic over the full shingle set — sensitive to any change in document length or added
  text. Landmark-pair hashing is purely local and translation-invariant within the passage.
- >-
  SimHash (Charikar 2002, used by Google for web dedup): Projects TF-IDF vector onto random hyperplanes, producing a bit-vector.
  Hamming distance in bit-vector space approximates cosine similarity. Key difference: a single dense vector captures the
  full document — there is no notion of local structural relationship between salient positions. Landmark pairs encode WHERE
  two salient n-grams co-occur relative to each other.
- >-
  RETSim (Zhang et al. 2023): Lightweight deep learning model trained to produce metric embeddings robust to character-level
  edits. Key difference: neural model requiring training data and inference compute. The landmark-pair method is training-free
  and purely symbolic, requiring no neural forward pass.
- >-
  Audio fingerprinting / Shazam (Wang 2003): The DIRECT inspiration — hashes (anchor-freq, target-freq, time-delta) pairs
  of spectral peaks. Has never been applied to text; the text domain requires rethinking 'frequency' (n-gram identity under
  TF-IDF) and 'time' (character/word position), and the saliency measure (audio energy vs. local TF-IDF).
inspiration: >-
  Directly inspired by Shazam's audio fingerprinting algorithm (Wang 2003), which identifies a 10-second audio snippet in
  a million-song database in under a second. Shazam's key insight — hash PAIRS of local spectral landmarks with their relative
  TIME OFFSET rather than individual landmarks or global statistics — makes the fingerprint invariant to absolute temporal
  position and robust to noise. This is a Level-3 (methodological) cross-domain transfer: the mechanism applies nearly as-is
  to text by substituting (audio-frequency, energy) with (n-gram-type, TF-IDF) and time with character position. The insight
  that 'structural near-duplicates preserve relative landmark distances even when absolute positions shift' is the direct
  textual analog of 'a noisy excerpt preserves spectral peak relationships even when played at a different time.'
terms:
- term: Landmark
  definition: >-
    A (position, n-gram) pair that is a local maximum of TF-IDF saliency within a sliding window over the text — the most
    informationally distinctive n-gram in its local neighborhood, analogous to a spectral peak in Shazam.
- term: Landmark pair hash
  definition: >-
    A hash of three values: (n-gram of anchor landmark, n-gram of target landmark, position_target - position_anchor). Encodes
    the structural relationship between two salient text features at a fixed relative distance.
- term: Structural near-duplicate
  definition: >-
    A near-duplicate passage created by insertion, deletion, or surrounding-text addition — not by character-level editing
    or paraphrasing. These preserve the internal structure of the original passage while changing its boundaries or surrounding
    context.
- term: Saliency surface
  definition: >-
    A 2D matrix indexed by (position, n-gram-id) where each cell contains the local TF-IDF score of that n-gram at that position,
    analogous to a spectrogram in audio processing.
- term: Lookahead window W
  definition: >-
    The maximum positional gap between an anchor and target landmark when forming pairs. Controls the trade-off between fingerprint
    density and sensitivity to large-scale reorderings.
summary: >-
  We hypothesize that text near-duplicate detection can be made more robust to structural edits (embedding passages in larger
  documents, inserting/deleting paragraphs) by adapting Shazam's audio fingerprinting mechanism: instead of hashing individual
  k-gram landmarks (Winnowing) or global shingle statistics (MinHash), hash PAIRS of locally-salient n-gram landmarks together
  with their relative positional offset, creating fingerprints that are invariant to shifts in absolute position and resilient
  to surrounding-text addition.
_relation_rationale: >-
  Narrows the comparison target from Jaccard MinHash to containment MinHash; expected gains revised downward accordingly.
_confidence_delta: decreased
_key_changes:
- >-
  Added MinHash Containment (|A∩B|/|A|, LSH Ensemble / datasketch MinHashLSHEnsemble) as the primary baseline that must be
  beaten — the reviewer correctly identifies this as the obvious fix for length-sensitivity, and the 33-39pp Jaccard MinHash
  improvements may largely collapse against it.
- >-
  Revised expected improvement magnitude from '10-40pp over MinHash' to '5-15pp over containment MinHash' to reflect that
  containment already addresses the length-sensitivity problem.
- >-
  Identified paragraph-scale reordering as the distinctive test case where landmark-pair fingerprinting should outperform
  containment (reordering breaks shingle co-occurrence patterns that containment still relies on, whereas offset-consistent
  landmark pairs can tolerate partial reordering within a lookahead window).
- >-
  Explicitly scoped out semantic paraphrase robustness (MRPC is acknowledged as uninformative for the main claim; structural
  near-duplicates with high lexical overlap remain the target).
- >-
  Added requirement to compare against Sectional MinHash (Expert Systems with Applications 2018) and Asymmetric Minwise Hashing
  (Shrivastava & Li, WWW 2015) to substantiate novelty over prior positional-extension work.
- >-
  Flagged that the synthetic benchmark must be supplemented with real-world structural edits (syndicated news pairs, CC-News
  duplicates) and must include paragraph-reorder as an edit type to test the scope of claimed robustness honestly.
- >-
  Clarified that the inverted-index scalability claim requires memory footprint analysis — landmark-pair fingerprints are
  500-2000 hashes/passage vs. 100-200 for MinHash, so index size at 1B passages is a material concern.
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

--- Item 1 ---
id: art_4FCC66jI4Gdq
type: research
title: Shazam Algorithm & Text Dedup Landscape Synthesis
summary: >-
  This research synthesizes Shazam's landmark-pair audio fingerprinting algorithm and compares it to existing text deduplication
  methods (MinHash, Winnowing, SimHash, RETSim). The investigation covers: (1) Shazam's core mechanism of pairing spectrogram
  peaks with relative time offsets to achieve massive speedup and robustness; (2) mapping audio concepts (spectral energy,
  frequency, time-delta) to text equivalents (TF-IDF, n-grams, position-delta); (3) analyzing strengths and weaknesses of
  existing text methods (MinHash degrades on structural edits, Winnowing lacks positional awareness, SimHash loses local structure,
  RETSim requires training/inference compute); (4) documenting key parameters for text adaptation (5-8 character n-grams,
  20-50 token lookahead window, 10-15% landmark density); (5) identifying critical gaps (n-gram brittleness vs audio peak
  robustness, boilerplate collision risk, large-scale reordering vulnerability). The landmark-pair approach shows theoretical
  promise for ~10pp recall improvement on structural edits via offset-consistency matching, but requires implementation validation
  to confirm effectiveness against dense boilerplate and paraphrase edits.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art__yFeBexgqp0M
type: dataset
title: GLUE MRPC Paraphrase Pairs for Near-Duplicate Detection
summary: >-
  Dataset: GLUE MRPC (Microsoft Research Paraphrase Corpus), sourced from nyu-mll/glue on HuggingFace (420,727 downloads).
  Contains 4,076 sentence pairs from news articles labeled 1=paraphrase (near-duplicate) or 0=non-paraphrase. 67.5% positive
  rate (2,753 paraphrase pairs). Paraphrase pairs share high n-gram overlap — the direct signal MinHash/Jaccard similarity
  measures via shingle sets. Non-paraphrase pairs serve as true negatives. Provenance: Dolan & Brockett 2005; incorporated
  into GLUE benchmark (Wang et al. 2019 ICLR). Each example encodes both sentences as JSON in the input field and the binary
  label as the output field, with metadata_task_type=binary_classification, metadata_source=glue_mrpc, and metadata_label_meaning.
  Schema validated against exp_sel_data_out. Files: full_data_out.json (2.3MB, 4,076 examples), mini_data_out.json (3 examples),
  preview_data_out.json (3 truncated examples). QQP was considered but MRPC was chosen because its news-domain paraphrase
  pairs have higher lexical overlap, longer texts (better shingling), and are the canonical benchmark for the near-duplicate
  detection evaluation task.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_e8BRF_V6s4Vn
type: experiment
in_dependencies:
- id: art__yFeBexgqp0M
  label: baseline paraphrase dataset
title: Landmark-Pair Fingerprinting vs MinHash/SimHash Benchmark
summary: |-
  Experiment: Landmark-Pair Fingerprinting vs MinHash/SimHash for Near-Duplicate Detection on GLUE MRPC.

  Datasets: GLUE MRPC (4,076 sentence pairs, 67.5% paraphrase) + 1,100 synthetic structural-edit pairs (prepend/append/insert edits on positive MRPC pairs).

  Methods implemented:
  1. landmark_pair: Shazam-inspired method — extract top-K salient tokens (sliding-window TF-IDF + NMS), hash pairs (anchor, target, delta) within a lookahead window W. Jaccard over fingerprint hash sets.
  2. landmark_pair_no_delta: Ablation without positional offset (delta=0).
  3. minhash_jaccard: datasketch MinHash Jaccard on 5-char shingles, 128 permutations.
  4. minhash_containment: MinHash-estimated containment (|A∩B|/min(|A|,|B|)).
  5. simhash: Custom 64-bit SimHash via TF-IDF projection onto random hyperplanes.

  Key results (recall@precision≥0.90):
  - MRPC: landmark_pair=0.109, minhash_jaccard=0.609, minhash_containment=0.000, simhash=0.000
  - Synthetic: landmark_pair=0.920, minhash_containment=1.000, minhash_jaccard=0.929, simhash=0.000

  Ablations:
  - Positional offset: SIGNIFICANT (z=-4.68, p≈0.0) — offset hurts performance vs no-delta (landmark_pair_no_delta outperforms landmark_pair on MRPC; offset adds noise at sentence length)
  - Density K: best at K=5 (diminishing returns at higher K)
  - Lookahead W: best at W=10

  Verdict: DISCONFIRM — Landmark-pair does not outperform MinHash containment (containment=1.000 vs landmark_pair=0.920 on synthetic). Structural edits with shared filler text make containment trivially effective. The positional offset is load-bearing but in a negative direction at sentence scale.

  Timing (5000-passage benchmark): landmark_pair indexing=15.4s, minhash_jaccard=1.9s, simhash=0.4s. Landmark-pair is ~8x slower than MinHash for indexing.

  Output files: method_out.json (4.7MB, schema exp_gen_sol_out validated) with per-example predict_* scores for all 5 methods across both datasets.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 4 ---
id: art_noLkmx3wo9Ir
type: dataset
title: Wikipedia Near-Duplicate Passage Benchmark
summary: >-
  Dataset: wikipedia-synthetic. Source: 2,000 English Wikipedia articles (400 words each, streamed from wikimedia/wikipedia
  20231101.en). Construction: for each source passage, 5 near-duplicate variants are generated via controlled structural edits
  — (1) insertion: boilerplate prepended; (2) deletion: middle paragraphs removed; (3) embedding: surrounded by boilerplate;
  (4) reorder: adjacent paragraphs swapped; (5) control: identical copy — plus 5 random negative pairs from unrelated articles.
  Total: 20,000 labeled pairs (10,000 positive near-duplicates, 10,000 negatives). Schema: each example has `input` (JSON
  string with passage_id, original_text, variant_text), `output` ('true'/'false'), and metadata fields (metadata_edit_type,
  metadata_source, metadata_domain, metadata_original_length_words, metadata_variant_length_words, metadata_edit_distance_jaccard,
  metadata_is_near_duplicate). The dataset directly evaluates MinHash landmark-pair fingerprinting: control pairs have Jaccard=1.0,
  structural edits produce Jaccard 0.6-0.9 (measuring robustness), negatives have Jaccard near 0.0 (measuring specificity).
  Split into two 55MB parts (10,000 examples each) under full_data_out/. Validated against exp_sel_data_out.json schema. LLM
  cost: $0.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 5 ---
id: art_p0krCKwfaXGi
type: evaluation
title: MinHash vs Landmark-Pair Fingerprinting Benchmark
summary: |-
  EVALUATION COMPLETED on GLUE MRPC (4076 pairs) + 2000 synthetic structural-edit variants (10 edit types × 200 source pairs). Implements and benchmarks 5 methods: landmark-pair fingerprinting (with and without positional offset), MinHash Jaccard, MinHash Containment, and SimHash.

  KEY FINDINGS:
  1. PRIMARY METRICS (Recall@Precision≥0.90):
     - Landmark-pair (with delta): all=0.277, MRPC=0.316, synthetic=1.000
     - Landmark-pair (no delta, ablation): all=0.378, MRPC=0.456, synthetic=1.000
     - MinHash Jaccard: all=0.201, MRPC=0.298, synthetic=1.000
     - MinHash Containment: all=0.402, MRPC=0.001 (length-sensitivity artifact), synthetic=1.000
     - SimHash: all=0.165, MRPC=0.182, synthetic=1.000

  2. ABLATION (positional offset): Removing the delta does NOT significantly reduce recall on the synthetic benchmark (all edits recoverable without position). p=1.0, z=0.0 — offset is NOT load-bearing for pure structural edits at this sentence scale.

  3. STRUCTURAL EDIT BREAKDOWN: All 10 edit types (insert_prefix_50, insert_prefix_100, insert_suffix_50, insert_suffix_100, insert_middle_30, reorder, delete_20pct, delete_40pct, embed_both, mixed_prefix_delete) achieve recall@P90=1.000 (n=200 each, Wilson CI [0.981, 1.000]). MRPC originals: recall@P90=0.316.

  4. SCALABILITY:
     - Avg hashes per passage: 151.5 (comparable to MinHash 128, not 500-2000 as expected — sentence-level texts are short)
     - Retrieval latency mean: 0.074 ms, p95: ~0.2 ms, throughput: ~1000 QPS
     - Memory at 1M passages: ~1.2 GB (8 bytes × 151.5 × 1M)

  5. NOVELTY: Landmark-pair is mechanistically distinct from Sectional MinHash (individual shingle hashing) and Asymmetric MinHash (containment via transformed shingles). The co-occurrence of high-salience token pairs with quantized relative offset constitutes a genuine cross-domain transfer from audio fingerprinting. However, offset is not load-bearing at sentence scale — the co-occurrence signal alone drives detection, suggesting the mechanism works but the positional component adds little for short texts.

  FILES: eval_out.json (4.5MB, 6076 examples, schema validated), full_eval_out.json, mini_eval_out.json, preview_eval_out.json.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

id: art_e8BRF_V6s4Vn
type: experiment
in_dependencies:
- id: art__yFeBexgqp0M
  label: baseline paraphrase dataset
title: Landmark-Pair Fingerprinting vs MinHash/SimHash Benchmark
summary: |-
  Experiment: Landmark-Pair Fingerprinting vs MinHash/SimHash for Near-Duplicate Detection on GLUE MRPC.

  Datasets: GLUE MRPC (4,076 sentence pairs, 67.5% paraphrase) + 1,100 synthetic structural-edit pairs (prepend/append/insert edits on positive MRPC pairs).

  Methods implemented:
  1. landmark_pair: Shazam-inspired method — extract top-K salient tokens (sliding-window TF-IDF + NMS), hash pairs (anchor, target, delta) within a lookahead window W. Jaccard over fingerprint hash sets.
  2. landmark_pair_no_delta: Ablation without positional offset (delta=0).
  3. minhash_jaccard: datasketch MinHash Jaccard on 5-char shingles, 128 permutations.
  4. minhash_containment: MinHash-estimated containment (|A∩B|/min(|A|,|B|)).
  5. simhash: Custom 64-bit SimHash via TF-IDF projection onto random hyperplanes.

  Key results (recall@precision≥0.90):
  - MRPC: landmark_pair=0.109, minhash_jaccard=0.609, minhash_containment=0.000, simhash=0.000
  - Synthetic: landmark_pair=0.920, minhash_containment=1.000, minhash_jaccard=0.929, simhash=0.000

  Ablations:
  - Positional offset: SIGNIFICANT (z=-4.68, p≈0.0) — offset hurts performance vs no-delta (landmark_pair_no_delta outperforms landmark_pair on MRPC; offset adds noise at sentence length)
  - Density K: best at K=5 (diminishing returns at higher K)
  - Lookahead W: best at W=10

  Verdict: DISCONFIRM — Landmark-pair does not outperform MinHash containment (containment=1.000 vs landmark_pair=0.920 on synthetic). Structural edits with shared filler text make containment trivially effective. The positional offset is load-bearing but in a negative direction at sentence scale.

  Timing (5000-passage benchmark): landmark_pair indexing=15.4s, minhash_jaccard=1.9s, simhash=0.4s. Landmark-pair is ~8x slower than MinHash for indexing.

  Output files: method_out.json (4.7MB, schema exp_gen_sol_out validated) with per-example predict_* scores for all 5 methods across both datasets.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

id: art_noLkmx3wo9Ir
type: dataset
title: Wikipedia Near-Duplicate Passage Benchmark
summary: >-
  Dataset: wikipedia-synthetic. Source: 2,000 English Wikipedia articles (400 words each, streamed from wikimedia/wikipedia
  20231101.en). Construction: for each source passage, 5 near-duplicate variants are generated via controlled structural edits
  — (1) insertion: boilerplate prepended; (2) deletion: middle paragraphs removed; (3) embedding: surrounded by boilerplate;
  (4) reorder: adjacent paragraphs swapped; (5) control: identical copy — plus 5 random negative pairs from unrelated articles.
  Total: 20,000 labeled pairs (10,000 positive near-duplicates, 10,000 negatives). Schema: each example has `input` (JSON
  string with passage_id, original_text, variant_text), `output` ('true'/'false'), and metadata fields (metadata_edit_type,
  metadata_source, metadata_domain, metadata_original_length_words, metadata_variant_length_words, metadata_edit_distance_jaccard,
  metadata_is_near_duplicate). The dataset directly evaluates MinHash landmark-pair fingerprinting: control pairs have Jaccard=1.0,
  structural edits produce Jaccard 0.6-0.9 (measuring robustness), negatives have Jaccard near 0.0 (measuring specificity).
  Split into two 55MB parts (10,000 examples each) under full_data_out/. Validated against exp_sel_data_out.json schema. LLM
  cost: $0.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

id: art_p0krCKwfaXGi
type: evaluation
title: MinHash vs Landmark-Pair Fingerprinting Benchmark
summary: |-
  EVALUATION COMPLETED on GLUE MRPC (4076 pairs) + 2000 synthetic structural-edit variants (10 edit types × 200 source pairs). Implements and benchmarks 5 methods: landmark-pair fingerprinting (with and without positional offset), MinHash Jaccard, MinHash Containment, and SimHash.

  KEY FINDINGS:
  1. PRIMARY METRICS (Recall@Precision≥0.90):
     - Landmark-pair (with delta): all=0.277, MRPC=0.316, synthetic=1.000
     - Landmark-pair (no delta, ablation): all=0.378, MRPC=0.456, synthetic=1.000
     - MinHash Jaccard: all=0.201, MRPC=0.298, synthetic=1.000
     - MinHash Containment: all=0.402, MRPC=0.001 (length-sensitivity artifact), synthetic=1.000
     - SimHash: all=0.165, MRPC=0.182, synthetic=1.000

  2. ABLATION (positional offset): Removing the delta does NOT significantly reduce recall on the synthetic benchmark (all edits recoverable without position). p=1.0, z=0.0 — offset is NOT load-bearing for pure structural edits at this sentence scale.

  3. STRUCTURAL EDIT BREAKDOWN: All 10 edit types (insert_prefix_50, insert_prefix_100, insert_suffix_50, insert_suffix_100, insert_middle_30, reorder, delete_20pct, delete_40pct, embed_both, mixed_prefix_delete) achieve recall@P90=1.000 (n=200 each, Wilson CI [0.981, 1.000]). MRPC originals: recall@P90=0.316.

  4. SCALABILITY:
     - Avg hashes per passage: 151.5 (comparable to MinHash 128, not 500-2000 as expected — sentence-level texts are short)
     - Retrieval latency mean: 0.074 ms, p95: ~0.2 ms, throughput: ~1000 QPS
     - Memory at 1M passages: ~1.2 GB (8 bytes × 151.5 × 1M)

  5. NOVELTY: Landmark-pair is mechanistically distinct from Sectional MinHash (individual shingle hashing) and Asymmetric MinHash (containment via transformed shingles). The co-occurrence of high-salience token pairs with quantized relative offset constitutes a genuine cross-domain transfer from audio fingerprinting. However, offset is not load-bearing at sentence scale — the co-occurrence signal alone drives detection, suggesting the mechanism works but the positional component adds little for short texts.

  FILES: eval_out.json (4.5MB, 6076 examples, schema validated), full_eval_out.json, mini_eval_out.json, preview_eval_out.json.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Introduction

Near-duplicate detection is critical for web search, LLM training data quality, and copyright violation detection. A web crawler indexing billions of documents must quickly identify exact and near-duplicate pages to prevent redundant storage and ranking. Modern large language models are trained on datasets containing hundreds of billions of tokens, and dataset contamination—where identical or near-duplicate passages appear across multiple sources—can compromise benchmark validity and create undesirable memorization [1]. Legal systems must identify contract reuse and plagiarism. At this scale, computational efficiency is paramount: methods must operate in sub-linear time with modest memory overhead.

MinHash, introduced by Broder in 1997, has become the industrial standard [2]. It estimates Jaccard similarity between documents by computing minimum hash values across k-gram shingles, enabling sub-linear candidate retrieval via Locality-Sensitive Hashing (LSH) [3, 4]. This approach powers deduplication at Google, HuggingFace, and major LLM training pipelines [1, 5, 6].

However, MinHash's global Jaccard similarity metric has a critical weakness: it is sensitive to document length. When a passage is embedded in a larger document or has surrounding boilerplate added, the Jaccard score drops dramatically. For example, a 100-shingle passage embedded in a 500-shingle context has Jaccard = 100/(100+500) = 0.17, far below typical thresholds of 0.80–0.95 [7, 8]. This structural-edit scenario is extremely common: article syndication with different headlines, legal contracts with preambles, and dataset contamination with varying surrounding context [9, 10, 11].

The solution is not a new algorithm but a metric fix: **MinHash Containment**, defined as |A∩B|/|A| (the fraction of query shingles found in the document), is invariant to document size [2]. This asymmetric similarity metric is implemented in production systems like datasketch and LSH Ensemble, yet is surprisingly absent from recent near-duplicate detection research and benchmarks [12, 13].

We began this work motivated by a cross-domain analogy: Shazam's audio fingerprinting algorithm solves a superficially similar problem by hashing **pairs** of locally-salient spectral peaks together with their relative time offset, rather than individual peaks or global statistics [14]. This insight—encoding WHERE two salient features co-occur relative to each other—creates fingerprints invariant to absolute temporal position and robust to noise. We hypothesized that adapting this landmark-pair hashing to text could provide an alternative mechanism for structural robustness, offering insights into why positional structure matters in fingerprinting.

This work explores that hypothesis and documents what we found: **the transfer succeeds mechanistically but fails empirically**. Landmark-pair fingerprinting is genuinely novel as a cross-domain adaptation, but provides no advantage over MinHash Containment on realistic data, and the positional offset component—the core innovation from Shazam—actually hurts performance. We contribute an honest analysis of why this transfer failed: text landmarks are fundamentally different from audio peaks (brittle to paraphrasing, short context for relative offsets), and text-scale structural features do not encode robustness in the way audio time offsets do.

## Summary of Contributions

- **Cross-domain transfer analysis**: Explicit mapping of Shazam's audio fingerprinting (peak-frequency-time-delta) to text (n-gram-identity-position-delta), identifying critical domain differences that explain transfer failure.
- **Empirical evidence of negative result**: Rigorous comparison showing landmark-pair provides no recall advantage over MinHash Containment on structural edits, and the positional offset is actually harmful (z=-4.68, p<0.001).
- **Benchmark critique**: Demonstration that synthetic structural-edit benchmarks can be misleading if they preserve high lexical overlap in the shared portion—all modern methods (MinHash Jaccard, Containment, SimHash, landmark-pair) achieve perfect recall when the shared text itself has high Jaccard overlap.
- **Mechanistic novelty without empirical advantage**: Documentation of a genuinely novel fingerprinting mechanism that fails to deliver expected benefits, contributing to understanding of cross-domain transfer boundaries in information retrieval.

# Related Work

## Classical and Industrial Approaches

MinHash [2] estimates Jaccard similarity of k-gram shingle sets via random hash minima. It scales to billions of documents and powers production deduplication systems [1, 5, 6]. A critical limitation: global Jaccard score |A∩B|/|A∪B| is sensitive to document length—adding any text to a document reduces the Jaccard score with the original.

MinHash Containment [2], defined as |A∩B|/|A|, addresses this by computing the fraction of query shingles found in a candidate. This asymmetric metric is invariant to the size of the document—a key insight formalized in LSH Ensemble by Zhu et al. [15], which provides efficient indexing for containment queries. The datasketch Python library implements MinHashLSHEnsemble, making containment-based deduplication practical at scale. Despite being a well-established solution, containment metrics are underrepresented in recent near-duplicate detection research.

Winnowing [16] selects a sparse subset of k-gram hashes using a sliding-window minimum, guaranteeing at least one fingerprint in every window of length w. This improves locality compared to random MinHash but does not encode positional relationships between landmarks—it indexes individual hash landmarks only.

SimHash [17] projects TF-IDF vectors onto random hyperplanes to produce dense bit-vectors, enabling fast Hamming-distance similarity. Like MinHash, it captures global document statistics without local structural encoding.

Recent neural approaches like RETSim [18] train deep models on character-level edits to produce robust embeddings, achieving state-of-the-art robustness to paraphrasing and character edits. These methods trade symbolic determinism for learned domain adaptation, requiring significant training data and inference compute.

## Audio Fingerprinting and Cross-Domain Transfer

Shazam's audio fingerprinting algorithm [14], deployed commercially for song identification, encodes **pairs** of locally-maximal spectral peaks (anchor-frequency, target-frequency, time-delta) rather than individual peaks or global spectra. This design exploits the observation that two peaks at a fixed time offset are unlikely to collide spuriously—the offset provides discriminative power. The algorithm identifies a 10-second audio snippet captured via noisy cellphone microphone against a database of millions of tracks in under a second.

The key insight—that relative positional relationships preserve robustness under noise and temporal shift—has never been applied to text near-duplicate detection. This work explores that transfer, mapping (audio-frequency, energy, time-delta) to (n-gram-identity, TF-IDF, position-delta).

# Methods

## Landmark Extraction

For each input passage, we compute a saliency surface indexed by token position and n-gram type, then extract landmarks as local maxima.

Let passage d have length L tokens. We slide a context window of size $W_c$ (typically 10–20 tokens) across the passage. For each position $p \in [1, L]$, we compute local TF-IDF scores for all character n-grams $g$ of length $k \in \{5, 6, 7, 8\}$ that occur within the window:

$$\text{TF-IDF}(g, p) = \text{TF}(g, p) \cdot \log\left(\frac{N}{\text{DF}(g)}\right)$$

where $\text{TF}(g, p)$ is the frequency of n-gram $g$ in the local window around $p$, $\text{DF}(g)$ is the number of passages containing $g$, and $N$ is the total corpus size.

We apply non-maximum suppression (NMS) with radius ~3 positions to identify local peaks in the saliency surface. To control landmark density, we retain only the top k% by TF-IDF score (typically k=5–15%), yielding ~5–10 landmarks per passage on GLUE MRPC sentence pairs.

## Landmark Pair Hashing

For each anchor landmark $(p_a, g_a)$, we enumerate target landmarks $(p_t, g_t)$ where $p_t \in [p_a, p_a + W]$ (lookahead window W, typically 10–20 tokens). We emit a hash:

$$\text{hash}(g_a, g_t, \lfloor (p_t - p_a) / Q \rfloor)$$

where Q is quantization factor (typically 5 tokens) rounding position-delta. The full fingerprint is the set of all such hashes.

## Inverted Index and Retrieval

We build an inverted index mapping each hash to passages containing it. For a query, we compute its fingerprint, look up all hashes in the index, and rank candidates by shared hash count. Candidates exceeding a similarity threshold (typically 50% of query hashes matched) are returned as near-duplicates.

# Experiments

## Setup

**Datasets:**
- GLUE MRPC: 4,076 sentence pairs from news articles, 67.5% labeled as paraphrases (near-duplicates), 10–30 words per sentence [19, 20].
- Synthetic Structural Edits: 2,000 Wikipedia passages (400 words each) with 10 variants per passage: prepended boilerplate (50–100 tokens), appended boilerplate, embedded in context (2000 tokens), paragraph reordering, middle deletions (20–40%), mixed edits, and exact copies. Total: 20,000 pairs (10,000 positive near-duplicates, 10,000 negatives).

**Methods Compared:**
1. Landmark-pair: Proposed method with positional offset.
2. Landmark-pair (no offset): Ablation without delta in hash.
3. MinHash Jaccard: Standard Jaccard similarity, 128 permutations, datasketch library.
4. MinHash Containment: Containment metric |A∩B|/|A|, 128 permutations, datasketch.
5. SimHash: 64-bit SimHash via TF-IDF projection onto random hyperplanes.

**Metrics:** Recall at precision ≥0.90, F1 score, Average Precision, Area Under PR curve.

## Results on GLUE MRPC

On the standard paraphrase benchmark (Table 1):

| Method | Recall@P≥0.90 | AUC-PR | F1 |
|--------|---|---|---|
| MinHash Jaccard | 0.364 | 0.853 | 0.813 |
| MinHash Containment | 0.000 | 0.808 | 0.814 |
| SimHash | 0.246 | 0.828 | 0.810 |
| Landmark-pair | 0.109 | 0.790 | 0.806 |
| Landmark-pair (no offset) | 0.152 | 0.806 | 0.806 |

Landmark-pair underperforms: recall of 0.11 versus Jaccard's 0.36. Removing the positional offset improves performance to 0.15, though still below Jaccard. MinHash Containment achieves 0 recall@P≥0.90, failing entirely on this dataset—likely because true paraphrases have lower containment scores than false positives when sentences are of similar length and differ in word order.

[FIGURE:fig_mrpc_results]

## Results on Synthetic Structural Edits

On the synthetic benchmark (Table 2), where the original passage and variants share the same core text:

| Edit Type | Landmark-pair | Containment | Jaccard | No Offset |
|---|---|---|---|---|
| Insertion (prepend) | 1.000 | 1.000 | 1.000 | 1.000 |
| Insertion (append) | 1.000 | 1.000 | 1.000 | 1.000 |
| Insertion (middle) | 1.000 | 1.000 | 1.000 | 1.000 |
| Deletion (20%) | 1.000 | 1.000 | 1.000 | 1.000 |
| Deletion (40%) | 1.000 | 1.000 | 1.000 | 1.000 |
| Reordering | 1.000 | 1.000 | 1.000 | 1.000 |
| Embedding | 1.000 | 1.000 | 1.000 | 1.000 |
| Mixed edits | 1.000 | 1.000 | 1.000 | 1.000 |

All methods achieve perfect recall (1.0) across all edit types. This surprising result reflects a fundamental property of the synthetic benchmark: variants preserve the original text verbatim, so the shared portion has Jaccard = 1.0. MinHash Containment, Jaccard, and landmark-pair all detect the shared core text because it is sufficiently large and identical. The benchmark does not test robustness to semantic variation or within-passage reordering.

[FIGURE:fig_synthetic_results]

## Ablation: Positional Offset is Harmful

We compare landmark-pair with and without the positional offset component (Table 3):

| Metric | With Offset | Without Offset | Difference |
|---|---|---|---|
| MRPC Recall@P≥0.90 | 0.109 | 0.152 | -0.043 |
| Synthetic Recall@P≥0.90 | 1.000 | 1.000 | 0.000 |

On MRPC, removing the offset **improves recall by 4.3 percentage points** (0.11 → 0.15), though both remain well below MinHash Jaccard (0.36). Statistical testing (two-proportion z-test): z = -4.68, p < 0.001, indicating the difference is highly significant. On synthetic data, both achieve perfect recall; removing the offset has no effect.

This result directly contradicts the hypothesis that positional offset is load-bearing. Instead, the offset adds noise on realistic text: text landmarks are brittle and unstable, and sentence-scale texts are too short for the relative offset to provide discriminative signal.

[FIGURE:fig_ablation]

## Scalability and Efficiency

On a 1M-passage indexed corpus:
- Landmark-pair: Average 151.5 hashes per passage, memory = 1.2 GB.
- MinHash: Average 128 hashes per passage, memory = 1.0 GB.
- Query latency: Landmark-pair 0.11 ms mean (p95: 0.16 ms), throughput ~900 queries/second.

Landmark-pair's indexing is 10–15% larger than MinHash but remains efficient at scale. Query latency is competitive with inverted-index lookups.

# Discussion

## Why Landmark-Pair Fails on Text

The core hypothesis was that Shazam's positional offset encoding would transfer to text, providing structural robustness unavailable in global methods like MinHash. Instead, the experiments show the opposite. We identify three domain differences that explain this failure:

### 1. Landmark Brittleness

In audio, spectral peaks (local energy maxima at specific frequencies) survive noise and temporal distortion reliably. A peak remains a peak unless the underlying signal changes fundamentally. In text, n-gram landmarks are brittle: a single character change, typo, or synonym substitution destroys the n-gram identity, eliminating the landmark entirely. On MRPC paraphrases where sentences are reworded, the set of n-gram landmarks changes substantially, reducing overlap. The ablation shows that when landmarks do overlap (synthetic data with verbatim shared text), the positional offset between them is actually **noise** that hurts matching.

### 2. Scale Mismatch

Shazam operates on audio snippets ~30–60 seconds long (thousands of spectral peaks), where the relative time offset between pairs encodes meaningful structure. GLUE MRPC sentences are 10–30 words (~50–150 characters), yielding only 5–10 landmarks per passage. At this scale, offset information is sparse and unreliable. The lookahead window W (typically 10–20 tokens) covers most of the text, making position differences less discriminative.

### 3. Containment Already Solves the Problem

The experiments show that MinHash Containment achieves perfect recall (1.0) on all synthetic structural edits, identical to landmark-pair. This simple metric fix—using |A∩B|/|A| instead of Jaccard—already addresses the length-sensitivity problem that motivated our work. Landmark-pair provides no advantage over this well-established baseline.

## Benchmark Critique: The Synthetic Dataset is Misleading

The synthetic structural-edit corpus, designed to test robustness to insertion/deletion/embedding, has a critical flaw: all variants preserve the original text verbatim. This means the shared portion has Jaccard = 1.0 or near-1.0, a strong signal that all reasonable methods can exploit. The benchmark does not test robustness to:
- Within-passage paragraph reordering (which breaks shingle co-occurrence patterns).
- Semantic paraphrasing (which changes n-gram identity).
- Subtle insertions that blur boundaries (e.g., replacing a clause with a longer explanation).

A more challenging benchmark would evaluate real-world duplicates: syndicated news pairs from Common Crawl, actual duplicate detection in web crawls, or near-duplicates mined from Wikipedia. The synthetic dataset's perfect recall across all methods suggests it is not discriminative enough for method comparison.

## Why the Offset Hurts on Real Data

The ablation result—removing the offset improves MRPC performance—has a straightforward explanation. Landmark-pair with offset hashes $(g_a, g_t, \Delta p)$ triples, creating sparse fingerprints: for any given pair of n-grams $(g_a, g_t)$, the offset dimension further subdivides the hash space. When text landmarks are unstable (changing across paraphrases), fingerprints become even sparser. The query fingerprint and document fingerprint share fewer hashes due to offset mismatch, reducing recall.

Without offset, the hash $(g_a, g_t)$ is coarser, capturing co-occurrence regardless of exact position. On text with unstable landmarks and limited length, this co-occurrence signal is more robust than positional structure.

## Implications for Cross-Domain Transfer

This work documents a mechanistically sound cross-domain transfer that fails empirically due to fundamental domain differences. The key lesson: **positional structure matters differently in audio and text**. In audio, peaks are stable and time offsets encode fundamental physical relationships (frequency spacing over time). In text, landmarks are fragile and spatial offsets are a secondary signal, often adding noise rather than information.

This does not invalidate the Shazam-to-text analogy entirely—landmark-pair fingerprinting is a genuine novel mechanism. But it highlights that algorithmic insights do not transfer directly across domains without accounting for domain-specific properties of the primitives (peaks vs. n-grams) and the scale at which they operate.

# Conclusion

We explored adapting Shazam's landmark-pair audio fingerprinting to text near-duplicate detection, motivated by the hypothesis that positional offset encoding would provide structural robustness unavailable in global methods like MinHash. Our experiments show this transfer succeeds mechanistically—landmark-pair is a genuinely novel fingerprinting approach—but fails empirically. MinHash Containment, a simple metric fix absent from recent research, achieves equal or superior performance at a fraction of the complexity. The positional offset component, the core innovation from Shazam's design, is actually harmful on realistic text due to landmark brittleness and text-scale limitations.

This negative result contributes to our understanding of cross-domain transfer boundaries: algorithmic insights from one domain do not transfer without accounting for fundamental differences in the problem primitives. Future work should focus on domain-adapted approaches like neural embeddings that learn robust features specific to text, rather than attempting to transfer audio fingerprinting principles directly.

The most practical insight from this work: **MinHash Containment is underutilized despite solving the structural-edit robustness problem that motivated recent research**. Practitioners should adopt asymmetric containment metrics as a standard baseline before exploring more complex approaches.

# References

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (rigor) The reference section is completely empty. The paper contains approximately 20 in-text citations ([1] through [20]) but the References section contains no entries. This is fatal for submission: reviewers cannot verify any cited claims, novelty cannot be assessed, and the paper does not meet the minimum bar of a scholarly document.
  Action: Populate the reference section with complete bibliographic entries for every in-text citation before resubmission. At minimum: Broder 1997 (MinHash), Indyk & Motwani 1998 (LSH), Wang et al. 2019 (GLUE), Dolan & Brockett 2005 (MRPC), Zhu et al. VLDB 2016 (LSH Ensemble), Wang 2003 (Shazam audio fingerprinting), Manasse et al. 2010 (Simhash), Manku et al. 2007 (Simhash web dedup), Pennington et al. (RETSim or equivalent neural baseline).
- [MAJOR] (evidence) Significant numerical discrepancies between Table 1 in the paper and both supplementary artifacts. For MinHash Jaccard recall@P≥0.90 on MRPC: paper reports 0.364, artifact e8BRF reports 0.609, artifact p0krCKwfaXGi reports 0.298. For landmark-pair: paper reports 0.109 but artifact p0krCKwfaXGi reports 0.316. For synthetic structural edits: paper claims 1.000 for all methods but artifact e8BRF reports landmark_pair = 0.920. These are not rounding differences—they suggest the paper's numbers were not generated from the artifacts. Conclusions about relative ordering of methods could be reversed depending on which numbers are correct.
  Action: Re-run the evaluation from artifact p0krCKwfaXGi (which appears most complete with 6,076 examples) and copy numbers directly from full_eval_out.json into the paper tables. Document in the paper which artifact and which output file each table row comes from. Reconcile or explain the discrepancy between artifact e8BRF and art_p0krCKwfaXGi.
- [MAJOR] (methodology) The MinHash Containment baseline may be implemented incorrectly. Artifact e8BRF describes it as '|A∩B|/min(|A|,|B|)' (symmetric), while standard MinHash Containment is |A∩B|/|A| (asymmetric, query shingles as denominator). These are different metrics with different properties: true asymmetric containment is invariant to document size for fixed query size, while the symmetric form is not. The paper describes the correct definition in text ('|A∩B|/|A|') but the artifact may implement the wrong one. If the containment baseline is wrong, the comparison is invalid.
  Action: Check the containment implementation in the artifact code. If it computes min(|A|,|B|) in the denominator, fix it to use |A| (query size). Re-run and update all tables. Also verify that the datasketch MinHashLSHEnsemble is configured to use the query set as the denominator, not the minimum.
- [MAJOR] (evidence) The synthetic benchmark scale is inconsistent across the paper. The paper states '2,000 Wikipedia passages × 10 variants = 20,000 pairs.' The experiment artifact (art_p0krCKwfaXGi) summary says '10 edit types × 200 source pairs.' The dataset artifact (art_noLkmx3wo9Ir) says '2,000 English Wikipedia articles × 5 variants = 20,000 labeled pairs' (5 variants, not 10). These three sources give three different numbers. Given perfect recall on synthetic in all conditions, the scale does not change the conclusions, but the inconsistency signals that numbers were not carefully verified against actual runs.
  Action: Run 'wc -l' or equivalent count on the actual output files and report the true number of source passages, edit types, and total pairs. Ensure the paper text, Table 2 header, and artifact summaries all state the same numbers.
- [MINOR] (methodology) GLUE MRPC remains an inappropriate primary benchmark for near-duplicate detection. Sentences of 10–30 words yield only 5–10 landmarks per passage, which is acknowledged in the Discussion but not adequately weighted in the framing. The paper uses MRPC for all comparative claims (Table 1, the ablation in Table 3) despite acknowledging it does not test the structural-edit hypothesis. Worse, MinHash Containment achieves 0 recall@P≥0.90 on MRPC—not because containment is bad, but because containment is correctly calibrated for length-asymmetric matching and MRPC pairs have matched sentence lengths, so containment behaves like Jaccard there. This makes the MRPC comparison misleading for evaluating containment's real-world utility.
  Action: Add a paragraph clarifying that MRPC results should not be used to rank methods for structural-edit deduplication—they test a different mode (short paraphrase matching). Either introduce a real-world structural-edit benchmark (syndicated news pairs, Common Crawl duplicates) or clearly label MRPC as a secondary evaluation that tests only short-text paraphrase matching, not the paper's primary hypothesis.
- [MINOR] (scope) The paper reports indexing is ~8× slower than MinHash (15.4s vs 1.9s from artifact e8BRF, not stated in the paper text) but the scalability section buries this. At 1B-passage corpus scale (the stated motivation in the introduction), this throughput gap is a practical blocker. The paper presents scalability as a strength without acknowledging this limitation.
  Action: Add a sentence in the Scalability section noting that landmark-pair indexing is approximately 8× slower than MinHash due to TF-IDF saliency computation and NMS. If landmark-pair cannot scale to 1B passages within practical compute budgets, say so explicitly rather than reporting only query latency (which is fast because it's inverted index lookup, not the bottleneck).
- [MINOR] (contribution) The paper's primary practical recommendation—'MinHash Containment is underutilized'—is not novel. LSH Ensemble (Zhu et al., VLDB 2016) formalized containment-based LSH, datasketch provides a production implementation, and the recommendation to use containment for document-in-document retrieval is well-established. The paper needs to either demonstrate that the NLP/IR community has genuinely overlooked this (by surveying recent papers that should have used containment but used Jaccard instead) or shift the contribution framing away from this recommendation.
  Action: Conduct a targeted survey of the last 3 years of near-duplicate detection papers at ACL/EMNLP/WWW and count how many use Jaccard vs. containment. If the majority use Jaccard, the empirical survey constitutes evidence that containment is underutilized and becomes a citable contribution. If not, drop the recommendation as a contribution and focus on the cross-domain transfer analysis and benchmark critique.
</reviewer_feedback>



<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-03 18:50:15 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [3] SYSTEM-USER prompt · 2026-07-03 18:50:47 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Previous H expected modest 5-15pp gains; evidence shows zero advantage and negative offset effect — reframed as documented null result.' is too long (at most 120 characters, got 135)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
