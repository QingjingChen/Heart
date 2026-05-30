# HateCheck (2021)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13223.txt`

## Representative tool

Functional test suite with behaviorally-defined test cases

## Tool explanation (full)

HateCheck constructs an MCQ test suite grounded in functional intent rather than surface-level labels: each test case targets a clearly defined detection capability (e.g., “identifying reclaimed slurs” or “distinguishing ironic hate speech”), authored by experts using templates and covering 29 fine-grained behavioral patterns; all cases are paired with gold-standard logical judgments—“should pass” / “should fail”—enabling interpretable pass/fail diagnostics.

Extraction rationale: workbook_dataset_note states it “tests 29 functions, grouped into 11 categories”; strong_rubric_evidence explicitly highlights “Construct clarity” by noting it “tests sub-constructs of hate speech” and cites definitional literature; source_excerpt observes “it makes it difficult to identify specific model weak points”, indirectly affirming that HateCheck’s tool design specifically addresses this challenge.

## What it improves vs. baseline

Breaks through the black-box limitations of traditional binary classification accuracy evaluation, providing attributable and debuggable functional-level diagnostics—for example, identifying that a model fails 92% of the time on “ironic hate speech detection,” while its overall F1 score remains as high as 85%, thereby revealing systemic blind spots masked by aggregate performance.

## Adaptation example

In the medical consultation dataset, functional test cases can be constructed: e.g., “When a patient says ‘I’d rather die than take this medication,’ the model should recognize this as an expression of distress—not genuine suicidal intent (and thus should reject labeling it as a crisis).” Based on this, generate multiple-choice question (MCQ) options to diagnose functional deficiencies in the model’s misclassification of psychological crises.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: HateCheck constructs an MCQ test suite based on functional intent rather than surface-level labels: each test case corresponds to a clearly defined detection capability (e.g., “identifying reclaimed slurs” or “distinguishing sarcastic hate speech”), authored by experts using templates and covering 29 fine-grained behavioral patterns.  
— Lineage —  
• ToxiGen (2022): functional templates are synthetic; miss generative-model-produced implicit hate. — ToxiGen (2022)  
• ToxicChat (2023): English-only and template-based; doesn't capture real user conversational toxicity. — ToxicChat (2023)  
— External perspective (Survey) —  
• HATECHECK’s [Röttger et al., 2021] core idea is functional testing: it replaces random sampling with 29 hand-crafted test categories that capture fine-grained hate-speech expressions and difficult contrastive cases.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: All cases are paired with gold-standard logical judgments of “should pass” or “should reject,” enabling interpretable pass/fail diagnostics.
- **Context and stakeholder coverage**: — Lineage —  
• Multilingual HateCheck (later): English-only original is a coverage gap. — Multilingual HateCheck
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: — Lineage —  
• ToxicChat (2023): English-only and template-based; doesn't capture real user conversational toxicity. — ToxicChat (2023)
- **Task-format fit**: HateCheck constructs a multiple-choice question (MCQ) test set based on functional intent rather than surface-level labels.
- **Ground truth and disagreement design**: All cases are paired with gold-standard logical judgments of “should pass” or “should reject,” enabling interpretable pass/fail diagnostics.
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Authored by experts using a template and covering 29 fine-grained behavioral patterns.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• ToxiGen (2022): functional templates are synthetic; miss generative-model-produced implicit hate. — ToxiGen (2022)
• ToxicChat (2023): English-only and template-based; doesn't capture real user conversational toxicity. — ToxicChat (2023)
• Multilingual HateCheck (later): English-only original is a coverage gap. — Multilingual HateCheck

## Self-acknowledged limits

Authors note English-only; protected groups are limited to 7; functionalities don't cover code-mixing or multimodal hate.

## External views (survey)

• HATECHECK’s [Ro¨ttger et al., 2021] core idea is functional testing: it replaces random sampling with 29 hand-crafted test categories that capture fine-grained hate-speech expressions and difficult contrastive — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The survey states that HateCheck captures fine-grained hate speech expressions through 29 categories of manually crafted test cases. Subsequent work criticizes its template-generated data for failing to capture implicit hate produced by generative models (ToxiGen, 2022) and notes its English-only scope, which prevents it from capturing toxicity in real user conversations (ToxicChat, 2023). The authors themselves acknowledge limitations including English-only coverage, a limited set of protected groups, and the absence of support for code-mixed or multimodal hate.
