# gen_plan_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_Bd0c_4hy9OC-` — Near Duplicate Detection
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_dataset_1` (terminal_claude_agent, claude-haiku-4-5)

### [1] CONFIG · 2026-07-03 17:49:38 UTC

```
model: claude-haiku-4-5 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1
```

### [2] SYSTEM-USER prompt · 2026-07-03 17:49:46 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: DATASET

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect
</artifact_type_info>

<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<time_budget>

The dataset executor has 6h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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

<hypothesis>
kind: hypothesis
title: Shazam-Style Landmark Pairs for Text Dedup
hypothesis: >-
  Near-duplicate text passages can be detected more robustly than MinHash by fingerprinting pairs of locally-salient n-gram
  landmarks together with their relative positional offset — directly analogous to how Shazam identifies audio by hashing
  (anchor-frequency, target-frequency, time-delta) pairs. The hypothesis is: a fingerprint built from (ngram_A, ngram_B, position_delta)
  hashes, where ngram_A and ngram_B are locally-maximal TF-IDF n-grams within the passage, will achieve higher recall than
  MinHash at equivalent precision on near-duplicates created by insertion, deletion, or surrounding-text addition, because
  the relative distance between co-occurring salient n-grams is preserved under these structural edits even when absolute
  positions shift.
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
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-multi-llm-agents** — Guide for implementing Multi-LLM Agent Systems research using Mirascope orchestration, HuggingFace datasets/evaluation, and proven multi-agent patterns.
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: dataset_iter1_dir2
type: dataset
objective: >-
  Acquire PAN-PC-11 plagiarism corpus and create a synthetic benchmark of Wikipedia passages with structural edits (insertions,
  deletions, surrounding text).
approach: >-
  Download PAN-PC-11 from official source or largest publicly available plagiarism dataset. Extract all copypaste, near-copy,
  and paraphrase cases. For the synthetic benchmark, select 500 Wikipedia passages (raw text, >500 characters) as canonical
  originals. Create 5 edit-type variants per passage: (1) 0–500 char prepended boilerplate, (2) 0–500 char appended boilerplate,
  (3) 1–3 random sentences inserted mid-passage, (4) 1–3 random sentences deleted, (5) combination edits. Pair each passage
  with 5–10 unrelated passages to create negative examples. Standardize all to JSON: {passage_id, original_text, variant_id,
  variant_text, edit_type, is_near_duplicate, fold}. Validate schema, generate preview variant for rapid testing, and split
  into full/mini for iteration 2 scalability.
depends_on: []
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead
</artifact_executor_scope>

<artifact_planning_rules>
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for dataset artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
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
  "description": "Plan for a DATASET artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "ideal_dataset_criteria": {
      "description": "What makes an ideal dataset for this purpose - size, format, content requirements",
      "title": "Ideal Dataset Criteria",
      "type": "string"
    },
    "dataset_search_plan": {
      "description": "Step-by-step plan for finding/creating this dataset - sources to check, fallback options",
      "title": "Dataset Search Plan",
      "type": "string"
    },
    "target_num_datasets": {
      "description": "How many individual datasets should be delivered. Count each dataset separately, not collections \u2014 a benchmark suite of N datasets counts as N. This controls how broadly the executor searches, so setting it too low will under-collect.",
      "title": "Target Num Datasets",
      "type": "integer"
    }
  },
  "required": [
    "title",
    "ideal_dataset_criteria",
    "dataset_search_plan",
    "target_num_datasets"
  ],
  "title": "DatasetPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-07-03 17:49:46 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [4] ASSISTANT · 2026-07-03 17:49:58 UTC

```
I'll create a detailed, actionable plan for the dataset artifact. Let me first research the key datasets and their availability to make the plan concrete and realistic.
```

### [5] TOOL CALL — Skill · 2026-07-03 17:49:58 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-07-03 17:49:58 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — ToolSearch · 2026-07-03 17:50:02 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 2}
```

### [8] TOOL RESULT — ToolSearch · 2026-07-03 17:50:02 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 21}
```

### [9] TOOL CALL — WebSearch · 2026-07-03 17:50:04 UTC

```
PAN-PC-11 plagiarism corpus download official
```

### [10] TOOL CALL — WebSearch · 2026-07-03 17:50:04 UTC

```
Wikipedia dataset download raw text 500 characters
```

### [11] TOOL CALL — WebSearch · 2026-07-03 17:50:04 UTC

```
Shazam fingerprinting landmark pairs algorithm time delta
```

### [12] TOOL RESULT — WebSearch · 2026-07-03 17:50:10 UTC

```
{"query": "PAN-PC-11 plagiarism corpus download official", "results": [{"tool_use_id": "srvtoolu_01CDc9gKcNVteypdiZ8M9jDA", "content": [{"title": "PAN Plagiarism Corpus 2011 (PAN-PC-11) | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/PAN-Plagiarism-Corpus-2011-(PAN-PC-11)-Potthast-Stein/507aa7ff1ab234d64d8a9c0cac99a3213cb53834"}, {"title": "Corpus statistics for 26 939 documents and 61 064 plagiarism cases in... | Download Table", "url": "https://www.researchgate.net/figure/Corpus-statistics-for-26-939-documents-and-61-064-plagiarism-cases-in-the-PAN-PC-11_tbl1_221159623"}, {"title": "PAN Plagiarism Corpus 2011 (PAN-PC-11)", "url": "https://zenodo.org/records/3250095"}, {"title": "Dataset Search - PAN Plagiarism Corpus 2011 (PAN-PC-11)", "url": "https://toolbox.google.com/datasetsearch/search?query=pan-pc-11"}, {"title": "Performances of 9 external plagiarism detector on the PAN-PC-11. The... | Download Scientific Diagram", "url": "https://www.researchgate.net/figure/Performances-of-9-external-plagiarism-detector-on-the-PAN-PC-11-The-detectors-are_tbl2_221159623"}, {"title": "Webis Data PAN-PC-11", "url": "https://webis.de/data/pan-pc-11.html"}, {"title": "PAN Plagiarism Corpus PAN-PC-09 | Request PDF", "url": "https://www.researchgate.net/publication/242823978_PAN_Plagiarism_Corpus_PAN-PC-09"}, {"title": "PAN Plagiarism Corpus 2011 (PAN-PC-11)", "url": "https://data.niaid.nih.gov/resources?id=zenodo_3250094"}, {"title": "ELG - PAN Plagiarism Corpus 2011 (PAN-PC-11)", "url": "https://live.european-language-grid.eu/catalogue/corpus/7529"}]}, "Based on the search results, here's what I found about the PAN-PC-11 plagiarism corpus and how to download it:\n\n## Overview\nThe PAN plagiarism corpus 2011 (PAN-PC-11) is a corpus for the evaluation of automatic plagiarism detection algorithms. For research purposes the corpus can be used free of charge.\n\n## Contents\nThe PAN-PC-11 contains documents in which plagiarism has been inserted automatically as well as documents in which plagiarism has been inserted manually, with the former constructed using a random plagiarist computer program and the latter obtained via Amazon's Mechanical Turk.\n\n## Official Download Location\nThe official download location for the PAN-PC-11 is on **Zenodo**: http://doi.org/10.5281/zenodo.3250095\n\nAlternatively, you can download the dataset from Zenodo via the Webis research group's data portal at webis.de."], "durationSeconds": 7.646086035999997, "searchCount": 1}
```

### [13] TOOL RESULT — WebSearch · 2026-07-03 17:50:10 UTC

```
{"query": "Wikipedia dataset download raw text 500 characters", "results": [{"tool_use_id": "srvtoolu_01FYwb6SHbKFbVSWDHq8Shc2", "content": [{"title": "Wikipedia:Database download - Wikipedia", "url": "https://en.wikipedia.org/wiki/Wikipedia:Database_download"}, {"title": "Wikipedia Plaintext (2023-07-01) | Kaggle", "url": "https://www.kaggle.com/datasets/jjinho/wikipedia-20230701"}, {"title": "Plain Text Wikipedia 2020-11", "url": "https://www.kaggle.com/datasets/ltcmdrdata/plain-text-wikipedia-202011"}, {"title": "Plaintext Wikipedia dump 2018 - Dataset - B2FIND", "url": "https://b2find.eudat.eu/dataset/3074cb26-6a0d-5803-8520-d0050a22c66e"}, {"title": "Plaintext Wikipedia (full English)", "url": "https://www.kaggle.com/datasets/ffatty/plaintext-wikipedia-full-english"}, {"title": "GitHub - GermanT5/wikipedia2corpus: Wikipedia text corpus for self-supervised NLP model training · GitHub", "url": "https://github.com/GermanT5/wikipedia2corpus"}]}, "Based on the search results, here are the main ways to download Wikipedia dataset as raw text:\n\n## Official Wikipedia Dumps\n\nWikipedia provides dumps in various formats, including all revisions or current revisions only. The multistream version (pages-articles-multistream.xml.bz2) is recommended because it allows you to extract an article without unpacking the entire archive.\n\n## Pre-processed Plaintext Datasets\n\nSeveral curated datasets are available on platforms like Kaggle:\n\n1. **Plaintext Wikipedia (Full English)** - Contains all 4,366,845 articles on the English Wikipedia. Articles are stripped of all Wiki formatting and concatenated into .txt files of ≤ 1MB each.\n\n2. **Plain Text Wikipedia 2020-11** - Includes ~40MB JSON files with Wikipedia articles containing an ID number, title, and plain text of the article.\n\n3. **Plaintext Wikipedia 2023-07-01** - Available on Kaggle for more recent data.\n\n## Processing Tools\n\nIf you prefer to process raw dumps yourself:\n- WikiExtractor is used to extract plaintext from Wikipedia dumps\n- The Wikipedia preprocessor (wikiprep.pl) is a Perl script that preprocesses raw XML dumps\n\nThe official source for raw dumps is https://dumps.wikimedia.org/."], "durationSeconds": 7.497616505000002, "searchCount": 1}
```

### [14] TOOL RESULT — WebSearch · 2026-07-03 17:50:14 UTC

```
{"query": "Shazam fingerprinting landmark pairs algorithm time delta", "results": [{"tool_use_id": "srvtoolu_01PXhkTmtBBiqYNGkQ4jLGEP", "content": [{"title": "GitHub - Sudo-3D/matlab-shazam-fingerprinting: Audio fingerprinting in MATLAB with algorithmic spectrogram peak-pair hashing — for music identification and song matching.", "url": "https://github.com/Sudo-3D/matlab-shazam-fingerprinting"}, {"title": "How do services like Shazam perform audio matching and search?", "url": "https://milvus.io/ai-quick-reference/how-do-services-like-shazam-perform-audio-matching-and-search"}, {"title": "TNShazam An FPGA Based Song Recognizer Eitan Kaplan Jose Rubianes", "url": "http://www.cs.columbia.edu/~sedwards/classes/2019/4840-spring/reports/TNShazam-presentation.pdf"}, {"title": "How does Shazam work? | ACRCloud Blog", "url": "https://blog.acrcloud.com/how-does-shazam-work"}, {"title": "abracadabra: How does Shazam work? - Cameron MacLeod", "url": "https://www.cameronmacleod.com/blog/how-does-shazam-work"}, {"title": "GitHub - BernardoOlisan/shazam-algorithm: Shazam's Clone Algorithm (From Scratch). An audio fingerprinting and recognition system built from scratch in C and Python, the same core algorithm behind Shazam. · GitHub", "url": "https://github.com/BernardoOlisan/shazam-algorithm"}, {"title": "A local fingerprinting approach for audio copy detection", "url": "https://arxiv.org/pdf/1304.0793"}, {"title": "Audio Fingerprinting. When I discovered Shazam had the… | by Shivam | Medium", "url": "https://medium.com/@shivam01110011/audio-fingerprinting-aee18fb88d4a"}, {"title": "Advancing Audio Fingerprinting Accuracy Addressing Background Noise and   Distortion Challenges", "url": "https://arxiv.org/pdf/2402.13957"}, {"title": "Digital Fingerprinting on Multimedia: A Survey", "url": "https://arxiv.org/pdf/2408.14155"}]}, "Based on the search results, here's information about Shazam's fingerprinting landmark pairs algorithm and time delta:\n\n## Overview\n\nKey points in the spectrogram, such as local maxima in specific frequency bands, are identified as \"landmarks.\" For example, a peak at 1 kHz occurring at 10 seconds might be paired with another peak at 2 kHz occurring 2 seconds later.\n\n## Landmark Pairs and Time Delta\n\nA hash is formed of two peaks, and the information that is recorded for each hash is the frequency of each peak, fA and fB, and the time delta between them, ΔT. Peaks are paired that are in close time-proximity to each other, and a fingerprint is formed from each pair by concatenating the frequency of each peak, and the time delta between them.\n\n## Hash Encoding\n\nPeak pairs are formed using a target zone (fan-out of up to 10 pairs per anchor) and encoded into 30-bit hashes: (f_anchor << 20) | (f_target << 10) | delta_t.\n\n## Matching Process\n\nFor every matching hash key, the system computes the absolute time-offset delay: ΔT_offset = t_database - t_query. A true match creates a sharp peak in the time-delay distribution, proving linear coherence even if the query starts mid-song."], "durationSeconds": 10.298611660999999, "searchCount": 1}
```

### [15] TOOL CALL — WebFetch · 2026-07-03 17:50:22 UTC

```
URL: https://webis.de/data/pan-pc-11.html
Prompt: What is the size, format, and how to download PAN-PC-11? What types of plagiarism cases does it contain (copypaste, paraphrase, near-copy)?
```

### [16] TOOL RESULT — WebFetch · 2026-07-03 17:50:22 UTC

```
{"bytes": 0, "code": 403, "codeText": "Forbidden", "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 329, "url": "https://webis.de/data/pan-pc-11.html"}
```

### [17] TOOL CALL — WebFetch · 2026-07-03 17:50:22 UTC

```
URL: https://zenodo.org/records/3250095
Prompt: What is the file format and size of PAN-PC-11? What metadata is available? How many documents and plagiarism cases?
```

### [18] TOOL RESULT — WebFetch · 2026-07-03 17:50:22 UTC

```
{"bytes": 81003, "code": 200, "codeText": "OK", "result": "# PAN-PC-11 Dataset Overview\n\n## File Format and Size\nThe corpus is distributed as two RAR archive files totaling **1.7 GB**:\n- Part 1: 1.0 GB\n- Part 2: 703.9 MB\n\n## Available Metadata\nThe page provides limited technical details. Key metadata elements include:\n- DOI: 10.5281/zenodo.3250095\n- Publication date: June 1, 2011\n- License: Creative Commons Attribution 4.0 International\n- Keywords: plagiarism, plagiarism detection, documents, PAN\n\n## Document and Plagiarism Case Count\nThe webpage does not specify the total number of documents or plagiarism cases contained in the corpus. The description only indicates that \"The PAN-PC-11 contains documents in which plagiarism has been inserted automatically as well as documents in which plagiarism has been inserted manually,\" but concrete statistics are absent from this page.\n\n**Note:** For detailed corpus composition information, you would need to consult the full corpus documentation or the referenced 2011 PAN workshop paper by Stein et al.", "durationMs": 4888, "url": "https://zenodo.org/records/3250095"}
```

### [19] TOOL CALL — WebSearch · 2026-07-03 17:50:26 UTC

```
PAN-PC-11 corpus 26939 documents 61064 plagiarism cases composition copypaste paraphrase
```

### [20] TOOL CALL — WebSearch · 2026-07-03 17:50:26 UTC

```
"winnowing" plagiarism detection algorithm Schleimer k-gram hashes
```

### [21] TOOL RESULT — WebSearch · 2026-07-03 17:50:34 UTC

```
{"query": "\"winnowing\" plagiarism detection algorithm Schleimer k-gram hashes", "results": [{"tool_use_id": "srvtoolu_01SnMDAPDL7gBxLqHAsamgXA", "content": [{"title": "Arabic-English Cross-language Plagiarism Detection using Winnowing Algorithm", "url": "https://scialert.net/fulltext/?doi=itj.2014.2349.2355"}, {"title": "A Plagiarism Detection Algorithm based on Extended ...", "url": "https://www.matec-conferences.org/articles/matecconf/pdf/2017/42/matecconf_eitce2017_02019.pdf"}, {"title": "Fingerprinting (hash-based methods) for plagiarism detection | Plagiarism Checker", "url": "https://www.plagiarismchecker.net/articles/fingerprinting-hash-based-methods-for-plagiarism-detection/"}, {"title": "Plagiarism Detection Using Manber and Winnowing ...", "url": "http://repository.uin-malang.ac.id/5641/1/5887.pdf"}, {"title": "(PDF) Detecting documents plagiarism using winnowing algorithm and k-gram method", "url": "https://www.researchgate.net/publication/323713099_Detecting_documents_plagiarism_using_winnowing_algorithm_and_k-gram_method"}, {"title": "(PDF) Winnowing: Local Algorithms for Document Fingerprinting", "url": "https://www.researchgate.net/publication/2840981_Winnowing_Local_Algorithms_for_Document_Fingerprinting"}, {"title": "How winnowing fingerprints work | Viper Blog", "url": "https://blog.scanmyessay.com/lexical-and-fingerprinting-algorithms/how-winnowing-fingerprints-work/"}, {"title": "Efficient and Scalable Provenance Tracking for LLM-Generated Code Snippets", "url": "https://arxiv.org/pdf/2605.28510"}, {"title": "Different Spirals of Sameness: A Study of Content Sharing in Mainstream   and Alternative Media", "url": "https://arxiv.org/pdf/1904.01534"}]}, "I found comprehensive information about the winnowing plagiarism detection algorithm. Here are the key findings:\n\n## Overview\n\nThe Winnowing algorithm is a fingerprint-based text similarity detection method, proposed by Schleimer et al. in 2003. The basic idea of Winnowing comes from the Karp-Rabin algorithm which uses overlapping k-gram and moving window for string matching.\n\n## How It Works\n\nWinnowing works by sliding a fixed-size window over the sequence of hash values and, for each window, selecting the minimum hash value in that window as a fingerprint. For example, if using a window of size w hashes, then among each group of w consecutive k-gram hashes, the smallest (or sometimes the rightmost smallest) hash is chosen.\n\nThe algorithm begins with code canonicalization, wherein comments, whitespace, and other non-essential tokens are removed to produce a normalized representation. The canonicalized code is segmented into overlapping k-grams (sequences of k characters), each of which is hashed. A sliding window of size w is then applied over the hash sequence, and the minimum hash value in each window is retained as a fingerprint. This guarantees that any matching substring will produce at least one common fingerprint between two documents.\n\n## Advantages and Applications\n\nWinnowing is a lightweight and flexible similarity detection method, it is robust for sentence and text block rearrangement, and the influence of interference words can be effectively reduced through reasonable parameter setting.\n\nTwenty-three years after the SIGMOD paper, winnowing remains the workhorse of lexical similarity detection. It is what MOSS uses for code; it is what most academic plagiarism detectors use under the hood for text; it is what git uses (with some adaptation) for similarity-based rename detection; it is the backbone of rsync-style delta compression, and it appears throughout near-duplicate detection on the web."], "durationSeconds": 8.868423206, "searchCount": 1}
```

### [22] TOOL RESULT — WebSearch · 2026-07-03 17:50:34 UTC

```
{"query": "PAN-PC-11 corpus 26939 documents 61064 plagiarism cases composition copypaste paraphrase", "results": [{"tool_use_id": "srvtoolu_01KAwMyW6b767xRjgrVdyVhC", "content": [{"title": "PAN Plagiarism Corpus 2011 (PAN-PC-11)", "url": "https://zenodo.org/records/3250095"}, {"title": "PAN Plagiarism Corpus 2011 (PAN-PC-11) | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/PAN-Plagiarism-Corpus-2011-(PAN-PC-11)-Potthast-Stein/507aa7ff1ab234d64d8a9c0cac99a3213cb53834"}, {"title": "Webis Data PAN-PC-11", "url": "https://webis.de/data/pan-pc-11.html"}, {"title": "Corpus statistics for 26 939 documents and 61 064 plagiarism cases in... | Download Table", "url": "https://www.researchgate.net/figure/Corpus-statistics-for-26-939-documents-and-61-064-plagiarism-cases-in-the-PAN-PC-11_tbl1_221159623"}, {"title": "Dataset Search - PAN Plagiarism Corpus 2011 (PAN-PC-11)", "url": "https://toolbox.google.com/datasetsearch/search?query=pan-pc-11"}, {"title": "An external plagiarism detection system based on part-of-speech (POS) tag n-grams and word embedding - ScienceDirect", "url": "https://www.sciencedirect.com/science/article/abs/pii/S0957417422001610"}, {"title": "Detecting Cross-Language Plagiarism using Open Knowledge Graphs", "url": "https://arxiv.org/pdf/2111.09749"}, {"title": "Automatic Detection of Plagiarism in Writing", "url": "https://files.eric.ed.gov/fulltext/EJ1340053.pdf"}, {"title": "PAN Plagiarism Corpus 2011 (PAN-PC-11)", "url": "https://data.niaid.nih.gov/resources?id=zenodo_3250094"}, {"title": "ELG - PAN Plagiarism Corpus 2011 (PAN-PC-11)", "url": "https://live.european-language-grid.eu/catalogue/corpus/7529"}]}, "Based on the search results, here's what I found about the PAN-PC-11 corpus:\n\nThe PAN plagiarism corpus 2011 (PAN-PC-11) is a corpus for the evaluation of automatic plagiarism detection algorithms. The corpus contains 26,939 documents, which matches the number you mentioned.\n\nThe PAN-PC-11 contains documents in which plagiarism has been inserted automatically as well as documents in which plagiarism has been inserted manually. The former have been constructed using a so-called random plagiarist, a computer program which constructs plagiarism according to a number of parameters, while the latter have been obtained with crowdsourcing via Amazon's Mechanical Turk.\n\nRegarding the composition of plagiarism types, the corpora have a variety of plagiarism types (verbatim, paraphrased, and independently written) created artificially and manually. Paraphrasing generation in the corpus is divided into two categories: artificial and simulated. Artificial cases have been generated automatically by a computer program using semantic word replacements and POS preserving word shuffling. In comparison, simulated cases have been generated manually using Amazon Mechanical Turk.\n\nThe search results reference the 26,939 documents you mentioned, though I found a direct reference to corpus statistics mentioning both the document count and 61,064 plagiarism cases in a table on ResearchGate, but detailed breakdown of the specific composition wasn't fully available in the search results."], "durationSeconds": 9.390889753999996, "searchCount": 1}
```

### [23] TOOL CALL — WebSearch · 2026-07-03 17:50:38 UTC

```
MinHash LSH near-duplicate detection Broder Jaccard similarity
```

### [24] TOOL CALL — WebSearch · 2026-07-03 17:50:38 UTC

```
SimHash web dedup Charikar cosine similarity bit vector
```

### [25] TOOL RESULT — WebSearch · 2026-07-03 17:50:44 UTC

```
{"query": "MinHash LSH near-duplicate detection Broder Jaccard similarity", "results": [{"tool_use_id": "srvtoolu_01RG1h4t5BsQn1XEjkTKqpFX", "content": [{"title": "ProbMinHash A Class of Locality-Sensitive Hash Algorithms for the (Probability) Jaccard Similarity", "url": "https://www.researchgate.net/publication/344143059_ProbMinHash_A_Class_of_Locality-Sensitive_Hash_Algorithms_for_the_Probability_Jaccard_Similarity"}, {"title": "MinHash: Jaccard Similarity, LSH, and Near-Duplicate Detection - Interactive | Michael Brenndoerfer | Michael Brenndoerfer", "url": "https://mbrenndoerfer.com/writing/minhash-algorithm-jaccard-similarity-lsh-deduplication"}, {"title": "MINHASH_LSH | Milvus Documentation", "url": "https://milvus.io/docs/minhash-lsh.md"}, {"title": "MinHash — Grokipedia", "url": "https://grokipedia.com/page/MinHash"}, {"title": "A Filter of Minhash for Image Similarity Measures", "url": "https://arxiv.org/pdf/1807.02895"}, {"title": "MinHash LSH in Milvus: The Secret Weapon for Fighting Duplicates in LLM Training Data - Milvus Blog", "url": "https://milvus.io/blog/minhash-lsh-in-milvus-the-secret-weapon-for-fighting-duplicates-in-llm-training-data.md"}, {"title": "Towards EnergyGPT: A Large Language Model Specialized for the Energy Sector", "url": "https://arxiv.org/pdf/2509.07177"}, {"title": "Set Similarity Search Beyond MinHash", "url": "https://arxiv.org/pdf/1612.07710"}, {"title": "Real-Time Community Detection in Large Social Networks on a Laptop", "url": "https://arxiv.org/pdf/1601.03958"}, {"title": "MinHash - Wikipedia", "url": "https://en.wikipedia.org/wiki/MinHash"}]}, "Here are the web search results for your query on MinHash, LSH, near-duplicate detection, and Jaccard similarity:\n\n## Key Findings\n\n**MinHash Overview:**\nMinHash is a technique for quickly estimating how similar two sets are. It's a probabilistic algorithm for efficiently estimating Jaccard similarity between large sets by generating compact signatures through random permutations or hash functions to identify minimum values.\n\n**Historical Context:**\nThe scheme was published by Andrei Broder in a 1997 conference and initially used in the AltaVista search engine to detect duplicate web pages.\n\n**Application to Near-Duplicate Detection:**\nMinHash is an algorithm that makes near-duplicate detection tractable at scale by compressing each document into a compact numerical signature, such that the probability of two signatures agreeing on any position equals the Jaccard similarity of the original documents.\n\n**LSH Integration:**\nWith an extension called Locality Sensitive Hashing (LSH), you can find all near-duplicate pairs in a large corpus without comparing every pair, reducing what would be a quadratic-time problem to something approaching linear time in practice. When combined with MinHash signatures, LSH enables the detection of near-duplicate sets or documents without exhaustively computing pairwise similarities.\n\n**Practical Use:**\nMinHash-based Jaccard similarity provides an efficient way to detect near-duplicate documents in large text corpora."], "durationSeconds": 7.670122001999997, "searchCount": 1}
```

### [26] TOOL RESULT — WebSearch · 2026-07-03 17:50:46 UTC

```
{"query": "SimHash web dedup Charikar cosine similarity bit vector", "results": [{"tool_use_id": "srvtoolu_01LF8fofpxBDB7e2p7rsU8Uk", "content": [{"title": "Speeding up SimHash by 10x using a bit hack", "url": "https://www.dynatrace.com/news/blog/speeding-up-simhash-by-10x/"}, {"title": "SimHash — Grokipedia", "url": "https://grokipedia.com/page/SimHash"}, {"title": "A New Unbiased and Efficient Class of LSH-Based Samplers and Estimators   for Partition Function Computation in Log-Linear Models", "url": "https://arxiv.org/pdf/1703.05160"}, {"title": "DotHash: Estimating Set Similarity Metrics for Link Prediction and   Document Deduplication", "url": "https://arxiv.org/pdf/2305.17310"}, {"title": "Near Duplicate Detection Using Simhash | Sumon Biswas", "url": "https://sumonbis.github.io/academic-project/simhash/"}, {"title": "Determining similarity of linguistic objects", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9298757"}, {"title": "SimKey: A Semantically Aware Key Module for Watermarking Language Models", "url": "https://arxiv.org/pdf/2510.12828"}, {"title": "Near Duplicate Detection Using Simhash", "url": "https://github.com/sumonbis/NearDuplicateDetection"}, {"title": "Sub-Linear Privacy-Preserving Near-Neighbor Search", "url": "https://arxiv.org/pdf/1612.01835"}, {"title": "Multi-reference Cosine: A New Approach to Text Similarity Measurement in   Large Collections", "url": "https://arxiv.org/pdf/1810.03099"}]}, "Here are the search results for your query about SimHash, web deduplication, Charikar's cosine similarity, and bit vectors:\n\n## Key Findings\n\n**SimHash Overview:**\nSimHash is a locality-sensitive hashing technique introduced by Moses Charikar in 2002 that generates compact binary fingerprints for high-dimensional data, such as text documents, enabling efficient detection of near-duplicates by ensuring similar inputs produce fingerprints with small Hamming distances.\n\n**How It Works:**\nFor each bit position across all features, the method computes a weighted sum where the feature's weight is added if the corresponding hash bit is 1 or subtracted if 0; the final fingerprint bit is set to 1 if this sum is positive and 0 otherwise, effectively approximating cosine similarity through random projections.\n\n**Cosine Similarity Connection:**\nThe collision probability for a single bit is roughly a function of the cosine similarity with a value range between 50% and 100%. By considering only the precalculated fingerprints, the cosine similarity between corresponding sets can be quickly estimated from the fraction of equal bits which allows accelerating tasks such as searching or grouping similar sets.\n\n**Web Deduplication Applications:**\nThis algorithm has good precision and recall and has been used as a near-duplication detection method in real-world problems in search engines like Google.\n\nThe search results contain comprehensive information about SimHash's mathematical foundations, implementation details, and practical applications in near-duplicate detection for web documents."], "durationSeconds": 10.328964978999997, "searchCount": 1}
```

### [27] ASSISTANT · 2026-07-03 17:51:07 UTC

```
Now I have enough concrete information to write a detailed, actionable plan. Let me create the JSON output.
```

### [28] TOOL CALL — Write · 2026-07-03 17:51:07 UTC

```
File: /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.terminal_claude_agent_struct_out.json

{
  "title": "PAN-PC-11 & synthetic structural-edit benchmark",
  "summary": "Acquire PAN-PC-11 plagiarism corpus (26,939 documents, 61,064 plagiarism cases) and create a synthetic benchmark of 500 Wikipedia passages with 5 structural-edit variants each (prepending/appending boilerplate, mid-passage insertion/deletion, combinations). Standardize both to JSON schema with metadata, validate, and split into full/mini/preview variants for rapid testing.",
  "runpod_compute_profile": "cpu_heavy",
  "ideal_dataset_criteria": "Real dataset: PAN-PC-11 must include copypaste, near-copy, and paraphrase cases; Wikipedia passages must be >500 characters to ensure sufficient content for meaningful structural edits. Synthetic variants must systematically vary edit type (prepend 0–500 chars, append 0–500 chars, insert 1–3 random sentences, delete 1–3 random sentences, combinations) with paired negative examples (5–10 unrelated passages per canonical). Final schema: JSON rows with {passage_id, original_text, variant_id, variant_text, edit_type, is_near_duplicate, fold}.",
  "dataset_search_plan": "STEP 1: Acquire PAN-PC-11. Download from Zenodo (DOI 10.5281/zenodo.3250095) — 1.7 GB RAR archive (2 parts). Extract XML files. Parse document-level source/suspicious pairs, plagiarism type annotations (copypaste, simulated-paraphrase, artificial-paraphrase). Keep raw text from all three plagiarism categories. Size: 26,939 documents, 61,064 plagiarism cases across copypaste, artificial paraphrase, and simulated paraphrase.\n\nSTEP 2: Acquire Wikipedia base passages. Download plaintext Wikipedia dump (Kaggle or dumps.wikimedia.org, e.g., 2023-07-01 version or latest). Extract articles as raw text. Filter to passages >500 characters to ensure sufficient content for structural edits. Target ~500 passages covering diverse topics (science, history, biography, arts). Standardize encoding to UTF-8, strip Wiki markup if needed.\n\nSTEP 3: Extract PAN-PC-11 cases. For each of the three plagiarism types (copypaste, artificial-paraphrase, simulated-paraphrase), extract source-suspicious pairs. Tokenize and standardize to UTF-8. Sample 100–200 copypaste cases, 100–200 near-copy cases (artificial paraphrase with <30% token divergence), 50–100 paraphrase cases (simulated paraphrase) for balanced representation. Validate each pair is extractable (both source and plagiarized text present, >100 characters).\n\nSTEP 4: Generate synthetic structural-edit variants. For each of 500 Wikipedia passages, create 5 structural-edit variants: (1) 0–500 char random boilerplate prepended; (2) 0–500 char random boilerplate appended; (3) 1–3 random sentences from unrelated passages inserted mid-passage; (4) 1–3 random sentences randomly deleted from passage; (5) combination of 2+ edits (prepend+insert OR append+delete). Use simple random text generators or other passages for boilerplate injection. Vary edit magnitudes uniformly across 0–500 chars and 1–3 insertions/deletions per variant.\n\nSTEP 5: Generate negative examples. For each canonical passage (Wikipedia or PAN source), create 5–10 random negative pairs: unrelated passages of similar length (±30% character count) from the corpus that are NOT near-duplicates. Ensure negatives are truly disjoint (different source, no textual overlap >50 characters).\n\nSTEP 6: Standardize to JSON schema. For PAN-PC-11 cases and synthetic variants, produce rows: {passage_id (str), original_text (str, >100 chars), variant_id (str), variant_text (str), edit_type (str: 'copypaste'|'artificial_paraphrase'|'simulated_paraphrase'|'prepend_boilerplate'|'append_boilerplate'|'insert_sentences'|'delete_sentences'|'combination'), is_near_duplicate (bool), source (str: 'pan_pc_11'|'wikipedia'), fold (str: 'train'|'val'|'test')}. ALL rows must be valid UTF-8, no null fields, passage_id globally unique.\n\nSTEP 7: Validate schema. Load all rows, confirm 100% compliance: all required fields present, types match, no malformed text, passage lengths reasonable (>100 chars). Report row counts per edit_type and source. Catch data integrity issues before handoff.\n\nSTEP 8: Create preview, mini, and full variants. (a) PREVIEW: 20 rows (4 per edit_type for Wikipedia, 2 per plagiarism_type for PAN) for rapid dev testing. (b) MINI: 500 rows (~250 Wikipedia, ~250 PAN) for iteration 2 fast runs. (c) FULL: All rows (~1000–1500 total) for final benchmark. All three variants share the same schema and are disjoint (no row overlap between preview/mini/full).\n\nSTEP 9: Write data_out.json. Output FULL variant as primary artifact; include metadata: {num_rows, num_wikipedia_passages, num_pan_cases, edit_type_distribution, source_distribution, char_length_stats, fold_split}.",
  "target_num_datasets": 1
}
```

### [29] TOOL RESULT — Write · 2026-07-03 17:51:07 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"PAN-PC-11 & synthetic structural-edit benchmark\",\n  \"summary\": \"Acquire PAN-PC-11 plagiarism corpus (26,939 documents, 61,064 plagiarism cases) and create a synthetic benchmark of 500 Wikipedia passages with 5 structural-edit variants each (prepending/appending boilerplate, mid-passage insertion/deletion, combinations). Standardize both to JSON schema with metadata, validate, and split into full/mini/preview variants for rapid testing.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"ideal_dataset_criteria\": \"Real dataset: PAN-PC-11 must include copypaste, near-copy, and paraphrase cases; Wikipedia passages must be >500 characters to ensure sufficient content for meaningful structural edits. Synthetic variants must systematically vary edit type (prepend 0–500 chars, append 0–500 chars, insert 1–3 random sentences, delete 1–3 random sentences, combinations) with paired negative examples (5–10 unrelated passages per canonical). Final schema: JSON rows with {passage_id, original_text, variant_id, variant_text, edit_type, is_near_duplicate, fold}.\",\n  \"dataset_search_plan\": \"STEP 1: Acquire PAN-PC-11. Download from Zenodo (DOI 10.5281/zenodo.3250095) — 1.7 GB RAR archive (2 parts). Extract XML files. Parse document-level source/suspicious pairs, plagiarism type annotations (copypaste, simulated-paraphrase, artificial-paraphrase). Keep raw text from all three plagiarism categories. Size: 26,939 documents, 61,064 plagiarism cases across copypaste, artificial paraphrase, and simulated paraphrase.\\n\\nSTEP 2: Acquire Wikipedia base passages. Download plaintext Wikipedia dump (Kaggle or dumps.wikimedia.org, e.g., 2023-07-01 version or latest). Extract articles as raw text. Filter to passages >500 characters to ensure sufficient content for structural edits. Target ~500 passages covering diverse topics (science, history, biography, arts). Standardize encoding to UTF-8, strip Wiki markup if needed.\\n\\nSTEP 3: Extract PAN-PC-11 cases. For each of the three plagiarism types (copypaste, artificial-paraphrase, simulated-paraphrase), extract source-suspicious pairs. Tokenize and standardize to UTF-8. Sample 100–200 copypaste cases, 100–200 near-copy cases (artificial paraphrase with <30% token divergence), 50–100 paraphrase cases (simulated paraphrase) for balanced representation. Validate each pair is extractable (both source and plagiarized text present, >100 characters).\\n\\nSTEP 4: Generate synthetic structural-edit variants. For each of 500 Wikipedia passages, create 5 structural-edit variants: (1) 0–500 char random boilerplate prepended; (2) 0–500 char random boilerplate appended; (3) 1–3 random sentences from unrelated passages inserted mid-passage; (4) 1–3 random sentences randomly deleted from passage; (5) combination of 2+ edits (prepend+insert OR append+delete). Use simple random text generators or other passages for boilerplate injection. Vary edit magnitudes uniformly across 0–500 chars and 1–3 insertions/deletions per variant.\\n\\nSTEP 5: Generate negative examples. For each canonical passage (Wikipedia or PAN source), create 5–10 random negative pairs: unrelated passages of similar length (±30% character count) from the corpus that are NOT near-duplicates. Ensure negatives are truly disjoint (different source, no textual overlap >50 characters).\\n\\nSTEP 6: Standardize to JSON schema. For PAN-PC-11 cases and synthetic variants, produce rows: {passage_id (str), original_text (str, >100 chars), variant_id (str), variant_text (str), edit_type (str: 'copypaste'|'artificial_paraphrase'|'simulated_paraphrase'|'prepend_boilerplate'|'append_boilerplate'|'insert_sentences'|'delete_sentences'|'combination'), is_near_duplicate (bool), source (str: 'pan_pc_11'|'wikipedia'), fold (str: 'train'|'val'|'test')}. ALL rows must be valid UTF-8, no null fields, passage_id globally unique.\\n\\nSTEP 7: Validate schema. Load all rows, confirm 100% compliance: all required fields present, types match, no malformed text, passage lengths reasonable (>100 chars). Report row counts per edit_type and source. Catch data integrity issues before handoff.\\n\\nSTEP 8: Create preview, mini, and full variants. (a) PREVIEW: 20 rows (4 per edit_type for Wikipedia, 2 per plagiarism_type for PAN) for rapid dev testing. (b) MINI: 500 rows (~250 Wikipedia, ~250 PAN) for iteration 2 fast runs. (c) FULL: All rows (~1000–1500 total) for final benchmark. All three variants share the same schema and are disjoint (no row overlap between preview/mini/full).\\n\\nSTEP 9: Write data_out.json. Output FULL variant as primary artifact; include metadata: {num_rows, num_wikipedia_passages, num_pan_cases, edit_type_distribution, source_distribution, char_length_stats, fold_split}.\",\n  \"target_num_datasets\": 1\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [30] ASSISTANT · 2026-07-03 17:51:15 UTC

```
Perfect! I've created a detailed, actionable plan for the dataset artifact. Let me summarize what the plan delivers:

## Plan Summary

**Artifact:** A combined benchmark dataset (PAN-PC-11 plagiarism corpus + synthetic Wikipedia structural-edit variants)

**Key Components:**

1. **PAN-PC-11 Acquisition** — Download 1.7 GB corpus (26,939 documents, 61,064 plagiarism cases) from Zenodo. Extract three plagiarism types: copypaste, artificial paraphrase, simulated paraphrase.

2. **Wikipedia Base Passages** — Download plaintext Wikipedia dump, filter to 500 passages >500 characters for sufficient content to meaningfully apply structural edits.

3. **Synthetic Variants** — Systematically generate 5 structural-edit variants per Wikipedia passage:
   - Prepend/append 0–500 char boilerplate
   - Insert/delete 1–3 random sentences mid-passage
   - Combinations of the above
   - Paired with 5–10 negative examples per passage

4. **Standardized JSON Schema** — Unified format: `{passage_id, original_text, variant_id, variant_text, edit_type, is_near_duplicate, source, fold}` with UTF-8 validation, schema compliance checks, and integrity guarantees.

5. **Splits for Scalability** — Three variants delivered:
   - **PREVIEW** (20 rows) — rapid dev testing
   - **MINI** (500 rows) — fast iteration 2 runs
   - **FULL** (1000–1500 rows) — complete benchmark

6. **Validation & Metadata** — Full schema validation, distribution statistics per edit_type and source, character-length stats, fold assignments.

The plan is concrete, specific, and respects the 6-hour executor time budget by:
- Using publicly available, well-documented sources (Zenodo, Kaggle)
- Avoiding complex preprocessing (simple UTF-8 standardization, no neural embeddings)
- Enabling rapid testing with preview/mini splits
- Specifying exact JSON schema upfront to avoid rework

Sources:
- [PAN-PC-11 on Zenodo](https://zenodo.org/records/3250095)
- [Wikipedia Database Download](https://en.wikipedia.org/wiki/Wikipedia:Database_download)
- [Plaintext Wikipedia on Kaggle](https://www.kaggle.com/datasets/jjinho/wikipedia-20230701)
- [Shazam Audio Fingerprinting](https://milvus.io/ai-quick-reference/how-do-services-like-shazam-perform-audio-matching-and-search)
- [MinHash & LSH Overview](https://mbrenndoerfer.com/writing/minhash-algorithm-jaccard-similarity-lsh-deduplication)
- [SimHash Web Dedup](https://grokipedia.com/page/SimHash)
```
