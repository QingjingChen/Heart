# FFT (2024)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13252.txt`

## Representative tool

Three-dimensional scenario taxonomy (True-False decision, open-generation, identity/context-sensitive assessment)

## Tool explanation (full)

FFT (2024) introduces a structured three-dimensional task taxonomy that explicitly separates evaluation into (1) binary truth-value judgment (e.g., “Is Cape of Good Hope the southernmost point of Africa?”), (2) unconstrained open-generation responses to sensitive prompts (e.g., health/crime/credit assessments), and (3) identity- or context-aware evaluations (e.g., preference elicitation under demographic framing). This taxonomy is grounded in real-world deployment scenarios and manually curated from diverse sources (Wikipedia, Reddit, blogs, GPT-3.5 generations), enabling fine-grained behavioral profiling beyond surface-level toxicity.  

Extraction basis: Primarily drawn from the Benchmark Diagnostic Table notes: “Type: Mixed multiple-choice and open-generation set”, “Scenarios include True-False decision-making, open generation, identity preferences, credit assessment, crime assessment, health assessment, and toxicity assessment”, and the high score (4/4) in strong_rubric_evidence for Scenario validity and Task-format fit—explicitly attributed to this three-dimensional task structure.

## What it improves vs. baseline

Moves beyond single-format (e.g., MCQ-only) safety benchmarks by enabling parallel assessment of model behavior across decision-making, generative refusal, and contextual bias dimensions — addressing SafetyBench (2024)'s criticism that MCQ formats fail to capture generative misalignment.

## Adaptation example

In the medical QA dataset, original single-turn dialogue samples are decomposed into three subtasks: (1) True-False verification (e.g., “Can insulin be used to treat type 1 diabetes? Yes/No”), (2) open-ended response generation (the same question requires the model to explain mechanisms and contraindications), and (3) identity-sensitive variants (adding contextual modifiers such as “the patient is a 12-year-old child with renal insufficiency”), thereby systematically exposing model failure points in factual accuracy, explanatory safety, and demographic-aware harm mitigation.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: — Lineage —  
• Three axes mixed; constructs not separately operationalized. — SALAD-bench (2024)  
• “Harmlessness” as joint of fact+fair+tox conflates orthogonal dimensions. — Construct validity literature
- **Normative grounding**: —
- **Source provenance and evidence fitness**: This taxonomy is grounded in real-world deployment scenarios and manually curated from diverse sources (Wikipedia, Reddit, blogs, GPT-3.5 generations)
- **Context and stakeholder coverage**: identity- or context-aware evaluations (e.g., preference elicitation under demographic framing)
- **Real-world harm linkage**: enabling fine-grained behavioral profiling beyond surface-level toxicity


### Evaluation design (5 rubrics)
- **Scenario validity**: introduces a structured three-dimensional task taxonomy that explicitly separates evaluation into (1) binary truth-value judgment (e.g., 'Is Cape of Good Hope the southernmost point of Africa?'), (2) unconstrained open-generation responses to sensitive prompts (e.g., health/crime/credit assessments), and (3) identity- or context-aware evaluations (e.g., preference elicitation under demographic framing)
- **Task-format fit**: Moves beyond single-format (e.g., MCQ-only) safety benchmarks by enabling parallel assessment of model behavior across decision-making, generative refusal, and contextual bias dimensions.  
— Lineage —  
• MCQ format limits coverage of generative behavior. — SafetyBench (2024)
- **Ground truth and disagreement design**: —
- **Metric validity**: addressing SafetyBench (2024)'s criticism that MCQ formats fail to capture generative misalignment
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• three axes mixed; constructs not separately operationalized. — SALAD-bench (2024)
• MCQ format limits coverage of generative behavior. — SafetyBench (2024)
• 'harmlessness' as joint of fact+fair+tox conflates orthogonal dimensions. — Construct validity literature

## Self-acknowledged limits

Workshop paper (KDD); authors note three axes mixed; size 2116 limits subgroup analysis.

## External views (survey)

• The FFT[Cui et al., 2024] dataset is a pioneering benchmark designed to provide a comprehensive evaluation of the harmlessness of Large Language Models (LLMs). Diverging from traditional assessments that focus primarily on toxic content, FFT introduces 2,116 meticulously crafted instances evaluated across three core dimensions: Factuality, Fairness, and Toxicity. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The survey states that FFT is a comprehensive benchmark for evaluating the harmlessness of LLMs, covering three core dimensions: factuality, fairness, and toxicity. Subsequent work criticizes FFT for mixing these three axes without separate operationalization, notes that its MCQ format limits coverage of generative behaviors, and argues that defining “harmlessness” as the conjunction of factuality, fairness, and toxicity conflates orthogonal dimensions. The authors acknowledge that this paper is a KDD workshop paper, that the three axes are mixed, and that scale limitations restrict subgroup analysis.
