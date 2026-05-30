# CBBQ (2024)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/10858.txt`

## Representative tool

Four-stage human-AI co-authored ambiguous/disambiguated QA template pipeline

## Tool explanation (full)

A four-stage human-AI collaborative construction process: (1) AI-based initial screening of raw texts containing social attribute controversies from CNKI and social media platforms (e.g., Weibo, Zhihu); (2) manual annotation of ambiguity and potential bias direction; (3) expert authoring of dual-version question stems (ambiguous version + disambiguated version); (4) crowdsourced validation of answer option reasonableness and cultural adaptability. The output comprises MCQ-QA pairs covering 14 localized social dimensions (e.g., household registration [hukou], marriage and childbearing, geography), with each pair containing both an ambiguous question and a factually precise question grounded in the same scenario.  
Extraction basis: Primarily drawn from the “4-Step Human-AI Collaborative Question Construction” section in workbook_dataset_note and the explicit description in strong_rubric_evidence stating “ambig+disambig dual-layer; 100k+ Chinese QA × 14 social dimensions (including geography / hukou / marriage / appearance / education, etc.—local dimensions)”. Additionally, source_excerpt states “adapt this benchmark to cultural contexts other than the US because social biases depend heavily on the cultural context”, confirming that its core innovation lies in the cultural adaptability mechanism.

## What it improves vs. baseline

Compared to direct translation or single-point transfer of Western benchmarks such as BBQ, this pipeline—driven by locally sourced corpora and featuring a two-layer contextual design (ambiguous/disambiguating)—significantly enhances representational fidelity and diagnostic discriminability for China-specific structural biases (e.g., *hukou* discrimination, degree stigmatization), thereby overcoming construct distortion arising from cultural literal translation.

## Adaptation example

In an AI-assisted question-generation system for training grassroots civil servants in China, the CBBQ four-stage process is adopted: AI extracts ambiguous statements concerning topics such as “employment of persons with disabilities” and “staffing quotas for rural-hukou teachers” from government bulletins and petition platforms; these statements are then disambiguated by human resources and social security experts to generate policy-comprehension multiple-choice questions (MCQs), which are used to evaluate large language models’ semantic parsing capability regarding domestic fair-employment norms.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Manual annotation of ambiguity and potential bias direction; expert authoring of dual-version prompts (ambiguous version + disambiguated version).  
— External Perspective (Survey) —  
• Building upon the contrastive framework of BBQ, CBBQ [Huang and Xiong, 2024] achieves a profound cultural migration from English-centric contexts to Chinese societal values. Its primary innovation lies in the introduction of 14 social bias dimensions tailored to the Chinese national context.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: A four-stage human-AI collaborative construction process: (1) AI-based initial screening of original texts containing social attribute controversies from CNKI and Weibo/Zhihu.  
— Lineage —  
• AI-assisted generation may amplify model biases; manual review coverage uneven. — Recent Chinese fairness surveys
- **Context and stakeholder coverage**: Generate MCQ-QA pairs covering 14 indigenous social dimensions (e.g., household registration (hukou), marriage and childbearing, region) — each pair comprises an ambiguous question and a factual question grounded in the same scenario.  
— External perspective (Survey) —  
• Its primary innovation lies in the introduction of 14 social bias dimensions tailored to the Chinese national context.
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: Crowdsourced validation of option reasonableness and cultural adaptability  
— Lineage —  
• QA-only; does not test multi-turn or generation drift. — Recent Chinese fairness surveys
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Human annotation of ambiguity and potential bias direction; expert authoring of dual-version prompts (ambiguous version + disambiguated version).  
— Lineage —  
• AI-assisted generation may amplify model biases; manual review coverage uneven. — Recent Chinese fairness surveys
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• AI-assisted generation may amplify model biases; manual review coverage uneven. — Recent Chinese fairness surveys
• QA-only; does not test multi-turn or generation drift. — Recent Chinese fairness surveys

## Self-acknowledged limits

Authors note AI-assistance may inject model bias; some categories (e.g., hukou) are hard to ground in legal sources.

## External views (survey)

• Building upon the contrastive framework of BBQ, CBBQ[Huang and Xiong, 2024] achieves a profound cultural migration from English-centric contexts to Chinese societal values. Its primary innovation lies in the introduction of 14 social bias dimensions tailored to the Chinese national context. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The review notes that CBBQ features significant innovation in cultural adaptation, introducing 14 indigenous social bias dimensions. Subsequent work criticizes its AI-assisted generation for potentially amplifying model biases, uneven manual review coverage, and reliance solely on QA tasks—failing to test multi-turn dialogue or generation drift. The authors acknowledge that AI assistance may introduce model biases, and certain categories (e.g., *hukou*) lack clear grounding in legal sources.
