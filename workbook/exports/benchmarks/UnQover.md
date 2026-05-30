# UnQover (2020)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/11163.txt`

## Representative tool

Underspecified Question (UQ) template with counterfactual answer inversion

## Tool explanation (full)

UQ template constructs ambiguous questions (e.g., “Who was an entrepreneur?”) by deliberately omitting key attributes (e.g., gender, race), forcing models to rely on stereotypical associations for answers; it then generates counterfactual answer pairs (e.g., if the original annotation is “Gerald”, the counterfactual annotation is “Jennifer”) via human annotation or expert validation, and computes the model’s prediction distribution shift (γ) and consistency drop rate (η) between original and counterfactual options. This tool relies on expert-designed passage–question–option triples, with its core innovation lying in leveraging semantic underspecification to expose implicit bias—not through explicit sensitive terms.

Extraction basis: The source_excerpt title “UNQOVERing Stereotyping Biases via Underspecified Questions” directly names this tool; the in-text example “Who was an entrepreneur?” paired with the passage “The person over the swing is Angela. Sitting by the side is Patrick.” illustrates typical underspecification; the workbook_dataset_note emphasizes “expert-designed” and “MCQ-QA” format; and strong_rubric_evidence’s Task-format fit score of 4 further corroborates that this template constitutes its methodological core.

## What it improves vs. baseline

Unlike traditional bias QA datasets (e.g., BOLD or StereoSet), which rely on explicit bias statements or unidimensional prompts, UQ systematically removes referential information to force models to expose their default assumptions, thereby more realistically simulating discriminatory attribution in real-world QA scenarios caused by missing information.

## Adaptation example

In the legal consultation QA dataset, append the ambiguous question “Who initiated the negotiation?” to case descriptions (e.g., “The defendant signed the contract under duress.”), manually construct gender/age counterfactual answer pairs (e.g., original label “plaintiff” → counterfactual “elderly plaintiff”), and re-annotate using the UQ template to drive model recognition of systematic underestimation of agency for vulnerable groups.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: The UQ template deliberately omits key attributes (e.g., gender, race) to construct ambiguous questions (e.g., “Who was an entrepreneur?”), forcing the model to rely on stereotypical associations for answers; it then generates counterfactual answer pairs (e.g., if the original annotation for a given passage is “Gerald,” the counterfactual annotation is “Jennifer”) via human annotation or expert validation, and computes the model’s predictive distribution shift (γ) and consistency drop rate (η) between original and counterfactual options. This tool relies on expert-designed passage–question–option triples, with its core innovation lying in leveraging semantic underspecification to expose implicit bias—not relying on explicit sensitive terms as triggers.  
— Lineage —  
• UnQover's reversal control is good but ambiguous-context Qs lack a 'correct' answer; only measures relative preference, not absolute harm. — Parrish 2022 (BBQ)
- **Normative grounding**: —
- **Source provenance and evidence fitness**: — Lineage —  
• English-only; protected-class taxonomy follows US categories. — Jin 2024 (KoBBQ) & Huang 2024 (CBBQ)
- **Context and stakeholder coverage**: — Lineage —  
• English-only; protected-class taxonomy follows US categories. — Jin 2024 (KoBBQ) & Huang 2024 (CBBQ)
- **Real-world harm linkage**: — Lineage —  
• UnQover's reversal control is good but ambiguous-context questions lack a "correct" answer; they only measure relative preference, not absolute harm. — Parrish 2022 (BBQ)


### Evaluation design (5 rubrics)
- **Scenario validity**: Compared to traditional bias QA datasets (e.g., BOLD or StereoSet), which rely on explicit bias statements or unidimensional prompts, UQ systematically removes referential information to force models to expose their default assumptions—thereby more realistically simulating discriminatory attribution in real-world QA arising from missing information.  
— Lineage —  
• UnQover's reversal control is good but ambiguous-context Qs lack a 'correct' answer; only measures relative preference, not absolute harm. — Parrish 2022 (BBQ)
- **Task-format fit**: The UQ template deliberately omits key attributes (e.g., gender, race) to construct ambiguous questions (e.g., “Who was an entrepreneur?”), thereby forcing models to rely on stereotypical associations for answers. Counterfactual answer pairs are then generated via human annotation or expert validation (e.g., if the original annotation for a given passage is “Gerald,” the counterfactual annotation is “Jennifer”), and the model’s prediction distribution shift (γ) and consistency drop rate (η) between original and counterfactual options are computed. This tool relies on expert-designed passage–question–option triples, with its core innovation lying in leveraging semantic underspecification to expose implicit bias, rather than depending on explicit sensitive terms as triggers.
- **Ground truth and disagreement design**: Then generate counterfactual answer pairs via manual annotation or expert validation (e.g., within the same passage, if the original annotation is 'Gerald', the counterfactual annotation is 'Jennifer').  
— Lineage —  
• UnQover's reversal control is good but ambiguous-context Qs lack a 'correct' answer; only measures relative preference, not absolute harm. — Parrish 2022 (BBQ)
- **Metric validity**: and compute the model’s predictive distribution shift (γ) and consistency drop rate (η) between original vs. counterfactual options.  
— Lineage —  
• UnQover's reversal control is good but ambiguous-context Qs lack a 'correct' answer; only measures relative preference, not absolute harm. — Parrish 2022 (BBQ)
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Counterfactual answer pairs are then generated via human annotation or expert validation (e.g., for the same passage, if the original annotation is “Gerald,” the counterfactual annotation is “Jennifer”).
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• UnQover's reversal control is good but ambiguous-context Qs lack a 'correct' answer; only measures relative preference, not absolute harm. — Parrish 2022 (BBQ)
• English-only; protected-class taxonomy follows US categories. — Jin 2024 (KoBBQ) & Huang 2024 (CBBQ)
• 4 axes is too few. — Smith 2022 (HolisticBias)

## Self-acknowledged limits

"Synthetic templates; subject-name based stereotypes; English."

## Synthesis

Subsequent work criticizes UnQover’s counterfactual control as effective yet insufficient for ambiguous-context questions, which lack ground-truth answers and thus measure only relative preferences rather than absolute harm. The framework is English-only and its classification relies on U.S.-centric standards; its four axes are deemed too few. Self-acknowledged limitations include synthetic templates, stereotypes derived solely from topic names, and English-only scope.
