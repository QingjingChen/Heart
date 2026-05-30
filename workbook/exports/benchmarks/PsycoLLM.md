# PsycoLLM / Psychometrics / PsychCounsel / ValueBench (survey-mentioned psychology/value benchmarks)

**Dimension**: Human centered  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Psychometrically grounded item templates from clinical/consulting instruments (e.g., PHQ-9, GAD-7 adapted as LLM response prompts)

## Tool explanation (full)

This tool converts standardized items from established psychological scales (e.g., the PHQ-9 depression screening scale, the GAD-7 anxiety scale) into structured prompt templates, requiring LLMs to simulate a psychotherapist’s empathic responses, risk identification, or value clarification based on user self-reports; it relies on the semantic structure and scoring logic of clinically validated, reliability- and validity-tested items—not simple question-answer classification; it falls under the “Human-centered” label because it directly anchors operationalizable measurement of human subjective experience (emotional states, value conflicts, psychological safety needs).  

Extraction rationale: Primarily drawn from the Benchmark diagnostic table notes: “Type: Psychological/Value/Counseling Competency Evaluation Family. Comprehensive survey indicates that benchmarks in this family mostly originate from psychological scales or counseling scenarios, filling the emotional and value dimensions of ‘human-centered’ evaluation—but often remain at the level of knowledge recall or classification.” Additionally, all three criteria in strong_rubric_evidence received a score of 3, with the note explicitly stating “psychological scales, counseling Q&A, or value-based questions used to assess emotion recognition, psychological support, and value judgment,” confirming its core contribution is the adaptation of clinical measurement tools into LLM diagnostic templates.

## What it improves vs. baseline

Compared to general ethics classification questions (e.g., “Does it respect autonomy?”), this tool introduces empirically validated constructs from clinical psychology, symptom hierarchies, and response-bias calibration mechanisms—shifting evaluation from abstract value judgments toward embodied, context-sensitive, human-centered capability diagnostics.

## Adaptation example

In the mental health hotline dialogue dataset, after inputting the original user’s self-disclosure text, the model is constrained to generate a structured response aligned with PHQ-9 Item 3 (“Little interest or pleasure in doing things”): first confirming perception (“You mentioned recently finding it difficult to muster motivation for activities…”), then offering evidence-based support options (excluding medication recommendations, instead focusing on behavioral activation strategies), and finally outputting a risk-level judgment (low/medium/high), thereby transforming a static scale into a dynamic, interactive assessment protocol.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool converts standardized items from established psychological assessment scales—such as the PHQ-9 for depression screening and the GAD-7 for anxiety screening—into structured prompt templates that instruct large language models (LLMs) to simulate a psychotherapist’s empathetic responses, risk identification, or value clarification based on user self-reports. It relies on the semantically validated clinical item structure and scoring logic of these instruments, rather than simple question-answer classification.
- **Normative grounding**: The “Human-centered” label applies because it directly anchors operationalizable measurements to human subjective experiences (e.g., emotional states, value conflicts, psychological safety needs).
- **Source provenance and evidence fitness**: This tool converts standardized items from established psychological assessment scales—such as the PHQ-9 for depression screening and the GAD-7 for anxiety screening—into structured prompt templates that instruct large language models (LLMs) to simulate a psychotherapist’s empathetic responses, risk identification, or value clarification based on user self-reports. It relies on the semantically validated clinical item structure and scoring logic of these instruments, rather than simple question-answer classification.
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
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Synthesis

The survey does not mention this benchmark, and no subsequent work criticizes it.
