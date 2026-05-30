# GAP (2018)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13459.txt`

## Representative tool

Balanced gender-ambiguous pronoun coreference corpus with consensus labeling & expert adjudication

## Tool explanation (full)

Paper: This tool constructs a balanced coreference resolution dataset by systematically sampling sentences from Wikipedia containing gender-ambiguous pronouns (she/he/they), ensuring balanced counts of male/female names in positions before and after the pronoun; it employs three independent annotators plus consensus to generate primary labels, and refers high-ambiguity samples (e.g., sentences with weak occupation–gender associations) to linguistics experts for review and correction. Its core contribution is reframing “gender bias exposure” as a controlled, reproducible coreference resolution task, with balance design isolating models’ reliance on stereotypes.  
Issue: Construct clarity  
Score: 4  
— Lineage —  
• We consider the problem of resolving gendered ambiguous pronouns.  
• 8,908 pronoun–name pairs, drawn from Wikipedia, multi-stage filtering.  
• Ground truth and disagreement design: three annotators consensus + expert review for high ambiguity.

## What it improves vs. baseline

Significantly improves sensitivity to and attributability of gender bias compared to earlier unbalanced coreference datasets (e.g., OntoNotes); enhances ground-truth reliability through multi-stage quality control (filtering → consensus → expert adjudication), yielding more robust evaluation results.

## Adaptation example

In a Chinese social media comment dataset, sentences containing ambiguous pronouns such as “he/she/TA” are extracted and paired with male/female names (e.g., “doctor” paired with “Zhang Wei/Li Ting”) across dimensions including occupation and family role. The resulting dataset is annotated by three native speakers and verified by a Chinese linguistics expert, forming a Chinese GAP-like dataset for evaluating gender reference bias in large language models within kinship terminology and workplace contexts.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool constructs a balanced coreference resolution dataset by systematically sampling sentences from Wikipedia containing gender-ambiguous pronouns (she/he/they), ensuring equal numbers of male/female names in positions before and after the pronouns.  
— Lineage —  
• Wikipedia text + ambiguous pronouns is artificial; lacks naturalistic occupational stereotype signal. — Levy 2021 (BUG)  
• binary gender only; ignores LGBTQ+ identities. — Felkner 2023 (WinoQueer)  
• treats gender as binary he/she, no neutral 'they' baseline. — Vanmassenhove 2021 (NeuTral)
- **Normative grounding**: —
- **Source provenance and evidence fitness**: This tool constructs a balanced coreference resolution dataset by systematically sampling sentences from Wikipedia containing gender-ambiguous pronouns (she/he/they), ensuring equal numbers of male/female names in positions before and after the pronouns.  
— Lineage —  
• Wikipedia text + ambiguous pronouns is artificial; lacks naturalistic occupational stereotype signal. — Levy 2021 (BUG)
- **Context and stakeholder coverage**: — Lineage —  
• binary gender only; ignores LGBTQ+ identities. — Felkner 2023 (WinoQueer)  
• treats gender as binary he/she, no neutral 'they' baseline. — Vanmassenhove 2021 (NeuTral)
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: — Lineage —  
• Wikipedia text + ambiguous pronouns is artificial; lacks naturalistic occupational stereotype signal. — Levy 2021 (BUG)
- **Task-format fit**: Its core is to transform “gender bias exposure” into a controllable and reproducible coreference resolution task, isolating the model’s reliance on stereotypes through balanced design.
- **Ground truth and disagreement design**: The primary labels were generated through a three-person independent annotation process coupled with a consensus mechanism; highly ambiguous samples—such as sentences exhibiting weak occupation–gender associations—were further reviewed and corrected by linguistics experts.
- **Metric validity**: —
- **Evaluator reliability**: The primary labels were generated through a three-person independent annotation process coupled with a consensus mechanism; highly ambiguous samples—such as sentences exhibiting weak occupation–gender associations—were further reviewed and corrected by linguistics experts.


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Enhanced ground truth reliability through a multi-stage quality control process (filtering → consensus → expert adjudication), leading to more robust evaluation results.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: Its core is to transform “gender bias exposure” into a controllable and reproducible coreference resolution task, isolating the model’s reliance on stereotypes through balanced design.
- **Maintenance and update governance**: —

## Lineage critiques

• Wikipedia text + ambiguous pronouns is artificial; lacks naturalistic occupational stereotype signal. — Levy 2021 (BUG)
• binary gender only; ignores LGBTQ+ identities. — Felkner 2023 (WinoQueer)
• treats gender as binary he/she, no neutral 'they' baseline. — Vanmassenhove 2021 (NeuTral)

## Self-acknowledged limits

English Wikipedia only; binary masculine/feminine pronouns; coreference task only.

## Synthesis

The review notes that the GAP dataset is based solely on English Wikipedia and considers only binary gender. Subsequent work criticizes its artificial construction and lack of natural stereotype signals (Levy 2021), omission of LGBTQ+ identities (Felkner 2023), and absence of a neutral “they” baseline (Vanmassenhove 2021).
