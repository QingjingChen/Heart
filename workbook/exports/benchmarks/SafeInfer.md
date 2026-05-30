# SafeInfer (2025)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13228.txt`

## Representative tool

Context-Adaptive Decoding-Time Safety Alignment (SA phase + HARMEV framework)

## Tool explanation (full)

SafeInfer introduces a two-phase decoding-time safety mechanism: (1) Safety Amplification (SA) phase, which uses safety-optimized demonstrations to steer generation toward ethical guidelines; (2) HARMEV—a context-aware harm evaluation module that dynamically assesses generated tokens for violations across 11 risk categories (e.g., stereotyping, illegal acts), leveraging GPT-4–curated jailbreak prompts and Perspective API toxicity scores as calibration signals. It operates *during* inference—not just post-hoc—by interleaving safety scoring with token sampling.

## What it improves vs. baseline

Moves beyond static prompt filtering or post-hoc toxicity classification by enabling real-time, context-sensitive safety steering during generation—addressing fragility and imbalance in prior safety alignment methods.

## Adaptation example

In the ToxiGen dialogue dataset, integrate HARMEV as a runtime guardrail: during model response generation, score each candidate token sequence against ToxiGen’s 22 bias subtypes using fine-tuned safety demonstrations derived from its annotated harmful utterances, thereby converting static toxicity detection into dynamic mitigation.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Safety Amplification (SA) phase, which uses safety-optimized demonstrations to steer generation toward ethical guidelines; (2) HARMEV — a context-aware harm evaluation module that dynamically assesses generated tokens for violations across 11 risk categories (e.g., stereotyping, illegal acts)  
— Lineage —  
• “safe-aligned model” may be re-attacked through SafeInfer-aware adversaries. — Construct validity
- **Normative grounding**: which uses safety-optimized demonstrations to steer generation toward ethical guidelines
- **Source provenance and evidence fitness**: leveraging GPT-4–curated jailbreak prompts and Perspective API toxicity scores as calibration signals
- **Context and stakeholder coverage**: a context-aware harm evaluation module that dynamically assesses generated tokens for violations across 11 risk categories (e.g., stereotyping, illegal acts)
- **Real-world harm linkage**: dynamically assesses generated tokens for violations across 11 risk categories (e.g., stereotyping, illegal acts)


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: It operates *during* inference—not just post-hoc—by interleaving safety scoring with token sampling
- **Ground truth and disagreement design**: —
- **Metric validity**: HARMEV — a context-aware harm evaluation module that dynamically assesses generated tokens for violations across 11 risk categories (e.g., stereotyping, illegal acts), leveraging GPT-4–curated jailbreak prompts and Perspective API toxicity scores as calibration signals  
— Lineage —  
• HARMEVAL subset less standardized than HarmBench. — HarmBench (2024)
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: leveraging GPT-4–curated jailbreak prompts and Perspective API toxicity scores as calibration signals
- **Robustness against gaming and contamination**: — Lineage —  
• “Safe-aligned model” may be re-attacked through SafeInfer-aware adversaries. — Construct validity
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• HARMEVAL subset less standardized than HarmBench. — HarmBench (2024)
• not action-grounded. — Agent-SafetyBench (2025)
• 'safe-aligned model' may be re-attacked through SafeInfer-aware adversaries. — Construct validity

## Self-acknowledged limits

Authors note safety alignment may be brittle and that knowledge-editing techniques can break SafeInfer.

## External views (survey)

• SafeInfer: context adaptive decoding time safety alignment for large language models. Proceedings of the AAAI Conference on Artificial Intelligence, 39(26):27188–27196, April 2025. — Survey paragraph 1055

## Synthesis

The survey states that SafeInfer is a decoding-time safety alignment method. Subsequent work criticizes its HARMEVAL subset for lower standardization compared to HarmBench and notes that it is not action-based. Moreover, safety-aligned models may be re-attacked by SafeInfer-aware adversaries. The authors acknowledge that safety alignment may be fragile and that knowledge editing techniques can undermine SafeInfer.
