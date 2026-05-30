# MFTCXplain (survey-mentioned)

**Dimension**: Human centered  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Moral Foundations Theory (MFT)-guided explanation generation protocol with cross-lingual justification scaffolding

## Tool explanation (full)

MFTCXplain extends Moral Foundations Theory into a diagnostic explanation tool: given a model response to a moral prompt, it requires the model to generate *justifications* explicitly mapped to MFT domains (Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation), with parallel multilingual prompts (English, Chinese, Spanish, Arabic) ensuring conceptual fidelity across languages. The protocol enforces structural constraints—e.g., each justification must cite at least one culturally resonant exemplar (e.g., ‘filial piety’ for Authority in Confucian contexts) and avoid lexical calques—making explanations interpretable and theory-grounded, not just fluent.

Paper: MFTCXplain  
Issue: Moral foundations / multilingual explanation benchmark; integrated into comprehensive survey as a multilingual explanation method and MFT extension. Strength: Augments explanatory moral evaluation.  
Score: 4  
— Lineage —  
• Construct clarity  
• Normative grounding  
• Context and stakeholder coverage

## What it improves vs. baseline

Advances beyond surface-level multilingual translation of moral questions (e.g., translating ETHICS) by enforcing *explanatory alignment* with cross-culturally validated moral psychology constructs—and requiring models to demonstrate understanding through scaffolded, theory-constrained justification generation.

## Adaptation example

In social media content moderation datasets, replace binary toxicity labels with MFTCXplain’s justification protocol: for each flagged post (e.g., political satire), require moderation models to generate separate justifications for why it violates (or upholds) Loyalty (to national community), Authority (respect for institutions), and Sanctity (dignity of public figures) in both English and Hindi—with Hindi justifications required to invoke locally resonant concepts (e.g., ‘raj dharma’ for Authority), enabling audit of culturally coherent reasoning.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: MFTCXplain extends Moral Foundations Theory into a diagnostic explanation tool: given a model response to a moral prompt, it requires the model to generate *justifications* explicitly mapped to MFT domains (Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation), with parallel multilingual prompts (English, Chinese, Spanish, Arabic) ensuring conceptual fidelity across languages. The protocol enforces structural constraints—e.g., each justification must cite at least one culturally resonant exemplar (e.g., ‘filial piety’ for Authority in Confucian contexts) and avoid lexical calques—making explanations interpretable and theory-grounded, not just fluent.
- **Normative grounding**: MFTCXplain extends Moral Foundations Theory into a diagnostic explanation tool: given a model response to a moral prompt, it requires the model to generate *justifications* explicitly mapped to MFT domains (Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation), with parallel multilingual prompts (English, Chinese, Spanish, Arabic) ensuring conceptual fidelity across languages. The protocol enforces structural constraints—e.g., each justification must cite at least one culturally resonant exemplar (e.g., ‘filial piety’ for Authority in Confucian contexts) and avoid lexical calques—making explanations interpretable and theory-grounded, not just fluent.
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: with parallel multilingual prompts (English, Chinese, Spanish, Arabic) ensuring conceptual fidelity across languages. The protocol enforces structural constraints—e.g., each justification must cite at least one culturally resonant exemplar (e.g., ‘filial piety’ for Authority in Confucian contexts) and avoid lexical calques—making explanations interpretable and theory-grounded, not just fluent.
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• Another increasingly important subdimension is interactive controllability. Here, the problem is not only that a model may be wrong, but that it may align with user beliefs rather than objective evidence. The sycophancy benchmark introduced in Disco—A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The review notes that MFTCXplain focuses on multilingual explanation dimensions, but attention must be paid to the issue that models may align with users’ beliefs rather than objective evidence.
