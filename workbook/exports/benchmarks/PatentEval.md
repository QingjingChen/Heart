# PatentEval (2024)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/pdf_texts_trust/13497.txt`

## Representative tool

Domain-specific error typology for patent text generation

## Tool explanation (full)

PatentEval introduces a fine-grained, linguistically grounded error taxonomy tailored to patent documents, distinguishing 7 error types across two tasks: (1) claims-to-abstract generation (e.g., “missing technical effect”, “inconsistent antecedent basis”), and (2) next-claim generation (e.g., “scope creep beyond original disclosure”, “violation of unity of invention”). Each type is defined with explicit linguistic markers (e.g., pronoun resolution failure → “inconsistent antecedent basis”) and mapped to patent law requirements (e.g., Art. 83 EPC on sufficiency of disclosure). Annotations are performed by patent attorneys using dual-review protocol.

## What it improves vs. baseline

Replaces generic fluency or BLEU-based evaluation with domain-anchored, legally consequential error categories—enabling targeted debugging of ownership risk (e.g., overclaiming) and factual fidelity (e.g., unsupported technical effects), rather than treating all deviations as equal 'hallucinations'.

## Adaptation example

In financial compliance report generation tasks (e.g., SEC 10-K risk factor drafting), adapt the error typology to flag “material omission” (failure to disclose known litigation), “regulatory misalignment” (citing outdated CFR sections), and “forward-looking statement unqualification” (lacking Safe Harbor language), each annotated by SEC-experienced lawyers using the same dual-review protocol.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: PatentEval introduces a fine-grained, linguistically grounded error taxonomy tailored to patent documents, distinguishing 7 error types across two tasks: (1) claims-to-abstract generation (e.g., 'missing technical effect', 'inconsistent antecedent basis'), and (2) next-claim generation (e.g., 'scope creep beyond original disclosure', 'violation of unity of invention'). Each type is defined with explicit linguistic markers (e.g., pronoun resolution failure → 'inconsistent antecedent basis') and mapped to patent law requirements (e.g., Art. 83 EPC on sufficiency of disclosure).  
— Lineage —  
• "error taxonomy useful but doesn't cover full trustworthy spectrum." — Sycophancy / TrustLLM  
— External perspective (Survey) —  
• "PatentEval [Shen et al., 2024] further shows how trustworthiness and controllability can be examined in domains where factual precision, normative interpretation, and ownership risk intersect."
- **Normative grounding**: Each type is defined with explicit linguistic markers (e.g., pronoun resolution failure → 'inconsistent antecedent basis') and mapped to patent law requirements (e.g., Art. 83 EPC on sufficiency of disclosure).  
— External Perspective (Survey) —  
• “PatentEval [Shen et al., 2024] further shows how trustworthiness and controllability can be examined in domains where factual precision, normative interpretation, and ownership risk intersect.”
- **Source provenance and evidence fitness**: Annotations are performed by patent attorneys using dual-review protocol.
- **Context and stakeholder coverage**: Annotations are performed by patent attorneys using dual-review protocol.
- **Real-world harm linkage**: Replaces generic fluency or BLEU-based evaluation with domain-anchored, legally consequential error categories—enabling targeted debugging of ownership risk (e.g., overclaiming) and factual fidelity (e.g., unsupported technical effects), rather than treating all deviations as equal 'hallucinations'.  
— External Perspective (Survey) —  
• “PatentEval [Shen et al., 2024] further shows how trustworthiness and controllability can be examined in domains where factual precision, normative interpretation, and ownership risk intersect.”


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: Replaces generic fluency or BLEU-based evaluation with domain-anchored, legally consequential error categories—enabling targeted debugging of ownership risk (e.g., overclaiming) and factual fidelity (e.g., unsupported technical effects), rather than treating all deviations as equal 'hallucinations'.
- **Ground truth and disagreement design**: Annotations are performed by patent attorneys using dual-review protocol.
- **Metric validity**: Replaces generic fluency or BLEU-based evaluation with domain-anchored, legally consequential error categories—enabling targeted debugging of ownership risk (e.g., overclaiming) and factual fidelity (e.g., unsupported technical effects), rather than treating all deviations as equal 'hallucinations'.
- **Evaluator reliability**: Annotations are performed by patent attorneys using dual-review protocol.


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Annotations are performed by patent attorneys using dual-review protocol.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: Annotations are performed by patent attorneys using dual-review protocol.
- **Maintenance and update governance**: —

## Lineage critiques

• 「error taxonomy useful but doesn't cover full trustworthy spectrum.」— Sycophancy / TrustLLM

## Self-acknowledged limits

「Authors note specialized domain; expert annotation required; English.」

## External views (survey)

• 「PatentEval[Shen and others, 2024] furthers show how trustworthiness and controllability can be examined in domains where factual precision, normative interpretation, and ownership risk intersect.」

## Synthesis

The survey notes that PatentEval demonstrates how to assess credibility and controllability in domains where factual accuracy, normative interpretation, and ownership risk are intertwined. Subsequent work criticizes its error typology as useful but incomplete in covering the full credibility spectrum. The authors acknowledge that this benchmark focuses on a specific domain, requires expert annotation, and is English-only.
