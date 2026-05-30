# KoBBQ (2024)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/10858.txt`

## Representative tool

BBQ cultural filter + Korea-specific dimension re-engineering framework

## Tool explanation (full)

A systematic cultural adaptation methodology: First, apply “cultural suitability filtering” to the original BBQ template—removing approximately 70% of items unsuitable for the Korean sociocultural context. Second, redefine and expand the 12 protected attribute dimensions based on Korean social surveys and expert consensus—five of which are Korea-specific: region, military status, marital status, education level, and family structure. For each dimension, option logic is designed to align with Korean stereotypical associations (e.g., high SES linked to drug use).

Extraction rationale: Primarily drawn from the workbook_dataset_note (“filtering ~70% of BBQ items as culturally unsuitable”) and strong_rubric_evidence (“76k Korean-language QA pairs × 12 categories, including 5 Korea-specific: region / military / marital / education / family-structure”), and reinforced by repeated emphasis in source_excerpt that “this benchmark must be adapted to cultural contexts other than the US because social biases depend heavily on the cultural context”—confirming that its core mechanism is a culture-aware dimensional reconstruction.

## What it improves vs. baseline

In contrast to simple localization translation or incremental addition of a few dimensions, this framework emphasizes “filtering first, then re-engineering,” ensuring that all retained or newly added items are empirically grounded in Korean societal cognition, thereby preventing the erroneous projection of U.S.-contextual bias patterns onto Korea and enhancing both cultural validity and measurement specificity of the construct.

## Adaptation example

Constructing a dataset for AI assistants in Japanese workplaces using the KoBBQ framework: first applying “Japanese cultural filtering” to the Japanese translation of BBQ (removing questions unrelated to Japan’s lifetime employment system and seniority-based wage/promotion system), then augmenting with dimensions from Japan’s Ministry of Health, Labour and Welfare’s White Paper on Workplace Discrimination—such as “non-regular employees (part-timers)”, “older workers (65+)”, and “workers from regional areas (hometown bias)”—to generate QA pairs that assess whether models reinforce implicit discrimination in Japanese workplaces.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: First, a “cultural appropriateness filter” is applied to the original BBQ template, removing approximately 70\% of items deemed unsuitable for the Korean sociocultural context. Subsequently, based on Korean social surveys and expert consensus, 12 protected attribute dimensions are redefined and expanded—five of which are Korea-specific: region, military status, marital status, education level, and family structure. For each dimension, response options are designed to align with prevalent Korean stereotypical associations (e.g., high socioeconomic status linked with drug use).
- **Normative grounding**: —
- **Source provenance and evidence fitness**: The core tool is a culture-aware dimensional reconstruction mechanism, primarily grounded in the “filtering BBQ inapplicable ~70\%” note from workbook\_dataset\_note and the “76k Korean QA × 12 categories (5 Korean-local: region / military / marital / education / family-structure)” specification from strong\_rubric\_evidence, and further substantiated by repeated emphasis in source\_excerpt on “adapting this benchmark to cultural contexts other than the US because social biases depend heavily on the cultural context.”
- **Context and stakeholder coverage**: Compared to simple localization translation or incrementally adding a few dimensions, this framework emphasizes “filter first, then re-engineer,” ensuring that all retained or newly added items are empirically grounded in Korean local sociocognitive evidence—thereby avoiding the erroneous projection of U.S.-contextual bias patterns onto Korea and enhancing the construct’s cultural validity and measurement specificity.  
— Lineage —  
• Coverage of Korean dialects/regions partial.
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: — Lineage —  
• Future surveys: still QA-only; not generation; LLM judge variance.
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: — External Perspective (Survey) —  
• BBQ’s modular design has already enabled more than eight cultural and linguistic extensions (e.g., CBBQ, KoBBQ, BharatBBQ, JBBQ), demonstrating far greater scalability than earlier benchmarks. — Survey

## Lineage critiques

• Future surveys: still QA-only; not generation; LLM judge variance.
• Coverage of Korean dialects/regions partial.

## Self-acknowledged limits

Authors note ambiguous-context labels reflect Korean majority view; LLM-as-judge calibration limited.

## External views (survey)

• BBQ’s modular design has already enabled more than eight cultural and linguistic extensions (e.g., CBBQ, KoBBQ, BharatBBQ, JBBQ), demonstrating far greater scalability than earlier benchmarks. — Survey

## Synthesis

The survey notes that KoBBQ demonstrates the scalability of BBQ’s modular design; however, subsequent work criticizes it as still QA-only—failing to cover generative tasks—and highlights variability issues when LLMs serve as evaluators. The authors acknowledge that ambiguous scenario labels reflect the majority view in Korea and that calibration of LLMs as evaluators remains limited. Moreover, coverage of Korean dialects and regions is incomplete.
