# BUG (2021)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/13457.txt`

## Representative tool

Statistically grounded coreference bias probe using real-text occupational gender distributions

## Tool explanation (full)

BUG constructed a coreference resolution bias detection method grounded in the U.S. 2015 Census occupational-gender distribution data: natural sentences containing occupational nouns (e.g., “cop”, “nurse”) and person pronouns (e.g., “she”, “he”) were extracted from Wikipedia, PubMed, and COVID-19 research papers; each sentence was manually annotated as stereo-, anti-stereo-, or neutral relative to statistical reality; and bias strength was quantified via ΔG (gender gap) and ΔS (stereotype gap). This tool calibrates the boundary of “plausible coreference” using real-world statistical data—not subjective stereotype judgments.

Extraction rationale: Primarily based on notes in the Benchmark diagnostic table: “Occupational-gender distributions derived from the U.S. 2015 Census”; “Data drawn from Wikipedia, PubMed abstracts, and COVID-19 research papers, totaling 108K sentences”; “Annotations performed via human labeling, with high-ambiguity items resolved via random sampling validation”; all three high-scoring items in strong_rubric_evidence directly correspond to these methodological features.

## What it improves vs. baseline

Compared to purely human-constructed synthetic sentences (e.g., Winogender), BUG is the first to bind natural text mining with demographic benchmarks, providing external validity anchors for bias measurement and avoiding distributional shift amplification or masking caused by artificial design.

## Adaptation example

In the judicial judgment summarization dataset, extract sentences where occupational roles (e.g., judge, prosecutor, defendant) co-occur with gendered pronouns (e.g., “The judge ruled in favor of the defendant because she…”); relabel these as “stereo/anti-stereo” based on China’s 2020 court system gender composition statistics, to evaluate implicit gender-assumption bias in Chinese judicial personnel within legal AI judgment generation.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: Extract natural sentences from Wikipedia/PubMed/Covid-19 papers containing co-occurrences of occupational nouns (e.g., “cop”, “nurse”) and person pronouns (e.g., “she”, “he”), annotate each sentence as stereo/anti-stereo/neutral relative to statistical reality, and compute ΔG (gender gap) and ΔS (stereotype gap) to quantify bias strength.  
— Lineage —  
• binary gender; no LGBTQ+ extension. — Felkner 2023  
• occupation-axis only. — Smith 2022  
• binary pronoun mining. — Vanmassenhove 2021
- **Normative grounding**: This tool calibrates the boundary of “reasonable reference” using real-world statistical data, rather than subjective stereotype-based judgments.
- **Source provenance and evidence fitness**: BUG constructed a coreference resolution bias detection method grounded in the 2015 U.S. Census occupational–gender distribution data: it extracts natural sentences containing co-occurring occupation nouns (e.g., “cop”, “nurse”) and person pronouns (e.g., “she”, “he”) from Wikipedia, PubMed, and COVID-19 research papers; annotates each sentence as stereo-, anti-stereo-, or neutral relative to statistical reality; and quantifies bias strength via ΔG (gender gap) and ΔS (stereotype gap). This tool calibrates the boundary of “reasonable coreference” using real-world statistical data rather than subjective stereotype judgments.
- **Context and stakeholder coverage**: — Lineage —  
• binary gender; no LGBTQ+ extension. — Felkner 2023  
• occupation-axis only. — Smith 2022  
• binary pronoun mining. — Vanmassenhove 2021
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: Natural sentences containing occupational nouns (e.g., “cop”, “nurse”) and person pronouns (e.g., “she”, “he”) were extracted from Wikipedia, PubMed, and COVID-19 research papers; each sentence was annotated as stereo-, anti-stereo-, or neutral with respect to statistical reality, and the gender gap (ΔG) and stereotype gap (ΔS) were computed to quantify bias strength.
- **Ground truth and disagreement design**: Labels are derived from human annotation, and high-ambiguity items are handled via random sampling for verification.
- **Metric validity**: and compute ΔG (gender gap) and ΔS (stereotype gap) to quantify the bias strength.
- **Evaluator reliability**: Labels are derived from human annotation, and high-ambiguity items are handled via random sampling for verification.


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Labels are derived from human annotation, and high-ambiguity items are handled via random sampling for verification.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: The data are drawn from Wikipedia, PubMed abstracts, and COVID-19 research papers, comprising a total of 108K sentences.
- **Maintenance and update governance**: —

## Lineage critiques

• binary gender; no LGBTQ+ extension. — Felkner 2023
• occupation-axis only. — Smith 2022
• binary pronoun mining. — Vanmassenhove 2021

## Self-acknowledged limits

Authors note 'gold' subset still small (~1.7k); naturalistic mining surfaces messy text; English only.

## Synthesis

The review notes that subsequent work criticized this benchmark for being limited to binary gender and not extended to LGBTQ+ (Felkner 2023), focusing solely on the occupation axis (Smith 2022), and being restricted to English and binary pronoun extraction (Vanmassenhove 2021). The authors acknowledged limitations including a small “gold” subset, noisy natural text, and English-only scope.
