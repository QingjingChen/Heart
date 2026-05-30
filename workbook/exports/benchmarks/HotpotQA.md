# HotpotQA (2018)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/pdf_texts_trust/13047.txt`

## Representative tool

Multi-hop supporting fact annotation with explicit evidence chaining and distractor injection

## Tool explanation (full)

HotpotQA constructs questions requiring reasoning across ≥2 Wikipedia paragraphs, mandating annotators to identify *all* supporting facts (numbered), label their logical role (bridge/entity linking), and include irrelevant distractor paragraphs. This enforces explicit multi-document traceability and exposes shallow pattern-matching or shortcut learning.  
— Lineage —  
• Paper: HotpotQA  
• Issue: Multi-hop reasoning with traceable evidence chains  
• Score: 5  
• Construct clarity: High — explicitly requires identification and labeling of supporting facts, logical roles, and distractors  
• Evidence grounding: Wikipedia-based; all claims anchored to specific, numbered paragraphs  
• Transparency: Full provenance via enumerated supporting facts (e.g., “Supporting facts: 1, 2, 4, 6, 7”) and role annotations  
• Robustness signal: Inclusion of irrelevant distractors tests resistance to spurious correlations

## What it improves vs. baseline

Advances beyond single-hop QA (e.g., SQuAD) by requiring *inter-document dependency resolution*: models must infer implicit connections (e.g., ‘Malfunkshun → Mother Love Bone → Andrew Wood’) — revealing brittleness in cross-source coherence and entity disambiguation.

## Adaptation example

In the financial compliance dialogue dataset, construction questions such as “Does a certain fund sales activity violate Article 23 of the Supervisory Measures for Sales Institutions of Publicly Offered Securities Investment Funds?” require the model to cite three heterogeneous document types: (1) the original regulatory text, (2) corresponding penalty cases, and (3) company disclosure announcements; and to annotate how each excerpt supports the legal conclusion—enforcing cross-institutional source reasoning.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: HotpotQA constructs questions requiring reasoning across ≥2 Wikipedia paragraphs, mandating annotators to identify *all* supporting facts (numbered), label their logical role (bridge/entity linking), and include irrelevant distractor paragraphs. This enforces explicit multi-document traceability and exposes shallow pattern-matching or shortcut learning.  
— Lineage —  
• HotpotQA has shortcut artifacts; reasoning chains may be spurious. — FEVER (2018) follow-ups  
— External perspective (Survey) —  
• FEVER requires models to determine whether claims are supported, refuted, or unverifiable and to retrieve supporting evidence, while HotpotQA introduces multi-hop question answering with sentence-level supporting facts. Although HotpotQA is not an ethics benchmark per se, it is highly relevant to this pillar because it operationalizes a crucial aspect of trustworthy reasoning. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Normative grounding**: —
- **Source provenance and evidence fitness**: HotpotQA constructs questions requiring reasoning across ≥2 Wikipedia paragraphs, mandating annotators to identify *all* supporting facts (numbered), label their logical role (bridge/entity linking), and include irrelevant distractor paragraphs. This enforces explicit multi-document traceability and exposes shallow pattern-matching or shortcut learning.  
— Lineage —  
• HotpotQA has shortcut artifacts; reasoning chains may be spurious. — FEVER (2018) follow-ups  
— External perspective (Survey) —  
• FEVER requires models to determine whether claims are supported, refuted, or unverifiable and to retrieve supporting evidence, while HotpotQA introduces multi-hop question answering with sentence-level supporting facts. Although HotpotQA is not an ethics benchmark per se, it is highly relevant to this pillar because it operationalizes a crucial aspect of trustworthy reasoning. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: Advances beyond single-hop QA (e.g., SQuAD) by requiring *inter-document dependency resolution*: models must infer implicit connections (e.g., ‘Malfunkshun → Mother Love Bone → Andrew Wood’) — revealing brittleness in cross-source coherence and entity disambiguation.  
— External perspective (Survey) —  
• FEVER requires models to determine whether claims are supported, refuted, or unverifiable and to retrieve supporting evidence, while HotpotQA introduces multi-hop question answering with sentence-level supporting facts. Although HotpotQA is not an ethics benchmark per se, it is highly relevant to this pillar because it operationalizes a crucial aspect of trustworthy reasoning. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: HotpotQA constructs questions requiring reasoning across ≥2 Wikipedia paragraphs, mandating annotators to identify *all* supporting facts (numbered), label their logical role (bridge/entity linking), and include irrelevant distractor paragraphs. This enforces explicit multi-document traceability and exposes shallow pattern-matching or shortcut learning.  
— Lineage —  
• HotpotQA has shortcut artifacts; reasoning chains may be spurious. — FEVER (2018) follow-ups
- **Robustness against gaming and contamination**: This enforces explicit multi-document traceability and exposes shallow pattern-matching or shortcut learning.  
— Lineage —  
• HotpotQA has shortcut artifacts; reasoning chains may be spurious. — FEVER (2018) follow-ups
- **Documentation and reproducibility**: HotpotQA constructs questions requiring reasoning across ≥2 Wikipedia paragraphs, mandating annotators to identify *all* supporting facts (numbered), label their logical role (bridge/entity linking), and include irrelevant distractor paragraphs. This enforces explicit multi-document traceability and exposes shallow pattern-matching or shortcut learning.  
— External Perspective (Survey) —  
• FEVER requires models to determine whether claims are supported, refuted, or unverifiable and to retrieve supporting evidence, while HotpotQA introduces multi-hop question answering with sentence-level supporting facts. Although HotpotQA is not an ethics benchmark per se, it is highly relevant to this pillar because it operationalizes a crucial aspect of trustworthy reasoning. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Maintenance and update governance**: —

## Lineage critiques

• HotpotQA is general QA; multi-hop reasoning ≠ trustworthy reasoning under uncertainty. — TrustLLM (2024)
• text-only; doesn't probe visual/cross-modal hallucination. — HallusionBench (2024)
• HotpotQA has shortcut artifacts; reasoning chains may be spurious. — FEVER (2018) follow-ups

## Self-acknowledged limits

Authors note Wikipedia bias; multi-hop questions sometimes solvable via single hop.

## External views (survey)

• FEVER requires models to determine whether claims are supported, refuted, or unverifiable and to retrieve supporting evidence, while HotpotQA introduces multi-hop question answering with sentence-level supporting facts. Although HotpotQA is not an ethics benchmark per se, it is highly relevant to this pillar because it operationalizes a crucial aspect of trustworthy reasoning. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The review notes that although HotpotQA is not an ethics benchmark, it operationalizes key aspects of trustworthy reasoning through multi-hop question answering and sentence-level supporting facts. Subsequent work criticizes it as a general QA benchmark: multi-hop reasoning does not equate to trustworthy reasoning under uncertainty; it is text-only and does not probe visual or cross-modal hallucinations; and it contains shortcut artifacts, leading to potentially spurious reasoning chains. The authors themselves acknowledge Wikipedia bias and note that some multi-hop questions can be solved via single-hop reasoning.
