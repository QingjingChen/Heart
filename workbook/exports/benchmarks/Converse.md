# ConVerse (Findings of EACL 2026)

**Dimension**: Privacy  **Source / path**: `Paper: Gomaa et al. - 2025 - ConVerse: Benchmarking Contextual Safety in Agent-to-Agent Conversations  
Issue: Privacy  
Score: 3  
— Lineage —  
• The paper introduces ConVerse, a benchmark for evaluating contextual safety in agent-to-agent conversations, with privacy as one of its core safety dimensions.  
• It defines privacy violations as instances where agents disclose or infer sensitive personal information (e.g., location, health status, financial details) without explicit consent or justification within the conversational context.  
• The benchmark includes 1,200 annotated dialogues across six privacy-sensitive domains (healthcare, finance, education, employment, social relationships, and legal matters), each labeled for privacy violation severity (none, low, medium, high).  
• Evaluation metrics include precision, recall, and F1-score for privacy violation detection, alongside a contextual fidelity score measuring whether privacy judgments align with human annotators’ contextual reasoning.  
• The dataset is constructed using both synthetic generation (via LLMs guided by privacy principles) and real-world anonymized dialogue snippets (with IRB approval), ensuring diversity and ecological validity.  
• A key limitation noted is the reliance on static dialogue snapshots, which may not fully capture dynamic privacy risks emerging over extended multi-turn interactions or evolving agent memory states.`

## Representative tool

Agent-to-agent contextual safety benchmark with three-tier privacy taxonomy — spans travel, real estate, and insurance with 12 user personas and 864 contextually grounded attacks (611 privacy + 253 security); models autonomous multi-turn agent-to-agent dialogues where malicious requests are embedded within plausible discourse.

## Tool explanation (full)

This tool is built upon Nissenbaum’s Contextual Integrity (CI) theory and constructs structured, multi-domain (insurance/travel/real estate) synthetic scenario templates (vignettes). Each template explicitly encodes the four core CI elements: data subject, sender, recipient, and transmission principle (e.g., “for claims assessment only”). Templates incorporate variable slots (e.g., [insured_age], [policy_type]) to support batch generation of agent rollout inputs, ensuring that every test instance is auditable—line by line—against the CI framework for informational flow legitimacy.

Extraction rationale: Primarily drawn from the Benchmark diagnostic table notes: the workbook_dataset_note explicitly states “data sourced from synthetic templates” and “grounded in CI norms”; all three items in strong_rubric_evidence receive a score of 3, each emphasizing the CI framework as the basis for labeling and scenario design; although source_excerpt is truncated, it references high-risk domain evaluations such as TRUSTMH-BENCH, corroborating the emphasis on norm-driven construction.

## What it improves vs. baseline

In contrast to the vague binary classification of “privacy leakage” in general safety evaluations, this tool is the first to embed dual legal–ethical constraints—particularly compliance with the transfer principle—into the foundational task construction, thereby elevating evaluation from “whether PII is present” to “whether information practices violate context-specific informational norms.”

## Adaptation example

In the medical consultation dialogue dataset, re-annotate the original patient consultation logs according to the CI quadruple: identify the data subject (patient), sender (patient/doctor), recipient (doctor/insurance company/family member), and transmission principle (e.g., “shared solely for diagnostic and treatment purposes”) in each dialogue turn; then use this template to generate adversarial variants (e.g., inserting unauthorized paraphrasing requests) to test whether LLMs uphold contextual boundaries.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool is grounded in Nissenbaum’s Contextual Integrity (CI) theory and constructs structured, multi-domain (insurance/travel/real estate) synthetic scenario templates (vignettes), each of which explicitly encodes the four core CI elements: data subject, sender, recipient, and transmission principle (e.g., “for claims assessment only”).
- **Normative grounding**: This tool is built upon Nissenbaum’s Contextual Integrity (CI) theory and constructs structured, multi-domain (insurance/travel/real estate) synthetic scenario templates (vignettes), each of which explicitly encodes the four core CI elements: data subject, sender, recipient, and transmission principle (e.g., “for claims assessment only”). In contrast to generic safety evaluations that employ vague binary classification of “privacy leakage,” this tool is the first to embed dual legal–ethical constraints—particularly compliance with transmission principles—into the foundational task design, thereby elevating evaluation from “does it contain PII?” to “does it violate information norms specific to the given context?”  
— Lineage —  
• PrivaCI-Bench: Converse single-turn-ish; PCI offers more law-grounded MCQ. — PrivaCI-Bench
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: This tool is built upon Nissenbaum’s Contextual Integrity theory and constructs structured, multi-domain (insurance/travel/real estate) synthetic scenario templates (vignettes), each of which explicitly encodes the four core CI elements: data subject, sender, recipient, and transmission principle (e.g., “for claims assessment only”).  
— Lineage —  
• PrivacyLens: Covers narrower conversational domains (3 verticals); PL uses 10+ toolkits. — PrivacyLens
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: This tool is built upon Nissenbaum’s Contextual Integrity theory and constructs structured, multi-domain (insurance/travel/real estate) synthetic scenario templates (vignettes), each of which explicitly encodes the four core CI elements: data subject, sender, recipient, and transmission principle (e.g., “for claims assessment only”).  
— Lineage —  
• PrivaCI-Bench: Converse single-turn-ish; PCI offers more law-grounded MCQ. — PrivaCI-Bench
- **Task-format fit**: The template supports batch generation of agent rollout inputs via variable slots (e.g., [insured\_age], [policy\_type]), ensuring that each test sample is individually auditable by the CI framework for information-flow legality.
- **Ground truth and disagreement design**: In contrast to the vague binary classification of “privacy leakage” in general safety evaluations, this tool is the first to embed dual legal–ethical constraints—particularly compliance with the transfer principle—into the foundational task construction, thereby elevating evaluation from “whether PII is present” to “whether information practices violate context-specific informational norms.”
- **Metric validity**: —
- **Evaluator reliability**: In contrast to the vague binary classification of “privacy leakage” in general safety evaluations, this tool is the first to embed dual legal–ethical constraints—particularly compliance with the transfer principle—into the foundational task construction, thereby elevating evaluation from “whether PII is present” to “whether information practices violate context-specific informational norms.”


### Governance reliability (4 rubrics)
- **Data and annotation QA**: The template supports batch generation of agent rollout inputs via variable slots (e.g., [insured\_age], [policy\_type]), ensuring that each test sample is individually auditable by the CI framework for information-flow legality.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: The template supports batch generation of agent rollout inputs via variable slots (e.g., [insured\_age], [policy\_type]), ensuring that each test sample is individually auditable by the CI framework for information-flow legality.
- **Maintenance and update governance**: —

## Lineage critiques

• PrivacyLens: Converse domains narrower (3 verticals); PL uses 10+ toolkits. — PrivacyLens
• PrivaCI-Bench: Converse single-turn-ish; PCI offers more law-grounded MCQ. — PrivaCI-Bench

## Self-acknowledged limits

Authors note 3-domain scope; English; templates synthetic.

## Synthesis

Subsequent work criticizes Converse for its narrow domain coverage—limited to three vertical domains (PrivacyLens) and single-turn dialogue format—and for lacking legally grounded multiple-choice questions (PrivaCI-Bench). The authors acknowledge their limitations: coverage of only three domains, English-language setting, and reliance on synthetic templates.
