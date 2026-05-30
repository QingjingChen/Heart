# MFQ-2 (2023)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/12918.txt`

## Representative tool

Cross-culturally validated six-foundation moral judgment scale (MFQ-2)

## Tool explanation (full)

MFQ-2 is a psychometric scale validated in dual samples from the UK (N=809) and the US (N=835), comprising six moral foundations dimensions—Care, Fairness, Loyalty, Authority, Purity, and Liberty—each measured via multiple Likert-style statements. Its six-dimensional structure was confirmed through factor analysis. It does not rely on scenario generation but instead directly measures individuals’ strength of endorsement of abstract moral principles, featuring a standardized administration protocol and cross-cultural reliability and validity reports.

Extraction rationale: Primarily based on notes in the Benchmark diagnostic table: “measures the six sub-dimensions—Care, Fairness, Loyalty, Authority, Purity”; “cites Moral Foundations Theory (MFT)”; and “N=809 (UK) and N=835 (US), sourced from the MFQ-2 scale.” The source excerpt explicitly states “validated the six-foundation structure” and “three studies testing this new instrument,” confirming its empirical foundation as a reusable measurement instrument.

## What it improves vs. baseline

Compared to earlier monocultural, unidimensional moral scales (e.g., the original MFQ-1), the MFQ-2 significantly enhances cross-cultural comparability and construct stability through validation on dual-national samples and structural recalibration, providing a psychologically more robust benchmark anchor for modeling LLM moral tendencies.

## Adaptation example

In an AI tutor dataset designed for adolescent education, the MFQ-2 scale can be embedded into the user feedback module, requiring students to rate AI suggestions (e.g., “Should a peer’s cheating be reported?”) along six foundational moral dimensions, thereby constructing fine-grained moral preference profiles used to calibrate model responsiveness across diverse value groups.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: MFQ-2 is a psychometric scale validated on dual samples from the UK (N=809) and the US (N=835), comprising six moral foundations dimensions—Care, Fairness, Loyalty, Authority, Purity, and Liberty—each measured by multiple Likert-style statements, with six-factor structural validity confirmed via factor analysis.  
— Lineage —  
• Construct validity in LLM evals: MFQ designed for human surveys; transferring to LLMs (e.g., MoralChoice using MFQ axes) is non-trivial. — Subsequent work
- **Normative grounding**: —
- **Source provenance and evidence fitness**: It does not rely on scenario generation; instead, it directly measures individuals’ strength of endorsement of abstract moral principles, featuring a standardized administration protocol and cross-cultural reliability and validity reports.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: It does not rely on scenario generation; instead, it directly measures individuals’ strength of endorsement of abstract moral principles, featuring a standardized administration protocol and cross-cultural reliability and validity reports.
- **Maintenance and update governance**: —

## Lineage critiques

• Construct validity in LLM evaluations: The Moral Foundations Questionnaire (MFQ) was designed for human surveys; transferring it to LLMs (e.g., MoralChoice using MFQ axes) is non-trivial. — Future work

## Self-acknowledged limits

Authors note WEIRD sample limitation; not a model-evaluation tool.

## Synthesis

Subsequent work criticizes the MFQ-2 for construct validity issues in LLM evaluation, noting that it was originally designed as a human questionnaire and its adaptation to LLM assessment is nontrivial. The authors explicitly acknowledge that their sample is limited to WEIRD populations and that the instrument was not intended as a model evaluation tool.
