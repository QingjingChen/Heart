# MoralChoice (2023)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/12853.txt`

## Representative tool

Ambiguity-stratified moral scenario template with violation tagging

## Tool explanation (full)

MoralChoice proposes a structured scenario template: each entry includes a clear situational description, two mutually exclusive action options, and an explicitly labeled “type of rule violation” (e.g., “violating the principle of honesty”, “violating the principle of non-harm”). Crucially, all scenarios are manually categorized into “high-ambiguity” and “low-ambiguity” classes (687 + 680 instances), based on expert joint assessment of moral conflict intensity, outcome uncertainty, and normative conflict degree—enabling differentiated evaluation of model performance on deterministic versus trade-off-based judgments.

Extraction rationale: Primarily drawn from the Benchmark diagnostic table notes: “1,367 scenarios (687 low-ambiguity + 680 high-ambiguity), human-written and LLM-assisted generation” and “MCQ format, containing description, two possible actions, and rule-violation labels”; although the source_excerpt is brief, it confirms inclusion within the same survey highlighting a novel, “human-centric” and “alignment-focused” evaluation paradigm, and the notes explicitly identify its strengths as “multi-template robustness and high/low ambiguity design”.

## What it improves vs. baseline

Unlike traditional moral multiple-choice questions (MCQs), which focus solely on answer correctness, this template systematically introduces, for the first time, a fuzziness-layering mechanism and violation-attribution labels—enabling evaluation to distinguish between a model’s rule-recognition capability and its value-tradeoff capability, and thereby avoiding equating “correct answer” with “ethical alignment.”

## Adaptation example

In the autonomous driving ethics decision-making simulation dataset, this template can be reused to reconstruct accident scenarios: for example, “whether to swerve and hit pedestrian A (elderly) or pedestrian B (young child),” explicitly labeled as “violating the age-neutrality principle” and “high ambiguity,” with a low-ambiguity control item added (e.g., “whether to obey a red light”), thereby systematically evaluating model behavioral consistency under strong normative constraints versus weak-consensus situations.

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
