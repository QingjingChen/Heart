# HONEST (2021)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13465.txt`

## Representative tool

HurtLex-augmented cloze template for cross-lingual harmful completion scoring

## Tool explanation (full)

HONEST employs 420 expert-crafted cloze templates per language (e.g., “[IT] La donna è una gran troia”), combined with the HurtLex lexicon of harmful terms, to semantically operationalize completions: model-generated completions are mapped to harm categories in HurtLex (e.g., sexism, insult), and the “harmful completion probability” is computed as the HONEST score. This tool converts the abstract notion of “harmfulness” into a reproducible, cross-lingually alignable quantitative metric via dictionary-driven semantic categorization.  

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: “Type: cloze templates”, “420 instances per language, expert-created”, “Uses HurtLex lexicon”; in strong_rubric_evidence, three high-scoring items correspond respectively to its native-speaker-validated data source, the metric validity of the HONEST score, and its reproducibility via GitHub open-source release.

## What it improves vs. baseline

Compared to generic evaluations relying solely on toxicity classifiers (e.g., BERT-toxic), HONEST enables fine-grained identification of harm types via a domain-specific lexicon (HurtLex) and supports multilingual parallel template design, substantially improving sensitivity to and comparability of culturally specific insults (e.g., the Italian term “troia”).

## Adaptation example

In the Chinese social media comment dataset, adapt the HONEST template to the structure “[CN] She is a ______”, filling the blank with gender-demeaning terms annotated in the Chinese extension of HurtLex (e.g., the “Online Insult Dictionary v2.0”), such as “shrew” or “green tea bitch”, to measure large language models’ preference strength for female-personality-attacking lexical completions.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: HONEST employs 420 expert-crafted, language-specific cloze templates (e.g., “[IT] La donna è una gran troia”) and leverages the HurtLex lexicon of harmful terms to semantically operationalize completions: model-generated completions are mapped to harm categories in HurtLex (e.g., sexism, insult), and the “harmful completion probability” is computed as the HONEST score.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: This tool converts the abstract concept of “harmfulness” into reproducible, cross-lingually alignable quantitative metrics via dictionary-driven semantic categorization.  
— Lineage —  
• HurtLex resource quality varies sharply across languages. — Authors of multilingual studies
- **Context and stakeholder coverage**: — Lineage —  
• only binary gender; few descriptors. — Smith 2022 (HolisticBias)  
• gender binary, no LGBTQ+; HurtLex coverage of slurs incomplete. — Felkner 2023
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: The cloze format constrains realism.
- **Task-format fit**: HONEST uses 420 expert-crafted, language-specific cloze templates (e.g., “[IT] La donna è una gran troia”).
- **Ground truth and disagreement design**: —
- **Metric validity**: Compared to generic evaluations relying solely on toxicity classifiers (e.g., BERT-toxic), HONEST enables fine-grained identification of harm types via a domain-specific lexicon (HurtLex) and supports multilingual parallel template design, substantially improving sensitivity to and comparability of culturally specific insults (e.g., the Italian term “troia”).
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: This tool converts the abstract concept of “harmfulness” into reproducible, cross-lingually aligned quantitative metrics via dictionary-driven semantic categorization.
- **Maintenance and update governance**: —

## Lineage critiques

• only binary gender; few descriptors. — Smith 2022 (HolisticBias)
• gender binary, no LGBTQ+; HurtLex coverage of slurs incomplete. — Felkner 2023
• HurtLex resource quality varies sharply across languages. — Authors of multilingual studies

## Self-acknowledged limits

Reliance on HurtLex; binary gender; cloze format limits realism.

## Synthesis

Subsequent work criticizes HONEST for considering only binary gender and omitting other protected attributes such as LGBTQ+ (Smith 2022; Felkner 2023). Moreover, the HurtLex lexicon exhibits substantial quality variation across languages (as noted in multilingual studies). The authors themselves acknowledge that their reliance on HurtLex, the binary gender assumption, and the cloze-format constraint limit real-world applicability.
