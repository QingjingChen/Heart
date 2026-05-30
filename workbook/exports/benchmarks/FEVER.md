# FEVER (2018)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/pdf_texts_trust/13484.txt`

## Representative tool

Evidence-grounded claim verification pipeline with explicit sentence-level retrieval + entailment classification

## Tool explanation (full)

FEVER introduces a two-stage pipeline: (1) retrieve relevant Wikipedia sentences for a given claim via IR, then (2) classify the logical relationship (Supported/Refuted/NotEnoughInfo) between claim and retrieved evidence using natural language inference. It constructs claims from Wikipedia edits and pairs them with human-annotated evidence snippets, enforcing explicit grounding — every verdict must be justified by cited textual spans.

Evidence extraction: The source excerpt explicitly contrasts FEVER with prior tasks where “the passage to verify each claim is given”, highlighting its novel requirement of retrieving evidence from a large document corpus. The workbook note confirms its strength in “evidence grounding” and identifies Wikipedia as a traceable source — core to the tool’s design.

## What it improves vs. baseline

Moves beyond single-sentence fact-checking benchmarks (e.g., SNLI) by requiring *retrieval-aware verification*: models must both find relevant evidence *and* reason over it — thus exposing failures in evidence sourcing, not just surface-level consistency.

## Adaptation example

In the medical QA dataset, patient questions (e.g., “Can metformin prevent cancer?”) are converted into claims; models are required to retrieve supporting/refuting sentences from PubMed abstracts and annotate their alignment with clinical guidelines (e.g., NCCN), thereby constructing an auditable, evidence-based reasoning chain.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: —
- **Normative grounding**: —
- **Source provenance and evidence fitness**: FEVER introduces a two-stage pipeline: (1) retrieve relevant Wikipedia sentences for a given claim via IR, then (2) classify the logical relationship (Supported/Refuted/NotEnoughInfo) between claim and retrieved evidence using natural language inference. It constructs claims from Wikipedia edits and pairs them with human-annotated evidence snippets, enforcing explicit grounding — every verdict must be justified by cited textual spans.  
— Lineage —  
• FEVER tests retrieval-grounded fact-checking; doesn't address truthfulness when models confabulate. — TruthfulQA (2022)  
— External Perspective (Survey) —  
• FEVER requires models to determine whether claims are supported, refuted, or unverifiable and to retrieve supporting evidence. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Moves beyond single-sentence fact-checking benchmarks (e.g., SNLI) by requiring *retrieval-aware verification*: models must both find relevant evidence *and* reason over it — thus exposing failures in evidence sourcing, not just surface-level consistency.  
— Lineage —  
• FEVER fact-checking misses calibration / adversarial-pressure failures. — Sycophancy literature
- **Task-format fit**: FEVER introduces a two-stage pipeline: (1) retrieve relevant Wikipedia sentences for a given claim via IR, then (2) classify the logical relationship (Supported/Refuted/NotEnoughINFO) between claim and retrieved evidence using natural language inference. It constructs claims from Wikipedia edits and pairs them with human-annotated evidence snippets, enforcing explicit grounding — every verdict must be justified by cited textual spans.  
— Lineage —  
• single-task; doesn't span multiple trustworthy dimensions. — TrustLLM (2024)  
— External perspective (Survey) —  
• FEVER requires models to determine whether claims are supported, refuted, or unverifiable and to retrieve supporting evidence. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Ground truth and disagreement design**: Authors note Wikipedia evidence boundary; NOT-ENOUGH-INFO label often debated.
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: It constructs claims from Wikipedia edits and pairs them with human-annotated evidence snippets, enforcing explicit grounding — every verdict must be justified by cited textual spans.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• FEVER tests retrieval-grounded fact-checking; doesn't address truthfulness when models confabulate. — TruthfulQA (2022)
• FEVER fact-checking misses calibration / adversarial-pressure failures. — Sycophancy literature
• single-task; doesn't span multiple trustworthy dimensions. — TrustLLM (2024)

## Self-acknowledged limits

Authors note Wikipedia evidence boundary; NOT-ENOUGH-INFO label often debated.

## External views (survey)

• FEVER requires models to determine whether claims are supported, refuted, or unverifiable and to retrieve supporting evidence. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The survey notes that FEVER requires models to determine whether a claim is supported, refuted, or unverifiable, and to retrieve supporting evidence. Subsequent work criticizes FEVER for testing only retrieval-based fact-checking, failing to address model hallucination and truthfulness; lacking calibration and adversarial stress testing; and being a single-task benchmark, thus not covering multiple trustworthiness dimensions. The authors acknowledge their reliance on Wikipedia as the evidence boundary and note that the NOT-ENOUGH-INFO label is often contentious.
