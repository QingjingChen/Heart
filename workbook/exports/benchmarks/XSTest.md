# XSTest (2024)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13282.txt`

## Representative tool

Controlled Over-refusal Contrast Pair Framework

## Tool explanation (full)

This tool constructs rigorously paired prompt contrast sets: each pair comprises one semantically safe but easily over-refused prompt (e.g., expressing routine requests via synonyms or metaphors) and one semantically unsafe prompt (containing explicit policy-violating intent), matched closely on surface-level linguistic complexity, length, and syntactic structure. Human triple annotation with high inter-annotator agreement (Fleiss’ κ ≥ 0.89) ensures adjudication reliability, specifically designed to quantify model bias in the “safety-helpfulness” trade-off.

Extraction rationale: Primarily based on notes in the Benchmark diagnostic table: “Type: over-refusal contrast pairs”, “450 prompts (250 safe + 200 unsafe)”, “manually annotated by three authors, Fleiss’ κ 0.89–0.97”; moreover, strong_rubric_evidence explicitly lists “over-refusal” as a measured construct, and although source_excerpt is fragmented, it appears in the context of a survey title, confirming its role as a methodological contribution.

## What it improves vs. baseline

In contrast to traditional safety evaluations—which focus solely on whether a model refuses unsafe inputs—this framework is the first to model “over-refusal” as an independent, measurable defect. By using controlled variable methodology to isolate and remove surface-level linguistic interference, the evaluation can precisely identify service capability degradation caused by the model’s overly conservative refusal strategies.

## Adaptation example

In a medical Q&A dataset, for each real patient query (e.g., “How to relieve migraine”), manually construct a semantically safe but lexically vague/metaphorical counterpart (e.g., “What can I do to make my head quiet down, like turning off an old, buzzing air conditioner?”), forming contrastive pairs to evaluate whether medical large language models erroneously reject legitimate health inquiries due to terminological uncertainty.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool constructs rigorously paired prompt contrast sets: each group contains one semantically safe but easily over-refused prompt (e.g., expressing routine requests using synonyms or metaphors) and one semantically unsafe prompt (containing explicit harmful intent), with high matching on surface-level linguistic complexity, length, and syntactic structure.  
— Lineage —  
• complementary; XSTest doesn't test under-refusal. — HarmBench (2024)  
— External perspective (Survey) —  
• XSTest [Röttger et al., 2024] is designed to detect whether a model refuses benign requests when it should not. It aims to reveal whether a model’s pursuit of “harmlessness” comes at the expense of its “helpfulness.” — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Normative grounding**: —
- **Source provenance and evidence fitness**: Discriminative reliability is ensured through manual triple annotation and high inter-annotator agreement (Fleiss’ κ ≥ 0.89).
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Specifically designed to quantify model bias toward the “safety-helpfulness” trade-off.  
— External Perspective (Survey) —  
• XSTest [Röttger et al., 2024] is designed to detect whether a model refuses benign requests when it should not. It aims to reveal whether a model’s pursuit of “harmlessness” comes at the expense of its “helpfulness.” — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Task-format fit**: —
- **Ground truth and disagreement design**: Discriminative reliability is ensured through manual triple annotation and high inter-annotator agreement (Fleiss’ κ ≥ 0.89).
- **Metric validity**: —
- **Evaluator reliability**: Discriminative reliability is ensured through manual triple annotation and high inter-annotator agreement (Fleiss’ κ ≥ 0.89).


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Discriminative reliability is ensured through manual triple annotation and high inter-annotator agreement (Fleiss’ κ ≥ 0.89).
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• complementary; XSTest doesn't test under-refusal. — HarmBench (2024)
• scale 200+250 limited. — SALAD-bench (2024)
• text-only. — MM-SafetyBench (2024)
• English-only over-refusal probes don't transfer. — Multilingual safety surveys

## Self-acknowledged limits

Authors note 450 prompts a diagnostic sample; English; over-refusal types not exhaustive.

## External views (survey)

• XSTest[Ro¨ttgeretal.,2024]isdesignedtodetectwhether a model refuses benign requests when it should not. It aims torevealwhetheramodel’spursuitof”harmlessness”comes attheexpenseofits”helpfulness.” — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The survey states that XSTest is designed to detect whether models reject benign requests when they should not, and to reveal whether pursuing “harmlessness” compromises “helpfulness.” Subsequent work criticizes its limited scale, text-only format, and failure to test under-refusal. The authors acknowledge that the dataset comprises diagnostic samples, is English-only, and does not comprehensively cover over-refusal types.
