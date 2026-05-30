# Phare (2025)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Discrimination-Generation Gap Analyzer (DGGA)

## Tool explanation (full)

DGGA is a dual-track fairness disparity quantification tool: under the same semantic premise, it simultaneously constructs discriminative tasks (e.g., MCQs such as “Who is more qualified to be a teacher?”) and open-ended generation tasks (e.g., “Please describe the traits of an excellent teacher”), then computes the systematic gap between the two on bias metrics (e.g., gender-occupation co-occurrence strength, stereotypical word frequency ratio, group representativeness entropy). The tool relies on paired prompt templates, controllable semantic anchoring sentences (e.g., “Teacher Zhang and Teacher Li both teach mathematics”), and an automated bias-scoring pipeline for LLM-generated content (including fine-grained entity-attribute relation extraction).

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: “Type: generation-discrimination gap fairness benchmark; comprehensive survey notes that models appearing unbiased in MCQs may still replicate stereotypes in open-ended generation”; in strong_rubric_evidence, Task-format fit scores 5, explicitly emphasizing “dual-track (discriminative + generative) alignment with risk mechanisms”, and Real-world harm linkage scores 4, pointing to “linking actual representational harms in generative outputs”.

## What it improves vs. baseline

In contrast to traditional fairness benchmarks that rely solely on discriminative tasks (e.g., BBQ, Winogender), DGGA reveals the critical disconnect that “discriminative fairness ≠ generative harmlessness,” advancing evaluation from a single-task paradigm to cross-format risk mapping and, for the first time, quantifying the amplification effect of implicit stereotypes in generative outputs.

## Adaptation example

In the resume screening dataset, DGGA is used to simultaneously submit both an MCQ scoring task (“Is this candidate suitable for a technical position? A. Yes B. No”) and an open-ended generation task (“Please summarize the candidate’s core strengths in three sentences”) for the same resume to the model. The analysis focuses on implicit cultural bias in the generated text—specifically, differential evaluative language associated with names signaling cultural background (e.g., more frequent use of “strong communication skills” rather than “solid algorithmic foundations” for resumes bearing the name “Mohammed”)—to identify risk points where classification accuracy remains high but generative outputs exhibit imbalance.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: DGGA is a dual-track fairness disparity quantification tool: under the same semantic premise, it simultaneously constructs discriminative tasks (e.g., MCQs such as “Who is more qualified to be a teacher?”) and open-generation tasks (e.g., “Please describe the traits of an excellent teacher”), and computes the systematic gap between them on bias metrics (e.g., gender–occupation co-occurrence strength, stereotypical word frequency ratio, group representativeness entropy).  
— Survey —  
• “Survey paragraph 025: New frameworks such as Phare (generation–discrimination gap) and FLEX (adversarial sensitivity) further show that traditional QA benchmarks miss important types of harm.”
- **Normative grounding**: —
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: This tool relies on paired prompt templates, controllable semantic anchor sentences (e.g., “Teacher Zhang and Teacher Li both teach mathematics”), and an automated bias-scoring pipeline based on LLM-generated content (including fine-grained entity–attribute relation extraction).  
— External Perspective (Survey) —  
• “Survey Section 025: New frameworks such as Phare (generation–discrimination gap) and FLEX (adversarial sensitivity) further show that traditional QA benchmarks miss important types of harm.”


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: Compared to traditional fairness benchmarks that rely solely on discriminative tasks (e.g., BBQ, Winogender), DGGA reveals the critical rupture that “discriminative fairness ≠ generative harmlessness”, advancing evaluation from a single-task paradigm to cross-format risk mapping and, for the first time, quantifying the amplification effect of implicit stereotypes in generative outputs.  
— Survey —  
• “Survey paragraph 025: New frameworks such as Phare (generation–discrimination gap) and FLEX (adversarial sensitivity) further show that traditional QA benchmarks miss important types of harm.”
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• Survey Section 025: New frameworks such as Phare (generation–discrimination gap) and FLEX (adversarial sensitivity) further show that traditional QA benchmarks miss important types of harm.

## Synthesis

The review notes that new frameworks such as Phare (generation-discrimination gap) indicate that traditional QA benchmarks overlook important types of harm.
