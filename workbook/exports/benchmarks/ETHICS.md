# ETHICS (2023)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/10776.txt`

## Representative tool

Multi-theoretic moral subconstruct annotation schema

## Tool explanation (full)

ETHICS constructs an explicit annotation schema mapped to five major normative ethical traditions (care ethics, justice ethics, deontology, virtue ethics, commonsense morality), with each sample manually annotated to at least one sub-construct axis (justice/well-being/duties/virtues/commonsense) and with independent prompt design and balanced distribution across axes. This schema relies on an interdisciplinary ethical theory framework to guide item generation and categorization, rather than relying solely on intuition or crowd-sourced consensus.

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: “measures moral judgment sub-constructs (justice, well-being, duties, virtues, commonsense morality)” and “draws upon the five ethical traditions: Care/Justice ethics, deontology, virtue ethics, utilitarianism, commonsense morality”; the source_excerpt does not provide technical details but confirms its placement within the ‘Human-Centric Framework’ as a human-value-anchored alignment evaluation paradigm.

## What it improves vs. baseline

Compared to earlier unidimensional “moral vs. immoral” binary evaluations, this work is the first to achieve fine-grained construct disentanglement driven by multiple ethical theory paradigms, enabling bias diagnosis of models across distinct ethical reasoning pathways.

## Adaptation example

In the medical AI consultation dialogue dataset, this schema can be reused to relabel decision recommendations in physician–patient interactions (e.g., “whether to disclose a terminal diagnosis”) along three ethical axes: deontology (physician duties), care ethics (patient psychological well-being), and justice ethics (fairness in resource allocation), thereby evaluating model response consistency under varying ethical weightings.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: ETHICS constructs an explicit annotation scheme mapped to five major normative ethical frameworks (care ethics, justice ethics, deontology, virtue ethics, and commonsense morality). Each sample is manually annotated to at least one sub-construct axis (justice/well-being/duties/virtues/commonsense), with independent prompt design and balanced distribution across axes.  
— Lineage —  
• Five frameworks chosen by authors; some categories thin (e.g., Virtue 2.5k). — CMoralEval (2024) / MFQ-2 (2023)
- **Normative grounding**: This schema relies on an interdisciplinary ethical theoretical framework to guide item generation and categorization, rather than relying solely on intuition or crowdsourced consensus.
- **Source provenance and evidence fitness**: Paper: Benchmark diagnostic table notes: “Measures moral judgment sub-constructs (justice, well-being, duties, virtues, commonsense morality)” and “Draws on five ethical frameworks: Care/Justice ethics, deontology, virtue ethics, utilitarianism, and commonsense morality.”  
— Lineage —  
• Authors flag MTurk crowdsourcing variance; English; some sub-benchmarks (Virtue) limited to single-word judgments.
- **Context and stakeholder coverage**: — Lineage —  
• No professional context; abstracts away role-bound duties. — Educator-LLM (2025)
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: — Lineage —  
• Low-ambiguity items only; doesn't probe disagreement. — Scherrer 2023 (MoralChoice)
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: — Lineage —  
• Authors flag MTurk crowdsourcing variance; English; some sub-benchmarks (Virtue) limited to single-word judgments.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• outcome-only; doesn't test moral reasoning chains. — MoReBench (2025)
• low-ambiguity items only; doesn't probe disagreement. — Scherrer 2023 (MoralChoice)
• five frameworks chosen by authors; some categories thin (e.g., Virtue 2.5k). — CMoralEval (2024) / MFQ-2 (2023)
• no professional context; abstracts away role-bound duties. — Educator-LLM (2025)

## Self-acknowledged limits

Authors flag MTurk crowdsourcing variance; English; some sub-benchmarks (Virtue) limited to single-word judgments.

## External views (survey)

• This fragmentation leads to a “measurement trap,” where measurable metrics (like toxicity scores) are optimized while harder-to-define values (like human autonomy or psychological well-being) are neglected. — Survey

## Synthesis

The survey notes that this benchmark suffers from a “measurement trap”—optimizing for measurable metrics while neglecting hard-to-define values. Subsequent work criticizes it for testing only outcomes rather than moral reasoning chains (MoReBench, 2025), for including only low-ambiguity items and failing to probe disagreement (Scherrer, 2023). The authors themselves acknowledge limitations including high crowdsourcing variance, English-only monolingualism, and the restriction of certain sub-benchmarks (e.g., Virtue) to word-level judgments.
