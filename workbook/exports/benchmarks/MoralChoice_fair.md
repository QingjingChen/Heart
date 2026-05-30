# MoralChoice (2023)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts_hc/12853.txt`

## Representative tool

Multi-Prompt Consistency Scoring Framework (MPCS)

## Tool explanation (full)

This tool elicits LLM outputs under the same ethical scenario using three standardized prompt templates (“ab” binary choice, “compare” comparative statement, and “repeat” confirmation repetition), and computes consistency metrics for action selection: Action Likelihood, Marginal Action Likelihood, and Question Format Consistency (QF-C). It relies on 1,767 high-/low-ambiguity ethical scenarios generated collaboratively by experts and LLMs to force models to expose their decision stability.  
Extraction basis: Primarily drawn from the Benchmark diagnostic table notes, which explicitly state the use of three prompt templates, 1,767 scenarios × 28 model sizes, and the definition of specific metrics including Action Likelihood; in strong_rubric_evidence, both Metric validity and Task-format fit received scores of 4, confirming the framework’s innovation in metric design and task alignment.

## What it improves vs. baseline

Breaks through the traditional single-prompt, single-answer multiple-choice question (MCQ) evaluation paradigm by operationalizing “moral judgment reliability” as response robustness across diverse prompt formats, thereby distinguishing surface-level compliance from deep value alignment and preventing models from “cheating” via memorization of fixed patterns.

## Adaptation example

In the medical AI consultation dialogue dataset, three types of user query formulations—ab, comparison, and repeat—are constructed for the same clinical ethical dilemma (e.g., “whether to withhold diagnosis from a terminally ill patient”); the probability consistency of model recommendations (“disclose” vs. “withhold”) is computed to identify value drift risk across different interaction formats.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Each entry includes a clear scenario description, two mutually exclusive action options, and an explicit label indicating the “type of rule violation” (e.g., “violating the principle of honesty”, “violating the principle of non-maleficence”). Crucially, all scenarios are manually categorized into “high ambiguity” and “low ambiguity” classes (687 + 680 instances), based on expert joint assessment of moral conflict intensity, outcome uncertainty, and normative conflict degree.
- **Normative grounding**: — Lineage —  
• English; Western moral intuitions. — CMoralEval (2024)
- **Source provenance and evidence fitness**: 1,367 scenarios (687 low ambiguity + 680 high ambiguity), manually written and LLM-assisted generation  
— Lineage —  
• MFQ axes used externally without psychometric calibration. — MFT-2 (2023)
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: All scenarios were manually categorized into “high ambiguity” and “low ambiguity” classes (687 + 680 scenarios), based on expert joint assessment of moral conflict intensity, outcome uncertainty, and normative conflict severity, enabling differential evaluation of model performance on deterministic versus trade-off-based judgments.  
— Lineage —  
• outcome-only choice; no procedural reasoning chain. — MoReBench (2025)
- **Task-format fit**: Multiple-choice question (MCQ) format, comprising a scenario description, two possible actions, and a violation label indicating which ethical or regulatory rule is breached.
- **Ground truth and disagreement design**: All scenarios were manually categorized into “high ambiguity” and “low ambiguity” classes (687 + 680 instances), based on expert joint assessment of moral conflict intensity, outcome uncertainty, and normative conflict degree.
- **Metric validity**: In contrast to traditional moral multiple-choice question (MCQ) benchmarks that focus solely on answer correctness, this template systematically introduces, for the first time, a fuzziness stratification mechanism and violation attribution labels—enabling evaluation to distinguish between a model’s rule recognition capability and its value trade-off capability, thereby avoiding the conflation of “answering correctly” with “ethical alignment.”
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: All scenarios were manually categorized into “high ambiguity” and “low ambiguity” classes (687 + 680 instances), based on expert joint assessment of moral conflict intensity, outcome uncertainty, and normative conflict degree.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: Primarily based on the Benchmark Diagnostic Table notes: “1,367 scenarios (687 low-ambiguity + 680 high-ambiguity), manually written and LLM-assisted generation” and “Multiple-choice question (MCQ) format, including scenario description, two possible actions, and violation-label tags.”
- **Maintenance and update governance**: —

## Lineage critiques

• outcome-only choice; no procedural reasoning chain. — MoReBench (2025)
• English; Western moral intuitions. — CMoralEval (2024)
• MFQ axes used externally without psychometric calibration. — MFT-2 (2023)

## Self-acknowledged limits

Authors flag English; rule labels Western canonical; high-ambiguity items lack ground-truth.

## Synthesis

Subsequent work criticizes MoralChoice for relying solely on outcome-based selection, lacking procedural reasoning chains (MoReBench, 2025), and being restricted to English and Western moral intuitions (CMoralEval, 2024). The authors acknowledge limitations including the English-only dataset, rule labels grounded in Western norms, and the absence of ground truth for highly ambiguous items.
