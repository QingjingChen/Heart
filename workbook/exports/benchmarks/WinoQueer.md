# WinoQueer (2023)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13008.txt`

## Representative tool

Community-in-the-Loop sentence pair generation protocol

## Tool explanation (full)

A method that co-designs with LGBTQ+ community members, identifies genuinely harmful stereotypes through structured surveys, and constructs Winograd-style contrastive sentence pairs (biased vs. non-biased) accordingly. It relies on qualitative feedback and semantic preference annotations from 295 community members to operationalize social identity theory (e.g., gender identity, sexual orientation dimensions) as discriminable linguistic stimuli, ensuring that each sentence pair exhibits systematic differences only in the evaluative polarity of social attributes while maintaining identical grammatical structure.

Extraction basis: Primarily drawn from the “notes” section of the Benchmark diagnostic table, which states: “Community-in-the-Loop—295 LGBTQ+ community members identified genuinely harmful stereotypes, serving as a normative source and a strong example of affected-group participation.” Also supported by explicit descriptions in strong_rubric_evidence regarding community-driven sentence-pair generation, invocation of social identity theory, and linkage to real-world harm.

## What it improves vs. baseline

Compared with earlier automated methods based on word-frequency statistics or generic corpus bias detection, this protocol returns the “authority to define harm” to affected communities, shifting bias measurement from abstract statistical deviations to embodied, contextualized experiences of real-world discrimination, thereby avoiding the normative risk of experts subjectively prescribing stereotypical templates.

## Adaptation example

In a Chinese psychotherapy dialogue dataset, LGBTQ+ help-seekers and counselors jointly annotate dialogue segments containing implicit identity denigration. Paired sentences contrasting “pathologizing labels” versus “affirming statements” are constructed following the WinoQueer protocol (e.g., “Homosexuality is a mental disorder” vs. “Homosexuality is a natural form of sexual orientation diversity”), to evaluate large language models’ identity sensitivity in psychological support tasks.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: A method that engages LGBTQ+ community members as co-designers, identifies genuinely harmful stereotypes through structured surveys, and constructs Winograd-style contrastive sentence pairs (biased vs. non-biased) accordingly. It relies on qualitative feedback and semantic preference annotations from 295 community members to operationalize social identity theory (e.g., gender identity, sexual orientation dimensions) into discriminable linguistic stimuli, ensuring that each sentence pair exhibits systematic variation only in the evaluative polarity of social attributes while maintaining identical grammatical structure.  
— External perspective (Survey) —  
• The WinoQueer dataset is a community-in-the-loop benchmark designed to quantify anti-LGBTQ+ bias in large language models. It consists of over 58,000 examples structured to test model behavior in two scenarios: ambiguous — Survey paragraph 469
- **Normative grounding**: Compared with earlier automated methods based on word-frequency statistics or generic corpus bias detection, this protocol returns the “authority to define harm” to affected communities, shifting bias measurement from abstract statistical deviations to embodied, contextualized experiences of real-world discrimination, thereby avoiding the normative risk of experts subjectively prescribing stereotypical templates.
- **Source provenance and evidence fitness**: A method that co-designs with LGBTQ+ community members, identifies genuinely harmful stereotypes through structured surveys, and constructs Winograd-style contrastive sentence pairs (biased vs. non-biased) accordingly. Relies on qualitative feedback and semantic preference annotations from 295 community members.  
— External perspective (Survey) —  
• The WinoQueer dataset is a community-in-the-loop benchmark designed to quantify anti-LGBTQ+ bias in large language models. It consists of over 58,000 examples structured to test model behavior in two scenarios: ambiguous — Survey paragraph 469
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: Compared with earlier automated methods based on word-frequency statistics or bias detection in general corpora, this protocol returns the “authority to define harm” to affected communities, shifting bias measurement from abstract statistical deviations to embodied, contextualized experiences of real-world discrimination.


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: — Lineage —  
• Generation-side critique: pseudo-log-likelihood metric still intrinsic, not deployment-grounded. — Subsequent work critique
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• Future surveys: still English-only; fluency artifacts in templates. — Future work critique  
• Generation-side critique: pseudo-log-likelihood metric remains intrinsic, not deployment-grounded. — Future work critique

## Self-acknowledged limits

English-only; MLM PLL metric; sample of US-context stereotypes; community covers but cannot exhaust queer identity space.

## External views (survey)

• The WinoQueer dataset is a community-in-the-loop benchmark designed to quantify anti-LGBTQ+ bias in large language models. It consists of over 58,000 examples structured to test model behavior in two scenarios: ambiguous — Survey paragraph 469

## Synthesis

The survey notes that WinoQueer is a community-engaged benchmark designed to quantify anti-LGBTQ+ bias in large language models. Subsequent work criticizes its future investigations as remaining English-only and notes potential fluency issues with its templates; the pseudo-log-likelihood metric remains an intrinsic metric, not deployment-oriented. Self-acknowledged limitations include English-only scope, sampling limited to U.S.-centric stereotypes, and inability to exhaustively cover the full queer identity space.
