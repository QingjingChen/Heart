# SALAD-bench (2024)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13277.txt`

## Representative tool

Three-Tier Hierarchical Safety Taxonomy with Attack-Enhanced Dual-Track Evaluation

## Tool explanation (full)

This tool defines a three-tiered safety hazard classification system: L1 (macro-level domains, e.g., Malicious Use), L2 (meso-level categories, e.g., CBRN), and L3 (micro-level behaviors, e.g., Bioterrorism). For each tier, it designs dual-track evaluation items: Base Questions (fundamental safety judgments) and Attack-Enhanced Questions (adversarial variants strengthened by jailbreaking strategies). It employs a hybrid format of multiple-choice questions (MCQ) and open-ended generation, requiring models not only to refuse high-risk requests but also to explain the rationale for refusal—thereby distinguishing “correct refusal” from “evasive refusal.”

Extraction basis: Directly grounded in the source_excerpt’s explicit description: “hierarchical safety benchmark: 6 Level-1 domains...Level-3: Bioterrorism”, “Base Question...Multiple Choice Attack Enhanced Defense Enhanced”; additionally, the workbook_dataset_note emphasizes “hierarchical taxonomy and complex attacks”, confirming that the tool’s core design centers on hierarchy and dual-track structure.

## What it improves vs. baseline

Compared to flat benchmarks (e.g., BeaverTails), it significantly enhances fine-grained threat analysis capability and robustness against jailbreak circumvention; by leveraging an attack-augmented subset, it exposes model vulnerabilities under jailbreaking strategies such as prompt engineering, role-playing, and stepwise induction, thereby shifting evaluation from static compliance to dynamic defense capability assessment.

## Adaptation example

In the HuggingFace OpenAssistant dialogue dataset, all dialogues exhibiting risk tendencies are relabeled according to the SALAD three-level taxonomy (e.g., L3 'Financial Scam → Romance Scam → Gift Card Fraud'), and attack-enhanced variants are injected at each L3 node (e.g., 'pretending to be a boyfriend requesting gift cards' → 'demanding advance payment of a guarantee under the pretext of tax inspection'), thereby constructing a progressive jailbreaking stress-test suite for open-source dialogue models.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool defines a three-tiered safety hazard classification system: L1 (macro-level domains, e.g., Malicious Use), L2 (meso-level categories, e.g., CBRN), and L3 (micro-level behaviors, e.g., Bioterrorism), and designs dual-track evaluation items for each tier—Base Question (fundamental safety judgment) and Attack-Enhanced Question (adversarial variants strengthened via jailbreaking strategies).  
— Lineage —  
• hierarchy is novel but Level-3 categories overlap. — HarmBench (2024)  
— External Perspective (Survey) —  
• SALAD-Bench [Li et al., 2024a] is a large-scale, hierarchical safety benchmark designed to comprehensively evaluate large language models, as well as various attack and defense methods. It features a three-level taxonomy and an innovative — Survey Paragraph 818
- **Normative grounding**: —
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Exposing model vulnerabilities to jailbreaking strategies—including prompt engineering, role-playing, and step-by-step induction—by attacking augmented subsets, thereby advancing evaluation from static compliance to dynamic defense capability assessment.  
— Lineage —  
• Question-format only, not action-grounded. — Agent-SafetyBench (2025)
- **Task-format fit**: Using a hybrid MCQ + open-generation format, the model is required not only to refuse high-risk requests but also to explain the rationale for refusal, thereby distinguishing “correct refusal” from “evasive refusal.”  
— Lineage —  
• text-only. — MM-SafetyBench (2024)  
• doesn't include over-refusal. — XSTest-family
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• hierarchy is novel but Level-3 categories overlap. — HarmBench (2024)
• question-format only, not action-grounded. — Agent-SafetyBench (2025)
• text-only. — MM-SafetyBench (2024)
• doesn't include over-refusal. — XSTest-family

## Self-acknowledged limits

Authors note hierarchy granularity choices are subjective; LLM-judge for response classification has biases.

## External views (survey)

• SALAD-Bench [Li et al., 2024a] is a large-scale, hierarchical safety benchmark designed to comprehensively evaluate large language models, as well as various attack and defense methods. It features a three-level taxonomy and an innovative — Survey Paragraph 818

## Synthesis

The survey states that SALAD-bench is a large-scale, hierarchical safety benchmark featuring a three-level taxonomy and novel attack and defense methodologies. Subsequent work criticizes its Level-3 categories for overlap, text-only format limitations, and failure to include over-rejection issues. The authors acknowledge that the granularity of the hierarchy is subjective and that LLM-based classification of responses introduces bias.
