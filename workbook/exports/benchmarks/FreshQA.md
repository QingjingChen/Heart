# FreshQA / FreshLLMs (2024)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

False-Premise-Aware Temporal Fact Probe

## Tool explanation (full)

This tool constructs two types of dynamic knowledge test questions: (1) temporally grounded question-answer pairs generated from recent, publicly available, trustworthy factual sources (e.g., Wikidata snapshots, news API summaries); and (2) counterfactual prompts that explicitly embed false premises (e.g., “Given that X happened in 2022, what was the outcome?”, while X actually occurred in 2024). Models must detect premise fallacies and either refuse to answer or actively correct them—rather than defaulting to accepting the premise. The approach relies on a versioned, timestamped factual knowledge base and human-validated false-premise injection rules.

Extraction rationale: Primarily drawn from the Benchmark diagnostic table notes: “Type: temporal validity / fresh-knowledge benchmark; comprehensive survey concludes it advances trustworthiness toward dynamic world knowledge and false-premise handling”; all three high-scoring items in strong_rubric_evidence target the model’s capability to handle “rapidly changing facts” and “false-premise questions”, and the note explicitly highlights the real-world risk of “misleading inferences arising from outdated facts”.

## What it improves vs. baseline

Going beyond static knowledge benchmarks (e.g., TruthfulQA), this work is the first to systematically incorporate “premise truthfulness verification” into the trustworthiness evaluation pipeline, elevating evaluation from “whether the answer is correct” to “whether the model possesses critical awareness of premises.”

## Adaptation example

In the medical question-answering dataset MedQA, temporality-based erroneous premises (e.g., “According to the 2021 guidelines, the first-line treatment for COVID-19 is…”) are injected; models are required to recognize that the guidelines have been updated and to reject adherence to outdated standards, thereby constructing a premise robustness subset for clinical decision-making scenarios.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool constructs two types of dynamic knowledge test questions: (1) temporally grounded question-answer pairs generated from recent, publicly available, and trustworthy factual sources (e.g., Wikidata snapshots, news API summaries); and (2) counterfactual prompts that explicitly embed false premises (e.g., “Given that X happened in 2022, what was the outcome?”, while X actually occurred in 2024). Models must identify premise fallacies and either refuse to answer or actively correct them, rather than defaulting to accepting the premise.  
— External perspective (Survey) —  
• FreshQA [Vu et al., 2024] extends trustworthiness into the temporal dimension by testing whether models can reason over rapidly changing world knowledge and correctly handle false-premise questions.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: Relies on a versioned, timestamped fact repository and human-verified misinformation injection rules.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: Misleading due to outdated factual connections  
— External Perspective (Survey) —  
• These benchmarks matter because


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: Depends on a versioned timestamped fact repository.

## External views (survey)

• FreshQA [Vu and others, 2024] extends trustworthiness into the temporal dimension by testing whether models can reason over rapidly changing world knowledge and correctly handle false-premise questions. These benchmarks matter because

## Synthesis

The survey notes that FreshQA extends credibility to the temporal dimension, testing models’ ability to handle rapidly changing facts and questions with false premises. Such benchmarks are important.
