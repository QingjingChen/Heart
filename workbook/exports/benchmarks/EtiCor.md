# EtiCor (2023)

**Dimension**: Human centered  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Multi-regional normative scenario template with culture-anchored annotation guidelines

## Tool explanation (full)

Paper: EtiCor constructs ethical evaluation items as culturally grounded scenario-response pairs, explicitly anchored to five distinct regional sociocultural contexts (e.g., East Asia, Sub-Saharan Africa, Latin America). Each scenario is paired with region-specific normative expectations, annotated by local domain experts using standardized guidelines that codify how moral judgments should vary across cultural frameworks—not just translate English prompts. The tool includes a modular template for generating new scenarios: [context] + [actor/stakeholder roles] + [culturally salient conflict] + [region-tagged normative expectation].  
Issue: Cross-regional social norm corpus.  
Score: 4  
— Lineage —  
• Zhong 2025 notes coverage of five regions.  
• Strong_rubric_evidence confirms high scores (4/4) on Construct clarity, Normative grounding, and Context and stakeholder coverage—all tied to its multi-regional design.  
• Source_excerpt mentions “HumaniBench” but does not describe EtiCor; extraction therefore relies entirely on workbook notes and rubric evidence.

## What it improves vs. baseline

Moves beyond monolingual or monocultural benchmarks (e.g., ETHICS, MoralBench) by embedding cultural variation *into the task design itself*, rather than treating culture as post-hoc metadata or translation layer; enables detection of alignment failures specific to regional normative divergence.

## Adaptation example

In the customer service dialogue dataset, replace the original consistency annotation template with EtiCor’s region-anchored template: for the same user complaint scenario (e.g., “delayed refund”), require annotators to generate compliant responses separately according to norms from Japan (emphasizing relationship maintenance and indirectness), Nigeria (emphasizing communal accountability), and Mexico (prioritizing personal dignity and familial impact), and annotate critical deviation points violating local norms.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: EtiCor constructs ethical evaluation items as culturally grounded scenario-response pairs, explicitly anchored to five distinct regional sociocultural contexts (e.g., East Asia, Sub-Saharan Africa, Latin America). Each scenario is paired with region-specific normative expectations, annotated by local domain experts using standardized guidelines that codify how moral judgments should vary across cultural frameworks—not just translate English prompts.
- **Normative grounding**: Each scenario is paired with region-specific normative expectations, annotated by local domain experts using standardized guidelines that codify how moral judgments should vary across cultural frameworks—not just translate English prompts.
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: EtiCor constructs ethical evaluation items as culturally grounded scenario-response pairs, explicitly anchored to five distinct regional sociocultural contexts (e.g., East Asia, Sub-Saharan Africa, Latin America). The tool includes a modular template for generating new scenarios: [context] + [actor/stakeholder roles] + [culturally salient conflict] + [region-tagged normative expectation].
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: The tool includes a modular template for generating new scenarios: [context] + [actor/stakeholder roles] + [culturally salient conflict] + [region-tagged normative expectation].
- **Task-format fit**: Moves beyond monolingual or monocultural benchmarks (e.g., ETHICS, MoralBench) by embedding cultural variation *into the task design itself*, rather than treating culture as post-hoc metadata or translation layer; enables detection of alignment failures specific to regional normative divergence.
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: annotated by local domain experts using standardized guidelines that codify how moral judgments should vary across cultural frameworks—not just translate English prompts.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Synthesis

The review notes that EtiCor targets multiregional ethical/social norm corpora for LLMs, but requires more detailed elaboration and a more complete data card and bias statement.
