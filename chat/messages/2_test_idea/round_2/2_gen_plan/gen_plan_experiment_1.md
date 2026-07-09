# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_Bd0c_4hy9OC-` — Near Duplicate Detection
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-haiku-4-5)

### [1] CONFIG · 2026-07-03 18:13:12 UTC

```
model: claude-haiku-4-5 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1
```

### [2] SYSTEM-USER prompt · 2026-07-03 18:13:20 UTC

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
You are expanding an artifact direction of type: EXPERIMENT

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance
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

The experiment executor has 6h total (including writing code, debugging, testing, and fixing errors).

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
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-multi-llm-agents** — Guide for implementing Multi-LLM Agent Systems research using Mirascope orchestration, HuggingFace datasets/evaluation, and proven multi-agent patterns.
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter2_dir1
type: experiment
objective: >-
  Implement landmark-pair fingerprinting algorithm and benchmark against MinHash (Jaccard), MinHash Containment, and SimHash
  on both GLUE MRPC and real structural-edit datasets with consistent precision@recall metrics and statistical ablation validation.
approach: >-
  Implement landmark extraction: (1) TF-IDF sliding-window saliency computation via sklearn/gensim, (2) 2D local maxima detection
  using scipy.ndimage.maximum_filter over (position, n-gram) matrix (clarify dimensionality: operate on position×hashed-ngram-id
  buckets, not full vocabulary), (3) sparse landmark selection (top-k% by TF-IDF score, k=10-15%). Implement landmark-pair
  hashing: (1) for each anchor landmark, enumerate target landmarks within lookahead window W (20-50 tokens), (2) emit hash(n-gram_a,
  n-gram_b, quantized_position_delta) using hashlib, (3) collect all hashes as fingerprint. Implement baselines: MinHash (Jaccard,
  100-200 hash functions) and MinHash Containment (|A∩B|/|A|, using datasketch.MinHashLSHEnsemble), SimHash (64-bit via random
  hyperplanes). Run on: (1) GLUE MRPC (use art__yFeBexgqp0M from iter_1), (2) real structural-edit benchmark (from new DATASET
  artifact). PRIMARY METRIC: recall@precision≥0.90 for all methods on both benchmarks (consistent with standard near-duplicate
  detection). Ablations: (1) with vs without positional offset in hash (two-proportion z-test, α=0.05), (2) vary landmark
  density (5%, 10%, 15%, 20%), (3) vary lookahead window W (10, 20, 50 tokens). Timing: query latency per method on 1M-passage
  corpus, throughput (queries/sec), 95th-percentile latency. Document exact threshold T used for each method. Output method_out.json
  containing: tables with precision@recall=0.90 for both benchmarks, precision-recall curves as JSON arrays, ablation results
  with p-values and 95% CIs, timing benchmarks, and implementation details (parameter values, hash function, neighborhood
  size for 2D filter).
depends_on:
- id: art__yFeBexgqp0M
  label: baseline paraphrase dataset
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
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
  "description": "Plan for an EXPERIMENT artifact.",
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
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-07-03 18:13:20 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [4] ASSISTANT · 2026-07-03 18:13:30 UTC

```
I'll research the technical landscape for near-duplicate detection baselines and then write a detailed, actionable plan for implementing landmark-pair fingerprinting.
```

### [5] TOOL CALL — Skill · 2026-07-03 18:13:30 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-07-03 18:13:30 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — Skill · 2026-07-03 18:13:30 UTC

```
aii-web-tools
```

### [8] TOOL RESULT — Skill · 2026-07-03 18:13:30 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [9] TOOL CALL — Skill · 2026-07-03 18:13:30 UTC

```
aii-web-tools
```

### [10] TOOL RESULT — Skill · 2026-07-03 18:13:30 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [11] TOOL CALL — Skill · 2026-07-03 18:13:30 UTC

```
aii-web-tools
```

### [12] TOOL RESULT — Skill · 2026-07-03 18:13:30 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [13] ASSISTANT · 2026-07-03 18:13:34 UTC

```
Let me load the built-in web tools first:
```

### [14] TOOL CALL — ToolSearch · 2026-07-03 18:13:34 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 2}
```

### [15] TOOL RESULT — ToolSearch · 2026-07-03 18:13:34 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 21}
```

### [16] TOOL CALL — WebSearch · 2026-07-03 18:13:36 UTC

```
datasketch Python library MinHash Containment LSHEnsemble documentation
```

### [17] TOOL CALL — WebSearch · 2026-07-03 18:13:36 UTC

```
Shazam audio fingerprinting algorithm anchor target frequency delta time
```

### [18] TOOL CALL — WebSearch · 2026-07-03 18:13:36 UTC

```
Winnowing algorithm Schleimer SIGMOD 2003 text fingerprinting sliding window
```

### [19] TOOL CALL — WebSearch · 2026-07-03 18:13:36 UTC

```
SimHash Python implementation TF-IDF hyperplane hashing bit vectors
```

### [20] TOOL RESULT — WebSearch · 2026-07-03 18:13:42 UTC

```
{"query": "datasketch Python library MinHash Containment LSHEnsemble documentation", "results": [{"tool_use_id": "srvtoolu_01CYzWDiBC6kJcCDc4swgV65", "content": [{"title": "MinHash LSH Ensemble — datasketch 1.10.0 documentation", "url": "https://ekzhu.com/datasketch/lshensemble.html"}, {"title": "GitHub - ekzhu/datasketch: MinHash, LSH, LSH Forest, Weighted MinHash, HyperLogLog, HyperLogLog++, LSH Ensemble and HNSW · GitHub", "url": "https://github.com/ekzhu/datasketch"}, {"title": "datasketch · PyPI", "url": "https://pypi.org/project/datasketch/"}, {"title": "MinHash LSH — datasketch 1.10.0 documentation", "url": "https://ekzhu.com/datasketch/lsh.html"}, {"title": "datasketch.lshensemble — datasketch 1.9.0 documentation", "url": "http://ekzhu.com/datasketch/_modules/datasketch/lshensemble.html"}, {"title": "datasketch/docs/lshensemble.rst at master · ekzhu/datasketch", "url": "https://github.com/ekzhu/datasketch/blob/master/docs/lshensemble.rst"}, {"title": "datasketch/datasketch/lshensemble.py at master · ekzhu/datasketch", "url": "https://github.com/ekzhu/datasketch/blob/master/datasketch/lshensemble.py"}, {"title": "datasketch/datasketch/lsh.py at master · ekzhu/datasketch", "url": "https://github.com/ekzhu/datasketch/blob/master/datasketch/lsh.py"}, {"title": "How to use the datasketch.lsh.MinHashLSH function in datasketch | Snyk", "url": "https://snyk.io/advisor/python/datasketch/functions/datasketch.lsh.MinHashLSH"}, {"title": "MinHash — datasketch 1.10.0 documentation", "url": "https://ekzhu.com/datasketch/minhash.html"}]}, "I found comprehensive documentation about the datasketch Python library with information on MinHash, Containment, and LSHEnsemble. Here's a summary of the key findings:\n\n## Overview\n\ndatasketch gives you probabilistic data structures that can process and search very large amount of data super fast, with little loss of accuracy.\n\n## MinHash\n\ndatasketch.MinHash lets you estimate the Jaccard similarity (resemblance) between sets of arbitrary sizes in linear time using a small and fixed memory space. It can also be used to compute Jaccard similarity between data streams.\n\n## Containment\n\nContainment is computed as the intersection size divided by the size of one of the set, and the containment threshold can be easily deduced from the intersection threshold by multiplying |Q|.\n\n## LSH Ensemble\n\nThere is an LSH index for containment search -- given a query set, find sets with containment above a certain threshold. It is LSH Ensemble by E. Zhu et al. This package implements a slightly simplified version of the index, :class:`datasketch.MinHashLSHEnsemble`.\n\nThe official documentation is available at:\n- **Main documentation**: https://ekzhu.com/datasketch/\n- **LSHEnsemble documentation**: https://ekzhu.com/datasketch/lshensemble.html\n- **GitHub repository**: https://github.com/ekzhu/datasketch\n- **PyPI package page**: https://pypi.org/project/datasketch/"], "durationSeconds": 6.1226888069999985, "searchCount": 1}
```

### [21] TOOL RESULT — WebSearch · 2026-07-03 18:13:44 UTC

```
{"query": "Shazam audio fingerprinting algorithm anchor target frequency delta time", "results": [{"tool_use_id": "srvtoolu_01SJ7HKLEyEPVSSu3XquYpKj", "content": [{"title": "Audio Fingerprinting. When I discovered Shazam had the… | by Shivam | Medium", "url": "https://medium.com/@shivam01110011/audio-fingerprinting-aee18fb88d4a"}, {"title": "GitHub - BernardoOlisan/shazam-algorithm: Shazam's Clone Algorithm (From Scratch). An audio fingerprinting and recognition system built from scratch in C and Python, the same core algorithm behind Shazam. · GitHub", "url": "https://github.com/BernardoOlisan/shazam-algorithm"}, {"title": "How The Heck Does Shazam Work? (An Interactive Exploration)", "url": "https://perthirtysix.com/how-the-heck-does-shazam-work"}, {"title": "The Five-Second Fingerprint: Inside Shazam’s Instant Song ID | Towards Data Science", "url": "https://towardsdatascience.com/the-five-second-fingerprint-inside-shazams-instant-song-id/"}, {"title": "abracadabra: How does Shazam work? - Cameron MacLeod", "url": "https://www.cameronmacleod.com/blog/how-does-shazam-work"}, {"title": "How Shazam Works. Shazam allows you to send a recording… | by Trey Cooper | Medium", "url": "https://medium.com/@treycoopermusic/how-shazam-works-d97135fb4582"}, {"title": "I Built the Shazam Algorithm from Scratch in Go — and It Actually Works | by Daniel Olowoniyi | Medium", "url": "https://danztee.medium.com/i-built-the-shazam-algorithm-from-scratch-in-go-and-it-actually-works-041beb16258e"}, {"title": "Digital Fingerprinting on Multimedia: A Survey", "url": "https://arxiv.org/pdf/2408.14155"}, {"title": "A local fingerprinting approach for audio copy detection", "url": "https://arxiv.org/pdf/1304.0793"}, {"title": "How does the Shazam app recognize music? An explanation of music recognition technology used in the Shazam app | TechAhead", "url": "https://www.techaheadcorp.com/blog/decoding-shazam-how-does-music-recognition-work-with-shazam-app/"}]}, "Based on the search results, here's what I found about Shazam's audio fingerprinting algorithm:\n\n## Core Hashing Structure\n\nFrom each anchor-target pair, a hash tuple is derived: [f1, f2, t], where f1 is the anchor's frequency bin, f2 is the target's frequency bin and t is the time gap between anchor and target peaks. This approach is also described in more technical terms: Peak pairs are encoded into 30-bit hashes: (f_anchor << 20) | (f_target << 10) | delta_t.\n\n## Algorithm Process\n\nThe algorithm gives every peak a turn as an anchor, and for each one, it defines a target zone to its right (a window of time and frequency) and pairs the anchor with every peak inside that zone. Shazam's key insight is that only a small number of high-energy frequency peaks are needed to uniquely identify a song.\n\n## Advantages of the Approach\n\nThis representation captures a local spectral relationship that is both distinctive (likely unique to a song) and invariant to small temporal shifts, which makes it resilient against minor edits or noise in the query signal.\n\n## Robustness\n\nThe extracted fingerprints are shown to be highly robust to audio compression, foreground noises, and other types of noise, however, they are not robust to tempo changes or pitch shifts."], "durationSeconds": 7.429953041000001, "searchCount": 1}
```

### [22] TOOL RESULT — WebSearch · 2026-07-03 18:13:44 UTC

```
{"query": "SimHash Python implementation TF-IDF hyperplane hashing bit vectors", "results": [{"tool_use_id": "srvtoolu_01QCNSN5Uo8uYroEFsAHyckt", "content": [{"title": "GitHub - hybridtheory/floc-simhash: A fast python implementation of the SimHash algorithm.", "url": "https://github.com/hybridtheory/floc-simhash"}, {"title": "floc-simhash · PyPI", "url": "https://pypi.org/project/floc-simhash/"}, {"title": "Hashing documents during the Cookiepocalypse // Alberto Cámara", "url": "https://ber2.github.io/posts/simhash/"}, {"title": "SimHash — Grokipedia", "url": "https://grokipedia.com/page/SimHash"}, {"title": "Real-Time Tf-Idf Clustering Using Simhash, Approximate Nearest", "url": "https://dash.harvard.edu/server/api/core/bitstreams/030cf124-530c-4df5-a228-0fd180899d00/content"}, {"title": "Locality Sensitive Hashing (LSH) - Aerodata - WordPress.com", "url": "https://aerodatablog.wordpress.com/2017/11/29/locality-sensitive-hashing-lsh/"}, {"title": "Simhash Algorithm Explained - kiwirafe.blog", "url": "https://kiwirafe.github.io/en/simhash-tutorial-1/"}, {"title": "What is SimHash? - DEV Community", "url": "https://dev.to/lovestaco/what-is-simhash-58m5"}, {"title": "Determining similarity of linguistic objects", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9298757"}, {"title": "Unnatural Language Processing: Bridging the Gap Between Synthetic and   Natural Language Data", "url": "https://arxiv.org/pdf/2004.13645"}]}, "Based on the search results, here's comprehensive information about SimHash Python implementation using TF-IDF and hyperplane hashing:\n\n## Overview\n\nSimHash is a fast Python implementation of the SimHash algorithm, which is a type of locality-sensitive hashing initially introduced for detecting near-duplicate documents.\n\n## How It Works\n\nThe SimHash algorithm operates through the following process:\n\nThe p-bit SimHash algorithm works by choosing p random unit vectors in feature space, which determine p hyperplanes passing through origin by relating each hyperplane to its normal vector, and these p hyperplanes determine a partition of space into 2^p regions. The choice of a random unit vector is equivalent to choosing a random hyperplane in feature space, and choosing p random hyperplanes partitions the feature space into 2^p regions.\n\n## Vector Representation and TF-IDF\n\nTo compute a SimHash fingerprint, the input data such as a text document is first preprocessed into a set of features represented as a high-dimensional vector, typically involving extracting shingles or individual terms, with each unique feature assigned a weight based on its TF-IDF value within the document corpus.\n\nTwo vectorizations are discussed in the whitepaper: one-hot and tf-idf; they are available in scikit-learn, and the SimHashTransformer supplies a transformer that can be used directly on the output of these vectorizers in order to obtain hashes.\n\n## Python Implementation\n\nThe package requires python>=3.7 and provides two main classes: SimHash, applying the SimHash algorithm on the md5 hashes of tokens in the given document, and SimHashTransformer, applying the SimHash algorithm to a document vectorization as part of a scikit-learn pipeline.\n\nThe **floc-simhash** package is available on PyPI and provides practical implementations for document hashing with TF-IDF weighting."], "durationSeconds": 8.202324292999998, "searchCount": 1}
```

### [23] TOOL RESULT — WebSearch · 2026-07-03 18:13:44 UTC

```
{"query": "Winnowing algorithm Schleimer SIGMOD 2003 text fingerprinting sliding window", "results": [{"tool_use_id": "srvtoolu_01Gh5jr6jjv4pyNPVyoVGhkp", "content": [{"title": "Digital Fingerprinting on Multimedia: A Survey", "url": "https://arxiv.org/pdf/2408.14155"}, {"title": "Fingerprinting (hash-based methods) for plagiarism detection | Plagiarism Checker", "url": "https://www.plagiarismchecker.net/articles/fingerprinting-hash-based-methods-for-plagiarism-detection/"}, {"title": "[PDF] Winnowing: local algorithms for document fingerprinting | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/Winnowing:-local-algorithms-for-document-Schleimer-Wilkerson/73acc491ec7eb8f0a29e0f06397cb517b79e658b"}, {"title": "Schleimer, S., Wilkerson, D. and Aiken, A. (2003) Winnowing Local Algorithms for Document Fingerprinting. SIGMOD 2003, San Diego, 9-12 June 2003, 76-85. - References - Scientific Research Publishing", "url": "https://www.scirp.org/reference/referencespapers?referenceid=1192464"}, {"title": "BibSLEIGH — Winnowing: Local Algorithms for Document Fingerprinting", "url": "http://bibtex.github.io/SIGMOD-2003-SchleimerWA.html"}, {"title": "Winnowing: local algorithms for document fingerprinting", "url": "https://bibbase.org/network/publication/schleimer-wilkerson-aiken-winnowinglocalalgorithmsfordocumentfingerprinting-2003"}, {"title": "(PDF) Winnowing: Local Algorithms for Document Fingerprinting", "url": "https://www.researchgate.net/publication/2840981_Winnowing_Local_Algorithms_for_Document_Fingerprinting"}, {"title": "Automatic Tracing in Task-Based Runtime Systems", "url": "https://arxiv.org/pdf/2406.18111"}, {"title": "‪Winnowing: local algorithms for document fingerprinting‬", "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=3vKjkoQAAAAJ&citation_for_view=3vKjkoQAAAAJ:u5HHmVD_uO8C"}]}, "Here are the search results for the Winnowing algorithm by Schleimer et al. from SIGMOD 2003:\n\n## Overview\n\nThe paper \"Winnowing: Local Algorithms for Document Fingerprinting\" was published in the 2003 ACM SIGMOD International Conference on Management of Data, pages 76-85. The authors are Saul Schleimer, Daniel Shawcross Wilkerson, and Alexander Aiken.\n\n## Algorithm Description\n\nThe Winnowing algorithm is used for text similarity comparison and deduplication. It works by sliding a fixed-size window over the sequence of hash values and, for each window, selecting the minimum hash value in that window as a fingerprint.\n\nBased on the Rabin algorithm, the Winnowing algorithm adds a denoising function. In the sliding window selection process, Winnowing only retains the fragments with the minimum hash value and discards the other fragments to remove interfering characters, which greatly reduces the size of the text representation while retaining fragments related to the key information.\n\n## Research Contributions\n\nThe paper introduces the class of local document fingerprinting algorithms and proves a novel lower bound on the performance of any local algorithm, showing that winnowing's performance is within 33% of the lower bound.\n\n## Impact and Extensions\n\nThe winnowing algorithm has become a standard for document fingerprinting. The algorithm has inspired various extensions, including frequency-biased winnowing (FBW) and modified frequency-biased winnowing (MFBW) for improved text reuse detection."], "durationSeconds": 8.490428603, "searchCount": 1}
```

### [24] TOOL CALL — WebFetch · 2026-07-03 18:13:48 UTC

```
URL: https://ekzhu.com/datasketch/lshensemble.html
Prompt: What is the API for MinHashLSHEnsemble? How do you initialize it, add items, and query for containment? What parameters are needed?
```

### [25] TOOL CALL — WebFetch · 2026-07-03 18:13:48 UTC

```
URL: https://perthirtysix.com/how-the-heck-does-shazam-work
Prompt: What is the exact process for creating anchor-target pairs in Shazam? What are the frequency range and time delta constraints?
```

### [26] TOOL RESULT — WebFetch · 2026-07-03 18:13:48 UTC

```
{"bytes": 0, "code": 403, "codeText": "Forbidden", "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 295, "url": "https://perthirtysix.com/how-the-heck-does-shazam-work"}
```

### [27] TOOL RESULT — WebFetch · 2026-07-03 18:13:52 UTC

```
{"bytes": 18830, "code": 200, "codeText": "OK", "result": "# MinHashLSHEnsemble API Overview\n\nBased on the documentation, here's how to use MinHashLSHEnsemble:\n\n## Initialization\n\nCreate an instance with: `\"MinHashLSHEnsemble(threshold=0.8, num_perm=128, num_part=32)\"`\n\nKey parameters include:\n- **threshold**: The containment similarity threshold for matching\n- **num_perm**: Number of permutations (128 or higher)\n- **num_part**: Number of partitions (affects precision and query time)\n\n## Adding Items\n\nUse the `index()` method with an iterable of tuples containing `(key, minhash, size)`:\n- **key**: Identifier for the set\n- **minhash**: MinHash sketch of the set\n- **size**: Cardinality of the original set\n\n## Querying\n\nCall `query(minhash, size)` with your query's MinHash sketch and size. This returns an iterator of matching keys where the containment exceeds your threshold.\n\n## Example Flow\n\nCreate MinHash objects for your sets, initialize the ensemble with desired parameters, index your collection using the index method, then query using the query method to find sets meeting your containment threshold.\n\nThe documentation notes that precision increases with more partitions, though this impacts query time accordingly.", "durationMs": 3910, "url": "https://ekzhu.com/datasketch/lshensemble.html"}
```

### [28] ASSISTANT · 2026-07-03 18:14:02 UTC

```
Let me try an alternative source for Shazam details:
```

### [29] TOOL CALL — WebFetch · 2026-07-03 18:14:02 UTC

```
URL: https://medium.com/@shivam01110011/audio-fingerprinting-aee18fb88d4a
Prompt: Describe the Shazam algorithm step by step. What are anchor peaks and target peaks? What is the time delta window? How are the hashes constructed?
```

### [30] TOOL RESULT — WebFetch · 2026-07-03 18:14:02 UTC

```
{"bytes": 134007, "code": 200, "codeText": "OK", "result": "# The Shazam Audio Fingerprinting Algorithm\n\n## Overview\nShazam identifies songs by extracting compact acoustic representations called fingerprints and matching them against a database.\n\n## Step-by-Step Process\n\n**1. Spectrogram Creation**\nAudio is converted to a spectrogram using Short-Time Fourier Transform (STFT), which visualizes \"the strength of the frequencies present in the different timestamps.\"\n\n**2. Peak Detection**\nLocal maxima are identified in the spectrogram to create a \"constellation map\" of high-energy points. Two parameters control this:\n- **Minimum distance**: Prevents clustering of nearby peaks\n- **Relative threshold**: Suppresses low-energy noise by only detecting peaks \"that exceed a certain fraction of the global maximum\"\n\n## Hash Construction via Anchor-Target Pairs\n\n**Anchor Peaks**: The prominent spectral peaks selected from the constellation map serve as reference points.\n\n**Target Peaks**: Other nearby peaks within a defined region relative to each anchor. The \"target zone\" is bounded by:\n- Maximum time difference (temporal reach)\n- Frequency bounds (pitch range)\n- Fan-out limit (number of targets per anchor)\n\n**Hash Creation**: Each anchor-target pair generates a hash tuple [f1, f2, t], where:\n- **f1** = anchor's frequency bin\n- **f2** = target's frequency bin  \n- **t** = time gap between the peaks\n\nThis representation captures \"local spectral relationship[s]\" that are distinctive yet resilient to minor edits or noise.\n\n## Query Matching\nThe query song undergoes the same process, and its hashes are compared against the database. Songs with the most matching hashes are returned as results.", "durationMs": 6265, "url": "https://medium.com/@shivam01110011/audio-fingerprinting-aee18fb88d4a"}
```

### [31] ASSISTANT · 2026-07-03 18:14:04 UTC

```
Perfect. Now let me check the GLUE MRPC dataset structure from the dependency:
```

### [32] TOOL CALL — Read · 2026-07-03 18:14:04 UTC

```
/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/mini_data_out.json
```

### [33] TOOL RESULT — Read · 2026-07-03 18:14:04 UTC

```
{"type": "text", "file": {"filePath": "/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/mini_data_out.json", "content": "{\n  \"metadata\": {\n    \"description\": \"GLUE MRPC (Microsoft Research Paraphrase Corpus) for MinHash near-duplicate detection evaluation. Sentence pairs labeled 1=paraphrase (near-duplicate, high lexical overlap) or 0=non-paraphrase.\",\n    \"dataset\": \"glue_mrpc\",\n    \"source\": \"nyu-mll/glue config=mrpc (Dolan & Brockett 2005; GLUE benchmark Wang et al. 2019)\",\n    \"num_rows\": 4076,\n    \"positive_rate\": 0.675,\n    \"relevance\": \"Paraphrase pairs share high n-gram overlap — direct MinHash/Jaccard evaluation signal\"\n  },\n  \"datasets\": [\n    {\n      \"dataset\": \"glue_mrpc\",\n      \"examples\": [\n        {\n          \"input\": \"{\\\"sentence1\\\": \\\"Amrozi accused his brother , whom he called \\\\\\\" the witness \\\\\\\" , of deliberately distorting his evidence .\\\", \\\"sentence2\\\": \\\"Referring to him as only \\\\\\\" the witness \\\\\\\" , Amrozi accused his brother of deliberately distorting his evidence .\\\"}\",\n          \"output\": \"1\",\n          \"metadata_label_meaning\": \"1=paraphrase(near-duplicate) 0=non-paraphrase\",\n          \"metadata_row_index\": 0,\n          \"metadata_task_type\": \"binary_classification\",\n          \"metadata_source\": \"glue_mrpc\"\n        },\n        {\n          \"input\": \"{\\\"sentence1\\\": \\\"Yucaipa owned Dominick 's before selling the chain to Safeway in 1998 for $ 2.5 billion .\\\", \\\"sentence2\\\": \\\"Yucaipa bought Dominick 's in 1995 for $ 693 million and sold it to Safeway for $ 1.8 billion in 1998 .\\\"}\",\n          \"output\": \"0\",\n          \"metadata_label_meaning\": \"1=paraphrase(near-duplicate) 0=non-paraphrase\",\n          \"metadata_row_index\": 1,\n          \"metadata_task_type\": \"binary_classification\",\n          \"metadata_source\": \"glue_mrpc\"\n        },\n        {\n          \"input\": \"{\\\"sentence1\\\": \\\"They had published an advertisement on the Internet on June 10 , offering the cargo for sale , he added .\\\", \\\"sentence2\\\": \\\"On June 10 , the ship 's owners had published an advertisement on the Internet , offering the explosives for sale .\\\"}\",\n          \"output\": \"1\",\n          \"metadata_label_meaning\": \"1=paraphrase(near-duplicate) 0=non-paraphrase\",\n          \"metadata_row_index\": 2,\n          \"metadata_task_type\": \"binary_classification\",\n          \"metadata_source\": \"glue_mrpc\"\n        }\n      ]\n    }\n  ]\n}", "numLines": 41, "startLine": 1, "totalLines": 41}}
```

### [34] ASSISTANT · 2026-07-03 18:15:02 UTC

```
Excellent. Now I have enough technical context to write a comprehensive plan. Let me create the detailed plan:
```

### [35] TOOL CALL — Write · 2026-07-03 18:15:02 UTC

```
File: /tmp/claude-0/-ai-inventor-aii-data-runs-run-Bd0c-4hy9OC--3-invention-loop-iter-2-gen-plan-gen-plan-experiment-1/ec85b06d-1dc6-4a51-95d4-7adb77569d91/scratchpad/.terminal_claude_agent_struct_out.json

{
  "title": "Landmark-Pair Fingerprinting vs MinHash/SimHash",
  "summary": "Implement landmark-pair text fingerprinting (inspired by Shazam's audio hashing), benchmark against MinHash Jaccard, MinHash Containment, and SimHash on GLUE MRPC and synthetic structural-edit test sets. Validate that positional offsets between salient n-gram pairs outperform global statistics for near-duplicate detection.",
  "runpod_compute_profile": "cpu_heavy",
  "implementation_pseudocode": "# PHASE 1: DATA PREPARATION\n1. Load GLUE MRPC from art__yFeBexgqp0M dependency (full_data_out.json)\n   - Parse JSON pairs: sentence1, sentence2, label\n   - Create synthetic structural-edit variants:\n     a) Prepend random sentences (50, 100, 200 tokens)\n     b) Append random sentences (50, 100, 200 tokens)\n     c) Insert sentences mid-paragraph (at 25%, 50%, 75% positions)\n     d) Reorder paragraphs (swap adjacent sentences within pairs)\n   - Store as (id, text, edit_type, original_pair_id, label) tuples\n   - Target: 500-1000 synthetic variants + 4076 MRPC originals\n\n# PHASE 2: LANDMARK EXTRACTION (Core Innovation)\n2. Implement landmark extraction for each passage:\n   a) Tokenize text into words (or 5-8 char n-grams)\n   b) Compute sliding-window TF-IDF:\n      - Build corpus-level IDF via sklearn.feature_extraction.text.TfidfVectorizer\n      - For each token position, compute local TF-IDF score (via gensim or sklearn)\n        using a 5-10 word sliding window (NOT over full doc)\n      - Output: position -> local_tfidf_score matrix\n   c) Find 2D local maxima using scipy.ndimage.maximum_filter:\n      - Apply 2D filter over (position, token_id_hash) sparse matrix\n      - Window size: ~3 positions x ~50 token buckets\n      - Threshold: Keep landmarks in top 10-15% by score within window\n   d) Output: list of (position, token/ngram, tfidf_score) landmarks\n   e) Store top-K landmarks (K=10-30 per passage, configurable)\n\n# PHASE 3: FINGERPRINT GENERATION\n3. Landmark-pair hashing (Shazam-inspired):\n   a) For each anchor landmark (pos_a, token_a, score_a):\n      - Define lookahead window W in tokens (e.g., W=20, 50)\n      - Enumerate all target landmarks (pos_t, token_t, score_t) where:\n        pos_a < pos_t <= pos_a + W\n      - For each (anchor, target) pair:\n        delta = pos_t - pos_a (relative positional offset, quantized to nearest 5 tokens)\n        hash_val = hash(token_a, token_t, delta) using hashlib.sha256 or xxhash\n        Emit (hash_val, delta) as single fingerprint entry\n   b) Fingerprint FP = set of all hash tuples for passage\n   c) Implement variant (ablation): FP_no_delta = set of hash(token_a, token_t) (no offset)\n   d) Output: FP, FP_no_delta, stats (|FP|, landmark_count, density)\n\n# PHASE 4: BASELINE IMPLEMENTATIONS\n4. MinHash Jaccard (using datasketch):\n   a) Tokenize text into 5-8 char shingles\n   b) Create MinHash(num_perm=128) for each passage\n   c) Store MinHash objects in dict keyed by passage_id\n\n5. MinHash Containment (using datasketch.MinHashLSHEnsemble):\n   a) Initialize MinHashLSHEnsemble(threshold=0.5, num_perm=128, num_part=32)\n   b) Index all passages: index([(id, minhash_obj, shingle_count)])\n   c) Query: query(minhash_query, shingle_count_query) -> candidates\n\n6. SimHash (using floc-simhash or custom implementation):\n   a) Extract TF-IDF vector for passage (sklearn TfidfVectorizer)\n   b) Project onto 64 random hyperplanes\n   c) Create 64-bit hash (bit_i = 1 if dot(tfidf_vec, random_vector_i) > 0)\n   d) Store bit-vector for each passage\n\n# PHASE 5: SIMILARITY COMPUTATION\n7. Compute pairwise similarity for all methods on test set:\n   a) Landmark-pair: Jaccard(FP1, FP2) = |FP1 ∩ FP2| / |FP1 ∪ FP2|\n   b) MinHash Jaccard: Use datasketch MinHash.jaccard() directly\n   c) MinHash Containment: Use LSHEnsemble query; compute |intersection| / |query|\n   d) SimHash: Hamming distance between bit-vectors / 64 (normalized)\n   e) Store similarity matrix for downstream metric computation\n\n# PHASE 6: EVALUATION METRICS\n8. Precision-recall curves at fixed thresholds:\n   a) For each method, sweep threshold from 0.0 to 1.0 in steps of 0.05\n   b) For each threshold:\n      - True positives: (pair, label=1, similarity >= threshold)\n      - False positives: (pair, label=0, similarity >= threshold)\n      - True negatives: (pair, label=0, similarity < threshold)\n      - False negatives: (pair, label=1, similarity < threshold)\n      - Compute: precision = TP / (TP + FP), recall = TP / (TP + FN)\n   c) PRIMARY METRIC: Recall at precision >= 0.90 for both MRPC and synthetic benchmarks\n   d) Secondary metrics:\n      - F1 at optimal threshold\n      - Area under PR curve (AP)\n      - Threshold T for each method (the value used)\n\n# PHASE 7: ABLATIONS & STATISTICAL TESTING\n9. Ablation 1 - Positional offset significance:\n   a) Run full pipeline for FP (with delta) and FP_no_delta (without delta)\n   b) Compute precision@recall=0.90 for both\n   c) Two-proportion z-test: H0: p_with = p_without (α=0.05)\n   d) Report: z-statistic, p-value, 95% CI for difference\n   e) Interpret: Offset must show statistically significant improvement\n\n10. Ablation 2 - Landmark density:\n    a) Re-run landmark extraction with K ∈ {5, 10, 15, 20, 30}\n    b) Compute fingerprints and precision@recall for each K\n    c) Plot: K vs recall@prec>=0.90 (sensitivity to density)\n    d) Report: Optimal K value and diminishing returns threshold\n\n11. Ablation 3 - Lookahead window W:\n    a) Re-run landmark-pair hashing with W ∈ {10, 20, 50, 100}\n    b) Compute precision@recall for each W\n    c) Plot: W vs recall@prec>=0.90 (sensitivity to structural scope)\n    d) Interpret: Larger W should handle greater reordering but reduce distinctiveness\n\n# PHASE 8: PERFORMANCE BENCHMARKING\n12. Query latency and throughput:\n    a) Create 1M-passage synthetic corpus (random Wikipedia subset)\n    b) Index all passages with all 4 methods\n    c) Draw 1000 random query passages\n    d) Measure per-method:\n      - Query latency (ms per query): median, 95th percentile\n      - Index memory footprint (MB)\n      - Throughput (queries/sec)\n      - Indexing time (minutes)\n    e) Report: Timing as table with method comparison\n\n# PHASE 9: OUTPUT GENERATION\n13. Write method_out.json with structure:\n    {\n      \"metadata\": {\n        \"objective\": \"Benchmark landmark-pair fingerprinting vs MinHash/SimHash\",\n        \"timestamp\": ISO8601,\n        \"run_id\": extracted from workspace_path\n      },\n      \"datasets\": [\n        {\n          \"name\": \"GLUE_MRPC\",\n          \"num_pairs\": 4076,\n          \"num_positive\": 2753,\n          \"num_negative\": 1323,\n          \"results\": {\n            \"landmark_pair\": {\n              \"threshold_at_prec90\": 0.XX,\n              \"recall_at_prec90\": 0.XX,\n              \"precision_at_recall90\": 0.XX,\n              \"f1_optimal\": 0.XX,\n              \"auc_pr\": 0.XX,\n              \"precision_recall_curve\": [[th, prec, recall], ...],\n              \"avg_fingerprint_size\": 150\n            },\n            \"minHash_jaccard\": {...},\n            \"minHash_containment\": {...},\n            \"simhash\": {...}\n          }\n        },\n        {\n          \"name\": \"Synthetic_Structural_Edits\",\n          \"num_pairs\": 1000,\n          \"edit_types\": [\"prepend\", \"append\", \"insert\", \"reorder\"],\n          \"results\": {...similar structure...}\n        }\n      ],\n      \"ablations\": {\n        \"positional_offset\": {\n          \"with_delta_recall_prec90\": 0.XX,\n          \"without_delta_recall_prec90\": 0.XX,\n          \"z_statistic\": 2.34,\n          \"p_value\": 0.019,\n          \"ci_95_difference\": [0.05, 0.25],\n          \"verdict\": \"SIGNIFICANT\" or \"NOT_SIGNIFICANT\"\n        },\n        \"landmark_density\": {\n          \"by_k\": {\n            \"k=5\": {\"recall_prec90\": 0.XX, \"avg_landmarks_per_passage\": 5},\n            \"k=10\": {...},\n            \"k=15\": {...},\n            \"k=20\": {...},\n            \"k=30\": {...}\n          }\n        },\n        \"lookahead_window\": {\n          \"by_w\": {\n            \"w=10\": {\"recall_prec90\": 0.XX, \"avg_fp_size\": 120},\n            \"w=20\": {...},\n            \"w=50\": {...},\n            \"w=100\": {...}\n          }\n        }\n      },\n      \"timing\": {\n        \"index_method\": \"All methods indexed on 1M synthetic corpus\",\n        \"by_method\": {\n          \"landmark_pair\": {\n            \"indexing_time_minutes\": 12.5,\n            \"index_memory_mb\": 850,\n            \"median_query_latency_ms\": 2.3,\n            \"p95_query_latency_ms\": 8.7,\n            \"throughput_queries_sec\": 435\n          },\n          \"minHash_jaccard\": {...},\n          \"minHash_containment\": {...},\n          \"simhash\": {...}\n        }\n      },\n      \"implementation_details\": {\n        \"landmark_extraction\": {\n          \"method\": \"scipy.ndimage.maximum_filter over (position, token_id) sparse matrix\",\n          \"filter_window_size\": [3, 50],\n          \"percentile_threshold\": 85,\n          \"sample_landmarks_per_passage\": [5, 10, 15, 20, 30]\n        },\n        \"landmark_pair_hashing\": {\n          \"hash_function\": \"hashlib.sha256 -> first 32 bits\",\n          \"lookahead_windows\": [10, 20, 50, 100],\n          \"delta_quantization\": \"nearest 5 tokens\",\n          \"ablations_run\": [\"with_delta\", \"without_delta\"]\n        },\n        \"baselines\": {\n          \"minHash_jaccard\": {\n            \"library\": \"datasketch\",\n            \"num_permutations\": 128,\n            \"shingle_size\": \"5-8 char\"\n          },\n          \"minHash_containment\": {\n            \"library\": \"datasketch.MinHashLSHEnsemble\",\n            \"threshold\": 0.5,\n            \"num_perm\": 128,\n            \"num_part\": 32\n          },\n          \"simhash\": {\n            \"method\": \"Custom or floc-simhash\",\n            \"bit_width\": 64,\n            \"vectorizer\": \"sklearn TfidfVectorizer\"\n          }\n        }\n      },\n      \"key_findings\": {\n        \"landmark_pair_beats_containment\": true or false,\n        \"recall_delta_vs_containment_percentage_points\": 8.3,\n        \"positional_offset_is_load_bearing\": true or false,\n        \"best_landmark_density_k\": 15,\n        \"best_lookahead_window_w\": 20,\n        \"verdict\": \"CONFIRM\" or \"PARTIAL\" or \"DISCONFIRM\"\n      }\n    }\n\n# PHASE 10: VALIDATION & ERROR HANDLING\n14. Validation checkpoints:\n    a) After landmark extraction: Assert >=5 landmarks per passage on avg\n    b) After fingerprinting: Assert |FP| in expected range (100-2000 hashes)\n    c) After baseline computation: Assert all similarity scores in [0, 1]\n    d) After metric computation: Assert precision + 1-recall >= 0 (no impossible curves)\n    e) Write validation_log.txt with pass/fail for each check",
  "fallback_plan": "# Fallback 1: If scipy.ndimage.maximum_filter causes memory issues\n- Instead of 2D sparse matrix, use 1D sliding window over position sequence\n- For each position window [i, i+K], find max TF-IDF token -> landmark\n- Simpler, memory-light, trades some locality for tractability\n- Landmark quality may decrease slightly but method remains viable\n\n# Fallback 2: If landmark-pair fingerprinting is too dense (>5000 hashes/doc)\n- Reduce lookahead window W from 50 to 20 tokens\n- Increase landmark density threshold (keep top-10% instead of top-15%)\n- Sample landmark pairs probabilistically (if >1000, keep 1000 random pairs)\n- This preserves method while limiting computation\n\n# Fallback 3: If MinHashLSHEnsemble indexing fails or is too slow\n- Use datasketch.MinHash with brute-force pairwise comparison\n- Trade O(n) indexing for O(n^2) query cost\n- Still valid baseline; just slower on 1M corpus\n- Fall back to 10k corpus instead of 1M for timing benchmarks\n\n# Fallback 4: If SimHash implementation unavailable or slow\n- Use a simpler bit-vector hash: hash first N tokens deterministically\n- Not ideal but provides a lightweight baseline for comparison\n\n# Fallback 5: If statistical significance test fails (e.g., perfect separation)\n- Report effect size (Cohen's h) instead of p-value\n- Use bootstrap CI instead of exact two-proportion z-test\n- Acknowledge ceiling/floor effects in ablation section\n\n# Fallback 6: If synthetic structural-edit generation is too slow\n- Use pre-made plagiarism datasets (PAN-PC-11 if available)\n- Or generate only 200-300 synthetic variants instead of 1000\n- Primary evaluation remains on GLUE MRPC (4076 pairs)\n\n# Fallback 7: If timing benchmark on 1M corpus exceeds time budget\n- Benchmark on 100k corpus instead\n- Scale up projections (multiply latencies by ~10x, memory by ~100x)\n- Focus on relative comparison (landmark-pair vs baselines) not absolute numbers",
  "testing_plan": "# PHASE 1: UNIT TESTS (First 30 minutes, before full run)\n1. Test landmark extraction:\n   - Load mini_data_out.json (3 examples from dependency)\n   - Extract landmarks from each sentence pair\n   - Assert: >=1 landmark per passage, landmarks in range [0, len(text)]\n   - Manually verify top landmark is plausibly a salient token (not common word)\n   - Output: landmark_extraction_unit_test.log\n\n2. Test fingerprint generation:\n   - Create 5-word synthetic passage: \"the quick brown fox jumps\"\n   - Manually compute expected landmark pairs\n   - Run algorithm, compare against manual expectation\n   - Assert: Fingerprint size matches manual pair count\n   - Test with/without positional offset variants\n   - Output: fingerprint_generation_unit_test.log\n\n3. Test baseline implementations:\n   a) MinHash: Create two identical 10-word passages\n     - Assert: jaccard(M1, M1) == 1.0 (identity check)\n   b) MinHash: Create two disjoint 10-word passages\n     - Assert: jaccard(M1, M2) close to 0 (disjoint check)\n   c) MinHash Containment: Query subset against superset\n     - Assert: containment(subset, superset) > 0.5\n   d) SimHash: Two identical passages\n     - Assert: Hamming(H1, H1) == 0\n   - Output: baseline_unit_tests.log\n\n4. Test evaluation metrics:\n   - Create mock similarity scores and labels\n   - Compute precision-recall curve\n   - Assert: At threshold=1.0, precision=1.0 (or NaN if no positive predictions)\n   - Assert: At threshold=0.0, recall=1.0\n   - Assert: Precision + (1-recall) >= 0 for all points\n   - Output: metric_validation.log\n\n# PHASE 2: MINI DATA TEST (30-60 minutes, full pipeline on 3 examples)\n5. Run full pipeline on mini_data_out.json only:\n   - All 4 methods on 3 MRPC pairs\n   - Compute similarities and metrics\n   - Manually verify a few scores make intuitive sense\n   - Expected: Should complete in <5 minutes, no crashes\n   - Output: mini_pipeline_results.json (same schema as method_out.json but tiny)\n\n6. Verify mini results:\n   - Check that landmark-pair and minHash both have results\n   - Check that similarity scores are in [0, 1]\n   - Check that precision-recall curve has >=3 points\n   - If landmark-pair scores are all identical or all zero -> debug landmark extraction\n   - Output: mini_validation_report.txt\n\n# PHASE 3: PREVIEW DATA TEST (1-2 hours, full pipeline on ~400 pairs)\n7. Run full pipeline on first 400 MRPC pairs (\"preview scale\"):\n   - Build TF-IDF corpus on these 400\n   - Extract landmarks, compute fingerprints, index baselines\n   - Compute all metrics and ablations (K=5,10,15; W=10,20,50)\n   - Expected time: ~30-60 minutes depending on compute\n   - Output: preview_results.json (complete schema, representatively small dataset)\n\n8. Validation checks on preview results:\n   a) Landmark counts:\n      - Average landmarks per passage: should be K +/- 2 (e.g., 15±2)\n      - Assert no passage has 0 landmarks\n   b) Fingerprint sizes:\n      - Average |FP|: should scale as ~K^2 / 2 (O(quadratic) in landmark count)\n      - Landmark-pair FP should be 2-5x larger than MinHash (100s vs 100-200 hashes)\n   c) Similarity distributions:\n      - Plot histogram of similarities for each method\n      - Landmark-pair should show clear bimodal (high for paraphrases, low for non-paraphrases)\n      - If distribution is uniform -> method not working\n   d) Ablation results:\n      - Recall@prec>=0.90 should increase monotonically with K (or plateau)\n      - Without-delta should have lower precision@recall than with-delta\n      - If opposite, landmark extraction or hashing is broken\n   e) Statistical test:\n      - Two-proportion z-test should yield p < 0.05 if delta is significant\n      - If p > 0.5, offset is NOT load-bearing -> hypothesis challenge\n   - Output: preview_validation_report.txt\n\n# PHASE 4: DECISION CHECKPOINT\n9. Decision: Should proceed to full dataset?\n   If ANY of the following:\n   - Unit tests FAIL -> Debug landmark extraction / fingerprinting\n   - Mini pipeline doesn't complete -> Fix crashes before scaling\n   - Mini results are nonsensical (all zeros, random) -> Rethink approach\n   - Ablation fails to show significance -> Revisit hypothesis\n   Otherwise: PROCEED to full data\n\n# PHASE 5: FULL DATA RUN (2-3 hours remaining)\n10. Run full pipeline on all GLUE MRPC + synthetic structural edits:\n    - Load all 4076 MRPC pairs\n    - Generate 500-1000 synthetic variants with edits\n    - Extract landmarks, fingerprint, compute all metrics\n    - Expected time: 90-180 minutes depending on optimization\n    - Output: method_out.json with final results\n\n# PHASE 6: FINAL VALIDATION\n11. Sanity checks on final results:\n    - Landmark-pair recall@prec>=0.90 should be >= 0.5 (at least half of true paraphrases)\n    - If < 0.3, hypothesis is weak; if > 0.95, possible overfitting on MRPC\n    - Containment MinHash recall should be > 0.4 (it's a strong baseline)\n    - Landmark-pair should beat or match containment (or document why it doesn't)\n    - Synthetic dataset should show larger recall gains vs MRPC\n      (landmark-pair designed for structural edits, should shine here)\n    - If synthetic results are worse than MRPC, structural-edit generation may be flawed\n    - Output: final_validation_report.txt\n\n# PHASE 7: VERIFICATION OF HYPOTHESIS VERDICT\n12. Determine CONFIRM / PARTIAL / DISCONFIRM:\n    - CONFIRM: landmark-pair recall@prec>=0.90 >= containment recall + 10pp on structural edits\n      AND positional offset ablation is significant (p<0.05)\n      AND timing is <10x slower than MinHash\n    - PARTIAL: Gains only on structural edits, not MRPC\n      OR Gains <5pp (lower than expected 10-15pp)\n      OR Statistical significance marginal (p close to 0.05)\n    - DISCONFIRM: landmark-pair <= containment baseline on both datasets\n      OR Inverted-index lookup >10x slower than MinHash\n      OR Cannot extract stable landmarks (too much variance across texts)\n    - Output: verdict.txt with final interpretation"
}
```

### [36] TOOL RESULT — Write · 2026-07-03 18:15:02 UTC

```
{"type": "create", "filePath": "/tmp/claude-0/-ai-inventor-aii-data-runs-run-Bd0c-4hy9OC--3-invention-loop-iter-2-gen-plan-gen-plan-experiment-1/ec85b06d-1dc6-4a51-95d4-7adb77569d91/scratchpad/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Landmark-Pair Fingerprinting vs MinHash/SimHash\",\n  \"summary\": \"Implement landmark-pair text fingerprinting (inspired by Shazam's audio hashing), benchmark against MinHash Jaccard, MinHash Containment, and SimHash on GLUE MRPC and synthetic structural-edit test sets. Validate that positional offsets between salient n-gram pairs outperform global statistics for near-duplicate detection.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"implementation_pseudocode\": \"# PHASE 1: DATA PREPARATION\\n1. Load GLUE MRPC from art__yFeBexgqp0M dependency (full_data_out.json)\\n   - Parse JSON pairs: sentence1, sentence2, label\\n   - Create synthetic structural-edit variants:\\n     a) Prepend random sentences (50, 100, 200 tokens)\\n     b) Append random sentences (50, 100, 200 tokens)\\n     c) Insert sentences mid-paragraph (at 25%, 50%, 75% positions)\\n     d) Reorder paragraphs (swap adjacent sentences within pairs)\\n   - Store as (id, text, edit_type, original_pair_id, label) tuples\\n   - Target: 500-1000 synthetic variants + 4076 MRPC originals\\n\\n# PHASE 2: LANDMARK EXTRACTION (Core Innovation)\\n2. Implement landmark extraction for each passage:\\n   a) Tokenize text into words (or 5-8 char n-grams)\\n   b) Compute sliding-window TF-IDF:\\n      - Build corpus-level IDF via sklearn.feature_extraction.text.TfidfVectorizer\\n      - For each token position, compute local TF-IDF score (via gensim or sklearn)\\n        using a 5-10 word sliding window (NOT over full doc)\\n      - Output: position -> local_tfidf_score matrix\\n   c) Find 2D local maxima using scipy.ndimage.maximum_filter:\\n      - Apply 2D filter over (position, token_id_hash) sparse matrix\\n      - Window size: ~3 positions x ~50 token buckets\\n      - Threshold: Keep landmarks in top 10-15% by score within window\\n   d) Output: list of (position, token/ngram, tfidf_score) landmarks\\n   e) Store top-K landmarks (K=10-30 per passage, configurable)\\n\\n# PHASE 3: FINGERPRINT GENERATION\\n3. Landmark-pair hashing (Shazam-inspired):\\n   a) For each anchor landmark (pos_a, token_a, score_a):\\n      - Define lookahead window W in tokens (e.g., W=20, 50)\\n      - Enumerate all target landmarks (pos_t, token_t, score_t) where:\\n        pos_a < pos_t <= pos_a + W\\n      - For each (anchor, target) pair:\\n        delta = pos_t - pos_a (relative positional offset, quantized to nearest 5 tokens)\\n        hash_val = hash(token_a, token_t, delta) using hashlib.sha256 or xxhash\\n        Emit (hash_val, delta) as single fingerprint entry\\n   b) Fingerprint FP = set of all hash tuples for passage\\n   c) Implement variant (ablation): FP_no_delta = set of hash(token_a, token_t) (no offset)\\n   d) Output: FP, FP_no_delta, stats (|FP|, landmark_count, density)\\n\\n# PHASE 4: BASELINE IMPLEMENTATIONS\\n4. MinHash Jaccard (using datasketch):\\n   a) Tokenize text into 5-8 char shingles\\n   b) Create MinHash(num_perm=128) for each passage\\n   c) Store MinHash objects in dict keyed by passage_id\\n\\n5. MinHash Containment (using datasketch.MinHashLSHEnsemble):\\n   a) Initialize MinHashLSHEnsemble(threshold=0.5, num_perm=128, num_part=32)\\n   b) Index all passages: index([(id, minhash_obj, shingle_count)])\\n   c) Query: query(minhash_query, shingle_count_query) -> candidates\\n\\n6. SimHash (using floc-simhash or custom implementation):\\n   a) Extract TF-IDF vector for passage (sklearn TfidfVectorizer)\\n   b) Project onto 64 random hyperplanes\\n   c) Create 64-bit hash (bit_i = 1 if dot(tfidf_vec, random_vector_i) > 0)\\n   d) Store bit-vector for each passage\\n\\n# PHASE 5: SIMILARITY COMPUTATION\\n7. Compute pairwise similarity for all methods on test set:\\n   a) Landmark-pair: Jaccard(FP1, FP2) = |FP1 ∩ FP2| / |FP1 ∪ FP2|\\n   b) MinHash Jaccard: Use datasketch MinHash.jaccard() directly\\n   c) MinHash Containment: Use LSHEnsemble query; compute |intersection| / |query|\\n   d) SimHash: Hamming distance between bit-vectors / 64 (normalized)\\n   e) Store similarity matrix for downstream metric computation\\n\\n# PHASE 6: EVALUATION METRICS\\n8. Precision-recall curves at fixed thresholds:\\n   a) For each method, sweep threshold from 0.0 to 1.0 in steps of 0.05\\n   b) For each threshold:\\n      - True positives: (pair, label=1, similarity >= threshold)\\n      - False positives: (pair, label=0, similarity >= threshold)\\n      - True negatives: (pair, label=0, similarity < threshold)\\n      - False negatives: (pair, label=1, similarity < threshold)\\n      - Compute: precision = TP / (TP + FP), recall = TP / (TP + FN)\\n   c) PRIMARY METRIC: Recall at precision >= 0.90 for both MRPC and synthetic benchmarks\\n   d) Secondary metrics:\\n      - F1 at optimal threshold\\n      - Area under PR curve (AP)\\n      - Threshold T for each method (the value used)\\n\\n# PHASE 7: ABLATIONS & STATISTICAL TESTING\\n9. Ablation 1 - Positional offset significance:\\n   a) Run full pipeline for FP (with delta) and FP_no_delta (without delta)\\n   b) Compute precision@recall=0.90 for both\\n   c) Two-proportion z-test: H0: p_with = p_without (α=0.05)\\n   d) Report: z-statistic, p-value, 95% CI for difference\\n   e) Interpret: Offset must show statistically significant improvement\\n\\n10. Ablation 2 - Landmark density:\\n    a) Re-run landmark extraction with K ∈ {5, 10, 15, 20, 30}\\n    b) Compute fingerprints and precision@recall for each K\\n    c) Plot: K vs recall@prec>=0.90 (sensitivity to density)\\n    d) Report: Optimal K value and diminishing returns threshold\\n\\n11. Ablation 3 - Lookahead window W:\\n    a) Re-run landmark-pair hashing with W ∈ {10, 20, 50, 100}\\n    b) Compute precision@recall for each W\\n    c) Plot: W vs recall@prec>=0.90 (sensitivity to structural scope)\\n    d) Interpret: Larger W should handle greater reordering but reduce distinctiveness\\n\\n# PHASE 8: PERFORMANCE BENCHMARKING\\n12. Query latency and throughput:\\n    a) Create 1M-passage synthetic corpus (random Wikipedia subset)\\n    b) Index all passages with all 4 methods\\n    c) Draw 1000 random query passages\\n    d) Measure per-method:\\n      - Query latency (ms per query): median, 95th percentile\\n      - Index memory footprint (MB)\\n      - Throughput (queries/sec)\\n      - Indexing time (minutes)\\n    e) Report: Timing as table with method comparison\\n\\n# PHASE 9: OUTPUT GENERATION\\n13. Write method_out.json with structure:\\n    {\\n      \\\"metadata\\\": {\\n        \\\"objective\\\": \\\"Benchmark landmark-pair fingerprinting vs MinHash/SimHash\\\",\\n        \\\"timestamp\\\": ISO8601,\\n        \\\"run_id\\\": extracted from workspace_path\\n      },\\n      \\\"datasets\\\": [\\n        {\\n          \\\"name\\\": \\\"GLUE_MRPC\\\",\\n          \\\"num_pairs\\\": 4076,\\n          \\\"num_positive\\\": 2753,\\n          \\\"num_negative\\\": 1323,\\n          \\\"results\\\": {\\n            \\\"landmark_pair\\\": {\\n              \\\"threshold_at_prec90\\\": 0.XX,\\n              \\\"recall_at_prec90\\\": 0.XX,\\n              \\\"precision_at_recall90\\\": 0.XX,\\n              \\\"f1_optimal\\\": 0.XX,\\n              \\\"auc_pr\\\": 0.XX,\\n              \\\"precision_recall_curve\\\": [[th, prec, recall], ...],\\n              \\\"avg_fingerprint_size\\\": 150\\n            },\\n            \\\"minHash_jaccard\\\": {...},\\n            \\\"minHash_containment\\\": {...},\\n            \\\"simhash\\\": {...}\\n          }\\n        },\\n        {\\n          \\\"name\\\": \\\"Synthetic_Structural_Edits\\\",\\n          \\\"num_pairs\\\": 1000,\\n          \\\"edit_types\\\": [\\\"prepend\\\", \\\"append\\\", \\\"insert\\\", \\\"reorder\\\"],\\n          \\\"results\\\": {...similar structure...}\\n        }\\n      ],\\n      \\\"ablations\\\": {\\n        \\\"positional_offset\\\": {\\n          \\\"with_delta_recall_prec90\\\": 0.XX,\\n          \\\"without_delta_recall_prec90\\\": 0.XX,\\n          \\\"z_statistic\\\": 2.34,\\n          \\\"p_value\\\": 0.019,\\n          \\\"ci_95_difference\\\": [0.05, 0.25],\\n          \\\"verdict\\\": \\\"SIGNIFICANT\\\" or \\\"NOT_SIGNIFICANT\\\"\\n        },\\n        \\\"landmark_density\\\": {\\n          \\\"by_k\\\": {\\n            \\\"k=5\\\": {\\\"recall_prec90\\\": 0.XX, \\\"avg_landmarks_per_passage\\\": 5},\\n            \\\"k=10\\\": {...},\\n            \\\"k=15\\\": {...},\\n            \\\"k=20\\\": {...},\\n            \\\"k=30\\\": {...}\\n          }\\n        },\\n        \\\"lookahead_window\\\": {\\n          \\\"by_w\\\": {\\n            \\\"w=10\\\": {\\\"recall_prec90\\\": 0.XX, \\\"avg_fp_size\\\": 120},\\n            \\\"w=20\\\": {...},\\n            \\\"w=50\\\": {...},\\n            \\\"w=100\\\": {...}\\n          }\\n        }\\n      },\\n      \\\"timing\\\": {\\n        \\\"index_method\\\": \\\"All methods indexed on 1M synthetic corpus\\\",\\n        \\\"by_method\\\": {\\n          \\\"landmark_pair\\\": {\\n            \\\"indexing_time_minutes\\\": 12.5,\\n            \\\"index_memory_mb\\\": 850,\\n            \\\"median_query_latency_ms\\\": 2.3,\\n            \\\"p95_query_latency_ms\\\": 8.7,\\n            \\\"throughput_queries_sec\\\": 435\\n          },\\n          \\\"minHash_jaccard\\\": {...},\\n          \\\"minHash_containment\\\": {...},\\n          \\\"simhash\\\": {...}\\n        }\\n      },\\n      \\\"implementation_details\\\": {\\n        \\\"landmark_extraction\\\": {\\n          \\\"method\\\": \\\"scipy.ndimage.maximum_filter over (position, token_id) sparse matrix\\\",\\n          \\\"filter_window_size\\\": [3, 50],\\n          \\\"percentile_threshold\\\": 85,\\n          \\\"sample_landmarks_per_passage\\\": [5, 10, 15, 20, 30]\\n        },\\n        \\\"landmark_pair_hashing\\\": {\\n          \\\"hash_function\\\": \\\"hashlib.sha256 -> first 32 bits\\\",\\n          \\\"lookahead_windows\\\": [10, 20, 50, 100],\\n          \\\"delta_quantization\\\": \\\"nearest 5 tokens\\\",\\n          \\\"ablations_run\\\": [\\\"with_delta\\\", \\\"without_delta\\\"]\\n        },\\n        \\\"baselines\\\": {\\n          \\\"minHash_jaccard\\\": {\\n            \\\"library\\\": \\\"datasketch\\\",\\n            \\\"num_permutations\\\": 128,\\n            \\\"shingle_size\\\": \\\"5-8 char\\\"\\n          },\\n          \\\"minHash_containment\\\": {\\n            \\\"library\\\": \\\"datasketch.MinHashLSHEnsemble\\\",\\n            \\\"threshold\\\": 0.5,\\n            \\\"num_perm\\\": 128,\\n            \\\"num_part\\\": 32\\n          },\\n          \\\"simhash\\\": {\\n            \\\"method\\\": \\\"Custom or floc-simhash\\\",\\n            \\\"bit_width\\\": 64,\\n            \\\"vectorizer\\\": \\\"sklearn TfidfVectorizer\\\"\\n          }\\n        }\\n      },\\n      \\\"key_findings\\\": {\\n        \\\"landmark_pair_beats_containment\\\": true or false,\\n        \\\"recall_delta_vs_containment_percentage_points\\\": 8.3,\\n        \\\"positional_offset_is_load_bearing\\\": true or false,\\n        \\\"best_landmark_density_k\\\": 15,\\n        \\\"best_lookahead_window_w\\\": 20,\\n        \\\"verdict\\\": \\\"CONFIRM\\\" or \\\"PARTIAL\\\" or \\\"DISCONFIRM\\\"\\n      }\\n    }\\n\\n# PHASE 10: VALIDATION & ERROR HANDLING\\n14. Validation checkpoints:\\n    a) After landmark extraction: Assert >=5 landmarks per passage on avg\\n    b) After fingerprinting: Assert |FP| in expected range (100-2000 hashes)\\n    c) After baseline computation: Assert all similarity scores in [0, 1]\\n    d) After metric computation: Assert precision + 1-recall >= 0 (no impossible curves)\\n    e) Write validation_log.txt with pass/fail for each check\",\n  \"fallback_plan\": \"# Fallback 1: If scipy.ndimage.maximum_filter causes memory issues\\n- Instead of 2D sparse matrix, use 1D sliding window over position sequence\\n- For each position window [i, i+K], find max TF-IDF token -> landmark\\n- Simpler, memory-light, trades some locality for tractability\\n- Landmark quality may decrease slightly but method remains viable\\n\\n# Fallback 2: If landmark-pair fingerprinting is too dense (>5000 hashes/doc)\\n- Reduce lookahead window W from 50 to 20 tokens\\n- Increase landmark density threshold (keep top-10% instead of top-15%)\\n- Sample landmark pairs probabilistically (if >1000, keep 1000 random pairs)\\n- This preserves method while limiting computation\\n\\n# Fallback 3: If MinHashLSHEnsemble indexing fails or is too slow\\n- Use datasketch.MinHash with brute-force pairwise comparison\\n- Trade O(n) indexing for O(n^2) query cost\\n- Still valid baseline; just slower on 1M corpus\\n- Fall back to 10k corpus instead of 1M for timing benchmarks\\n\\n# Fallback 4: If SimHash implementation unavailable or slow\\n- Use a simpler bit-vector hash: hash first N tokens deterministically\\n- Not ideal but provides a lightweight baseline for comparison\\n\\n# Fallback 5: If statistical significance test fails (e.g., perfect separation)\\n- Report effect size (Cohen's h) instead of p-value\\n- Use bootstrap CI instead of exact two-proportion z-test\\n- Acknowledge ceiling/floor effects in ablation section\\n\\n# Fallback 6: If synthetic structural-edit generation is too slow\\n- Use pre-made plagiarism datasets (PAN-PC-11 if available)\\n- Or generate only 200-300 synthetic variants instead of 1000\\n- Primary evaluation remains on GLUE MRPC (4076 pairs)\\n\\n# Fallback 7: If timing benchmark on 1M corpus exceeds time budget\\n- Benchmark on 100k corpus instead\\n- Scale up projections (multiply latencies by ~10x, memory by ~100x)\\n- Focus on relative comparison (landmark-pair vs baselines) not absolute numbers\",\n  \"testing_plan\": \"# PHASE 1: UNIT TESTS (First 30 minutes, before full run)\\n1. Test landmark extraction:\\n   - Load mini_data_out.json (3 examples from dependency)\\n   - Extract landmarks from each sentence pair\\n   - Assert: >=1 landmark per passage, landmarks in range [0, len(text)]\\n   - Manually verify top landmark is plausibly a salient token (not common word)\\n   - Output: landmark_extraction_unit_test.log\\n\\n2. Test fingerprint generation:\\n   - Create 5-word synthetic passage: \\\"the quick brown fox jumps\\\"\\n   - Manually compute expected landmark pairs\\n   - Run algorithm, compare against manual expectation\\n   - Assert: Fingerprint size matches manual pair count\\n   - Test with/without positional offset variants\\n   - Output: fingerprint_generation_unit_test.log\\n\\n3. Test baseline implementations:\\n   a) MinHash: Create two identical 10-word passages\\n     - Assert: jaccard(M1, M1) == 1.0 (identity check)\\n   b) MinHash: Create two disjoint 10-word passages\\n     - Assert: jaccard(M1, M2) close to 0 (disjoint check)\\n   c) MinHash Containment: Query subset against superset\\n     - Assert: containment(subset, superset) > 0.5\\n   d) SimHash: Two identical passages\\n     - Assert: Hamming(H1, H1) == 0\\n   - Output: baseline_unit_tests.log\\n\\n4. Test evaluation metrics:\\n   - Create mock similarity scores and labels\\n   - Compute precision-recall curve\\n   - Assert: At threshold=1.0, precision=1.0 (or NaN if no positive predictions)\\n   - Assert: At threshold=0.0, recall=1.0\\n   - Assert: Precision + (1-recall) >= 0 for all points\\n   - Output: metric_validation.log\\n\\n# PHASE 2: MINI DATA TEST (30-60 minutes, full pipeline on 3 examples)\\n5. Run full pipeline on mini_data_out.json only:\\n   - All 4 methods on 3 MRPC pairs\\n   - Compute similarities and metrics\\n   - Manually verify a few scores make intuitive sense\\n   - Expected: Should complete in <5 minutes, no crashes\\n   - Output: mini_pipeline_results.json (same schema as method_out.json but tiny)\\n\\n6. Verify mini results:\\n   - Check that landmark-pair and minHash both have results\\n   - Check that similarity scores are in [0, 1]\\n   - Check that precision-recall curve has >=3 points\\n   - If landmark-pair scores are all identical or all zero -> debug landmark extraction\\n   - Output: mini_validation_report.txt\\n\\n# PHASE 3: PREVIEW DATA TEST (1-2 hours, full pipeline on ~400 pairs)\\n7. Run full pipeline on first 400 MRPC pairs (\\\"preview scale\\\"):\\n   - Build TF-IDF corpus on these 400\\n   - Extract landmarks, compute fingerprints, index baselines\\n   - Compute all metrics and ablations (K=5,10,15; W=10,20,50)\\n   - Expected time: ~30-60 minutes depending on compute\\n   - Output: preview_results.json (complete schema, representatively small dataset)\\n\\n8. Validation checks on preview results:\\n   a) Landmark counts:\\n      - Average landmarks per passage: should be K +/- 2 (e.g., 15±2)\\n      - Assert no passage has 0 landmarks\\n   b) Fingerprint sizes:\\n      - Average |FP|: should scale as ~K^2 / 2 (O(quadratic) in landmark count)\\n      - Landmark-pair FP should be 2-5x larger than MinHash (100s vs 100-200 hashes)\\n   c) Similarity distributions:\\n      - Plot histogram of similarities for each method\\n      - Landmark-pair should show clear bimodal (high for paraphrases, low for non-paraphrases)\\n      - If distribution is uniform -> method not working\\n   d) Ablation results:\\n      - Recall@prec>=0.90 should increase monotonically with K (or plateau)\\n      - Without-delta should have lower precision@recall than with-delta\\n      - If opposite, landmark extraction or hashing is broken\\n   e) Statistical test:\\n      - Two-proportion z-test should yield p < 0.05 if delta is significant\\n      - If p > 0.5, offset is NOT load-bearing -> hypothesis challenge\\n   - Output: preview_validation_report.txt\\n\\n# PHASE 4: DECISION CHECKPOINT\\n9. Decision: Should proceed to full dataset?\\n   If ANY of the following:\\n   - Unit tests FAIL -> Debug landmark extraction / fingerprinting\\n   - Mini pipeline doesn't complete -> Fix crashes before scaling\\n   - Mini results are nonsensical (all zeros, random) -> Rethink approach\\n   - Ablation fails to show significance -> Revisit hypothesis\\n   Otherwise: PROCEED to full data\\n\\n# PHASE 5: FULL DATA RUN (2-3 hours remaining)\\n10. Run full pipeline on all GLUE MRPC + synthetic structural edits:\\n    - Load all 4076 MRPC pairs\\n    - Generate 500-1000 synthetic variants with edits\\n    - Extract landmarks, fingerprint, compute all metrics\\n    - Expected time: 90-180 minutes depending on optimization\\n    - Output: method_out.json with final results\\n\\n# PHASE 6: FINAL VALIDATION\\n11. Sanity checks on final results:\\n    - Landmark-pair recall@prec>=0.90 should be >= 0.5 (at least half of true paraphrases)\\n    - If < 0.3, hypothesis is weak; if > 0.95, possible overfitting on MRPC\\n    - Containment MinHash recall should be > 0.4 (it's a strong baseline)\\n    - Landmark-pair should beat or match containment (or document why it doesn't)\\n    - Synthetic dataset should show larger recall gains vs MRPC\\n      (landmark-pair designed for structural edits, should shine here)\\n    - If synthetic results are worse than MRPC, structural-edit generation may be flawed\\n    - Output: final_validation_report.txt\\n\\n# PHASE 7: VERIFICATION OF HYPOTHESIS VERDICT\\n12. Determine CONFIRM / PARTIAL / DISCONFIRM:\\n    - CONFIRM: landmark-pair recall@prec>=0.90 >= containment recall + 10pp on structural edits\\n      AND positional offset ablation is significant (p<0.05)\\n      AND timing is <10x slower than MinHash\\n    - PARTIAL: Gains only on structural edits, not MRPC\\n      OR Gains <5pp (lower than expected 10-15pp)\\n      OR Statistical significance marginal (p close to 0.05)\\n    - DISCONFIRM: landmark-pair <= containment baseline on both datasets\\n      OR Inverted-index lookup >10x slower than MinHash\\n      OR Cannot extract stable landmarks (too much variance across texts)\\n    - Output: verdict.txt with final interpretation\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [37] ASSISTANT · 2026-07-03 18:15:24 UTC

```
Perfect. I've written a comprehensive, detailed plan for the landmark-pair fingerprinting experiment. Here's what I've delivered:

## Plan Summary

**File location**: `./.terminal_claude_agent_struct_out.json` (in scratchpad)

### Key Components:

1. **Implementation Pseudocode (10 phases)**:
   - Data prep: Load GLUE MRPC + generate synthetic structural edits (prepend/append/insert/reorder)
   - Landmark extraction: TF-IDF sliding windows → 2D local maxima via `scipy.ndimage.maximum_filter`
   - Fingerprint generation: Shazam-inspired anchor-target pairs with quantized position deltas
   - Baselines: MinHash Jaccard, MinHash Containment (datasketch), SimHash (64-bit)
   - Metrics: Precision-recall curves, recall@precision≥0.90 as primary metric
   - Ablations: Positional offset (with vs without delta), landmark density K={5,10,15,20,30}, lookahead window W={10,20,50,100}
   - Performance: 1M-corpus benchmark (latency, throughput, memory, indexing time)
   - Output: Detailed `method_out.json` schema with all results, stats, and findings

2. **Fallback Plan (7 scenarios)**:
   - Memory overflow → use 1D sliding window instead of 2D sparse matrix
   - Too-dense fingerprints → reduce W or increase threshold
   - MinHash indexing fails → fall back to brute-force comparison
   - SimHash unavailable → use deterministic token hash
   - Statistical tests fail → use effect size / bootstrap CI
   - Synthetic generation too slow → use pre-made datasets or fewer variants
   - 1M corpus timeout → use 100k corpus with scaling projections

3. **Testing Plan (12 progressive phases)**:
   - **Unit tests** (30 min): Landmark extraction on toy examples, fingerprint generation validation, baseline sanity checks
   - **Mini data** (30-60 min): Full pipeline on 3 MRPC examples from dependency
   - **Preview data** (1-2 hours): Full pipeline on 400 pairs with complete ablations
   - **Decision checkpoint**: Explicit go/no-go criteria before full run
   - **Full data** (2-3 hours): 4076 MRPC + 500-1000 synthetic variants
   - **Final validation**: Sanity checks and hypothesis verdict (CONFIRM/PARTIAL/DISCONFIRM)

### Critical Details for Executor:

- **Landmark extraction**: Top-K% by TF-IDF within 5-10 word sliding windows using `scipy.ndimage.maximum_filter` on (position, token_id) sparse matrix with 3×50 window size
- **Hash construction**: `hash(token_a, token_b, quantized_delta)` where delta is relative position in 5-token bins, inspired by Shazam's (f_anchor, f_target, time_delta) tuples
- **Primary validation**: Landmark-pair must achieve ≥10 percentage point higher recall than MinHash Containment at precision≥0.90 on **structural-edit** variants (the distinctive test case where landmark pairs preserve relative distances better than shingle co-occurrence)
- **Compute profile**: `cpu_heavy` (4 vCPU, 32GB RAM) for 1M-corpus indexing and large TF-IDF matrix operations
- **Budget**: $10 cap on LLM API calls (not used in this artifact, but noted)

The plan respects the hypothesis's revised expectations (5-15pp over containment, not 33pp over Jaccard), emphasizes paragraph-reordering as the key discriminator, and includes explicit abort criteria if early validation fails.

Sources:
- [datasketch MinHashLSHEnsemble](https://ekzhu.com/datasketch/lshensemble.html)
- [Shazam Algorithm Explained](https://medium.com/@shivam01110011/audio-fingerprinting-aee18fb88d4a)
- [Winnowing Paper](https://www.semanticscholar.org/paper/Winnowing:-local-algorithms-for-document-Schleimer-Wilkerson/73acc491ec7eb8f0a29e0f06397cb517b79e658b)
- [SimHash Implementation](https://github.com/hybridtheory/floc-simhash)
```

### [38] SYSTEM-USER prompt · 2026-07-03 18:15:26 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [39] ASSISTANT · 2026-07-03 18:16:32 UTC

```
I see the issue—I wrote to the wrong path. The file needs to be in the working directory (`./.terminal_claude_agent_struct_out.json`), which is `/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/`. Let me fix that:
```

### [40] TOOL CALL — Write · 2026-07-03 18:16:32 UTC

```
File: /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json

{
  "title": "Landmark-Pair Fingerprinting vs MinHash/SimHash",
  "summary": "Implement landmark-pair text fingerprinting (inspired by Shazam's audio hashing), benchmark against MinHash Jaccard, MinHash Containment, and SimHash on GLUE MRPC and synthetic structural-edit test sets. Validate that positional offsets between salient n-gram pairs outperform global statistics for near-duplicate detection.",
  "runpod_compute_profile": "cpu_heavy",
  "implementation_pseudocode": "# PHASE 1: DATA PREPARATION\n1. Load GLUE MRPC from art__yFeBexgqp0M dependency (full_data_out.json)\n   - Parse JSON pairs: sentence1, sentence2, label\n   - Create synthetic structural-edit variants:\n     a) Prepend random sentences (50, 100, 200 tokens)\n     b) Append random sentences (50, 100, 200 tokens)\n     c) Insert sentences mid-paragraph (at 25%, 50%, 75% positions)\n     d) Reorder paragraphs (swap adjacent sentences within pairs)\n   - Store as (id, text, edit_type, original_pair_id, label) tuples\n   - Target: 500-1000 synthetic variants + 4076 MRPC originals\n\n# PHASE 2: LANDMARK EXTRACTION (Core Innovation)\n2. Implement landmark extraction for each passage:\n   a) Tokenize text into words (or 5-8 char n-grams)\n   b) Compute sliding-window TF-IDF:\n      - Build corpus-level IDF via sklearn.feature_extraction.text.TfidfVectorizer\n      - For each token position, compute local TF-IDF score (via gensim or sklearn)\n        using a 5-10 word sliding window (NOT over full doc)\n      - Output: position -> local_tfidf_score matrix\n   c) Find 2D local maxima using scipy.ndimage.maximum_filter:\n      - Apply 2D filter over (position, token_id_hash) sparse matrix\n      - Window size: ~3 positions x ~50 token buckets\n      - Threshold: Keep landmarks in top 10-15% by score within window\n   d) Output: list of (position, token/ngram, tfidf_score) landmarks\n   e) Store top-K landmarks (K=10-30 per passage, configurable)\n\n# PHASE 3: FINGERPRINT GENERATION\n3. Landmark-pair hashing (Shazam-inspired):\n   a) For each anchor landmark (pos_a, token_a, score_a):\n      - Define lookahead window W in tokens (e.g., W=20, 50)\n      - Enumerate all target landmarks (pos_t, token_t, score_t) where:\n        pos_a < pos_t <= pos_a + W\n      - For each (anchor, target) pair:\n        delta = pos_t - pos_a (relative positional offset, quantized to nearest 5 tokens)\n        hash_val = hash(token_a, token_t, delta) using hashlib.sha256 or xxhash\n        Emit (hash_val, delta) as single fingerprint entry\n   b) Fingerprint FP = set of all hash tuples for passage\n   c) Implement variant (ablation): FP_no_delta = set of hash(token_a, token_t) (no offset)\n   d) Output: FP, FP_no_delta, stats (|FP|, landmark_count, density)\n\n# PHASE 4: BASELINE IMPLEMENTATIONS\n4. MinHash Jaccard (using datasketch):\n   a) Tokenize text into 5-8 char shingles\n   b) Create MinHash(num_perm=128) for each passage\n   c) Store MinHash objects in dict keyed by passage_id\n\n5. MinHash Containment (using datasketch.MinHashLSHEnsemble):\n   a) Initialize MinHashLSHEnsemble(threshold=0.5, num_perm=128, num_part=32)\n   b) Index all passages: index([(id, minhash_obj, shingle_count)])\n   c) Query: query(minhash_query, shingle_count_query) -> candidates\n\n6. SimHash (using floc-simhash or custom implementation):\n   a) Extract TF-IDF vector for passage (sklearn TfidfVectorizer)\n   b) Project onto 64 random hyperplanes\n   c) Create 64-bit hash (bit_i = 1 if dot(tfidf_vec, random_vector_i) > 0)\n   d) Store bit-vector for each passage\n\n# PHASE 5: SIMILARITY COMPUTATION\n7. Compute pairwise similarity for all methods on test set:\n   a) Landmark-pair: Jaccard(FP1, FP2) = |FP1 ∩ FP2| / |FP1 ∪ FP2|\n   b) MinHash Jaccard: Use datasketch MinHash.jaccard() directly\n   c) MinHash Containment: Use LSHEnsemble query; compute |intersection| / |query|\n   d) SimHash: Hamming distance between bit-vectors / 64 (normalized)\n   e) Store similarity matrix for downstream metric computation\n\n# PHASE 6: EVALUATION METRICS\n8. Precision-recall curves at fixed thresholds:\n   a) For each method, sweep threshold from 0.0 to 1.0 in steps of 0.05\n   b) For each threshold:\n      - True positives: (pair, label=1, similarity >= threshold)\n      - False positives: (pair, label=0, similarity >= threshold)\n      - True negatives: (pair, label=0, similarity < threshold)\n      - False negatives: (pair, label=1, similarity < threshold)\n      - Compute: precision = TP / (TP + FP), recall = TP / (TP + FN)\n   c) PRIMARY METRIC: Recall at precision >= 0.90 for both MRPC and synthetic benchmarks\n   d) Secondary metrics:\n      - F1 at optimal threshold\n      - Area under PR curve (AP)\n      - Threshold T for each method (the value used)\n\n# PHASE 7: ABLATIONS & STATISTICAL TESTING\n9. Ablation 1 - Positional offset significance:\n   a) Run full pipeline for FP (with delta) and FP_no_delta (without delta)\n   b) Compute precision@recall=0.90 for both\n   c) Two-proportion z-test: H0: p_with = p_without (alpha=0.05)\n   d) Report: z-statistic, p-value, 95% CI for difference\n   e) Interpret: Offset must show statistically significant improvement\n\n10. Ablation 2 - Landmark density:\n    a) Re-run landmark extraction with K in {5, 10, 15, 20, 30}\n    b) Compute fingerprints and precision@recall for each K\n    c) Plot: K vs recall@prec>=0.90 (sensitivity to density)\n    d) Report: Optimal K value and diminishing returns threshold\n\n11. Ablation 3 - Lookahead window W:\n    a) Re-run landmark-pair hashing with W in {10, 20, 50, 100}\n    b) Compute precision@recall for each W\n    c) Plot: W vs recall@prec>=0.90 (sensitivity to structural scope)\n    d) Interpret: Larger W should handle greater reordering but reduce distinctiveness\n\n# PHASE 8: PERFORMANCE BENCHMARKING\n12. Query latency and throughput:\n    a) Create 1M-passage synthetic corpus (random Wikipedia subset)\n    b) Index all passages with all 4 methods\n    c) Draw 1000 random query passages\n    d) Measure per-method:\n      - Query latency (ms per query): median, 95th percentile\n      - Index memory footprint (MB)\n      - Throughput (queries/sec)\n      - Indexing time (minutes)\n    e) Report: Timing as table with method comparison\n\n# PHASE 9: OUTPUT GENERATION\n13. Write method_out.json with structure:\n    {\n      \"metadata\": {\n        \"objective\": \"Benchmark landmark-pair fingerprinting vs MinHash/SimHash\",\n        \"timestamp\": ISO8601,\n        \"run_id\": extracted from workspace_path\n      },\n      \"datasets\": [\n        {\n          \"name\": \"GLUE_MRPC\",\n          \"num_pairs\": 4076,\n          \"num_positive\": 2753,\n          \"num_negative\": 1323,\n          \"results\": {\n            \"landmark_pair\": {\n              \"threshold_at_prec90\": 0.XX,\n              \"recall_at_prec90\": 0.XX,\n              \"precision_at_recall90\": 0.XX,\n              \"f1_optimal\": 0.XX,\n              \"auc_pr\": 0.XX,\n              \"precision_recall_curve\": [[th, prec, recall], ...],\n              \"avg_fingerprint_size\": 150\n            },\n            \"minHash_jaccard\": {...},\n            \"minHash_containment\": {...},\n            \"simhash\": {...}\n          }\n        },\n        {\n          \"name\": \"Synthetic_Structural_Edits\",\n          \"num_pairs\": 1000,\n          \"edit_types\": [\"prepend\", \"append\", \"insert\", \"reorder\"],\n          \"results\": {...similar structure...}\n        }\n      ],\n      \"ablations\": {\n        \"positional_offset\": {\n          \"with_delta_recall_prec90\": 0.XX,\n          \"without_delta_recall_prec90\": 0.XX,\n          \"z_statistic\": 2.34,\n          \"p_value\": 0.019,\n          \"ci_95_difference\": [0.05, 0.25],\n          \"verdict\": \"SIGNIFICANT\" or \"NOT_SIGNIFICANT\"\n        },\n        \"landmark_density\": {\n          \"by_k\": {\n            \"k=5\": {\"recall_prec90\": 0.XX, \"avg_landmarks_per_passage\": 5},\n            \"k=10\": {...},\n            \"k=15\": {...},\n            \"k=20\": {...},\n            \"k=30\": {...}\n          }\n        },\n        \"lookahead_window\": {\n          \"by_w\": {\n            \"w=10\": {\"recall_prec90\": 0.XX, \"avg_fp_size\": 120},\n            \"w=20\": {...},\n            \"w=50\": {...},\n            \"w=100\": {...}\n          }\n        }\n      },\n      \"timing\": {\n        \"index_method\": \"All methods indexed on 1M synthetic corpus\",\n        \"by_method\": {\n          \"landmark_pair\": {\n            \"indexing_time_minutes\": 12.5,\n            \"index_memory_mb\": 850,\n            \"median_query_latency_ms\": 2.3,\n            \"p95_query_latency_ms\": 8.7,\n            \"throughput_queries_sec\": 435\n          },\n          \"minHash_jaccard\": {...},\n          \"minHash_containment\": {...},\n          \"simhash\": {...}\n        }\n      },\n      \"implementation_details\": {\n        \"landmark_extraction\": {\n          \"method\": \"scipy.ndimage.maximum_filter over (position, token_id) sparse matrix\",\n          \"filter_window_size\": [3, 50],\n          \"percentile_threshold\": 85,\n          \"sample_landmarks_per_passage\": [5, 10, 15, 20, 30]\n        },\n        \"landmark_pair_hashing\": {\n          \"hash_function\": \"hashlib.sha256 -> first 32 bits\",\n          \"lookahead_windows\": [10, 20, 50, 100],\n          \"delta_quantization\": \"nearest 5 tokens\",\n          \"ablations_run\": [\"with_delta\", \"without_delta\"]\n        },\n        \"baselines\": {\n          \"minHash_jaccard\": {\n            \"library\": \"datasketch\",\n            \"num_permutations\": 128,\n            \"shingle_size\": \"5-8 char\"\n          },\n          \"minHash_containment\": {\n            \"library\": \"datasketch.MinHashLSHEnsemble\",\n            \"threshold\": 0.5,\n            \"num_perm\": 128,\n            \"num_part\": 32\n          },\n          \"simhash\": {\n            \"method\": \"Custom or floc-simhash\",\n            \"bit_width\": 64,\n            \"vectorizer\": \"sklearn TfidfVectorizer\"\n          }\n        }\n      },\n      \"key_findings\": {\n        \"landmark_pair_beats_containment\": true or false,\n        \"recall_delta_vs_containment_percentage_points\": 8.3,\n        \"positional_offset_is_load_bearing\": true or false,\n        \"best_landmark_density_k\": 15,\n        \"best_lookahead_window_w\": 20,\n        \"verdict\": \"CONFIRM\" or \"PARTIAL\" or \"DISCONFIRM\"\n      }\n    }\n\n# PHASE 10: VALIDATION & ERROR HANDLING\n14. Validation checkpoints:\n    a) After landmark extraction: Assert >=5 landmarks per passage on avg\n    b) After fingerprinting: Assert |FP| in expected range (100-2000 hashes)\n    c) After baseline computation: Assert all similarity scores in [0, 1]\n    d) After metric computation: Assert precision + 1-recall >= 0 (no impossible curves)\n    e) Write validation_log.txt with pass/fail for each check",
  "fallback_plan": "# Fallback 1: If scipy.ndimage.maximum_filter causes memory issues\n- Instead of 2D sparse matrix, use 1D sliding window over position sequence\n- For each position window [i, i+K], find max TF-IDF token -> landmark\n- Simpler, memory-light, trades some locality for tractability\n- Landmark quality may decrease slightly but method remains viable\n\n# Fallback 2: If landmark-pair fingerprinting is too dense (>5000 hashes/doc)\n- Reduce lookahead window W from 50 to 20 tokens\n- Increase landmark density threshold (keep top-10% instead of top-15%)\n- Sample landmark pairs probabilistically (if >1000, keep 1000 random pairs)\n- This preserves method while limiting computation\n\n# Fallback 3: If MinHashLSHEnsemble indexing fails or is too slow\n- Use datasketch.MinHash with brute-force pairwise comparison\n- Trade O(n) indexing for O(n^2) query cost\n- Still valid baseline; just slower on 1M corpus\n- Fall back to 10k corpus instead of 1M for timing benchmarks\n\n# Fallback 4: If SimHash implementation unavailable or slow\n- Use a simpler bit-vector hash: hash first N tokens deterministically\n- Not ideal but provides a lightweight baseline for comparison\n\n# Fallback 5: If statistical significance test fails (e.g., perfect separation)\n- Report effect size (Cohen's h) instead of p-value\n- Use bootstrap CI instead of exact two-proportion z-test\n- Acknowledge ceiling/floor effects in ablation section\n\n# Fallback 6: If synthetic structural-edit generation is too slow\n- Use pre-made plagiarism datasets (PAN-PC-11 if available)\n- Or generate only 200-300 synthetic variants instead of 1000\n- Primary evaluation remains on GLUE MRPC (4076 pairs)\n\n# Fallback 7: If timing benchmark on 1M corpus exceeds time budget\n- Benchmark on 100k corpus instead\n- Scale up projections (multiply latencies by ~10x, memory by ~100x)\n- Focus on relative comparison (landmark-pair vs baselines) not absolute numbers",
  "testing_plan": "# PHASE 1: UNIT TESTS (First 30 minutes, before full run)\n1. Test landmark extraction:\n   - Load mini_data_out.json (3 examples from dependency)\n   - Extract landmarks from each sentence pair\n   - Assert: >=1 landmark per passage, landmarks in range [0, len(text)]\n   - Manually verify top landmark is plausibly a salient token (not common word)\n   - Output: landmark_extraction_unit_test.log\n\n2. Test fingerprint generation:\n   - Create 5-word synthetic passage: \"the quick brown fox jumps\"\n   - Manually compute expected landmark pairs\n   - Run algorithm, compare against manual expectation\n   - Assert: Fingerprint size matches manual pair count\n   - Test with/without positional offset variants\n   - Output: fingerprint_generation_unit_test.log\n\n3. Test baseline implementations:\n   a) MinHash: Create two identical 10-word passages\n     - Assert: jaccard(M1, M1) == 1.0 (identity check)\n   b) MinHash: Create two disjoint 10-word passages\n     - Assert: jaccard(M1, M2) close to 0 (disjoint check)\n   c) MinHash Containment: Query subset against superset\n     - Assert: containment(subset, superset) > 0.5\n   d) SimHash: Two identical passages\n     - Assert: Hamming(H1, H1) == 0\n   - Output: baseline_unit_tests.log\n\n4. Test evaluation metrics:\n   - Create mock similarity scores and labels\n   - Compute precision-recall curve\n   - Assert: At threshold=1.0, precision=1.0 (or NaN if no positive predictions)\n   - Assert: At threshold=0.0, recall=1.0\n   - Assert: Precision + (1-recall) >= 0 for all points\n   - Output: metric_validation.log\n\n# PHASE 2: MINI DATA TEST (30-60 minutes, full pipeline on 3 examples)\n5. Run full pipeline on mini_data_out.json only:\n   - All 4 methods on 3 MRPC pairs\n   - Compute similarities and metrics\n   - Manually verify a few scores make intuitive sense\n   - Expected: Should complete in <5 minutes, no crashes\n   - Output: mini_pipeline_results.json (same schema as method_out.json but tiny)\n\n6. Verify mini results:\n   - Check that landmark-pair and minHash both have results\n   - Check that similarity scores are in [0, 1]\n   - Check that precision-recall curve has >=3 points\n   - If landmark-pair scores are all identical or all zero -> debug landmark extraction\n   - Output: mini_validation_report.txt\n\n# PHASE 3: PREVIEW DATA TEST (1-2 hours, full pipeline on ~400 pairs)\n7. Run full pipeline on first 400 MRPC pairs (\"preview scale\"):\n   - Build TF-IDF corpus on these 400\n   - Extract landmarks, compute fingerprints, index baselines\n   - Compute all metrics and ablations (K=5,10,15; W=10,20,50)\n   - Expected time: ~30-60 minutes depending on compute\n   - Output: preview_results.json (complete schema, representatively small dataset)\n\n8. Validation checks on preview results:\n   a) Landmark counts:\n      - Average landmarks per passage: should be K +/- 2 (e.g., 15+-2)\n      - Assert no passage has 0 landmarks\n   b) Fingerprint sizes:\n      - Average |FP|: should scale as ~K^2 / 2 (O(quadratic) in landmark count)\n      - Landmark-pair FP should be 2-5x larger than MinHash (100s vs 100-200 hashes)\n   c) Similarity distributions:\n      - Plot histogram of similarities for each method\n      - Landmark-pair should show clear bimodal (high for paraphrases, low for non-paraphrases)\n      - If distribution is uniform -> method not working\n   d) Ablation results:\n      - Recall@prec>=0.90 should increase monotonically with K (or plateau)\n      - Without-delta should have lower precision@recall than with-delta\n      - If opposite, landmark extraction or hashing is broken\n   e) Statistical test:\n      - Two-proportion z-test should yield p < 0.05 if delta is significant\n      - If p > 0.5, offset is NOT load-bearing -> hypothesis challenge\n   - Output: preview_validation_report.txt\n\n# PHASE 4: DECISION CHECKPOINT\n9. Decision: Should proceed to full dataset?\n   If ANY of the following:\n   - Unit tests FAIL -> Debug landmark extraction / fingerprinting\n   - Mini pipeline doesn't complete -> Fix crashes before scaling\n   - Mini results are nonsensical (all zeros, random) -> Rethink approach\n   - Ablation fails to show significance -> Revisit hypothesis\n   Otherwise: PROCEED to full data\n\n# PHASE 5: FULL DATA RUN (2-3 hours remaining)\n10. Run full pipeline on all GLUE MRPC + synthetic structural edits:\n    - Load all 4076 MRPC pairs\n    - Generate 500-1000 synthetic variants with edits\n    - Extract landmarks, fingerprint, compute all metrics\n    - Expected time: 90-180 minutes depending on optimization\n    - Output: method_out.json with final results\n\n# PHASE 6: FINAL VALIDATION\n11. Sanity checks on final results:\n    - Landmark-pair recall@prec>=0.90 should be >= 0.5 (at least half of true paraphrases)\n    - If < 0.3, hypothesis is weak; if > 0.95, possible overfitting on MRPC\n    - Containment MinHash recall should be > 0.4 (it's a strong baseline)\n    - Landmark-pair should beat or match containment (or document why it doesn't)\n    - Synthetic dataset should show larger recall gains vs MRPC\n      (landmark-pair designed for structural edits, should shine here)\n    - If synthetic results are worse than MRPC, structural-edit generation may be flawed\n    - Output: final_validation_report.txt\n\n# PHASE 7: VERIFICATION OF HYPOTHESIS VERDICT\n12. Determine CONFIRM / PARTIAL / DISCONFIRM:\n    - CONFIRM: landmark-pair recall@prec>=0.90 >= containment recall + 10pp on structural edits\n      AND positional offset ablation is significant (p<0.05)\n      AND timing is <10x slower than MinHash\n    - PARTIAL: Gains only on structural edits, not MRPC\n      OR Gains <5pp (lower than expected 10-15pp)\n      OR Statistical significance marginal (p close to 0.05)\n    - DISCONFIRM: landmark-pair <= containment baseline on both datasets\n      OR Inverted-index lookup >10x slower than MinHash\n      OR Cannot extract stable landmarks (too much variance across texts)\n    - Output: verdict.txt with final interpretation"
}
```

### [41] TOOL RESULT — Write · 2026-07-03 18:16:32 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Landmark-Pair Fingerprinting vs MinHash/SimHash\",\n  \"summary\": \"Implement landmark-pair text fingerprinting (inspired by Shazam's audio hashing), benchmark against MinHash Jaccard, MinHash Containment, and SimHash on GLUE MRPC and synthetic structural-edit test sets. Validate that positional offsets between salient n-gram pairs outperform global statistics for near-duplicate detection.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"implementation_pseudocode\": \"# PHASE 1: DATA PREPARATION\\n1. Load GLUE MRPC from art__yFeBexgqp0M dependency (full_data_out.json)\\n   - Parse JSON pairs: sentence1, sentence2, label\\n   - Create synthetic structural-edit variants:\\n     a) Prepend random sentences (50, 100, 200 tokens)\\n     b) Append random sentences (50, 100, 200 tokens)\\n     c) Insert sentences mid-paragraph (at 25%, 50%, 75% positions)\\n     d) Reorder paragraphs (swap adjacent sentences within pairs)\\n   - Store as (id, text, edit_type, original_pair_id, label) tuples\\n   - Target: 500-1000 synthetic variants + 4076 MRPC originals\\n\\n# PHASE 2: LANDMARK EXTRACTION (Core Innovation)\\n2. Implement landmark extraction for each passage:\\n   a) Tokenize text into words (or 5-8 char n-grams)\\n   b) Compute sliding-window TF-IDF:\\n      - Build corpus-level IDF via sklearn.feature_extraction.text.TfidfVectorizer\\n      - For each token position, compute local TF-IDF score (via gensim or sklearn)\\n        using a 5-10 word sliding window (NOT over full doc)\\n      - Output: position -> local_tfidf_score matrix\\n   c) Find 2D local maxima using scipy.ndimage.maximum_filter:\\n      - Apply 2D filter over (position, token_id_hash) sparse matrix\\n      - Window size: ~3 positions x ~50 token buckets\\n      - Threshold: Keep landmarks in top 10-15% by score within window\\n   d) Output: list of (position, token/ngram, tfidf_score) landmarks\\n   e) Store top-K landmarks (K=10-30 per passage, configurable)\\n\\n# PHASE 3: FINGERPRINT GENERATION\\n3. Landmark-pair hashing (Shazam-inspired):\\n   a) For each anchor landmark (pos_a, token_a, score_a):\\n      - Define lookahead window W in tokens (e.g., W=20, 50)\\n      - Enumerate all target landmarks (pos_t, token_t, score_t) where:\\n        pos_a < pos_t <= pos_a + W\\n      - For each (anchor, target) pair:\\n        delta = pos_t - pos_a (relative positional offset, quantized to nearest 5 tokens)\\n        hash_val = hash(token_a, token_t, delta) using hashlib.sha256 or xxhash\\n        Emit (hash_val, delta) as single fingerprint entry\\n   b) Fingerprint FP = set of all hash tuples for passage\\n   c) Implement variant (ablation): FP_no_delta = set of hash(token_a, token_t) (no offset)\\n   d) Output: FP, FP_no_delta, stats (|FP|, landmark_count, density)\\n\\n# PHASE 4: BASELINE IMPLEMENTATIONS\\n4. MinHash Jaccard (using datasketch):\\n   a) Tokenize text into 5-8 char shingles\\n   b) Create MinHash(num_perm=128) for each passage\\n   c) Store MinHash objects in dict keyed by passage_id\\n\\n5. MinHash Containment (using datasketch.MinHashLSHEnsemble):\\n   a) Initialize MinHashLSHEnsemble(threshold=0.5, num_perm=128, num_part=32)\\n   b) Index all passages: index([(id, minhash_obj, shingle_count)])\\n   c) Query: query(minhash_query, shingle_count_query) -> candidates\\n\\n6. SimHash (using floc-simhash or custom implementation):\\n   a) Extract TF-IDF vector for passage (sklearn TfidfVectorizer)\\n   b) Project onto 64 random hyperplanes\\n   c) Create 64-bit hash (bit_i = 1 if dot(tfidf_vec, random_vector_i) > 0)\\n   d) Store bit-vector for each passage\\n\\n# PHASE 5: SIMILARITY COMPUTATION\\n7. Compute pairwise similarity for all methods on test set:\\n   a) Landmark-pair: Jaccard(FP1, FP2) = |FP1 ∩ FP2| / |FP1 ∪ FP2|\\n   b) MinHash Jaccard: Use datasketch MinHash.jaccard() directly\\n   c) MinHash Containment: Use LSHEnsemble query; compute |intersection| / |query|\\n   d) SimHash: Hamming distance between bit-vectors / 64 (normalized)\\n   e) Store similarity matrix for downstream metric computation\\n\\n# PHASE 6: EVALUATION METRICS\\n8. Precision-recall curves at fixed thresholds:\\n   a) For each method, sweep threshold from 0.0 to 1.0 in steps of 0.05\\n   b) For each threshold:\\n      - True positives: (pair, label=1, similarity >= threshold)\\n      - False positives: (pair, label=0, similarity >= threshold)\\n      - True negatives: (pair, label=0, similarity < threshold)\\n      - False negatives: (pair, label=1, similarity < threshold)\\n      - Compute: precision = TP / (TP + FP), recall = TP / (TP + FN)\\n   c) PRIMARY METRIC: Recall at precision >= 0.90 for both MRPC and synthetic benchmarks\\n   d) Secondary metrics:\\n      - F1 at optimal threshold\\n      - Area under PR curve (AP)\\n      - Threshold T for each method (the value used)\\n\\n# PHASE 7: ABLATIONS & STATISTICAL TESTING\\n9. Ablation 1 - Positional offset significance:\\n   a) Run full pipeline for FP (with delta) and FP_no_delta (without delta)\\n   b) Compute precision@recall=0.90 for both\\n   c) Two-proportion z-test: H0: p_with = p_without (alpha=0.05)\\n   d) Report: z-statistic, p-value, 95% CI for difference\\n   e) Interpret: Offset must show statistically significant improvement\\n\\n10. Ablation 2 - Landmark density:\\n    a) Re-run landmark extraction with K in {5, 10, 15, 20, 30}\\n    b) Compute fingerprints and precision@recall for each K\\n    c) Plot: K vs recall@prec>=0.90 (sensitivity to density)\\n    d) Report: Optimal K value and diminishing returns threshold\\n\\n11. Ablation 3 - Lookahead window W:\\n    a) Re-run landmark-pair hashing with W in {10, 20, 50, 100}\\n    b) Compute precision@recall for each W\\n    c) Plot: W vs recall@prec>=0.90 (sensitivity to structural scope)\\n    d) Interpret: Larger W should handle greater reordering but reduce distinctiveness\\n\\n# PHASE 8: PERFORMANCE BENCHMARKING\\n12. Query latency and throughput:\\n    a) Create 1M-passage synthetic corpus (random Wikipedia subset)\\n    b) Index all passages with all 4 methods\\n    c) Draw 1000 random query passages\\n    d) Measure per-method:\\n      - Query latency (ms per query): median, 95th percentile\\n      - Index memory footprint (MB)\\n      - Throughput (queries/sec)\\n      - Indexing time (minutes)\\n    e) Report: Timing as table with method comparison\\n\\n# PHASE 9: OUTPUT GENERATION\\n13. Write method_out.json with structure:\\n    {\\n      \\\"metadata\\\": {\\n        \\\"objective\\\": \\\"Benchmark landmark-pair fingerprinting vs MinHash/SimHash\\\",\\n        \\\"timestamp\\\": ISO8601,\\n        \\\"run_id\\\": extracted from workspace_path\\n      },\\n      \\\"datasets\\\": [\\n        {\\n          \\\"name\\\": \\\"GLUE_MRPC\\\",\\n          \\\"num_pairs\\\": 4076,\\n          \\\"num_positive\\\": 2753,\\n          \\\"num_negative\\\": 1323,\\n          \\\"results\\\": {\\n            \\\"landmark_pair\\\": {\\n              \\\"threshold_at_prec90\\\": 0.XX,\\n              \\\"recall_at_prec90\\\": 0.XX,\\n              \\\"precision_at_recall90\\\": 0.XX,\\n              \\\"f1_optimal\\\": 0.XX,\\n              \\\"auc_pr\\\": 0.XX,\\n              \\\"precision_recall_curve\\\": [[th, prec, recall], ...],\\n              \\\"avg_fingerprint_size\\\": 150\\n            },\\n            \\\"minHash_jaccard\\\": {...},\\n            \\\"minHash_containment\\\": {...},\\n            \\\"simhash\\\": {...}\\n          }\\n        },\\n        {\\n          \\\"name\\\": \\\"Synthetic_Structural_Edits\\\",\\n          \\\"num_pairs\\\": 1000,\\n          \\\"edit_types\\\": [\\\"prepend\\\", \\\"append\\\", \\\"insert\\\", \\\"reorder\\\"],\\n          \\\"results\\\": {...similar structure...}\\n        }\\n      ],\\n      \\\"ablations\\\": {\\n        \\\"positional_offset\\\": {\\n          \\\"with_delta_recall_prec90\\\": 0.XX,\\n          \\\"without_delta_recall_prec90\\\": 0.XX,\\n          \\\"z_statistic\\\": 2.34,\\n          \\\"p_value\\\": 0.019,\\n          \\\"ci_95_difference\\\": [0.05, 0.25],\\n          \\\"verdict\\\": \\\"SIGNIFICANT\\\" or \\\"NOT_SIGNIFICANT\\\"\\n        },\\n        \\\"landmark_density\\\": {\\n          \\\"by_k\\\": {\\n            \\\"k=5\\\": {\\\"recall_prec90\\\": 0.XX, \\\"avg_landmarks_per_passage\\\": 5},\\n            \\\"k=10\\\": {...},\\n            \\\"k=15\\\": {...},\\n            \\\"k=20\\\": {...},\\n            \\\"k=30\\\": {...}\\n          }\\n        },\\n        \\\"lookahead_window\\\": {\\n          \\\"by_w\\\": {\\n            \\\"w=10\\\": {\\\"recall_prec90\\\": 0.XX, \\\"avg_fp_size\\\": 120},\\n            \\\"w=20\\\": {...},\\n            \\\"w=50\\\": {...},\\n            \\\"w=100\\\": {...}\\n          }\\n        }\\n      },\\n      \\\"timing\\\": {\\n        \\\"index_method\\\": \\\"All methods indexed on 1M synthetic corpus\\\",\\n        \\\"by_method\\\": {\\n          \\\"landmark_pair\\\": {\\n            \\\"indexing_time_minutes\\\": 12.5,\\n            \\\"index_memory_mb\\\": 850,\\n            \\\"median_query_latency_ms\\\": 2.3,\\n            \\\"p95_query_latency_ms\\\": 8.7,\\n            \\\"throughput_queries_sec\\\": 435\\n          },\\n          \\\"minHash_jaccard\\\": {...},\\n          \\\"minHash_containment\\\": {...},\\n          \\\"simhash\\\": {...}\\n        }\\n      },\\n      \\\"implementation_details\\\": {\\n        \\\"landmark_extraction\\\": {\\n          \\\"method\\\": \\\"scipy.ndimage.maximum_filter over (position, token_id) sparse matrix\\\",\\n          \\\"filter_window_size\\\": [3, 50],\\n          \\\"percentile_threshold\\\": 85,\\n          \\\"sample_landmarks_per_passage\\\": [5, 10, 15, 20, 30]\\n        },\\n        \\\"landmark_pair_hashing\\\": {\\n          \\\"hash_function\\\": \\\"hashlib.sha256 -> first 32 bits\\\",\\n          \\\"lookahead_windows\\\": [10, 20, 50, 100],\\n          \\\"delta_quantization\\\": \\\"nearest 5 tokens\\\",\\n          \\\"ablations_run\\\": [\\\"with_delta\\\", \\\"without_delta\\\"]\\n        },\\n        \\\"baselines\\\": {\\n          \\\"minHash_jaccard\\\": {\\n            \\\"library\\\": \\\"datasketch\\\",\\n            \\\"num_permutations\\\": 128,\\n            \\\"shingle_size\\\": \\\"5-8 char\\\"\\n          },\\n          \\\"minHash_containment\\\": {\\n            \\\"library\\\": \\\"datasketch.MinHashLSHEnsemble\\\",\\n            \\\"threshold\\\": 0.5,\\n            \\\"num_perm\\\": 128,\\n            \\\"num_part\\\": 32\\n          },\\n          \\\"simhash\\\": {\\n            \\\"method\\\": \\\"Custom or floc-simhash\\\",\\n            \\\"bit_width\\\": 64,\\n            \\\"vectorizer\\\": \\\"sklearn TfidfVectorizer\\\"\\n          }\\n        }\\n      },\\n      \\\"key_findings\\\": {\\n        \\\"landmark_pair_beats_containment\\\": true or false,\\n        \\\"recall_delta_vs_containment_percentage_points\\\": 8.3,\\n        \\\"positional_offset_is_load_bearing\\\": true or false,\\n        \\\"best_landmark_density_k\\\": 15,\\n        \\\"best_lookahead_window_w\\\": 20,\\n        \\\"verdict\\\": \\\"CONFIRM\\\" or \\\"PARTIAL\\\" or \\\"DISCONFIRM\\\"\\n      }\\n    }\\n\\n# PHASE 10: VALIDATION & ERROR HANDLING\\n14. Validation checkpoints:\\n    a) After landmark extraction: Assert >=5 landmarks per passage on avg\\n    b) After fingerprinting: Assert |FP| in expected range (100-2000 hashes)\\n    c) After baseline computation: Assert all similarity scores in [0, 1]\\n    d) After metric computation: Assert precision + 1-recall >= 0 (no impossible curves)\\n    e) Write validation_log.txt with pass/fail for each check\",\n  \"fallback_plan\": \"# Fallback 1: If scipy.ndimage.maximum_filter causes memory issues\\n- Instead of 2D sparse matrix, use 1D sliding window over position sequence\\n- For each position window [i, i+K], find max TF-IDF token -> landmark\\n- Simpler, memory-light, trades some locality for tractability\\n- Landmark quality may decrease slightly but method remains viable\\n\\n# Fallback 2: If landmark-pair fingerprinting is too dense (>5000 hashes/doc)\\n- Reduce lookahead window W from 50 to 20 tokens\\n- Increase landmark density threshold (keep top-10% instead of top-15%)\\n- Sample landmark pairs probabilistically (if >1000, keep 1000 random pairs)\\n- This preserves method while limiting computation\\n\\n# Fallback 3: If MinHashLSHEnsemble indexing fails or is too slow\\n- Use datasketch.MinHash with brute-force pairwise comparison\\n- Trade O(n) indexing for O(n^2) query cost\\n- Still valid baseline; just slower on 1M corpus\\n- Fall back to 10k corpus instead of 1M for timing benchmarks\\n\\n# Fallback 4: If SimHash implementation unavailable or slow\\n- Use a simpler bit-vector hash: hash first N tokens deterministically\\n- Not ideal but provides a lightweight baseline for comparison\\n\\n# Fallback 5: If statistical significance test fails (e.g., perfect separation)\\n- Report effect size (Cohen's h) instead of p-value\\n- Use bootstrap CI instead of exact two-proportion z-test\\n- Acknowledge ceiling/floor effects in ablation section\\n\\n# Fallback 6: If synthetic structural-edit generation is too slow\\n- Use pre-made plagiarism datasets (PAN-PC-11 if available)\\n- Or generate only 200-300 synthetic variants instead of 1000\\n- Primary evaluation remains on GLUE MRPC (4076 pairs)\\n\\n# Fallback 7: If timing benchmark on 1M corpus exceeds time budget\\n- Benchmark on 100k corpus instead\\n- Scale up projections (multiply latencies by ~10x, memory by ~100x)\\n- Focus on relative comparison (landmark-pair vs baselines) not absolute numbers\",\n  \"testing_plan\": \"# PHASE 1: UNIT TESTS (First 30 minutes, before full run)\\n1. Test landmark extraction:\\n   - Load mini_data_out.json (3 examples from dependency)\\n   - Extract landmarks from each sentence pair\\n   - Assert: >=1 landmark per passage, landmarks in range [0, len(text)]\\n   - Manually verify top landmark is plausibly a salient token (not common word)\\n   - Output: landmark_extraction_unit_test.log\\n\\n2. Test fingerprint generation:\\n   - Create 5-word synthetic passage: \\\"the quick brown fox jumps\\\"\\n   - Manually compute expected landmark pairs\\n   - Run algorithm, compare against manual expectation\\n   - Assert: Fingerprint size matches manual pair count\\n   - Test with/without positional offset variants\\n   - Output: fingerprint_generation_unit_test.log\\n\\n3. Test baseline implementations:\\n   a) MinHash: Create two identical 10-word passages\\n     - Assert: jaccard(M1, M1) == 1.0 (identity check)\\n   b) MinHash: Create two disjoint 10-word passages\\n     - Assert: jaccard(M1, M2) close to 0 (disjoint check)\\n   c) MinHash Containment: Query subset against superset\\n     - Assert: containment(subset, superset) > 0.5\\n   d) SimHash: Two identical passages\\n     - Assert: Hamming(H1, H1) == 0\\n   - Output: baseline_unit_tests.log\\n\\n4. Test evaluation metrics:\\n   - Create mock similarity scores and labels\\n   - Compute precision-recall curve\\n   - Assert: At threshold=1.0, precision=1.0 (or NaN if no positive predictions)\\n   - Assert: At threshold=0.0, recall=1.0\\n   - Assert: Precision + (1-recall) >= 0 for all points\\n   - Output: metric_validation.log\\n\\n# PHASE 2: MINI DATA TEST (30-60 minutes, full pipeline on 3 examples)\\n5. Run full pipeline on mini_data_out.json only:\\n   - All 4 methods on 3 MRPC pairs\\n   - Compute similarities and metrics\\n   - Manually verify a few scores make intuitive sense\\n   - Expected: Should complete in <5 minutes, no crashes\\n   - Output: mini_pipeline_results.json (same schema as method_out.json but tiny)\\n\\n6. Verify mini results:\\n   - Check that landmark-pair and minHash both have results\\n   - Check that similarity scores are in [0, 1]\\n   - Check that precision-recall curve has >=3 points\\n   - If landmark-pair scores are all identical or all zero -> debug landmark extraction\\n   - Output: mini_validation_report.txt\\n\\n# PHASE 3: PREVIEW DATA TEST (1-2 hours, full pipeline on ~400 pairs)\\n7. Run full pipeline on first 400 MRPC pairs (\\\"preview scale\\\"):\\n   - Build TF-IDF corpus on these 400\\n   - Extract landmarks, compute fingerprints, index baselines\\n   - Compute all metrics and ablations (K=5,10,15; W=10,20,50)\\n   - Expected time: ~30-60 minutes depending on compute\\n   - Output: preview_results.json (complete schema, representatively small dataset)\\n\\n8. Validation checks on preview results:\\n   a) Landmark counts:\\n      - Average landmarks per passage: should be K +/- 2 (e.g., 15+-2)\\n      - Assert no passage has 0 landmarks\\n   b) Fingerprint sizes:\\n      - Average |FP|: should scale as ~K^2 / 2 (O(quadratic) in landmark count)\\n      - Landmark-pair FP should be 2-5x larger than MinHash (100s vs 100-200 hashes)\\n   c) Similarity distributions:\\n      - Plot histogram of similarities for each method\\n      - Landmark-pair should show clear bimodal (high for paraphrases, low for non-paraphrases)\\n      - If distribution is uniform -> method not working\\n   d) Ablation results:\\n      - Recall@prec>=0.90 should increase monotonically with K (or plateau)\\n      - Without-delta should have lower precision@recall than with-delta\\n      - If opposite, landmark extraction or hashing is broken\\n   e) Statistical test:\\n      - Two-proportion z-test should yield p < 0.05 if delta is significant\\n      - If p > 0.5, offset is NOT load-bearing -> hypothesis challenge\\n   - Output: preview_validation_report.txt\\n\\n# PHASE 4: DECISION CHECKPOINT\\n9. Decision: Should proceed to full dataset?\\n   If ANY of the following:\\n   - Unit tests FAIL -> Debug landmark extraction / fingerprinting\\n   - Mini pipeline doesn't complete -> Fix crashes before scaling\\n   - Mini results are nonsensical (all zeros, random) -> Rethink approach\\n   - Ablation fails to show significance -> Revisit hypothesis\\n   Otherwise: PROCEED to full data\\n\\n# PHASE 5: FULL DATA RUN (2-3 hours remaining)\\n10. Run full pipeline on all GLUE MRPC + synthetic structural edits:\\n    - Load all 4076 MRPC pairs\\n    - Generate 500-1000 synthetic variants with edits\\n    - Extract landmarks, fingerprint, compute all metrics\\n    - Expected time: 90-180 minutes depending on optimization\\n    - Output: method_out.json with final results\\n\\n# PHASE 6: FINAL VALIDATION\\n11. Sanity checks on final results:\\n    - Landmark-pair recall@prec>=0.90 should be >= 0.5 (at least half of true paraphrases)\\n    - If < 0.3, hypothesis is weak; if > 0.95, possible overfitting on MRPC\\n    - Containment MinHash recall should be > 0.4 (it's a strong baseline)\\n    - Landmark-pair should beat or match containment (or document why it doesn't)\\n    - Synthetic dataset should show larger recall gains vs MRPC\\n      (landmark-pair designed for structural edits, should shine here)\\n    - If synthetic results are worse than MRPC, structural-edit generation may be flawed\\n    - Output: final_validation_report.txt\\n\\n# PHASE 7: VERIFICATION OF HYPOTHESIS VERDICT\\n12. Determine CONFIRM / PARTIAL / DISCONFIRM:\\n    - CONFIRM: landmark-pair recall@prec>=0.90 >= containment recall + 10pp on structural edits\\n      AND positional offset ablation is significant (p<0.05)\\n      AND timing is <10x slower than MinHash\\n    - PARTIAL: Gains only on structural edits, not MRPC\\n      OR Gains <5pp (lower than expected 10-15pp)\\n      OR Statistical significance marginal (p close to 0.05)\\n    - DISCONFIRM: landmark-pair <= containment baseline on both datasets\\n      OR Inverted-index lookup >10x slower than MinHash\\n      OR Cannot extract stable landmarks (too much variance across texts)\\n    - Output: verdict.txt with final interpretation\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [42] ASSISTANT · 2026-07-03 18:16:42 UTC

```
Perfect! I've created the `.terminal_claude_agent_struct_out.json` file in the correct working directory. The plan is now complete and ready for the executor.

## Summary of Deliverable

The plan provides a comprehensive roadmap for implementing and benchmarking landmark-pair text fingerprinting:

**Key Structural Elements:**
- **10-phase implementation** covering data prep, landmark extraction via TF-IDF + scipy local maxima detection, Shazam-inspired anchor-target pair hashing, three baselines (MinHash Jaccard/Containment, SimHash), precision-recall evaluation, ablations, and performance benchmarking
- **Specific parameters**: landmark density K∈{5,10,15,20,30}, lookahead window W∈{10,20,50,100}, corpus size 1M passages for timing
- **Primary metric**: recall@precision≥0.90 on both GLUE MRPC and synthetic structural-edit datasets
- **Core ablation**: two-proportion z-test (α=0.05) comparing fingerprints with vs without positional offset to validate it's load-bearing
- **Detailed output schema**: method_out.json with results tables, precision-recall curves as JSON arrays, ablation p-values and CIs, timing benchmarks, and implementation details

**Testing Strategy:**
- Progressive validation: unit tests → mini data (3 pairs) → preview data (400 pairs) → decision checkpoint → full data (4076 MRPC + 500-1000 synthetic) 
- Early failure detection with explicit pass/fail criteria at each stage
- Sanity checks to catch when the method is not working (all-zero similarities, missing landmarks, etc.)

**Fallback Plans:**
7 specific scenarios (memory overflow, too-dense fingerprints, indexing failures, etc.) with concrete alternatives to keep progress moving

The executor now has everything needed to implement this experiment systematically.
```
