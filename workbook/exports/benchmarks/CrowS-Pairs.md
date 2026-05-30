# CrowS-Pairs (2020)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/10856.txt`

## Representative tool

Crowd-sourced stereotypical vs. anti-stereotypical sentence pairs annotated under EEOC-protected-category taxonomy

## Tool explanation (full)

This tool collects 1,508 sentence pairs via the crowdsourcing platform Amazon Mechanical Turk, with each pair strictly satisfying: (1) differing only in protected group identifiers (e.g., black/white, gay/straight, disabled/able-bodied); (2) maintaining identical context; and (3) being labeled by annotators—who determine which sentence is more stereotypical based on the U.S. Equal Employment Opportunity Commission (EEOC) definitions of protected categories (e.g., race, gender, religion). The resulting benchmark thus captures bias strength across nine social dimensions and is human-consensus-driven.

Extraction rationale: Primarily drawn from the Benchmark diagnostic table’s “notes”: the notes explicitly state “based on U.S. EEOC protected categories,” “data source: Amazon Mechanical Turk; scale: 1,508 sentence pairs; crowdsourcing bias disclosed,” and provide concrete example pairs (e.g., “black kids” / “white kids”). The “source_excerpt”—citing “CrowS-Pairs: A Challenge Dataset for Measuring Social Biases” and “Warning: explicit statements of offensive stereotypes”—further corroborates that its core mechanism is human-annotated binary discrimination between stereotypical and counter-stereotypical statements.

## What it improves vs. baseline

Compared to prior evaluations relying on synthetic templates or word-vector analogies, this tool is the first to use real human crowd-sourced judgments as the gold standard and anchors the definition of bias within a legal framework (EEOC), significantly enhancing the operational rigor of “what constitutes a stereotype”; the sentence-pair format naturally aligns with masked language models’ (MLMs) per-token log-probability (PLL) scoring, enabling zero-shot bias detection without fine-tuning.

## Adaptation example

In the social media content moderation dataset, the original moderation instruction “Remove posts promoting hate against X group” is reformulated into a CrowS-Pairs-style sentence pair: “This policy protects [Black/Latino/Disabled] users from harassment” (stereotypical) vs. “This policy protects [White/Non-disabled] users from harassment” (anti-stereotypical), to evaluate whether moderation models internalize group-priority bias during policy text comprehension.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Each pair strictly satisfies: 1) differing only in protected group identifiers (e.g., black/white, gay/straight, disabled/able-bodied); 2) maintaining identical context; 3) annotators judging which sentence is more stereotypical based on EEOC-defined protected categories (race, gender, religion, etc.).  
— Lineage —  
• stereotyping content underspecified, many examples invalid; construct of 'social bias' not operationalized. — Blodgett 2021  
— External Perspective (Survey) —  
•
- **Normative grounding**: Annotators determine which sentence is more stereotypical based on the EEOC-defined protected categories (e.g., race, gender, religion); the resulting benchmark covers nine social dimensions and is driven by human consensus for bias intensity judgment.  
— Lineage —  
•  
— External Perspective (Survey) —  
•
- **Source provenance and evidence fitness**: This tool collects 1,508 sentence pairs via the crowdsourcing platform Amazon Mechanical Turk, with each pair strictly satisfying: (1) differing only in protected group identifiers (e.g., black/white, gay/straight, disabled/able-bodied); (2) maintaining identical context; and (3) being annotated by raters who determine which sentence is more stereotypical, based on EEOC-defined protected categories (e.g., race, gender, religion).  
— Lineage —  
•   
— External Perspective (Survey) —  
• A key challenge across fairness benchmarks is the trade-off between quantity and quality. Aribandi et al. (2021) show that although CrowS-Pairs maintains higher data quality, its small size leads to high variance within specific categories; for example, religious-bias results differ sharply between StereoSet and CrowS-Pairs simply because one has more samples. — Survey
- **Context and stakeholder coverage**: — Lineage —  
• US-centric stereotypes; not transferable to other cultures. — Jin 2024 (KoBBQ)  
• no Chinese-context categories (region, hukou). — Huang 2024 (CBBQ)  
— External Perspectives (Survey) —  
•
- **Real-world harm linkage**: — Lineage —  
•  
— External perspectives (Survey) —  
•


### Evaluation design (5 rubrics)
- **Scenario validity**: Each pair strictly satisfies: 1) differing only in protected group identifiers (e.g., black/white, gay/straight, disabled/able-bodied); 2) maintaining identical context; 3) annotators judging which sentence is more stereotypical based on EEOC-defined protected categories (race, gender, religion, etc.).  
— Lineage —  
• stereotyping content underspecified, many examples invalid; construct of 'social bias' not operationalized. — Blodgett 2021  
— External Perspective (Survey) —  
•
- **Task-format fit**: Sentence-pair format naturally aligns with the per-token log-probability (PLL) scoring of masked language models (MLMs), enabling zero-shot bias detection without fine-tuning.  
— Lineage —  
• PLL metric sensitive to spurious lexical differences. — Nadeem 2021 (StereoSet) & later authors  
— External Perspective (Survey) —  
•
- **Ground truth and disagreement design**: Annotators determine which sentence is more stereotypical based on the EEOC-defined protected categories (e.g., race, gender, religion); the resulting benchmark covers nine social dimensions and is driven by human consensus for bias intensity judgment.  
— Lineage —  
•  
— External Perspective (Survey) —  
•
- **Metric validity**: Sentence-pair format naturally aligns with the per-token log-probability (PLL) scoring of masked language models (MLMs), enabling zero-shot bias detection without fine-tuning.  
— Lineage —  
• PLL metric sensitive to spurious lexical differences. — Nadeem 2021 (StereoSet) & later authors  
— External Perspective (Survey) —  
•
- **Evaluator reliability**: MTurk workers from US/UK; English; possibly noisy crowd judgments; nine fixed categories.  
— Lineage —  
•  
— External perspective (Survey) —  
•


### Governance reliability (4 rubrics)
- **Data and annotation QA**: This tool collects 1,508 sentence pairs via the crowdsourcing platform Amazon Mechanical Turk, with each pair strictly satisfying: (1) differing only in protected group identifiers (e.g., black/white, gay/straight, disabled/able-bodied); (2) maintaining identical context; and (3) being annotated by raters who determine which sentence is more stereotypical, based on EEOC-defined protected categories (e.g., race, gender, religion).  
— Lineage —  
•   
— External Perspective (Survey) —  
• A key challenge across fairness benchmarks is the trade-off between quantity and quality. Aribandi et al. (2021) show that although CrowS-Pairs maintains higher data quality, its small size leads to high variance within specific categories; for example, religious-bias results differ sharply between StereoSet and CrowS-Pairs simply because one has more samples. — Survey
- **Robustness against gaming and contamination**: — Lineage —  
•  
— External perspectives (Survey) —  
•
- **Documentation and reproducibility**: This tool collects 1,508 sentence pairs via the crowdsourcing platform Amazon Mechanical Turk, with each pair strictly satisfying: 1) differing only in protected group identifiers (e.g., black/white, gay/straight, disabled/able-bodied); 2) maintaining identical context; and 3) being annotated by raters who determine which sentence is more stereotypical, based on EEOC-defined protected categories (e.g., race, gender, religion).  
— Lineage —  
•  
— External Perspective (Survey) —  
•
- **Maintenance and update governance**: — Lineage —  
•  
— External perspectives (Survey) —  
•

## Lineage critiques

• stereotyping content underspecified, many examples invalid; construct of 'social bias' not operationalized. — Blodgett 2021
• PLL metric sensitive to spurious lexical differences. — Nadeem 2021 (StereoSet) & later authors
• US-centric stereotypes; not transferable to other cultures. — Jin 2024 (KoBBQ)
• no Chinese-context categories (region, hukou). — Huang 2024 (CBBQ)

## Self-acknowledged limits

MTurk workers from US/UK; English; possibly noisy crowd judgements; nine fixed categories.

## External views (survey)

• A key challenge across fairness benchmarks is the trade-off between quantity and quality. Aribandi et al. (2021) show that although CrowS-Pairs maintains higher data quality, its small size leads to high variance within specific categories; for example, religious-bias results differ sharply between StereoSet and CrowS-Pairs simply because one has more samples. — Survey

## Synthesis

The review notes that although CrowS-Pairs exhibits high data quality, its small sample size leads to high variance within specific categories. Subsequent work criticizes its stereotypical content as ill-defined, identifies many examples as invalid, and points out that the social bias construct remains unoperationalized; the PLL metric is sensitive to lexical differences; U.S.-centric stereotypes are difficult to transfer cross-culturally; and Chinese contextual categories are absent.
