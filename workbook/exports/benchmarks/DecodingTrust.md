# DecodingTrust (2023)

**Dimension**: Trustworthy  **Source / path**: `Paper: Wang et al. - DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models  
Issue: Privacy  
Score: 3  
— Lineage —  
• The paper introduces DecodingTrust, a benchmark for evaluating the trustworthiness of large language models (LLMs), with privacy as one of six core dimensions.  
• Privacy evaluation focuses on model behavior regarding sensitive personal information, including memorization of training data, leakage of private information from prompts, and compliance with privacy-preserving instructions (e.g., “Do not disclose personal details”).  
• The benchmark includes three privacy subtasks: (1) Membership inference (detecting whether a given sample was in the training set), (2) Attribute inference (inferring sensitive attributes such as gender or age from model outputs), and (3) Privacy instruction following (assessing adherence to explicit privacy constraints in prompts).  
• Evaluation uses both synthetic and real-world datasets, including subsets of PII-identified text from C4 and custom-curated prompts containing personally identifiable information (PII).  
• Results show that GPT-family models exhibit non-negligible privacy risks: e.g., up to 68% success rate in membership inference attacks; significant attribute leakage across demographic categories; and inconsistent compliance with privacy instructions—even when explicitly instructed not to reveal PII, models sometimes output it.  
• The paper acknowledges limitations: evaluations rely on static prompt-based testing without dynamic adversarial probing; no assessment of differential privacy guarantees or formal privacy bounds; and limited coverage of cross-cultural privacy norms.`

## Representative tool

Multi-Dimensional Trust Scorecard

## Tool explanation (full)

This tool is a modular evaluation suite that provides independent yet aligned assessment protocols for each trustworthiness dimension—factual consistency, safety, fairness, privacy, and robustness—unified under a ternary structure of “prompt + reference answer + adversarial perturbation set.” It outputs standardized scores (0–1) per dimension and a cross-dimensional consistency heatmap. All dimensions share the same underlying prompt engineering framework and human verification process, enabling horizontal attribution analysis.

Extraction rationale: Primarily based on the Benchmark diagnostic table notes: “Type: Multi-dimensional trustworthiness evaluation suite; Strengths: Covers factual consistency, safety, fairness, privacy, etc.; Weaknesses: Broad dimension coverage, but each requires individual justification of applicability.” In strong_rubric_evidence, all three 5-point items correspond to “comprehensive evaluation of LLM trustworthiness, including factual consistency, safety, fairness, privacy, robustness, etc.,” and the criterion “Metric: Strong multi-metric profiling” directly points to the Scorecard design.

## What it improves vs. baseline

Breaks through the limitations of single-dimensional benchmarks and, for the first time, achieves decoupled quantification and joint diagnosis of multiple trustworthiness attributes, transforming “trustworthiness” from an ambiguous label into an engineering-oriented profiling tool capable of pinpointing weak links (e.g., high factual accuracy but low privacy protection).

## Adaptation example

On the financial customer service dataset FinChat, the “Safety” and “Factuality” modules of Scorecard are invoked to inject phishing script perturbations (for safety) and outdated interest-rate policy information (for factuality), respectively, generating a two-dimensional risk score used to train the risk-aware routing mechanism of the customer service model.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool is a modular evaluation suite that provides independent yet aligned assessment protocols for each trustworthiness dimension—factual consistency, safety, fairness, privacy, and robustness—unified under a ternary structure of “prompt + reference answer + adversarial perturbation set.” It outputs standardized scores (ranging from 0 to 1) per dimension and a cross-dimensional consistency heatmap.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: On the financial customer service dataset FinChat, the “Safety” and “Factuality” modules of Scorecard are invoked to inject phishing script perturbations (for safety) and outdated interest-rate policy information (for factuality), respectively, generating a two-dimensional risk score used to train the risk-aware routing mechanism of the customer service model.


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: A unified triplet structure of “prompt + reference answer + adversarial perturbation set” is adopted.
- **Ground truth and disagreement design**: —
- **Metric validity**: Output standardized scores (0–1) for each dimension and a cross-dimension consistency heatmap. All dimensions share the same underlying prompt engineering framework and human verification process, enabling horizontal attribution analysis.
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: All dimensions share the same underlying prompt engineering framework and human verification process.
- **Robustness against gaming and contamination**: A unified triplet structure of “prompt + reference answer + adversarial perturbation set” is adopted.
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• Survey Section 941: Notably, DecodingTrust [Wang et al., 2023] introduced a rigorous privacy vertical utilizing the Enron Email dataset to evaluate Personally Identifiable Information (PII) leakage under adversarial system prompts.

## Synthesis

The survey notes that DecodingTrust introduces rigorous privacy evaluation, leveraging the Enron Email dataset to assess personally identifiable information (PII) leakage under adversarial system prompts.
