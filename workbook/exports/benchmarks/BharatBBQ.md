# BharatBBQ (2024/2025)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/10858.txt`

## Representative tool

Culturally-Localized BBQ Template Adapter (CL-BTA)

## Tool explanation (full)

CL-BTA is a modular cultural adaptation toolkit: it decouples the generic bias QA structure of the original BBQ (e.g., “Who is more likely to become a nurse? A. Sarah B. James”) into swappable “social category slots” (e.g., caste, regional language, religious practice), “localized contextual anchors” (e.g., Indian public school admissions, South Asian family property inheritance), and “culture-specific commonsense knowledge bases” (e.g., local occupational prestige rankings, kinship term hierarchies), enabling researchers to inject regional norms and institutional contexts on demand and generate bias-detection instances aligned with local fairness concerns.

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: “Type: BBQ cultural extension; comprehensive survey lists it as one of the multilingual/cultural extensions of BBQ’s modular design. Strength: localized bias detection; weakness: if only the template is migrated, intersectional identities and real-world scenarios remain insufficient”; in strong_rubric_evidence, the Normative grounding score is 4, explicitly stating “closer alignment with local social categories and cultural contexts”, and the Source provenance and evidence fitness score of 4 emphasizes “BBQ modular extension with traceable provenance”.

## What it improves vs. baseline

In contrast to coarse-grained transfer approaches that directly translate or adopt Western BBQ templates, CL-BTA enhances the normative grounding and contextual authenticity of fairness evaluation by explicitly modeling culture-specific social categories and institutional constraints, thereby addressing the core deficiency in cross-cultural transfer—namely, “terms are translatable, but biases are not transferable.”

## Adaptation example

In the Southeast Asian Multicultural Education Policy QA dataset, CL-BTA is applied to replace the “caste” slot in the BBQ template with “ethnic minority status in Malaysia (e.g., Orang Asli, Indian Malaysian)”, set the situational anchor to “PT3 examination eligibility review for academic advancement”, and inject domain-specific knowledge from local education regulations regarding affirmative action policies for Indigenous peoples, thereby constructing a localized fairness evaluation instance that reflects genuine institutional bias risks.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: CL-BTA is a modular cultural adaptation toolkit: it decouples the generic bias QA structure of the original BBQ (e.g., “Who is more likely to become a nurse? A. Sarah B. James”) into swappable components—namely, “social category slots” (e.g., caste, regional language, religious practice), “localized contextual anchors” (e.g., admissions to Indian public schools, inheritance of family property in South Asia), and “culture-specific commonsense knowledge bases” (e.g., local occupational prestige rankings, kinship term hierarchies)—enabling researchers to inject region-specific norms and institutional contexts on demand and thereby generate bias-detection instances aligned with local fairness concerns.
- **Normative grounding**: In contrast to coarse-grained transfer approaches that directly translate or adopt Western BBQ templates, CL-BTA enhances the normative grounding and contextual authenticity of fairness evaluation by explicitly modeling culture-specific social categories and institutional constraints, thereby addressing the core deficiency in cross-cultural transfer—namely, “terms are translatable, but biases are not transferable.”
- **Source provenance and evidence fitness**: CL-BTA is a modular cultural adaptation toolkit: it decouples the generic bias QA structure of the original BBQ (e.g., “Who is more likely to become a nurse? A. Sarah B. James”) into swappable components—namely, “social category slots” (e.g., caste, regional language, religious practice), “localized contextual anchors” (e.g., admissions to Indian public schools, inheritance of family property in South Asia), and “culture-specific commonsense knowledge bases” (e.g., local occupational prestige rankings, kinship term hierarchies)—enabling researchers to inject region-specific norms and institutional contexts on demand and thereby generate bias-detection instances aligned with local fairness concerns.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —
