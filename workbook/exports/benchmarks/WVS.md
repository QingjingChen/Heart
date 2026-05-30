# WVS / World Values Survey (2012)

**Dimension**: Human centered  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Cross-Cultural Value Distribution Anchoring Template

## Tool explanation (full)

This tool converts the World Values Survey (WVS) value questionnaires—administered across 50+ countries with nationally representative, ~1,000-person samples per country (e.g., “importance of gender equality”, “acceptance of religious authority”)—into standardized anchor templates embeddable in LLM tasks. For each value dimension, it extracts country- or region-level distributional parameters (mean, variance, skewness) and cultural clusters (e.g., English-speaking vs. Confucian societies), then constructs a “value consistency scoring function”: the smaller the Wasserstein distance between the model’s output distribution and the target cultural cluster’s empirical distribution, the higher the score. It does not rely on a single “correct answer”, but instead treats empirically observed distributions as the gold standard.

Extraction rationale: Primarily based on notes in the Benchmark diagnostic table: “cross-cultural value survey, used to assess value consistency and cross-cultural value distributions; contextual subject: covers multiple cultures and value dimensions” and “strength: cross-cultural coverage; weakness: not an LLM benchmark, requires rewriting into task format”; source_excerpt states “Beyond Alignment... places Human-Centricity as the core value destination”, aligning with WVS’s role as the “value consistency baseline”.

## What it improves vs. baseline

It addresses the Western-centric ethical assumptions inherent in traditional benchmarks by introducing the first value alignment benchmark grounded in large-scale empirical cross-cultural data—distributed and non-normative—enabling evaluation to shift from “whether a system conforms to a given set of principles” to “whether it aligns with the actual value distribution of a specific cultural group.”

## Adaptation example

In a multilingual LLM for e-commerce customer service targeting Southeast Asia, use this template to anchor the importance ratings of “respecting elders during service” from the World Values Survey (WVS) for Thailand, Vietnam, and Indonesia (Likert-scale 1–10 means: 8.2, 7.9, and 8.5, respectively), and adapt the original customer-service instruction-tuning data accordingly: require the model, when handling scenarios involving “complaints about elders being neglected”, to align its responses’ honorific density and responsibility-attribution phrasing with the empirically observed distributions across these three countries—rather than uniformly applying Western “egalitarian” discourse patterns.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: —
- **Normative grounding**: It addresses the Western-centric ethical assumptions inherent in traditional benchmarks by introducing the first value alignment benchmark grounded in large-scale empirical cross-cultural data—distributed and non-normative—enabling evaluation to shift from “whether a system conforms to a given set of principles” to “whether it aligns with the actual value distribution of a specific cultural group.”
- **Source provenance and evidence fitness**: This tool transforms the World Values Survey (WVS)’s value questionnaires—administered across 50+ countries with nationally representative samples of ~1,000 respondents per country (e.g., “importance of gender equality”, “acceptance of religious authority”)—into standardized anchor templates embeddable in LLM tasks. For each value dimension, it extracts country- or region-level distributional parameters (mean, variance, skewness) and cultural clusters (e.g., English-speaking vs. Confucian societies), then constructs a “value consistency scoring function”: the smaller the Wasserstein distance between the model’s output and the target cultural cluster’s empirical distribution, the higher the score. It does not rely on a single “correct answer”, but instead uses empirically observed distributions as the gold standard.  
— External Perspective (Survey) —  
• The World Values Survey (WVS) [noa, 2012] is a comprehensive cross-cultural study of human values, examining the evolution of social, cultural, political, and religious values across the globe. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Context and stakeholder coverage**: This tool transforms the World Values Survey (WVS)’s value questionnaires—administered across 50+ countries with nationally representative samples of ~1,000 respondents per country (e.g., “importance of gender equality”, “acceptance of religious authority”)—into standardized anchor templates embeddable in LLM tasks. For each value dimension, it extracts country- or region-level distributional parameters (mean, variance, skewness) and cultural clusters (e.g., English-speaking vs. Confucian societies), then constructs a “value consistency scoring function”: the smaller the Wasserstein distance between the model’s output and the target cultural cluster’s empirical distribution, the higher the score. It does not rely on a single “correct answer”, but instead uses empirically observed distributions as the gold standard.  
— External Perspective (Survey) —  
• The World Values Survey (WVS) [noa, 2012] is a comprehensive cross-cultural study of human values, examining the evolution of social, cultural, political, and religious values across the globe. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: It does not rely on a single “correct answer” but instead uses an empirical distribution as the gold standard.
- **Metric validity**: We further construct a “value-consistency scoring function” such that a model’s score increases as the Wasserstein distance between its output distribution and the target cultural cluster distribution decreases.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• The World Values Survey (WVS) [noa, 2012] is a comprehensive cross-cultural study of human values, examining the evolution of social, cultural, political, and religious values across the globe. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The review states that the WVS is a comprehensive cross-cultural study of human values, examining the evolution of social, cultural, political, and religious values worldwide.
