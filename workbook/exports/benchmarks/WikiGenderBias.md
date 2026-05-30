# WikiGenderBias (2020)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13012.txt`

## Representative tool

Gender-Sensitive Relation Schema (GSRS) with disparity-aware relation extraction evaluation

## Tool explanation (full)

GSRS is a structured relation extraction bias diagnostic protocol: it defines four gender-sensitive relations (spouse, occupation, birthdate, birthplace), extracts entity triples with explicit gender markers from Wikipedia/DBPedia (e.g., HeadEntity=Robert M. Kimmitt, Relation=occupation, TailEntity=Treasury official), and computes the disparity score for each relation type as the absolute difference in F1 scores between male and female head entities (Disparity Score = |F1_male − F1_female|). This tool maps the social construct (gender equality of opportunity) onto concrete relation-type selection and extraction stability, relying on the distribution of structured biases present in real-world encyclopedic text.

Extraction basis: Primarily drawn from benchmark diagnostic table notes: workbook_dataset_note explicitly states “Type: Relation Extraction Bias Dataset”, “Sub-dimension: spouse, occupation, birthdate, and birthplace relations”, and cites “Social Identity Theory”; strong_rubric_evidence assigns a Normative grounding score of 4, annotated as “grounded in fairness principles, particularly equal opportunity”, confirming GSRS as its normative anchor; source_excerpt—though fragmentary—mentions “gender bias in Neural Relation Extraction” and “social biases exhibited in NRE systems”, aligning with the notes.

## What it improves vs. baseline

Compared to general-purpose RE benchmarks (e.g., TACRED), which ignore social attribute dimensions or report only overall accuracy, GSRS is the first to embed fairness requirements directly into the relation schema design layer—thereby tightly coupling bias measurement with task structure and enabling fine-grained attribution (e.g., identifying that models extract “occupation” relations significantly less accurately for women than for men).

## Adaptation example

In the Financial News Entity Relation Dataset, extend the GSRS schema to include the 'board_member_of' and 'founder_of' relations; extract corporate executive triples from Bloomberg/Reuters reports; compute the gap in model-extracted F1 scores for the 'founder_of' relation between female and male CEOs; diagnose whether this reflects systematic under-recognition of women’s founder identity.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Define four gender-sensitive relations (spouse, occupation, birthdate, birthplace), extract entity triples with explicit gender markers from Wikipedia/DBPedia (e.g., HeadEntity = Robert M. Kimmitt, Relation = occupation, TailEntity = Treasury official), and compare model F1 scores for extracting the same relation type when the head entity is male versus female (Disparity Score = |F1_male − F1_female|).  
— Lineage —  
• RE-only; dimensional coverage limited to 4 relations. — Smith 2022 (HolisticBias)
- **Normative grounding**: This tool maps the social construct (gender equal opportunity) onto specific relation type selection and extraction stability, relying on the structured bias distribution observed in real-world encyclopedic texts.
- **Source provenance and evidence fitness**: Extract gender-annotated entity triples from Wikipedia/DBPedia.  
— Lineage —  
• Wikipedia source skews male-biased; data inherits encyclopedic biases. — Smith 2022 (HolisticBias)  
— External Perspectives (Survey) —  
• The WikiGenderBias [Gaut et al., 2020] is a diagnostic benchmark specifically designed for neural relation extraction, consisting of over 45,000 sentences extracted from Wikipedia via distant supervision. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Context and stakeholder coverage**: — Lineage —  
• binary gender; LGBTQ+ erased. — Felkner 2023
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: GSRS is the first benchmark to embed fairness requirements into the relational schema design layer, tightly coupling bias measurement with task structure and enabling fine-grained attribution (e.g., identifying that the model extracts occupations for female entities significantly less accurately than for male entities).
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: The disparity score is defined as the absolute difference between the F1 scores for relation extraction on male and female head entities for the same relation type: Disparity Score = |F1\_male − F1\_female|.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• RE-only; dimensional coverage limited to 4 relations. — Smith 2022 (HolisticBias)
• Wikipedia source skews male-biased; data inherits encyclopedic biases. — Smith 2022 (HolisticBias)
• binary gender; LGBTQ+ erased. — Felkner 2023

## Self-acknowledged limits

Authors note Wikipedia underrepresents women (~18% of biographies); 4 relations only.

## External views (survey)

• The WikiGenderBias[Gaut et al., 2020] is a diagnostic benchmark specifically designed for neural relation extraction, consisting of over 45,000 sentences extracted from Wikipedia via distant supervision. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The survey states that WikiGenderBias is a diagnostic benchmark specifically designed for neural relation extraction, comprising over 45,000 sentences sourced from Wikipedia. Subsequent work criticizes it for covering only four relations and inheriting gender bias from Wikipedia, while overlooking LGBTQ+ populations. The authors acknowledge that biographies of women constitute only ~18% of Wikipedia’s biographical content and that the dataset covers only four relations.
