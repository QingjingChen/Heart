# BBQ (2022)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/10858.txt`

## Representative tool

Disambiguated-Ambiguous Context Pairing Template

## Tool explanation (full)

BBQ constructs paired contextual templates: for each social dimension (e.g., religion, race), the same core biased proposition is embedded into two types of contexts—ambiguous context (containing stereotypical cues but no factual basis) and disambiguated context (augmented with neutral or counter-stereotypical information to weaken biased cues). Each template pair shares identical question and answer-option structures, differing only in contextual details, enabling isolation of whether the model relies on stereotypes rather than logical reasoning to generate responses.

## What it improves vs. baseline

Compared with earlier monolingual bias evaluation benchmarks (e.g., Winogender or StereoSet), this tool introduces, for the first time, a systematically designed context-controllable contrastive framework, enabling model bias responses to be attributed to contextual ambiguity rather than mere lexical co-occurrence—thereby enhancing attribution rigor and diagnostic granularity.

## Adaptation example

In the Chinese customer service dialogue dataset, ambiguous contexts (e.g., “This elderly customer repeatedly questions the refund process”) and disambiguating contexts (e.g., “This 72-year-old retired teacher repeatedly confirms details due to visual impairment preventing clear reading of the terms”) can be constructed from user complaint texts, while keeping the question “Who is more likely to be unreasonable?” and its answer options unchanged, to detect model sensitivity to age-based stereotypes.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: BBQ constructs paired contextual templates: for each social dimension (e.g., religion, race), the same core biased proposition is embedded into two types of contexts—ambiguous contexts (containing stereotypical cues but no factual grounding) and disambiguated contexts (augmented with neutral or counter-stereotypical information to weaken bias cues). Each template pair shares identical question and answer-option structures, differing only in contextual details, to isolate whether the model relies on stereotypes rather than logical reasoning to answer.  
— External perspective (Survey) —  
• BBQ (Bias Benchmark for QA) [Parrish et al., 2022] is a hand-built dataset designed to evaluate social biases in question answering systems across nine social dimensions in U.S. English contexts. It consists of over 58,000 examples structured into ambiguous and disambiguated contexts, where clear evidence is provided to see if the model’s internal biases override factual information. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Normative grounding**: —
- **Source provenance and evidence fitness**: — Lineage —  
• BBQ (Bias Benchmark for QA) [Parrish et al., 2022] is a hand-built dataset designed to evaluate social biases in question answering systems across nine social dimensions in U.S. English contexts. It consists of over 58,000 examples structured into ambiguous and disambiguated contexts, where clear evidence is provided to see if the model’s internal biases override factual information.
- **Context and stakeholder coverage**: — Lineage —  
• explicitly critiques BBQ for English-only and US categories; ~70% of BBQ items unsuitable for Korean culture; introduces 5 new Korean dimensions. — Jin 2024 (KoBBQ)  
• BBQ misses Chinese-relevant categories like region/hukou/educational background; only 9 dimensions vs 14 in CBBQ. — Huang & Xiong 2024 (CBBQ)
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Each pair of templates shares the same question and option structure, differing only in contextual details, to isolate whether the model relies on stereotypes rather than logical reasoning to answer.  
— External Perspective (Survey) —  
• BBQ (Bias Benchmark for QA) [Parrish et al., 2022] is a hand-built dataset designed to evaluate social biases in question answering systems across nine social dimensions in U.S. English contexts. It consists of over 58,000 examples structured into ambiguous and disambiguated contexts, where clear evidence is provided to see if the model’s internal biases override factual information. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• explicitly critiques BBQ for English-only and US categories; ~70% of BBQ items unsuitable for Korean culture; introduces 5 new Korean dimensions. — Jin 2024 (KoBBQ)
• BBQ misses Chinese-relevant categories like region/hukou/educational background; only 9 dimensions vs 14 in CBBQ. — Huang & Xiong 2024 (CBBQ)
• BBQ's 9 axes are too coarse compared to 600+ HolisticBias descriptors. — Smith 2022 (HolisticBias)

## Self-acknowledged limits

Authors note US-English social biases only; nine categories; relies on attested-stereotype literature.

## External views (survey)

• BBQ (Bias Benchmark for QA) [Parrish et al., 2022] is a hand-built dataset designed to evaluate social biases in question answering systems across nine social dimensions in U.S. English contexts. It consists of over 58,000 examples structured into ambiguous and disambiguated contexts, where clear evidence is provided to see if the model’s internal biases override factual information. — A_Comprehensive_Survey_of_AI_Ethics_Benchmarks

## Synthesis

The survey notes that BBQ is a manually constructed dataset designed to evaluate social biases in question-answering systems within U.S. English contexts, comprising over 58,000 instances across nine dimensions. Subsequent work criticizes its restriction to English and U.S. culture, as well as its coarse-grained dimensions, calling for localization and expansion.
