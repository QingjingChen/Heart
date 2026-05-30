# MM-SafetyBench (2024)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13285.txt`

## Representative tool

Cross-Modal Jailbreak Probe Construction Framework

## Tool explanation (full)

This framework systematically constructs text-image collaborative jailbreak samples: first, domain experts design malicious queries (e.g., “how to make a Molotov cocktail”), then GPT-4 extracts keywords to drive Stable Diffusion to generate semantically related or distracting images (e.g., blueprints of a Molotov cocktail vs. a photograph of an artistic glass bottle), forming multimodal adversarial pairs. During evaluation, the model is required to simultaneously refuse the textual request and identify the potential risk in the image, exposing safety vulnerabilities of multimodal large language models (MLLMs) under modality misalignment.

Extraction rationale: Primarily based on the Benchmark diagnostic table’s notes: “Type: Multimodal jailbreak set”, “5,040 text-image pairs, sourced from expert-generated malicious queries and keywords extracted by GPT-4”, “Images generated using Stable Diffusion and Typography”; the source_excerpt contains only the title and a warning statement, with no technical details—thus, the framework is distilled from the three elements in the notes: “multimodal”, “expert + GPT-4”, and “image generation”.

## What it improves vs. baseline

Compared with unimodal safety evaluation (e.g., SafeBench), this work is the first to extend jailbreak detection to cross-modal coupling scenarios, revealing novel evasion patterns such as text being “rationalized” by images or images being “decriminalized” by text, thereby advancing safety evaluation from purely linguistic logic toward perception-language joint reasoning.

## Adaptation example

In the MedVQA medical imaging question-answering dataset, patient queries (e.g., “Does this CT scan show lung cancer?”) are paired with tampered CT images (e.g., with forged nodules superimposed), using this framework to construct “diagnosis-inducing jailbreak” samples to test whether multimodal medical AI systems violate clinical guidelines by issuing definitive conclusions due to image perturbations.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This framework systematically constructs text–image collaborative jailbreaking samples: domain experts first design malicious queries (e.g., “how to make a Molotov cocktail”), then GPT-4 extracts keywords from these queries to drive Stable Diffusion to generate semantically related yet distracting images (e.g., blueprints of a Molotov cocktail versus photographs of artistic glass bottles), thereby forming multimodal adversarial pairs.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: Evaluation requires the model to simultaneously refuse text requests and identify potential risks in images, exposing safety vulnerabilities of MLLMs under modality misalignment. Compared to unimodal safety evaluation (e.g., SafeBench), this work is the first to extend jailbreak detection to cross-modal coupling scenarios, revealing novel evasion patterns such as text being “rationalized” by images or images being “decriminalized” by text.  
— Lineage —  
• MM-SafetyBench focuses on benign-looking text + harmful image; lacks adversarial attack diversity. — JailBreakV (2024)
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: During evaluation, models are required to simultaneously reject text-based requests and identify potential risks in images, thereby exposing safety vulnerabilities of multimodal large language models (MLLMs) under modality misalignment.


### Evaluation design (5 rubrics)
- **Scenario validity**: Compared with unimodal safety evaluation (e.g., SafeBench), this work is the first to extend jailbreak detection to cross-modal coupling scenarios, revealing novel evasion patterns such as text being “rationalized” by images or images being “decriminalized” by text.  
— Lineage —  
• question-only; not action-grounded. — Agent-SafetyBench (2025)
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: Primary basis: Benchmark diagnostic table notes: “Type: Multimodal jailbreak set”, “5,040 text–image pairs, sourced from expert-generated malicious queries and keywords extracted by GPT-4”, “Images generated using Stable Diffusion and Typography”.  
— Lineage —  
• Newer standardization may supersede. — HarmBench (2024)
- **Maintenance and update governance**: —

## Lineage critiques

• MM-SafetyBench focuses on benign-looking text + harmful image; lacks adversarial attack diversity. — JailBreakV (2024)
• question-only; not action-grounded. — Agent-SafetyBench (2025)
• newer standardization may supersede. — HarmBench (2024)

## Self-acknowledged limits

Authors note image generation for typeset-attack may not transfer to natural multimodal queries; English.

## Synthesis

Subsequent work criticizes MM-SafetyBench for lacking adversarial attack diversity, failing to consider action-based scenarios, and potentially being superseded by newer benchmarks. The authors acknowledge that their image-generation methodology may not generalize to natural multimodal queries and is restricted to English-language settings.
