# review_hypo — create_idea

> Phase: `hypo_loop` · round 1 · `review_hypo`
> Run: `run_Bd0c_4hy9OC-` — Near Duplicate Detection
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `review_hypo` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-07-03 17:45:47 UTC

```
model: claude-sonnet-4-6 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/iter_1/review_hypo
```

### [2] SYSTEM-USER prompt · 2026-07-03 17:45:53 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviewer (Step 2.2: REVIEW_HYPO)

Pipeline: GEN_HYPO → REVIEW_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You review a hypothesis BEFORE any experiments run. Catch problems early.

Rigorous pre-flight check → saves compute. Rubber-stamping → wasted pipeline run.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the hypothesis under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of
this research hypothesis BEFORE any experiments have been run.

GOAL: Your review feeds directly back to the hypothesis author. The objective is to
maximize the overall review score in subsequent rounds. Every piece of feedback you
give should be written with this goal in mind — prioritize the critiques and suggestions
that would produce the largest score improvement if addressed. Don't waste the author's
iteration budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the ideas new? Novel combination of known techniques? Clear
    differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the proposal technically sound? Are claims well supported? Is the
    methodology appropriate? Are the authors honest about limitations?
(c) Clarity: Is the hypothesis clearly written and well organized? Does it provide
    enough information for an expert to understand and evaluate it?
(d) Significance: Are the expected results important? Would others build on this?
    Does it address a meaningful problem better than prior work?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims and proposed methodology:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would waste compute if not fixed) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Flag fatal flaws that would make experiments pointless if not addressed first

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

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

<review_context>
No experiments have been run yet — evaluate the hypothesis purely on its merits.
</review_context>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. Use it for judging whether the hypothesis is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-multi-llm-agents** — Guide for implementing Multi-LLM Agent Systems research using Mirascope orchestration, HuggingFace datasets/evaluation, and proven multi-agent patterns.
</available_domain_handbooks>





<task>
Provide a thorough peer review of this research hypothesis.

STEP 1 — GROUND YOUR REVIEW IN EVIDENCE:
Before writing critiques, search for relevant context to make your review authoritative:
- Search for accepted papers at top venues in this area — what level of
  contribution gets accepted? How does this hypothesis compare?
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes in the literature

STEP 2 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would waste compute if not fixed) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Flag fatal flaws that would waste compute if not fixed first.

STABILITY IS OK: If the hypothesis is on track and just needs more iterations to prove itself,
keep your feedback similar to the previous round. Don't manufacture new critiques — only escalate
when the revision introduced new issues or failed to address prior ones.

STEP 3 — H↔H EDGE:
This is the first iteration — there is no previous hypothesis. Leave
``relation_type`` null and ``relation_rationale`` empty.

Provide your review via structured output.
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
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "ReviewerFeedback + Moulines H\u2194H typology for hypo_loop iterations.\n\nAdds ``relation_type`` + ``relation_rationale`` so the trace projection\ncan build a typed edge from the previous iteration's hypothesis to\nthis iteration's. On iteration 1 (no previous), both fields are\nempty/None.",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    },
    "relation_type": {
      "anyOf": [
        {
          "enum": [
            "evolution",
            "embedding",
            "replacement"
          ],
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": null,
      "description": "Moulines's structuralist typology classifying how this iteration's hypothesis relates to the previous iteration's: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (Kuhnian shift). Leave null on the first iteration (no previous hypothesis).",
      "title": "Relation Type"
    },
    "relation_rationale": {
      "default": "",
      "description": "Brief rationale (one short line, \u2264120 chars) for the relation_type. Empty on the first iteration.",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "HypoReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-07-03 17:45:53 UTC

```
A simple and efficient MinHash-based method for detecting near-duplicate text passages in large corpora.
```

### [4] ASSISTANT · 2026-07-03 17:45:57 UTC

```
I'll research the relevant prior work before writing the review.
```

### [5] TOOL CALL — Skill · 2026-07-03 17:45:57 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-07-03 17:45:57 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — ToolSearch · 2026-07-03 17:45:59 UTC

```
{'query': 'select:WebSearch,WebFetch'}
```

### [8] TOOL RESULT — ToolSearch · 2026-07-03 17:45:59 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 21}
```

### [9] TOOL CALL — WebSearch · 2026-07-03 17:46:03 UTC

```
text near-duplicate detection fingerprinting landmark pairs positional offset 2023 2024 2025
```

### [10] TOOL CALL — WebSearch · 2026-07-03 17:46:03 UTC

```
Winnowing text fingerprinting near-duplicate detection survey 2024
```

### [11] TOOL RESULT — WebSearch · 2026-07-03 17:46:09 UTC

```
{"query": "text near-duplicate detection fingerprinting landmark pairs positional offset 2023 2024 2025", "results": [{"tool_use_id": "srvtoolu_012GosZWd2zRJGdLTomQ3Sfi", "content": [{"title": "RETSim: Resilient and Efficient Text Similarity", "url": "https://arxiv.org/pdf/2311.17264"}, {"title": "Near-Duplicate Text Alignment under Weighted Jaccard Similarity", "url": "https://arxiv.org/pdf/2509.00627"}, {"title": "US8750624B2 - Detection of duplicate document content using two-dimensional visual fingerprinting - Google Patents", "url": "https://patents.google.com/patent/US8750624B2/en"}, {"title": "(PDF) Near-Duplicate Web Page Detection: An Efficient Approach Using Clustering, Sentence Feature and Fingerprinting", "url": "https://www.researchgate.net/publication/261577147_Near-Duplicate_Web_Page_Detection_An_Efficient_Approach_Using_Clustering_Sentence_Feature_and_Fingerprinting"}, {"title": "Detecting duplicate and near-duplicate files", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6658423"}, {"title": "Document near-duplicate detection", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7707157"}, {"title": "Document near-duplicate detection", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7962491"}, {"title": "Fingerprint-Based Near-Duplicate Document Detection with Applications to SNS Spam Detection - Phuc-Tran Ho, Sung-Ryul Kim, 2014", "url": "https://journals.sagepub.com/doi/10.1155/2014/612970"}, {"title": "Near-duplicate document detection for web crawling", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8548972"}]}, "I've found several relevant results on near-duplicate text detection with fingerprinting techniques:\n\n## Key Research Findings:\n\n**Recent Work (2023-2024):**\n\nRecent research includes benchmarks like the NEWS-COPY Deduplication dataset with 27,210 historical news articles and the CORE Near-Duplicates dataset with 100k scholarly articles, both focusing on detecting near-duplicate content from sources like OCR errors, plagiarism, and news aggregation.\n\nNear-duplicate text alignment research includes work with one permutation hashing, published in 2024. Winnowing is a technique for local algorithms for document fingerprinting, which has been foundational in this area.\n\n**Fingerprinting Approaches:**\n\nNear-duplicate detection systems typically include fingerprint creation components that generate compact representations of documents. Similarity detection between documents can be computed as the hamming distance between fingerprints.\n\nThe search results show that fingerprinting-based approaches remain an active area of research, with recent work comparing various algorithms like RETSim and MinHash for near-duplicate detection tasks across different document types and conditions."], "durationSeconds": 7.006209588999998, "searchCount": 1}
```

### [12] TOOL RESULT — WebSearch · 2026-07-03 17:46:11 UTC

```
{"query": "Winnowing text fingerprinting near-duplicate detection survey 2024", "results": [{"tool_use_id": "srvtoolu_017x3DxPCWniogkXPHvFBwZP", "content": [{"title": "(PDF) Winnowing: Local Algorithms for Document Fingerprinting", "url": "https://www.researchgate.net/publication/2840981_Winnowing_Local_Algorithms_for_Document_Fingerprinting"}, {"title": "RETSim: Resilient and Efficient Text Similarity", "url": "https://arxiv.org/pdf/2311.17264"}, {"title": "[PDF] Winnowing: local algorithms for document fingerprinting | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/Winnowing:-local-algorithms-for-document-Schleimer-Wilkerson/73acc491ec7eb8f0a29e0f06397cb517b79e658b"}, {"title": "Fingerprinting (hash-based methods) for plagiarism detection | Plagiarism Checker", "url": "https://www.plagiarismchecker.net/articles/fingerprinting-hash-based-methods-for-plagiarism-detection/"}, {"title": "Near-duplicate document detection for web crawling", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8140505"}, {"title": "Near-Duplicate Text Alignment under Weighted Jaccard Similarity", "url": "https://arxiv.org/pdf/2509.00627"}, {"title": "Determining near duplicate “noisy” data objects", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8391614"}, {"title": "Near-duplicate document detection for web crawling", "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8548972"}]}, "Based on the search results, here's what I found regarding winnowing, text fingerprinting, and near-duplicate detection:\n\n## Winnowing Algorithm\n\nWinnowing works by sliding a fixed-size window over the sequence of hash values and, for each window, selecting the minimum hash value in that window as a fingerprint. Winnowing is an efficient local fingerprinting algorithm, and winnowing's performance is within 33% of the lower bound.\n\n## Near-Duplicate Detection Applications\n\nSystems using these techniques reliably detected near-duplicate texts and paraphrased passages within practical runtimes on standard laboratory computers. Hybrid similarity analysis combines n-gram shingling, Winnowing fingerprinting for quick candidate retrieval, and TF-IDF with cosine similarity for detailed scoring, enabling detection of direct copying, paraphrased content, and self-plagiarism.\n\n## Related Approaches\n\nMinHash was pioneered in finding near-duplicate web pages and has been applied to plagiarism detection, compressing the fingerprint set while preserving the resemblance information. This technique allows large-scale plagiarism search engines to query a new document's signature against a database in sub-linear time, though MinHash is an approximate method that trades some accuracy for speed.\n\n## Recent Research\n\nRecent work includes near-duplicate text alignment with one permutation hashing published in 2024."], "durationSeconds": 8.110641259, "searchCount": 1}
```

### [13] TOOL CALL — WebSearch · 2026-07-03 17:46:15 UTC

```
Shazam audio fingerprinting text adaptation NLP document similarity
```

### [14] TOOL CALL — WebSearch · 2026-07-03 17:46:15 UTC

```
MinHash structural near-duplicate limitations surrounding text insertion LLM pretraining dedup 2024
```

### [15] TOOL RESULT — WebSearch · 2026-07-03 17:46:23 UTC

```
{"query": "MinHash structural near-duplicate limitations surrounding text insertion LLM pretraining dedup 2024", "results": [{"tool_use_id": "srvtoolu_016xQzJSq4gTHqMw2FtvrFCq", "content": [{"title": "MinHash: Jaccard Similarity, LSH, and Near-Duplicate Detection - Interactive | Michael Brenndoerfer | Michael Brenndoerfer", "url": "https://mbrenndoerfer.com/writing/minhash-algorithm-jaccard-similarity-lsh-deduplication"}, {"title": "Merlin: Deterministic Byte-Exact Deduplication for Lossless Context Optimization in Large Language Model Inference", "url": "https://arxiv.org/pdf/2605.09990"}, {"title": "Evaluation of Document Deduplication Algorithms for Large Text Corpora | Machine Learning, Optimization, and Data Science", "url": "https://dl.acm.org/doi/10.1007/978-3-031-82481-4_27"}, {"title": "DecomposeRL: Learning to Ask Useful, Informative, and Diverse Questions for Semi-Supervised, Traceable Claim Verification", "url": "https://arxiv.org/pdf/2605.27858"}, {"title": "SEDD: Scalable and Efficient Dataset Deduplication with GPUs", "url": "https://arxiv.org/pdf/2501.01046"}, {"title": "D4: Improving LLM Pretraining via Document De-Duplication and Diversification", "url": "https://arxiv.org/pdf/2308.12284"}, {"title": "D4: Improving LLM Pretraining via Document De-Duplication and Diversiﬁcation", "url": "https://proceedings.neurips.cc/paper_files/paper/2023/file/a8f8cbd7f7a5fb2c837e578c75e5b615-Paper-Datasets_and_Benchmarks.pdf"}, {"title": "FOLD: Fuzzy Online Deduplication for Very Large Evolving Datasets via Approximate Nearest Neighbor Search", "url": "https://arxiv.org/pdf/2606.03001"}, {"title": "Byte-Exact Deduplication in Retrieval-Augmented Generation: A Three-Regime Empirical Analysis Across Public Benchmarks", "url": "https://arxiv.org/pdf/2605.09611"}, {"title": "Building a Large Japanese Web Corpus for Large Language Models", "url": "https://arxiv.org/pdf/2404.17733"}]}, "I found relevant information about MinHash and its limitations in the context of LLM pretraining deduplication. Here are the key findings:\n\n## MinHash Limitations\n\nThe primary concern for LLM training data is surface redundancy, which distorts the training distribution and causes memorization. However, semantic deduplication (removing documents that express the same ideas differently) is a separate and harder problem, typically approached using embedding-based similarity methods rather than MinHash.\n\nMinHash-based techniques catch near-duplicate claims but fail to identify paraphrased claim pairs. Additionally, documents can remain near-duplicates under shingle-based Jaccard similarity even when edits, formatting changes, boilerplate, or reordering alter their byte-level chunks.\n\n## Structural Limitations with Text Insertion\n\nA key limitation regarding text insertion appears in comparative studies: byte-exact deduplication captures 5.81% of duplicates while MinHash-LSH captures 31.32%, with byte-exact deduplication capturing lossless strict duplicates and MinHash-LSH capturing fuzzy semantic near-duplicates with controlled information loss.\n\n## Current Status in LLM Pretraining\n\nDespite these limitations, MinHash LSH remains the practical gold standard for near-duplicate detection at scale, with its linear-time signature computation, compact storage, tunable parameters, and probabilistic guarantees making it uniquely suited to the data volumes required for LLM pretraining. MinHash/LSH is the most suitable algorithm to deduplicate pretraining data for LLMs."], "durationSeconds": 7.435763489000001, "searchCount": 1}
```

### [16] TOOL RESULT — WebSearch · 2026-07-03 17:46:23 UTC

```
{"query": "Shazam audio fingerprinting text adaptation NLP document similarity", "results": [{"tool_use_id": "srvtoolu_01WVU2cNmM3X3GxMJSoC6mD9", "content": [{"title": "Application of SHAZAM-Based Audio Fingerprinting for Multilingual Indian Song Retrieval | Request PDF", "url": "https://www.researchgate.net/publication/300780288_Application_of_SHAZAM-Based_Audio_Fingerprinting_for_Multilingual_Indian_Song_Retrieval"}, {"title": "A Short Introduction to Audio Fingerprinting with a Focus on Shazam MUS-17", "url": "https://hpac.cs.umu.se/teaching/sem-mus-17/Reports/Froitzheim.pdf"}, {"title": "Machine Learning and Audio Data. I was excited to see WSJ featuring… | by Joyce J. Shen | Medium", "url": "https://medium.com/@joycejshen/machine-learning-and-audio-data-694bc870b339"}, {"title": "How does the Shazam app recognize music? An explanation of music recognition technology used in the Shazam app | TechAhead", "url": "https://www.techaheadcorp.com/blog/decoding-shazam-how-does-music-recognition-work-with-shazam-app/"}, {"title": "A local fingerprinting approach for audio copy detection", "url": "https://arxiv.org/pdf/1304.0793"}, {"title": "How does Shazam work? Music Recognition Algorithms, Fingerprinting, and Processing | Toptal®", "url": "https://www.toptal.com/developers/algorithms/shazam-it-music-processing-fingerprinting-and-recognition"}, {"title": "Application of Audio Fingerprinting Techniques for Real-Time Scalable Speech Retrieval and Speech Clusterization", "url": "https://arxiv.org/pdf/2410.21876"}, {"title": "Contrastive and Transfer Learning for Effective Audio Fingerprinting through a Real-World Evaluation Protocol", "url": "https://arxiv.org/pdf/2507.06070"}, {"title": "Topological fingerprints for audio identification", "url": "https://arxiv.org/pdf/2309.03516"}, {"title": "Audio Fingerprinting. When I discovered Shazam had the… | by Shivam | Medium", "url": "https://medium.com/@shivam01110011/audio-fingerprinting-aee18fb88d4a"}]}, "Based on the search results, here's what I found about audio fingerprinting techniques like Shazam and their potential connection to NLP and document similarity:\n\n## Shazam Audio Fingerprinting Overview\n\nShazam finds music by comparing the audio fingerprint of a user-supplied recording with fingerprints of known songs from its database. Shazam uses the peaks (maxima) observed in the spectrogram of an audio signal as the local feature points of a song, and feature descriptors (fingerprints) are generated from attributes of pairs of these points, where the frequency of every point in each pair as well as their time difference form a compact fingerprint.\n\n## Technical Process\n\nOnce the Shazam app records the first few seconds of a song or any audio content (max is 20 seconds of recording), it creates a unique audio fingerprint by converting the recorded analog sound into a spectrogram, wherein the X-axis represents time, the Y-axis represents frequency, and the density of the shading represents amplitude.\n\n## Limitations and Robustness\n\nThe extracted fingerprints are highly robust to audio compression, foreground noises, and other types of noise, but are not robust to tempo changes or pitch shifts.\n\n## Connection to Other Applications\n\nThe approach that Shazam uses is now applied in many different use cases, including voice biometrics and identification, recommendation systems (finding near-neighbors or clusters), and sound/audio/music generation.\n\nHowever, the search results did not contain specific information connecting audio fingerprinting techniques to NLP (Natural Language Processing) or document similarity directly. Those appear to be separate domains in the results."], "durationSeconds": 8.601473691000002, "searchCount": 1}
```

### [17] ASSISTANT · 2026-07-03 17:47:55 UTC

```
Now I have enough context. Let me write the review.
```

### [18] TOOL CALL — Write · 2026-07-03 17:47:55 UTC

```
File: /ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/iter_1/review_hypo/.terminal_claude_agent_struct_out.json

{
  "overall_assessment": "The Shazam-to-text analogy is genuinely novel and the motivation is well-grounded: MinHash's Jaccard-based global statistics do degrade when passages are embedded in larger documents, and this is a real pain point in web-crawl and LLM-pretraining deduplication pipelines. The cross-domain transfer is intellectually clean and the investigation plan has concrete success criteria and a well-chosen ablation. However, three issues risk wasting compute if not addressed first: (1) the core assumption that relative landmark distances are preserved breaks down for intra-passage insertions, which is one of the targeted edit types; (2) the most natural strong baseline — passage-bounded MinHash — is missing, and if it closes the gap, the hypothesis is refuted without needing the new method; (3) TF-IDF landmark extraction requires corpus-level IDF statistics that are not available in typical streaming or online dedup scenarios, creating a practical circularity. These are fixable at the hypothesis level before experiments run.",
  "strengths": [
    "Genuinely novel cross-domain transfer: no prior published work appears to have adapted Shazam-style (anchor, target, delta) hashing to text near-duplicate detection. The level-3 methodological analogy is clean and well-articulated.",
    "The core motivation is technically sound and empirically well-known: MinHash Jaccard similarity degrades proportionally to the fraction of added tokens, so a 1000-token passage embedded in a 10,000-token document loses ~90% of its Jaccard score, making structural duplicates nearly undetectable at typical thresholds.",
    "Success criteria are concrete, quantitative, and falsifiable (10pp recall gain at ≥0.90 precision; offset ablation must show significant precision drop; 10x latency bound). These are exactly the right operationalizations.",
    "The positional-offset ablation (removing delta from the hash to test co-occurrence vs. structural relationship) is the correct key experiment and directly isolates the hypothesis mechanism.",
    "The investigation plan correctly identifies that PAN-PC-11 alone is insufficient and supplements it with a synthetic Wikipedia corpus targeting the specific structural edits of interest.",
    "Related work coverage is honest and appropriately scoped: Winnowing (1D analog), MinHash, SimHash, RETSim, and the original Shazam paper are all correctly positioned and differentiated."
  ],
  "dimension_scores": [
    {
      "dimension": "soundness",
      "score": 2,
      "justification": "The analogy is structurally sound for surrounding-text addition (the main claimed use case), but assumption #2 — that relative positional distance between co-occurring landmarks is preserved under the targeted edits — is only true for insertions/deletions outside the passage. Intra-passage insertions shift all downstream landmark positions, breaking the offset. This is a non-trivial failure mode for one of the three claimed edit types. Additionally, TF-IDF landmark extraction introduces a corpus-level dependency that is unaddressed.",
      "improvements": [
        "Explicitly bound the claim: the offset-preservation property holds for extra-passage edits (prepend/append) but NOT for intra-passage insertions between two landmarks. Revise assumption #2 to reflect this, or add an analysis of how many landmark pairs survive intra-passage insertion (hint: only pairs where both landmarks fall entirely before or after the insertion point).",
        "Address the IDF computation problem: TF-IDF requires IDF statistics from a reference corpus. In streaming dedup over a web crawl, you don't have this. Propose either (a) using a pre-built IDF table from a fixed reference corpus, (b) using character-n-gram hash local maxima as a corpus-free landmark alternative, or (c) bounding the experiment to the batch-dedup setting where IDF can be computed first."
      ]
    },
    {
      "dimension": "presentation",
      "score": 3,
      "justification": "The hypothesis is clearly written, well-organized, and provides good term definitions. The Shazam analogy is explained at exactly the right level of detail. Minor clarity issues exist around the saliency surface definition (it would be an enormous sparse matrix) and how 'local maxima' in a 2D space of position×n-gram are practically computed.",
      "improvements": [
        "Replace 'saliency surface as a 2D matrix indexed by (position, n-gram-id)' with a more practical description: compute TF-IDF for each (position, k-gram) pair in a sliding window, then find positions where the local k-gram score exceeds all neighbors within ±L positions. The 2D matrix framing implies O(|vocab|×|doc|) space which is impractical.",
        "Clarify whether 'position' means character offset or word/token index — this matters for the offset delta and for cross-document comparison when documents have different tokenizations."
      ]
    },
    {
      "dimension": "contribution",
      "score": 3,
      "justification": "If the experiments confirm the hypothesis, the contribution is meaningful for the LLM pretraining dedup community where structural duplicates from article syndication are a known problem. The training-free, purely symbolic method contrasts well with RETSim-style neural approaches. However, the contribution magnitude depends critically on whether a trivially stronger baseline (passage-bounded MinHash) is included and whether it can also solve the problem cheaply.",
      "improvements": [
        "Add passage-bounded MinHash as a baseline: this method simply computes MinHash over the detected 'core' passage (using the candidate landmark region) rather than the full document. If this trivially closes the gap with the new method, it significantly weakens the contribution. Include it to avoid a reviewer objection that will certainly arise.",
        "Quantify the expected speedup or storage advantage over neural alternatives (RETSim, embedding-based dedup) at web scale — this positions the contribution more concretely for the LLM pretraining audience."
      ]
    }
  ],
  "critiques": [
    {
      "category": "methodology",
      "severity": "major",
      "description": "The offset-preservation assumption (assumption #2) breaks for intra-passage insertions. The hypothesis claims the method handles 'insertion, deletion, or surrounding-text addition,' but for intra-passage insertions (a paragraph inserted in the middle of a passage), every landmark pair that straddles the insertion point will have a different offset in the modified passage. Only pairs where both landmarks fall before or after the insertion point are preserved. This is a critical failure mode for one of the three advertised edit types, and it means the method may not outperform MinHash on intra-passage insertion benchmarks.",
      "suggested_action": "Add a formal analysis of what fraction of landmark pairs survive each edit type. For surrounding-text addition (prepend/append): 100% of pairs preserved. For deletion of a suffix/prefix: pairs within the retained region preserved. For intra-passage insertion: only pairs where both landmarks are on the same side of the insertion point survive. Based on this, either (a) restrict the claimed edit types to extra-passage edits where the method is clearly correct, or (b) propose a tolerance mechanism (allow offset match within ±δ, analogous to Shazam's frequency bin tolerance) and add this to the method description."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "Missing strong baseline: passage-bounded MinHash. The natural response to 'MinHash degrades when a passage is embedded in a larger document' is to detect or estimate the passage boundaries first and apply MinHash only to the core passage. This is a known practical workaround. If passage-bounded MinHash achieves comparable recall gains, the landmark-pair method's contribution is marginal. The absence of this baseline is likely to be the first objection from reviewers.",
      "suggested_action": "Add passage-bounded MinHash as an explicit baseline in the benchmark. One concrete implementation: (1) run Winnowing to find the densest landmark region, (2) crop the document to that region, (3) apply standard MinHash to the cropped passage. This isolates whether the landmark-pair offset mechanism is necessary beyond simple passage cropping."
    },
    {
      "category": "methodology",
      "severity": "major",
      "description": "TF-IDF landmark extraction has a corpus-level IDF dependency. Computing TF-IDF requires IDF statistics over a reference corpus. For near-duplicate detection at web scale (the primary motivating use case), you are building the corpus incrementally — you cannot compute IDF before you have all documents. This creates either a circularity (use IDF from the dedup target corpus itself) or a distribution mismatch (use IDF from a separate reference corpus). Neither is addressed.",
      "suggested_action": "Either (a) restrict the evaluation to the batch-dedup setting where IDF is precomputed over a fixed corpus snapshot, and explicitly state this is not an online/streaming method; or (b) propose a corpus-free landmark selector such as local n-gram frequency within the document itself (self-IDF), or entropy-based local maxima, or character n-gram hash collisions. Compare both landmark selectors in the ablation."
    },
    {
      "category": "evidence",
      "severity": "major",
      "description": "PAN-PC-11 (2011) is not a good primary benchmark for the claimed use case. PAN-PC-11 targets academic plagiarism (copy, paraphrase, simulated paraphrase of Wikipedia articles) and does not include the web-crawl structural edits (article syndication, boilerplate addition) that motivate the hypothesis. Most modern systems already achieve near-saturating recall on the copy cases in PAN-PC-11, so the benchmark may not discriminate between methods on the proposed mechanism.",
      "suggested_action": "Demote PAN-PC-11 to a secondary benchmark and make the synthetic Wikipedia corpus (with prepend/append/insert variants) the primary evaluation. Additionally, consider using the CC-News or Common Crawl dedup benchmarks if available, or the CORE near-duplicates dataset mentioned in recent dedup surveys, to validate on realistic web-crawl distributions."
    },
    {
      "category": "scope",
      "severity": "minor",
      "description": "The O(k²) fingerprint count per document is stated as a property but its dependence on document length is unspecified. If k (number of landmark local maxima) grows linearly with document length n, then fingerprint count is O(n²), which is much worse than MinHash's O(n). This could make the method impractical for long documents.",
      "suggested_action": "Add an explicit analysis: either cap k (e.g., keep only the top-K highest-saliency landmarks, making k a constant), or show empirically that k grows sub-linearly with document length in typical corpora (e.g., because TF-IDF local maxima saturate). State the cap in the method description and include it in the runtime analysis."
    },
    {
      "category": "novelty",
      "severity": "minor",
      "description": "The hypothesis does not cite the 'term-pair indexing' literature in IR (e.g., Bernstein & Zobel 2004's work on feature-based copy detection, or Hoad & Zobel 2003 on 'Methods for Identifying Versioned and Plagiarised Documents'). These methods select salient terms and index their co-occurrence for copy detection, which is structurally adjacent to the proposed method. The differentiation from this work should be made explicit.",
      "suggested_action": "Search for and cite Hoad & Zobel 2003 (JASIST, 'Methods for identifying versioned and plagiarised documents') and related feature-based copy detection work. Explicitly state how the proposed method differs: the positional OFFSET delta between landmark pairs (not just co-occurrence) is the novel ingredient, and the local-maximum selection via TF-IDF saliency is the text analog of spectral peak selection."
    },
    {
      "category": "clarity",
      "severity": "minor",
      "description": "The lookahead window W interacts with the offset-preservation property in a non-obvious way. A large W captures more pairs but also captures pairs with large offsets that are more likely to be disrupted by intra-passage insertions. A small W is more robust to intra-passage edits but may miss pairs across paragraph boundaries.",
      "suggested_action": "Add a brief analysis of how W should be set relative to expected insertion size. Specifically, note that W should be smaller than the typical insertion block size to maintain offset preservation, and include W as an explicit ablation dimension in the experiment (not just varying k)."
    }
  ],
  "score": 5,
  "confidence": 4,
  "relation_type": null,
  "relation_rationale": ""
}
```

### [19] TOOL RESULT — Write · 2026-07-03 17:47:55 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_Bd0c_4hy9OC-/iter_1/review_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"overall_assessment\": \"The Shazam-to-text analogy is genuinely novel and the motivation is well-grounded: MinHash's Jaccard-based global statistics do degrade when passages are embedded in larger documents, and this is a real pain point in web-crawl and LLM-pretraining deduplication pipelines. The cross-domain transfer is intellectually clean and the investigation plan has concrete success criteria and a well-chosen ablation. However, three issues risk wasting compute if not addressed first: (1) the core assumption that relative landmark distances are preserved breaks down for intra-passage insertions, which is one of the targeted edit types; (2) the most natural strong baseline — passage-bounded MinHash — is missing, and if it closes the gap, the hypothesis is refuted without needing the new method; (3) TF-IDF landmark extraction requires corpus-level IDF statistics that are not available in typical streaming or online dedup scenarios, creating a practical circularity. These are fixable at the hypothesis level before experiments run.\",\n  \"strengths\": [\n    \"Genuinely novel cross-domain transfer: no prior published work appears to have adapted Shazam-style (anchor, target, delta) hashing to text near-duplicate detection. The level-3 methodological analogy is clean and well-articulated.\",\n    \"The core motivation is technically sound and empirically well-known: MinHash Jaccard similarity degrades proportionally to the fraction of added tokens, so a 1000-token passage embedded in a 10,000-token document loses ~90% of its Jaccard score, making structural duplicates nearly undetectable at typical thresholds.\",\n    \"Success criteria are concrete, quantitative, and falsifiable (10pp recall gain at ≥0.90 precision; offset ablation must show significant precision drop; 10x latency bound). These are exactly the right operationalizations.\",\n    \"The positional-offset ablation (removing delta from the hash to test co-occurrence vs. structural relationship) is the correct key experiment and directly isolates the hypothesis mechanism.\",\n    \"The investigation plan correctly identifies that PAN-PC-11 alone is insufficient and supplements it with a synthetic Wikipedia corpus targeting the specific structural edits of interest.\",\n    \"Related work coverage is honest and appropriately scoped: Winnowing (1D analog), MinHash, SimHash, RETSim, and the original Shazam paper are all correctly positioned and differentiated.\"\n  ],\n  \"dimension_scores\": [\n    {\n      \"dimension\": \"soundness\",\n      \"score\": 2,\n      \"justification\": \"The analogy is structurally sound for surrounding-text addition (the main claimed use case), but assumption #2 — that relative positional distance between co-occurring landmarks is preserved under the targeted edits — is only true for insertions/deletions outside the passage. Intra-passage insertions shift all downstream landmark positions, breaking the offset. This is a non-trivial failure mode for one of the three claimed edit types. Additionally, TF-IDF landmark extraction introduces a corpus-level dependency that is unaddressed.\",\n      \"improvements\": [\n        \"Explicitly bound the claim: the offset-preservation property holds for extra-passage edits (prepend/append) but NOT for intra-passage insertions between two landmarks. Revise assumption #2 to reflect this, or add an analysis of how many landmark pairs survive intra-passage insertion (hint: only pairs where both landmarks fall entirely before or after the insertion point).\",\n        \"Address the IDF computation problem: TF-IDF requires IDF statistics from a reference corpus. In streaming dedup over a web crawl, you don't have this. Propose either (a) using a pre-built IDF table from a fixed reference corpus, (b) using character-n-gram hash local maxima as a corpus-free landmark alternative, or (c) bounding the experiment to the batch-dedup setting where IDF can be computed first.\"\n      ]\n    },\n    {\n      \"dimension\": \"presentation\",\n      \"score\": 3,\n      \"justification\": \"The hypothesis is clearly written, well-organized, and provides good term definitions. The Shazam analogy is explained at exactly the right level of detail. Minor clarity issues exist around the saliency surface definition (it would be an enormous sparse matrix) and how 'local maxima' in a 2D space of position×n-gram are practically computed.\",\n      \"improvements\": [\n        \"Replace 'saliency surface as a 2D matrix indexed by (position, n-gram-id)' with a more practical description: compute TF-IDF for each (position, k-gram) pair in a sliding window, then find positions where the local k-gram score exceeds all neighbors within ±L positions. The 2D matrix framing implies O(|vocab|×|doc|) space which is impractical.\",\n        \"Clarify whether 'position' means character offset or word/token index — this matters for the offset delta and for cross-document comparison when documents have different tokenizations.\"\n      ]\n    },\n    {\n      \"dimension\": \"contribution\",\n      \"score\": 3,\n      \"justification\": \"If the experiments confirm the hypothesis, the contribution is meaningful for the LLM pretraining dedup community where structural duplicates from article syndication are a known problem. The training-free, purely symbolic method contrasts well with RETSim-style neural approaches. However, the contribution magnitude depends critically on whether a trivially stronger baseline (passage-bounded MinHash) is included and whether it can also solve the problem cheaply.\",\n      \"improvements\": [\n        \"Add passage-bounded MinHash as a baseline: this method simply computes MinHash over the detected 'core' passage (using the candidate landmark region) rather than the full document. If this trivially closes the gap with the new method, it significantly weakens the contribution. Include it to avoid a reviewer objection that will certainly arise.\",\n        \"Quantify the expected speedup or storage advantage over neural alternatives (RETSim, embedding-based dedup) at web scale — this positions the contribution more concretely for the LLM pretraining audience.\"\n      ]\n    }\n  ],\n  \"critiques\": [\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"The offset-preservation assumption (assumption #2) breaks for intra-passage insertions. The hypothesis claims the method handles 'insertion, deletion, or surrounding-text addition,' but for intra-passage insertions (a paragraph inserted in the middle of a passage), every landmark pair that straddles the insertion point will have a different offset in the modified passage. Only pairs where both landmarks fall before or after the insertion point are preserved. This is a critical failure mode for one of the three advertised edit types, and it means the method may not outperform MinHash on intra-passage insertion benchmarks.\",\n      \"suggested_action\": \"Add a formal analysis of what fraction of landmark pairs survive each edit type. For surrounding-text addition (prepend/append): 100% of pairs preserved. For deletion of a suffix/prefix: pairs within the retained region preserved. For intra-passage insertion: only pairs where both landmarks are on the same side of the insertion point survive. Based on this, either (a) restrict the claimed edit types to extra-passage edits where the method is clearly correct, or (b) propose a tolerance mechanism (allow offset match within ±δ, analogous to Shazam's frequency bin tolerance) and add this to the method description.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"Missing strong baseline: passage-bounded MinHash. The natural response to 'MinHash degrades when a passage is embedded in a larger document' is to detect or estimate the passage boundaries first and apply MinHash only to the core passage. This is a known practical workaround. If passage-bounded MinHash achieves comparable recall gains, the landmark-pair method's contribution is marginal. The absence of this baseline is likely to be the first objection from reviewers.\",\n      \"suggested_action\": \"Add passage-bounded MinHash as an explicit baseline in the benchmark. One concrete implementation: (1) run Winnowing to find the densest landmark region, (2) crop the document to that region, (3) apply standard MinHash to the cropped passage. This isolates whether the landmark-pair offset mechanism is necessary beyond simple passage cropping.\"\n    },\n    {\n      \"category\": \"methodology\",\n      \"severity\": \"major\",\n      \"description\": \"TF-IDF landmark extraction has a corpus-level IDF dependency. Computing TF-IDF requires IDF statistics over a reference corpus. For near-duplicate detection at web scale (the primary motivating use case), you are building the corpus incrementally — you cannot compute IDF before you have all documents. This creates either a circularity (use IDF from the dedup target corpus itself) or a distribution mismatch (use IDF from a separate reference corpus). Neither is addressed.\",\n      \"suggested_action\": \"Either (a) restrict the evaluation to the batch-dedup setting where IDF is precomputed over a fixed corpus snapshot, and explicitly state this is not an online/streaming method; or (b) propose a corpus-free landmark selector such as local n-gram frequency within the document itself (self-IDF), or entropy-based local maxima, or character n-gram hash collisions. Compare both landmark selectors in the ablation.\"\n    },\n    {\n      \"category\": \"evidence\",\n      \"severity\": \"major\",\n      \"description\": \"PAN-PC-11 (2011) is not a good primary benchmark for the claimed use case. PAN-PC-11 targets academic plagiarism (copy, paraphrase, simulated paraphrase of Wikipedia articles) and does not include the web-crawl structural edits (article syndication, boilerplate addition) that motivate the hypothesis. Most modern systems already achieve near-saturating recall on the copy cases in PAN-PC-11, so the benchmark may not discriminate between methods on the proposed mechanism.\",\n      \"suggested_action\": \"Demote PAN-PC-11 to a secondary benchmark and make the synthetic Wikipedia corpus (with prepend/append/insert variants) the primary evaluation. Additionally, consider using the CC-News or Common Crawl dedup benchmarks if available, or the CORE near-duplicates dataset mentioned in recent dedup surveys, to validate on realistic web-crawl distributions.\"\n    },\n    {\n      \"category\": \"scope\",\n      \"severity\": \"minor\",\n      \"description\": \"The O(k²) fingerprint count per document is stated as a property but its dependence on document length is unspecified. If k (number of landmark local maxima) grows linearly with document length n, then fingerprint count is O(n²), which is much worse than MinHash's O(n). This could make the method impractical for long documents.\",\n      \"suggested_action\": \"Add an explicit analysis: either cap k (e.g., keep only the top-K highest-saliency landmarks, making k a constant), or show empirically that k grows sub-linearly with document length in typical corpora (e.g., because TF-IDF local maxima saturate). State the cap in the method description and include it in the runtime analysis.\"\n    },\n    {\n      \"category\": \"novelty\",\n      \"severity\": \"minor\",\n      \"description\": \"The hypothesis does not cite the 'term-pair indexing' literature in IR (e.g., Bernstein & Zobel 2004's work on feature-based copy detection, or Hoad & Zobel 2003 on 'Methods for Identifying Versioned and Plagiarised Documents'). These methods select salient terms and index their co-occurrence for copy detection, which is structurally adjacent to the proposed method. The differentiation from this work should be made explicit.\",\n      \"suggested_action\": \"Search for and cite Hoad & Zobel 2003 (JASIST, 'Methods for identifying versioned and plagiarised documents') and related feature-based copy detection work. Explicitly state how the proposed method differs: the positional OFFSET delta between landmark pairs (not just co-occurrence) is the novel ingredient, and the local-maximum selection via TF-IDF saliency is the text analog of spectral peak selection.\"\n    },\n    {\n      \"category\": \"clarity\",\n      \"severity\": \"minor\",\n      \"description\": \"The lookahead window W interacts with the offset-preservation property in a non-obvious way. A large W captures more pairs but also captures pairs with large offsets that are more likely to be disrupted by intra-passage insertions. A small W is more robust to intra-passage edits but may miss pairs across paragraph boundaries.\",\n      \"suggested_action\": \"Add a brief analysis of how W should be set relative to expected insertion size. Specifically, note that W should be smaller than the typical insertion block size to maintain offset preservation, and include W as an explicit ablation dimension in the experiment (not just varying k).\"\n    }\n  ],\n  \"score\": 5,\n  \"confidence\": 4,\n  \"relation_type\": null,\n  \"relation_rationale\": \"\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [20] ASSISTANT · 2026-07-03 17:48:06 UTC

```
Review written and saved. Here's the summary:

**Score: 5/10 (Borderline Accept)** | Confidence: 4

The Shazam-to-text analogy is genuinely novel — no prior work appears to apply (anchor, target, delta) landmark-pair hashing to text dedup. The motivation is technically grounded. However, three **major issues** need fixing before experiments run:

1. **Offset-preservation breaks for intra-passage insertions** — one of the three advertised edit types. When text is inserted between two landmarks, all downstream offsets shift. The method only provably works for extra-passage edits (prepend/append). Either restrict the claim or add an offset-tolerance mechanism (±δ, like Shazam's frequency bin tolerance).

2. **Missing strong baseline: passage-bounded MinHash** — the natural fix to MinHash's length-sensitivity is to crop the document to the detected landmark region first, then apply standard MinHash. If this achieves the same recall gains, the contribution is marginal. This baseline must be included.

3. **TF-IDF requires corpus-level IDF** — unavailable in streaming/online dedup scenarios (the primary use case). Either restrict to batch-dedup or propose a corpus-free landmark selector (self-IDF, entropy-based local maxima, or character n-gram hash collisions).

Minor issues: O(k²) fingerprint count unbounded if k grows with document length; PAN-PC-11 is a weak primary benchmark for the claimed structural-edit use case; Hoad & Zobel 2003 term-pair copy detection work should be cited to sharpen the novelty claim.
```
