# Panda (2022)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13467.txt`

## Representative tool

Demographic Perturbation Augmentation Pipeline with Legal Anchoring

## Tool explanation (full)

Panda proposes a text perturbation pipeline constrained by law and policy: given an original text snippet, it identifies demographic referents (e.g., “Queen Victoria”), then generates semantically consistent rewrites with altered demographic attributes—replacing each referent according to predefined axes (gender/race/age) and their legally sanctioned alternative sets (e.g., EEOC-defined gender-neutral titles, U.S. Census Bureau standard racial/ethnic terminology). All perturbations must satisfy the “fairscore” metric—i.e., the KL divergence between the model’s output distribution on perturbed inputs and its output distribution on original inputs must fall below a specified threshold.

Extraction basis: The source_excerpt explicitly states “approaches for perturbing demographic references” and criticizes existing methods as “rigid and error prone”, emphasizing that this work “asks whether training on demographic references” can improve fairness; the workbook_dataset_note explicitly grounds the method in “law (U.S. EEOC), policy (AI RMF), and social surveys”; and strong_rubric_evidence assigns a score of 4 to “Normative grounding”, confirming legal anchoring as a core innovation, primarily drawn from the Benchmark diagnostic table notes.

## What it improves vs. baseline

Unlike rule-driven simple substitutions (e.g., GENDER-SWAP), this pipeline explicitly anchors perturbation generation in legal definitions (EEOC), policy frameworks (NIST AI RMF), and social survey data, endowing perturbations with normative legitimacy and real-world deployment relevance—thereby shifting fairness evaluation from technical correction toward compliance orientation.

## Adaptation example

In the resume screening dataset, this pipeline can be applied to the statement “She is a young Black woman with a PhD from MIT”, generating perturbed versions per EEOC guidelines (e.g., “They are an early-career Black professional with a PhD from MIT”), and enforcing a constraint that the KL divergence of the model’s “leadership potential” scores before and after perturbation remains < 0.05—thereby embedding fairness constraints into the end-to-end evaluation process.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Given an original text snippet, identify demographic referents (e.g., “Queen Victoria”) and, based on predefined axes (gender/race/age) and their legally grounded substitute sets (e.g., EEOC-defined gender-neutral titles, U.S. Census Bureau–standard racial/ethnic terminology), generate semantically consistent rewritten samples with modified demographic attributes.
- **Normative grounding**: This pipeline explicitly anchors perturbation generation to legal definitions (e.g., EEOC), policy frameworks (e.g., NIST AI RMF), and social survey data, thereby ensuring normative legitimacy and real-world deployment relevance.
- **Source provenance and evidence fitness**: Generate rewritten samples that preserve semantic consistency while altering demographic attributes, based on predefined axes (e.g., gender, race, age) and their legally sanctioned alternatives (e.g., EEOC-defined gender-neutral honorifics, U.S. Census Bureau-standard racial/ethnic terminology).
- **Context and stakeholder coverage**: — Lineage —  
• Panda only 3 axes; HolisticBias extends to 13 axes. — Smith 22 (HolisticBias)
- **Real-world harm linkage**: — Lineage —  
• Perturbation may produce ungrammatical or culturally awkward outputs in low-resource settings. — Real-world deployment papers


### Evaluation design (5 rubrics)
- **Scenario validity**: Promoting fair evaluation from technical correction toward compliance-oriented assessment.
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: All perturbations must satisfy the “FairScore” metric—that is, the KL divergence between the model’s output distribution after perturbation and the original output distribution must be below a specified threshold.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• Panda only 3 axes; HolisticBias extends to 13 axes. — Smith 2022 (HolisticBias)
• perturbation may produce ungrammatical or culturally awkward outputs in low-resource settings. — Real-world deployment papers
• Panda is English-only; perturber not transferable. — Jin 2024

## Self-acknowledged limits

Authors flag English-only and 3-axis scope; perturber accuracy ~92%, errors propagate.

## Synthesis

Subsequent work criticizes Panda for covering only three axes (gender, race/ethnicity, and age), whereas HolisticBias extends to 13 axes. Moreover, perturbations may yield ungrammatical or culturally inappropriate outputs in low-resource settings, and Panda is limited to English, with non-transferable perturbers. The authors acknowledge limitations including English-only coverage, restriction to three axes, and perturber accuracy of approximately 92%, with errors propagating.
