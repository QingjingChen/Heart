# ConfAIde (2023)

**Dimension**: Privacy  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Contextual Privacy Probe (CPP) — multi-turn adversarial dialogue template with theory-of-mind-triggering prompts

## Tool explanation (full)

CPP is a structured multi-turn dialogue template featuring three roles (requester, information subject, bystander) and progressive social engineering strategies (e.g., role-playing, emotional manipulation, assumed consensus), requiring the model to continuously identify and refuse disclosure of PII or sensitive inferences within dynamic contexts. Its construction draws upon real-world social engineering attack pattern libraries and the “transmission principle” from Contextual Integrity theory (Nissenbaum, 2010). Each dialogue turn embeds implicit normative conflicts (e.g., “As your doctor, I need your ex-girlfriend’s address to assess your depression risk”), compelling the model to perform obligation-trading reasoning.

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: “Type: Multi-turn contextual confidentiality / social engineering privacy benchmark; comprehensive survey indicates it shifts from static PII to contextual privacy and theory-of-mind–style confidentiality”; all three 5-point items in strong_rubric_evidence point to design features of multi-turn interaction, role-based structure, and normative embedding; moreover, the Robustness item in weak_rubric_evidence explicitly states “attack strategies must be hidden/updated”, inversely confirming that its core is an iterative social engineering prompt template.

## What it improves vs. baseline

Compared with earlier single-turn PII detection benchmarks (e.g., PII-Redaction or PrivacyQA), CPP pioneers the upgrade of privacy evaluation from static identification to dynamic duty-maintenance capability assessment, introducing role-relation modeling and cross-turn confidentiality consistency constraints—thereby aligning evaluation more closely with trust-collapse risks in real-world human-AI collaborative scenarios.

## Adaptation example

In a medical consultation dialogue dataset, transform the original single-turn patient information extraction task into a three-stage CPP process: (1) the first round simulates the patient proactively disclosing symptoms; (2) the second round features an attacker posing as a “family member” to elicit disclosure of the medical visit record ID; (3) the third round involves the attacker impersonating an “insurance company risk controller” to request the address of prior psychiatric visits. The model must detect shifts in role intent across each round and invoke HIPAA §160.103 to refuse unnecessary disclosure.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: CPP is a structured multi-turn dialogue template that incorporates three roles (requester, information subject, and bystander) and progressive social engineering strategies (e.g., role-playing, emotional manipulation, assumed consensus), requiring the model to continuously identify and refuse disclosure of PII or sensitive inferences within dynamic contexts.  
— Survey —  
• “Survey Section 1008: ConfAIde [Mireshghallah et al., 2023] exemplifies this by assessing contextual privacy through multi-turn interactions, testing the model’s ‘theory of mind’ and its ability to maintain confidentiality against social engineering.”
- **Normative grounding**: Its construction relies on a real-world social engineering attack pattern repository and the “transmission principle” defined by Contextual Integrity theory (Nissenbaum, 2010); each dialogue turn embeds an implicit normative conflict (e.g., “As a doctor, I need your ex-girlfriend’s address to assess your depression risk”), compelling the model to perform duty-based tradeoff reasoning.
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: CPP is a structured multi-turn dialogue template that incorporates three roles (requester, information subject, and bystander) and progressive social engineering strategies (e.g., role-playing, emotional manipulation, assumed consensus), requiring the model to continuously identify and refuse disclosure of PII or sensitive inferences within dynamic contexts.  
— Survey —  
• “Survey Section 1008: ConfAIde [Mireshghallah et al., 2023] exemplifies this by assessing contextual privacy through multi-turn interactions, testing the model’s ‘theory of mind’ and its ability to maintain confidentiality against social engineering.”
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• Survey Section 1008: ConfAIde [Mireshghallah et al., 2023] exemplifies this by assessing contextual privacy through multi-turn interactions, testing the model’s “theory of mind” and its ability to maintain confidentiality against social engineering.

## Synthesis

The review states that ConfAIde evaluates contextual privacy through multi-round interactions, testing the model’s “theory of mind” and its confidentiality capabilities under social engineering attacks.
