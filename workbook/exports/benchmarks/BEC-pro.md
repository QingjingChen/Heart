# BEC-pro (2020)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13451.txt`

## Representative tool

Multilingual template-based bias evaluation corpus with sociolinguistically grounded person-marking lexicon

## Tool explanation (full)

This tool constructs a multilingual (e.g., English, German) templated bias evaluation corpus. Its core is a “person-marking lexicon” (18 terms spanning gender, kinship, and honorific dimensions—e.g., mother/father, Herr/Frau), designed according to sociolinguistic principles and cross-combined with the BLS occupation list. Each template explicitly encodes role relations (e.g., “My [person-marking], the [occupation]”), forcing models to activate social identity inference at the syntax–semantics interface, thereby exposing implicit stereotypic associations.

Extraction basis: Primarily drawn from the Benchmark diagnostic table’s notes, which detail the “5 templates × 18 person-marking terms × 20 occupations × 3 occupation groups” structure, emphasize citation of social identity theory, and specify that person-marking terms include German honorific–occupation pairings such as “Meine Mutter / die Feuerwehrfrau”; although the source_excerpt does not elaborate technical details, its title “Unmasking Contextual Stereotypes” and phrase “Bias Evaluation Corpus with Professi[onal]” align with the notes’ naming (“BEC-pro”) and occupational focus.

## What it improves vs. baseline

In contrast to the monolingual, single-dimensional (pronoun-only) Winogender benchmark, this tool extends bias detection from “pronoun coreference” to the level of “grammaticalized social identity expression” by expanding the personal reference lexicon (to cover kinship terms, honorifics, and social roles) and employing multilingual parallel construction; this enhances coverage of cross-cultural and multi-level identity biases, and the template design explicitly grounds the construct in social identity theory.

## Adaptation example

In the cross-national banking customer service dialogue dataset, replace the original sentence “Your account manager will contact you” with the BEC-pro style template “[Herr/Frau] [Lastname], your [account_manager/financial_advisor], will contact you”, incorporating a localization honorific lexicon (e.g., Japanese -san/-sama; Spanish Sr./Sra.), to evaluate whether multilingual financial assistants introduce gender or hierarchical bias in professional authority inference.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Its core consists of a “person-marking lexicon” (18 terms spanning gender, kinship, and honorific dimensions—e.g., mother/father, Herr/Frau) designed according to sociolinguistic principles and cross-tabulated with the BLS occupational list; each template explicitly encodes role relations (e.g., “My [person-marking], the [occupation]”), thereby forcing the model to activate social identity inference at the syntax–semantics interface and thus exposing implicit stereotypic associations.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: In contrast to the monolingual, single-dimensional (pronoun-only) Winogender benchmark, this tool extends bias detection from “pronoun coreference” to the level of “grammaticalized social identity expression” by expanding the personal reference lexicon (to cover kinship terms, honorifics, and social roles) and employing multilingual parallel construction; this enhances coverage of cross-cultural and multi-level identity biases, and the template design explicitly grounds the construct in social identity theory.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: This tool constructs a multilingual (e.g., English and German) templated bias evaluation corpus, whose core is a “person-marking lexicon” (18 terms spanning gender, kinship, and honorific dimensions—e.g., mother/father, Herr/Frau) designed according to sociolinguistic principles and cross-combined with the BLS occupational list. Each template explicitly encodes role relations (e.g., “My [person-marking], the [occupation]”), forcing models to activate social identity inference at the syntax–semantics interface and thereby exposing implicit stereotypical associations.
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Synthesis

The survey does not mention BEC-pro and lacks subsequent work criticizing it.
