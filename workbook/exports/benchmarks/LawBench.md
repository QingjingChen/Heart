# LawBench (2024)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/pdf_texts_trust/13494.txt`

## Representative tool

Multi-step legal fact verification pipeline with jurisdiction-aware grounding

## Tool explanation (full)

LawBench constructs a multi-step verification workflow for legal QA: (1) retrieval of relevant statutory provisions from authoritative sources (e.g., Criminal Law Article 257), (2) decomposition of questions into atomic factual claims (e.g., 'violence used', 'marriage freedom interfered', 'causes death'), and (3) cross-checking each claim against codified text via exact phrase matching and semantic entailment. It relies on curated legal corpora (FLK, CAIL, LAIC) and enforces jurisdictional scope alignment (e.g., PRC Criminal Law only) to prevent hallucinated or extraterritorial interpretations.  

Extraction basis: The primary basis is the Benchmark diagnostic table notes: 'multi-step factual verification' is explicitly listed as the type; 'data sourced from multiple public databases and competition platforms including FLK, JEC_QA, CAIL, LAIC, and AIStudio' supports jurisdiction-aware grounding; the sample prompt’s explicit instruction to 'just give the content of the law directly' confirms statutory anchoring as the core design.

## What it improves vs. baseline

Moves beyond single-turn truthfulness scoring by enforcing stepwise factual anchoring to statutory text—prevents surface-level correctness masking logical gaps (e.g., answering 'Article 257' without verifying whether the provided sentence matches the full, contextually qualified provision). No contamination-resistant test set is implemented, but the multi-step structure inherently raises the bar for shallow memorization.

## Adaptation example

In medical QA datasets (e.g., MedQA-USMLE), replace the original single-hop answer with a three-step verification template: (1) retrieve a relevant clinical guideline paragraph (e.g., AHA/ACC hypertension staging), (2) extract discrete diagnostic criteria (e.g., 'SBP ≥140 mmHg AND DBP ≥90 mmHg'), (3) validate each criterion against the retrieved text before generating the final answer.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: LawBench constructs a multi-step verification workflow for legal QA: (1) retrieval of relevant statutory provisions from authoritative sources (e.g., Criminal Law Article 257), (2) decomposition of questions into atomic factual claims (e.g., 'violence used', 'marriage freedom interfered', 'causes death'), and (3) cross-checking each claim against codified text via exact phrase matching and semantic entailment.
- **Normative grounding**: — Lineage —  
• TrustLLM: knowledge ≠ trustworthiness.
- **Source provenance and evidence fitness**: It relies on curated legal corpora (FLK, CAIL, LAIC) and enforces jurisdictional scope alignment (e.g., PRC Criminal Law only) to prevent hallucinated or extraterritorial interpretations.  
— Lineage —  
• LegalBench (2023) cross-comparison: LawBench Chinese-focused; cross-jurisdiction transfer untested.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: LawBench constructs a multi-step verification workflow for legal QA: (1) retrieval of relevant statutory provisions from authoritative sources (e.g., Criminal Law Article 257), (2) decomposition of questions into atomic factual claims (e.g., 'violence used', 'marriage freedom interfered', 'causes death'), and (3) cross-checking each claim against codified text via exact phrase matching and semantic entailment.
- **Task-format fit**: Moves beyond single-turn truthfulness scoring by enforcing stepwise factual anchoring to statutory text—prevents surface-level correctness masking logical gaps (e.g., answering 'Article 257' without verifying whether the provided sentence matches the full, contextually qualified provision).
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Authors note Chinese-only; some tasks have answer-leakage from training data.
- **Robustness against gaming and contamination**: No contamination-resistant test set is implemented, but the multi-step structure inherently raises the bar for shallow memorization.
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• LegalBench (2023) cross-comparison: LawBench Chinese-focused; cross-jurisdiction transfer untested.
• TrustLLM: knowledge ≠ trustworthiness.
• PatentEval / domain-specific: doesn't cover patent law specifics.

## Self-acknowledged limits

Authors note Chinese-only; some tasks have answer-leakage from training data.

## Synthesis

Subsequent work criticizes LawBench for focusing solely on Chinese and not testing cross-jurisdictional transferability; knowledge does not equate to trustworthiness; and patent law is not covered. The authors acknowledge limitations including the exclusive focus on Chinese, and the presence of training-data leakage—where answers are inadvertently revealed in the training data—for some tasks.
