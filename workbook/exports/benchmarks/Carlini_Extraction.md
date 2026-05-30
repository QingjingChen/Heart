# Carlini Extraction / Training Data Extraction (2021)

**Dimension**: Privacy  **Source / path**: `Paper: Carlini et al. - Extracting Training Data from Large Language Models`

## Representative tool

Verbatim Memorization Attack Pipeline

## Tool explanation (full)

This tool implements a systematic training data extraction attack pipeline: First, it samples high-likelihood, low-entropy sensitive fragments (e.g., personally identifiable information, medical records) from the target model’s training corpus and constructs targeted prompts to trigger verbatim reproduction of the original text; second, it determines whether verbatim leakage has occurred via exact string matching and an edit-distance threshold. It relies on a high-quality, traceable subset of the original training data as ground truth, emphasizing causal attribution—rather than correlational statistics—of model memorization behavior.

Extraction rationale: Primarily based on notes in the Benchmark diagnostic table: “Type: Training data memorization/extraction attack; comprehensive surveys cite it as establishing the verbatim memorization methodology in LLM privacy evaluation”; additionally, all three criteria in strong_rubric_evidence receive full scores, each explicitly anchoring the construct, normative basis, and harm linkage.

## What it improves vs. baseline

It pioneers the operationalization of privacy risk as a reproducible and attributable word-level leakage measurement, distinguishing itself from earlier qualitative assessments that relied solely on manual spot-checking or vague similarity judgments, thereby establishing an empirical paradigm of “memory-as-risk” in privacy evaluation.

## Adaptation example

In the medical Q&A fine-tuning dataset, use this pipeline to extract model verbatim repetition of patient medical record summaries: first sample de-identification failure samples containing SSN/DOB from public clinical text corpora (e.g., MIMIC-III), construct prompts such as “Please repeat the following medical record verbatim”, and detect whether the model outputs protected health information (PHI) unchanged.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool implements a systematic training data extraction attack pipeline: first, it samples high-likelihood, low-entropy sensitive segments (e.g., personally identifiable information, medical records) from the target model’s training corpus; then, it constructs targeted prompts to elicit verbatim reproduction of the original text by the model; finally, it determines whether verbatim leakage has occurred via exact string matching and a thresholded edit distance.
- **Normative grounding**: Relies on high-quality, traceable subsets of raw training data as ground truth, emphasizing causal attribution—rather than correlational statistics—for model memorization behavior.
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: It pioneers the operationalization of privacy risk as a reproducible and attributable word-level leakage measurement, distinguishing itself from earlier qualitative assessments that relied solely on manual spot-checking or vague similarity judgments, thereby establishing an empirical paradigm of “memory-as-risk” in privacy evaluation.


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: Relying on high-quality, traceable subsets of raw training data as ground truth.
- **Metric validity**: Subsequently, exact string matching and a threshold on edit distance are employed to determine whether verbatim leakage has occurred.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —
