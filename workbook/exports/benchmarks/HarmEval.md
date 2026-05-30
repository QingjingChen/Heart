# HarmEval (2025)

**Dimension**: Safety  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Safety Amplification (SA) vector + Safety-guided decoding strategy (sGDS)

## Tool explanation (full)

HarmEval proposes a two-stage safety enhancement mechanism: In the first stage (Safety Amplification), a “safety amplification vector” is computed using demonstration examples annotated for safety; this vector is injected into the language model’s hidden layers to bias token selection. In the second stage (sGDS), the decoding process is dynamically adjusted by fusing or pruning outputs from different distributions (e.g., safe vs. unsafe LM output distributions), prioritizing token sampling from the safety-optimized distribution. This tool relies on instruction-response pairs annotated according to enterprise AI safety policies and requires pre-defined safety-sensitive attribute dimensions.  

— Lineage —  
• Source excerpt explicitly describes the “Safety amplification (SA) phase” and “Safety guided decoding strategy (sGDS)”.  
• Workbook dataset note specifies its foundation in policy mapping, fully aligning with strong_rubric_evidence stating “evaluated per AI provider safety policies”.

## What it improves vs. baseline

Compared with traditional static safety classification evaluations (e.g., binary harmfulness scoring only), this tool internalizes safety constraints as a plug-and-play control mechanism within the generation process, enabling fine-grained, distribution-level safety intervention rather than post-hoc filtering or coarse-grained scoring.

## Adaptation example

In medical Q&A datasets, a demonstration example set can be constructed based on the HIPAA Compliance Guidelines and policies of leading medical AI vendors; the HIPAA-sensitive amplification vector can be extracted, and sGDS can be enabled during generation of patient consultation responses to forcibly suppress token distributions that may leak PHI (Protected Health Information).

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: HarmEval proposes a two-stage safety enhancement mechanism: the first stage (Safety Amplification) computes a “safety amplification vector” using demonstration examples annotated for safety; this vector is injected into the language model’s hidden layers to bias token selection. The second stage (sGDS) dynamically adjusts the decoding process by fusing or pruning outputs from different distributions (e.g., safe vs. unsafe LM output distributions), prioritizing token sampling from the safety-optimized distribution.  
— Survey —  
• HarmEval [Banerjee et al., 2025] is built around the safety policies of major AI providers, organizing risks into 11 policy-violation categories that span safety, social–political harms, economic–privacy risks, and restricted content.
- **Normative grounding**: This tool relies on annotated instruction–response pairs mapped to enterprise AI safety policies and requires predefined dimensions of safety-sensitive attributes.  
— External Perspective (Survey) —  
• HarmEval [Banerjee et al., 2025] is built around the safety policies of major AI providers, organizing risks into 11 policy-violation categories that span safety, social–political harms, economic–privacy risks, and restricted content. — Survey
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: Compared to traditional static safety classification evaluations (e.g., binary harmfulness scoring only), this tool internalizes safety constraints as plug-and-play control mechanisms within the generation process, enabling fine-grained, distribution-level safety intervention—not post-hoc filtering or coarse-grained scoring.  
— Survey —  
• HarmEval [Banerjee et al., 2025] is built around the safety policies of major AI providers, organizing risks into 11 policy-violation categories that span safety, social–political harms, economic–privacy risks, and restricted content.


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

• HarmEval [Banerjee et al., 2025] is built around the safety policies of major AI providers, organizing risks into 11 policy-violation categories that span safety, social–political harms, economic–privacy risks, and restricted content. — Survey

## Synthesis

The review states that HarmEval is built upon the safety policies of major AI providers and categorizes risks into 11 policy violation categories, covering safety, socio-political harms, economic and privacy risks, and restricted content.
