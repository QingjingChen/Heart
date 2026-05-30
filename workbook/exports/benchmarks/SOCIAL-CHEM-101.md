# SOCIAL-CHEM-101 (2020)

**Dimension**: Human centered  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Rules-of-thumb generation and contextual applicability scoring framework

## Tool explanation (full)

This tool uses a million-scale dataset of “commonsense social rules” (e.g., “Don’t tell jokes when someone is crying”) extracted from Reddit as seed data to construct a three-tier evaluation framework:  
1) Given a novel scenario (e.g., “a friend posts on social media after a breakup”), the model is prompted to generate applicable rules;  
2) The generated rules are scored for applicability (0–3 points), based on alignment with scenario elements (e.g., agent relationship, emotional intensity, cultural scripts);  
3) Rule conflicts (e.g., “prioritize comforting” vs. “give space”) are identified and modeled via weighted allocation.  
Its core premise is to transform descriptive social norms into a computable, debuggable intermediate representation for ethical reasoning.  

Extraction rationale: Primarily drawn from the Benchmark diagnostic table notes: “Type: Social norm / Rules-of-Thumb dataset; cited in Zhong 2025 and Xu 2025. Strengths: rich rules, scenarios, and social norms. Weaknesses: Reddit-/English-centric; descriptive norms ≠ ethical norms.” In strong_rubric_evidence, both Construct clarity and Scenario validity received scores of 4. Notes emphasize “large-scale social norms and rules-of-thumb data, supporting evaluation of social behavior” and “inclusion of everyday actions and normative contexts”, confirming that the core mechanism is rule generation coupled with contextual applicability scoring.

## What it improves vs. baseline

Compared to single-rule matching or binary compliance judgments, this framework is the first to model social norms as dynamic, context-bound, and negotiable knowledge units, enabling quantitative evaluation of higher-order human-centered reasoning—such as “when is an exception reasonable.”

## Adaptation example

In a cross-cultural telemedicine AI dataset, map the English rule from SOCIAL-CHEM-101—“Physicians should avoid discussing patient conditions in waiting rooms”—to the context of grassroots clinics in China, requiring the model to generate a culturally adapted rule (e.g., “When a village doctor discloses test results under the big tree at the village entrance, they must confirm no other villagers are within earshot”), and score its applicability along three dimensions: “strength of privacy expectations”, “tolerance in close-knit communities”, and “urgency of information”, thereby transforming generic rules into culturally sensitive clinical communication protocols.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool uses a seed set of millions of “commonsense social rules” (e.g., “Do not tell jokes when someone is crying”) extracted from Reddit to construct a three-tiered evaluation: 1) Given a novel scenario (e.g., “a friend posts on social media about a recent breakup”), the model is prompted to generate applicable rules; 2) The generated rules are scored for applicability (0–3 points) based on alignment with scenario elements—such as agent relationships, emotional intensity, and cultural scripts; 3) Rule conflicts (e.g., “prioritize comforting” vs. “give space”) are identified and modeled via learned weight allocation.
- **Normative grounding**: Its essence is to transform descriptive social norms into a computable and debuggable intermediate representation for ethical reasoning.
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: Given a novel scenario (e.g., “a friend posts on social media after a recent breakup”), the model is required to generate applicable ethical guidelines.
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: 1) Given a novel scenario (e.g., “a friend posts on social media after a recent breakup”), the model is required to generate applicable normative rules;  
2) The generated rules are scored for applicability on a 0–3 scale, based on alignment with scenario-specific elements—namely, relational role (e.g., friend vs. family), emotional intensity, and culturally embedded scripts;  
3) Rule conflicts (e.g., “prioritize comfort” vs. “grant personal space”) are identified and modeled via learned weight allocation.
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: Score the applicability of the generated rules on a 0–3 scale, based on their alignment with situational elements (agent relationships, emotional intensity, cultural scripts).
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Synthesis

The review notes that the benchmark requires more detailed clarification regarding construct clarity, normative foundations, provenance, and applicability of evidence. Moreover, it relies primarily on descriptive community norms, lacks calibration against legal or ethical theory, and exhibits pronounced U.S./English/Reddit bias.
