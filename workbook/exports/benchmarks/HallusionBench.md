# HallusionBench (2024)

**Dimension**: Trustworthy  **Source / path**: `/private/tmp/pdf_texts_trust/12263.txt`

## Representative tool

Temporal-Sequence Image Reversal Diagnostic Protocol

## Tool explanation (full)

HallusionBench designs a diagnostic protocol for multimodal hallucinations: for the same event (e.g., “Homer Simpson walks into a bush”), it collects a forward-temporal image sequence (original sequence) and a manually reversed-temporal image sequence (reversed sequence), and asks the model the same question (e.g., “Does he disappear into the bush?”) for both sequences; if the model gives identical answers to both sequences, it is deemed incapable of genuinely reasoning about temporal causal logic and instead relies solely on static visual cues—thereby producing hallucinations. This protocol exposes the model’s fragility in modeling dynamic processes by artificially injecting temporal counterfactuals.  

Extraction basis: Directly grounded in the source_excerpt example: “Prompt: According to the positive sequence images... Original sequence Answer: Yes. Reversed sequence Answer: No. GPT-4V: Yes...”; additionally, the notes emphasize “diagnosing entangled linguistic hallucinations and visual illusions”, confirming this protocol as its core methodological innovation—not a generic multimodal benchmark.

## What it improves vs. baseline

In contrast to single-image hallucination detection (e.g., POPE, MME), this work introduces controllable temporal counterfactual perturbations for the first time, elevating hallucination evaluation from “static factual errors” to “dynamic reasoning breakdown” diagnosis; it requires no external knowledge base or human rewriting, constructing strong interference tests solely via image sequence manipulation.

## Adaptation example

In the autonomous driving scene understanding dataset, reuse this protocol to collect positive-frame sequences (“vehicle lane-changing”: left lane → center → right lane) and reverse-frame sequences (right → center → left) for the “vehicle lane-changing” event; ask the question “Is the vehicle entering the right lane?” to detect whether the model misjudges lane-changing intent due to temporal confusion—thereby transferring HallusionBench’s causal hallucination diagnosis to safety-critical decision chains.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: HallusionBench designs a diagnostic protocol for multimodal hallucinations: for the same event (e.g., “Homer Simpson walks into a bush”), it collects a forward-temporal image sequence (original\_sequence) and a manually reversed temporal image sequence (reversed\_sequence), and asks the model the same question (e.g., “Does he disappear into the bush?”) for both sequences; if the model gives identical answers to the two sequences, it is deemed incapable of genuinely reasoning about temporal causality and instead relies solely on static visual cues—thereby producing hallucinations.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: Compared with single-image hallucination detection (e.g., POPE, MME), this work introduces, for the first time, controllable temporal counterfactual perturbations, elevating hallucination evaluation from “static factual errors” to “dynamic reasoning breakdown” diagnosis; it requires no external knowledge base or manual rewriting, and constructs strong interference tests solely via image-sequence manipulation.  
— Lineage —  
• “PatentEval / domain trustworthy: domain-specific hallucination not covered.” — PatentEval
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: In contrast to single-image hallucination detection (e.g., POPE, MME), this work introduces controllable temporal counterfactual perturbations for the first time, elevating hallucination evaluation from “static factual errors” to “dynamic reasoning breakdown” diagnosis; it requires no external knowledge base or human rewriting, constructing strong interference tests solely via image sequence manipulation.
- **Task-format fit**: HallusionBench designs a diagnostic protocol for multimodal hallucinations: for the same event (e.g., Homer Simpson walking into a bush), it collects a forward-timed image sequence (original sequence) and a manually reversed-timed image sequence (reversed sequence), and asks the model the same question (e.g., “Did he disappear into the bush?”) for both sequences; if the model gives the same answer for both sequences, it is judged to lack genuine understanding of temporal causal logic and instead relies solely on static visual cues to generate hallucinations.  
— Lineage —  
• “TrustLLM-MM extensions: HallusionBench focuses on visual; LLM-judge for entanglement diagnosis has noise.” — TrustLLM-MM
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: — Lineage —  
• "TrustLLM-MM extensions: HallusionBench focuses on visual; LLM-judge for entanglement diagnosis has noise." — TrustLLM-MM


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: — Lineage —  
• "Recent surveys: 1k size limits subgroup analysis."— Recent surveys
- **Maintenance and update governance**: —

## Lineage critiques

• 「TrustLLM-MM extensions: HallusionBench focuses on visual; LLM-judge for entanglement diagnosis has noise.」— TrustLLM-MM
• 「PatentEval / domain trustworthy: domain-specific hallucination not covered.」— PatentEval
• 「Recent surveys: 1k size limits subgroup analysis.」— Recent surveys

## Self-acknowledged limits

「Authors note image generation may transfer poorly; LLM judge variance.」

## External views (survey)

• 「Hallusionbench: An advanced diagnostic suite for entangled language hallucination and visual illusion in large vision-language models. arXiv preprint arXiv:2310.14566, 2023.」— Survey

## Synthesis

The paper states that HallusionBench is a diagnostic suite for evaluating language hallucinations and visual illusions in multimodal models. Subsequent work criticizes it for primarily focusing on the visual aspect, containing noise in LLM-based judgments, failing to cover domain-specific hallucinations, and having dataset size limitations that restrict subgroup analysis. The authors acknowledge that image generation may perform poorly and that LLM-based judgments exhibit variance.
