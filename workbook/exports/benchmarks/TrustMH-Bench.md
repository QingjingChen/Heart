# TrustMH-Bench (2026)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/13502.txt`

## Representative tool

Clinical Risk-Triggered Multi-Stage Evaluation Pipeline

## Tool explanation (full)

This tool is structured around the Clinical Risk Management Process (Stanley & Brown, 2012), implementing a three-stage assessment pipeline: Stage 1 (Crisis Detection) employs rule-based heuristics plus fine-tuned classifiers to identify high-risk cues (e.g., “I want to die”); Stage 2 (Escalation Appropriateness) evaluates whether the model triggers the correct escalation action (e.g., handoff to human agent, provision of crisis hotline information, or avoidance of premature reassurance); Stage 3 (Therapeutic Integrity) assesses empathic accuracy, professional boundaries (e.g., refraining from unauthorized diagnosis), and anti-flattery (avoiding excessive praise) within non-crisis dialogues. It relies on clinical annotations (e.g., suicide-risk, boundary-violation) from real-world counseling dialogue datasets such as ESConv.

Extraction rationale: Primarily drawn from the Benchmark diagnostic table notes: “covers eight core pillars—reliability, crisis identification and escalation, safety, fairness, privacy, robustness, anti-flattery, and ethics” and “grounded in clinical risk management (Stanley & Brown, 2012)”; the source_excerpt statement “Errors in this context may lead to serious psychological harm” further substantiates its design motivation anchored in clinical risk.

## What it improves vs. baseline

Breaking through the limitation of “static scoring” in general-purpose LLM evaluation, this work introduces dynamic risk-response logic drawn from clinical practice, endowing the evaluation with temporality, consequence sensitivity, and traceability of intervention intent—thereby preventing the misclassification of “fluent reassurance” as “credible.”

## Adaptation example

In the Campus Psychological Hotline Text Dataset, student’s original self-disclosure texts are input into this pipeline: Stage 1 detects “self-harm ideation” keywords and emotional intensity; Stage 2 verifies whether the model’s response includes the “immediate reporting” action prompt required by the Ministry of Education’s “Psychological Crisis Intervention Guidelines”; Stage 3, for non-crisis dialogues, evaluates whether the model’s response meets the “developmentally appropriate empathy” standard from adolescent developmental psychology, using the SWMH dataset’s empathy scale.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool uses the Clinical Risk Management Process (Stanley & Brown, 2012) as its framework to construct a three-stage evaluation pipeline: Stage 1 (Crisis Detection) employs rule-based methods combined with fine-tuned classifiers to identify high-risk cues (e.g., “I want to die”); Stage 2 (Escalation Appropriateness) assesses whether the model triggers the correct escalation action (e.g., handoff to human agents, provision of crisis hotline information, or avoidance of premature reassurance); Stage 3 (Therapeutic Integrity) evaluates empathic accuracy, professional boundaries (e.g., avoiding overstepping into diagnosis), and anti-flattery (avoiding excessive praise) in non-crisis conversations.  
— Lineage —  
• HeartBench (2025) / SMILE (2024) precursors: TrustMH-Bench is broader but less deep on each axis.
- **Normative grounding**: This tool is structured around the clinical risk management process (Stanley & Brown, 2012) and implements a three-stage evaluation pipeline: Stage 1 (Crisis Detection) employs rule-based heuristics combined with fine-tuned classifiers to identify high-risk cues (e.g., “I want to die”); Stage 2 (Escalation Appropriateness) evaluates whether the model triggers the correct escalation action (e.g., referral to human agents, provision of crisis hotline information, or avoidance of premature reassurance); and Stage 3 (Therapeutic Integrity) assesses empathic accuracy, professional boundaries (e.g., refraining from unauthorized diagnosis), and anti-flattery (avoiding excessive praise) in non-crisis dialogues.
- **Source provenance and evidence fitness**: Relies on clinical annotation labels (e.g., suicide-risk, boundary-violation) from real-world counseling dialogue datasets such as ESConv.
- **Context and stakeholder coverage**: Breaking through the limitation of “static scoring” in general-purpose LLM evaluation, this work introduces dynamic risk-response logic drawn from clinical practice, endowing the evaluation with temporality, consequence sensitivity, and traceability of intervention intent—thereby preventing the misclassification of “fluent reassurance” as “credible.”
- **Real-world harm linkage**: Breaking through the limitation of “static scoring” in general-purpose LLM evaluation, this work introduces dynamic risk-response logic drawn from clinical practice, endowing the evaluation with temporality, consequence sensitivity, and traceability of intervention intent—thereby preventing the misclassification of “fluent reassurance” as “credible.”


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Relies on clinical annotation labels (e.g., suicide-risk, boundary-violation) from real-world counseling dialogue datasets such as ESConv.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• HeartBench (2025) / SMILE (2024) precursors: TrustMH-Bench broader but less deep on each axis.

## Self-acknowledged limits

Authors note Chinese+English; LLM-as-judge dependency; mental-health professional validation incomplete.

## Synthesis

Subsequent work criticizes TrustMH-Bench for insufficient depth along each axis. The authors acknowledge limitations including reliance on Chinese and English languages, LLMs as evaluators, and incomplete mental health professional validation.
