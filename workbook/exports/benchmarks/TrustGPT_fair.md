# TrustGPT (2023)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/12363.txt`

## Representative tool

SocialNorm-Grounded Cloze Task with Multi-Attribute Toxicity Anchoring

## Tool explanation (full)

This tool converts social norm statements from SOCIALCHEMISTRY101 into cloze-style fill-in-the-blank questions (e.g., “speak up when others do harmful things” → options A/B/C corresponding to “can/can’t/good/bad”) and uses the PERSPECTIVE API to compute multi-dimensional toxicity scores (e.g., gender, race, religion) for each option text, thereby forming a bias evaluation task anchored in empirically grounded social norms and calibrated via quantifiable toxicity scores.  
Paper: SOCIALCHEMISTRY101  
Issue: Bias evaluation via cloze-style social norm probes calibrated with PERSPECTIVE API toxicity scores  
Score: 3  
— Lineage —  
• Benchmark diagnostic table notes explicitly state: data source is SOCIALCHEMISTRY101; cloze template is used; social norm theory is cited; average toxicity scores are computed using the PERSPECTIVE API.  
• In strong_rubric_evidence, both Construct clarity and Source provenance receive scores of 3, reflecting the anchoring method’s strengthening effect on construct definition and data provenance.

## What it improves vs. baseline

Unlike general toxicity detection (e.g., ToxiGen) or abstract value-based question answering, this tool embeds bias evaluation within concrete social behavioral contexts and achieves cross-attribute (gender/race/religion) comparability through external API toxicity scores, thereby enhancing construct operational validity.

## Adaptation example

In a social media content moderation training dataset, user comments (e.g., “He is unsuitable to be a teacher because he is too emotional”) are rewritten as cloze-style prompts, with answer options covering responses such as “suitable,” “unsuitable,” and “requires training.” The PERSPECTIVE API is used to annotate each option with gender bias scores, enabling the training of moderation models to identify implicit stereotypical expressions.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool converts social norm statements from SOCIALCHEMISTRY101 into cloze-style fill-in-the-blank questions (e.g., “speak up when others do harmful things” → options A/B/C corresponding to “okay”/“good”/“not okay”) and uses the PERSPECTIVE API to score each option text across multiple toxicity dimensions (gender, race, religion, etc.), thereby constructing a bias evaluation task anchored in empirically grounded social norms and calibrated by quantifiable toxicity scores.  
— Lineage —  
• TrustGPT’s three axes mixed without clear operationalization. — Construct validity literature
- **Normative grounding**: —
- **Source provenance and evidence fitness**: This tool converts social norm statements from SOCIAL-CHEM-101 into cloze-style multiple-choice questions (e.g., “speak up when others do something harmful” → options A/B/C corresponding to “okay”/“good”/“bad”) and employs the PERSPECTIVE API to assign multi-dimensional toxicity scores (e.g., gender, race, religion) to each option’s text.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Unlike general toxicity detection (e.g., ToxiGen) or abstract value-based question answering, this tool embeds bias evaluation within concrete social behavioral contexts and achieves cross-attribute (gender/race/religion) comparability through external API toxicity scores, thereby enhancing construct operational validity.
- **Task-format fit**: This tool converts social norm statements from SOCIAL-CHEM-101 into cloze-style multiple-choice questions (e.g., “speaking up when others do something harmful” → options A/B/C correspond to “permissible”/“good”/“bad”).
- **Ground truth and disagreement design**: —
- **Metric validity**: and employed the PERSPECTIVE API to compute multi-dimensional toxicity scores (e.g., gender, race, religion) for each option text, thereby constructing a bias evaluation task anchored in empirical social norms and calibrated by quantifiable toxicity scores.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• broader trustworthiness coverage; TrustGPT's value-alignment narrowly defined. — TrustLLM (2024)
• doesn't cover sycophancy. — Sycophancy (2025)
• TrustGPT's three axes mixed without clear operationalization. — Construct validity literature

## Self-acknowledged limits

Authors flag work-in-progress; metrics heuristic.

## Synthesis

Subsequent work criticizes TrustGPT’s value alignment definition as narrow, failing to cover sycophantic behavior, and notes that its three axes are conflated. The authors acknowledge it as ongoing work and describe the metrics as heuristic.
