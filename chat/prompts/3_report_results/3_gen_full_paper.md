# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_Bd0c_4hy9OC-` — Near Duplicate Detection
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-07-03 19:27:01 UTC

````
<research_methodology>
Write like an experienced academic. Reviewers judge both the science and the writing.

- Claims must be proportional to evidence. Choose verbs carefully — "demonstrate," "observe," and "hypothesize" mean different things.
- Every result needs: what was measured, on what data, the numbers, and what they mean.
- Methodology must be specific enough to reproduce. Related work must be organized by theme, not a literature dump.
- State limitations honestly. Avoid both overclaiming and excessive hedging.
</research_methodology>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: 'Landmark-Pair Fingerprinting for Text: Cross-Domain Transfer Without Advantage'
abstract: >-
  Near-duplicate detection via MinHash is the dominant approach for large-scale text deduplication, but fails on structural
  edits where passages are embedded in larger documents or have surrounding text added. We explore adapting Shazam's audio
  fingerprinting algorithm—which encodes landmark pairs with relative time offsets—directly to text. Despite being a mechanistically
  novel cross-domain transfer, landmark-pair fingerprinting provides no empirical advantage over MinHash Containment (|A∩B|/|A|),
  a well-established asymmetric similarity metric that addresses length-sensitivity. On GLUE MRPC paraphrases, landmark-pair
  achieves 0.11 recall@precision≥0.90 versus MinHash Jaccard's 0.36; on synthetic structural edits, both containment MinHash
  and landmark-pair achieve perfect recall (1.0), suggesting the synthetic benchmark's shared-text assumption makes the problem
  trivial for modern baselines. Ablation studies show the positional offset component—the core novel contribution from Shazam's
  design—actually hurts performance on real data (0.11 with offset vs. 0.46 without, z=-4.68, p<0.001), contradicting the
  hypothesis that offset encodes useful structural information for text. We analyze the source of this failure: text landmarks
  (n-gram overlaps) are brittle to character-level edits and paraphrasing in ways audio spectral peaks are not, and sentence-scale
  text is too short to benefit from positional structure. This work documents a cross-domain transfer that succeeds mechanistically
  but fails empirically, contributing to our understanding of which insights transfer across domains.
paper_text: |
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
summary: >-
  This work explores adapting Shazam's audio landmark-pair fingerprinting to text near-duplicate detection. Experiments show
  the cross-domain transfer is mechanistically novel but empirically fails: MinHash Containment (a simple asymmetric metric)
  achieves equal performance, and the positional offset component actually hurts recall on realistic data (z=-4.68, p<0.001).
  The paper documents why: text landmarks are brittle to paraphrasing, text-scale is too small for positional structure to
  help, and containment MinHash already solves the problem. This is a negative-result paper contributing honest analysis of
  cross-domain transfer boundaries.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig_mrpc_results
title: Performance Comparison on GLUE MRPC
caption: >-
  Recall at precision ≥0.90 across methods on GLUE MRPC paraphrase detection. MinHash Jaccard achieves 0.364 recall, landmark-pair
  achieves 0.109. Removing positional offset improves landmark-pair to 0.152, indicating offset adds noise. MinHash Containment
  fails completely (0.0) on paraphrases, suggesting asymmetric metrics handle length mismatch but struggle with semantic variation.
image_gen_detailed_description: >-
  Bar chart, horizontal orientation. X-axis: recall at precision ≥0.90 (0.0–0.5). Y-axis: methods (MinHash Jaccard, MinHash
  Containment, SimHash, Landmark-pair with offset, Landmark-pair no offset). Values: MinHash Jaccard=0.364 (blue), MinHash
  Containment=0.0 (red), SimHash=0.246 (green), Landmark-pair with offset=0.109 (orange), Landmark-pair no offset=0.152 (purple).
  Error bars for 95% Wilson confidence intervals. Font: sans-serif. Background: white.
aspect_ratio: '21:9'
summary: >-
  MRPC recall comparison showing landmark-pair underperforms standard baselines; offset component hurts performance.
figure_path: figures/fig_mrpc_results_v0.jpg

--- Item 2 ---
id: fig_synthetic_results
title: All Methods Peak on Synthetic Structural Edits
caption: >-
  Recall at precision ≥0.90 across all methods on synthetic structural-edit variants. All methods achieve perfect recall (1.0)
  across insertion, deletion, reordering, and embedding variants. This indicates the synthetic benchmark's shared-text assumption
  makes the problem trivial—all modern methods exploit high Jaccard overlap in the preserved core.
image_gen_detailed_description: >-
  Grouped bar chart. X-axis: edit type (prepend, append, middle insert, delete 20%, delete 40%, reorder, embed, mixed). Y-axis:
  recall at precision ≥0.90 (0.0–1.0). Five groups per edit type: MinHash Jaccard=1.0 (blue), MinHash Containment=1.0 (red),
  SimHash=1.0 (green), Landmark-pair with offset=1.0 (orange), Landmark-pair no offset=1.0 (purple). All bars reach 1.0. Wilson
  CIs [0.981, 1.0] shown. Font: sans-serif. Background: white.
aspect_ratio: '21:9'
summary: >-
  Perfect recall across all methods on synthetic data, demonstrating benchmark is not discriminative.
figure_path: figures/fig_synthetic_results_v0.jpg

--- Item 3 ---
id: fig_ablation
title: 'Ablation: Positional Offset Hurts Performance'
caption: >-
  Effect of removing positional offset from landmark-pair hashing. On MRPC, recall improves from 0.109 (with offset) to 0.152
  (without offset). Difference significant at α=0.05 (z=-4.68, p<0.001). On synthetic data, no difference (both achieve 1.0).
  Offset acts as noise on realistic text.
image_gen_detailed_description: >-
  Side-by-side bar chart. Left panel: MRPC recall@P≥0.90. Right panel: Synthetic recall@P≥0.90. Each panel has two bars: 'With
  offset' (orange) and 'Without offset' (purple). MRPC: with=0.109, without=0.152. Synthetic: both=1.0. 95% confidence intervals
  shown. Left panel: z=-4.68, p<0.001 annotation. Font: sans-serif. Background: white.
aspect_ratio: '21:9'
summary: >-
  Ablation showing positional offset is harmful on real data, contradicting the core hypothesis.
figure_path: figures/fig_ablation_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-03 19:27:01 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-07-03 19:27:05 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-03 19:27:07 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
