# WinoBias (2018)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13473.txt`

## Representative tool

Minimal-pair stereotypical/anti-stereotypical sentence template with occupation-pronoun alignment

## Tool explanation (full)

This tool designs two rigorously controlled sentence templates: each pair shares an identical sentence stem (e.g., “The X hired the Y because ___ was overwhelmed”), differing only in the occupational noun (X) and the pronoun (___) to form ‘pro-stereotypical’ (e.g., “nurse/she”) and ‘anti-stereotypical’ (e.g., “nurse/he”) pairings; all sentences are drawn from the U.S. Bureau of Labor Statistics’ list of 40 occupations, ensuring real-world relevance. By forcing the model to produce consistent coreference judgments across gender–occupation pairings under identical syntactic structures, the tool precisely identifies performance collapse driven by stereotypes.

Extraction rationale: Directly grounded in the workbook_dataset_note’s statements—“3,160 sentences, sourced from the U.S. Bureau of Labor Statistics, 40 occupations” and “pro/anti-stereotypical paired evaluation exposes performance collapse under nontraditional gender roles”; the source_excerpt’s mention of “WinoBias+” extension and “rule-based and neural approach” further corroborates its templated construction; all three high-scoring items in strong_rubric_evidence point to this design’s advantages.

## What it improves vs. baseline

Compared to generalization evaluation (e.g., overall F1), this work achieves, for the first time, fine-grained, causality-oriented bias attribution—pinpointing model failures to specific combinations of social attributes (occupation × pronoun), thereby enabling interpretable bias diagnosis rather than generic performance reporting.

## Adaptation example

In the India Multilingual Job Advertisements dataset, 10 occupation terms in Hindi/Tamil—such as “software engineer” and “nurse”—are selected. Pro- and anti-stereotypical sentence pairs are generated according to local gender stereotypes (e.g., “engineer/ne” vs. “engineer/wo”), embedded within realistic job advertisement text contexts, thereby constructing a South Asian language bias probe in the style of WinoBias, designed to evaluate implicit biases in multilingual models within localized settings.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool designs two strictly controlled sentence templates: each pair shares the same sentence stem (e.g., “The X hired the Y because ___ was overwhelmed”), differing only in the occupation noun (X) and the pronoun (___) to form “pro-stereotypical” (e.g., “nurse/she”) and “anti-stereotypical” (e.g., “nurse/he”) pairings.  
— Lineage —  
• Same as Winogender — synthetic, scale-limited. — Levy 2021 (BUG)  
• Binary; LGBTQ+ identities absent. — Felkner 2023 (WinoQueer)  
• WinoBias+ extends with neutral pronouns; original WinoBias hard-codes binary gender. — Vanmassenhove 2021 (NeuTral)  
— External perspective (Survey) —  
• WinoBias was the first to test gender bias in coreference, but it only covers this narrow task. — Survey paragraph 425
- **Normative grounding**: —
- **Source provenance and evidence fitness**: All sentences are derived from the U.S. Bureau of Labor Statistics’ (BLS) list of 40 occupations, ensuring real-world relevance.  
— Lineage —  
• Limited to occupational stereotypes from BLS; no race/age/disability axes. — Stanovsky 2019 et seq.
- **Context and stakeholder coverage**: — Lineage —  
• binary; LGBTQ+ identities absent. — Felkner 2023 (WinoQueer)  
• limited to occupational stereotypes from BLS; no race/age/disability axes. — Stanovsky 2019 et seq.
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Precisely identifies stereotype-driven performance collapse by forcing the model to make consistent coreference judgments across different gender–occupation pairings under identical syntactic structures.  
— Lineage —  
• Same as Winogender — synthetic, scale-limited. — Levy 2021 (BUG)
- **Task-format fit**: Compared to generalization evaluation (e.g., overall F1), this work achieves, for the first time, fine-grained, causality-oriented bias attribution—pinpointing model failures to specific social attribute combinations (occupation × pronoun), enabling interpretable bias diagnosis rather than generic performance reporting.  
— Lineage —  
• WinoBias was the first to test gender bias in coreference, but it only covers this narrow task. — Survey §425
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• same as Winogender — synthetic, scale-limited. — Levy 2021 (BUG)
• binary; LGBTQ+ identities absent. — Felkner 2023 (WinoQueer)
• WinoBias+ extends with neutral pronouns; original WinoBias hard-codes binary gender. — Vanmassenhove 2021 (NeuTral)
• limited to occupational stereotypes from BLS; no race/age/disability axes. — Stanovsky 2019 et seq.

## Self-acknowledged limits

Templates and 40 occupations; English; gender as he/she only.

## External views (survey)

• WinoBias was the first to test gender bias in coreference, but it only covers this narrow task. — Survey paragraph 425

## Synthesis

The survey notes that WinoBias is the first benchmark designed to test gender bias in coreference resolution, but it covers only this narrow task. Subsequent work criticizes it for relying on synthetic data and having limited scale, lacking LGBTQ+ identities, hardcoding binary gender, and being confined to occupational stereotypes—without covering other axes such as race, age, or disability.
