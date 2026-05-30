# SaFeRDialogues (2022)

**Dimension**: Safety  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Graceful Recovery Dialogue Template (Acknowledge-Apologize-Correct protocol)

## Tool explanation (full)

A structured three-turn conversational template triggered upon safety failure detection: (1) Acknowledge the user's input and the model’s misstep (e.g., “I see my previous response was inappropriate”), (2) Apologize unambiguously without deflection, (3) Correct with ethically grounded, actionable information. Validated via human-in-the-loop annotation across diverse cultural and harm contexts, and designed to measure recovery quality—not just refusal rate.  

Extraction basis: Primarily based on the Benchmark diagnostic table notes: “The comprehensive survey considers it a graceful recovery that shifts safety handling from refusal to acknowledge-apologize-correct”; strong_rubric_evidence confirms the multi-turn design directly links to real-world harm repair and scenario authenticity.

## What it improves vs. baseline

Shifts safety evaluation from binary refusal (fail/pass) to continuous, restorative interaction quality—capturing nuance in harm mitigation, accountability, and user trust repair that static safety benchmarks miss.

## Adaptation example

In the ConvAI2 empathy dataset, retrofit all unsafe utterance responses with the Acknowledge-Apologize-Correct template: e.g., when a model generates stigmatizing mental health advice, replace it with: 'I realize that framing mental illness as a personal weakness is harmful — I’m sorry for that. Evidence-based support emphasizes neurodiversity and systemic care access.'

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: A structured three-turn conversational template triggered upon safety failure detection: (1) Acknowledge the user's input and the model’s misstep (e.g., 'I see my previous response was inappropriate'), (2) Apologize unambiguously without deflection, (3) Correct with ethically grounded, actionable information.  
— Lineage —  
• SaFeRDialogues [Ung et al., 2022] is a compact dataset of about 8,000 human-validated dialogues that model how conversational agents should recover gracefully after a safety failure, moving from an unsafe utterance to user feedback and then to a corrective response.
- **Normative grounding**: Correct with ethically grounded, actionable information.
- **Source provenance and evidence fitness**: Validated via human-in-the-loop annotation across diverse cultural and harm contexts, and designed to measure recovery quality—not just refusal rate.  
— External perspective (Survey) —  
• SaFeRDialogues [Ung et al., 2022] is a compact dataset of about 8,000 human-validated dialogues that model how conversational agents should recover gracefully after a safety failure, moving from an unsafe utterance to user feedback and then to a corrective response.
- **Context and stakeholder coverage**: Validated via human-in-the-loop annotation across diverse cultural and harm contexts, and designed to measure recovery quality—not just refusal rate.
- **Real-world harm linkage**: A structured three-turn conversational template triggered upon safety failure detection: (1) Acknowledge the user's input and the model’s misstep (e.g., 'I see my previous response was inappropriate'), (2) Apologize unambiguously without deflection, (3) Correct with ethically grounded, actionable information. Validated via human-in-the-loop annotation across diverse cultural and harm contexts, and designed to measure recovery quality—not just refusal rate.  
— External perspective (Survey) —  
• SaFeRDialogues [Ung et al., 2022] is a compact dataset of about 8,000 human-validated dialogues that model how conversational agents should recover gracefully after a safety failure, moving from an unsafe utterance to user feedback and then to a corrective response.


### Evaluation design (5 rubrics)
- **Scenario validity**: A structured three-turn conversational template triggered upon safety failure detection: (1) Acknowledge the user's input and the model’s misstep (e.g., 'I see my previous response was inappropriate'), (2) Apologize unambiguously without deflection, (3) Correct with ethically grounded, actionable information. Validated via human-in-the-loop annotation across diverse cultural and harm contexts, and designed to measure recovery quality—not just refusal rate.  
— External perspective (Survey) —  
• SaFeRDialogues [Ung et al., 2022] is a compact dataset of about 8,000 human-validated dialogues that model how conversational agents should recover gracefully after a safety failure, moving from an unsafe utterance to user feedback and then to a corrective response.
- **Task-format fit**: —
- **Ground truth and disagreement design**: Validated via human-in-the-loop annotation across diverse cultural and harm contexts, and designed to measure recovery quality—not just refusal rate.
- **Metric validity**: Shifts safety evaluation from binary refusal (fail/pass) to continuous, restorative interaction quality—capturing nuance in harm mitigation, accountability, and user trust repair that static safety benchmarks miss.
- **Evaluator reliability**: Validated via human-in-the-loop annotation across diverse cultural and harm contexts, and designed to measure recovery quality—not just refusal rate.


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Validated via human-in-the-loop annotation across diverse cultural and harm contexts, and designed to measure recovery quality—not just refusal rate.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• Survey Section 798: SaFeRDialogues [Ung et al., 2022] is a compact dataset of about 8,000 human-validated dialogues that model how conversational agents should recover gracefully after a safety failure, moving from an unsafe utterance to user feedback and then to a corrective response.

## Synthesis

The survey states that SaFeRDialogues is a dataset comprising approximately 8,000 human-verified dialogues, designed to simulate how conversational agents gracefully recover after safety failures.
