# Chinese-Safeguard (2024)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13270.txt`

## Representative tool

China-specific safeguard refusal taxonomy with policy-aligned multi-tier labeling schema

## Tool explanation (full)

This tool defines five categories of localized risks—covering China’s Measures for the Administration of Generative AI Services, the Cybersecurity Law, and mainstream platform policies—namely: political sensitivity, criminal or illegal activities, ethics and morality, personal privacy, and protection of minors. Under each category, representative prompt templates and expected response patterns (refused / refused-or-careful / informative-with-safeguards) are specified. The annotation process employs a collaborative expert-writing + LLM-as-judge approach, yielding a hierarchical refusal-behavior evaluation framework explicitly mapped to regulatory red lines.

Extraction rationale: Primarily based on the “layered by China-specific risk categories” and “content moderation classification grounded in China’s Measures for the Administration of Generative AI Services + Cybersecurity Law + mainstream platform policies” notes in the Benchmark diagnostic table; the source_excerpt states “localize the dataset to Mandarin Chinese” and “align it with country-specific AI generation regulations”.

## What it improves vs. baseline

Compared with general English refusal datasets (e.g., Do-not-answer), it implements a three-tier regulatory anchoring framework—laws, policies, and platform rules—and operationalizes the abstract concept of “safeguard” into a response classification system bounded by China’s administrative authority, thereby enabling verifiable compliance evaluation.

## Adaptation example

In a government Q&A dataset, replace originally vague phrasings such as 'the status of Taiwan' or 'rights of Hong Kong/Macao residents' with precise wordings that comply with the Anti-Secession Law and the Hong Kong National Security Law (e.g., 'Under Article 31 of the Constitution of the People's Republic of China, who determines the system to be instituted in a Special Administrative Region?'), and require the model's response to cite the specific legal article number; otherwise the answer is classified as refused-or-careful — thereby enforcing explicit legal grounding.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool defines five categories of localized risks—covering China’s Measures for the Administration of Generative AI Services, the Cybersecurity Law, and mainstream platform policies: political sensitivity, criminal or illegal activities, ethics and morality, personal privacy, and protection of minors. Under each category, typical prompt templates and expected response patterns are specified (refused / refused-or-careful / informative-with-safeguards).  
— Lineage —  
• flat taxonomy. — SALAD-bench (2024)
- **Normative grounding**: and employ a collaborative annotation approach combining expert-written labels with LLM-as-judge evaluation to construct a hierarchical refusal-behavior assessment framework that is explicitly mapped to regulatory red lines.
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: Compared with general English refusal datasets (e.g., Do-not-answer), it implements a three-tier regulatory anchoring framework—laws, policies, and platform rules—and operationalizes the abstract concept of “safeguard” into a response classification system bounded by China’s administrative authority, thereby enabling verifiable compliance evaluation.
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: — Lineage —  
• single-turn refusal-only. — Agent-SafetyBench (2025)
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: and employ collaborative annotation combining expert-written labels with LLM-as-judge evaluation.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• smaller scale; flat taxonomy. — SALAD-bench (2024)
• single-turn refusal-only. — Agent-SafetyBench (2025)
• text-only. — MM-SafetyBench (2024)

## Self-acknowledged limits

Authors note Chinese-specific framing limits cross-cultural transfer; LLM-as-judge for policy compliance has variance.

## Synthesis

Subsequent work criticizes it for its small scale, flat classification system, restriction to single-turn refusal tasks only, and text-only format. The authors acknowledge that the Chinese-specific framework limits cross-cultural transferability and that policy compliance in LLM-as-judge evaluations exhibits variability.
