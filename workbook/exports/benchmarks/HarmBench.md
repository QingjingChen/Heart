# HarmBench (2024)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/10869.txt`

## Representative tool

Policy-grounded red-teaming taxonomy with explicit red-line vs. disputed-behavior labeling

## Tool explanation (full)

HarmBench constructs its test behaviors by systematically mapping 7 semantic harm categories (e.g., chemical weapons, non-consensual imagery, fraud) to real-world AI usage policies from OpenAI, Anthropic, Meta, and Inflection AI. Crucially, it distinguishes 'red-line' behaviors (explicitly prohibited by law/policy, e.g., bomb-making instructions) from 'disputed' behaviors (context-dependent, dual-use, e.g., jailbreak techniques or deepfake tools), enabling granular refusal robustness measurement via automated classifiers trained on policy-aligned labels.

## What it improves vs. baseline

Introduces normatively anchored categorization—unlike earlier red-teaming efforts that treated all harmful prompts uniformly—thereby enabling differential evaluation of model refusal strength against legally mandated vs. ethically contested behaviors, improving construct validity and policy relevance.

## Adaptation example

In the financial risk control dialogue dataset, reconstruct HarmBench’s taxonomy based on China’s Interim Measures for the Management of Generative Artificial Intelligence Services and the CBIRC’s anti-money laundering guidelines: label “forging bank statements” as red-line (explicitly illegal), and label “teaching users reasonable tax planning” as disputed; then re-annotate 1,000 customer service dialogues using this labeling scheme to drive the model to learn how to provide ambiguous responses within compliance boundaries rather than applying blanket refusal.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: HarmBench constructs its test behaviors by systematically mapping 7 semantic harm categories (e.g., chemical weapons, non-consensual imagery, fraud) to real-world AI usage policies from OpenAI, Anthropic, Meta, and Inflection AI. Crucially, it distinguishes 'red-line' behaviors (explicitly prohibited by law/policy, e.g., bomb-making instructions) from 'disputed' behaviors (context-dependent, dual-use, e.g., jailbreak techniques or deepfake tools), enabling granular refusal robustness measurement via automated classifiers trained on policy-aligned labels.  
— Lineage —  
• “HarmBench's behavior-only design less comprehensive on knowledge-style probes.” — SafetyBench / SALAD-bench  
— External perspectives (Survey) —  
• “HarmBench [Mazeika et al., 2024] is introduced as a standardized evaluation framework that tackles the lack of unified metrics in automated red-teaming for large language models. It builds a hierarchical taxonomy of harmful behaviors and supports large-scale comparisons across 18 red-teaming methods and 33 target models, offering a comprehensive benchmark for safety assessment.” — Survey paragraphs 757–769
- **Normative grounding**: Introduces normatively anchored categorization—unlike earlier red-teaming efforts that treated all harmful prompts uniformly—thereby enabling differential evaluation of model refusal strength against legally mandated vs. ethically contested behaviors, improving construct validity and policy relevance.
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: HarmBench constructs its test behaviors by systematically mapping 7 semantic harm categories (e.g., chemical weapons, non-consensual imagery, fraud) to real-world AI usage policies from OpenAI, Anthropic, Meta, and Inflection AI. Crucially, it distinguishes 'red-line' behaviors (explicitly prohibited by law/policy, e.g., bomb-making instructions) from 'disputed' behaviors (context-dependent, dual-use, e.g., jailbreak techniques or deepfake tools).  
— Lineage —  
• “action-grounded harm not covered.”— Agent-SafetyBench (2025)


### Evaluation design (5 rubrics)
- **Scenario validity**: Enabling granular refusal robustness measurement via automated classifiers trained on policy-aligned labels.  
— Lineage —  
• “HarmBench tests under-refusal but not over-refusal.”— XSTest (2024)  
• “multimodal red-teaming partial.”— JailBreakV (2024)
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: It builds a hierarchical taxonomy of harmful behaviors and supports large-scale comparisons across 18 red-teaming methods and 33 target models, offering a comprehensive benchmark for safety assessment.  
— Survey —  
• “HarmBench [Mazeika et al., 2024] is introduced as a standardized evaluation framework that tackles the lack of unified metrics in automated red-teaming for large language models.” — Survey paragraphs 757–769
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• 「HarmBench tests under-refusal but not over-refusal.」— XSTest (2024)
• 「action-grounded harm not covered.」— Agent-SafetyBench (2025)
• 「multimodal red-teaming partial.」— JailBreakV (2024)
• 「HarmBench's behavior-only design less comprehensive on knowledge-style probes.」— SafetyBench / SALAD-bench

## Self-acknowledged limits

「Authors note 510 behaviors a sample; English; copyright subset US-centric.」

## External views (survey)

• HarmBench [Mazeika et al., 2024] is introduced as a standardized evaluation framework that tackles the lack of unified metrics in automated red-teaming for large language models. It builds a hierarchical taxonomy of harmful behaviors and supports large-scale comparisons across 18 red-teaming methods and 33 target models, offering a comprehensive benchmark for safety assessment. — Survey paragraphs 757–769

## Synthesis

The review states that HarmBench constructs a hierarchical taxonomy of harmful behaviors, supporting large-scale comparisons. Subsequent work criticizes it for testing only under-refusal rather than over-refusal, failing to cover action-oriented harms, providing incomplete multimodal red-teaming tests, and featuring insufficiently comprehensive behavior design. The authors acknowledge that the dataset is a sample, primarily English, and its copyright subset is U.S.-centric.
