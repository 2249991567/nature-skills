# Compliance Check Report

Rules sourced exclusively from `nature-polishing/` (SKILL.md, writing-strategy.md, section-moves.md, phrasebank-playbook.md, style-guardrails.md).

## Summary statistics

- Total issues flagged: **111**
- Sentences overall: 429
- Mean words / sentence: 17.3 (target 15–25; hard max 30)
- Sentences > 30 words: 37
- Sections present: Abstract, Introduction, Methods, Discussion, Conclusion
- Sections missing: Results

### Issues by category

- `integrity`: 1
- `length`: 99
- `structure`: 2
- `style`: 8
- `tense`: 1

## Sentence-length checks

- **[WARNING][GREEN]** Abstract: Sentence 1 has 24 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Automatic assessment of open-ended mathematical responses must handle intermediate reasoning, handwritten or scanned inputs, evidence traceability, and controlled feedback rather than only final-answer equivalence.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Abstract: Sentence 3 has 24 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The adaptation layer converts handwritten, scanned, or already structured responses into parsed steps, formula sequences, layout anchors, final-answer regions, confidence values, and low-quality flags.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Abstract: Sentence 5 has 22 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: SAGE then performs step-behavior parsing, graph-vector retrieval, Neo4j–ChromaDB Node_ID binding, local evidence-subgraph construction, reference-student trace alignment, and Evidence Gate validation.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Abstract: Sentence 6 has 29 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Only graph-resolved textbook nodes inside the local evidence subgraph can be cited as evidence_nodes; diagnostic states such as unsupported methods, low-confidence input, and final-answer conflicts are routed separately.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Abstract: Sentence 8 has 45 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Compared with direct LLM grading, textbook-context grading, flat RAG, graph retrieval without gate validation, and SAGE without a fine-tuned generator, the full SAGE framework achieved the strongest point estimates fo...
  - Suggestion: Compared with direct LLM grading, textbook-context grading, flat RAG, graph retrieval without gate validation. SAGE without a fine-tuned generator, the full SAGE framework achieved the strongest point estimates for grading-state classification, OOD/unsupported-method detection, evidence grounding, retrieval quality, Node_ID binding, and format validity.
- **[WARNING][GREEN]** Abstract: Sentence 9 has 23 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The results indicate that evidence-constrained graph validation, rather than handwriting recognition or free-form LLM explanation alone, is central to traceable and controllable assessment.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Introduction: Sentence 2 has 22 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Student responses may appear as typed solutions, scanned answer sheets, or handwritten multi-line derivations containing formulas, diagrams, arrows, corrections, and natural-language explanations.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Introduction: Sentence 3 has 23 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Although OCR, handwritten mathematical expression recognition (HMER), and vision-language models can convert visual responses into machine-processable fields, recognition and grading are different problems.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Introduction: Sentence 4 has 37 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: A visually plausible transcription does not prove that the invoked rule belongs to the target textbook, that a non-standard solution path is permitted by the course evidence space, or that a low-confidence region shou...
  - Suggestion: A visually plausible transcription does not prove that the invoked rule belongs to the target textbook. A non-standard solution path is permitted by the course evidence space, or that a low-confidence region should be automatically graded.
- **[ERROR][GREEN]** Introduction: Sentence 7 has 45 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: This study therefore asks: after a handwritten, scanned, or already structured mathematical response has been converted into structured fields, how can a system diagnose step-level deviations while ensuring that gradi...
  - Suggestion: This study therefore asks: after a handwritten, scanned, or already structured mathematical response has been converted into structured fields, how can a system diagnose step-level deviations while ensuring that grading_state, credit_level, error_localization, missed_points, grading_explanation. Evidence_nodes are explicitly verifiable?
- **[WARNING][GREEN]** Introduction: Sentence 11 has 21 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Textbook evidence identity is confirmed only through graph-vector retrieval, Node_ID binding, local evidence-subgraph validation, trace alignment, and the Evidence Gate.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Introduction: Sentence 14 has 26 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The same requirements–ordered operations, rule invocation, intermediate-state checking, evidence-boundary control, and schema-valid diagnostic feedback–also arise in programming, algorithms, data structures, databases...
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Introduction: Sentence 17 has 29 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Handwritten or scanned mathematical responses are first converted into structured fields through an upstream AI-assisted input-adaptation layer, including handwriting recognition, formula parsing, layout anchors, conf...
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Introduction: Sentence 18 has 36 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: These fields are then processed by the SAGE evidence-constrained closed loop, where graph-vector retrieval, Node_ID binding, local evidence subgraph H construction, reference-student trace alignment, and Evidence Gate...
  - Suggestion: These fields are then processed by the SAGE evidence-constrained closed loop, where graph-vector retrieval, Node_ID binding, local evidence subgraph H construction, reference-student trace alignment. Evidence Gate validation restrict grading outputs to graph-valid textbook evidence.
- **[WARNING][GREEN]** Introduction: Sentence 22 has 26 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: SAGE builds a textbook evidence graph in which chapters, concepts, rules, formulas, examples, tables, visual descriptions, rubrics, and source anchors are represented as traceable evidence objects.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Introduction: Sentence 26 has 28 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: SAGE aligns reference and student step-behavior traces inside a local evidence subgraph  and separates graph-valid evidence_nodes from diagnostic nodes such as unsupported_method and final_answer_conflict.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Introduction: Sentence 28 has 27 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: SAGE constructs graph-anchored synthetic supervision data and uses supervised fine-tuning (SFT) to stabilize structured generation while retrieval, binding, alignment, and Evidence Gate validation remain external cons...
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Introduction: Sentence 29 has 25 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Related Work

Automatic short-answer grading has progressed from lexical matching to deep semantic representation and Transformer-based scoring (Burrows et al., 2015; Haller et al., 2022).
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Introduction: Sentence 30 has 37 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Mathematical constructed responses are harder because they involve symbolic expressions, formula invocation, transformations, boundary substitution, and partial reasoning (Erickson et al., 2020; Baral et al., 2021, 20...
  - Suggestion: Mathematical constructed responses are harder because they involve symbolic expressions, formula invocation, transformations, boundary substitution. Partial reasoning (Erickson et al., 2020; Baral et al., 2021, 2023; Morris et al., 2025; Chen & Wan, 2025; Bhandari & Pardos, 2025).
- **[ERROR][GREEN]** Introduction: Sentence 31 has 37 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: LLMs improve feedback fluency (Ouyang et al., 2022; Wei et al., 2022; Wang et al., 2023; Bai et al., 2022), but free-form LLM grading remains difficult to audit unless knowledge identity and evidence support are exter...
  - Suggestion: LLMs improve feedback fluency (Ouyang et al., 2022; Wei et al., 2022; Wang et al., 2023; Bai et al., 2022). Free-form LLM grading remains difficult to audit unless knowledge identity and evidence support are externally constrained.
- **[ERROR][GREEN]** Introduction: Sentence 33 has 59 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: CROHME-style HMER, image-to-markup models, syntax-aware networks, and recent VLM-based grading approaches show that visual mathematical work can be parsed into structured representations (Mouchere et al., 2016; Deng e...
  - Suggestion: CROHME-style HMER, image-to-markup models, syntax-aware networks, and recent VLM-based grading approaches show that visual mathematical work can be parsed into structured representations (Mouchere et al., 2016. Deng et al., 2017; Zhang et al., 2017, 2019; Mahdavi et al., 2019; Wang & Liu, 2021; Yuan et al., 2022; Bian et al., 2022; Xie et al., 2023; Nguyen et al., 2025).
- **[WARNING][GREEN]** Introduction: Sentence 34 has 25 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: SAGE does not propose a new OCR/HMER/VLM model; it evaluates evidence-constrained grading after such input adaptation has produced structured fields and quality signals.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Introduction: Sentence 35 has 44 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: RAG reduces hallucination by grounding generation in retrieved knowledge (Lewis et al., 2020; Karpukhin et al., 2020; Gao et al., 2023; Yu et al., 2024), while GraphRAG extends retrieval to graph-structured evidence (...
  - Suggestion: RAG reduces hallucination by grounding generation in retrieved knowledge (Lewis et al., 2020; Karpukhin et al., 2020; Gao et al., 2023. Yu et al., 2024), while GraphRAG extends retrieval to graph-structured evidence (Edge et al., 2024; Peng et al., 2024; Guo et al., 2024).
- **[ERROR][GREEN]** Introduction: Sentence 36 has 40 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Educational knowledge graphs organize concepts, resources, prerequisites, and learning paths (Ji et al., 2022; Hogan et al., 2021; Peng, Xia, et al., 2023; Qu et al., 2024; Abu-Salih & Alotaibi, 2024; Dang et al., 202...
  - Suggestion: Educational knowledge graphs organize concepts, resources, prerequisites, and learning paths (Ji et al., 2022; Hogan et al., 2021. Peng, Xia, et al., 2023; Qu et al., 2024; Abu-Salih & Alotaibi, 2024; Dang et al., 2021; Su & Zhang, 2020; Canal-Esteve & Gutierrez, 2024).
- **[WARNING][GREEN]** Introduction: Sentence 37 has 23 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: For mathematical grading, however, a graph is not merely a resource index; it defines the evidence boundary against which grading outputs are validated.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 3 has 22 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Let  denote the problem image or structured problem source,  the reference answer or rubric, and  the student handwritten or scanned response image.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 5 has 51 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Its output contains parsed text steps , formula sequences , layout anchors or bounding boxes , final-answer regions , recognition-confidence values , and low-quality or unreadable-region flags :

The structured SAGE i...
  - Suggestion: Its output contains parsed text steps , formula sequences , layout anchors or bounding boxes , final-answer regions , recognition-confidence values. Low-quality or unreadable-region flags :

The structured SAGE input is then

where  is the normalized problem,  is the reference trace, and  is the student trace derived from either structured input or the adaptation layer.
- **[WARNING][GREEN]** Methods: Sentence 9 has 29 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Handwritten or scanned mathematical responses are first converted into structured mathematical fields through an upstream input-adaptation layer, including handwriting recognition, formula parsing, layout anchors, con...
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 10 has 34 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The structured input is then processed by the SAGE evidence-constrained grading pipeline: step-behavior parsing, graph-vector retrieval, Node_ID binding, local evidence subgraph H construction, reference-student trace...
  - Suggestion: The structured input is then processed by the SAGE evidence-constrained grading pipeline: step-behavior parsing, graph-vector retrieval, Node_ID binding, local evidence subgraph H construction, reference-student trace alignment, Evidence Gate validation. Structured grading output.
- **[ERROR][GREEN]** Methods: Sentence 11 has 55 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Input-adaptation results are not treated as graph-valid evidence unless they are resolved to valid textbook nodes through Node_ID binding and included within H.

3.2 Textbook Evidence Graph Schema and Node_ID Binding
...
  - Suggestion: Input-adaptation results are not treated as graph-valid evidence unless they are resolved to valid textbook nodes through Node_ID binding and included within H.

3.2 Textbook Evidence Graph Schema and Node_ID Binding

The textbook evidence graph is defined as

where  is the node set,  is the relation set. Is the attribute set.
- **[WARNING][GREEN]** Methods: Sentence 13 has 23 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Each citable object must have a stable Node_ID, source provenance, and enough attributes to support traceback, local-subgraph construction, and Evidence Gate validation.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 19 has 42 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: A retrieved chunk can support a grading output only if it is resolved to a valid Neo4j Node_ID, belongs to the target textbook scope, is relevant to the current problem and reference path, and is included in the local...
  - Suggestion: A retrieved chunk can support a grading output only if it is resolved to a valid Neo4j Node_ID, belongs to the target textbook scope, is relevant to the current problem and reference path. Is included in the local evidence subgraph .
- **[WARNING][GREEN]** Methods: Sentence 22 has 28 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: This figure illustrates how textbook text, formulas, tables, figures, and spatial anchors are represented as graph-resolved evidence objects and connected to ChromaDB vector chunks through Node_ID metadata.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 25 has 27 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: A chunk can be cited as graph-valid evidence only after it is resolved to a valid Neo4j Node_ID and included in the local evidence subgraph H.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 26 has 29 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Therefore, only graph-validated nodes inside H can appear in evidence_nodes.

3.3 Step-Behavior Parsing, Retrieval, and Binding Score

SAGE parses reference and student responses into ordered step-behavior units.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 27 has 28 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: For step ,

where  is the step identifier,  is the step text,  is the mathematical expression,  is the action type,  is the behavior description, and  is the retrieval query.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 30 has 37 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: For each step , SAGE retrieves candidate chunks and binds the best graph-valid node by

where  is the candidate set,  is embedding similarity,  is formula-structure consistency, and  is contextual agreement with the p...
  - Suggestion: For each step , SAGE retrieves candidate chunks and binds the best graph-valid node by

where  is the candidate set,  is embedding similarity,  is formula-structure consistency. Is contextual agreement with the problem, reference trace, and textbook scope.
- **[WARNING][GREEN]** Methods: Sentence 33 has 26 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: No fixed universal acceptance threshold is applied across all cases; the best candidate must also pass Neo4j existence, textbook-scope, source-anchor, relevance, and Evidence Gate supportability checks.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 34 has 33 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The local evidence subgraph is constructed by joint graph-vector retrieval:

where  is the chunk collection.  contains valid concepts, formulas, rules, examples, rubrics, prerequisite relations, and source anchors tha...
  - Suggestion: The local evidence subgraph is constructed by joint graph-vector retrieval:

where  is the chunk collection.  contains valid concepts, formulas, rules, examples, rubrics, prerequisite relations. Source anchors that can support the current instance.
- **[WARNING][GREEN]** Methods: Sentence 35 has 30 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Diagnostic states are stored separately and are not inserted into the valid evidence set.

3.4 Trace Alignment and Evidence Gate

Let  be the reference trace and  the student trace.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 37 has 36 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The pairwise matching score is

where  measures behavior similarity,  measures Node_ID agreement or graph-distance similarity,  measures evidence-path consistency inside , and  penalizes unsupported methods, missing s...
  - Suggestion: The pairwise matching score is

where  measures behavior similarity,  measures Node_ID agreement or graph-distance similarity,  measures evidence-path consistency inside. Penalizes unsupported methods, missing steps, final-answer conflicts, unreadable or low-confidence steps, and severe order violations.
- **[WARNING][GREEN]** Methods: Sentence 44 has 28 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Input: structured instance x=(q,a_R,a_S,x_a), textbook graph G_T, chunk store C
Output: structured grading output y and routing decision g
1.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 53 has 24 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The Evidence Gate validates the structured output  rather than re-grading the response:

Here,  denotes the cited evidence nodes and  the valid node set inside .
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 55 has 23 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: If a student uses an alternative valid method, SAGE accepts it only when that method can be represented by nodes and paths inside .
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 56 has 41 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: For example, if a reference solution evaluates  by an antiderivative but a student correctly uses the area of a triangle, the solution can be aligned through an alternative_to or equivalent_to path if the geometric ar...
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[WARNING][GREEN]** Methods: Sentence 62 has 22 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Matched, partially_matched, missing, unsupported_method, and final_answer_conflict states are used to derive error_localization, missed_points, and grading_explanation.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 63 has 25 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Graph-valid evidence_nodes must be resolved textbook nodes inside H, whereas diagnostic_nodes remain outside the valid evidence set and are used only for diagnosis.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 64 has 43 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The Evidence Gate validates evidence boundary, Node_ID validity, step consistency, OOD/insufficient-evidence routing, input-quality routing, and schema validity before accepting or routing the structured grading outpu...
  - Suggestion: The Evidence Gate validates evidence boundary, Node_ID validity, step consistency, OOD/insufficient-evidence routing, input-quality routing. Schema validity before accepting or routing the structured grading output.

3.5 Graph-Anchored Supervision and SFT

A SAGE training instance is not an ordinary question-answer pair.
- **[WARNING][GREEN]** Methods: Sentence 65 has 27 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: It contains a seed problem, reference trace, controlled student trace, optional input-adaptation metadata, Node_ID binding, local evidence subgraph , alignment labels , teacher target , and Evidence Gate result.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 66 has 22 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Controlled perturbations cover missing steps, incorrect formula invocation, calculation inconsistencies, unsupported methods, final-answer conflicts, equivalent expressions, near-domain OOD cases, and insufficient-inp...
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 67 has 24 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: FERMAT-style corrupted-reasoning patterns are used only as error-pattern inspiration and are not used as textbook evidence labels, gold grading labels, or formal evaluation samples.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 68 has 28 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The SFT objective is

where  denotes Clean SFT Data after Node_ID binding, Evidence Gate filtering, schema checking, diagnostic-node exclusion, duplicate removal, input-quality routing checks, and leakage control.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 69 has 24 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: SFT trains the generator to produce schema-compliant structured outputs; retrieval, Node_ID binding, handwriting recognition, alignment, and Evidence Gate validation remain external verifiable constraints.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 72 has 38 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: This figure summarizes how textbook-aligned seed problems are converted into reference-student trace pairs, optionally augmented with input-adaptation metadata, bound to graph-resolved textbook evidence through graph-...
  - Suggestion: This figure summarizes how textbook-aligned seed problems are converted into reference-student trace pairs, optionally augmented with input-adaptation metadata, bound to graph-resolved textbook evidence through graph-vector retrieval and Node_ID binding. Organized under the local evidence boundary H.
- **[WARNING][GREEN]** Methods: Sentence 74 has 25 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Candidate samples are filtered by Evidence Gate validation, schema checking, diagnostic-node exclusion, duplicate removal, input-quality routing checks, and leakage control before entering Clean SFT Data.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 78 has 31 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Experiments

4.1 Experimental Protocol and Compared Methods

The experiments evaluate SAGE after mathematical responses have been converted into structured input through either existing structured sources or upstream ...
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[WARNING][GREEN]** Methods: Sentence 81 has 30 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The finalized benchmark contains 6,500 AI-assisted graph-anchored samples: 5,000 Clean SFT samples, 500 validation samples, 500 Main Test samples, 300 Hard Test samples, and 200 OOD/Unsupported samples.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 84 has 25 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Each evaluation sample is checked for split separation by seed problem, normalized formula signature, reference trace, controlled student trace, target label, and bound evidence-node set.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 89 has 26 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Compared methods.

4.2 Evaluation Metrics

State accuracy is defined as

Knowledge-node precision, recall, and F1 compare the predicted node set  with the author-audited node set .
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 90 has 24 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Step-alignment precision, recall, and F1 compare predicted alignment relations with verified relations over matched, partially_matched, missing, unsupported_method, and final_answer_conflict states.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 91 has 37 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: To avoid the empty-set problem in evidence grounding, EGR is computed only over gradable cases  for which a supported evidence-citing decision is expected:

Thus, an output with empty evidence_nodes cannot receive EGR...
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[WARNING][GREEN]** Methods: Sentence 96 has 22 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Direct LLM, Textbook Context LLM, and Flat RAG cannot obtain strict EGR because their outputs are not resolved to valid Node_IDs.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Methods: Sentence 99 has 29 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: These results should be interpreted under the stated synthetic and author-audited protocol rather than as classroom deployment validation or handwriting-recognition validation.

4.4 Retrieval, Binding, and Ablation

T...
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Methods: Sentence 107 has 49 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The relatively high OOD-F1 without the final Gate suggests that retrieval and generation can detect some unsupported cases, but boundary validation and schema supportability remain less stable.

4.5 Case Study and Err...
  - Suggestion: The relatively high OOD-F1 without the final Gate suggests that retrieval and generation can detect some unsupported cases. Boundary validation and schema supportability remain less stable.

4.5 Case Study and Error Analysis

The case study illustrates how SAGE localizes reasoning deviations rather than simply displaying an interface.
- **[ERROR][GREEN]** Methods: Sentence 108 has 32 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: A representative definite-integral case shows that the student recognizes the integral, skips the required antiderivative transformation, applies an unsupported average-value shortcut, and reports a final answer that ...
  - Suggestion: A representative definite-integral case shows that the student recognizes the integral, skips the required antiderivative transformation, applies an unsupported average-value shortcut. Reports a final answer that conflicts with the reference result.
- **[ERROR][GREEN]** Methods: Sentence 109 has 34 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: SAGE decomposes the response into step behaviors, confirms graph-valid textbook nodes through retrieval and binding, aligns the student trace with the reference trace, and separates partial match, missing step, unsupp...
  - Suggestion: SAGE decomposes the response into step behaviors, confirms graph-valid textbook nodes through retrieval and binding, aligns the student trace with the reference trace. Separates partial match, missing step, unsupported reasoning, and final-answer conflict.
- **[ERROR][GREEN]** Methods: Sentence 112 has 34 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The figure presents a definite-integral case in which the reference solution uses an antiderivative path, whereas the student response skips the required transformation, applies an unsupported average-value shortcut, ...
  - Suggestion: The figure presents a definite-integral case in which the reference solution uses an antiderivative path. The student response skips the required transformation, applies an unsupported average-value shortcut, and produces a conflicting final answer.
- **[WARNING][GREEN]** Methods: Sentence 113 has 28 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Graph-valid evidence_nodes are kept inside the local evidence subgraph H, while diagnostic_nodes such as missing_transformation, unsupported_shortcut, and final_answer_conflict remain outside evidence_nodes.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Discussion: Sentence 2 has 29 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Its graph-anchored validation principle can be adapted to domains where responses involve ordered operations, rule invocation, intermediate states, and local errors, including introductory programming, algorithms, dat...
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Discussion: Sentence 5 has 27 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The design allows controlled testing of missing steps, unsupported methods, final-answer conflicts, and evidence-boundary violations, but future work should include real student-answer collections and independent mult...
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Discussion: Sentence 6 has 22 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Second, the input-adaptation layer makes SAGE compatible with handwritten and scanned responses, but this paper does not independently evaluate handwriting recognition quality.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Discussion: Sentence 10 has 27 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Fifth, the reported results are single-setting point estimates; bootstrap confidence intervals, paired significance tests, repeated-run standard deviations, and external handwriting-recognition metrics should be added...
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 3 has 22 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Instead, it constrains grading through step-behavior parsing, graph-vector retrieval, Node_ID binding, local evidence-subgraph construction, dynamic-programming trace alignment, and Evidence Gate validation.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 4 has 28 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Experiments on a 6,500-sample author-audited controlled benchmark show stronger point estimates than direct LLM grading, textbook-context grading, flat RAG, graph retrieval without gate validation, and ablated variants.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Conclusion: Sentence 5 has 37 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The central implication is that trustworthy AI-assisted assessment should be evaluated not only by fluent feedback or answer agreement, but also by evidence traceability, boundary-aware rejection, schema validity, and...
  - Suggestion: The central implication is that trustworthy AI-assisted assessment should be evaluated not only by fluent feedback or answer agreement. Also by evidence traceability, boundary-aware rejection, schema validity, and consistency between diagnosed steps and cited instructional evidence.
- **[WARNING][GREEN]** Conclusion: Sentence 9 has 26 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: This research was supported by the Science and Technology Project of the Department of Housing and Urban-Rural Development of Liaoning Province under Subproject No. LNSJSKJ-2026-030.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Conclusion: Sentence 18 has 33 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Generative AI and AI-assisted tools were used for language and grammar editing, generation and refinement of manuscript figures and graphical elements, and construction of AI-assisted synthetic supervision samples as ...
  - Suggestion: Generative AI and AI-assisted tools were used for language and grammar editing, generation and refinement of manuscript figures and graphical elements. Construction of AI-assisted synthetic supervision samples as described in the manuscript.
- **[ERROR][GREEN]** Conclusion: Sentence 27 has 54 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Heliyon, 10(3), Article e25383. https://doi.org/10.1016/j.heliyon.2024.e25383

Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N., Drain, D., Fort, S., Ganguli, D., Henighan, T., Joseph, N., Kadavath,...
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[WARNING][GREEN]** Conclusion: Sentence 29 has 25 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Training a helpful and harmless assistant with reinforcement learning from human feedback. arXiv. https://doi.org/10.48550/arXiv.2204.05862

Baral, S., Botelho, A.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 73 has 24 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Journal of Computer Science and Technology, 36(5), 1200-1211. https://doi.org/10.1007/s11390-020-0328-2

Deng, Y., Kanervisto, A., Ling, J., & Rush, A.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 98 has 23 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: LightRAG: Simple and fast retrieval-augmented generation. arXiv. https://doi.org/10.48550/arXiv.2410.05779

Haller, S., Aldea, A., Seifert, C., & Strisciuglio, N.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Conclusion: Sentence 100 has 42 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Survey on automated short answer grading with deep learning: From word embeddings to transformers. arXiv. https://doi.org/10.48550/arXiv.2204.03503

Hogan, A., Blomqvist, E., Cochez, M., D’Amato, C., de Melo, G., Guti...
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[ERROR][GREEN]** Conclusion: Sentence 114 has 37 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: IEEE Transactions on Neural Networks and Learning Systems, 33(2), 494-514. https://doi.org/10.1109/TNNLS.2021.3070843

Karpukhin, V., Oğuz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., & Yih, W.-T.
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[ERROR][GREEN]** Conclusion: Sentence 123 has 37 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Springer. https://doi.org/10.1007/978-3-031-19815-1_29

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-T., Rocktäschel, T., Riedel, S., & Kiela, D.
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[ERROR][GREEN]** Conclusion: Sentence 147 has 40 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, ...
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[ERROR][GREEN]** Conclusion: Sentence 149 has 34 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Training language models to follow instructions with human feedback. arXiv. https://doi.org/10.48550/arXiv.2203.02155

Peng, B., Zhu, Y., Liu, Y., Bo, X., Shi, H., Hong, C., Zhang, Y., & Tang, S.
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[ERROR][GREEN]** Conclusion: Sentence 180 has 32 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: International Journal on Document Analysis and Recognition, 24, 63-75. https://doi.org/10.1007/s10032-020-00360-2

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q.
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[ERROR][GREEN]** Conclusion: Sentence 202 has 31 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: IEEE Transactions on Multimedia, 21(1), 221-233. https://doi.org/10.1109/TMM.2018.2844689

Zhang, J., Du, J., Zhang, S., Liu, D., Hu, Y., Hu, J., Wei, S., & Dai, L.
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[WARNING][GREEN]** Conclusion: Sentence 206 has 22 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Supplementary Implementation Details

This appendix provides implementation details that are useful for reproduction but are not required to understand the main argument.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 208 has 24 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: A.1 Notation and Structured Input Fields

Let  denote the normalized problem statement,  the reference trace,  the student trace, and  the optional input-adaptation metadata.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 216 has 23 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The exact serialization can be JSON or a schema-equivalent dictionary, but the Evidence Gate checks the field names, value types, and evidence boundary.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Conclusion: Sentence 217 has 73 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The manuscript uses the following canonical field set.

{
  "grading_state": "MATCHED | PARTIAL | INCORRECT | OOD | REVIEW",
  "credit_level": "FULL | PARTIAL | LOW | NONE | REVIEW",
  "error_localization": ["step-lev...
  - Suggestion: Split into two sentences at the main clause boundary (one subject–verb proposition each; SKILL.md).
- **[WARNING][GREEN]** Conclusion: Sentence 218 has 25 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: A diagnostic node may explain why an answer is unsupported or why review is required, but it must not be counted as graph-valid textbook evidence.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 223 has 27 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Input: textbook graph G_T, chunk store C, seed problem set Q, perturbation set Ω
Output: Clean SFT Data D_clean and evaluation candidate pools D_eval
1.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 236 has 26 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The main perturbation operators include missing key steps, formula-substitution errors, calculation inconsistencies, unsupported-method substitution, final-answer conflicts, equivalent but non-standard expressions, ne...
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 241 has 21 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The figure shows raw input sources, adaptation outputs, structured SAGE fields, and input-quality routing; these fields are inputs, not graph-valid evidence.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 247 has 26 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: The Gate checks Node_ID validity, evidence boundary, diagnostic-node separation, input quality, schema validity, and alignment consistency before routing outputs to PASS, REPAIR, REVIEW, or REJECT.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[WARNING][GREEN]** Conclusion: Sentence 251 has 25 words and may contain more than one main proposition.
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: During inference, unresolved chunks, low-confidence bindings, out-of-scope nodes, and diagnostic states are routed to review or rejection rather than being coerced into evidence_nodes.
  - Suggestion: Prefer one core subject–verb proposition per sentence.
- **[ERROR][GREEN]** Conclusion: Sentence 255 has 1266 words (limit 30).
  - Rule: SKILL.md § Sentence rules — every sentence <= 30 words
  - Sentence: Area | Existing foundation | Remaining limitation | Positioning of SAGE

Mathematical grading | Open-response scoring and process-oriented feedback | Fluent explanations may lack verifiable textbook evidence | Restric...
  - Suggestion: Area | Existing foundation | Remaining limitation | Positioning of SAGE

Mathematical grading | Open-response scoring and process-oriented feedback | Fluent explanations may lack verifiable textbook evidence | Restricts grading through graph evidence, trace alignment, and Evidence Gate

Handwritten/VLM input | OCR, HMER, formula parsing, spatial localization | Structured visual fields do not guarantee graph-valid evidence | Uses input adaptation only as structured input and routing signal

RAG and GraphRAG | External knowledge retrieval and graph-structured evidence | Flat passages do not ensure valid Node_IDs or local boundaries | Maps chunks to standardized graph nodes and validates them inside

Educational knowledge graphs | Concepts, resources, prerequisites, learning paths | Usually not designed for step-level grading validation | Treats the textbook graph as a constrained evidence space

SFT data | LLMs learn structured formats from supervision | Ordinary QA data lack evidence nodes and alignment labels | Builds graph-anchored supervision with Evidence Gate filtering

Component | Typical elements | Key attributes or relations | Role in grading

Node types | Chapter, Section, Concept, Definition, Theorem, Rule, Formula, Example, Rubric, Table, Figure, SpatialAnchor | node_id, book_id, section_id, page_id, evidence_type, formula_latex, source_text, bbox | Provides standardized evidence objects

Edge types | contains, has_concept, invokes_rule, has_formula, exemplified_by, prerequisite_of, located_at, equivalent_to, alternative_to, supports_step | directed typed relation, source and target Node_IDs | Supports evidence paths and alternative solution paths

Source anchors | page number, bounding box, formula block, table cell, figure description | page_id, bbox, anchor_type, source_hash | Makes evidence traceable to textbook objects

Vector chunks | text chunks, formula chunks, figure/table descriptions | primary_node_id, linked_node_ids, node_ids, book_key, page_id | Supplies retrieval candidates, not final evidence

Diagnostic nodes | unsupported_method, final_answer_conflict, low_confidence_input, insufficient_evidence | diagnostic tag and routing reason | Explains errors but cannot appear in evidence_nodes

Split | N | Use | Purpose | Filtering requirement

Clean SFT Data | 5,000 | Training only | Train structured-output generation | Node_ID binding, Gate validation, schema checks, duplicate removal, leakage control

Validation Set | 500 | Tuning only | Tune prompts, retrieval, weights, Gate settings, and schema repair | Separated from all test subsets and Clean SFT Data

Main Test Set | 500 | Test only | Main grading evaluation | Author-audited; no shared seed, trace, formula signature, target, or reference node set with SFT

Hard Test Set | 300 | Test only | Missing, unsupported, calculation. Final-answer conflict cases | Author-audited challenging subset

OOD / Unsupported Test Set | 200 | Test only | Evidence-boundary rejection and unsupported-method evaluation | Diagnostic nodes cannot appear in evidence_nodes

Method | Generator/backbone | Retrieval | Node_ID binding | Trace alignment | Evidence Gate

Direct LLM | Qwen3.5-9B | No | No | No | No

Textbook Context LLM | Qwen3.5-9B | Provided textbook context | No | No | No

Flat RAG | Qwen3.5-9B RAG | Flat vector retrieval | No | No | No

Graph Retrieval w/o Gate | SAGE retrieval backbone | Graph-vector retrieval | Yes | Partial | No

SAGE w/o SFT | General LLM generator | Yes | Yes | Yes | Yes

SAGE Full | SFT-trained SAGE generator | Yes | Yes | Yes | Yes

Method | Main Acc | Main F1 | Hard Acc | Hard F1 | OOD F1 | EGR | FVR

Direct LLM | 0.620 | 0.533 | 0.552 | 0.491 | 0.000 | 0.000 | 0.842

Textbook Context | 0.806 | 0.788 | 0.732 | 0.701 | 0.588 | 0.000 | 0.904

Flat RAG | 0.812 | 0.801 | 0.755 | 0.718 | 0.621 | 0.000 | 0.917

Graph Retrieval w/o Gate | 0.866 | 0.846 | 0.808 | 0.782 | 0.742 | 0.883 | 0.936

SAGE w/o SFT | 0.889 | 0.872 | 0.861 | 0.842 | 0.874 | 0.912 | 0.961

SAGE Full | 0.922 | 0.908 | 0.908 | 0.899 | 0.920 | 0.964 | 0.989

Method | Hit@1 | Hit@3 | Hit@5 | MRR | Binding Rate

Direct LLM | - | - | - | - | 0.000

Textbook Context LLM | - | - | - | - | 0.000

Flat RAG | 0.611 | 0.742 | 0.806 | 0.694 | 0.000

Graph Retrieval w/o Gate | 0.802 | 0.901 | 0.944 | 0.857 | 0.930

SAGE w/o SFT | 0.824 | 0.923 | 0.958 | 0.881 | 0.950

SAGE Full | 0.846 | 0.940 | 0.970 | 0.902 | 0.964

Setting | State Acc | State F1 | OOD F1 | EGR | FVR | Align F1

SAGE Full | 0.9083 | 0.8992 | 0.9195 | 0.9125 | 0.983 | 0.8720

w/o SFT | 0.8610 | 0.8420 | 0.8740 | 0.9120 | 0.961 | 0.8460

w/o trace alignment | 0.8170 | 0.7810 | 0.7420 | 0.9010 | 0.958 | 0.0000

w/o Node_ID binding | 0.7670 | 0.6470 | 0.5120 | 0.0000 | 0.947 | 0.6470

w/o local subgraph | 0.8080 | 0.7420 | 0.7940 | 0.8500 | 0.961 | 0.7420

w/o Evidence Gate | 0.8420 | 0.8610 | 0.9040 | 0.8750 | 0.891 | 0.8610

w/o schema validation | 0.8560 | 0.8680 | 0.9060 | 0.9050 | 0.826 | 0.8680

Error category | Representative symptom | SAGE response | Remaining risk

Missing transformation | Student skips the antiderivative transformation | Marks missing and localizes the missed reference step | Implicit valid shortcuts require alternative-path evidence

Unsupported method | Student applies an unsupported shortcut | Routes to unsupported_method without adding it to evidence_nodes | Some non-standard valid methods need expanded graph coverage

Calculation inconsistency | Correct method but arithmetic or boundary error | Separates method evidence from local conflict | Long algebra chains need finer segmentation

Final-answer conflict | Intermediate trace partly aligns but final value differs | Marks final_answer_conflict and cites reference final evidence | Equivalent final forms require normalization

OOD / insufficient evidence | Method or input falls outside available evidence | Routes to OOD, REVIEW, or REJECT | Deployment needs stronger input-quality detection

Schema error | Output misses fields or mixes diagnostic/evidence nodes | Repairs format-level errors or rejects output | Complex JSON outputs should be compact

Symbol or field | Meaning | Used as evidence?

normalized problem statement | No

reference step-behavior trace | No, but used for evidence retrieval

student step-behavior trace | No, but used for alignment

input-adaptation metadata | No

local evidence subgraph | Defines valid evidence boundary

alignment output produced by the external alignment module | No, but constrains diagnosis

teacher structured target in SFT | Training target only

evidence_nodes | graph-resolved textbook nodes cited by output | Yes, only if inside

diagnostic_nodes | unsupported, conflict, unreadable, or routing states | No

Action type | Description | Typical evidence relation

formula_invocation | invokes a named formula, theorem, or rule | invokes_rule, has_formula

integral_transformation | converts a limit, sum, or expression into an integral form | supports_step, equivalent_to

limit_operation | evaluates or transforms a limiting process | invokes_rule

boundary_evaluation | substitutes bounds or endpoint values | supports_step

calculation | performs arithmetic or algebraic simplification | local consistency check

final_answer | states the final result | evidence plus trace consistency

unreadable_region | marks low-quality or uncertain input | diagnostic/routing only

unsupported_method | uses a method outside the evidence boundary | diagnostic/routing only

extra | provides additional but not necessary reasoning | accepted only if graph-supported

OOD | outside the textbook or task evidence space | routing only

Prompt role | Input | Required output | Guardrail

Step parsing | problem, response, formulas, confidence | ordered step-behavior units | no final grading

Retrieval query construction | step behavior and formula expression | retrieval query and formula signature | no invented Node_ID

Alignment drafting | reference trace, student trace, bound nodes | candidate alignment labels | checked by dynamic programming and Gate

Structured grading | , , | schema-compliant | evidence only from

Evidence Gate validation | , , , schema | PASS/REPAIR/REVIEW/REJECT | diagnostic nodes excluded from evidence

Leakage key | Rule

Seed problem identifier | no shared seed across training and test

Normalized problem text | exact and near-duplicate problem text removed

Formula-structure signature | same symbolic skeleton excluded across splits

Reference trace | identical or near-identical reference paths excluded

Student trace | identical perturbation traces excluded

Target output | duplicate structured targets removed

Evidence-node set | cases with identical evidence-node set and trace pattern checked manually

Prompt leakage | no test labels, reference outputs, or evidence decisions included in prompt templates

## Tense & hedging checks

- **[ERROR][YELLOW]** Discussion: Sentence 8 uses absolute / unhedged interpretive language.
  - Rule: SKILL.md § Discussion + phrasebank-playbook.md hedging families
  - Sentence: Third, the textbook graph must be updated when course materials, textbook editions, or rubrics change.
  - Suggestion: Use moderate/speculative phrasing: suggest / may reflect / could indicate (phrasebank-playbook.md).

## Style & register checks

- **[ERROR][YELLOW]** Introduction: Overclaim language matched /\bprove[sd]?\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: A visually plausible transcription does not prove that the invoked rule belongs to the target textbook, that a non-standard solution path is permitted by the course evidence space, or that a low-confidence region shou...
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Introduction: Overclaim language matched /\bprove[sd]?\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: Flat retrieval-augmented generation (RAG) introduces textbook passages, but retrieved text alone does not prove graph-valid textbook evidence.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Methods: Overclaim language matched /\bprove[sd]?\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: A book_key, book_id, page_id, or source_text field records provenance but does not itself prove evidence validity.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Methods: Overclaim language matched /\bthe best\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: For each step , SAGE retrieves candidate chunks and binds the best graph-valid node by

where  is the candidate set,  is embedding similarity,  is formula-structure consistency, and  is contextual agreement with the p...
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Methods: Overclaim language matched /\bthe best\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: No fixed universal acceptance threshold is applied across all cases; the best candidate must also pass Neo4j existence, textbook-scope, source-anchor, relevance, and Evidence Gate supportability checks.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Methods: Overclaim language matched /\bmust be\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: Graph-valid evidence_nodes must be resolved textbook nodes inside H, whereas diagnostic_nodes remain outside the valid evidence set and are used only for diagnosis.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[ERROR][YELLOW]** Discussion: Overclaim language matched /\bmust be\b/.
  - Rule: style-guardrails.md § Overclaim checklist
  - Sentence: Third, the textbook graph must be updated when course materials, textbook editions, or rubrics change.
  - Suggestion: Soften: show / suggest / to our knowledge / among the strongest / in this cohort.
- **[WARNING][GREEN]** Conclusion: Rhetorical question in polished manuscript prose.
  - Rule: style-guardrails.md § Academic register
  - Sentence: Can language models grade algebra worked solutions?
  - Suggestion: Avoid rhetorical questions (style-guardrails.md).

## Hourglass & section-structure checks

- **[WARNING][YELLOW]** Results: Section 'Results' is missing or empty.
  - Rule: section-moves.md — section questions and move order
  - Suggestion: Ensure Results fulfils its rhetorical questions (section-moves.md).
- **[INFO][YELLOW]** Abstract: Abstract may be incomplete as a mini-paper (missing signals: gap/objective, implication).
  - Rule: section-moves.md — section questions and move order
  - Suggestion: Pattern: context/problem → gap → approach → key results → implication.

## Integrity / risk reminders

- **[INFO][RED]** ALL: Red-line reminder: do not invent references, data, mechanisms, or rewrite the paper's core scientific argument.
  - Rule: SKILL.md § AI traffic-light + style-guardrails.md Integrity rules
  - Suggestion: AI may polish wording only; authors own the core argument.

## Risk summary

- **Green** items are mechanical language fixes; still verify terminology.
- **Yellow** items change claim strength or section logic; require author review.
- **Red** items mark forbidden AI actions (fabrication / core-argument authorship).
