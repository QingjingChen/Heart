# SCRUPLES (2021)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/12942.txt`

## Representative tool

Community-sourced real-life anecdote corpus with multi-stakeholder moral judgment labels (AUTHOR/OTHER/EVERYBODY/NOBODY/INFO)

## Tool explanation (full)

SCRUPLES curates 32,000 real-world anecdotes scraped from Reddit’s r/AmItheAsshole, each annotated with over 19 aggregated community judgments per post, mapped to five stakeholder-aligned categories: AUTHOR (judgment about the poster), OTHER (about the other person involved), EVERYBODY (universal condemnation/praise), NOBODY (no one at fault), and INFO (insufficient information). This transforms noisy crowd votes into a structured, role-aware ethical labeling schema — preserving ambiguity and pluralism rather than forcing binary right/wrong classification.

Extraction basis: The workbook_dataset_note explicitly states its source as “Reddit AmItheAsshole”, scale as “32,000 anecdotes, 625,000 moral judgments”, and lists the five label categories (AUTHOR/OTHER/EVERYBODY/NOBODY/INFO); the source_excerpt summary emphasizes that it “focuses on people’s descriptive judgments rather than theoretical prescriptions”; in strong_rubric_evidence, the Construct clarity criterion confirms “measures moral judgment” and enumerates this five-dimensional label system, while Scenario validity underscores “real-life anecdotes” involving stakeholder roles.

## What it improves vs. baseline

Shifts from artificial, decontextualized dilemmas (e.g., trolley variants) to naturally occurring, linguistically rich, multi-party social conflicts — and crucially, retains judgment heterogeneity as signal rather than noise, enabling evaluation of whether models recognize legitimate moral disagreement and stakeholder-positioned reasoning.

## Adaptation example

In the online education platform teacher-student interaction log dataset, this tool is reusable: crawl authentic discussion threads titled “Was I unfair grading this student?” from teacher forums; extract pedagogical context anecdotes; and invite multi-role annotation (STUDENT/TEACHER/ADMIN/PARENT/INFO) to construct a multi-perspective benchmark for educational fairness judgment—designed to evaluate AI teaching assistants’ ethical sensitivity in power-asymmetry scenarios.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: SCRUPLES curates 32,000 real-world anecdotes scraped from Reddit’s r/AmItheAsshole, each annotated with over 19 aggregated community judgments per post, mapped to five stakeholder-aligned categories: AUTHOR (judgment about the poster), OTHER (about the other person involved), EVERYBODY (universal condemnation/praise), NOBODY (no one at fault), and INFO (insufficient information). This transforms noisy crowd votes into a structured, role-aware ethical labeling schema — preserving ambiguity and pluralism rather than forcing binary right/wrong classification.  
— External perspective (Survey) —  
• The SCRUPLES [lou,] dataset comprises two core components: DILEMMAS (simple moral value rankings of action pairs) and complex real-life anecdotes extracted from Reddit. The task requires models to judge “who is in the wrong”. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Normative grounding**: —
- **Source provenance and evidence fitness**: SCRUPLES curates 32,000 real-world anecdotes scraped from Reddit’s r/AmItheAsshole, each annotated with over 19 aggregated community judgments per post, mapped to five stakeholder-aligned categories: AUTHOR (judgment about the poster), OTHER (about the other person involved), EVERYBODY (universal condemnation/praise), NOBODY (no one at fault), and INFO (insufficient information).  
— Lineage —  
• English-only Reddit demographic skew. — CMoralEval (2024)  
— External perspective (Survey) —  
• The SCRUPLES [lou,] dataset comprises two core components: DILEMMAS (simple moral value rankings of action pairs) and complex real-life anecdotes extracted from Reddit. The task requires models to judge 'who is in the wrong'. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Context and stakeholder coverage**: mapped to five stakeholder-aligned categories: AUTHOR (judgment about the poster), OTHER (about the other person involved), EVERYBODY (universal condemnation/praise), NOBODY (no one at fault), and INFO (insufficient information).
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Shifts from artificial, decontextualized dilemmas (e.g., trolley variants) to naturally occurring, linguistically rich, multi-party social conflicts—and crucially, retains judgment heterogeneity as signal rather than noise, enabling evaluation of whether models recognize legitimate moral disagreement and stakeholder-positioned reasoning.  
— External Perspective (Survey) —  
• The SCRUPLES [lou,] dataset comprises two core components: DILEMMAS (simple moral value rankings of action pairs) and complex real-life anecdotes extracted from Reddit. The task requires models to judge “who is in the wrong”. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Task-format fit**: —
- **Ground truth and disagreement design**: This transforms noisy crowd votes into a structured, role-aware ethical labeling schema — preserving ambiguity and pluralism rather than forcing binary right/wrong classification.
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• outcome-only; doesn't model procedural reasoning. — MoReBench (2025)
• English-only Reddit demographic skew. — CMoralEval (2024)
• lacks healthcare/professional alignment context. — VITAL/HumaniBench

## Self-acknowledged limits

Authors flag Reddit demographic skew (young Western); community verdicts noisy; binary labels suppress moral pluralism.

## External views (survey)

• The SCRUPLES [lou,] dataset comprises two core components: DILEMMAS (simple moral value rankings of action pairs) and complex real-life anecdotes extracted from Reddit. The task requires models to judge 'who is in the wrong'. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The survey notes that the SCRUPLES dataset comprises two core components: DILEMMAS and complex, real-life anecdotes extracted from Reddit. Subsequent work criticizes it for focusing solely on outcomes, lacking procedural reasoning, and exhibiting English-language and Reddit demographic biases. The authors acknowledge limitations including Reddit demographic bias (young, Western), noisy community judgments, and binary labels that suppress moral pluralism.
