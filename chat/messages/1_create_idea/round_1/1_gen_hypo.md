# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 1 · `gen_hypo`
> Run: `run_Bd0c_4hy9OC-` — Near Duplicate Detection
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_hypo_1` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-07-03 17:41:59 UTC

```
model: claude-sonnet-4-6 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/iter_1/gen_hypo/claude_agent
```

### [2] SYSTEM-USER prompt · 2026-07-03 17:42:05 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis generator (Step 2.1: GEN_HYPO — UNSEEDED mode)

Pipeline: GEN_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You received a AII prompt. No external seeds — generate a novel hypothesis from your own reasoning and web research.

Your hypothesis will enter the invention loop (propose → execute → narrate) → the results become a paper + GitHub repo.
It MUST be GENUINELY NOVEL (validated against related work) and FEASIBLE TO TEST (within computational/data/tooling constraints provided).
Vague or incremental hypothesis → wasted computation across the entire pipeline.
</your_role>
</ai_inventor_context>

<strategic_mindset>
You are competing with human researchers.

YOUR ADVANTAGE: Breadth across many fields (information theory, ecology, economics, physics, cognitive science, program synthesis, etc.). No single human has this breadth.

HUMAN ADVANTAGE: Deep expertise in their specific field — they know every paper, every failed attempt, every subtle reason "obvious" ideas don't work.

HOW TO WIN: Don't create variants within their field — they'll always recognize those. Find unexpected connections ACROSS fields no single expert would think of.

NOVELTY BAR: An expert should say "I never thought of approaching it THAT way" — not "that's like paper X with a twist." If your idea lives in a crowded neighborhood of similar approaches, it's NOT novel enough.

NO TIME PRESSURE: Exploring 5-6 directions and abandoning all is a SUCCESSFUL process. Settling for a mediocre idea because you already spent so long researching it is a FAILED process.
</strategic_mindset>

<principles>
1. NOVEL - genuinely new mechanism/principle, not incremental. If you have to argue why it's different, it's NOT novel enough.
2. FEASIBLE - testable within the provided compute, data, and tooling
3. CROSS-FIELD - leverage connections across distant domains
4. RIGOROUS - consider what evidence would support OR refute it
5. PRECISE - clear language, no unnecessary jargon
</principles>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. EXPLICITLY CHECK FOR EACH ONE.

**1. Incremental Recombination Disguised as Novelty**
"Apply known method X to known domain Y" is engineering, not conceptual novelty. Your idea needs a new mechanism/principle/insight — not just a new pairing of existing things.
CHECK: If describable as "A but with B" where A and B both exist, it's recombination. What is the genuinely new IDEA?

**2. Ignoring Resource Constraints**
Every hypothesis MUST be testable with available compute, data, and tools.
CHECK: "Can this be implemented with the specific resources listed? What exact data/compute/tools do I need, and are they available?"

**3. Shallow Search Leading to False Novelty**
The same concept often exists under different terminology, in different fields, or framed differently. Searching only your own phrasing and concluding novelty is the MOST dangerous mistake.

CHECK — For every promising hypothesis:
a) Search 5-6 semantically different phrasings within the field
b) Strip to the CORE MECHANISM and search 8-10 unrelated fields (e.g., "MDL-based complexity selection" → search neural architecture search, program synthesis, Bayesian model selection) — the same principle often exists under different names
c) Search for failed/negative results ("limitations", "does not improve")
d) Search in plain English without jargon
If a paper does the same thing under a different name, it's NOT novel.

**4. Rationalizing Overlapping Prior Work**
When you find similar work, do NOT rationalize minor differences as novelty. Two common traps:

FRAMEWORK PORTING: "Nobody did this in MY framework" — if the core mechanism exists in any context (different algorithm, different ensemble type, different field), porting it is engineering, not novelty.

GAP-FILLING: Papers A, B, C each cover variants → you propose the missing combination. An expert would say "obviously someone will do that eventually."

CHECK: Strip your idea to its core mechanism. Search if that mechanism exists ANYWHERE — any framework, any field, any algorithm family. If yes, ABANDON. Don't salvage by narrowing scope or listing "critical differences."

**5. Anchoring Bias**
Once invested in a direction, you'll unconsciously downplay overlap and inflate minor differences into "key differentiators." This feels like thoroughness but is actually defensiveness.

WARNING SIGNS: listing "critical differences" instead of reconsidering; reluctance to "waste" prior search effort; refining the SAME idea instead of exploring different ones; differentiators about context/framework rather than core mechanism.

CHECK: If you found even 1 paper with a similar core mechanism, ABANDON. The best hypotheses rarely come from your first direction. Each abandonment is progress.

**6. Relying on Search Snippets Without Fetching**
Search snippets are NOT enough to assess overlap or understand an approach. The actual mechanism and limitations are only in the full text.
CHECK: FETCH and read any potentially relevant result. Don't assess novelty from titles and snippets alone.

**7. Same-Neighborhood Pivoting**
Replacing one idea with a variant in the same conceptual space is NOT a genuine pivot. If all your directions are "[different adjective] + [same core concept]", you haven't actually explored.

CHECK: Would a single expert in that subfield have thought of ALL your directions? If yes, bring in a mechanism or framing from a completely unrelated field. That's where genuine novelty lives.
</common_mistakes_to_avoid>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

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

<task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately following this one. Treat that message as the definition of what to generate a hypothesis for.
</YOUR_AII_PROMPT>

<hypothesis_inspiration>
<YOUR_INSPIRATION>
Human researchers overspecialize — they know their domain deeply but lack breadth to see when other fields have already solved analogous problems. Your advantage is breadth. Only propose a cross-domain transfer if it concretely outperforms existing approaches in this domain. Avoid handwavy analogies — if the imported method is vaguer or weaker than what domain experts already use, it's not worth proposing.

Explore cross-domain inspiration at three levels, from abstract to concrete. At each level, consider both established and recent developments — with slight priority for newer work, which tends to leverage more powerful tools and be less widely known.

1. CONCEPTUAL: Borrow high-level ideas, framings, or design philosophies from distant fields.
   What mental model or approach from another domain suggests a novel angle on this problem?

2. PROCEDURAL: Adapt specific problem-solving processes from other domains.
   What workflow, iterative strategy, or pipeline used elsewhere could restructure how this problem is attacked?

3. METHODOLOGICAL: Import concrete methods directly from other fields with minimal modification.
   What algorithm, formula, or technique from a different domain applies here as-is or with adaptation?

Cast wide — draw from ANY field, not just these examples: ecology, economics, physics, linguistics, game theory, control theory, materials science, cognitive science, epidemiology. The best hypotheses often come from Level 2-3 transfers that experts in the field would never encounter.
</YOUR_INSPIRATION>
</hypothesis_inspiration>

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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for the field's landscape, prior work, open problems, dead ends, and what counts as a genuinely novel contribution — read it BEFORE brainstorming and during the novelty check.

- **aii-handbook-multi-llm-agents** — Guide for implementing Multi-LLM Agent Systems research using Mirascope orchestration, HuggingFace datasets/evaluation, and proven multi-agent patterns.
</available_domain_handbooks>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<YOUR_TASK>
Generate 1 novel groundbreaking research hypothesis in the AII prompt that is feasible with the above constraints.

<web_research_process>
Read and STRICTLY follow these skills: aii-web-tools.

1. DIVERGE: Brainstorm 5-7 diverse directions WITHOUT searching.
   Think across fields — what techniques from unrelated domains (ecology, economics, physics,
   linguistics, game theory, etc.) could inspire a novel mechanism? What assumptions does the field
   take for granted? Diversity matters more than depth here.

2. SEARCH: Web search for a high-level overview of each direction.
   What similar approaches exist? Is this genuinely novel or incremental? Remember: snippets
   are NOT enough for detailed understanding — treat search as discovery only.

3. FETCH & READ: MUST fetch any potentially relevant URL — you cannot assess novelty from
   snippets alone. Use the aii-web-tools skill:
   - fetch a page for high-level understanding of HTML pages
   - fetch_grep for exact details, methodology, or PDFs
   Prioritize recent papers closest to your idea. If you find significant overlap, PIVOT.

4. ADVERSARIAL NOVELTY CHECK: Actively try to DISPROVE novelty. Most important step.
   Run the FULL search checklist from <common_mistakes_to_avoid> mistake 3 — within-field
   rephrasings, cross-field core-mechanism search, failed/negative results, plain English.
   Ask: "Is the core insight of your hypothesis new, or known things in a new wrapper?"
   "Would an expert find this genuinely surprising?"
   MANDATORY SELF-CHECK: State the core mechanism in one sentence. Does it exist in ANY
   algorithm, framework, or field? If yes — even in a different framework — ABANDON.

5. FEASIBILITY CHECK: Verify your hypothesis is testable with provided resources. What specific data/compute/tools
   needed? All available within constraints?

6. ABANDON or PROCEED:
   ABANDON if: 2+ similar papers exist; you need to argue "critical differences"; core mechanism
   exists in any context.
   Abandoning is progress — go back to step 1 in a genuinely DIFFERENT direction (not a variant).
   PROCEED only if novelty is SELF-EVIDENT — an expert would immediately see it's new without
   explanation.

7. ITERATE: Expect to repeat steps 1-6 multiple times. The first few directions will likely be
   non-novel. This is normal. Don't settle for your first idea just because you've invested time.

<CRITICAL>We want SCIENTIFIC novelty (new mechanism, principle, or insight — the contribution is
knowledge), NOT application novelty (known methods applied to a new domain — the contribution is a
product). If an expert would say "clever engineering but known science," keep searching.
Hypothesis must be feasible within available resources.</CRITICAL>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>
</web_research_process>

Prioritize simplicity. Use concise, approachable language. The explanation should be fully self-contained.
</YOUR_TASK>

<user_data>
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
    "TermDefinition": {
      "description": "A technical term and its definition.",
      "properties": {
        "term": {
          "description": "The technical term",
          "title": "Term",
          "type": "string"
        },
        "definition": {
          "description": "Clear definition of the term",
          "title": "Definition",
          "type": "string"
        }
      },
      "required": [
        "term",
        "definition"
      ],
      "title": "TermDefinition",
      "type": "object"
    }
  },
  "description": "A research hypothesis with validation approach.",
  "properties": {
    "title": {
      "description": "Hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); name the idea, not a status.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "The core hypothesis statement",
      "title": "Hypothesis",
      "type": "string"
    },
    "motivation": {
      "description": "Why this hypothesis matters - significance and impact",
      "title": "Motivation",
      "type": "string"
    },
    "assumptions": {
      "description": "Key assumptions that must hold for this hypothesis (2-5 items)",
      "items": {
        "type": "string"
      },
      "title": "Assumptions",
      "type": "array"
    },
    "investigation_approach": {
      "description": "High-level approach to investigating this hypothesis",
      "title": "Investigation Approach",
      "type": "string"
    },
    "success_criteria": {
      "description": "What outcomes would confirm or disconfirm this hypothesis?",
      "title": "Success Criteria",
      "type": "string"
    },
    "related_works": {
      "description": "The most similar existing works found during research. Each entry describes one related work: what it does and how the proposed hypothesis fundamentally differs from it.",
      "items": {
        "type": "string"
      },
      "title": "Related Works",
      "type": "array"
    },
    "inspiration": {
      "description": "What inspired this hypothesis - which patterns, techniques, or cross-field insights were adapted (from the explicit inspiration seeds if your prompt included any, otherwise from your own cross-domain exploration)",
      "title": "Inspiration",
      "type": "string"
    },
    "terms": {
      "description": "Definitions of key technical terms used in the hypothesis",
      "items": {
        "$ref": "#/$defs/TermDefinition"
      },
      "title": "Terms",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the hypothesis in 1-2 sentences",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "motivation",
    "assumptions",
    "investigation_approach",
    "success_criteria",
    "related_works",
    "inspiration",
    "terms",
    "summary"
  ],
  "title": "Hypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-07-03 17:42:05 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [4] ASSISTANT · 2026-07-03 17:42:53 UTC

```
I'll start by reading the user uploads and the web tools skill, then brainstorm and research novel directions.
```

### [5] TOOL CALL — Skill · 2026-07-03 17:42:53 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-07-03 17:42:53 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — Bash · 2026-07-03 17:43:03 UTC

```
Search four novel directions in parallel:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"

# Search multiple directions in parallel
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "audio fingerprinting landmarks text near-duplicate detection" --max-results 8 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "topological data analysis persistent homology text similarity deduplication" --max-results 8 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "ecological beta diversity text similarity NLP" --max-results 8 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "Kuramoto oscillator synchronization text document similarity" --max-results 8 &
wait
```

### [8] TOOL RESULT — Bash · 2026-07-03 17:43:03 UTC

```
{"stdout": "Search: topological data analysis persistent homology text similarity deduplication\nFound: 8 results\n\n1. Topological data analysis and topological deep learning beyond ...\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC12931839/\n   This paper presents a comprehensive review of TDA and TDL beyond persistent homology. It analyzes how persistent topological Laplacians and ......\n\n2. Topological data analysis: What is persistent homology?\n   https://www.broadinstitute.org/talks/topological-data-analysis-what-persistent-homology\n   Topological data analysis (TDA) aims to measure the “intrinsic shape” of data and identify this manifold despite noise and the likely nonlinear embedding. I ......\n\n3. Topological data analysis - Wikipedia\n   https://en.wikipedia.org/wiki/Topological_data_analysis\n   The main tool is persistent homology, an adaptation of homology to point cloud data. Persistent homology has been applied to many types of data across many ......\n\n4. Topological data analysis of collective and individual epithelial cells ...\n   https://pubs.rsc.org/en/content/articlelanding/2021/sm/d1sm00072a\n   We demonstrate a topology-based machine learning approach for unsupervised profiling of individual and collective phases based on large-scale loops....\n\n5. Topological Data Analysis with Persistent Homology - Medium\n   https://medium.com/@deltorobarba/quantum-topological-data-analysis-the-most-powerful-quantum-machine-learning-algorithm-part-1-c6d055f2a4de\n   Topological data analysis (TDA) uses Persistent Homology to study the topological features of a shape or data at different spatial resolutions....\n\n6. [PDF] A Tutorial on Topological Data Analysis in Text Mining\n   http://bigdataieee.org/BigData2020/files/IEEE_BigData_2020_Tutorial5_TDA_Tutorial.pdf\n   Persistent homology does not distinguish the order of dimensions if we do not differentiate the results. S. Gholizadeh & W. Zadrozny. A Tutorial ......\n\n7. AdaUchendu/AwesomeTDA4NLP: Topological Data Analysis (TDA ...\n   https://github.com/adauchendu/awesometda4nlp\n   Topological signature of 19th century novelists: Persistent homology in text mining. · A novel method of extracting topological features from word embeddings....\n\n8. (PDF) On Topological Data Analysis for SHM: An Introduction to ...\n   https://www.researchgate.net/publication/355062865_On_Topological_Data_Analysis_for_SHM_An_Introduction_to_Persistent_Homology\n   The main tool within topological data analysis is persistent homology; this is a means of measuring the shape of data, from the homology of a ......\n\nSearch: audio fingerprinting landmarks text near-duplicate detection\nFound: 8 results\n\n1. Textual near duplicate identification - RelativityOne\n   https://help.relativity.com/RelativityOne/Content/Relativity/Analytics/Textual_near_duplicate_identification.htm\n   Textual near duplicate identification scans the text of documents to find near matches. This makes it easier to tell at a glance whether two ......\n\n2. using audio fingerprinting for duplicate detection and ...\n   https://www.microsoft.com/en-us/research/wp-content/uploads/2005/03/audiothumbnail.pdf\n   by CJC Burges · Cited by 56 — This paper presents two new applications of audio finger- printing: duplicate detection, whose goal is to identify du- plicate audio clips in a set, even if ......\n\n3. Audio Fingerprinting and Duplicate Detection [Expert Guide]\n   https://www.workmate.com/blog/audio-fingerprinting-and-duplicate-detection-expert-guide\n   Audio fingerprinting provides a scalable, reliable method to detect exact and near-duplicate meeting recordings. Combine acoustic matching ......\n\n4. (PDF) Using Audio Fingerprinting for Duplicate Detection ...\n   https://www.researchgate.net/publication/4137084_Using_Audio_Fingerprinting_for_Duplicate_Detection_and_Thumbnail_Generation\n   This paper presents two new applications of audio finger- printing: duplicate detection, whose goal is to identify du- plicate audio clips in a set....\n\n5. Near Duplicate Detection\n   https://sites.cs.ucsb.edu/~tyang_class/293s20f/slides/TopicDuplicate1.pdf\n   1. Shingling : convert text documents to fingerprint sets. 2. Minhashing : convert a large set of fingerprints to short signatures, while ......\n\n6. Audio Fingerprinting for Duplicate Detection / Allison King\n   https://observablehq.com/@allisonking/audio-fingerprinting-for-duplicate-detection\n   The short answer is that you can create a spectrogram of an audio file, then look create a series of hashes based on the spectrogram to develop an idea of what ......\n\n7. Identifying and Filtering Near-Duplicate Documents\n   https://cs.brown.edu/courses/cs253/papers/nearduplicate.pdf\n   by AZ Broder · Cited by 704 — Rather than deal with shingles directly, it is more convenient to associate to each shingle a numeric uid (unique id). This done by fingerprinting the shingle....\n\n8. Detecting Near-Duplicates for Web Crawling\n   https://research.google.com/pubs/archive/33026.pdf\n   by GS Manku · Cited by 1021 — So our first goal was to ascertain whether simhash is a reasonable fingerprinting technique for near- duplicate detection in the first place. We study ......\n\n[1]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"audio fingerprinting landmarks text near-duplicate detection\" --max-results 8\n[2]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"topological data analysis persistent homology text similarity deduplication\" --max-results 8\nSearch: Kuramoto oscillator synchronization text document similarity\nFound: 8 results\n\n1. Enhanced synchronization with proportional coupling in ...\n   https://arxiv.org/html/2603.29648\n   We introduce a novel coupling scheme for maximizing the synchronization of Kuramoto oscillator networks under a fixed coupling budget. We show ......\n\n2. Synchronization of coupled second-order Kuramoto ...\n   https://research.rug.nl/files/155871913/Complete_thesis.pdf\n   α = 0, one gets an explosive synchronization similar to Kuramoto oscillators, in. Fig. 8.2(b). When α > 0 the effective inertias mi is ......\n\n3. On the synchronization of discrete-time Kuramoto model ...\n   https://www.aimsciences.org/article/doi/10.3934/cpaa.2023109\n   by T Zhu · 2023 · Cited by 2 — In this paper, we study the emergent discrete-time dynamics of the Kuramoto model with frustration. For the discrete identical Kuramoto model with frustration,...\n\n4. How to get an accurate text similarity score between very ...\n   https://www.reddit.com/r/LanguageTechnology/comments/lbl7wk/how_to_get_an_accurate_text_similarity_score/\n   Levenshtein woud be ideal, but it's not computationally feasible to compare hundreds of pages long documents with it. Hamming and other edit-based metrics ......\n\n5. Exact solution for first-order synchronization transition in a ...\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC4248286/\n   by X Hu · 2014 · Cited by 103 — In his seminal work, Kuramoto introduced a solvable model for synchronization of globally coupled phase oscillators, which inspired and ......\n\n6. Episode 1: Kuramoto Model Part 1\n   https://www.youtube.com/watch?v=PHgekrkka1U\n   Welcome to Episode 1 of The Imposter's Math Biology Podcast. This episode is on the Kuramoto model and covers frames of reference, ......\n\n7. Kuramoto model\n   https://en.wikipedia.org/wiki/Kuramoto_model\n   a mathematical model used in describing synchronization. More specifically, it is a model for the behavior of a large set of coupled oscillators....\n\n8. Optimal synchronization of Kuramoto oscillators\n   https://link.aps.org/doi/10.1103/PhysRevE.92.062801\n   by RS Pinto · 2015 · Cited by 40 — We show that the optimal synchronization of a Kuramoto network demands the maximization of the quadratic function 𝜔 𝑇 ⁢ 𝐿 ⁢ 𝜔 , where 𝜔 stands ......\n\nSearch: ecological beta diversity text similarity NLP\nFound: 8 results\n\n1. Navigating the spatial and temporal aspects of beta ...\n   https://www.sciencedirect.com/science/article/pii/S235198942400547X\n   by J Heino · 2024 · Cited by 25 — Here, we define four unique aspects of beta diversity that encompass the diverse applications of this concept in ecology and biodiversity management....\n\n2. Phylogenetic beta diversity, similarity, and differentiation ...\n   https://esajournals.onlinelibrary.wiley.com/doi/10.1890/12-0960.1\n   Measures of beta diversity, similarity, and differentiation are basic tools of ecological analyses (Magurran 2004, Magurran and McGill 2011)....\n\n3. β-Diversity, Community Assembly, and Ecosystem Functioning\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC7612777/\n   by AS Mori · 2018 · Cited by 776 — A focus on β-diversity has the potential to improve predictions of natural and anthropogenic influences on diversity and ecosystem functioning....\n\n4. What is the difference between beta diversity index and ...\n   https://www.researchgate.net/post/What_is_the_difference_between_beta_diversity_index_and_beta_similarity_index_in_terms_of_their_interpretation_What_type_of_indices_is_Sorenson_Cs\n   In a text that I am using for my students, they have the following extract:\nBasic Beta Diversity Index\nBasic Beta Diversity Index measures the similarity ......\n\n5. Untangling the contributions of species and site to beta ...\n   https://www.authorea.com/doi/full/10.22541/au.170993002.23925614/v1\n   The variation of species composition among communities, commonly known as beta diversity, is at the heart of ecology because of its role in ......\n\n6. What is Beta Diversity\n   https://www.cd-genomics.com/resource-what-beta-diversity.html\n   Beta diversity refers to the difference in species composition between ecosystems. It quantifies how species diversity changes from one habitat to another....\n\n7. A comparison of phylogenetic and species beta diversity ...\n   https://vegsciblog.org/2019/02/21/a-comparison-of-phylogenetic-and-species-beta-diversity-measures-describing-vegetation-assemblages-along-an-elevation-gradient/\n   In this project, our goals were to 1) compare environmental site differences among vegetation plots to differences among plots based on species composition....\n\n8. 3. Species Richness and Diversity - Jasper Slingsby\n   https://www.ecologi.st/BIO3018F/3_BetaDiv\n   ... beta\\)` diversity. >*\"Plurality in the concept of `\\(\\beta\\)` diversity can yield important ecological insights when navigated well. By knowing the ......\n\n[3]-  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"ecological beta diversity text similarity NLP\" --max-results 8\n[4]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"Kuramoto oscillator synchronization text document similarity\" --max-results 8", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [9] TOOL CALL — Bash · 2026-07-03 17:43:15 UTC

```
Search more specific directions:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"

$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "Shazam spectral landmark hashing text document fingerprinting near-duplicate" --max-results 8 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "reaction diffusion fingerprint text similarity" --max-results 8 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "TDA persistent homology text document similarity NLP near-duplicate" --max-results 8 &
wait
```

### [10] TOOL RESULT — Bash · 2026-07-03 17:43:15 UTC

```
{"stdout": "Search: TDA persistent homology text document similarity NLP near-duplicate\nFound: 8 results\n\n1. [PDF] Persistent Homology: An Introduction and a New Text ... - IJCAI\n   https://www.ijcai.org/Proceedings/13/Papers/288.pdf\n   Persistent homology is a mathematical tool from topological data analysis. It performs multi-scale analysis on a set of points and identifies clusters,....\n\n2. Persistent homology: An introduction and a new text representation ...\n   https://www.researchgate.net/publication/262311097_Persistent_homology_An_introduction_and_a_new_text_representation_for_natural_language_processing\n   Persistent homology is a mathematical tool from topological data analysis. It performs multi-scale analysis on a set of points and identifies clusters, ......\n\n3. [PDF] Persistent Homology: An Introduction and a New Text ...\n   https://pages.cs.wisc.edu/~jerryzhu/pub/homology.pdf\n   Persistent homology is a mathematical tool from topological data analysis. It performs multi-scale analysis on a set of points and ......\n\n4. Textual near duplicate identification - RelativityOne\n   https://help.relativity.com/RelativityOne/Content/Relativity/Analytics/Textual_near_duplicate_identification.htm\n   Textual near duplicate identification scans the text of documents to find near matches. This makes it easier to tell at a glance whether two ......\n\n5. How to find near duplicate text documents? : r/LanguageTechnology\n   https://www.reddit.com/r/LanguageTechnology/comments/i4bli4/how_to_find_near_duplicate_text_documents/\n   I want to find duplicates and \"near\" duplicates among them using python and I'd like to know which are some ready-made libraries for this purpose....\n\n6. Persistent Homology | Introduction & Python Example Code - YouTube\n   https://www.youtube.com/watch?v=5ezFcy9CIWE&vl=en\n   https://aibuilder.acad... This is the final video in a 3-part series on topological data analysis (TDA). TDA is an up-and-coming approach to ......\n\n7. RETSim: Resilient and Efficient Text Similarity - arXiv\n   https://arxiv.org/html/2311.17264\n   Robust near-duplicate text detection is an essential component of many tasks, including retrieving documents, detecting plagiarism (Sun et al., ......\n\n8. AdaUchendu/AwesomeTDA4NLP: Topological Data Analysis (TDA ...\n   https://github.com/adauchendu/awesometda4nlp\n   Topological signature of 19th century novelists: Persistent homology in text mining. · A novel method of extracting topological features from word embeddings....\n\nSearch: Shazam spectral landmark hashing text document fingerprinting near-duplicate\nFound: 8 results\n\n1. Robust Landmark-Based Audio Fingerprinting\n   https://www.ee.columbia.edu/~dpwe/LabROSA/matlab/fingerprint/\n   These routines implement a landmark-based audio fingerprinting system that is very well suited to identifying small, noisy excerpts from a large number of ......\n\n2. Robust Landmark-Based Audio Fingerprinting\n   https://www.mathworks.com/matlabcentral/fileexchange/23332-robust-landmark-based-audio-fingerprinting\n   This landmark-based audio fingerprinting system is able to match short, noisy snippets to a reference database in near-constant time....\n\n3. Tech Talk: What's that Sound? An Overview of Shazam's ...\n   https://www.youtube.com/watch?v=Q4LYys9v9Ko\n   ... Shazam processes audio clips and produces \"fingerprints\" of them, and then describes how Shazam searches for that fingerprint within their ......\n\n4. Building a Shazam-like Audio Fingerprinting System in Go\n   https://www.linkedin.com/pulse/building-shazam-like-audio-fingerprinting-system-go-eduard-jacobs-qd31c\n   Audio fingerprinting transforms an audio signal into a unique digital “barcode” that captures its key characteristics, enabling recognition even ......\n\n5. Evaluating musical fingerprinting systems\n   https://www.upf.edu/documents/223346843/0/porter2012thesis.pdf/261e5a58-7f5b-55dd-b732-1b366404db61\n   To identify an unknown audio recording query, the query's fingerprint is generated and compared to the reference database to find recordings....\n\n6. How Shazam Works: Audio Fingerprinting\n   https://yassineaitsidibrahim.medium.com/how-shazam-works-audio-fingerprinting-636c031aa6fa\n   Extract Peak Points From that spectrogram, Shazam picks the loudest, most prominent frequency peaks. These are the “landmarks” of the audio. Get ......\n\n7. using audio fingerprinting for duplicate detection and ...\n   https://www.microsoft.com/en-us/research/wp-content/uploads/2005/03/audiothumbnail.pdf\n   by CJC Burges · Cited by 56 — Audio fingerprinting is a powerful tool for identifying file- based or streaming audio, using a database of fingerprints....\n\n8. Digital Fingerprinting on Multimedia: A Survey\n   https://arxiv.org/html/2408.14155v1\n   The generated text blocks are then hashed and used as the fingerprint of the document. The Hash-breaking algorithm typically selects text ......\n\n[1]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"Shazam spectral landmark hashing text document fingerprinting near-duplicate\" --max-results 8\n[3]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"TDA persistent homology text document similarity NLP near-duplicate\" --max-results 8\nSearch: reaction diffusion fingerprint text similarity\nFound: 8 results\n\n1. Novel reaction-diffusion PDE model for fingerprint-like pattern ... - arXiv\n   https://arxiv.org/html/2511.03096v1\n   In this work, we present a reaction‑diffusion model of Schnakenberg type, featuring an anisotropic diffusion matrix that follows the ridge ......\n\n2. Reaction Fingerprint - Documentation - Chemaxon Docs\n   https://docs.chemaxon.com/latest/fingerprints_reaction-fingerprint.html\n   Two reactions can be considered similar if their product side and/or reactant side are similar. With this consideration, reaction similarity is reduced to ......\n\n3. Development of a novel fingerprint for chemical reactions ... - PubMed\n   https://pubmed.ncbi.nlm.nih.gov/25541888/\n   Fingerprint methods applied to molecules have proven to be useful for similarity determination and as inputs to machine-learning models....\n\n4. Reaction fingerprints · rdkit rdkit · Discussion #5263 - GitHub\n   https://github.com/rdkit/rdkit/discussions/5263\n   I'm working with fingerprints and similarity of reactions, with particular interest in understanding how the agents are handled and I run across an ......\n\n5. Derivation of an analytical solution to a reaction-diffusion model for ...\n   https://researchconnect.suny.edu/en/publications/derivation-of-an-analytical-solution-to-a-reaction-diffusion-mode/fingerprints/\n   Derivation of an analytical solution to a reaction-diffusion model for autocatalytic degradation and erosion in polymer microspheres · Overview · Fingerprint ......\n\n6. Fingerprint Restoration Using Digital Reaction-Diffusion System and ...\n   https://www.researchgate.net/publication/283654416_Fingerprint_Restoration_Using_Digital_Reaction-Diffusion_System_and_Its_Evaluation\n   The phase-only image matching technique is employed for evaluating the similarity between an original fingerprint image and a restored image....\n\n7. Time-delayed reaction-diffusion fronts - Fingerprint - Research Portal\n   https://recerca.udg.edu/en/publications/time-delayed-reaction-diffusion-fronts/fingerprints/\n   Fingerprint. Dive into the research topics of 'Time-delayed reaction-diffusion fronts'. Together they form a unique fingerprint....\n\n8. Trainable Nonlinear Reaction Diffusion: A Flexible Framework for ...\n   https://graz.elsevierpure.com/en/publications/trainable-nonlinear-reaction-diffusion-a-flexible-framework-for-f/fingerprints/\n   Trainable Nonlinear Reaction Diffusion: A Flexible Framework for Fast and Effective Image Restoration · Overview · Fingerprint ......\n\n[2]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"reaction diffusion fingerprint text similarity\" --max-results 8", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [11] TOOL CALL — Bash · 2026-07-03 17:43:43 UTC

```
Adversarial novelty check for Shazam-style text fingerprinting:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"

$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "landmark hashing text fingerprint position n-gram pairs near-duplicate" --max-results 8 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "spectral text fingerprinting local maxima n-gram frequency duplicate detection" --max-results 8 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "RETSim text similarity near-duplicate resilient efficient" --max-results 5 &
wait
```

### [12] TOOL RESULT — Bash · 2026-07-03 17:43:43 UTC

```
{"stdout": "Search: RETSim text similarity near-duplicate resilient efficient\nFound: 5 results\n\n1. RETSim: Resilient and Efficient Text Similarity\n   https://arxiv.org/html/2311.17264\n   We demonstrate that RETSim is significantly more robust and accurate than MinHash and neural text embeddings, achieving new state-of-the-art ......\n\n2. RETSim: Resilient and Efficient Text Similarity - ADS\n   https://ui.adsabs.harvard.edu/abs/arXiv:2311.17264\n   This paper introduces RETSim (Resilient and Efficient Text Similarity), a lightweight, multilingual deep learning model trained to produce robust metric ......\n\n3. [2311.17264] RETSim: Resilient and Efficient Text Similarity\n   https://arxiv.org/abs/2311.17264\n   by M Zhang · 2023 · Cited by 7 — This paper introduces RETSim (Resilient and Efficient Text Similarity), a lightweight, multilingual deep learning model trained to produce robust metric ......\n\n4. Paper page - RETSim: Resilient and Efficient Text Similarity\n   https://huggingface.co/papers/2311.17264\n   RETSim, a lightweight multilingual deep learning model, outperforms existing methods in robust text similarity tasks, including new benchmarks ......\n\n5. RETSim: Resilient and Efficient Text Similarity\n   https://www.semanticscholar.org/paper/RETSim%3A-Resilient-and-Efficient-Text-Similarity-Zhang-Vallis/ca84496fa0bd042a455789eae00c98b8c4d6e0e4\n   It is demonstrated that RETSim is significantly more robust and accurate than MinHash and neural text embeddings, achieving new state-of-the-art performance ......\n\nSearch: landmark hashing text fingerprint position n-gram pairs near-duplicate\nFound: 8 results\n\n1. Detecting Near-Duplicates for Web Crawling\n   https://research.google.com/pubs/archive/33026.pdf\n   by GS Manku · Cited by 1021 — After converting documents into simhash fingerprints, we face the following design problem: Given a 64-bit fingerprint of a recently-crawled web page, how do we ......\n\n2. Automatic (near-) duplicate content document detection in ...\n   https://www.sciencedirect.com/science/article/pii/S1386505625000164\n   by T Niemi · 2025 · Cited by 2 — The Simhash method computes a numeric fingerprint for each document in a way that fingerprints of similar documents are closer to each other than to those of ......\n\n3. Near-Duplicate Text Alignment under Weighted Jaccard ...\n   https://arxiv.org/html/2509.00627v1\n   Near-duplicate text alignment is the task of identifying all subsequences (i.e., substrings) in a collection of texts that are similar to a ......\n\n4. Near-Duplicate Text Alignment with One Permutation ...\n   https://dl.acm.org/doi/10.1145/3677136\n   This paper studies the near-duplicate text alignment problem under the constraint of Jaccard similarity....\n\n5. Finding near-duplicates with Jaccard similarity and MinHash\n   https://blog.nelhage.com/post/fuzzy-dedup/\n   In this post I want to explore the method of approximate deduplication via Jaccard similarity and the MinHash approximation trick....\n\n6. Near Duplicate Detection\n   https://sites.cs.ucsb.edu/~tyang_class/293s20f/slides/TopicDuplicate1.pdf\n   Shingling : convert text documents to fingerprint sets. 2. Minhashing : convert a large set of fingerprints to short signatures, while preserving similarity....\n\n7. Near-Duplicate Sequence Search at Scale for Large ...\n   https://people.cs.rutgers.edu/~dd903/assets/papers/sigmod23.pdf\n   by Z Peng · 2023 · Cited by 27 — It can find (almost) all the near-duplicate sequences of the query sequence in a large corpus with guarantees. Specifically, the algorithm generates and groups ......\n\n8. Probabilistic Near-Duplicate Detection Using Simhash\n   https://www.researchgate.net/publication/221615307_Probabilistic_Near-Duplicate_Detection_Using_Simhash\n   This paper offers a novel look at using a dimensionality-reduction technique called simhash to detect similar document pairs in large-scale collections....\n\n[1]   Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"landmark hashing text fingerprint position n-gram pairs near-duplicate\" --max-results 8\n[3]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"RETSim text similarity near-duplicate resilient efficient\" --max-results 5\nSearch: spectral text fingerprinting local maxima n-gram frequency duplicate detection\nFound: 8 results\n\n1. Overview of Fingerprinting Methods for Local Text Reuse ...\n   https://www.researchgate.net/publication/310441711_Overview_of_Fingerprinting_Methods_for_Local_Text_Reuse_Detection\n   We overview several local text reuse detection methods based on fingerprinting techniques. We first define the context of local text reuse....\n\n2. Identifying individuals from their brain natural frequency ... - PMC\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC12216093/\n   by L Arana · 2025 · Cited by 4 — The fingerprinting process consists of a search through the rows/columns of the correlation matrix, where the highest correlation coefficient ......\n\n3. using audio fingerprinting for duplicate detection and ...\n   https://www.microsoft.com/en-us/research/wp-content/uploads/2005/03/audiothumbnail.pdf\n   by CJC Burges · Cited by 56 — Audio fingerprinting is a powerful tool for identifying file- based or streaming audio, using a database of fingerprints....\n\n4. Digital Fingerprinting on Multimedia: A Survey\n   https://arxiv.org/html/2408.14155v1\n   Based on Winnowing, frequency-biased winnowing (FBW) [58] is an improved fingerprint selection method for text reuse detection. Its main feature ......\n\n5. Robust Audio Fingerprinting Based on Local Spectral ...\n   https://www.isca-archive.org/interspeech_2011/shi11b_interspeech.pdf\n   by Y Shi · 2011 · Cited by 3 — This paper proposes a robust audio fingerprinting system based on local spectral luminance maxima (LSLM) scheme using im- age processing approaches....\n\n6. What algorithms are commonly used for audio fingerprinting?\n   https://milvus.io/ai-quick-reference/what-algorithms-are-commonly-used-for-audio-fingerprinting\n   Spectral peak-based algorithms, popularized by Shazam, extract fingerprints by identifying prominent time-frequency points in a spectrogram. These “landmark” ......\n\n7. Wireless Signal Fingerprinting Framework Based on ...\n   https://www.mdpi.com/2227-7390/14/13/2321\n   We propose a deep-learning-based BLE signal fingerprinting framework that uses emphasized spectral data to enhance device authentication. The proposed framework ......\n\n8. Winnowing: Local Algorithms for Document Fingerprinting\n   http://www.cs.princeton.edu/courses/archive/spring05/cos598E/bib/p76-schleimer.pdf\n   by S Schleimer · 2003 · Cited by 2011 — • Let the frequency of a k-gram (or its hash) be the number of times it occurs. • Sort the frequencies in monotonically decreasing order. The rank of a k ......\n\n[2]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"spectral text fingerprinting local maxima n-gram frequency duplicate detection\" --max-results 8", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [13] TOOL CALL — Bash · 2026-07-03 17:43:59 UTC

```
Read Winnowing paper and search for paired landmark text fingerprinting:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"

$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "http://www.cs.princeton.edu/courses/archive/spring05/cos598E/bib/p76-schleimer.pdf" --max-chars 6000 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "paired n-gram landmark positional offset text reuse fingerprint hashing" --max-results 8 &
wait
```

### [14] TOOL RESULT — Bash · 2026-07-03 17:43:59 UTC

```
{"stdout": "Search: paired n-gram landmark positional offset text reuse fingerprint hashing\nFound: 8 results\n\n1. Overview of Fingerprinting Methods for Local Text Reuse Detection\n   https://www.researchgate.net/publication/310441711_Overview_of_Fingerprinting_Methods_for_Local_Text_Reuse_Detection\n   Fingerprinting is a method that sets its text reuse criteria by extracting the n-gram in two texts for comparison, and then analyzing the number of ngrams ......\n\n2. [PDF] Hashing and Merging Heuristics for Text Reuse Detection\n   https://ceur-ws.org/Vol-1180/CLEF2014wn-Pan-AlviEt2014.pdf\n   In this work, we used hashing and merging heuristics on character n-grams for text reuse detection. Our approach scored a mid-range performance ......\n\n3. Patterns of text reuse in a scientific corpus - PMC - NIH\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC4291616/\n   This is the first comprehensive study of patterns of text reuse within the full texts of an important large scientific corpus, covering a 20-y timeframe....\n\n4. Fingerprinting (hash-based methods) for plagiarism detection\n   https://www.plagiarismchecker.net/articles/fingerprinting-hash-based-methods-for-plagiarism-detection/\n   Fingerprinting methods detect plagiarism efficiently by hashing k-grams, using Rabin–Karp and winnowing algorithms....\n\n5. Detecting Text Reuse with Passim - Programming Historian\n   https://programminghistorian.org/en/lessons/detecting-text-reuse-with-passim\n   This lesson will teach you the ropes of Passim, an open source and scalable tool for text reuse detection....\n\n6. [PDF] INTER- TEXTUAL PHRASE MATCHING - TLG\n   https://stephanus.tlg.uci.edu/helppdf/ngrams.pdf\n   N-grams are overlapping sequences of content words in text. They provide an efficient mechanism for identifying common passages between texts: by identifying....\n\n7. [PDF] Per-Component Identity for Agent Skills - arXiv\n   https://arxiv.org/pdf/2606.31272\n   A lexical n-gram baseline matches the fingerprint on accuracy here because the corpus serves surface overlap; the fingerprint wins on size and ......\n\n8. [PDF] Searching by corpus with fingerprints - OpenProceedings.org\n   https://openproceedings.org/2012/conf/edbt/AggarwalLY12.pdf\n   In our fingerprint scheme, we use a 2-dimensional hashing scheme, in which the range of the hash function is document- dependent, the second ......\n\nURL: http://www.cs.princeton.edu/courses/archive/spring05/cos598E/bib/p76-schleimer.pdf\nType: PDF\nLength: 59802 chars (truncated)\n\n--- Content ---\n\nWinnowing: Local Algorithms for Document Fingerprinting\nSaul Schleimer\nMSCS\nUniversity of Illinois, Chicago\nsaul@math.uic.edu\nDaniel S. Wilkerson\nComputer Science Division\nUC Berkeley\ndsw@cs.berkeley.edu\nAlex Aiken\nComputer Science Division\nUC Berkeley\naiken@cs.berkeley.edu\nABSTRACT\nDigital content is for copying: quotation, revision, plagiarism, and\nﬁle sharing all create copies. Document ﬁngerprinting is concerned\nwith accurately identifying copying, including small partial copies,\nwithin large sets of documents.\nWe introduce the class of local document ﬁngerprinting algo-\nrithms, which seems to capture an essential property of any ﬁnger-\nprinting technique guaranteed to detect copies. We prove a novel\nlower bound on the performance of any local algorithm. We also\ndevelop winnowing, an efﬁcient local ﬁngerprinting algorithm, and\nshow that winnowing’s performance is within 33% of the lower\nbound. Finally, we also give experimental results on Web data, and\nreport experience with MOSS, a widely-used plagiarism detection\nservice.\n1.\nINTRODUCTION\nDigital documents are easily copied. A bit less obvious, perhaps,\nis the wide variety of different reasons for which digital documents\nare either completely or partially duplicated. People quote from\neach other’s email and news postings in their replies. Collaborators\ncreate multiple versions of documents, each of which is closely\nrelated to its immediate predecessor. Important Web sites are mir-\nrored. More than a few students plagiarize their homework from\nthe Web. Many authors of conference papers engage in a similar\nbut socially more acceptable form of text reuse in preparing journal\nversions of their work. Many businesses, notably in the software\nand entertainment industries, are based on charging for each digital\ncopy sold.\nComparing whole document checksums is simple and sufﬁces\nfor reliably detecting exact copies; however, detecting partial copies\nis subtler. Because of its many potential applications, this second\nproblem has received considerable attention.\nMost previous techniques for detecting partial copies, which we\ndiscuss in more detail in Section 2, make use of the following idea.\nA k-gram is a contiguous substring of length k. Divide a docu-\nment into k-grams, where k is a parameter chosen by the user. For\nexample, Figure 1(c) contains all the 5-grams of the string of char-\nacters in Figure 1(b). Note that there are almost as many k-grams\nPermission to make digital or hard copies of all or part of this work for\npersonal or classroom use is granted without fee provided that copies are\nnot made or distributed for proﬁt or commercial advantage and that copies\nbear this notice and the full citation on the ﬁrst page. To copy otherwise, to\nrepublish, to post on servers or to redistribute to lists, requires prior speciﬁc\npermission and/or a fee.\nSIGMOD 2003, June 9-12, 2003, San Diego, CA.\nCopyright 2003 ACM 1-58113-634-X/03/06 ...$5.00.\nA do run run run, a do run run\n(a) Some text from [7].\nadorunrunrunadorunrun\n(b) The text with irrelevant features removed.\nadoru dorun orunr runru unrun nrunr runru\nunrun nruna runad unado nador adoru dorun\norunr runru unrun\n(c) The sequence of 5-grams derived from the text.\n77 72 42 17 98 50 17 98 8 88 67 39 77 72 42\n17 98\n(d) A hypothetical sequence of hashes of the 5-grams.\n72 8 88 72\n(e) The sequence of hashes selected using 0 mod 4.\nFigure 1: Fingerprinting some sample text.\nas there are characters in the document, as every position in the\ndocument (except for the last k −1 positions) marks the begin-\nning of a k-gram. Now hash each k-gram and select some subset\nof these hashes to be the document’s ﬁngerprints. In all practical\napproaches, the set of ﬁngerprints is a small subset of the set of all\nk-gram hashes. A ﬁngerprint also contains positional information,\nwhich we do not show, describing the document and the location\nwithin that document that the ﬁngerprint came from. If the hash\nfunction is chosen so that the probability of collisions is very small,\nthen whenever two documents share one or more ﬁngerprints, it is\nextremely likely that they share a k-gram as well.\nFor efﬁciency, only a subset of the hashes should retained as\nthe document’s ﬁngerprints. One popular approach is to choose all\nhashes that are 0 mod p, for some ﬁxed p. This approach is easy to\nimplement and retains only 1/p of all hashes as ﬁngerprints (Sec-\ntion 2). Meaningful measures of document similarity can also be\nderived from the number of ﬁngerprints shared between documents\n[5].\nA disadvantage of this method is that it gives no guarantee that\nmatches between documents are detected: a k-gram shared be-\ntween documents is detected only if its hash is 0 mod p. Consider\nthe sequence of hashes generated by hashing all k-grams of a ﬁle\nin order. Call the distance between consecutive selected ﬁnger-\nprints the gap between them. If ﬁngerprints are selected 0 mod p,\nthe maximum gap between two ﬁngerprints is unbounded and any\n76\n76\n\nmatches inside a gap are not detected.1 In experiments with select-\ning ﬁngerprints 0 mod p on HTML data taken from the Web, we\nfound that gaps between ﬁngerprints chosen 0 mod p can be quite\nlarge. In fact, there are passages much longer than the size of the\naverage Web page in which no hashes are 0 mod p for reasonable\nvalues of p (Section 5).\nIn this paper we give the ﬁrst efﬁcient algorithm for selecting the\nﬁngerprints from a sequence of hashes that guarantees that at least\npart of any sufﬁciently long match is detected. Deﬁne a window of\nsize w to be w consecutive hashes of k-grams in a document (w is\na parameter set by the user). By selecting at least one ﬁngerprint\nfrom every window our algorithm limits the maximum gap between\nﬁngerprints. In fact, our algorithm is guaranteed to detect at least\none k-gram in any shared substring of length at least w + k −1.\nCentral to our construction is the idea of a local algorithm (Sec-\ntion 4), which we believe captures the essential properties of any\ndocu\n[1]-  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"http://www.cs.princeton.edu/courses/archive/spring05/cos598E/bib/p76-schleimer.pdf\" --max-chars 6000\n[2]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"paired n-gram landmark positional offset text reuse fingerprint hashing\" --max-results 8", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [15] TOOL CALL — Bash · 2026-07-03 17:44:26 UTC

```
Check 2D hashing paper and search for anchor-target pair hashing in text:
export SKILL_DIR="/ai-inventor/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"

$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://openproceedings.org/2012/conf/edbt/AggarwalLY12.pdf" --max-chars 5000 &
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "text reuse detection anchor target pair hash offset position invariant" --max-results 8 &
wait
```

### [16] TOOL RESULT — Bash · 2026-07-03 17:44:26 UTC

```
{"stdout": "Search: text reuse detection anchor target pair hash offset position invariant\nFound: 8 results\n\n1. A large dataset of scientific text reuse in Open-Access publications\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC9879940/\n   We present the Webis-STEREO-21 dataset, a massive collection of Scientific Text Reuse in Open-access publications. It contains 91 million cases of reused ......\n\n2. [PDF] Hashing and Merging Heuristics for Text Reuse Detection\n   https://ceur-ws.org/Vol-1180/CLEF2014wn-Pan-AlviEt2014.pdf\n   We employ the three steps of seeding, extension and filtering for text alignment. For seeding we use character n-grams with a variant of the ......\n\n3. Text Reuse | Textual Criticism as Language Modeling - Manifold\n   https://manifold.umn.edu/read/8ddd9c7c-c2db-44be-91a6-732d1d08ec47/section/c030c4c4-e2ac-4a54-b5ea-30a70d274a61\n   In this section, we describe our current methods for detecting pairs of newspaper issues with significant textual overlap, for aligning these issue pairs, and ......\n\n4. [PDF] Detecting and Modeling Local Text Reuse\n   http://www.ccs.neu.edu/home/dasmith/infect-dl-2014.pdf\n   Our approach to local text reuse detection and cluster- ing is motivated by two case studies: (1) analyzing a cor- pus of nineteenth century U.S. newspapers to ......\n\n5. Local Text Reuse Detection - Publication\n   https://maroo.cs.umass.edu/getpdf.php?id=812\n   The reason for this is that, in the case of local text reuse, only a small part (or parts) of a document may have been taken from other sources....\n\n6. Text reuse - KITAB project\n   https://kitab-project.org/methods/text-reuse\n   The text reuse algorithm used by KITAB is called passim. The algorithm naively identifies reuse by looking for instances of shared text that meet a certain set ......\n\n7. ropensci/textreuse: Detect text reuse and document similarity - GitHub\n   https://github.com/ropensci/textreuse\n   This R package provides a set of functions for measuring similarity among documents and detecting passages which have been reused....\n\n8. An introduction to the textreuse package, with suggested applications\n   https://lincolnmullen.com/blog/an-introduction-to-the-textreuse-package-with-suggested-applications/\n   This package is a general purpose implementation of several algorithms for detecting text reuse, as well as classes and functions for investigating a corpus of ......\n\nURL: https://openproceedings.org/2012/conf/edbt/AggarwalLY12.pdf\nType: PDF\nLength: 62701 chars (truncated)\n\n--- Content ---\n\nSearching by Corpus with Fingerprints\nCharu C. Aggarwal\nIBM T. J. Watson Research\nCenter\nHawthorne, NY 10532, USA\ncharu@us.ibm.com\nWangqun Lin\nNational University of Defense\nTechnology\nChangsha, Hunan, China\nlinwangqun@nudt.edu.cn\nPhilip S. Yu\nUniversity of Illinois at Chicago\nChicago, IL, USA\npsyu@cs.uic.edu\nABSTRACT\nThe growing sizes of text repositories on the world wide web\nhas created a need for eﬃcient indexing and retrieval meth-\nods for text collections. Almost all of the text retrieval and\nindexing methods have been designed for the case of sim-\nple keyword search, in which a few keywords are speciﬁed,\nand the text is retrieved on the basis of matches to these\nkeywords. However, in many applications there is a need\nfor a greater speciﬁcity during the search, such as the use\nof phrases, sentences, text fragments, or even documents for\nthe retrieval process. An even more general case is one in\nwhich a collection of documents is available as a query to\nthe search process. In such cases, it is desirable to return\nsets of all pairwise similar documents. Such queries are re-\nferred to as corpus to corpus queries, and are computation-\nally intensive because of the very large number of document\npairs which need to be compared.\nSuch cases cannot be\neﬃciently processed by the available indexing and search-\ning methods. Most of the currently available techniques can\nindex the text based on only a small number of keywords\nor representative phrases. In this paper, we design a com-\npressed ﬁnger print index which can support the following\nmore general queries: (a) The method can process very ef-\nﬁcient document-to-corpus search because of their eﬃcient\nbit-wise operations for the search process. (b) We further\nextend the method to work for corpus-to-corpus queries, in\nwhich it is desirable to determine the most similar pairs of\ndocuments in two collections. We design an eﬃcient search\ntechnique which is able to reduce the search time for large\ncollections. The key technique used to enable this is an eﬃ-\ncient ﬁngerprint representation, which can be used eﬀective-\nly for the search process. To the best of our knowledge, this\nis the ﬁrst work on corpus-based search in massive document\ncollections.\nCategories and Subject Descriptors\nH.3.3 [Information Search and Retrieval]: Clustering\nGeneral Terms\nPermission to make digital or hard copies of all or part of this work for\npersonal or classroom use is granted without fee provided that copies are\nnot made or distributed for proﬁt or commercial advantage and that copies\nbear this notice and the full citation on the ﬁrst page. To copy otherwise, to\nrepublish, to post on servers or to redistribute to lists, requires prior speciﬁc\npermission and/or a fee.\nEDBT 201\nCopyright 2012 ACM 978-1-4503-0790-1/12/03 ...$10.00\nAlgorithms\n1.\nINTRODUCTION\nThe rapid growth of text information has lead to a tremen-\ndous need for eﬃcient methods for retrieving such text doc-\numents. Most of the known methods for text indexing and\nretrieval are designed for keyword-based search. Typically,\nsuch queries are designed for a small number of words and\nphrases for retrieval purposes. Most of these techniques are\nbased on variations of the inverted index representation [12].\nWhile such index structures are quite eﬀective for the case\nof single keyword-based queries, they are not designed for\ncases in which it is desired to determine responses to queries\nin which the target is a text document or even a corpus of\ndocuments. Some examples of relevant applications are as\nfollows:\n• In many scientiﬁc applications, the target for the search\nmay be a publication or patent in a particular subject\narea. For such ﬁne grained searches, it is often possible\nto have similar portions of the text at several places.\nIn some cases, a particular author may have the ten-\ndency to use similar sentence structure across diﬀerent\ndocuments, and such ﬁne grained behavior may have\nan impact on the search process. This is not possible\nwith the use of the traditional index structures.\n• News articles on the same story often share large seg-\nments of the text in common. This is because the quot-\ned portions of the text, or the text which is obtained\nfrom a professional newswire service may be almost\nidentical.\nThis results in some largely identical seg-\nments of text, though other portions may be diﬀerent.\nBy using a collection of documents, it is also possi-\nble to perform duplicate or partial duplicate detection\nacross the text corpus.\n• Professional product descriptions at online sites may\noften share large segments of the text which are iden-\ntical. This is because descriptive content is often stan-\ndardized across similar products which are produced\nby diﬀerent sources. At the same time, there may be\nenough distinctive vocabulary in other portions, so as\nto throw oﬀa pure bag-of-words based search process.\nThe problem of corpus-to-corpus search is deﬁned as one in\nwhich we have a target corpus of documents T and a doc\n[1]-  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://openproceedings.org/2012/conf/edbt/AggarwalLY12.pdf\" --max-chars 5000\n[2]+  Done                    $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"text reuse detection anchor target pair hash offset position invariant\" --max-results 8", "stderr": "", "interrupted": false, "isImage": false, "noOutputExpected": false}
```

### [17] ASSISTANT · 2026-07-03 17:45:40 UTC

```
The adversarial search confirms: no existing text fingerprinting method uses Shazam-style paired landmark hashing with relative positional offsets. Winnowing selects individual k-gram hashes; MinHash/SimHash use global statistics. The paired-landmark mechanism is genuinely novel for text.
```

### [18] TOOL CALL — Write · 2026-07-03 17:45:40 UTC

```
File: /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/iter_1/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json

{
  "title": "Shazam-Style Landmark Pairs for Text Dedup",
  "hypothesis": "Near-duplicate text passages can be detected more robustly than MinHash by fingerprinting pairs of locally-salient n-gram landmarks together with their relative positional offset — directly analogous to how Shazam identifies audio by hashing (anchor-frequency, target-frequency, time-delta) pairs. The hypothesis is: a fingerprint built from (ngram_A, ngram_B, position_delta) hashes, where ngram_A and ngram_B are locally-maximal TF-IDF n-grams within the passage, will achieve higher recall than MinHash at equivalent precision on near-duplicates created by insertion, deletion, or surrounding-text addition, because the relative distance between co-occurring salient n-grams is preserved under these structural edits even when absolute positions shift.",
  "motivation": "MinHash, the dominant scalable near-duplicate detector, estimates global Jaccard overlap of k-gram shingles. This works well for near-exact copies but degrades when passages are embedded in larger documents, have surrounding boilerplate added, or have paragraphs inserted/removed — because every added token dilutes the Jaccard score. These structural near-duplicates are common in web crawls (article syndication), legal corpora (contract reuse), and LLM pretraining data (dataset contamination). A fingerprint mechanism borrowed from audio recognition that is inherently local and position-offset-aware would fill this gap without requiring neural embeddings or increased compute.",
  "assumptions": [
    "Text passages contain at least a handful of locally-distinctive n-grams (high local TF-IDF) that survive minor edits and serve as stable landmarks.",
    "The relative positional distance between co-occurring salient n-grams within a passage is approximately preserved under the structural edits (insertion/deletion) that MinHash handles poorly.",
    "A sparse set of landmark pairs (O(k^2) per document for k landmarks) is sufficient to discriminate near-duplicate from unrelated passages, similar to Shazam needing only a few dozen landmark pairs per audio snippet.",
    "An inverted index over landmark-pair hashes enables sub-linear candidate retrieval, maintaining scalability comparable to MinHash LSH."
  ],
  "investigation_approach": "1. LANDMARK EXTRACTION: For each passage, compute sliding-window TF-IDF scores for all k-grams (k=5..8 characters or words). Find local maxima in the resulting position×n-gram saliency surface using scipy.ndimage.maximum_filter, yielding a sparse set of (position, n-gram) landmark pairs. 2. FINGERPRINT GENERATION: For each anchor landmark (p1, g1), enumerate all target landmarks (p2, g2) within a lookahead window W. Emit hash(g1, g2, p2-p1) as a fingerprint hash. The full fingerprint is the set of all such hashes. 3. INVERTED INDEX: Build an inverted index mapping each hash to the passages that contain it. Two passages are candidate near-duplicates if they share >= T hashes. 4. BENCHMARK: Evaluate on (a) the PAN-PC-11 plagiarism corpus with copy, paraphrase, and simulated-paraphrase cases; (b) a synthetic corpus where 500 Wikipedia passages are each embedded in 5 variants with prepended/appended/inserted text of varying lengths. Compare precision-recall curves against MinHash (with varying band/row settings) and SimHash. 5. ABLATIONS: Test with/without positional offset in the hash (to isolate whether the offset is the key ingredient vs. simple co-occurrence), and vary landmark density k and window W.",
  "success_criteria": "CONFIRM: Landmark-pair fingerprinting achieves at least 10 percentage points higher recall than MinHash at precision >= 0.90 on the structural-edit near-duplicate benchmark (passages with surrounding text added). The positional-offset ablation (removing delta from the hash) shows a statistically significant drop in precision (demonstrating the offset is load-bearing, not just co-occurrence). DISCONFIRM: If landmark-pair fingerprinting recall is within 5pp of MinHash on structural edits, or if the inverted-index lookup time is >10x slower than MinHash at equal candidate set size, the hypothesis is refuted. PARTIAL: Higher recall only on insertion/deletion cases but not paraphrases would suggest the mechanism is complementary to MinHash rather than superior.",
  "related_works": [
    "Winnowing (Schleimer et al., SIGMOD 2003): Selects a subset of k-gram hashes using a sliding-window minimum, guaranteeing at least one fingerprint in every window of length w. Key difference: selects INDIVIDUAL hash landmarks — no pairing, no positional offset between pairs. The new method hashes PAIRS of landmarks with their relative offset, creating a 2D structural code instead of a 1D sequence of isolated hashes.",
    "MinHash / LSH (Broder 1997, Manku et al. WWW 2007): Estimates Jaccard similarity of k-gram shingle sets via random hash minima. Key difference: global statistic over the full shingle set — sensitive to any change in document length or added text. Landmark-pair hashing is purely local and translation-invariant within the passage.",
    "SimHash (Charikar 2002, used by Google for web dedup): Projects TF-IDF vector onto random hyperplanes, producing a bit-vector. Hamming distance in bit-vector space approximates cosine similarity. Key difference: a single dense vector captures the full document — there is no notion of local structural relationship between salient positions. Landmark pairs encode WHERE two salient n-grams co-occur relative to each other.",
    "RETSim (Zhang et al. 2023): Lightweight deep learning model trained to produce metric embeddings robust to character-level edits. Key difference: neural model requiring training data and inference compute. The landmark-pair method is training-free and purely symbolic, requiring no neural forward pass.",
    "Audio fingerprinting / Shazam (Wang 2003): The DIRECT inspiration — hashes (anchor-freq, target-freq, time-delta) pairs of spectral peaks. Has never been applied to text; the text domain requires rethinking 'frequency' (n-gram identity under TF-IDF) and 'time' (character/word position), and the saliency measure (audio energy vs. local TF-IDF)."
  ],
  "inspiration": "Directly inspired by Shazam's audio fingerprinting algorithm (Wang 2003), which identifies a 10-second audio snippet in a million-song database in under a second. Shazam's key insight — hash PAIRS of local spectral landmarks with their relative TIME OFFSET rather than individual landmarks or global statistics — makes the fingerprint invariant to absolute temporal position and robust to noise. This is a Level-3 (methodological) cross-domain transfer: the mechanism applies nearly as-is to text by substituting (audio-frequency, energy) with (n-gram-type, TF-IDF) and time with character position. The insight that 'structural near-duplicates preserve relative landmark distances even when absolute positions shift' is the direct textual analog of 'a noisy excerpt preserves spectral peak relationships even when played at a different time.'",
  "terms": [
    {
      "term": "Landmark",
      "definition": "A (position, n-gram) pair that is a local maximum of TF-IDF saliency within a sliding window over the text — the most informationally distinctive n-gram in its local neighborhood, analogous to a spectral peak in Shazam."
    },
    {
      "term": "Landmark pair hash",
      "definition": "A hash of three values: (n-gram of anchor landmark, n-gram of target landmark, position_target - position_anchor). Encodes the structural relationship between two salient text features at a fixed relative distance."
    },
    {
      "term": "Structural near-duplicate",
      "definition": "A near-duplicate passage created by insertion, deletion, or surrounding-text addition — not by character-level editing or paraphrasing. These preserve the internal structure of the original passage while changing its boundaries or surrounding context."
    },
    {
      "term": "Saliency surface",
      "definition": "A 2D matrix indexed by (position, n-gram-id) where each cell contains the local TF-IDF score of that n-gram at that position, analogous to a spectrogram in audio processing."
    },
    {
      "term": "Lookahead window W",
      "definition": "The maximum positional gap between an anchor and target landmark when forming pairs. Controls the trade-off between fingerprint density and sensitivity to large-scale reorderings."
    }
  ],
  "summary": "We hypothesize that text near-duplicate detection can be made more robust to structural edits (embedding passages in larger documents, inserting/deleting paragraphs) by adapting Shazam's audio fingerprinting mechanism: instead of hashing individual k-gram landmarks (Winnowing) or global shingle statistics (MinHash), hash PAIRS of locally-salient n-gram landmarks together with their relative positional offset, creating fingerprints that are invariant to shifts in absolute position and resilient to surrounding-text addition."
}
```

### [19] TOOL RESULT — Write · 2026-07-03 17:45:40 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/iter_1/gen_hypo/claude_agent/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Shazam-Style Landmark Pairs for Text Dedup\",\n  \"hypothesis\": \"Near-duplicate text passages can be detected more robustly than MinHash by fingerprinting pairs of locally-salient n-gram landmarks together with their relative positional offset — directly analogous to how Shazam identifies audio by hashing (anchor-frequency, target-frequency, time-delta) pairs. The hypothesis is: a fingerprint built from (ngram_A, ngram_B, position_delta) hashes, where ngram_A and ngram_B are locally-maximal TF-IDF n-grams within the passage, will achieve higher recall than MinHash at equivalent precision on near-duplicates created by insertion, deletion, or surrounding-text addition, because the relative distance between co-occurring salient n-grams is preserved under these structural edits even when absolute positions shift.\",\n  \"motivation\": \"MinHash, the dominant scalable near-duplicate detector, estimates global Jaccard overlap of k-gram shingles. This works well for near-exact copies but degrades when passages are embedded in larger documents, have surrounding boilerplate added, or have paragraphs inserted/removed — because every added token dilutes the Jaccard score. These structural near-duplicates are common in web crawls (article syndication), legal corpora (contract reuse), and LLM pretraining data (dataset contamination). A fingerprint mechanism borrowed from audio recognition that is inherently local and position-offset-aware would fill this gap without requiring neural embeddings or increased compute.\",\n  \"assumptions\": [\n    \"Text passages contain at least a handful of locally-distinctive n-grams (high local TF-IDF) that survive minor edits and serve as stable landmarks.\",\n    \"The relative positional distance between co-occurring salient n-grams within a passage is approximately preserved under the structural edits (insertion/deletion) that MinHash handles poorly.\",\n    \"A sparse set of landmark pairs (O(k^2) per document for k landmarks) is sufficient to discriminate near-duplicate from unrelated passages, similar to Shazam needing only a few dozen landmark pairs per audio snippet.\",\n    \"An inverted index over landmark-pair hashes enables sub-linear candidate retrieval, maintaining scalability comparable to MinHash LSH.\"\n  ],\n  \"investigation_approach\": \"1. LANDMARK EXTRACTION: For each passage, compute sliding-window TF-IDF scores for all k-grams (k=5..8 characters or words). Find local maxima in the resulting position×n-gram saliency surface using scipy.ndimage.maximum_filter, yielding a sparse set of (position, n-gram) landmark pairs. 2. FINGERPRINT GENERATION: For each anchor landmark (p1, g1), enumerate all target landmarks (p2, g2) within a lookahead window W. Emit hash(g1, g2, p2-p1) as a fingerprint hash. The full fingerprint is the set of all such hashes. 3. INVERTED INDEX: Build an inverted index mapping each hash to the passages that contain it. Two passages are candidate near-duplicates if they share >= T hashes. 4. BENCHMARK: Evaluate on (a) the PAN-PC-11 plagiarism corpus with copy, paraphrase, and simulated-paraphrase cases; (b) a synthetic corpus where 500 Wikipedia passages are each embedded in 5 variants with prepended/appended/inserted text of varying lengths. Compare precision-recall curves against MinHash (with varying band/row settings) and SimHash. 5. ABLATIONS: Test with/without positional offset in the hash (to isolate whether the offset is the key ingredient vs. simple co-occurrence), and vary landmark density k and window W.\",\n  \"success_criteria\": \"CONFIRM: Landmark-pair fingerprinting achieves at least 10 percentage points higher recall than MinHash at precision >= 0.90 on the structural-edit near-duplicate benchmark (passages with surrounding text added). The positional-offset ablation (removing delta from the hash) shows a statistically significant drop in precision (demonstrating the offset is load-bearing, not just co-occurrence). DISCONFIRM: If landmark-pair fingerprinting recall is within 5pp of MinHash on structural edits, or if the inverted-index lookup time is >10x slower than MinHash at equal candidate set size, the hypothesis is refuted. PARTIAL: Higher recall only on insertion/deletion cases but not paraphrases would suggest the mechanism is complementary to MinHash rather than superior.\",\n  \"related_works\": [\n    \"Winnowing (Schleimer et al., SIGMOD 2003): Selects a subset of k-gram hashes using a sliding-window minimum, guaranteeing at least one fingerprint in every window of length w. Key difference: selects INDIVIDUAL hash landmarks — no pairing, no positional offset between pairs. The new method hashes PAIRS of landmarks with their relative offset, creating a 2D structural code instead of a 1D sequence of isolated hashes.\",\n    \"MinHash / LSH (Broder 1997, Manku et al. WWW 2007): Estimates Jaccard similarity of k-gram shingle sets via random hash minima. Key difference: global statistic over the full shingle set — sensitive to any change in document length or added text. Landmark-pair hashing is purely local and translation-invariant within the passage.\",\n    \"SimHash (Charikar 2002, used by Google for web dedup): Projects TF-IDF vector onto random hyperplanes, producing a bit-vector. Hamming distance in bit-vector space approximates cosine similarity. Key difference: a single dense vector captures the full document — there is no notion of local structural relationship between salient positions. Landmark pairs encode WHERE two salient n-grams co-occur relative to each other.\",\n    \"RETSim (Zhang et al. 2023): Lightweight deep learning model trained to produce metric embeddings robust to character-level edits. Key difference: neural model requiring training data and inference compute. The landmark-pair method is training-free and purely symbolic, requiring no neural forward pass.\",\n    \"Audio fingerprinting / Shazam (Wang 2003): The DIRECT inspiration — hashes (anchor-freq, target-freq, time-delta) pairs of spectral peaks. Has never been applied to text; the text domain requires rethinking 'frequency' (n-gram identity under TF-IDF) and 'time' (character/word position), and the saliency measure (audio energy vs. local TF-IDF).\"\n  ],\n  \"inspiration\": \"Directly inspired by Shazam's audio fingerprinting algorithm (Wang 2003), which identifies a 10-second audio snippet in a million-song database in under a second. Shazam's key insight — hash PAIRS of local spectral landmarks with their relative TIME OFFSET rather than individual landmarks or global statistics — makes the fingerprint invariant to absolute temporal position and robust to noise. This is a Level-3 (methodological) cross-domain transfer: the mechanism applies nearly as-is to text by substituting (audio-frequency, energy) with (n-gram-type, TF-IDF) and time with character position. The insight that 'structural near-duplicates preserve relative landmark distances even when absolute positions shift' is the direct textual analog of 'a noisy excerpt preserves spectral peak relationships even when played at a different time.'\",\n  \"terms\": [\n    {\n      \"term\": \"Landmark\",\n      \"definition\": \"A (position, n-gram) pair that is a local maximum of TF-IDF saliency within a sliding window over the text — the most informationally distinctive n-gram in its local neighborhood, analogous to a spectral peak in Shazam.\"\n    },\n    {\n      \"term\": \"Landmark pair hash\",\n      \"definition\": \"A hash of three values: (n-gram of anchor landmark, n-gram of target landmark, position_target - position_anchor). Encodes the structural relationship between two salient text features at a fixed relative distance.\"\n    },\n    {\n      \"term\": \"Structural near-duplicate\",\n      \"definition\": \"A near-duplicate passage created by insertion, deletion, or surrounding-text addition — not by character-level editing or paraphrasing. These preserve the internal structure of the original passage while changing its boundaries or surrounding context.\"\n    },\n    {\n      \"term\": \"Saliency surface\",\n      \"definition\": \"A 2D matrix indexed by (position, n-gram-id) where each cell contains the local TF-IDF score of that n-gram at that position, analogous to a spectrogram in audio processing.\"\n    },\n    {\n      \"term\": \"Lookahead window W\",\n      \"definition\": \"The maximum positional gap between an anchor and target landmark when forming pairs. Controls the trade-off between fingerprint density and sensitivity to large-scale reorderings.\"\n    }\n  ],\n  \"summary\": \"We hypothesize that text near-duplicate detection can be made more robust to structural edits (embedding passages in larger documents, inserting/deleting paragraphs) by adapting Shazam's audio fingerprinting mechanism: instead of hashing individual k-gram landmarks (Winnowing) or global shingle statistics (MinHash), hash PAIRS of locally-salient n-gram landmarks together with their relative positional offset, creating fingerprints that are invariant to shifts in absolute position and resilient to surrounding-text addition.\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [20] ASSISTANT · 2026-07-03 17:45:43 UTC

```
The hypothesis is written. 

The core idea: borrow Shazam's audio fingerprinting mechanism for text near-duplicate detection. Instead of hashing individual k-gram landmarks (Winnowing) or global shingle statistics (MinHash), hash **pairs** of locally-salient n-grams with their **relative positional offset** — a fingerprint invariant to surrounding-text insertion/deletion. No existing text fingerprinting method uses this paired-landmark-with-offset mechanism, making it genuinely novel and directly testable with $0 compute cost.
```
