# FLEX (2025)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/survey_texts/gu_survey_2025.txt`

## Representative tool

Adversarial Fairness Sensitivity Probe (AFSP)

## Tool explanation (full)

AFSP is an adversarial perturbation detection tool designed to assess robustness of fairness-related behavior: it applies semantically preserving yet attribute-highlighting or attribute-attenuating minor perturbations (e.g., pronoun substitution, kinship term adjustment, modification of occupational descriptor adjectives) to original fairness-sensitive prompts (e.g., decision-making scenarios involving protected attributes), and systematically measures inconsistency in model outputs on fairness-relevant judgments (e.g., whether to recommend a certain job, whether to deem a behavior reasonable). The tool relies on a manually constructed lexicon of protected-attribute anchor terms and a rule set for perturbations, integrated within a counterfactual comparative evaluation framework, specifically engineered to expose “fragile fairness”—a limitation that static fairness benchmarks fail to capture.

Extraction rationale: Primarily based on notes in the Benchmark Diagnostic Table: “Type: fairness adversarial sensitivity benchmark; comprehensive survey concludes it fills the gap left by static fairness benchmarks, which cannot detect vulnerability to small perturbations”; all three high-scoring items in strong_rubric_evidence point explicitly to “testing model fairness behavior robustness via minor adversarial changes”, and are clearly linked to the construct, scenario, and task-format dimensions.

## What it improves vs. baseline

In contrast to traditional static fairness benchmarks (e.g., those assessing group-wise accuracy disparity using fixed templates), AFSP is the first to advance fairness evaluation from “outcome bias detection” to “behavioral robustness diagnosis,” enabling identification of models that appear fair on the surface but fail under minor perturbations—thereby filling a critical gap in evaluating adversarial sensitivity.

## Adaptation example

In a medical consultation dialogue dataset, AFSP is applied to perturb physician recommendation responses (e.g., changing “this elderly female patient” to “this senior lady” or “this 65-year-old woman”) to measure the degree of decline in referral recommendation consistency across varying age/gender formulations, thereby diagnosing the adversarial fragility of the model’s clinical decision fairness.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: AFSP is an adversarial perturbation detection tool targeting robustness of fairness-related behavior: it applies small, semantics-preserving perturbations—such as pronoun substitution, kinship term adjustment, or modification of occupational descriptor adjectives—that either highlight or obscure protected attributes, atop original fairness-sensitive prompts (e.g., decision-making scenarios involving protected attributes), and systematically measures inconsistency in model outputs on fairness-related judgments (e.g., whether to recommend a job position, whether to deem a behavior reasonable).  
— External Perspective (Survey) —  
• “Survey Section 425: FLEX adds something new by testing how models behave under small adversarial changes, revealing weaknesses that static benchmarks cannot detect.”
- **Normative grounding**: —
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: This tool relies on manually constructed lexicons of protected attributes and perturbation rule sets, integrated with a counterfactual comparative evaluation framework, specifically designed to expose “fragile fairness”—a phenomenon static fairness benchmarks fail to capture.  
— External Perspective (Survey) —  
• “Survey Section 425: FLEX adds something new by testing how models behave under small adversarial changes, revealing weaknesses that static benchmarks cannot detect.”
- **Task-format fit**: Compared with traditional static fairness benchmarks (e.g., those testing group-wise accuracy disparity using only fixed templates), AFSP pioneers the advancement of fairness evaluation from “outcome bias detection” to “behavioral robustness diagnosis”, enabling identification of models that appear fair on the surface but fail immediately under slight perturbations—thereby filling the assessment gap regarding adversarial sensitivity.  
— Lineage —  
• “Survey Section 425: FLEX adds something new by testing how models behave under small adversarial changes, revealing weaknesses that static benchmarks cannot detect.”
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• “Survey Section 425: FLEX adds something new by testing how models behave under small adversarial changes, revealing weaknesses that static benchmarks cannot detect.”

## Synthesis

The review states that FLEX reveals weaknesses undetectable by static benchmarks by testing model behavior under minor adversarial perturbations.
