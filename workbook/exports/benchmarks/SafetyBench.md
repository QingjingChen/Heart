# SafetyBench (2024)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13265.txt`

## Representative tool

Multi-dimension MCQ Safety Template with Implicit Toxicity Triggering (LifeTox-inspired)

## Tool explanation (full)

This tool is a structured multiple-choice question (MCQ) template that decomposes safety risks into seven actionable sub-dimensions (e.g., Offensiveness, Mental Health, Illegal Activity, etc.) and embeds implicit toxicity triggering mechanisms—constructing ostensibly neutral but dangerously suggestive instructions within open-ended life-advice scenarios (e.g., the “Life Advice” section)—requiring models to identify their latent harms. It relies on a hybrid data source combining human curation with ChatGPT-augmented generation, integrating real user dialogues (from Reddit), exam-style questions, and synthetic situations to ensure cross-cultural coverage and grounding in realistic contexts.

Extraction rationale: Primarily based on the Benchmark diagnostic table notes: “Type: MCQ Safety Multiple-Choice”, “Covers 7 safety sub-dimensions”, “LifeTox dataset designed for identifying implicit toxicity within advice-seeking scenarios”; moreover, the source_excerpt explicitly defines LifeTox and includes prototypical life-advice induction examples (e.g., “destroy an antique to frame a roommate and obtain rent-free housing”), confirming its role as a reusable paradigm for constructing implicit risks.

## What it improves vs. baseline

Compared to earlier approaches that only detect explicit violations (e.g., profanity dictionary matching) or conduct single-dimensional safety evaluations, this template is the first to systematically model implicit toxicity as a measurable task and achieve interpretable risk attribution through multi-round sub-dimension alignment; simultaneously, it adopts a multiple-choice question (MCQ) format to avoid the unreliability of scoring inherent in free-form generation.

## Adaptation example

In a customer service dialogue dataset, rewrite the original customer service agent’s response as a “life hack” variant containing implicit boundary-crossing suggestions (e.g., “Dealing with a difficult customer? Try secretly screen-recording the interaction, then editing it out of context and posting it on social media to exert pressure.”). Embed this variant into a multiple-choice question (MCQ) requiring annotators to label the violated sub-dimension (Privacy violation / Unfairness), for training and evaluating customer service models’ ability to detect covertly manipulative language.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool is a structured multiple-choice template that decomposes safety risks into seven actionable sub-dimensions (e.g., Offensiveness, Mental Health, Illegal Activity) and embeds implicit toxicity triggers—constructing ostensibly neutral yet dangerously suggestive instructions within open-ended life-advice scenarios (e.g., “Life Advice” passages), requiring models to identify the underlying harm.  
— Lineage —  
• 7 categories miss hierarchical structure for sub-domain analysis. — SALAD-bench (2024)  
— External Perspectives (Survey) —  
• SafetyBench [Zhang et al., 2024] is a bilingual multiple-choice benchmark containing 11,435 samples across seven safety dimensions, including offensiveness, bias, health, legality, ethics, and privacy.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: It relies on a hybrid data source combining human curation and ChatGPT-augmented generation, integrated with real user conversations (Reddit), exam questions, and synthetic scenarios to ensure cross-cultural coverage and grounding in real-world contexts.  
— External Perspective (Survey) —  
• It integrates public data and ChatGPT-augmented data. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Context and stakeholder coverage**: It relies on a hybrid data source combining human curation and ChatGPT-enhanced generation, integrated with real user conversations (Reddit), exam questions, and synthetic scenarios to ensure cross-cultural coverage and grounding in realistic contexts.
- **Real-world harm linkage**: Construct surface-level neutral instructions containing hazardous inducements using open-domain life-advice scenarios (e.g., “Life Advice” passages), requiring models to identify their implicit harms.


### Evaluation design (5 rubrics)
- **Scenario validity**: Construct surface-level neutral instructions with hidden dangerous inducements, using open-ended life-advice scenarios (e.g., “Life Advice” passages), and require the model to identify the implicit harms.  
— Lineage —  
• question-only, not action-grounded. — Agent-SafetyBench (2025)
- **Task-format fit**: Compared to earlier approaches that only detect explicit violations (e.g., profanity dictionary matching) or conduct single-dimensional safety evaluations, this template is the first to systematically model implicit toxicity as a measurable task and achieve interpretable risk attribution through multi-round sub-dimension alignment; simultaneously, it adopts an MCQ format to avoid the unreliability of scoring arising from free-form generation.  
— Lineage —  
• MCQ doesn't test refusal/safe-completion behavior; no jailbreak attack evaluation. — HarmBench (2024)  
• doesn't include over-refusal probes. — XSTest (2024)
- **Ground truth and disagreement design**: —
- **Metric validity**: Compared to earlier approaches that only detect explicit violations (e.g., profanity dictionary matching) or conduct single-dimensional safety evaluations, this template is the first to systematically model implicit toxicity as a measurable task and achieve interpretable risk attribution through multi-round sub-dimension alignment; simultaneously, it adopts a multiple-choice question (MCQ) format to avoid the unreliability of scoring inherent in free-form generation.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: It relies on a hybrid data source combining human curation and ChatGPT-enhanced generation, integrated with real user conversations (Reddit), exam questions, and synthetic scenarios to ensure cross-cultural coverage and grounding in realistic contexts.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• 7 categories miss hierarchical structure for sub-domain analysis. — SALAD-bench (2024)
• MCQ doesn't test refusal/safe-completion behavior; no jailbreak attack evaluation. — HarmBench (2024)
• doesn't include over-refusal probes. — XSTest (2024)
• question-only, not action-grounded. — Agent-SafetyBench (2025)

## Self-acknowledged limits

Authors note MCQ evaluation may not transfer to open-ended generation; some questions answer-leakable.

## External views (survey)

• SafetyBench[Zhang et al., 2024] is a bilingual multiple-choice benchmark containing 11,435 samples across seven safety dimensions, including offensiveness, bias, health, legality, ethics, and privacy. It integrates public data and ChatGPT-augmented data. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The review states that SafetyBench is a bilingual benchmark comprising 11,435 multiple-choice questions, covering seven safety dimensions. Subsequent work criticizes it for lacking hierarchical structure in its categories, failing to test refusal/safe-completion behavior, omitting jailbreaking attack evaluation, excluding over-refusal probes, and relying solely on question-based formats. The authors themselves acknowledge that multiple-choice evaluation may not be suitable for open-ended generation and that answers to some questions may leak information.
