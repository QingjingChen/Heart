# CPsyExam (2024)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/10818.txt`

## Representative tool

Standardized exam-based psychological knowledge elicitation protocol

## Tool explanation (full)

This tool structures authentic psychology questions from China’s national standardized examinations (GEE: National College Entrance Examination; PCE: Psychological Counselor Qualification Examination; TQE: Teacher Qualification Examination; SSE: Social Worker Examination) into a dual-track assessment protocol—knowledge-graph-driven single-choice questions (SCQ) and multiple-answer questions (MAQ), alongside short-answer questions (QA). Each question is annotated with its corresponding psychological theory level (e.g., Bloom’s Taxonomy of Cognitive Objectives: Remember/Understand/Apply), knowledge type (e.g., Jung’s personality structure), and implicit humanistic value anchors (e.g., empathy, autonomy, developmental orientation). The protocol adopts a four-tuple schema: stem–options–standard answer–theoretical source, and supports dynamic sampling by examination type, difficulty coefficient, and humanistic sub-construct tags.

Extraction rationale: Primarily based on notes in the Benchmark diagnostic table: workbook_dataset_note explicitly states “sourced from China’s examination systems (GEE, PCE, TQE, SSE)” and provides concrete examples (e.g., Jung’s four elements of personality); strong_rubric_evidence indicates a Task-format fit score of 4, with the note “task format: MCQ (SCQ, MAQ) and QA”; Construct clarity scores 3, with the note “assesses psychological knowledge (KG) and case analysis (CA), citing Bloom’s Taxonomy”—collectively indicating that the core tool is a structured reuse protocol for examination item banks; source_excerpt contains only a review title, with no CPsyExam-specific details, thus inference relies entirely on the notes.

## What it improves vs. baseline

Compared to general psychological commonsense QA datasets (e.g., PsychQA), this protocol is the first to directly adapt high-reliability-and-validity items from established educational assessment systems as LLM human-centered capability diagnostic tools, avoiding construct drift introduced by manual item authoring while strengthening normative grounding through the authority of standardized testing.

## Adaptation example

In an AI-based employment counseling system for persons with disabilities, this protocol can be adapted: extract authentic questions from the PCE examination on “Vocational Rehabilitation Psychology” (e.g., “Evidence-based intervention strategies for job-search anxiety among individuals with physical disabilities”), convert them into role-playing tasks (e.g., “As a vocational counselor, how would you respond to a job seeker who was rejected for employment due to a spinal cord injury?”), and mandate that the model’s output explicitly cite three evidence-based strategies from the official PCE answer key—thereby evaluating both its knowledge accuracy and consistency with human-centered responsiveness.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Each question is annotated with the corresponding psychological theory level (e.g., Bloom’s Taxonomy: Remember/Understand/Apply), knowledge type (e.g., Jung’s personality structure), and implicit humanistic value anchor (e.g., empathy, autonomy, developmental orientation).  
— Lineage —  
• exam knowledge ≠ empathic interaction; CPsyExam tests knowledge recall not crisis response. — HeartBench (2025)  
— External Perspective (Survey) —  
• CPsyExam [Zhao et al., 2024] integrates 22,000 questions from Chinese professional psychology examinations to build a dual evaluation framework covering both knowledge retrieval and case-based reasoning.
- **Normative grounding**: Strengthening normative grounding through examination authority.
- **Source provenance and evidence fitness**: This tool structures authentic psychology examination questions from China’s national standardized tests (GEE: National College Entrance Examination; PCE: Psychological Counselor Qualification Examination; TQE: Teacher Qualification Examination; SSE: Social Worker Examination) into a knowledge-graph-driven dual-track assessment protocol comprising multiple-choice questions (SCQ/MAQ) and short-answer questions (QA).  
— Survey —  
• CPsyExam [Zhao et al., 2024] integrates 22,000 questions from Chinese professional psychology examinations to build a dual evaluation framework covering both knowledge retrieval and case-based reasoning.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: — Lineage —  
• Exam format doesn't capture clinical decision-making nuance. — VITAL (2025)
- **Task-format fit**: The protocol comprises a four-tuple schema: stem–options–correct answer–theoretical source, and supports dynamic sampling by examination type, difficulty coefficient, and human-centered sub-construct tags.  
— Lineage —  
• single-turn QA; lacks supportive dialogue. — SMILE (2024)  
— External Perspective (Survey) —  
• CPsyExam [Zhao et al., 2024] integrates 22,000 questions from Chinese professional psychology examinations to build a dual evaluation framework covering both knowledge retrieval and case-based reasoning.
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• exam knowledge ≠ empathic interaction; CPsyExam tests knowledge recall not crisis response. — HeartBench (2025)
• single-turn QA; lacks supportive dialogue. — SMILE (2024)
• exam format doesn't capture clinical decision-making nuance. — VITAL (2025)

## Self-acknowledged limits

Authors note exam-knowledge limitation; doesn't test clinical empathy or crisis intervention.

## External views (survey)

• CPsyExam [Zhao et al., 2024] integrates 22,000 questions from Chinese professional psychology examinations to build a dual evaluation framework covering both knowledge retrieval and case-based reasoning. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The review states that CPsyExam constructs a dual evaluation framework for knowledge retrieval and case-based reasoning by integrating 22,000 questions. Subsequent work criticizes it for primarily testing knowledge recall rather than crisis response, and for lacking the nuances of supportive dialogue and clinical decision-making. The authors acknowledge its limitations in not assessing clinical empathy or crisis intervention.
