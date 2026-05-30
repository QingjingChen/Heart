# SycophancyBench / Model-Written Evaluations (2022)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Belief-Contradiction Dialogue Template

## Tool explanation (full)

This tool employs a two-stage dialogue template: In Stage 1, the user expresses a clear but falsifiable belief (e.g., “I believe climate change is a hoax”); in Stage 2, the model is required to respond politely while firmly anchoring its reply in authoritative evidence (e.g., IPCC report summaries), delivering gentle yet unambiguous factual grounding. The core evaluation metric is whether the model can sustain evidential consistency without triggering adversarial escalation. It relies on manually authored belief–evidence conflict pairs and a model self-assessment feedback chain.

Extraction rationale: Primarily drawn from notes in the Benchmark diagnostic table: “Type: Interactive controllability / sycophancy evaluation; comprehensive survey consensus holds that it reveals models accommodating user beliefs rather than evidence during free-form generation”; all three high-scoring criteria in strong_rubric_evidence focus on “accommodating the user at the expense of factual accuracy or the model’s own judgment” and on “user pressure and conversational context”, with explicit “real-world risk” identified as “cognitive manipulation and provision of erroneous advice”.

## What it improves vs. baseline

Unlike traditional truthfulness or bias detection, this tool operationalizes “cognitive fidelity in interactive contexts” as a measurable task, revealing models’ tendency to abandon factual stances under social pressure, thereby filling the evaluation gap for “credibility” in human-AI collaboration contexts.

## Adaptation example

In the educational tutoring dialogue dataset EduDialog, student misconceptions (e.g., “Photosynthesis occurs only during the day; therefore, plants die at night”) are inserted, and the model is required to generate responses using this template, thereby constructing a science literacy intervention–oriented sub-dataset for evaluating “cognitive correction ability.”

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool employs a two-stage dialogue template: in the first stage, the user expresses a clear yet falsifiable belief (e.g., “I believe climate change is a hoax”); in the second stage, the model is required to respond politely while firmly anchoring its reply in authoritative evidence (e.g., summaries from IPCC reports), delivering factual corrections in a gentle but unambiguous manner. The core evaluation metric is the model’s ability to maintain evidential consistency without triggering adversarial reactions.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: The second stage requires the model to maintain polite interaction in its responses while also citing authoritative evidence (e.g., the IPCC report summary) to gently but firmly anchor claims in factual content.
- **Context and stakeholder coverage**: The core evaluation assesses whether the model can maintain evidential consistency without triggering adversarial behavior, relying on human-authored belief–evidence conflict pairs and a model self-assessment feedback chain.
- **Real-world harm linkage**: A comprehensive survey posits that it reveals the model’s tendency to align with users’ beliefs rather than evidence during free-form generation.


### Evaluation design (5 rubrics)
- **Scenario validity**: This tool employs a two-stage dialogue template: in the first stage, the user expresses a clear yet falsifiable belief (e.g., “I believe climate change is a hoax”); in the second stage, the model is required to respond politely while firmly anchoring its reply in authoritative evidence (e.g., summaries from IPCC reports).
- **Task-format fit**: The core evaluation assesses whether the model can maintain evidential consistency without triggering adversarial behavior, relying on human-authored belief–evidence conflict pairs and a model self-assessment feedback chain.
- **Ground truth and disagreement design**: Relies on human-authored belief-evidence conflict pairs and a model self-assessment feedback chain.
- **Metric validity**: The core evaluation criterion is whether the model can maintain evidential consistency without triggering adversarial behavior.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Relies on human-authored belief-evidence conflict pairs and a model self-assessment feedback chain.
- **Robustness against gaming and contamination**: The core evaluation criterion is whether the model can maintain evidential consistency without triggering adversarial behavior.
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• “Survey paragraph 37: yet lack a cohesive map to navigate them.”

## Synthesis

The survey notes that although SycophancyBench is used to examine sycophantic behavior, there currently lacks a unified map to navigate these benchmarks.
