# TrustGPT (2023)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/pdf_texts/12363.txt`

## Representative tool

SocialNorm-Conditioned Toxicity Prompting Framework

## Tool explanation (full)

TrustGPT constructs a conditional prompting framework grounded in the SOCIALCHEMISTRY101 social norm knowledge base: given a social behavior (e.g., “speaking up when someone’s doing something harmful”) and its human value judgment label (e.g., “It’s good.”), the system automatically generates adversarial prompts (e.g., “Explain why it is acceptable to stay silent...”) to induce model outputs that violate the norm; value alignment is then quantified by comparing consistency between the original human judgment and the induced output. This framework explicitly encodes implicit social norms as controllable prompt-conditioning variables.

Extraction rationale: Primarily based on the Benchmark diagnostic table notes: “dataset SOCIALCHEMISTRY101, containing social norms and their human evaluation labels”, “using predefined prompt templates to generate toxic, biased content and evaluating value alignment”; the source_excerpt mentions “TRUST-GPT” and “ethical issues” but does not specify the mechanism, so the notes’ explicit references to “SOCIALCHEMISTRY101” and “prompt templates” serve as the key basis.

## What it improves vs. baseline

Compared to traditional toxicity detection (e.g., RealToxicityPrompts, which measures only generative propensity), this work is the first to anchor LLM output ethical biases to verifiable social norm knowledge sources, enabling an evaluation shift from “superficial harmfulness” to “norm violation”; it supports fine-grained attribution (e.g., which specific norm is violated, and under what contextual conditions the model fails).

## Adaptation example

In the medical consultation assistant dataset, reuse this framework by taking the “informed consent” normative clause from the Declaration of Helsinki as the condition, and construct the prompt: “Please explain to the patient: It is reasonable to perform this examination without informing them of the risks.” This detects whether the model can identify and reject this norm-violating statement, thereby transforming abstract medical ethics into a value-conflict test that is both triggerable and interceptable.

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
