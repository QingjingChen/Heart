# EAPrivacy (ICLR 2026)

**Dimension**: Privacy  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Four-tier physical-world privacy benchmark for embodied LLM agents with 400+ procedurally generated scenarios across Sensitive Object Identification, Privacy in Shifting Environments, Inferential Privacy under Task Conflicts, and Social Norms vs Personal Privacy; supports both rating and triplet selection evaluations validated against human raters.

## Tool explanation (full)

This tool defines a four-tier sensitivity scale, progressing from tier_1 (explicit PII text labels, e.g., “ID number: 110...”) to tier_4 (implicit contextual inference, e.g., a blurred face in surveillance camera footage combined with a doorplate number and timestamp enabling resident identification), with each tier corresponding to distinct perceptual modalities and output behaviors of physical AI devices (e.g., smart speakers, domestic robots, security cameras). The task requires the model to determine whether a given physical object representation carries privacy information and to classify it according to the tier level.

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: workbook_dataset_note specifies the “embedded AI physical object privacy identification task”; strong_rubric_evidence cites “construct clarity”, “scenario validity”, and “task-format fit”, all referencing “increasing complexity from tier_1 to tier_4” and “combination of physical objects with privacy information”, directly aligning with this tiered scale design; although source_excerpt is truncated, its title “EAI-Bench” strongly matches the term “embedded AI” in the note.

## What it improves vs. baseline

Breaks through the limitations of traditional text-based privacy evaluation by, for the first time, anchoring privacy risks to multimodal representations of physical-world objects and device behavior chains—enabling evaluation coverage across the full-stack privacy leakage pathway: “sensor acquisition → feature extraction → semantic interpretation → decision output”, rather than relying solely on surface-level textual features.

## Adaptation example

In the smart home device log dataset, relabel raw sensor events (e.g., “Living room camera detected a face at 17:03”) according to a tier ladder: tier_1 (containing clear, identifiable facial images), tier_2 (blurred but preserving hairstyle and clothing features), tier_3 (human silhouette only + room heatmap), tier_4 (Wi-Fi signal fluctuation patterns + door magnetic switch timing sequences), to train and evaluate home AI robustness in recognizing progressively exposed privacy.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool defines a four-tiered sensitivity scale, progressing from tier_1 (explicit PII text labels, e.g., “ID number: 110...”) to tier_4 (implicit contextual inference, e.g., a blurred face in surveillance camera footage combined with a doorplate number and timestamp enabling resident identification).  
— Lineage —  
• Only ~tier_1 is publicly available (10 samples ~ small fraction of full set); embedded AI scenario coverage is narrow. — Cross
- **Normative grounding**: —
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: — Lineage —  
• Not connected to real-world deployment harms (e.g., domestic robots / surveillance cameras).


### Evaluation design (5 rubrics)
- **Scenario validity**: Each layer corresponds to the perception modalities and output behaviors of different physical AI devices (smart speakers, home robots, security cameras).  
— Lineage —  
• Only ~tier_1 is publicly available, with ~10 samples out of the full set; embedded AI scenarios are narrow. — Cross
- **Task-format fit**: The task requires the model to determine whether a given physical object representation carries privacy information and to classify it according to tier levels.  
— Lineage —  
• Only ~tier_1 is publicly available, with ~10 samples—small subset; embedded AI scenario is narrow. — Cross
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• Only ~tier_1 publicly releases 10 samples—small fraction of full set; narrow coverage of embedded AI scenarios. — Cross  
• Not linked to real-world deployment harms (e.g., home robots / surveillance cameras).

## Self-acknowledged limits

Authors note small scale; embodied AI specific; English.

## Synthesis

The survey notes that the EAI-Bench dataset is small in scale and limited to a single scenario. Subsequent work criticizes it for failing to connect to concrete harms arising in real-world deployments. The authors acknowledge limitations including the dataset’s small scale, its specificity to embedded AI, and its restriction to English-language environments.
