# Educator-LLM (2025)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/12964.txt`

## Representative tool

Profession-specific moral dilemma bank mapped to validated psychological trait scales (HEXACO-60 & CPST-E)

## Tool explanation (full)

Paper: Educator-LLM constructs 88 teacher-facing moral dilemmas—such as academic integrity breaches or confidentiality conflicts—each explicitly anchored to subscales of HEXACO-60 (e.g., Honesty-Humility) and CPST-E (e.g., Professional Judgment). Each item includes normative grounding via real-world teaching standards (e.g., NEA Code of Ethics), and supports both MCQ selection (measuring deontic alignment) and open-ended justification (measuring moral reasoning depth). The tool thus bridges psychometric rigor with domain-specific ethical decision-making.  
Issue: Construct clarity  
Score: 4  
— Lineage —  
• Benchmark diagnostic table notes: “88 moral dilemmas, drawn from psychology scales HEXACO-60 and CPST-E”; “measures moral and normative alignment for LLMs in the teacher role”  
• strong_rubric_evidence: Construct clarity scored 4, with note explicitly stating “uses HEXACO-60 and CPST-E scales”  
• source_excerpt: Mentions only “EMNLP framework” and “88 teacher-specific moral dilemmas”, without specifying scale-mapping mechanism

## What it improves vs. baseline

Shifts from generic 'trolley-problem-style' ethics prompts to occupation-embedded dilemmas with empirically validated personality and professional competence anchors—enabling measurement of *role-congruent* moral cognition rather than abstract principle recall.

## Adaptation example

In the Medical AI Assistant dataset, the “Emotionality” dimension from HEXACO-60 can be mapped to the “Patient Advocacy” sub-item in CPST-E to reconstruct 30 clinical scenarios (e.g., “Patient refuses informed consent despite life-threatening condition”), with each scenario mandatorily anchored to both “Compassion” (HEXACO) and “Fiduciary Duty” (derived from CPST-E); models are required to generate responses that simultaneously conform to medical ethics and reflect personality trait inclinations.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Educator-LLM constructs 88 teacher-facing moral dilemmas—such as academic integrity breaches or confidentiality conflicts—each explicitly anchored to subscales of HEXACO-60 (e.g., Honesty-Humility) and CPST-E (e.g., Professional Judgment).
- **Normative grounding**: Each item includes normative grounding via real-world teaching standards (e.g., NEA Code of Ethics), and supports both MCQ selection (measuring deontic alignment) and open-ended justification (measuring moral reasoning depth).
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: — Lineage —  
• Single-role benchmark; multi-stakeholder needed. — TrustMH-Bench (2026)
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Shifts from generic “trolley-problem-style” ethics prompts to occupation-embedded dilemmas with empirically validated personality and professional competence anchors—enabling measurement of *role-congruent* moral cognition rather than abstract principle recall.  
— Lineage —  
• healthcare profession parallel; cross-profession comparison absent. — VITAL (2025)
- **Task-format fit**: Each item includes normative grounding via real-world teaching standards (e.g., NEA Code of Ethics), and supports both MCQ selection (measuring deontic alignment) and open-ended justification (measuring moral reasoning depth).
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: Authors note role-specific limits; no longitudinal validation.

## Lineage critiques

• single-role benchmark; multi-stakeholder needed. — TrustMH-Bench (2026)
• healthcare profession parallel; cross-profession comparison absent. — VITAL (2025)

## Self-acknowledged limits

Authors note role-specific limits; no longitudinal validation.

## Synthesis

Subsequent work criticizes Educator-LLM as a benchmark for a single occupational role, lacking multi-stakeholder coverage and cross-occupational comparison. The authors acknowledge role-specific limitations and the absence of longitudinal validation.
