# HeartBench (2025)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/12782.txt`

## Representative tool

Five-dimensional anthropomorphic intelligence framework with case-specific rubric generation (personality/emotion/social/moral/motivational axes)

## Tool explanation (full)

Paper: HeartBench defines anthropomorphic intelligence via five theoretically grounded dimensions—Personality, Emotion, Sociality, Morality, Motivation—each decomposed into 3 sub-capabilities (total 15), and generates *case-specific scoring rubrics* for each of its 2,818 dialogue cases. For example, a grief-support dialogue triggers rubrics evaluating 'moral boundary awareness' (e.g., avoiding premature advice) and 'motivational scaffolding' (e.g., co-constructing agency), derived from clinical psychology and cultural anthropology literature. Rubrics are not static templates but dynamically instantiated per scenario.  
Issue: Construct clarity  
Score: 4  
— Lineage —  
• Based on psychological and anthropological theoretical frameworks, defines five primary dimensions (Personality, Emotion, Sociality, Morality, Motivation) and 15 sub-capabilities.

## What it improves vs. baseline

Replaces monolithic 'empathy score' metrics with modular, theory-driven, and scenario-contingent evaluation axes—enabling fine-grained diagnosis of *where* and *why* anthropomorphic failures occur (e.g., high emotion recognition but low moral boundary adherence), unlike holistic benchmarks like EmpatheticDialogues.

## Adaptation example

In the Elderly Companion Robot User Interaction Log Dataset, this five-dimensional framework can be applied to automatically generate a customized rubric for the case of “elderly individuals living alone concealing their history of falls”: “Sociality → Relational Trust Maintenance” (whether questioning-style probing is avoided), “Morality → Autonomy Respect” (whether autonomous decision-making is supported rather than overridden), and “Motivation → Goal Co-construction” (whether gradual rehabilitation goals are collaboratively formulated), thereby enabling culturally adaptive, capability-oriented assessment of elderly care.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: — External Perspective (Survey) —  
• HeartBench [Liu et al., 2025a] is an evaluation framework that targets the limitations of large language models in anthropomorphic intelligence. Grounded in the Chinese cultural context, it draws on real psychological counseling scenarios and collaborates with clinical experts. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Normative grounding**: — External Perspective (Survey) —  
• Grounded in the Chinese cultural context, it draws on real psychological counseling scenarios and collaborates with clinical experts. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Source provenance and evidence fitness**: Rubrics are not static templates but dynamically instantiated per scenario.
- **Context and stakeholder coverage**: — External Perspective (Survey) —  
• Grounded in the Chinese cultural context, it draws on real psychological counseling scenarios and collaborates with clinical experts. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Replaces monolithic 'empathy score' metrics with modular, theory-driven, and scenario-contingent evaluation axes—enabling fine-grained diagnosis of *where* and *why* anthropomorphic failures occur (e.g., high emotion recognition but low moral boundary adherence), unlike holistic benchmarks like EmpatheticDialogues.  
— Lineage —  
• empathy benchmarks tend toward outcome scoring; HeartBench tries to address this but procedural eval still incomplete. — MoReBench (2025)
- **Task-format fit**: Replaces monolithic 'empathy score' metrics with modular, theory-driven, and scenario-contingent evaluation axes—enabling fine-grained diagnosis of *where* and *why* anthropomorphic failures occur (e.g., high emotion recognition but low moral boundary adherence), unlike holistic benchmarks like EmpatheticDialogues.
- **Ground truth and disagreement design**: —
- **Metric validity**: Replaces monolithic 'empathy score' metrics with modular, theory-driven, and scenario-contingent evaluation axes—enabling fine-grained diagnosis of *where* and *why* anthropomorphic failures occur (e.g., high emotion recognition but low moral boundary adherence), unlike holistic benchmarks like EmpatheticDialogues.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: Rubrics are not static templates but dynamically instantiated per scenario.
- **Maintenance and update governance**: —

## Lineage critiques

• empathy benchmarks tend toward outcome scoring; HeartBench tries to address this but procedural eval still incomplete. — MoReBench (2025)
• HeartBench richer than knowledge tests but smaller scale. — CPsyExam-style

## Self-acknowledged limits

Authors flag English; new benchmark, lacking longitudinal validation against human therapy outcomes.

## External views (survey)

• HeartBench [Liu et al., 2025a] is an evaluation framework that targets the limitations of large language models in anthropomorphic intelligence. Grounded in the Chinese cultural context, it draws on real psychological counseling scenarios and collaborates with clinical experts. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The review states that HeartBench is an evaluation framework grounded in Chinese cultural context, targeting the limitations of large language models in anthropomorphic intelligence. Subsequent work criticizes its process evaluation as still incomplete and small-scale. The authors acknowledge the lack of longitudinal validation and an English version.
