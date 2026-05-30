# MPCI-Bench (2026)

**Dimension**: Privacy

## Representative tool

First multimodal pairwise contextual-integrity benchmark for LM agents — paired positive/negative instances derived from the same visual source, instantiated across three tiers (normative Seed judgments, context-rich Story reasoning, and executable agent action Traces) via a Tri-Principle Iterative Refinement pipeline; explicitly surfaces a modality-leakage gap where sensitive visual information leaks more frequently than equivalent textual information.

## What it improves vs. baseline

Existing CI benchmarks are largely text-centric and primarily emphasize negative refusal scenarios; MPCI-Bench fills that gap by being multimodal, by using paired positive/negative instances tied to the same visual source (so privacy–utility trade-offs are explicit), and by reaching all the way to executable agent action traces rather than stopping at norm judgments.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: —
- **Normative grounding**: —
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
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

## Self-acknowledged limits

Authors note that current state-of-the-art multimodal models systematically fail to balance privacy and utility, and that modality leakage requires further investigation; coverage of social/cultural CI norms is bounded by the underlying visual sources.

## Synthesis

Compared with existing CI benchmarks (PrivaCI-Bench, ConfAIde, PrivacyLens), MPCI-Bench extends evaluation from pure text to multimodal settings, mandates that models perform positive/negative contrast on the same visual source, and extends the evaluation pipeline from “judgment” to “execution”, thereby revealing cross-modal leakage asymmetry.
