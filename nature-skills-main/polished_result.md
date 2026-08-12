# Polished Manuscript (Nature-polishing rules)

> Key automated edits are marked with HTML `<u>underline</u>`.
> Logic-first principle: structural issues are flagged in Revision Notes and the Compliance Report; wording edits never invent data or citations.

---

Title Page

SAGE: Step-Aligned Graph Evidence for Evidence-Constrained Assessment of Mathematical Responses after AI-Assisted Input Adaptation

Yang Wenquan¹, Lu Haiyan¹,*

¹ Shenyang University of Technology, Shenyang, China
*Corresponding author: Lu Haiyan
ORCID: Yang Wenquan, https://orcid.org/0009-0007-5852-3970

Funding. This research was supported by the Science and Technology Project of the Department of Housing and Urban-Rural Development of Liaoning Province under Subproject No. LNSJSKJ-2026-030.

Conflict of interest. The authors declare no competing interests.

Ethics approval and consent. This manuscript does not report primary research involving human participants or identifiable personal data; ethics approval was not required.

Data, materials, and code availability. The graph schemas, synthetic-sample protocol, and implementation records are available from the corresponding author upon reasonable request. Public release of textbook-derived materials may be subject to copyright restrictions.

Generative AI disclosure. Generative AI and AI-assisted tools were used for language and grammar editing, generation and refinement of manuscript figures and graphical elements, and construction of AI-assisted synthetic supervision samples as described in the manuscript. The authors reviewed, verified, edited, and take full responsibility for all content, data, figures, analysis, and conclusions. AI tools are not credited as authors.

Author contributions. Yang Wenquan contributed to conceptualization, methodology, implementation, data curation, experiments, and original drafting. Lu Haiyan contributed to supervision, validation, manuscript review and editing, and correspondence.

SAGE: Step-Aligned Graph Evidence for Evidence-Constrained Assessment of Mathematical Responses after AI-Assisted Input Adaptation

## Abstract

Automatic assessment of open-ended mathematical responses must handle intermediate reasoning, handwritten or scanned inputs, evidence traceability, and controlled feedback rather than only final-answer equivalence. This study proposes SAGE (Step-Aligned Graph Evidence), an evidence-constrained framework for assessing mathematical responses after an upstream AI-assisted input-adaptation layer. The adaptation layer converts handwritten, scanned, or already structured responses into parsed steps, formula sequences, layout anchors, final-answer regions, confidence values, and low-quality flags. These fields are treated as structured inputs rather than grading evidence. SAGE then performs <u>step-behaviour</u> parsing, graph-vector retrieval, Neo4j–ChromaDB Node_ID binding, local evidence-subgraph construction, reference-student trace alignment, and Evidence Gate validation. Only graph-resolved textbook nodes inside the local evidence subgraph can be cited as evidence_nodes; diagnostic states such as unsupported methods, low-confidence input, and final-answer conflicts are routed separately. A 6,500-sample AI-assisted graph-anchored synthetic benchmark was constructed under textbook-evidence constraints. Compared with direct LLM grading, textbook-context grading, flat RAG, graph retrieval without gate <u>validation.</u> SAGE without a fine-tuned generator, the full SAGE framework achieved the strongest point estimates for grading-state classification, OOD/unsupported-method detection, evidence grounding, retrieval quality, Node_ID binding, and format validity. The results indicate that evidence-constrained graph validation, rather than handwriting recognition or free-form LLM explanation alone, is central to traceable and controllable assessment.

Keywords: informatics education; mathematical response assessment; evidence-constrained grading; step-level diagnosis; graph-vector retrieval; Node_ID binding; large language models

## Introduction

Open-ended mathematical grading is a process-oriented assessment task. Student responses may appear as typed solutions, scanned answer sheets, or handwritten multi-line derivations containing formulas, diagrams, arrows, corrections, and natural-language explanations. Although OCR, handwritten mathematical expression recognition (HMER), and vision-language models can convert visual responses into machine-processable fields, recognition and grading are different problems. A visually plausible transcription does not <u>suggest</u> that the invoked rule belongs to the target textbook, that a non-standard solution path is permitted by the course evidence space, or that a low-confidence region should be automatically graded.

Direct LLM-based grading can generate fluent explanations, but its knowledge labels, evidence references, and error localization are difficult to verify. Flat retrieval-augmented generation (RAG) introduces textbook passages, but retrieved text alone does not <u>suggest</u> graph-valid textbook evidence. This study therefore asks: after a handwritten, scanned, or already structured mathematical response has been converted into structured fields, how can a system diagnose step-level deviations while ensuring that grading_state, credit_level, error_localization, missed_points, grading_explanation, and evidence_nodes are explicitly verifiable?

SAGE addresses this problem by separating three roles: input adaptation, <u>step-behaviour</u> description, and textbook evidence identity. The input-adaptation layer may provide parsed text, formulas, layout anchors, confidence values, and low-quality flags. These outputs help construct a student trace, but they are not treated as graph-valid evidence. Textbook evidence identity is confirmed only through graph-vector retrieval, Node_ID binding, local evidence-subgraph validation, trace alignment, and the Evidence Gate.

The controlled benchmark in this study uses textbook-aligned calculus problems. Calculus is used as a controlled symbolic-reasoning test bed, not as a complete representation of all informatics education tasks. The same requirements–ordered operations, rule invocation, intermediate-state checking, evidence-boundary control, and schema-valid diagnostic feedback–also arise in programming, algorithms, data structures, databases, and computational-thinking assessment.

Figure 1. Motivation and overall idea of SAGE with AI-assisted input adaptation. Handwritten or scanned mathematical responses are first converted into structured fields through an upstream AI-assisted input-adaptation layer, including handwriting recognition, formula parsing, layout anchors, confidence estimation, and low-quality flagging. These fields are then processed by the SAGE evidence-constrained closed loop, where graph-vector retrieval, Node_ID binding, local evidence subgraph H construction, reference-student trace <u>alignment.</u> Evidence Gate validation restrict grading outputs to graph-valid textbook evidence. The lower branch summarizes graph-anchored synthetic supervision and SFT for structured-output stabilization.

The main contributions are as follows.

Textbook evidence graph and evidence-object schema. SAGE builds a textbook evidence graph in which chapters, concepts, rules, formulas, examples, tables, visual descriptions, rubrics, and source anchors are represented as traceable evidence objects.

Graph-vector retrieval with standardized Node_ID binding. SAGE connects ChromaDB vector chunks to Neo4j graph nodes through standardized Node_ID metadata, distinguishing semantically relevant text from graph-valid textbook evidence.

Step-aligned diagnosis under a local evidence boundary. SAGE aligns reference and student <u>step-behaviour</u> traces inside a local evidence subgraph and separates graph-valid evidence_nodes from diagnostic nodes such as unsupported_method and final_answer_conflict.

Graph-anchored supervision for structured-output stabilization. SAGE constructs graph-anchored synthetic supervision data and uses supervised fine-tuning (SFT) to stabilize structured generation while retrieval, binding, alignment, and Evidence Gate validation remain external constraints.

2. Related Work

Automatic short-answer grading has progressed from lexical matching to deep semantic representation and Transformer-based scoring (Burrows et al., 2015; Haller et al., 2022). Mathematical constructed responses are harder because they involve symbolic expressions, formula invocation, transformations, boundary <u>substitution.</u> <u>Partial</u> reasoning (Erickson et al., 2020; Baral et al., 2021, 2023; Morris et al., 2025; Chen & Wan, 2025; Bhandari & Pardos, 2025). LLMs improve feedback fluency (Ouyang et al., 2022; Wei et al., 2022; Wang et al., 2023; Bai et al., <u>2022).</u> <u>However,</u> free-form LLM grading remains difficult to audit unless knowledge identity and evidence support are externally constrained.

Handwritten mathematical input structuring provides the upstream tools needed to convert images into formulas, text, and layout information. CROHME-style HMER, image-to-markup models, syntax-aware networks, and recent VLM-based grading approaches show that visual mathematical work can be parsed into structured representations (Mouchere et al., <u>2016.</u> Deng et al., <u>2017.</u> Zhang et al., 2017, 2019; Mahdavi et al., 2019; Wang & Liu, 2021; Yuan et al., 2022; Bian et al., 2022; Xie et al., 2023; Nguyen et al., 2025). SAGE does not propose a new OCR/HMER/VLM model; it evaluates evidence-constrained grading after such input adaptation has produced structured fields and quality signals.

RAG reduces hallucination by grounding generation in retrieved knowledge (Lewis et al., <u>2020.</u> Karpukhin et al., 2020; Gao et al., 2023; Yu et al., <u>2024).</u> <u>Meanwhile,</u> <u>graphRAG</u> extends retrieval to graph-structured evidence (Edge et al., 2024; Peng et al., 2024; Guo et al., 2024). Educational knowledge graphs organize concepts, resources, prerequisites, and learning paths (Ji et al., <u>2022.</u> Hogan et al., 2021; Peng, Xia, et al., 2023; Qu et al., 2024; Abu-Salih & Alotaibi, 2024; Dang et al., 2021; Su & Zhang, 2020; Canal-Esteve & Gutierrez, 2024). For mathematical grading, however, a graph is not merely a resource index; it defines the evidence boundary against which grading outputs are validated.

Table 1. Positioning of SAGE relative to related research.

## Methods

3.1 Problem Definition after AI-Assisted Input Adaptation

SAGE operates after a mathematical response has been represented in structured form. In deployed settings, this structure may come from online homework systems, curated answer records, or an AI-assisted handwriting input-adaptation layer. Let denote the problem image or structured problem source, the reference answer or rubric, and the student handwritten or scanned response image. The adaptation stage is defined as

where is the AI-assisted input-adaptation operator. Its output contains parsed text <u>steps,</u> formula <u>sequences,</u> layout anchors or bounding <u>boxes,</u> final-answer <u>regions,</u> recognition-confidence <u>values,</u> and low-quality or unreadable-region <u>flags:</u>

The structured SAGE input is then

where is the normalized problem, is the reference trace, and is the student trace derived from either structured input or the adaptation layer. If key formulas, steps, final answers, or layout regions cannot be reliably parsed, SAGE routes the case to EVIDENCE_INSUFFICIENT or human review rather than forcing a grading decision.

Figure 2. Methodology pipeline of SAGE with AI-assisted input adaptation. Handwritten or scanned mathematical responses are first converted into structured mathematical fields through an upstream input-adaptation layer, including handwriting recognition, formula parsing, layout anchors, confidence estimation, and low-quality flagging. The structured input is then processed by the SAGE evidence-constrained grading pipeline: <u>step-behaviour</u> parsing, graph-vector retrieval, Node_ID binding, local evidence subgraph H construction, reference-student trace alignment, Evidence Gate validation, and structured grading output. Input-adaptation results are not treated as graph-valid evidence unless they are resolved to valid textbook nodes through Node_ID binding and included within H.

3.2 Textbook Evidence Graph Schema and Node_ID Binding

The textbook evidence graph is defined as

where is the node set, is the relation set, and is the attribute set. The graph schema is intentionally evidence-oriented. Each citable object must have a stable Node_ID, source provenance, and enough attributes to support traceback, local-subgraph construction, and Evidence Gate validation.

Table 2. Textbook evidence graph schema used by SAGE.

Neo4j <u>stores,</u> while ChromaDB stores retrievable text, formula, and multimodal-description chunks. The two stores are linked by Node_ID metadata. A book_key, book_id, page_id, or source_text field records provenance but does not itself <u>suggest</u> evidence validity. A retrieved chunk can support a grading output only if it is resolved to a valid Neo4j Node_ID, belongs to the target textbook scope, is relevant to the current <u>problem.</u> <u>Reference</u> path, and is included in the local evidence <u>subgraph.</u>

Figure 3. Multimodal textbook evidence graph and Node_ID binding. This figure illustrates how textbook text, formulas, tables, figures, and spatial anchors are represented as graph-resolved evidence objects and connected to ChromaDB vector chunks through Node_ID metadata. Vector retrieval provides candidate chunks, but chunk-level metadata such as book_key, page_id, or source_text only records provenance. Structured fields produced by input adaptation are retrieval and parsing inputs, not graph-valid evidence. A chunk can be cited as graph-valid evidence only after it is resolved to a valid Neo4j Node_ID and included in the local evidence subgraph H. Therefore, only graph-validated nodes inside H can appear in evidence_nodes.

3.3 <u>Step-Behaviour</u> Parsing, Retrieval, and Binding Score

SAGE parses reference and student responses into ordered <u>step-behaviour</u> units. For <u>step,</u>

where is the step identifier, is the step text, is the mathematical expression, is the action type, is the <u>behaviour</u> description, and is the retrieval query. Action types include formula_invocation, integral_transformation, limit_operation, boundary_evaluation, calculation, final_answer, unreadable_region, and unsupported_method. The action type describes what a step does; it is not a final textbook knowledge label.

For each <u>step,</u> SAGE retrieves candidate chunks and binds <u>among</u> the <u>strongest</u> graph-valid node by

where is the candidate set, is embedding similarity, is formula-structure consistency, and is contextual agreement with the problem, reference trace, and textbook scope. The weights are selected on the validation set rather than the test sets. In the reported implementation, the final validation setting <u>used,,</u> <u>and,</u> with retrieval top- and graph-neighborhood expansion <u>depth.</u> No fixed universal acceptance threshold is applied across all cases; <u>among</u> the <u>strongest</u> candidate must also pass Neo4j existence, textbook-scope, source-anchor, relevance, and Evidence Gate supportability checks.

The local evidence subgraph is constructed by joint graph-vector retrieval:

where is the chunk collection. contains valid concepts, formulas, rules, examples, rubrics, prerequisite relations, and source anchors that can support the current instance. Diagnostic states are stored separately and are not inserted into the valid evidence set.

3.4 Trace Alignment and Evidence Gate

Let be the reference trace and the student trace. SAGE aligns them by ordered dynamic programming rather than by unconstrained text similarity. The pairwise matching score is

where measures <u>behaviour</u> similarity, measures Node_ID agreement or graph-distance similarity, measures evidence-path consistency <u>inside.</u> <u>Penalizes</u> unsupported methods, missing steps, final-answer conflicts, unreadable or low-confidence steps, and severe order violations. The optimal alignment is

subject to step order, nullable skips, diagnostic labels, and local evidence-boundary constraints. During inference, is produced by this external alignment module. It is not a gold label and is not supplied by an oracle. The SFT generator conditions on the verified alignment output produced by the same pipeline used at inference time.

Algorithm 1. Evidence-constrained SAGE inference.

Input: structured instance x=(q,a_R,a_S,x_a), textbook graph G_T, chunk store C
Output: structured grading output y and routing decision g
1. Parse or receive ordered <u>step-behaviour</u> units for a_R and a_S.
2. Retrieve candidate chunks for each step and compute the binding score.
3. Resolve candidate chunks to Neo4j Node_IDs; reject unresolved or out-of-scope nodes.
4. Construct the local evidence subgraph H from valid bound nodes and d-hop expansion.
5. Align R and S by ordered dynamic programming to obtain A_star.
6. Draft y using the structured-output generator conditioned on x, H, and A_star.
7. Apply Evidence Gate checks: evidence boundary, Node_ID validity, diagnostic-node
 separation, alignment consistency, input-quality routing, and schema validity.
8. Return accepted y, repaired y, or a REVIEW/REJECT routing decision g.

The Evidence Gate validates the structured output rather than re-grading the response:

Here, denotes the cited evidence nodes and the valid node set <u>inside.</u> The Gate also requires diagnostic nodes to remain outside evidence_nodes. If a student uses an alternative valid method, SAGE accepts it only when that method can be represented by nodes and paths <u>inside.</u> For example, if a reference solution evaluates by an <u>antiderivative.</u> <u>However,</u> a student correctly uses the area of a triangle, the solution can be aligned through an alternative_to or equivalent_to path if the geometric area rule is present <u>in.</u> If the alternative path is not graph-supported, SAGE returns insufficient evidence or review instead of <u>labelling</u> the method as valid by model intuition alone.

Figure 4. Reference-student trace alignment and Evidence-Gated grading. This figure shows how SAGE aligns reference and student <u>step-behaviour</u> traces within the local evidence subgraph H. The student trace may be derived from AI-assisted handwriting adaptation; low-confidence or unreadable steps may trigger evidence-insufficient or human-review routing. Matched, partially_matched, missing, unsupported_method, and final_answer_conflict states are used to derive error_localization, missed_points, and grading_explanation. Graph-valid evidence_nodes must be resolved textbook nodes inside H, whereas diagnostic_nodes remain outside the valid evidence set and are used only for diagnosis. The Evidence Gate validates evidence boundary, Node_ID validity, step consistency, OOD/insufficient-evidence routing, input-quality routing, and schema validity before accepting or routing the structured grading output.

3.5 Graph-Anchored Supervision and SFT

A SAGE training instance is not an ordinary question-answer pair. It contains a seed problem, reference trace, controlled student trace, optional input-adaptation metadata, Node_ID binding, local evidence <u>subgraph,</u> alignment <u>labels,</u> teacher <u>target,</u> and Evidence Gate result. Controlled perturbations cover missing steps, incorrect formula invocation, calculation inconsistencies, unsupported methods, final-answer conflicts, equivalent expressions, near-domain OOD cases, and insufficient-input states. FERMAT-style corrupted-reasoning patterns are used only as error-pattern inspiration and are not used as textbook evidence labels, gold grading labels, or formal evaluation samples.

The SFT objective is

where denotes Clean SFT Data after Node_ID binding, Evidence Gate filtering, schema checking, diagnostic-node exclusion, duplicate removal, input-quality routing checks, and leakage control. SFT trains the generator to produce schema-compliant structured outputs; retrieval, Node_ID binding, handwriting recognition, alignment, and Evidence Gate validation remain external verifiable constraints.

Figure 5. Graph-anchored synthetic supervision data construction for SAGE. This figure summarizes how textbook-aligned seed problems are converted into reference-student trace pairs, optionally augmented with input-adaptation metadata, bound to graph-resolved textbook evidence through graph-vector <u>retrieval.</u> Node_ID binding, and organized under the local evidence boundary H. Alignment labels A* and structured targets y* are constructed under the constraint evidence_nodes ⊆ Id(H). Candidate samples are filtered by Evidence Gate validation, schema checking, diagnostic-node exclusion, duplicate removal, input-quality routing checks, and leakage control before entering Clean SFT Data. The workflow describes AI-assisted synthetic supervision construction under textbook-evidence constraints rather than manual classroom-data annotation or handwriting-recognition benchmarking.

Table 3. Dataset construction and split protocol.

4. Experiments

4.1 Experimental Protocol and Compared Methods

The experiments evaluate SAGE after mathematical responses have been converted into structured input through either existing structured sources or upstream AI-assisted input adaptation. They do not claim a new handwriting-recognition benchmark, OCR model, HMER model, VLM training pipeline, character/word error rate, or bounding-box mAP. Low-confidence adapted fields are handled through evidence-insufficient or human-review states.

The finalized benchmark contains 6,500 AI-assisted graph-anchored samples: 5,000 Clean SFT samples, 500 validation samples, 500 Main Test samples, 300 Hard Test samples, and 200 OOD/Unsupported samples. The validation set is used only for prompt, retrieval, weighting, and Gate-setting selection. The test subsets are not used for tuning. Each evaluation sample is checked for split separation by seed problem, normalized formula signature, reference trace, controlled student trace, target label, and bound evidence-node set.

All compared methods receive the same normalized problem, reference answer, and student-answer content after input adaptation. Retrieval-based baselines use the same textbook chunk collection. Only graph-based variants access Neo4j Node_ID binding and local-subgraph verification.

Table 4. Compared methods.

4.2 Evaluation Metrics

State accuracy is defined as

Knowledge-node precision, recall, and F1 compare the predicted node set with the author-audited node <u>set.</u> Step-alignment precision, recall, and F1 compare predicted alignment relations with verified relations over matched, partially_matched, missing, unsupported_method, and final_answer_conflict states.

To avoid the empty-set problem in evidence grounding, EGR is computed only over gradable cases for which a supported evidence-citing decision is expected:

Thus, an output with empty evidence_nodes cannot receive EGR credit for gradable cases. OOD, unsupported, or insufficient-evidence cases are evaluated by OOD-F1 and routing <u>behaviour</u> rather than by vacuous subset satisfaction. Format Validity Rate is

4.3 Main Results

Table 5. Overall grading performance on author-audited evaluation subsets.

SAGE Full achieves the strongest point estimates on the controlled benchmark. Direct LLM, Textbook Context LLM, and Flat RAG cannot obtain strict EGR because their outputs are not resolved to valid Node_IDs. Graph Retrieval without Gate improves evidence grounding but is less stable for unsupported methods, input-quality routing, and schema validity. SAGE without SFT benefits from the full evidence pipeline but is less stable than the SFT-trained generator. These results should be interpreted under the stated synthetic and author-audited protocol rather than as classroom deployment validation or handwriting-recognition validation.

4.4 Retrieval, Binding, and Ablation

Table 6. Retrieval and Node_ID binding performance.

Table 7. Ablation results on the Hard Test Set.

The ablation results support the contribution of each external constraint. Removing trace alignment eliminates explicit alignment relations even though coarse state prediction remains possible. Removing Node_ID binding reduces EGR to zero, confirming that retrieved text cannot substitute for graph-resolved evidence. Removing the local subgraph weakens boundary control, while removing the Evidence Gate reduces both supportability and format validity. The relatively high OOD-F1 without the final Gate suggests that retrieval and generation can detect some unsupported cases, but boundary validation and schema supportability remain less stable.

4.5 Case Study and Error Analysis

The case study illustrates how SAGE localizes reasoning deviations rather than simply displaying an interface. A representative definite-integral case shows that the student recognizes the integral, skips the required antiderivative transformation, applies an unsupported average-value <u>shortcut.</u> <u>Reports</u> a final answer that conflicts with the reference result. SAGE decomposes the response into step <u>behaviours,</u> confirms graph-valid textbook nodes through <u>retrieval.</u> <u>Binding,</u> aligns the student trace with the reference trace, and separates partial match, missing step, unsupported reasoning, and final-answer conflict.

Figure 6. Case study of evidence-gated step-level diagnosis. The figure presents a definite-integral case in which the reference solution uses an antiderivative <u>path.</u> <u>By</u> <u>contrast,</u> the student response skips the required transformation, applies an unsupported average-value shortcut, and produces a conflicting final answer. Graph-valid evidence_nodes are kept inside the local evidence subgraph H, while diagnostic_nodes such as missing_transformation, unsupported_shortcut, and final_answer_conflict remain outside evidence_nodes.

Table 8. Error analysis summary.

## Discussion

SAGE provides a reproducible pattern for constraining AI-assisted assessment with externally verifiable textbook evidence. Its graph-anchored validation principle can be adapted to domains where responses involve ordered operations, rule invocation, intermediate states, and local errors, including introductory programming, algorithms, databases, and computational thinking.

The study has limitations. First, the benchmark is AI-assisted, synthetic, and author-audited rather than independently collected classroom deployment data. The design allows controlled testing of missing steps, unsupported methods, final-answer conflicts, and evidence-boundary violations, but future work should include real student-answer collections and independent multi-annotator validation. Second, the input-adaptation layer makes SAGE compatible with handwritten and scanned responses, but this paper does not independently evaluate handwriting recognition quality. OCR, HMER, formula parsing, VLM-based layout interpretation, and confidence calibration may affect downstream parsing, retrieval, alignment, and routing. Third, the textbook graph must be updated when course materials, textbook editions, or rubrics change. Fourth, complex open reasoning with multiple valid solution paths may require richer local evidence subgraphs and stronger alternative-path validation. Fifth, the reported results are single-setting point estimates; bootstrap confidence intervals, paired significance tests, repeated-run standard deviations, and external handwriting-recognition metrics should be added in future work.

## Conclusion

This study presents SAGE, a step-aligned graph-evidence framework for evidence-constrained grading of mathematical responses after AI-assisted input adaptation. SAGE does not treat <u>recognised</u> handwriting fields or free-form LLM explanations as sufficient grading evidence. Instead, it constrains grading through <u>step-behaviour</u> parsing, graph-vector retrieval, Node_ID binding, local evidence-subgraph construction, dynamic-programming trace alignment, and Evidence Gate validation. Experiments on a 6,500-sample author-audited controlled benchmark show stronger point estimates than direct LLM grading, textbook-context grading, flat RAG, graph retrieval without gate validation, and ablated variants. The central implication is that trustworthy AI-assisted assessment should be evaluated not only by fluent feedback or answer <u>agreement.</u> <u>However,</u> also by evidence traceability, boundary-aware rejection, schema validity, and consistency between diagnosed steps and cited instructional evidence.

Declarations

Acknowledgements. No additional acknowledgements are reported.

Funding. This research was supported by the Science and Technology Project of the Department of Housing and Urban-Rural Development of Liaoning Province under Subproject No. LNSJSKJ-2026-030.

Conflicts of Interest. The authors declare no competing interests.

Ethics Approval and Consent. This manuscript does not report primary research involving human participants or identifiable personal data; ethics approval was not required.

Data, Materials, and Code Availability. The graph schemas, synthetic-sample protocol, and implementation records are available from the corresponding author upon reasonable request. Public release of textbook-derived materials may be subject to copyright restrictions.

Generative AI Disclosure. Generative <u>AI.</u> AI-assisted tools were used for language and grammar editing, generation and refinement of manuscript figures and graphical elements, and construction of AI-assisted synthetic supervision samples as described in the manuscript. The authors reviewed, verified, edited, and take full responsibility for all content, data, figures, analysis, and conclusions. AI tools are not credited as authors.

Author Contributions. Yang Wenquan contributed to conceptualization, methodology, implementation, data curation, experiments, and original drafting. Lu Haiyan contributed to supervision, validation, manuscript review and editing, and correspondence.

References

Abu-Salih, B., & Alotaibi, S. (2024). A systematic literature review of knowledge graph construction and application in education. Heliyon, 10(3), Article e25383. https://doi.org/10.1016/j.heliyon.2024.e25383

Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., DasSarma, N., Drain, D., Fort, S., Ganguli, D., Henighan, T., Joseph, N., Kadavath, S., Kernion, J., Conerly, T., El-Showk, S., Elhage, N., Hatfield-Dodds, Z., Hernandez, D., Hume, T., … Kaplan, J. (2022). Training a helpful and harmless assistant with reinforcement learning from human feedback. arXiv. https://doi.org/10.48550/arXiv.2204.05862

Baral, S., Botelho, A. F., Erickson, J. A., Benachamardi, P., & Heffernan, N. T. (2021). Improving automated scoring of student open responses in mathematics. In Proceedings of the 14th International Conference on Educational Data Mining (pp. 130-138). International Educational Data Mining Society.

Baral, S., Botelho, A. F., Santhanam, A., Gurung, A., Cheng, L., & Heffernan, N. T. (2023). Auto-scoring student responses with images in mathematics. In Proceedings of the 16th International Conference on Educational Data Mining (pp. 362-369). https://doi.org/10.5281/zenodo.8115645

Bhandari, S., & Pardos, Z. A. (2025). Can language models grade algebra worked solutions? Evaluating LLM-based autograders against human grading. In Proceedings of the 18th International Conference on Educational Data Mining (pp. 554-558). International Educational Data Mining Society.

Bian, X., Qin, B., Xin, X., Li, J., Su, X., & Wang, Y. (2022). Handwritten mathematical expression recognition via attention aggregation based bi-directional mutual learning. In Proceedings of the AAAI Conference on Artificial Intelligence, 36(1), 113-121. https://doi.org/10.1609/aaai.v36i1.19885

Blecher, L., Cucurull, G., Scialom, T., & Stojnic, R. (2023). Nougat: Neural optical understanding for academic documents. arXiv. https://doi.org/10.48550/arXiv.2308.13418

Burrows, S., Gurevych, I., & Stein, B. (2015). The eras and trends of automatic short answer grading. International Journal of Artificial Intelligence in Education, 25, 60-117. https://doi.org/10.1007/s40593-014-0026-8

Canal-Esteve, M., & Gutiérrez, Y. (2024). Educational material to knowledge graph conversion: A methodology to enhance digital education. In Proceedings of the 1st Workshop on Knowledge Graphs and Large Language Models (pp. 85-91). Association for Computational Linguistics. https://doi.org/10.18653/v1/2024.kallm-1.9

Chen, Z., & Wan, T. (2025). Grading explanations of problem-solving process and generating feedback using large language models at human-level accuracy. Physical Review Physics Education Research, 21(1), Article 010126. https://doi.org/10.1103/PhysRevPhysEducRes.21.010126

Condor, A., Litster, M., & Pardos, Z. A. (2021). Automatic short answer grading with SBERT on out-of-sample questions. In Proceedings of the 14th International Conference on Educational Data Mining (pp. 345-352). International Educational Data Mining Society.

Dang, F.-R., Tang, J.-T., Pang, K.-Y., Wang, T., Li, S.-S., & Li, X. (2021). Constructing an educational knowledge graph with concepts linked to Wikipedia. Journal of Computer Science and Technology, 36(5), 1200-1211. https://doi.org/10.1007/s11390-020-0328-2

Deng, Y., Kanervisto, A., Ling, J., & Rush, A. M. (2017). Image-to-markup generation with coarse-to-fine attention. In Proceedings of the 34th International Conference on Machine Learning (pp. 980-989). PMLR.

Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., Metropolitansky, D., Ness, R. O., & Larson, J. (2024). From local to global: A GraphRAG approach to query-focused summarization. arXiv. https://doi.org/10.48550/arXiv.2404.16130

Erickson, J. A., Botelho, A. F., McAteer, S., Varatharaj, A., & Heffernan, N. T. (2020). The automated grading of student open responses in mathematics. In Proceedings of the 10th International Conference on Learning Analytics and Knowledge (pp. 615-624). ACM. https://doi.org/10.1145/3375462.3375523

Es, S., James, J., Espinosa-Anke, L., & Schockaert, S. (2024). RAGAs: Automated evaluation of retrieval augmented generation. In Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations (pp. 150-158). Association for Computational Linguistics.

Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., Wang, M., & Wang, H. (2023). Retrieval-augmented generation for large language models: A survey. arXiv. https://doi.org/10.48550/arXiv.2312.10997

Guo, Z., Xia, L., Yu, Y., Ao, T., & Huang, C. (2024). LightRAG: Simple and fast retrieval-augmented generation. arXiv. https://doi.org/10.48550/arXiv.2410.05779

Haller, S., Aldea, A., Seifert, C., & Strisciuglio, N. (2022). Survey on automated short answer grading with deep learning: From word embeddings to transformers. arXiv. https://doi.org/10.48550/arXiv.2204.03503

Hogan, A., Blomqvist, E., Cochez, M., D’Amato, C., de Melo, G., Gutierrez, C., Kirrane, S., Labra Gayo, J. E., Navigli, R., Neumaier, S., Ngonga Ngomo, A.-C. N., Polleres, A., Rashid, S. M., Rula, A., Schmelzeisen, L., Sequeda, J., Staab, S., & Zimmermann, A. (2021). Knowledge graphs. ACM Computing Surveys, 54(4), Article 71. https://doi.org/10.1145/3447772

Huang, Y., Lv, T., Cui, L., Lu, Y., & Wei, F. (2022). LayoutLMv3: Pre-training for document AI with unified text and image masking. In Proceedings of the 30th ACM International Conference on Multimedia (pp. 4083-4091). ACM. https://doi.org/10.1145/3503161.3548112

Ji, S., Pan, S., Cambria, E., Marttinen, P., & Yu, P. S. (2022). A survey on knowledge graphs: Representation, acquisition, and applications. IEEE Transactions on Neural Networks and Learning Systems, 33(2), 494-514. https://doi.org/10.1109/TNNLS.2021.3070843

Karpukhin, V., Oğuz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., & Yih, W.-T. (2020). Dense passage retrieval for open-domain question answering. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (pp. 6769-6781). Association for Computational Linguistics.

Kim, G., Hong, T., Yim, M., Nam, J., Park, J., Yim, J., Hwang, W., Yun, S., Han, D., & Park, S. (2022). OCR-free document understanding transformer. In Computer Vision - ECCV 2022 (pp. 498-517). Springer. https://doi.org/10.1007/978-3-031-19815-1_29

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W.-T., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. In Advances in Neural Information Processing Systems, 33, 9459-9474.

Mahdavi, M., Zanibbi, R., Mouchère, H., Viard-Gaudin, C., & Garain, U. (2019). ICDAR 2019 CROHME + TFD: Competition on recognition of handwritten mathematical expressions and typeset formula detection. In Proceedings of the International Conference on Document Analysis and Recognition (pp. 1533-1538). IEEE.

Morris, W., Holmes, L., Choi, J. S., & Crossley, S. (2025). Automated scoring of constructed response items in math assessment using large language models. International Journal of Artificial Intelligence in Education, 35(2), 559-586. https://doi.org/10.1007/s40593-024-00418-w

Mouchère, H., Viard-Gaudin, C., Zanibbi, R., & Garain, U. (2016). ICFHR 2016 CROHME: Competition on recognition of online handwritten mathematical expressions. In Proceedings of the 15th International Conference on Frontiers in Handwriting Recognition (pp. 607-612). IEEE. https://doi.org/10.1109/ICFHR.2016.0116

Nguyen, T. P., Nguyen, D. M., Jeon, H., Lee, H., Song, H., Ko, S., & Kim, T. (2025). VEHME: A vision-language model for evaluating handwritten mathematics expressions. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (pp. 31793-31813). Association for Computational Linguistics.

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. arXiv. https://doi.org/10.48550/arXiv.2203.02155

Peng, B., Zhu, Y., Liu, Y., Bo, X., Shi, H., Hong, C., Zhang, Y., & Tang, S. (2024). Graph retrieval-augmented generation: A survey. arXiv. https://doi.org/10.48550/arXiv.2408.08921

Peng, C., Xia, F., Naseriparsa, M., & Osborne, F. (2023). Knowledge graphs: Opportunities and challenges. Artificial Intelligence Review, 56, 13071-13102. https://doi.org/10.1007/s10462-023-10465-9

Qu, K., Li, K. C., Wong, B. T. M., Wu, M. M. F., & Liu, M. (2024). A survey of knowledge graph approaches and applications in education. Electronics, 13(13), Article 2537. https://doi.org/10.3390/electronics13132537

Su, Y., & Zhang, Y. (2020). Automatic construction of subject knowledge graph based on educational big data. In Proceedings of the 3rd International Conference on Big Data and Education (pp. 30-36). ACM. https://doi.org/10.1145/3396452.3396458

Tornqvist, M., Mahamud, M., Mendez Guzman, E., & Farazouli, A. (2023). ExASAG: Explainable framework for automatic short answer grading. In Proceedings of the 18th Workshop on Innovative Use of NLP for Building Educational Applications (pp. 361-371). Association for Computational Linguistics.

Wang, X., Wei, J., Schuurmans, D., Le, Q. V., Chi, E., Narang, S., Chowdhery, A., & Zhou, D. (2023). Self-consistency improves chain-of-thought reasoning in language models. In Proceedings of the 11th International Conference on Learning Representations.

Wang, Z., & Liu, J. C.-S. (2021). Translating math formula images to LaTeX sequences using deep neural networks with sequence-level training. International Journal on Document Analysis and Recognition, 24, 63-75. https://doi.org/10.1007/s10032-020-00360-2

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q. V., & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. In Advances in Neural Information Processing Systems, 35, 24824-24837.

Xie, Y., Mouchère, H., Simistira Liwicki, F., Rakesh, S., Saini, R., Nakagawa, M., Nguyen, C. T., & Truong, T. N. (2023). ICDAR 2023 CROHME: Competition on recognition of handwritten mathematical expressions. In Document Analysis and Recognition - ICDAR 2023 (pp. 553-565). Springer.

Yu, H., Gan, A., Zhang, K., Tong, S., Liu, Q., & Liu, Z. (2024). Evaluation of retrieval-augmented generation: A survey. arXiv. https://doi.org/10.48550/arXiv.2405.07437

Yuan, Y., Liu, X., Dikubab, W., Liu, H., Ji, Z., Wu, Z., & Bai, X. (2022). Syntax-aware network for handwritten mathematical expression recognition. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4543-4552). IEEE.

Zhang, J., Du, J., & Dai, L. (2019). Track, attend, and parse (TAP): An end-to-end framework for online handwritten mathematical expression recognition. IEEE Transactions on Multimedia, 21(1), 221-233. https://doi.org/10.1109/TMM.2018.2844689

Zhang, J., Du, J., Zhang, S., Liu, D., Hu, Y., Hu, J., Wei, S., & Dai, L. (2017). Watch, attend and parse: An end-to-end neural network based approach to handwritten mathematical expression recognition. Pattern Recognition, 71, 196-206. https://doi.org/10.1016/j.patcog.2017.06.017

Appendix A. Supplementary Implementation Details

This appendix provides implementation details that are useful for reproduction but are not required to understand the main argument. The appendix also indicates which supplementary figures can be redrawn after the main text has been finalized.

A.1 Notation and Structured Input Fields

Let denote the normalized problem statement, the reference trace, the student trace, and the optional input-adaptation metadata. The adaptation metadata may contain parsed text steps, formula sequences, layout anchors, final-answer regions, recognition confidence values, and low-quality flags. In deployment, may be obtained from handwritten response parsing, online homework logs, or teacher-curated structured answers. SAGE treats these fields as input observations rather than textbook evidence.

A.2 <u>Step-Behaviour</u> Taxonomy

The taxonomy is intentionally operational rather than purely conceptual. A step label describes what the student or reference step does. It is later resolved to textbook evidence through retrieval and Node_ID binding.

A.3 Structured Output Schema

The generator produces a compact structured output. The exact serialization can be JSON or a schema-equivalent dictionary, but the Evidence Gate checks the field names, value types, and evidence boundary. The manuscript uses the following canonical field set.

{
 "grading_state": "MATCHED | PARTIAL | INCORRECT | OOD | REVIEW",
 "credit_level": "FULL | PARTIAL | LOW | NONE | REVIEW",
 "error_localization": ["step-level diagnostic tags"],
 "missed_points": ["reference steps or scoring points not satisfied"],
 "grading_explanation": "brief evidence-grounded explanation",
 "evidence_nodes": ["graph-valid textbook Node_IDs inside H"],
 "diagnostic_nodes": ["unsupported_method, final_answer_conflict, <u>low_confidence_input,..."],</u>
 "routing_decision": "ACCEPT | REPAIR | REVIEW | REJECT"
}

evidence_nodes and diagnostic_nodes are deliberately separated. A diagnostic node may explain why an answer is unsupported or why review is required, but it must not be counted as graph-valid textbook evidence.

A.4 Prompt Roles and Guardrails

SAGE uses prompts as controlled interfaces rather than as sources of evidence. The prompt roles are <u>summarised</u> below.

A.5 Algorithm for Synthetic Supervision Construction

Algorithm A.1. Graph-anchored synthetic supervision construction.

Input: textbook graph G_T, chunk store C, seed problem set Q, perturbation set Ω
Output: Clean SFT Data D_clean and evaluation candidate pools D_eval
1. Initialize D_clean and D_eval.
2. For each seed problem q in Q:
3. Construct or verify a textbook-aligned reference trace R.
4. Bind each reference step to graph-valid Node_IDs.
5. Generate a controlled student trace S using perturbation operators Ω.
6. Retrieve candidate chunks and resolve them to Neo4j Node_IDs.
7. Construct local evidence subgraph H by evidence-node expansion and filtering.
8. Align R and S to obtain A_star using the same alignment module used at inference.
9. Construct target y_star and separate evidence_nodes from diagnostic_nodes.
10. Apply Evidence Gate, schema checks, input-quality routing checks, and leakage control.
11. Assign the sample to training, validation, test, or review pools.
12. Return D_clean and D_eval.

The main perturbation operators include missing key steps, formula-substitution errors, calculation inconsistencies, unsupported-method substitution, final-answer conflicts, equivalent but non-standard expressions, near-domain OOD construction, and insufficient-input simulation.

A.6 Leakage-Control Rules

Leakage control removes overlapping or near-overlapping cases before final splits are locked. The following keys are checked jointly rather than independently.

A.7 Supplementary Figures

Supplementary Figure A1. Structured input fields after AI-assisted input adaptation. The figure shows raw input sources, adaptation outputs, structured SAGE fields, and input-quality routing; these fields are inputs, not graph-valid evidence.

Supplementary Figure A2. Detailed reference-student trace alignment. The figure separates antiderivative application from boundary evaluation and shows that diagnostic states remain outside evidence_nodes.

Supplementary Figure A3. Evidence Gate failure cases and routing decisions. The Gate checks Node_ID validity, evidence boundary, diagnostic-node separation, input quality, schema validity, and alignment consistency before routing outputs to PASS, REPAIR, REVIEW, or REJECT.

A.8 Implementation and Reproducibility Notes

The implementation stores textbook graph objects in Neo4j and vector chunks in ChromaDB. Chunk metadata includes primary_node_id, linked_node_ids, node_id, or node_ids when graph binding is available. Metadata fields such as book_key, page_id, and source_text record provenance but are not sufficient for evidence validity. During inference, unresolved chunks, low-confidence bindings, out-of-scope nodes, and diagnostic states are routed to review or rejection rather than being coerced into evidence_nodes.

The reported results use a validation-selected binding setting with retrieval top-, graph-neighborhood expansion <u>depth,</u> and weighting <u>coefficients,,</u> <u>and.</u> These values are implementation settings rather than universal constants. Future deployment should re-tune them on the target textbook, rubric, and task family.

Area | Existing foundation | Remaining limitation | Positioning of SAGE

Mathematical grading | Open-response scoring and process-oriented feedback | Fluent explanations may lack verifiable textbook evidence | Restricts grading through graph evidence, trace alignment, and Evidence Gate

Handwritten/VLM input | OCR, HMER, formula parsing, spatial localization | Structured visual fields do not guarantee graph-valid evidence | Uses input adaptation only as structured input and routing signal

RAG and GraphRAG | External knowledge retrieval and graph-structured evidence | Flat passages do not ensure valid Node_IDs or local boundaries | Maps chunks to standardized graph nodes and validates them inside

Educational knowledge graphs | Concepts, resources, prerequisites, learning paths | Usually not designed for step-level grading validation | Treats the textbook graph as a constrained evidence space

SFT data | LLMs learn structured formats from supervision | Ordinary QA data lack evidence nodes and alignment labels | Builds graph-anchored supervision with Evidence Gate filtering

Component | Typical elements | Key attributes or relations | Role in grading

Node types | Chapter, Section, Concept, Definition, Theorem, Rule, Formula, Example, Rubric, Table, Figure, SpatialAnchor | node_id, book_id, section_id, page_id, evidence_type, formula_latex, source_text, bbox | Provides standardized evidence objects

Edge types | contains, has_concept, invokes_rule, has_formula, exemplified_by, prerequisite_of, located_at, equivalent_to, alternative_to, supports_step | directed typed relation, <u>source.</u> <u>Target</u> Node_IDs | Supports evidence paths and alternative solution <u>paths.</u>

Source anchors | page number, bounding box, formula block, table cell, figure description | page_id, bbox, anchor_type, source_hash | Makes evidence traceable to textbook objects

Vector chunks | text chunks, formula chunks, figure/table descriptions | primary_node_id, linked_node_ids, node_ids, book_key, page_id | Supplies retrieval candidates, not final evidence

Diagnostic nodes | unsupported_method, final_answer_conflict, low_confidence_input, insufficient_evidence | diagnostic tag and routing reason | Explains errors but cannot appear in evidence_nodes

Split | N | Use | Purpose | Filtering requirement

Clean SFT Data | 5,000 | Training only | Train structured-output generation | Node_ID binding, Gate validation, schema checks, duplicate removal, leakage control

Validation Set | 500 | Tuning only | Tune prompts, retrieval, weights, Gate settings, and schema repair | Separated from all test subsets and Clean SFT Data

Main Test Set | 500 | Test only | Main grading evaluation | Author-audited; no shared seed, trace, formula signature, target, or reference node set with SFT

Hard Test Set | 300 | Test only | Missing, unsupported, calculation, and final-answer conflict cases | Author-audited challenging subset

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

reference <u>step-behaviour</u> trace | No, but used for evidence retrieval

student <u>step-behaviour</u> trace | No, but used for alignment

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

Step parsing | problem, response, formulas, confidence | ordered <u>step-behaviour</u> units | no final grading

Retrieval query construction | step <u>behaviour</u> and formula expression | retrieval query and formula signature | no invented Node_ID

Alignment drafting | reference trace, student trace, bound nodes | candidate alignment labels | checked by dynamic programming and Gate

Structured grading <u>|,,</u> | schema-compliant | evidence only from

Evidence Gate validation <u>|,,,</u> schema | PASS/REPAIR/REVIEW/REJECT | diagnostic nodes excluded from evidence

Leakage key | Rule

Seed problem identifier | no shared seed across training and test

Normalized problem text | exact and near-duplicate problem text removed

Formula-structure signature | same symbolic skeleton excluded across splits

Reference trace | identical or near-identical reference paths excluded

Student trace | identical perturbation traces excluded

Target output | duplicate structured targets removed

Evidence-node set | cases with identical evidence-node set and trace pattern checked manually

Prompt leakage | no test labels, reference outputs, or evidence decisions included in prompt templates
