# HolisticBias (2022)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13463.txt`

## Representative tool

HolisticBias Descriptor Bucketing Framework

## Tool explanation (full)

This framework divides 13 identity axes (e.g., ability, age, body type, culture) into fine-grained “descriptor buckets,” such as the ‘Ability’ axis containing terms like ‘Deaf,’ ‘hard-of-hearing,’ and ‘hearing-impaired.’ Within each bucket, semantically similar terms—differing in societal acceptance or stigmatization—are aggregated, and a cloze-style MLM-PLL task measures model prediction preference differences across terms in the same bucket, thereby quantifying bias amplification.  
Paper:  
Issue: Construct clarity  
Score: 5  
— Lineage —  
• Strong_rubric_evidence: “Construct clarity” emphasizes “participatory community co-construction” and “HolisticBiasR measures bias amplification.”  
• Source_excerpt: Explicitly lists the “Axis Bucket Descriptor” structure and provides multiple term examples (e.g., ‘paraplegic’/‘paralyzed’/‘quadriplegic’).  
• Workbook_dataset_note: Specifies scale as “459k prompt × 600 descriptor × 13 demographic axes.”

## What it improves vs. baseline

Compared to coarse-grained evaluation using only a single label (e.g., “disabled”), this framework reveals models’ sensitivity to subtle linguistic stigmatization through term-level bucketing, enabling fine-grained and comparable bias measurement across identity axes, thereby enhancing both semantic coverage and operational precision of the construct.

## Adaptation example

In the medical consultation dataset, descriptor buckets for the “Mental health” axis can be constructed (e.g., “depressed”, “has depression”, “is clinically depressed”, “struggles with low mood”), and patients’ self-reported statements can be formalized into cloze templates (e.g., “The patient reported feeling ______”) to assess large language models’ biases in inferring sentiment polarity and severity when generating diagnostic recommendations.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This framework divides 13 identity axes (e.g., ability, age, body type, culture, etc.) into fine-grained “descriptor buckets,” such as the ‘Ability’ axis containing terms like ‘Deaf,’ ‘hard-of-hearing,’ and ‘hearing-impaired’; each bucket aggregates semantically similar expressions that differ in societal acceptance or stigmatization level, and quantifies bias amplification via a cloze-style MLM-PLL task measuring model prediction preference differences across terms within each bucket.  
— Lineage —  
• Even HolisticBias's LGBTQ+ axis is descriptor-list-based; community endorsement is weaker than WinoQueer's iterative loop. — Felkner 2023 (WinoQueer)  
• Still English/US-centric in descriptor sourcing. — Jin 2024  
• Cultural translation of HolisticBias to Chinese is non-trivial; many descriptors are not applicable. — Huang 2024 (CBBQ)  
— External perspective (Survey) —  
• Recent work such as HolisticBias (Smith et al., 2022) and WinoQueer (Felkner et al., 2023) shows the value of participatory design, where people from affected communities help decide which harms should be represented. — Survey paragraph 645
- **Normative grounding**: —
- **Source provenance and evidence fitness**: — Lineage —  
• still English/US-centric in descriptor sourcing. — Jin 2024  
• cultural translation of HolisticBias to Chinese non-trivial; many descriptors not applicable. — Huang 2024 (CBBQ)
- **Context and stakeholder coverage**: — Lineage —  
• Even HolisticBias's LGBTQ+ axis is descriptor-list-based; community endorsement is weaker than WinoQueer's iterative loop. — Felkner 2023 (WinoQueer)  
— External Perspective (Survey) —  
• Recent work such as HolisticBias (Smith et al., 2022) and WinoQueer (Felkner et al., 2023) shows the value of participatory design, where people from affected communities help decide which harms should be represented. — Survey paragraph 645
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Compared to coarse-grained evaluation using only a single label (e.g., “disabled”), this framework reveals models’ sensitivity to subtle linguistic stigmatization through term-level bucketing, enabling fine-grained and comparable bias measurement across identity axes, thereby enhancing both semantic coverage and operational precision of the construct.
- **Task-format fit**: and quantified bias amplification by measuring the model’s predictive preference differences for terms within each bucket via a cloze-style MLM-PLL task.
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• even HolisticBias's LGBTQ+ axis is descriptor-list-based; community endorsement weaker than WinoQueer's iterative loop. — Felkner 2023 (WinoQueer)
• still English/US-centric in descriptor sourcing. — Jin 2024
• cultural translation of HolisticBias to Chinese non-trivial; many descriptors not applicable. — Huang 2024 (CBBQ)

## Self-acknowledged limits

Authors note descriptors are English; some categories (caste, neurodiversity) under-validated; templates are short.

## External views (survey)

• Recent work such as HolisticBias (Smith et al., 2022) and WinoQueer (Felkner et al., 2023) shows the value of participatory design, where people from affected communities help decide which harms should be represented. — Survey paragraph 645

## Synthesis

The review notes that HolisticBias’s participatory design helps affected communities determine which harms should be represented. Subsequent work criticizes its LGBTQ+ axis for relying on a list of descriptors with weak community endorsement; it remains English- and U.S.-centric; and many descriptors prove inapplicable when translated into Chinese. The authors acknowledge that the descriptors are English-only, certain categories lack sufficient validation, and the templates are relatively short.
