# gen_plan_dataset_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_Bd0c_4hy9OC-` — Near Duplicate Detection
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_dataset_1` (terminal_claude_agent, claude-haiku-4-5)

### [1] CONFIG · 2026-07-03 18:13:12 UTC

```
model: claude-haiku-4-5 | effort: high | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1
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

id: dataset_iter2_dir2
type: dataset
objective: >-
  Construct a real-world near-duplicate benchmark with 5000+ passages and diverse structural-edit types (insertion, deletion,
  embedding, paragraph-reorder) to replace the circular synthetic benchmark.
approach: >-
  Search for existing real-world near-duplicate corpora: (1) CC-News duplicate pairs from Common Crawl (news syndication with
  real boilerplate), (2) ClueWeb near-duplicate benchmark or similar, (3) AllSides matched news articles (same story, different
  publication, genuine different context), (4) contracts or legal document repositories with known variants. Evaluate candidates
  by: scale (≥5000 source passages), edit-type diversity (must include insertion, deletion, embedding, paragraph-reorder),
  manual ground truth validation (spot-check ≥50 pairs). If no suitable dataset exists, construct from: (a) 2000 Wikipedia
  passages randomly selected (>300 words each), (b) apply structural edits using REAL boilerplate sources (Wikipedia article
  talk pages, genuine legal disclaimers, news template headers from Wayback Machine, product reviews with product-description
  insertion), (c) create 5 variants per passage: prepended boilerplate (200-500 tokens), appended boilerplate, sentence insertion
  mid-passage (1-3 sentences), sentence deletion (20-30% middle section), paragraph-reorder (shuffle 2-3 consecutive paragraphs).
  Pair each passage with 10+ unrelated passages as negative examples (non-duplicates). Standardize to JSON: {passage_id, original_text,
  variant_id, variant_text, edit_type ['insertion','deletion','embedding','reorder','control'], is_near_duplicate [true/false],
  source_metadata}. Schema validation (exp_sel_data_out format). Generate splits: full (5000+ originals, 25000+ pairs), mini
  (50 originals, 100 pairs), preview (5 examples). Output data_out.json (~30-100MB for full).
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

### [3] HUMAN-USER prompt · 2026-07-03 18:13:20 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [4] ASSISTANT · 2026-07-03 18:13:30 UTC

```
I'll create a detailed, actionable plan for constructing a real-world near-duplicate benchmark. Let me first research existing datasets to understand what's available and make concrete recommendations.
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
Let me load the built-in web tools and run the searches:
```

### [14] TOOL CALL — ToolSearch · 2026-07-03 18:13:34 UTC

```
{'query': 'select:WebSearch,WebFetch', 'max_results': 2}
```

### [15] TOOL RESULT — ToolSearch · 2026-07-03 18:13:34 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 21}
```

### [16] TOOL CALL — WebSearch · 2026-07-03 18:13:38 UTC

```
CC-News duplicate detection dataset Common Crawl 2025
```

### [17] TOOL CALL — WebSearch · 2026-07-03 18:13:38 UTC

```
PAN-PC plagiarism corpus download near-duplicate
```

### [18] TOOL CALL — WebSearch · 2026-07-03 18:13:38 UTC

```
ClueWeb duplicate dataset benchmark
```

### [19] TOOL CALL — WebSearch · 2026-07-03 18:13:38 UTC

```
Wikipedia near-duplicate detection corpus structural edits
```

### [20] TOOL RESULT — WebSearch · 2026-07-03 18:13:42 UTC

```
{"query": "Wikipedia near-duplicate detection corpus structural edits", "results": [{"tool_use_id": "srvtoolu_01WbwcAVN7xCRmngRngEzDfH", "content": [{"title": "(PDF) Identifying Duplicate and Contradictory Information in Wikipedia", "url": "https://www.researchgate.net/publication/262878126_Identifying_Duplicate_and_Contradictory_Information_in_Wikipedia"}, {"title": "(PDF) Demonstration Wikipedia in the Pocket Indexing Technology for Near-duplicate Detection and High Similarity Search", "url": "https://www.researchgate.net/publication/221301219_Demonstration_Wikipedia_in_the_Pocket_Indexing_Technology_for_Near-duplicate_Detection_and_High_Similarity_Search"}, {"title": "Automated near-duplicate detection for text documents", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12124518"}, {"title": "Identifying Duplicate and Contradictory Information in Wikipedia | Proceedings of the 15th ACM/IEEE-CS Joint Conference on Digital Libraries", "url": "https://dl.acm.org/doi/10.1145/2756406.2756947"}, {"title": "Structured output of duplicate or near-duplicate text documents identified using automated near-duplicate detection for text documents", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12481708"}, {"title": "Expediting automated near-duplicate detection for new text documents", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12450295"}, {"title": "Detecting duplicate and near-duplicate files", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9275143"}, {"title": "Detecting duplicate and near-duplicate files", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7366718"}, {"title": "Clustering of near-duplicate documents", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9355171"}, {"title": "[1406.1143] Identifying Duplicate and Contradictory Information in Wikipedia", "url": "https://ar5iv.labs.arxiv.org/html/1406.1143"}]}, "Based on the search results, here's what I found about Wikipedia near-duplicate detection and structural edits:\n\n## Wikipedia Near-Duplicate Detection\n\nResearchers have identified sentences in Wikipedia articles that are either identical or highly similar by applying minhash techniques in a MapReduce implementation to identify sentences with high Jaccard similarity, followed by generating sentence clusters.\n\n## Types of Near-Duplicates Found\n\nThe research identifies several categories of near-duplicate content in Wikipedia:\n\n1. **Templates**: Templates describe sentences that have identical structure but with different entities, facts, or figures for different topics, reflecting conscious attempts to impose structure across groups of related articles, with the largest template clusters containing tens of thousands of sentences.\n\n2. **Identical Sentences**: Identical sentences are the result of copy and paste, and are often found in articles that cover similar topics or articles that are subtopics of other topics.\n\n3. **Copyediting**: Copyediting refers to nearly identical sentences that differ in stylistic or otherwise non-substantive ways, arising with minor editing after a copy and paste.\n\n## Edit Structure Patterns\n\nAnalysis of large near-duplicate clusters suggests that there are complex edit histories that form tree-like structures."], "durationSeconds": 5.079328495999999, "searchCount": 1}
```

### [21] TOOL RESULT — WebSearch · 2026-07-03 18:13:44 UTC

```
{"query": "ClueWeb duplicate dataset benchmark", "results": [{"tool_use_id": "srvtoolu_012Zbs8jKs6Edzr4monZ9ccH", "content": [{"title": "The ClueWeb09 Dataset", "url": "http://www.lemurproject.org/clueweb09/clueweb09info.php"}, {"title": "cx-cmu/ClueWeb-Reco · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/cx-cmu/ClueWeb-Reco"}, {"title": "The ClueWeb12 Dataset: Dataset Details", "url": "https://lemurproject.org/clueweb12/specs.php"}, {"title": "ClueWeb09 Related Data", "url": "https://lemurproject.org/clueweb09/related-data.php"}, {"title": "RETSim: Resilient and Efficient Text Similarity", "url": "https://arxiv.org/pdf/2311.17264"}, {"title": "Multi-granular Adversarial Attacks against Black-box Neural Ranking   Models", "url": "https://arxiv.org/pdf/2404.01574"}, {"title": "The Impact of Main Content Extraction on Near-Duplicate Detection", "url": "https://arxiv.org/pdf/2111.10864"}, {"title": "Topic-oriented Adversarial Attacks against Black-box Neural Ranking   Models", "url": "https://arxiv.org/pdf/2304.14867"}, {"title": "Benchmarks for measurement of duplicate detection methods in nucleotide databases", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10755258/"}]}, "Based on the search results, here's what I found about ClueWeb duplicate dataset benchmarks:\n\n## ClueWeb Duplicate Content\n\nThe ClueWeb09 Dataset contains about 0.2% duplicate URLs in the Category A set.\n\nIn contrast, the ClueWeb12 version 1.0 dataset inadvertently contained more than 100 million duplicate documents during post-processing when some crawler files were processed twice. To address this, a deduplicated version was created by taking every 14th document from each file after duplicate records were removed.\n\n## Near-Duplicate Detection Benchmark\n\nResearchers have also created a duplicate detection benchmark using ClueWeb data. A dataset of 186,819 ClueWeb document pairs with redundant content (indicated by canonical URLs) was constructed. This involved identifying documents in ClueWeb09 and ClueWeb12 that share the same canonical URL, randomly selecting 5,000 groups, and forming all possible pairs (with a maximum of 50 pairs per group).\n\nThese benchmarks have been used to evaluate near-duplicate detection methods and the impact of content extraction algorithms on duplicate identification."], "durationSeconds": 6.190029007000001, "searchCount": 1}
```

### [22] TOOL RESULT — WebSearch · 2026-07-03 18:13:46 UTC

```
{"query": "CC-News duplicate detection dataset Common Crawl 2025", "results": [{"tool_use_id": "srvtoolu_01MQYB5Nj583sAJGKjxS5Wwi", "content": [{"title": "Common Crawl - Blog - A Sampling of 2025 Research Referencing Common Crawl", "url": "https://commoncrawl.org/blog/a-sampling-of-2025-research-referencing-common-crawl"}, {"title": "Inside Common Crawl: The Dataset Behind AI Models (and Its Real World Limits) - DEV Community", "url": "https://dev.to/extractdata/inside-common-crawl-the-dataset-behind-ai-models-and-its-real-world-limits-2eo2"}, {"title": "ContinuousBench: Can Differentially Private Synthetic Text Improve Capabilities?", "url": "https://arxiv.org/pdf/2606.01849"}, {"title": "ViClickbait-2025: A comprehensive dataset for Vietnamese clickbait detection", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12557553/"}, {"title": "Infini-News: Efficiently Queryable Access to 1.3 Billion Processed Common Crawl News Articles", "url": "https://arxiv.org/html/2605.18337"}, {"title": "Reliability Estimation of News Media Sources: Birds of a Feather Flock   Together", "url": "https://arxiv.org/pdf/2404.09565"}, {"title": "RETSim: Resilient and Efficient Text Similarity", "url": "https://arxiv.org/pdf/2311.17264"}, {"title": "Statistics of Common Crawl Monthly Archives by commoncrawl", "url": "https://commoncrawl.github.io/cc-crawl-statistics/plots/languages"}, {"title": "CCQA: A New Web-Scale Question Answering Dataset for Model Pre-Training", "url": "https://arxiv.org/pdf/2110.07731"}, {"title": "HunSum-1: an Abstractive Summarization Dataset for Hungarian", "url": "https://arxiv.org/pdf/2302.00455"}]}, "Based on the search results, here's what I found about CC-News and duplicate detection in the context of Common Crawl:\n\n## CC-News Dataset\n\nThe Common Crawl Foundation maintains the Common Crawl News Dataset (CC-News), the world's largest collection of news articles crawled from global news web sites since 2016. The data is updated daily and published as a series of snapshots organized by year and month.\n\n## Duplicate Detection Challenges\n\nCommon Crawl captures the same pages across multiple crawls, sometimes hundreds of times, meaning a lot of duplicate data that needs deduplication before use.\n\n## Deduplication Approaches\n\nRecent research shows practical implementations of deduplication techniques. One approach involves two-pass deduplication: Pass 1 removes exact duplicates globally via SHA-256 hashing of article text, and Pass 2 performs near-deduplication using MinHash LSH with 128 permutations, word 5-gram shingles, and a containment similarity threshold of 0.80.\n\n## Related Work\n\nRecent projects process the entirety of CC-News from its 2016 inception onward, preserving its multilingual, cross-country coverage.\n\nThe search results show that while there isn't a specific \"CC-News duplicate detection dataset\" by that exact name released in 2025, the challenge of duplicate detection in CC-News data is an active area of research, with various methodologies being applied to handle this issue."], "durationSeconds": 8.482935537000001, "searchCount": 1}
```

### [23] TOOL RESULT — WebSearch · 2026-07-03 18:13:46 UTC

```
{"query": "PAN-PC plagiarism corpus download near-duplicate", "results": [{"tool_use_id": "srvtoolu_014nH8PLcgYLvCf9kq93q7hy", "content": [{"title": "Corpus statistics for 26 939 documents and 61 064 plagiarism cases in... | Download Table", "url": "https://www.researchgate.net/figure/Corpus-statistics-for-26-939-documents-and-61-064-plagiarism-cases-in-the-PAN-PC-11_tbl1_221159623"}, {"title": "Performances of 9 external plagiarism detector on the PAN-PC-11. The... | Download Scientific Diagram", "url": "https://www.researchgate.net/figure/Performances-of-9-external-plagiarism-detector-on-the-PAN-PC-11-The-detectors-are_tbl2_221159623"}, {"title": "PAN Plagiarism Corpus PAN-PC-09 | Request PDF", "url": "https://www.researchgate.net/publication/242823978_PAN_Plagiarism_Corpus_PAN-PC-09"}, {"title": "Plagiarism detection performance on the entire PAN-PC-10. | Download Table", "url": "https://www.researchgate.net/figure/Plagiarism-detection-performance-on-the-entire-PAN-PC-10_tbl1_221159542"}, {"title": "Detecting Cross-Language Plagiarism using Open Knowledge Graphs", "url": "https://arxiv.org/pdf/2111.09749"}, {"title": "Webis Data PAN-PC-11", "url": "https://webis.de/data/pan-pc-11.html"}, {"title": "Dataset Search - PAN Plagiarism Corpus 2011 (PAN-PC-11)", "url": "https://toolbox.google.com/datasetsearch/search?query=pan-pc-11"}, {"title": "PAN Plagiarism Corpus 2011 (PAN-PC-11)", "url": "https://zenodo.org/records/3250095"}, {"title": "Corpus statistics for 27 073 documents and 68 558 plagiarism cases in... | Download Table", "url": "https://www.researchgate.net/figure/Corpus-statistics-for-27-073-documents-and-68-558-plagiarism-cases-in-PAN-PC-10_tbl1_220466568"}, {"title": "Taxonomy of Mathematical Plagiarism", "url": "https://arxiv.org/pdf/2401.16969"}]}, "Based on the search results, here's information about the PAN-PC plagiarism corpus:\n\n## Overview\n\nThe PAN-PC corpora are an outcome of PAN (Plagiarism analysis, Authorship attribution, and Near-duplicate detection) and share different tasks involved in plagiarism detection including paraphrased plagiarism detection. PAN-PC is a set of three benchmark corpora: PAN-PC-09, PAN-PC-10, and PAN-PC-11.\n\n## Corpus Features\n\nThese corpora have various features, such as intrinsic and extrinsic plagiarism cases, translated cases of plagiarism from German and Spanish languages to English, and a variety of plagiarism types (verbatim, paraphrased, and independently written) created artificially and manually.\n\n## Download Information\n\nFor the most recent version (PAN-PC-11):\n\nThe PAN plagiarism corpus 2011 (PAN-PC-11) is a corpus for the evaluation of automatic plagiarism detection algorithms and can be used free of charge for research purposes. The dataset can be downloaded from Zenodo.\n\nThe PAN-PC-11 contains documents in which plagiarism has been inserted automatically as well as documents in which plagiarism has been inserted manually, constructed using a random plagiarist computer program or crowdsourced via Amazon's Mechanical Turk."], "durationSeconds": 8.524270263999995, "searchCount": 1}
```

### [24] TOOL CALL — WebFetch · 2026-07-03 18:13:50 UTC

```
URL: https://zenodo.org/records/3250095
Prompt: What is the dataset size, structure, plagiarism types, and how can it be downloaded?
```

### [25] TOOL CALL — WebFetch · 2026-07-03 18:13:50 UTC

```
URL: https://webis.de/data/pan-pc-11.html
Prompt: What are the corpus statistics, plagiarism types included, and download instructions?
```

### [26] TOOL CALL — WebSearch · 2026-07-03 18:13:50 UTC

```
news article syndication duplicate dataset SemEval
```

### [27] TOOL CALL — WebSearch · 2026-07-03 18:13:50 UTC

```
legal contracts dataset near-duplicate reuse corpus
```

### [28] TOOL RESULT — WebFetch · 2026-07-03 18:13:50 UTC

```
{"bytes": 0, "code": 403, "codeText": "Forbidden", "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.", "durationMs": 465, "url": "https://webis.de/data/pan-pc-11.html"}
```

### [29] TOOL RESULT — WebFetch · 2026-07-03 18:13:56 UTC

```
{"bytes": 81003, "code": 200, "codeText": "OK", "result": "# PAN Plagiarism Corpus 2011 Dataset Overview\n\n**Dataset Size:**\nThe corpus totals 1.7 GB across two compressed files: part1 (1.0 GB) and part2 (703.9 MB).\n\n**Structure:**\nThe PAN-PC-11 contains documents with inserted plagiarism instances designed for evaluating automated detection algorithms. The corpus includes two categories of plagiarized content: artificially generated using a random plagiarist computer program, and manually crafted through crowdsourcing via Amazon Mechanical Turk.\n\n**Plagiarism Types:**\nWhile the page doesn't explicitly enumerate plagiarism types, it indicates the corpus was constructed \"using a so-called random plagiarist, a computer program which constructs plagiarism according to a number of parameters,\" suggesting algorithmic variation in plagiarism instances alongside manually inserted examples.\n\n**Download Instructions:**\nBoth RAR files are available on Zenodo with direct download links. Users can retrieve them individually:\n- Part 1 (MD5: b2930f859497dd48ba5bb606d3f4a4f3)\n- Part 2 (MD5: b23d86c17a47d2bfbdc4c314ea5810df)\n\n**Access & License:**\nThe dataset is freely available for research under a Creative Commons Attribution 4.0 International license, with DOI: 10.5281/zenodo.3250095.", "durationMs": 6155, "url": "https://zenodo.org/records/3250095"}
```

### [30] TOOL RESULT — WebSearch · 2026-07-03 18:13:58 UTC

```
{"query": "legal contracts dataset near-duplicate reuse corpus", "results": [{"tool_use_id": "srvtoolu_01HJ3VSyzTRNyvbpQ3aPbQnT", "content": [{"title": "LAUKIN: A Multi-jurisdictional Common Law Contract Dataset", "url": "https://arxiv.org/html/2606.13184v1"}, {"title": "ACORD: An Expert-Annotated Dataset for Legal Contract Clause Retrieval", "url": "https://arxiv.org/html/2501.06582v2"}, {"title": "A survey of classification tasks and approaches for legal contracts | Artificial Intelligence Review | Springer Nature Link", "url": "https://link.springer.com/article/10.1007/s10462-025-11359-8"}, {"title": "Pile of Law: Learning Responsible Data Filtering from the Law and a   256GB Open-Source Legal Dataset", "url": "https://arxiv.org/pdf/2207.00220"}, {"title": "A large dataset of scientific text reuse in Open-Access publications", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9879940/"}, {"title": "The Material Contracts Corpus", "url": "https://arxiv.org/pdf/2504.02864"}, {"title": "theatticusproject/cuad-qa · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/theatticusproject/cuad-qa"}, {"title": "The Material Contracts Corpus", "url": "https://arxiv.org/html/2504.02864v1"}]}, "Based on the search results, here are several relevant legal contracts datasets that address near-duplicate reuse and corpus issues:\n\n## Key Datasets\n\n**LAUKIN Dataset**: This multi-jurisdictional common law contract dataset addresses near-duplicate clauses by applying deduplication within jurisdictions using rapidfuzz, where pairwise similarity is computed and any two clauses scoring ≥90% are grouped into a duplicate cluster, retaining only the longest clause. This per-jurisdiction deduplication reduces the final corpus to 36K+, 32K+, and 9K+ clauses for Australia, the UK, and India, respectively.\n\n**ACORD Dataset**: ACORD (Atticus Clause Retrieval Dataset) is the first expert-annotated retrieval benchmark explicitly designed for contract drafting, addressing the challenge of retrieving complex and heavily negotiated contract clauses, such as Limitation of Liability, Indemnification, Most Favored Nation, and Termination for Convenience.\n\n**Material Contracts Corpus (MCC)**: The Material Contracts Corpus is a publicly available dataset comprising over one million contracts filed by public companies with the U.S. Securities and Exchange Commission (SEC) between 2000 and 2023, facilitating empirical research on contract design and legal language, and supporting the development of AI-based legal tools.\n\n**CUAD Dataset**: Contract Understanding Atticus Dataset (CUAD) v1 is a corpus of more than 13,000 labels in 510 commercial legal contracts that have been manually labeled to identify 41 categories of important clauses.\n\nThese datasets represent different approaches to handling contract reuse, deduplication, and clause retrieval challenges in legal text."], "durationSeconds": 7.470162691999998, "searchCount": 1}
```

### [31] TOOL RESULT — WebSearch · 2026-07-03 18:13:58 UTC

```
{"query": "news article syndication duplicate dataset SemEval", "results": [{"tool_use_id": "srvtoolu_01RYVyB3nuyWrakw5JSjhWBw", "content": [{"title": "SemEval-2022 Task 8: Multilingual news article similarity - ACL Anthology", "url": "https://aclanthology.org/2022.semeval-1.155/"}, {"title": "Duplicate News Story Detection Revisited | Request PDF", "url": "https://www.researchgate.net/publication/291586658_Duplicate_News_Story_Detection_Revisited"}, {"title": "Hierarchical Level-Wise News Article Clustering via Multilingual Matryoshka Embeddings", "url": "https://arxiv.org/pdf/2506.00277"}, {"title": "SemEval-2022 Task 8: Multilingual news article similarity", "url": "https://aclanthology.org/2022.semeval-1.155.pdf"}, {"title": "SemEval-2022 Task 8: Multilingual news article similarity", "url": "https://zenodo.org/records/6507872"}, {"title": "RETSim: Resilient and Efficient Text Similarity", "url": "https://arxiv.org/pdf/2311.17264"}, {"title": "Duplicate News Story Detection Revisited Omar Alonso Microsoft Corporation", "url": "https://www.microsoft.com/en-us/research/wp-content/uploads/2013/05/paper-1.pdf"}, {"title": "Duplicate News Story Detection Revisited | Springer Nature Link", "url": "https://link.springer.com/chapter/10.1007/978-3-642-45068-6_18"}, {"title": "SemEval2023 shared task on \"Detecting the Genre, the Framing, and the Persuasion Techniques in Online News in a Multi-lingual Setup\"", "url": "https://propaganda.math.unipd.it/semeval2023task3/"}, {"title": "SemEval 2022 Task 8: Multilingual News Article Similarity", "url": "https://competitions.codalab.org/competitions/33835"}]}, "Based on the search results, here's what I found about news article syndication and duplicate datasets in relation to SemEval:\n\n## SemEval-2022 Task 8: Multilingual News Article Similarity\n\nA new dataset of nearly 10,000 news article pairs spanning 18 language combinations was introduced for SemEval 2022 Task 8, annotated for seven dimensions of similarity.\n\nThe dataset contains pairs of news articles from the first half of 2020 annotated for seven aspects of similarity: GEO (geographic focus), ENT (named entities), TIME (relevant time periods), NAR (narrative schemas), OVERALL (whether articles cover the same substantive news story), and STYLE (writing styles).\n\n## Syndication and Duplicate Detection\n\nNews articles are particularly challenging due to the prevalence of syndicated articles, where very similar articles are run with different headlines and surrounded by different HTML markup and site templates. These stories often consist primarily of syndicated information, with local replacement of headlines and captions, and by detecting near-duplicates, users can be offered only stories with content materially different from previously-viewed versions.\n\nNews article similarity measures facilitate important tasks such as clustering of news, duplicate news detection, fact-checking, and tracking of the spread of news."], "durationSeconds": 7.660708667999999, "searchCount": 1}
```

### [32] ASSISTANT · 2026-07-03 18:14:02 UTC

```
Now let me search for more specific information about synthetic benchmark creation and evaluation methodologies:
```

### [33] TOOL CALL — WebSearch · 2026-07-03 18:14:02 UTC

```
MinHash containment benchmark evaluation precision recall
```

### [34] TOOL CALL — WebSearch · 2026-07-03 18:14:02 UTC

```
paragraph reordering text edit synthesis evaluation
```

### [35] TOOL RESULT — WebSearch · 2026-07-03 18:14:08 UTC

```
{"query": "paragraph reordering text edit synthesis evaluation", "results": [{"tool_use_id": "srvtoolu_01N9kWzpPvkL5uMdKx6bRNk6", "content": [{"title": "The Complete Guide for Re-order Paragraph in PTE Reading | MarvelPTE", "url": "https://marvelpte.com/reorder-paragraph-complete-guide/"}, {"title": "Document data structure for linking a text editor with integrated editing tools", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11868589"}, {"title": "Method and apparatus for removing redundant information from digital documents", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7017113"}, {"title": "Layout-Aware Text Editing for Efficient Transformation of Academic PDFs to Markdown", "url": "https://arxiv.org/html/2512.18115v1"}, {"title": "RAVEL: Reasoning Agents for Validating and Evaluating LLM Text Synthesis", "url": "https://arxiv.org/pdf/2603.00686"}, {"title": "Text editor and integrated outline tool linked through a shared document data structure", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11599250"}, {"title": "Evaluation synthesis analysis can be accelerated through text mining, searching, and highlighting: A case-study on data extraction from 631 UNICEF evaluation reports", "url": "https://www.medrxiv.org/content/10.1101/2024.08.27.24312630.full.pdf"}, {"title": "Neural Pipeline for Zero-Shot Data-to-Text Generation", "url": "https://arxiv.org/pdf/2203.16279"}, {"title": "Chapter 33: Synthesis for Research Writing – English 1110 and 1120 Central New Mexico Community College", "url": "https://nmoer.pressbooks.pub/english1101/chapter/chapter-23-2-synthesis-writing-mytext-cnm/"}]}, "Based on the search results, here's what I found about paragraph reordering, text editing, synthesis, and evaluation:\n\n## Text Editing and Paragraph Reordering Tools\n\nSentence reorder tools in integrated text editors display sentences as elements within lists corresponding to paragraphs and allow users to move sentences to reorder them. When a user moves a sentence within a sentence reorder tool, the document tool applies a corresponding movement of the sentence within the document itself.\n\n## Text Synthesis Evaluation\n\nC3EBENCH is a comprehensive benchmark designed to isolate and evaluate the distinct capabilities required for agentic text synthesis. This framework includes one coarse-grained task (End2End) and three fine-grained subtasks (Expand, Cloze, Edit), which evaluate different aspects of the text generation process. These tasks evaluate LLMs across varying levels of granularity, from end-to-end generation to specific editing capabilities.\n\n## Synthesis Writing\n\nA synthesis essay should be organized so that others can understand the sources and evaluate comprehension of them and their presentation of specific data, themes, etc.\n\nThe search results contain a mix of resources related to text editing tools with paragraph reordering features, benchmarks for evaluating text synthesis with LLMs, and educational materials on synthesis writing."], "durationSeconds": 6.812461766, "searchCount": 1}
```

### [36] TOOL RESULT — WebSearch · 2026-07-03 18:14:08 UTC

```
{"query": "MinHash containment benchmark evaluation precision recall", "results": [{"tool_use_id": "srvtoolu_01Nj2evmS2RFAzhW26UdW7H1", "content": [{"title": "Benchmark Contamination in LLMs: Detection & Mitigation Strategies - Interactive | Michael Brenndoerfer | Michael Brenndoerfer", "url": "https://mbrenndoerfer.com/writing/benchmark-contamination-llm-detection-mitigation"}, {"title": "GitHub - tmpsrcrepo/benchmark_minhash_lsh: insight data engineering fellow project", "url": "https://github.com/tmpsrcrepo/benchmark_minhash_lsh"}, {"title": "A Memory-Efficient Sketch Method for Estimating High ...", "url": "https://arxiv.org/pdf/1905.08977"}, {"title": "Retrieve, Merge, Predict: Augmenting Tables with Data Lakes", "url": "https://arxiv.org/pdf/2402.06282"}, {"title": "MinHash LSH — datasketch 1.10.0 documentation", "url": "https://ekzhu.com/datasketch/lsh.html"}, {"title": "Minner: Improved Similarity Estimation and Recall on MinHashed Databases", "url": "https://thomasahle.com/papers/minner.pdf"}, {"title": "LexicHash: sequence similarity estimation via lexicographic comparison of hashes", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10628434/"}, {"title": "Mash Screen: high-throughput sequence containment estimation for genome discovery", "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6833257/"}, {"title": "MinHash LSH Ensemble — datasketch 1.10.0 documentation", "url": "https://ekzhu.com/datasketch/lshensemble.html"}]}, "I've performed the web search for \"MinHash containment benchmark evaluation precision recall\". Here are the key findings:\n\n## Key Results:\n\n**Containment Estimation:**\nContainment is a \"normalized\" intersection that measures the fraction of the query set contained in another set. The MinHash algorithm cannot reliably estimate the containment of a genome within a metagenome, though an online algorithm has been developed capable of measuring the containment of genomes and proteomes within sequencing read sets.\n\n**Precision-Recall Trade-offs:**\nMinHash has a threshold that can be tweaked to reduce the number of candidates retrieved, though recall drops sharply at high thresholds. Larger k-values in MinHash give greater confidence in identifying alignments (high precision) but can lead to many missing alignments (low recall).\n\n**Benchmark Performance:**\nMore permutation functions in MinHash improves accuracy but increases query cost, with average recall, precision, and query time typically plotted against the number of permutation functions. MinHash returns thousands of candidates for larger datasets, of which only a fraction are selected due to very low average containment.\n\n**Related Methods:**\nLexicHash, a variant of MinHash, showed an average improvement of 20.9% over standard MinHash in terms of the area under precision-recall curves."], "durationSeconds": 7.100760425999994, "searchCount": 1}
```

### [37] ASSISTANT · 2026-07-03 18:14:48 UTC

```
Perfect. Now I have sufficient research to create a detailed, actionable plan. Let me write the JSON output:
```

### [38] TOOL CALL — Write · 2026-07-03 18:14:48 UTC

```
File: /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.terminal_claude_agent_struct_out.json

{
  "title": "Real-world + Synthetic Near-duplicate Benchmark",
  "summary": "Construct a 5000+ passage near-duplicate detection benchmark combining real-world data from PAN-PC-11 plagiarism corpus and CC-News syndication with controlled synthetic structural edits (insertion, deletion, embedding, paragraph-reorder) to evaluate landmark-pair fingerprinting against MinHash baselines. Outputs: full dataset (25K+ pairs), mini split (100 pairs), preview (5 examples), standardized JSON with edit-type labels and ground-truth near-duplicate flags.",
  "runpod_compute_profile": "cpu_heavy",
  "ideal_dataset_criteria": "5000+ source passages with diverse near-duplicate types; edit-type labels (insertion, deletion, embedding, paragraph-reorder, control); paired with 10+ negative examples per source; manual spot-check validation (≥50 pairs); JSON format with schema {passage_id, original_text, variant_id, variant_text, edit_type, is_near_duplicate, source_metadata}; total size 30-100MB; splits: full (5000+ originals, 25000+ pairs), mini (50 originals, 100 pairs), preview (5 examples).",
  "dataset_search_plan": "PHASE 1: SOURCE ACQUISITION (Real-world baseline)\n\n1.1 PAN-PC-11 Plagiarism Corpus (PRIMARY REAL-WORLD SOURCE)\n   - Source: Zenodo https://zenodo.org/records/3250095 (freely available, CC-BY 4.0)\n   - Size: 27,073 documents with 68,558 plagiarism cases (total 1.7 GB, downloadable as 2 RAR files)\n   - Content: Artificially-generated plagiarism via random program + manually-crafted via crowdsourcing\n   - Plagiarism types included: verbatim copy, paraphrased, automatically-synthesized variations\n   - Executor task: Extract source-plagiarism pairs from metadata XML, filter for >300-word passages, deduplicate\n   - Expected yield: 3000-5000 passage pairs with structured plagiarism labels\n   - Validation approach: Spot-check 50 pairs to confirm edit types match artifact expectations (paraphrase vs structural)\n\n1.2 CC-News Syndication Dataset (SECONDARY REAL-WORLD SOURCE)\n   - Source: Common Crawl News (daily updates, multilingual since 2016)\n   - Challenge: No pre-packaged \"CC-News duplicate pairs\" dataset; requires custom extraction\n   - Feasibility: Rather than full Common Crawl, use Infini-News processed index (https://arxiv.org/html/2605.18337)\n   - Corpus: 1.3B processed Common Crawl news articles with deduplication metadata\n   - Executor task: Query Infini-News for same-story articles across different publications (e.g., AP Wire vs local news)\n   - Expected approach: Identify articles with high Jaccard overlap (>0.8) via sampling; validate 50-100 pairs\n   - Expected yield: 500-1000 high-quality syndicated article pairs (real boilerplate, real structural variation)\n   - Fallback if Infini-News API unavailable: Use pre-built news similarity dataset from SemEval-2022 Task 8 (Zenodo https://zenodo.org/records/6507872, ~10K multilingual news pairs, annotated for similarity dimensions)\n\n1.3 Legal Contracts Dataset (OPTIONAL supplemental source for diverse domain)\n   - Source: Material Contracts Corpus (SEC filings, 1M+ contracts 2000-2023)\n   - Relevance: High prevalence of clause reuse and boilerplate → demonstrates insertion/embedding edits\n   - Executor task: If time permits, sample 200-300 contracts with known duplicate clauses (via rapidfuzz ≥90% match)\n   - Expected yield: 300-500 passage pairs from legal domain (out-of-domain validation)\n   - Note: OPTIONAL; prioritize PAN-PC-11 + CC-News if time-constrained\n\nPHASE 2: SYNTHETIC BENCHMARK CONSTRUCTION (Controlled structural edits)\n\n2.1 Wikipedia Base Passages (SYNTHETIC VARIANT GENERATION SOURCE)\n   - Acquire: 2000 Wikipedia passages >300 words each from Wikipedia API or HuggingFace wiki dataset\n   - Selection: Random sample ensuring diversity across categories (science, history, culture, sports)\n   - Preprocessing: Remove infoboxes, references, tables; keep main prose only\n   - Expected size: 2000 originals × 5 variants = 10,000 synthetic pairs + negatives\n\n2.2 Boilerplate Injection Sources (REALISTIC SYNTHETIC EDITS)\n   For insertion and embedding edits, apply REAL boilerplate rather than random text:\n   - Wikipedia article talk pages: Download 100-200 example talk page sections (metadata, edit history)\n   - News headers: Scrape canonical news template headers from Web Archive (e.g., \"Published by\\n...\", \"Share this\", \"Related articles\")\n   - Legal disclaimers: Collect 20-30 standard legal disclaimers from SEC forms, ToS pages\n   - Product descriptions: Sample 50 product-description templates from review sites\n   - Executor task: Build a boilerplate corpus (~2-5MB) and apply randomly during edit generation\n\n2.3 Edit Type Generators (Controlled synthetic variations)\n   For each of 2000 Wikipedia passages, generate 5 variants:\n   \n   a) INSERTION (prepend boilerplate)\n      - Select random boilerplate from corpus (200-500 tokens)\n      - Prepend to passage start\n      - Mark as edit_type: \"insertion\"\n      - Edit distance: ~1500 tokens added at boundary\n   \n   b) DELETION (remove middle section)\n      - Delete 1-3 consecutive paragraphs from middle 50% of passage\n      - Retain first and last paragraphs for continuity\n      - Mark as edit_type: \"deletion\"\n      - Edit distance: 20-30% of passage removed\n   \n   c) EMBEDDING (surround with boilerplate)\n      - Prepend + append different boilerplate sections\n      - Total added text: 400-1000 tokens\n      - Mark as edit_type: \"embedding\"\n      - Analogous to article syndication in different contexts\n   \n   d) PARAGRAPH-REORDER (shuffle consecutive paragraphs)\n      - Identify paragraph boundaries (empty line separation)\n      - Randomly swap 2-3 consecutive paragraphs\n      - Mark as edit_type: \"reorder\"\n      - Key test: preserves local landmark relationships despite positional shifts\n      - Paragraph count must be ≥4 to enable reordering\n   \n   e) CONTROL (no edit)\n      - Identical to original\n      - Mark as edit_type: \"control\"\n      - Ground truth: is_near_duplicate = true (identical)\n\n2.4 Negative Example Generation\n   For each passage (original or variant), pair with 10-15 unrelated passages as negatives:\n   - Negatives: Random Wikipedia passages from different categories\n   - Mark all negatives as is_near_duplicate: false\n   - Expected: 2000 originals × 15 negatives = 30,000 negative pairs\n   - Prevents class imbalance; ensures benchmark tests both positive and negative discrimination\n\nPHASE 3: INTEGRATION & STANDARDIZATION\n\n3.1 Merge Real + Synthetic Data\n   - Real-world: PAN-PC-11 pairs + CC-News pairs + legal contracts (if included)\n   - Synthetic: Wikipedia variants (2000 × 5 = 10,000 pairs) + negatives (30,000 pairs)\n   - Total: 5000-7000 unique source passages, 40,000-50,000 total pairs\n   - Subset to target: 5000+ originals → 25,000-30,000 pairs for full dataset\n\n3.2 JSON Standardization (exp_sel_data_out format)\n   Each row in data_out.json:\n   {\n     \"passage_id\": \"unique-source-id\",\n     \"original_text\": \"full text of source passage\",\n     \"variant_id\": \"unique-variant-id-or-null\",\n     \"variant_text\": \"edited/paired variant text\",\n     \"edit_type\": \"[insertion|deletion|embedding|reorder|control|paraphrase|copy]\",\n     \"is_near_duplicate\": true/false,\n     \"source_metadata\": {\n       \"source\": \"[pan-pc-11|cc-news|legal|wikipedia-synthetic]\",\n       \"domain\": \"[news|legal|encyclopedia|general]\",\n       \"original_length_tokens\": 500,\n       \"variant_length_tokens\": 700,\n       \"edit_distance_jaccard\": 0.75,\n       \"manual_validation\": true/false/null\n     }\n   }\n\n3.3 Splits Generation\n   - full: 5000+ source passages, 25,000+ pairs (40-100MB)\n   - mini: 50 source passages, 250 pairs (200KB)\n   - preview: 5 source passages, 25 pairs (10KB)\n   - Each split maintains ratio of edit types (insertion 20%, deletion 20%, embedding 20%, reorder 20%, control 10%, negatives 10%)\n\n3.4 Schema Validation\n   - Use aii-json skill to validate all rows against the schema above\n   - Enforce: passage_id uniqueness, is_near_duplicate ∈ {true, false}, edit_type ∈ allowed values\n   - Flag any missing required fields\n   - Generate summary statistics: total pairs, edit-type histogram, source distribution\n\nPHASE 4: QUALITY ASSURANCE\n\n4.1 Manual Spot-Check (≥50 pairs)\n   - Sample 50 pairs stratified by:\n     - Source (PAN-PC-11: 20, CC-News: 15, synthetic: 15)\n     - Edit type (10 per edit type)\n   - For each pair:\n     - Read both texts\n     - Verify edit_type label is correct\n     - Assess is_near_duplicate ground truth (does it look like a real near-dup?)\n     - Flag misclassifications\n   - Document discrepancy rate; if >5%, reprocess\n\n4.2 Length and Coverage Validation\n   - Verify all passages >300 words (or justify exceptions)\n   - Confirm edit-type distribution matches plan (all 5 types represented)\n   - Check for leakage: no passage appears in both training and negative sets\n   - Report statistics: min/max/mean passage length, pair count per edit type\n\nPHASE 5: FAILURE SCENARIOS & MITIGATIONS\n\n5.1 If PAN-PC-11 Zenodo download fails\n   - Fallback: Use PAN plagiarism papers (ResearchGate PDFs) to manually extract example pairs\n   - Fallback 2: Use MRPC (Microsoft Research Paraphrase Corpus, 5K pairs) as lightweight substitute\n   - Impact: Reduces real-world diversity; synthetic benchmark becomes primary\n\n5.2 If CC-News/Infini-News unavailable or API-rate-limited\n   - Fallback: Use SemEval-2022 Task 8 multilingual news dataset (Zenodo, 10K pairs, pre-built)\n   - Impact: Reduces news-domain scale; dataset remains viable\n\n5.3 If Wikipedia API quota exhausted\n   - Fallback: Use HuggingFace \"wikipedia\" dataset (pre-cached, unlimited)\n   - Impact: Minimal; Wikipedia data is stable\n\n5.4 If boilerplate corpus insufficient\n   - Fallback: Generate synthetic boilerplate using common templates (\"Top Articles\", \"Latest News\", etc.)\n   - Impact: Reduces realism; still valid for testing insertion/embedding robustness\n\n5.5 If paragraph-reorder edit fails (insufficient paragraph count)\n   - Fallback: Only apply reorder to passages with ≥4 paragraphs; skip others (mark as control instead)\n   - Impact: May reduce reorder variant count; acceptable trade-off\n\nEXECUTOR DELIVERABLES:\n\n- data_out.json: Full dataset, 25,000+ pairs, ~40-100MB\n- data_out_mini.json: Mini split, 250 pairs, ~200KB\n- data_out_preview.json: Preview split, 25 pairs, ~10KB\n- schema_validation_report.txt: Line-by-line validation errors (if any)\n- quality_assurance_report.txt: 50-pair spot-check results, discrepancy rate, recommendations\n- dataset_statistics.json: Edit-type histogram, source distribution, length statistics, pair counts\n- README.md: Dataset documentation (sources, edit types, limitations, validation notes)\n\nCRITICAL SUCCESS CRITERIA:\n\n✓ ≥5000 source passages with ≥25,000 pairs\n✓ All 5 edit types represented (insertion, deletion, embedding, reorder, control)\n✓ Real-world data from PAN-PC-11 (mandatory); CC-News (strongly preferred); legal (optional)\n✓ Manual validation of ≥50 pairs; ≤5% discrepancy in is_near_duplicate labels\n✓ JSON schema fully validated with aii-json\n✓ Total size fits within 100MB; splits provided (full, mini, preview)\n✓ Execution completed within 6h time budget\n\nESTIMATED TIME ALLOCATION:\n- Phase 1 (source acquisition): 1.5h\n- Phase 2 (synthetic generation): 2h\n- Phase 3 (integration & standardization): 1h\n- Phase 4 (QA): 1h\n- Phase 5 (troubleshooting & documentation): 0.5h\n- Buffer: 0.5h\nTOTAL: ~6h\n",
  "target_num_datasets": 1
}
```

### [39] TOOL RESULT — Write · 2026-07-03 18:14:48 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Real-world + Synthetic Near-duplicate Benchmark\",\n  \"summary\": \"Construct a 5000+ passage near-duplicate detection benchmark combining real-world data from PAN-PC-11 plagiarism corpus and CC-News syndication with controlled synthetic structural edits (insertion, deletion, embedding, paragraph-reorder) to evaluate landmark-pair fingerprinting against MinHash baselines. Outputs: full dataset (25K+ pairs), mini split (100 pairs), preview (5 examples), standardized JSON with edit-type labels and ground-truth near-duplicate flags.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"ideal_dataset_criteria\": \"5000+ source passages with diverse near-duplicate types; edit-type labels (insertion, deletion, embedding, paragraph-reorder, control); paired with 10+ negative examples per source; manual spot-check validation (≥50 pairs); JSON format with schema {passage_id, original_text, variant_id, variant_text, edit_type, is_near_duplicate, source_metadata}; total size 30-100MB; splits: full (5000+ originals, 25000+ pairs), mini (50 originals, 100 pairs), preview (5 examples).\",\n  \"dataset_search_plan\": \"PHASE 1: SOURCE ACQUISITION (Real-world baseline)\\n\\n1.1 PAN-PC-11 Plagiarism Corpus (PRIMARY REAL-WORLD SOURCE)\\n   - Source: Zenodo https://zenodo.org/records/3250095 (freely available, CC-BY 4.0)\\n   - Size: 27,073 documents with 68,558 plagiarism cases (total 1.7 GB, downloadable as 2 RAR files)\\n   - Content: Artificially-generated plagiarism via random program + manually-crafted via crowdsourcing\\n   - Plagiarism types included: verbatim copy, paraphrased, automatically-synthesized variations\\n   - Executor task: Extract source-plagiarism pairs from metadata XML, filter for >300-word passages, deduplicate\\n   - Expected yield: 3000-5000 passage pairs with structured plagiarism labels\\n   - Validation approach: Spot-check 50 pairs to confirm edit types match artifact expectations (paraphrase vs structural)\\n\\n1.2 CC-News Syndication Dataset (SECONDARY REAL-WORLD SOURCE)\\n   - Source: Common Crawl News (daily updates, multilingual since 2016)\\n   - Challenge: No pre-packaged \\\"CC-News duplicate pairs\\\" dataset; requires custom extraction\\n   - Feasibility: Rather than full Common Crawl, use Infini-News processed index (https://arxiv.org/html/2605.18337)\\n   - Corpus: 1.3B processed Common Crawl news articles with deduplication metadata\\n   - Executor task: Query Infini-News for same-story articles across different publications (e.g., AP Wire vs local news)\\n   - Expected approach: Identify articles with high Jaccard overlap (>0.8) via sampling; validate 50-100 pairs\\n   - Expected yield: 500-1000 high-quality syndicated article pairs (real boilerplate, real structural variation)\\n   - Fallback if Infini-News API unavailable: Use pre-built news similarity dataset from SemEval-2022 Task 8 (Zenodo https://zenodo.org/records/6507872, ~10K multilingual news pairs, annotated for similarity dimensions)\\n\\n1.3 Legal Contracts Dataset (OPTIONAL supplemental source for diverse domain)\\n   - Source: Material Contracts Corpus (SEC filings, 1M+ contracts 2000-2023)\\n   - Relevance: High prevalence of clause reuse and boilerplate → demonstrates insertion/embedding edits\\n   - Executor task: If time permits, sample 200-300 contracts with known duplicate clauses (via rapidfuzz ≥90% match)\\n   - Expected yield: 300-500 passage pairs from legal domain (out-of-domain validation)\\n   - Note: OPTIONAL; prioritize PAN-PC-11 + CC-News if time-constrained\\n\\nPHASE 2: SYNTHETIC BENCHMARK CONSTRUCTION (Controlled structural edits)\\n\\n2.1 Wikipedia Base Passages (SYNTHETIC VARIANT GENERATION SOURCE)\\n   - Acquire: 2000 Wikipedia passages >300 words each from Wikipedia API or HuggingFace wiki dataset\\n   - Selection: Random sample ensuring diversity across categories (science, history, culture, sports)\\n   - Preprocessing: Remove infoboxes, references, tables; keep main prose only\\n   - Expected size: 2000 originals × 5 variants = 10,000 synthetic pairs + negatives\\n\\n2.2 Boilerplate Injection Sources (REALISTIC SYNTHETIC EDITS)\\n   For insertion and embedding edits, apply REAL boilerplate rather than random text:\\n   - Wikipedia article talk pages: Download 100-200 example talk page sections (metadata, edit history)\\n   - News headers: Scrape canonical news template headers from Web Archive (e.g., \\\"Published by\\\\n...\\\", \\\"Share this\\\", \\\"Related articles\\\")\\n   - Legal disclaimers: Collect 20-30 standard legal disclaimers from SEC forms, ToS pages\\n   - Product descriptions: Sample 50 product-description templates from review sites\\n   - Executor task: Build a boilerplate corpus (~2-5MB) and apply randomly during edit generation\\n\\n2.3 Edit Type Generators (Controlled synthetic variations)\\n   For each of 2000 Wikipedia passages, generate 5 variants:\\n   \\n   a) INSERTION (prepend boilerplate)\\n      - Select random boilerplate from corpus (200-500 tokens)\\n      - Prepend to passage start\\n      - Mark as edit_type: \\\"insertion\\\"\\n      - Edit distance: ~1500 tokens added at boundary\\n   \\n   b) DELETION (remove middle section)\\n      - Delete 1-3 consecutive paragraphs from middle 50% of passage\\n      - Retain first and last paragraphs for continuity\\n      - Mark as edit_type: \\\"deletion\\\"\\n      - Edit distance: 20-30% of passage removed\\n   \\n   c) EMBEDDING (surround with boilerplate)\\n      - Prepend + append different boilerplate sections\\n      - Total added text: 400-1000 tokens\\n      - Mark as edit_type: \\\"embedding\\\"\\n      - Analogous to article syndication in different contexts\\n   \\n   d) PARAGRAPH-REORDER (shuffle consecutive paragraphs)\\n      - Identify paragraph boundaries (empty line separation)\\n      - Randomly swap 2-3 consecutive paragraphs\\n      - Mark as edit_type: \\\"reorder\\\"\\n      - Key test: preserves local landmark relationships despite positional shifts\\n      - Paragraph count must be ≥4 to enable reordering\\n   \\n   e) CONTROL (no edit)\\n      - Identical to original\\n      - Mark as edit_type: \\\"control\\\"\\n      - Ground truth: is_near_duplicate = true (identical)\\n\\n2.4 Negative Example Generation\\n   For each passage (original or variant), pair with 10-15 unrelated passages as negatives:\\n   - Negatives: Random Wikipedia passages from different categories\\n   - Mark all negatives as is_near_duplicate: false\\n   - Expected: 2000 originals × 15 negatives = 30,000 negative pairs\\n   - Prevents class imbalance; ensures benchmark tests both positive and negative discrimination\\n\\nPHASE 3: INTEGRATION & STANDARDIZATION\\n\\n3.1 Merge Real + Synthetic Data\\n   - Real-world: PAN-PC-11 pairs + CC-News pairs + legal contracts (if included)\\n   - Synthetic: Wikipedia variants (2000 × 5 = 10,000 pairs) + negatives (30,000 pairs)\\n   - Total: 5000-7000 unique source passages, 40,000-50,000 total pairs\\n   - Subset to target: 5000+ originals → 25,000-30,000 pairs for full dataset\\n\\n3.2 JSON Standardization (exp_sel_data_out format)\\n   Each row in data_out.json:\\n   {\\n     \\\"passage_id\\\": \\\"unique-source-id\\\",\\n     \\\"original_text\\\": \\\"full text of source passage\\\",\\n     \\\"variant_id\\\": \\\"unique-variant-id-or-null\\\",\\n     \\\"variant_text\\\": \\\"edited/paired variant text\\\",\\n     \\\"edit_type\\\": \\\"[insertion|deletion|embedding|reorder|control|paraphrase|copy]\\\",\\n     \\\"is_near_duplicate\\\": true/false,\\n     \\\"source_metadata\\\": {\\n       \\\"source\\\": \\\"[pan-pc-11|cc-news|legal|wikipedia-synthetic]\\\",\\n       \\\"domain\\\": \\\"[news|legal|encyclopedia|general]\\\",\\n       \\\"original_length_tokens\\\": 500,\\n       \\\"variant_length_tokens\\\": 700,\\n       \\\"edit_distance_jaccard\\\": 0.75,\\n       \\\"manual_validation\\\": true/false/null\\n     }\\n   }\\n\\n3.3 Splits Generation\\n   - full: 5000+ source passages, 25,000+ pairs (40-100MB)\\n   - mini: 50 source passages, 250 pairs (200KB)\\n   - preview: 5 source passages, 25 pairs (10KB)\\n   - Each split maintains ratio of edit types (insertion 20%, deletion 20%, embedding 20%, reorder 20%, control 10%, negatives 10%)\\n\\n3.4 Schema Validation\\n   - Use aii-json skill to validate all rows against the schema above\\n   - Enforce: passage_id uniqueness, is_near_duplicate ∈ {true, false}, edit_type ∈ allowed values\\n   - Flag any missing required fields\\n   - Generate summary statistics: total pairs, edit-type histogram, source distribution\\n\\nPHASE 4: QUALITY ASSURANCE\\n\\n4.1 Manual Spot-Check (≥50 pairs)\\n   - Sample 50 pairs stratified by:\\n     - Source (PAN-PC-11: 20, CC-News: 15, synthetic: 15)\\n     - Edit type (10 per edit type)\\n   - For each pair:\\n     - Read both texts\\n     - Verify edit_type label is correct\\n     - Assess is_near_duplicate ground truth (does it look like a real near-dup?)\\n     - Flag misclassifications\\n   - Document discrepancy rate; if >5%, reprocess\\n\\n4.2 Length and Coverage Validation\\n   - Verify all passages >300 words (or justify exceptions)\\n   - Confirm edit-type distribution matches plan (all 5 types represented)\\n   - Check for leakage: no passage appears in both training and negative sets\\n   - Report statistics: min/max/mean passage length, pair count per edit type\\n\\nPHASE 5: FAILURE SCENARIOS & MITIGATIONS\\n\\n5.1 If PAN-PC-11 Zenodo download fails\\n   - Fallback: Use PAN plagiarism papers (ResearchGate PDFs) to manually extract example pairs\\n   - Fallback 2: Use MRPC (Microsoft Research Paraphrase Corpus, 5K pairs) as lightweight substitute\\n   - Impact: Reduces real-world diversity; synthetic benchmark becomes primary\\n\\n5.2 If CC-News/Infini-News unavailable or API-rate-limited\\n   - Fallback: Use SemEval-2022 Task 8 multilingual news dataset (Zenodo, 10K pairs, pre-built)\\n   - Impact: Reduces news-domain scale; dataset remains viable\\n\\n5.3 If Wikipedia API quota exhausted\\n   - Fallback: Use HuggingFace \\\"wikipedia\\\" dataset (pre-cached, unlimited)\\n   - Impact: Minimal; Wikipedia data is stable\\n\\n5.4 If boilerplate corpus insufficient\\n   - Fallback: Generate synthetic boilerplate using common templates (\\\"Top Articles\\\", \\\"Latest News\\\", etc.)\\n   - Impact: Reduces realism; still valid for testing insertion/embedding robustness\\n\\n5.5 If paragraph-reorder edit fails (insufficient paragraph count)\\n   - Fallback: Only apply reorder to passages with ≥4 paragraphs; skip others (mark as control instead)\\n   - Impact: May reduce reorder variant count; acceptable trade-off\\n\\nEXECUTOR DELIVERABLES:\\n\\n- data_out.json: Full dataset, 25,000+ pairs, ~40-100MB\\n- data_out_mini.json: Mini split, 250 pairs, ~200KB\\n- data_out_preview.json: Preview split, 25 pairs, ~10KB\\n- schema_validation_report.txt: Line-by-line validation errors (if any)\\n- quality_assurance_report.txt: 50-pair spot-check results, discrepancy rate, recommendations\\n- dataset_statistics.json: Edit-type histogram, source distribution, length statistics, pair counts\\n- README.md: Dataset documentation (sources, edit types, limitations, validation notes)\\n\\nCRITICAL SUCCESS CRITERIA:\\n\\n✓ ≥5000 source passages with ≥25,000 pairs\\n✓ All 5 edit types represented (insertion, deletion, embedding, reorder, control)\\n✓ Real-world data from PAN-PC-11 (mandatory); CC-News (strongly preferred); legal (optional)\\n✓ Manual validation of ≥50 pairs; ≤5% discrepancy in is_near_duplicate labels\\n✓ JSON schema fully validated with aii-json\\n✓ Total size fits within 100MB; splits provided (full, mini, preview)\\n✓ Execution completed within 6h time budget\\n\\nESTIMATED TIME ALLOCATION:\\n- Phase 1 (source acquisition): 1.5h\\n- Phase 2 (synthetic generation): 2h\\n- Phase 3 (integration & standardization): 1h\\n- Phase 4 (QA): 1h\\n- Phase 5 (troubleshooting & documentation): 0.5h\\n- Buffer: 0.5h\\nTOTAL: ~6h\\n\",\n  \"target_num_datasets\": 1\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [40] ASSISTANT · 2026-07-03 18:14:58 UTC

```
Perfect! I've created a comprehensive, actionable plan for the near-duplicate benchmark dataset artifact. 

## Summary

The plan I've delivered is structured across **5 phases**:

**Phase 1: Source Acquisition** — Combines real-world data from:
- **PAN-PC-11 Plagiarism Corpus** (27K documents, 68K+ plagiarism cases, freely available on Zenodo)
- **CC-News Syndication** (via Infini-News processed index or SemEval-2022 Task 8 fallback)
- **Legal Contracts** (Material Contracts Corpus, optional supplemental source)

**Phase 2: Synthetic Benchmark** — Generates controlled structural edits on 2,000 Wikipedia passages:
- **Insertion**: Prepend real boilerplate (200-500 tokens)
- **Deletion**: Remove middle paragraphs (20-30% loss)
- **Embedding**: Surround with boilerplate (400-1K tokens total)
- **Paragraph-Reorder**: Shuffle 2-3 consecutive paragraphs (key test for landmark-pair fingerprinting)
- **Control**: Identical passages (ground truth baseline)
- **Negatives**: 10-15 unrelated passages per source

**Phase 3: Integration** — Standardizes to JSON with schema: `{passage_id, original_text, variant_id, variant_text, edit_type, is_near_duplicate, source_metadata}`

**Phase 4: Quality Assurance** — Manual spot-check of ≥50 pairs, schema validation with aii-json

**Phase 5: Failure Mitigations** — Fallbacks for dataset unavailability, API limits, edge cases

The plan targets **5000+ source passages** with **25,000+ pairs**, splits into full/mini/preview, and fits within the **6-hour execution budget**. Each phase includes specific executor tasks, expected yields, and validation criteria.

Output JSON written to `./.terminal_claude_agent_struct_out.json` ✓

Sources:
- [PAN-PC-11 Plagiarism Corpus](https://zenodo.org/records/3250095)
- [Infini-News: Common Crawl Processing](https://arxiv.org/html/2605.18337)
- [SemEval-2022 Task 8: Multilingual News Similarity](https://zenodo.org/records/6507872)
- [Material Contracts Corpus](https://arxiv.org/html/2504.02864v1)
- [RETSim: Text Similarity Methods](https://arxiv.org/pdf/2311.17264)
- [MinHash LSH Documentation](https://ekzhu.com/datasketch/lsh.html)
```
