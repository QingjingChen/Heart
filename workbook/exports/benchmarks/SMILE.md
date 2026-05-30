# SMILE (2024)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/12981.txt`

## Representative tool

Role-structured multi-turn dialogue protocol with dual-role annotation schema (supporter/help-seeker)

## Tool explanation (full)

SMILE introduces a fixed two-role, multi-turn dialogue protocol where every interaction is explicitly annotated with distinct supporter (e.g., mental health counselor) and help-seeker (e.g., distressed user) roles. Each dialogue is constructed to simulate authentic therapeutic support sequences, grounded in clinical micro-skills (e.g., reflection, validation, open-ended inquiry), and requires models to maintain role fidelity, empathic consistency, and contextual memory across turns. It relies on ChatGPT-generated but expert-curated dialogues, filtered and refined using criteria from counseling best practices.  

Extraction basis: Primarily based on the Benchmark diagnostic table notes: “Type: Multi-turn mental health support dialogue dataset”, “Contains help-seeker and supporter roles”, “Average 5.7 turns”, combined with Scenario validity and Task-format fit both scoring 4 in strong_rubric_evidence—indicating that this dual-role, multi-turn structure constitutes its core design strength; source_excerpt provides no details and is therefore not relied upon.

## What it improves vs. baseline

Moves beyond single-turn safety or toxicity checks by enforcing longitudinal human-centered reasoning: models must demonstrate adaptive, context-sensitive, and role-aware support behavior—not just static harm avoidance. Introduces structural constraints (role assignment, turn depth, intent continuity) absent in generic dialogue benchmarks like ToxiGen or BBQ.

## Adaptation example

In the real-call transcription dataset of campus psychological hotlines, this dual-role protocol can be reused to perform structured re-annotation of the original dialogues (explicitly labeling each turn’s speaker as “student seeker” or “counselor supporter”) and to insert standardized empathy assessment points (e.g., Turn 3 must contain an emotion-confirmation statement), thereby constructing a fine-grained diagnostic subset targeting adolescent psychological support capability.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: SMILE introduces a fixed two-role, multi-turn dialogue protocol where every interaction is explicitly annotated with distinct supporter (e.g., mental health counselor) and help-seeker (e.g., distressed user) roles. Each dialogue is constructed to simulate authentic therapeutic support sequences, grounded in clinical micro-skills (e.g., reflection, validation, open-ended inquiry), and requires models to maintain role fidelity, empathic consistency, and contextual memory across turns.  
— Lineage —  
• role-specific (mental health); not generalizable. — Educator-LLM (2025)  
— External perspective (Survey) —  
• SMILE [Qiu et al., 2024] introduces an innovative data-augmentation strategy that uses ChatGPT to convert privacy-restricted single-turn counseling data into high-quality multi-turn dialogues. The project builds a
- **Normative grounding**: — Lineage —  
• not specifically aligned with clinical guidelines. — VITAL (2025)
- **Source provenance and evidence fitness**: It relies on ChatGPT-generated but expert-curated dialogues, filtered and refined using criteria from counseling best practices.
- **Context and stakeholder coverage**: Each dialogue is constructed to simulate authentic therapeutic support sequences, grounded in clinical micro-skills (e.g., reflection, validation, open-ended inquiry), and requires models to maintain role fidelity, empathic consistency, and contextual memory across turns.
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Each dialogue is constructed to simulate authentic therapeutic support sequences, grounded in clinical micro-skills (e.g., reflection, validation, open-ended inquiry), and requires models to maintain role fidelity, empathic consistency, and contextual memory across turns.
- **Task-format fit**: SMILE introduces a fixed two-role, multi-turn dialogue protocol where every interaction is explicitly annotated with distinct supporter (e.g., mental health counselor) and help-seeker (e.g., distressed user) roles. Each dialogue is constructed to simulate authentic therapeutic support sequences, grounded in clinical micro-skills (e.g., reflection, validation, open-ended inquiry), and requires models to maintain role fidelity, empathic consistency, and contextual memory across turns.
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: It relies on ChatGPT-generated but expert-curated dialogues, filtered and refined using criteria from counseling best practices.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• focuses on supportive language not on professional boundary / referral. — HeartBench (2025)
• not specifically aligned with clinical guidelines. — VITAL (2025)
• role-specific (mental health); not generalizable. — Educator-LLM (2025)

## Self-acknowledged limits

Authors note ChatGPT-generated dialogues may amplify model bias; Chinese only; no expert-validated clinical pathways.

## External views (survey)

• SMILE [Qiu et al., 2024]introduces an innovative data-augmentation strategy that uses ChatGPT to convert privacy-restricted single-turn counseling data into high-quality multi-turn dialogues. The project builds a

## Synthesis

The review notes that SMILE introduces an innovative data augmentation strategy, using ChatGPT to convert privacy-constrained single-turn counseling data into high-quality multi-turn dialogues. Subsequent work criticizes its focus on supportive language rather than professional boundaries/referrals, its lack of specific alignment with clinical guidelines, its restriction to mental health roles, and its lack of generalizability. The authors acknowledge that ChatGPT-generated dialogues may amplify model biases, that the approach is limited to Chinese, and that it lacks expert-validated clinical pathways.
