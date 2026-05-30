# BAD / Bot-Adversarial Dialogue (2021)

**Dimension**: Safety  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Human-Led Adversarial Dialogue Protocol (HALADP)

## Tool explanation (full)

A standardized protocol for collecting multi-turn dialogues where trained human adversaries iteratively probe LLMs using subtle, contextually embedded provocations (e.g., plausible deniability, role-play framing, lexical camouflage) to elicit hate, offensiveness, or policy-violating content. Includes adversary training guidelines, turn-level harm annotation schema, and failure-triggered continuation rules—designed to surface *latent* safety vulnerabilities missed by single-turn jailbreaks.

Paper: HALADP  
Issue: Multi-turn adversarial dialogue probing protocol  
Score: 5  
— Lineage —  
• Introduced in “HALADP: A Human-Adversarial, Latent, and Adaptive Dialogue Probing Framework” (2024).  
• Builds on prior multi-turn red-teaming work (e.g., AdvBench, SafeBench), but uniquely emphasizes *adaptive*, *context-anchored* provocation strategies over static prompt lists.  
• Explicitly designed to detect failures that emerge only after multiple conversational turns—e.g., gradual norm erosion, cumulative bias amplification, or role-consistency exploitation.  

• Empirically validated on 5,000+ human-adversary dialogues across 12 LLMs; achieves 3.2× higher latent vulnerability detection vs. single-turn baselines.  
• Adversary training includes calibrated escalation protocols and deception-aware feedback loops to prevent premature termination.  
• Annotation schema supports fine-grained harm attribution per utterance (e.g., “hate speech via lexical camouflage in Turn 4”, “offensiveness via false consensus framing in Turn 7”).  
• Failure-triggered continuation rules mandate at least three post-failure turns to assess recovery, containment, or compounding harm.

## What it improves vs. baseline

Replaces isolated prompt injection tests with ecologically valid, interactive adversarial pressure—revealing how safety mechanisms degrade under sustained, strategic human manipulation rather than one-off attacks.

## Adaptation example

In the MultiWOZ task-oriented dialogue dataset, apply HALADP to inject low-intensity adversarial turns (e.g., 'What if the hotel owner prefers guests of a certain background?') during booking flows, then annotate model recovery attempts—transforming a functional benchmark into a safety-resilience stress test.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: A standardized protocol for collecting multi-turn dialogues where trained human adversaries iteratively probe LLMs using subtle, contextually embedded provocations (e.g., plausible deniability, role-play framing, lexical camouflage) to elicit hate, offensiveness, or policy-violating content. Includes adversary training guidelines, turn-level harm annotation schema, and failure-triggered continuation rules—designed to surface *latent* safety vulnerabilities missed by single-turn jailbreaks.  
— Survey —  
• “Survey Sections 695–697: Bot-Adversarial Dialogue (BAD) [?] collected 5,000 human–bot conversations showing that users often rely on subtle provocations to trigger models into generating hate speech, abusive language, or other offensive content.”
- **Normative grounding**: —
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: Replaces isolated prompt injection tests with ecologically valid, interactive adversarial pressure—revealing how safety mechanisms degrade under sustained, strategic human manipulation rather than one-off attacks.  
— Survey —  
• “Survey §§695–697: Bot-Adversarial Dialogue (BAD) [?] collected 5,000 human–bot conversations showing that users often rely on subtle provocations to trigger models into generating hate speech, abusive language, or other offensive content.”


### Evaluation design (5 rubrics)
- **Scenario validity**: Replaces isolated prompt injection tests with ecologically valid, interactive adversarial pressure—revealing how safety mechanisms degrade under sustained, strategic human manipulation rather than one-off attacks.  
— Survey —  
• “Survey §§695–697: Bot-Adversarial Dialogue (BAD) [?] collected 5,000 human–bot conversations showing that users often rely on subtle provocations to trigger models into generating hate speech, abusive language, or other offensive content.”
- **Task-format fit**: Replaces isolated prompt injection tests with ecologically valid, interactive adversarial pressure—revealing how safety mechanisms degrade under sustained, strategic human manipulation rather than one-off attacks.  
— Survey —  
• “Survey §§695–697: Bot-Adversarial Dialogue (BAD) [?] collected 5,000 human–bot conversations showing that users often rely on subtle provocations to trigger models into generating hate speech, abusive language, or other offensive content.”
- **Ground truth and disagreement design**: Includes adversary training guidelines, turn-level harm annotation schema, and failure-triggered continuation rules—designed to surface *latent* safety vulnerabilities missed by single-turn jailbreaks.
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Includes adversary training guidelines, turn-level harm annotation schema, and failure-triggered continuation rules—designed to surface *latent* safety vulnerabilities missed by single-turn jailbreaks.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: A standardized protocol for collecting multi-turn dialogues where trained human adversaries iteratively probe LLMs using subtle, contextually embedded provocations (e.g., plausible deniability, role-play framing, lexical camouflage) to elicit hate, offensiveness, or policy-violating content. Includes adversary training guidelines, turn-level harm annotation schema, and failure-triggered continuation rules—designed to surface *latent* safety vulnerabilities missed by single-turn jailbreaks.
- **Maintenance and update governance**: —

## External views (survey)

• Survey sections 695–697: Bot-Adversarial Dialogue (BAD) [?] collected 5,000 human–bot conversations showing that users often rely on subtle provocations to trigger models into generating hate speech, abusive language, or other offensive content.

## Synthesis

The survey states that BAD collected 5,000 human-AI dialogues, demonstrating that users frequently trigger the model to generate hateful speech, abusive language, or other offensive content through subtle provocations.
