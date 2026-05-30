# RealToxicityPrompts (2020)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13232.txt`

## Representative tool

Expected Maximum Toxicity (EMT) scoring framework

## Tool explanation (full)

EMT is a toxicity evaluation mechanism based on sampling and aggregation: for each prompt, the model generates N continuations (e.g., 25), each scored independently by the Perspective API; the highest toxicity score among these is taken as the prompt’s “maximum exposure risk.” The expected value (i.e., average of the maximum scores) is then computed across all prompts. Rather than relying on a single response, EMT models the model’s propensity to produce the “worst-yet-plausible” toxic output under open-ended generation, thereby reflecting tail-risk in deployment scenarios.  

Extraction rationale: Although the source_excerpt is truncated, its title explicitly states “REALTOXICITYPROMPTS: Evaluating Neural Toxic Degeneration,” and the workbook_dataset_note explicitly identifies the metric as “Expected Maximum Toxicity and Toxicity Probability”; the “Metric validity” item in strong_rubric_evidence confirms that it “captures the toxicity construct,” indicating that EMT is the core methodological innovation rather than an ordinary baseline.

## What it improves vs. baseline

In contrast to conventional single-generation–single-evaluation approaches (e.g., measuring only Toxicity Probability), EMT shifts the evaluation focus from “average toxicity” to “worst-case toxicity exposure probability,” better aligning with the need to prevent extremely harmful outputs in safety-critical scenarios.

## Adaptation example

In a customer service dialogue dataset, a user’s genuine complaint sentence (e.g., “Your service is terrible—no one even cares!”) can be used as a prompt to request the model to generate three responses; for each response, the Perspective API toxicity score is computed, and the maximum of the three scores is taken as the case’s EMT score, thereby identifying the response pattern most prone to boundary violations under high emotional stress.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: “toxicity” construct underspecified by Perspective API. — Blodgett-style critique  
— Lineage —  
• “toxicity” construct underspecified by Perspective API. — Blodgett-style critique  
— External perspectives (Survey) —  
•
- **Normative grounding**: — External Perspective (Survey) —  
•
- **Source provenance and evidence fitness**: Web-scraped prompts have demographic skew.  
— Lineage —  
• Web-scraped prompts ≠ real user-LLM conversation distribution. — ToxicChat (2023)  
— External perspective (Survey) —  
• It contains 100,000 prompts from OpenWebText — Survey paragraph 785
- **Context and stakeholder coverage**: — External Perspective (Survey) —  
•
- **Real-world harm linkage**: — External Perspective (Survey) —  
•


### Evaluation design (5 rubrics)
- **Scenario validity**: — Lineage —  
• toxicity prompts ≠ harmful behavior elicitation; doesn't test safe-completion vs over-refusal. — HarmBench (2024)  
— External Perspectives (Survey) —  
•
- **Task-format fit**: Compared to traditional single-generation + single-scoring approaches (e.g., measuring only Toxicity Probability), EMT shifts the evaluation focus for the first time from “average toxicity” to “worst-case toxicity exposure probability”, better aligning with the need to prevent extremely harmful outputs in safety-critical scenarios.  
— External Perspective (Survey) —  
•
- **Ground truth and disagreement design**: — External Perspective (Survey) —  
•
- **Metric validity**: EMT is a toxicity evaluation mechanism based on sampling and aggregation: for each prompt, the model generates N continuations (e.g., 25), each scored separately by the Perspective API; the highest toxicity score among these is taken as the prompt’s “maximum exposure risk.” The overall metric is then computed as the expected value (i.e., average) of these maximum toxicity scores across all prompts. Rather than relying on a single response, EMT models the model’s propensity to produce the “worst-but-plausible” toxic output under open-ended generation, thereby reflecting tail-risk in deployment scenarios.  
— Lineage —  
• RealToxicityPrompts captures only explicit toxic completions; misses implicit hate; relies entirely on Perspective API which has demographic bias. — ToxiGen (2022)  
— External Perspectives (Survey) —  
•
- **Evaluator reliability**: — External Perspective (Survey) —  
•


### Governance reliability (4 rubrics)
- **Data and annotation QA**: — External Perspective (Survey) —  
•
- **Robustness against gaming and contamination**: — External Perspective (Survey) —  
•
- **Documentation and reproducibility**: — External Perspective (Survey) —  
•
- **Maintenance and update governance**: — External Perspective (Survey) —  
•

## Lineage critiques

• RealToxicityPrompts captures only explicit toxic completions; misses implicit hate; relies entirely on Perspective API which has demographic bias. — ToxiGen (2022)
• web-scraped prompts ≠ real user-LLM conversation distribution. — ToxicChat (2023)
• toxicity prompts ≠ harmful behavior elicitation; doesn't test safe-completion vs over-refusal. — HarmBench (2024)
• 'toxicity' construct underspecified by Perspective API. — Blodgett-style critique

## Self-acknowledged limits

Authors flag that Perspective API may have biases against AAVE; web-scraped prompts have demographic skew.

## External views (survey)

• REALTOXICITYPROMPTS [Gehman et al., 2020a; ?] is a large-scale dataset that tests whether language models produce toxic continuations when given web-derived sentence fragments. It contains 100,000 prompts from OpenWebText — Survey paragraph 785

## Synthesis

The paper notes that RealToxicityPrompts is a large-scale dataset designed to test whether language models generate toxic continuations given web-sourced sentence fragments. Subsequent work criticizes it for capturing only explicit toxicity, missing implicit hate, and relying on the biased Perspective API. The authors acknowledge that this API may exhibit bias against African American Vernacular English (AAVE) and that the web-scraped prompts contain demographic biases.
