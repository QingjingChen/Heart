# HumaniBench (2025)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/12869.txt`

## Representative tool

Expert-validated, stakeholder-informed multimodal VQA template with identity-anchored question framing

## Tool explanation (full)

HumaniBench introduces a standardized visual-question-answering (VQA) template where each image–question pair is explicitly anchored to one of five socially salient attributes (age, gender, race/ethnicity, occupation, mobility status), and questions are designed to probe model recognition, attribution, and contextual inference about human identity and role. Questions undergo expert validation (e.g., ethicists + domain practitioners) and include built-in ambiguity handling (e.g., “uncertain” option) and multilingual grounding. The template enforces alignment between visual grounding, linguistic framing, and social construct relevance.

Extraction basis: Primarily based on the Benchmark Diagnostic Table notes: workbook_dataset_note specifies “32,000 image–question pairs from real-world news images, covering five social attributes”, and strong rubric evidence notes “stakeholder role” inclusion in scenarios and “connection to deployment chains”. Also supported by strong scores in Scenario validity (score 4) citing “stakeholder roles” and Real-world harm linkage (score 4) citing “unfair/harmful content in actual application”. Source_excerpt is generic and insufficient; no tool details appear there.

## What it improves vs. baseline

Moves beyond generic VQA or bias probes by embedding human-centered constructs directly into task design—requiring models to demonstrate not just object detection or captioning, but socially situated understanding. Unlike earlier multimodal benchmarks (e.g., VQA v2), it systematically links stimulus selection (real-world news images), attribute framing, and stakeholder roles (e.g., patient, doctor, teacher) to real-world deployment risks.

## Adaptation example

In medical imaging-assisted diagnosis datasets, transform original radiology reports paired with images into HumaniBench-style VQA templates: e.g., input a chest X-ray image + question “What is the gender of the radiologist in the image?” (options: A. Male; B. Female; C. Uncertain), and enforce annotation of the radiologist’s institutional type (public hospital/private clinic) and the patient’s age group, to evaluate whether the model reproduces occupational gender stereotypes in clinical contexts.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: HumaniBench introduces a standardized visual-question-answering (VQA) template where each image–question pair is explicitly anchored to one of five socially salient attributes (age, gender, race/ethnicity, occupation, mobility status), and questions are designed to probe model recognition, attribution, and contextual inference about human identity and role.  
— Survey —  
• “HumaniBench [Raza et al., 2025] is a large-scale, human-centric evaluation framework for Large Multimodal Models (LMMs). Utilizing a dataset of 32,000 expert-verified image-question pairs from real-world news, it assesses models on alignment with human values, fairness, harm in image+text scenarios.” — Survey
- **Normative grounding**: Questions undergo expert validation (e.g., ethicists + domain practitioners) and include built-in ambiguity handling (e.g., 'uncertain' option) and multilingual grounding.
- **Source provenance and evidence fitness**: The template enforces alignment between visual grounding, linguistic framing, and social construct relevance. Moves beyond generic VQA or bias probes by embedding human-centered constructs directly into task design—requiring models to demonstrate not just object detection or captioning, but socially situated understanding. Unlike earlier multimodal benchmarks (e.g., VQA v2), it systematically links stimulus selection (real-world news images), attribute framing, and stakeholder roles (e.g., patient, doctor, teacher) to real-world deployment risks.  
— Survey —  
• “HumaniBench [Raza et al., 2025] is a large-scale, human-centric evaluation framework for Large Multimodal Models (LMMs). Utilizing a dataset of 32,000 expert-verified image-question pairs from real-world news, it assesses models on alignment with human values, fairness, harm in image+text scenarios.”— Survey
- **Context and stakeholder coverage**: Unlike earlier multimodal benchmarks (e.g., VQA v2), it systematically links stimulus selection (real-world news images), attribute framing, and stakeholder roles (e.g., patient, doctor, teacher) to real-world deployment risks.  
— Lineage —  
• “TrustMH-Bench (2026): broader trustworthiness coverage needed.”— TrustMH-Bench  
— External Perspective (Survey) —  
• “HumaniBench [Raza et al., 2025] is a large-scale, human-centric evaluation framework for Large Multimodal Models (LMMs). Utilizing a dataset of 32,000 expert-verified image-question pairs from real-world news, it assesses models on alignment with human values, fairness, and harm in image+text scenarios.”— Survey
- **Real-world harm linkage**: Moves beyond generic VQA or bias probes by embedding human-centered constructs directly into task design—requiring models to demonstrate not just object detection or captioning, but socially situated understanding. Unlike earlier multimodal benchmarks (e.g., VQA v2), it systematically links stimulus selection (real-world news images), attribute framing, and stakeholder roles (e.g., patient, doctor, teacher) to real-world deployment risks.  
— External Perspective (Survey) —  
• “HumaniBench [Raza et al., 2025] is a large-scale, human-centric evaluation framework for Large Multimodal Models (LMMs). Utilizing a dataset of 32,000 expert-verified image-question pairs from real-world news, it assesses models on alignment with human values, fairness, harm in image+text scenarios.”— Survey


### Evaluation design (5 rubrics)
- **Scenario validity**: Unlike earlier multimodal benchmarks (e.g., VQA v2), it systematically links stimulus selection (real-world news images), attribute framing, and stakeholder roles (e.g., patient, doctor, teacher) to real-world deployment risks.  
— Lineage —  
• “VITAL (2025): healthcare alignment more specialized.”— VITAL  
— External Perspectives (Survey) —  
• “HumaniBench [Raza et al., 2025] is a large-scale, human-centric evaluation framework for Large Multimodal Models (LMMs). Utilizing a dataset of 32,000 expert-verified image-question pairs from real-world news, it assesses models on alignment with human values, fairness, and harm in image+text scenarios.”— Survey
- **Task-format fit**: HumaniBench introduces a standardized visual-question-answering (VQA) template where each image–question pair is explicitly anchored to one of five socially salient attributes (age, gender, race/ethnicity, occupation, mobility status), and questions are designed to probe model recognition, attribution, and contextual inference about human identity and role.
- **Ground truth and disagreement design**: Questions undergo expert validation (e.g., ethicists + domain practitioners) and include built-in ambiguity handling (e.g., 'uncertain' option) and multilingual grounding.
- **Metric validity**: —
- **Evaluator reliability**: Questions undergo expert validation (e.g., ethicists + domain practitioners) and include built-in ambiguity handling (e.g., 'uncertain' option) and multilingual grounding.


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Questions undergo expert validation (e.g., ethicists + domain practitioners) and include built-in ambiguity handling (e.g., 'uncertain' option) and multilingual grounding.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: Authors note English; multimodal subset limited; LLM-as-judge dependency.
- **Maintenance and update governance**: —

## Lineage critiques

• 「VITAL (2025): healthcare alignment more specialized.」— VITAL
• 「TrustMH-Bench (2026): broader trustworthiness coverage needed.」— TrustMH-Bench

## Self-acknowledged limits

「Authors note English; multimodal subset limited; LLM-as-judge dependency.」

## External views (survey)

• 「HumaniBench [Raza et al., 2025] is a large-scale, human-centric evaluation framework for Large Multimodal Models (LMMs). Utilizing a dataset of 32,000 expert-verified image-question pairs from real-world news, it assesses models on alignment with human values, fairness, harm in image+text scenarios.」— Survey

## Synthesis

The survey states that HumaniBench is a large-scale, human-centered multimodal model evaluation framework that uses 32,000 expert-validated image–question pairs to assess model performance on human values, fairness, and harmful content. Subsequent work criticizes its need for greater specialization in medical alignment (VITAL) and broader coverage of trustworthiness (TrustMH-Bench). The authors acknowledge limitations including English-language predominance, limited multimodal subsets, and reliance on LLMs as evaluators.
