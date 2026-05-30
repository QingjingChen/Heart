# CMoralEval (2024)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/10834.txt`

## Representative tool

MFT-grounded multi-dimensional moral scenario template

## Tool explanation (full)

This tool constructs a five-dimensional moral judgment task template based on Moral Foundations Theory (MFT, Graham et al., 2009): familial morality, social morality, professional morality, cyber ethics, and personal morality. Each instance is drawn from authentic moral anomaly cases in Chinese legal statutes, the ethical television program “Observing Morality,” and academic papers, and is manually annotated to map onto MFT sub-dimensions. The template mandates that each multiple-choice question (MCQ) covers at least one MFT dimension, and its options are designed to reflect moral tension (e.g., journalistic neutrality vs. proactive helping). Its core contribution is operationalizing abstract ethical constructs into a reusable protocol for generating scenario–dimension–option triples.

Extraction rationale: Primarily based on notes in the Benchmark diagnostic table: workbook_dataset_note explicitly states “cites MFT theory and covers five sub-dimensions” and specifies sources as the “Observing Morality” program and moral anomaly cases from academic papers; strong_rubric_evidence notes that Construct clarity received a score of 4, with the supporting note stating “cites MFT theory and covers five sub-dimensions,” while also pointing out “no explicit exclusion scope or operationalization details”—which inversely confirms that this template constitutes its core methodological contribution; source_excerpt, though truncated, contains repeated author affiliations and title, confirming CMoralEval as an independent benchmark effort.

## What it improves vs. baseline

Compared with earlier generalized Chinese moral evaluation approaches (e.g., using only generic ethical Q&A or single-dimension true/false questions), this template is the first to systematically introduce the cross-culturally validated Moral Foundations Theory (MFT) framework and achieve bidirectional alignment between localized scenarios and theoretical dimensions, significantly enhancing construct validity and cultural adaptability.

## Adaptation example

In the medical assistant dialogue dataset for elderly users, this template can be reused to reconstruct user queries: transforming the original symptom description (e.g., “I feel dizzy after taking medication”) into an MFT-aligned moral scenario (e.g., “You discover that a community physician failed to disclose the dizziness-inducing side effect of a certain antihypertensive drug, and multiple elderly patients have already fallen—A. Quietly switch medications to avoid conflict; B. Anonymously report the issue to the National Health Commission; C. Warn neighbors in the residential community group”), thereby evaluating the model’s trade-off capability among family caregiving responsibility, social trust, and professional ethics.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool constructs a five-dimensional moral judgment task template based on Moral Foundations Theory (MFT, Graham et al., 2009): familial morality, societal morality, professional morality, cyber ethics, and personal morality. Each instance is drawn from authentic moral anomaly cases in Chinese legal statutes, the ethical television program “Observing Morality,” and academic papers, and is manually annotated to map onto MFT sub-dimensions; the template mandates that each multiple-choice question (MCQ) covers at least one MFT dimension, and that answer options reflect moral tension (e.g., journalistic neutrality vs. proactive helping). Its core innovation is operationalizing abstract ethical constructs into a reusable scenario–dimension–option triplet generation protocol.  
— Lineage —  
• doesn't map to MFQ axes for cross-comparison. — MFT critique
- **Normative grounding**: —
- **Source provenance and evidence fitness**: Each instance is drawn from authentic moral anomaly cases found in Chinese legal statutes, the ethics-themed television program “Observing Morality,” and academic papers, and has been manually annotated to map onto the Moral Foundations Theory (MFT) sub-dimensions.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Each instance originates from authentic moral anomaly cases drawn from Chinese legal statutes, the ethics-themed television program “Observing Morality,” and academic papers, and has been manually annotated to map onto MFT sub-dimensions; the template mandates that every multiple-choice question (MCQ) covers at least one MFT dimension, with answer options deliberately designed to reflect moral tension (e.g., journalistic neutrality vs. proactive helping).  
— Lineage —  
• Outcome-style choice items dominate. — MoReBench (2025)  
— External Perspective (Survey) —  
• CMoralEval [Yu et al., 2024] is a large-scale morality evaluation benchmark for Chinese LLMs addressing the gap in Eastern cultural contexts. It constructs Explicit and Dilemma scenarios from real-world cases, integrating Confucian principles and modern cultural norms.
- **Task-format fit**: The template mandates that each multiple-choice question (MCQ) must cover at least one Moral Foundations Theory (MFT) dimension, and the answer options must be designed to reflect moral tension (e.g., journalistic neutrality versus proactive helping).
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Each instance is drawn from authentic moral anomaly cases found in Chinese legal statutes, the ethics-themed television program “Observing Morality,” and academic papers, and has been manually annotated to map onto the Moral Foundations Theory (MFT) sub-dimensions.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• Chinese-only; cross-national value alignment unaddressed. — NaVAB (2025)
• outcome-style choice items dominate. — MoReBench (2025)
• doesn't map to MFQ axes for cross-comparison. — MFT critique

## Self-acknowledged limits

Authors note cultural specificity may limit generalization; some categories rely on subjective interpretation.

## External views (survey)

• Survey Section 404: CMoralEval [Yu et al., 2024] is a large-scale morality evaluation benchmark for Chinese LLMs addressing the gap in Eastern cultural contexts. It constructs Explicit and Dilemma scenarios from real-world cases, integrating Confucian principles and modern cultural norms.

## Synthesis

The paper notes that CMoralEval is a large-scale moral evaluation benchmark designed for Chinese LLMs, filling a gap in Eastern cultural contexts. Subsequent work criticizes it for being limited to Chinese only, failing to address cross-national value alignment, and relying predominantly on multiple-choice formats. The authors acknowledge that cultural specificity may limit generalizability, and some categories depend on subjective interpretation.
