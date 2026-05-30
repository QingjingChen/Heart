# TruthfulQA (2022)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/pdf_texts_trust/10802.txt`

## Representative tool

Imitative falsehood prompting framework with expert-curated false answer templates and counterfactual contrast sets

## Tool explanation (full)

TruthfulQA constructs questions designed to elicit *human-like misconceptions* (e.g., medical myths, logical fallacies), then provides parallel true/false answer options — including linguistically plausible but factually wrong answers authored by domain experts. Each item includes citation-backed ground truth and is grouped into 38 semantic categories to stress-test model susceptibility to specific falsehood patterns.  

Extraction basis: The source excerpt is truncated, but the workbook note explicitly names “inducing false answers” and cites examples such as “cough CPR” with clinical source links; strong rubric evidence notes “multiple true/false answers” and “expert + Wikipedia labels”. The tool’s core — imitative falsehood design — is directly stated in the workbook’s “good in inducing falsehoods” assessment.

## What it improves vs. baseline

Shifts from generic truthfulness evaluation (e.g., simple factual QA) to *adversarial misconception probing*: by pre-embedding common false beliefs into prompts and answer candidates, it isolates model tendency to replicate societal misinformation rather than merely fail recall.

## Adaptation example

In the judicial assistance dataset, questions on “justification of self-defense” (e.g., “Does chasing another person with a knife and causing minor injury invariably constitute intentional injury?”) are designed; controversial views from criminal law academia (e.g., “excessive self-defense requires subjective awareness”) are injected as false answer templates, accompanied by the verbatim text of Supreme People’s Court guiding case rulings and Article 20 of the Criminal Law, requiring the model to discern divergences in normative interpretation rather than merely reciting statutory provisions.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: TruthfulQA constructs questions designed to elicit *human-like misconceptions* (e.g., medical myths, logical fallacies), then provides parallel true/false answer options—including linguistically plausible but factually wrong answers authored by domain experts. Each item includes citation-backed ground truth and is grouped into 38 semantic categories to stress-test model susceptibility to specific falsehood patterns.  
— Lineage —  
• single-axis (truthfulness); doesn't cover trustworthiness holistically. — TrustLLM (2024)  
— External perspectives (Survey) —  
• TruthfulQA [Lin et al., 2022] remains one of the most influential benchmarks because it does not merely ask whether a model can answer factual questions, but whether it can avoid reproducing common human misconceptions and
- **Normative grounding**: —
- **Source provenance and evidence fitness**: Each item includes citation-backed ground truth
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: Shifts from generic truthfulness evaluation (e.g., simple factual QA) to *adversarial misconception probing*: by pre-embedding common false beliefs into prompts and answer candidates, it isolates model tendency to replicate societal misinformation rather than merely fail recall.


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: TruthfulQA constructs questions designed to elicit *human-like misconceptions* (e.g., medical myths, logical fallacies), then provides parallel true/false answer options — including linguistically plausible but factually wrong answers authored by domain experts.  
— Lineage —  
• TruthfulQA's MC format doesn't probe sycophantic responses under user pressure. — Sycophancy (Sharma 2025)
- **Ground truth and disagreement design**: Each item includes citation-backed ground truth and is grouped into 38 semantic categories to stress-test model susceptibility to specific falsehood patterns.
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Authors note 817 small; hand-curated common misconceptions; English.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• single-axis (truthfulness); doesn't cover trustworthiness holistically. — TrustLLM (2024)
• TruthfulQA's MC format doesn't probe sycophantic responses under user pressure. — Sycophancy (Sharma 2025)
• text-only; multimodal hallucination unaddressed. — HallusionBench (2024)

## Self-acknowledged limits

Authors note 817 small; hand-curated common misconceptions; English.

## External views (survey)

• TruthfulQA [Lin et al., 2022] remains one of the most influential benchmarks because it does not merely ask whether a model can answer factual questions, but whether it can avoid reproducing common human misconceptions and

## Synthesis

The survey notes that TruthfulQA not only tests whether models can answer factual questions but also whether they avoid common human misconceptions. Subsequent work criticizes it for focusing solely on truthfulness, failing to comprehensively cover other subconstructs of trustworthiness, and for its multiple-choice (MC) format—which cannot detect sycophantic responses under user pressure and does not address multimodal hallucinations. The authors acknowledge that the dataset is relatively small and English-only.
