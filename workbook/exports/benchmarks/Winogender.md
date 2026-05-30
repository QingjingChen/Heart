# Winogender (2018)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/10838.txt`

## Representative tool

Minimal-pair Winograd-style coreference templates with BLS-calibrated gender occupation priors

## Tool explanation (full)

This tool constructs a set of minimal pair sentences that differ only in pronoun gender (he/she/they), with all other components—including occupational nouns, syntactic structure, and semantic roles—held strictly constant. All templates are anchored to real-world occupational gender distribution data published by the U.S. Bureau of Labor Statistics (BLS), thereby grounding “pro-stereotype” and “anti-stereotype” judgments in empirical benchmarks. Bias strength is quantified in an interpretable manner by computing the accuracy difference (Δ) between model performance on pro- versus anti-stereotype sentence pairs, and correlating this Δ with the corresponding BLS gender proportions.

Extraction rationale: Primarily based on the Benchmark diagnostic table’s “notes”: the notes explicitly state “based on occupational gender ratios from the U.S. Bureau of Labor Statistics (BLS)”, and the metric design includes Accuracy, Δ (pro vs. anti), and the correlation coefficient with BLS gender proportions. Although the source_excerpt is truncated, it repeatedly contains key phrases such as “Winograd schema-style minimal pair sentences that differ only by pronoun gender” and “correlate this bias with real-world”, confirming the dual core of template construction and empirical calibration.

## What it improves vs. baseline

Compared to earlier bias detection methods that relied solely on human intuition or static word vector analogies (e.g., “Bias in Word Embeddings”), this tool is the first to embed empirical social statistics (BLS) into evaluation construction, elevating bias measurement from “relative preference” to “systematic diagnosis of deviation from real-world distributions”, and supporting normalized metrics (Δ + r) for cross-model horizontal comparison.

## Adaptation example

In the medical consultation dialogue dataset, replace the doctor–patient role pairs with BLS-calibrated occupation–pronoun combinations (e.g., “The nurse told the patient… he/she could schedule a follow-up”), generating minimally divergent sentence pairs to diagnose whether large models distort responsibility attribution or professional credibility judgments in clinical recommendation generation due to gender priors.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool constructs a set of minimal pair sentences that differ only in pronoun gender (he/she/they), with all other components—including occupational nouns, syntactic structure, and semantic roles—held constant.  
— Lineage —  
• Synthetic templates underestimate real-world bias; tiny size (720 sentences); cannot stress-test models. — Levy 2021 (BUG)  
• Only binary gender + 'they'; no LGBTQ+ axis. — Felkner 2023 (WinoQueer)  
• Winogender pairs forced into binary categorization, no neutral targets. — Vanmassenhove 2021 (NeuTral Rewriter)  
• Occupation axis only, ignores hundreds of other demographic descriptors. — Smith 2022 (HolisticBias)  
— External perspective (Survey) —  
• Winogender serves as a diagnostic benchmark to quantify gender bias in coreference resolution systems using 120 hand-crafted templates across 60 occupations. — Survey paragraphs 425–430
- **Normative grounding**: All templates are anchored to real-world occupational gender distribution data published by the U.S. Bureau of Labor Statistics (BLS), providing an empirical basis for “pro-stereotype” and “anti-stereotype” judgments.
- **Source provenance and evidence fitness**: All templates are anchored to real-world occupational gender distribution data published by the U.S. Bureau of Labor Statistics (BLS).
- **Context and stakeholder coverage**: — Lineage —  
• only binary gender + 'they'; no LGBTQ+ axis. — Felkner 2023 (WinoQueer)  
• occupation axis only, ignores hundreds of other demographic descriptors. — Smith 2022 (HolisticBias)
- **Real-world harm linkage**: Quantify bias strength in an interpretable manner by computing the accuracy difference (Δ) of the model on two sentence types and correlating this difference with the actual proportion of BLS data.  
— Lineage —  
• synthetic templates underestimate real-world bias; tiny size (720 sentences); cannot stress-test models. — Levy 2021 (BUG)


### Evaluation design (5 rubrics)
- **Scenario validity**: This tool constructs a set of minimal pairs—sentences that differ only in pronoun gender (he/she/they), with all other components (occupation nouns, syntactic structure, semantic roles) held constant.  
— Lineage —  
• Synthetic templates underestimate real-world bias; tiny size (720 sentences); cannot stress-test models. — Levy 2021 (BUG)
- **Task-format fit**: By computing the accuracy difference (Δ) of the model on two types of sentences and correlating this difference with the actual proportion of BLS, the strength of bias is quantified in an interpretable manner.
- **Ground truth and disagreement design**: —
- **Metric validity**: By computing the accuracy difference (Δ) of the model on two types of sentences and correlating this difference with the actual proportion of BLS, the strength of bias is quantified in an interpretable manner.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: All templates are anchored to real-world occupational gender distribution data published by the U.S. Bureau of Labor Statistics (BLS), providing an empirical basis for “pro-stereotype” and “anti-stereotype” judgments.
- **Robustness against gaming and contamination**: — Lineage —  
• synthetic templates underestimate real-world bias; tiny size (720 sentences); cannot stress-test models. — Levy 2021 (BUG)
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• synthetic templates underestimate real-world bias; tiny size (720 sentences); cannot stress-test models. — Levy 2021 (BUG)
• only binary gender + 'they'; no LGBTQ+ axis. — Felkner 2023 (WinoQueer)
• Winogender pairs forced into binary categorization, no neutral targets. — Vanmassenhove 2021 (NeuTral Rewriter)
• occupation axis only, ignores hundreds of other demographic descriptors. — Smith 2022 (HolisticBias)

## Self-acknowledged limits

Diagnostic, not training; binary occupation set; synthetic templates.

## External views (survey)

• WinoBias was the first to test gender bias in coreference, but it only covers this narrow task. Winogender serves as a diagnostic benchmark to quantify gender bias in coreference resolution systems using 120 hand-crafted templates across 60 occupations. — Survey §§425–430

## Synthesis

The review states that Winogender is a diagnostic benchmark using 120 handcrafted templates and 60 occupations to quantify gender bias in coreference resolution. Subsequent work criticizes it for covering only a narrow task, failing to encompass other social dimensions, and underestimating real-world bias due to its synthetic templates.
