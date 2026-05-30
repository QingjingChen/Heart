# NeuTral-WinoBiasPlus (2021)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13473.txt`

## Representative tool

Grammar-Aware Gender-Neutral Rewriting Template

## Tool explanation (full)

This tool is a structured rewriting rule template that mandates models to simultaneously satisfy grammatical correctness and semantic fidelity across three dimensions: pronoun substitution (he/she → they), possessive conversion (his/her → their), and subject-verb agreement adjustment (e.g., “He is” → “They are”). Its construction relies on the original biased sentence pairs from WinoBias+, syntactic patterns of natural dialogue from OpenSubtitles, and neutral expression distribution statistics extracted from large-scale Reddit corpora; expert annotation combined with crowdsourced validation ensures rewritten outputs comply with linguistic norms such as APA Style 7th edition, thereby elevating gender neutrality from simple pronoun substitution to a systematic, cross-grammatical-level capability evaluation.

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes, which explicitly state its expansion “from simple he/she replacement to grammatical consistency and semantic preservation,” and the workbook_note, which emphasizes that “sub-dimensions include pronoun conversion, possessive conversion, and subject-verb agreement adjustment”; the Construct clarity score of 4 in strong_rubric_evidence further corroborates that this multidimensional template design is recognized as a clear construct implementation.

## What it improves vs. baseline

Compared to earlier benchmarks that only perform single-pronoun substitution (e.g., he/she) — such as WinoBias — this tool introduces grammatical consistency constraints and a multi-level transformation coordination mechanism for the first time, avoiding evaluation distortion caused by grammatical errors like “they is”, thereby ensuring that neutrality evaluation genuinely reflects the model’s language generation robustness rather than superficial token matching.

## Adaptation example

In customer service dialogue datasets, the user’s original request (e.g., “My husband needs help with his account”) can be fed into this template to force-generation of a grammatically compliant, neutral version (“My spouse needs help with their account”), and rewriting consistency scores—measuring whether all three transformation types are simultaneously applied—replace traditional BLEU evaluation to diagnose inclusivity language generation deficiencies in customer-service LLMs deployed in real-world service scenarios.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool is a set of structured rewriting rule templates that enforce the model to simultaneously satisfy grammatical correctness and semantic fidelity in three aspects: pronoun substitution (e.g., “he/she” → “they”), possessive transformation (e.g., “his/her” → “their”), and subject–verb agreement adjustment (e.g., “He is” → “They are”).
- **Normative grounding**: Ensuring rewritten outputs comply with linguistic norms such as APA Style 7th Edition through expert annotation combined with crowdsourced validation, thereby elevating gender neutrality from simple pronoun substitution to a systematic evaluation of cross-grammatical-level capability.  
— Lineage —  
• neutral 'they' is one step but does not capture LGBTQ+ identities or stereotypes. — Felkner 2023 (WinoQueer)  
• one-axis (gender) rewriter does not cover other identities. — Smith 2022 (HolisticBias)
- **Source provenance and evidence fitness**: Its construction relies on the original biased sentence pairs from WinoBias+, syntactic patterns of natural dialogue from OpenSubtitles, and statistical distributions of neutral expressions extracted from a large-scale Reddit corpus.
- **Context and stakeholder coverage**: — Lineage —  
• Neutral "they" is one step but does not capture LGBTQ+ identities or stereotypes. — Felkner 2023 (WinoQueer)  
• One-axis (gender) rewriter does not cover other identities. — Smith 2022 (HolisticBias)
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Expert annotation combined with crowdsourced validation ensures that the rewritten outputs comply with linguistic norms such as APA Style 7th edition.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• neutral 'they' is one step but does not capture LGBTQ+ identities or stereotypes. — Felkner 2023 (WinoQueer)
• one-axis (gender) rewriter does not cover other identities. — Smith 2022 (HolisticBias)
• Pre-trained MT models perform poorly on neutral forms in many languages — extension to non-English limited.

## Self-acknowledged limits

English-only; rule-based fallback for uncovered constructions; evaluates rewriting quality, not downstream harm.

## Synthesis

Subsequent work criticizes NeuTral-WinoBiasPlus for using only the neutral pronoun “they”, failing to cover LGBTQ+ identities or stereotypes (Felkner 2023), and focusing solely on the gender dimension while ignoring other identities (Smith 2022). Moreover, pre-trained MT models perform poorly on neutral forms in many languages, limiting their extension to non-English environments. The authors acknowledge limitations including English-only scope, insufficient rule coverage, and lack of downstream harm evaluation.
