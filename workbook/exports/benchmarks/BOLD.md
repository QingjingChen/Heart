# BOLD (2021)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13455.txt`

## Representative tool

Multi-axis open-ended prompt template with structured demographic attribute injection

## Tool explanation (full)

BOLD constructs a large-scale (23,679 prompts) open-generation prompt set, systematically injecting five protected attribute axes (occupation, gender, race, religion, political ideology) into Wikipedia sentences. Each prompt is truncated at a natural-language fragment (e.g., “A flight nurse is a registered…”), forcing the model to complete the text and thereby exposing its implicit biases. This template relies on real-world textual context combined with human-defined attribute alignment rules, ensuring prompts maintain linguistic coherence while enabling comparable activation of stereotypical associations along specific social dimensions.

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: “Type: Open-generation prompt set”, “23,679 prompts, sourced from English Wikipedia, with primary attribute axes including occupation, gender, race, religious belief, and political ideology”; strong_rubric_evidence explicitly states that its scenario includes role/purpose/constraints/consequences, and its task format accommodates detection of multiple bias types.

## What it improves vs. baseline

Compared with earlier synthetic prompts (e.g., single-gender pronoun substitution), BOLD enhances the authenticity and multidimensional concurrency of bias detection: rather than testing individual attributes in isolation, it supports cross-axis interactive analysis (e.g., sentiment polarity differences between “Black nurse” and “White lawyer”) and covers realistic trigger forms from downstream generation tasks.

## Adaptation example

In a medical consultation dialogue dataset, patient chief complaint sentences (e.g., “He has chest pain and fatigue”) are reformulated into multi-axis embedded prompts following the BOLD template (e.g., “A [Black] [male] patient says: ‘I have chest pain and fatigue...’”), to evaluate whether LLM-generated diagnostic recommendations systematically deviate from clinical guidelines across race–gender combinations.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: BOLD constructs a large-scale (23,679 prompts) open-generation prompt set, systematically injecting five protected attribute axes (occupation, gender, race, religion, political ideology) into Wikipedia sentences; each prompt is truncated with a natural-language fragment (e.g., “A flight nurse is a registered...”), forcing the model to complete the sentence and thereby exposing its implicit biases.  
— Lineage —  
• 5 axes & ~600 descriptors not covered; uses Wikipedia which propagates encyclopedic bias. — Smith 2022 (HolisticBias)
- **Normative grounding**: —
- **Source provenance and evidence fitness**: This template relies on real-text contexts and manually defined attribute-alignment rules to ensure prompts maintain linguistic coherence while comparably activating stereotypical associations along specific social dimensions.  
— Lineage —  
• 5 axes & ~600 descriptors not covered; uses Wikipedia which propagates encyclopedic bias. — Smith 2022 (HolisticBias)
- **Context and stakeholder coverage**: BOLD constructs a large-scale (23,679 prompts) open-generation prompt set, systematically injecting five protected attribute axes (occupation, gender, race, religion, political ideology) into Wikipedia sentences.  
— Lineage —  
• no LGBTQ+ subgroups. — Felkner 2023 (WinoQueer)
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Compared with earlier synthetic prompts (e.g., single-gender pronoun substitution), BOLD enhances the authenticity and multidimensional concurrency of bias detection: rather than testing individual attributes in isolation, it supports cross-axis interactive analysis (e.g., sentiment polarity differences between “Black nurse” and “White lawyer”) and covers realistic trigger forms from downstream generation tasks.
- **Task-format fit**: Compared with earlier synthetic prompts (e.g., single-gender pronoun substitution), BOLD enhances the authenticity and multidimensional concurrency of bias detection: rather than testing individual attributes in isolation, it supports cross-axis interactive analysis (e.g., sentiment polarity differences between “Black nurse” and “White lawyer”) and covers realistic trigger forms from downstream generation tasks.
- **Ground truth and disagreement design**: —
- **Metric validity**: — Lineage —  
• sentiment/regard metrics correlate weakly with hurtfulness; English-only. — Nozza 2021 (HONEST)
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: This template relies on real-text contexts and human-defined attribute alignment rules to ensure that prompts maintain linguistic coherence while comparably activating stereotypical associations along specific social dimensions.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• 5 axes & ~600 descriptors not covered; uses Wikipedia which propagates encyclopedic bias. — Smith 2022 (HolisticBias)
• sentiment/regard metrics correlate weakly with hurtfulness; English-only. — Nozza 2021 (HONEST)
• no LGBTQ+ subgroups. — Felkner 2023 (WinoQueer)

## Self-acknowledged limits

Authors flag Wikipedia coverage bias and that automatic toxicity classifiers themselves contain bias.

## Synthesis

Subsequent work criticizes BOLD’s 5 axes and ~600 descriptors as insufficiently comprehensive; affect/attention metrics exhibit weak correlation with harm, and the framework is English-only. The authors acknowledge Wikipedia coverage bias and inherent biases in the automated toxicity classifier itself.
