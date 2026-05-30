# JBBQ (2024/2025)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/10858.txt`

## Representative tool

Culturally grounded, language-specific BBQ template adaptation framework

## Tool explanation (full)

This tool is built upon the structured bias-detection paradigm of the original BBQ (Bias Benchmark for QA), systematically rewriting question templates, social group dimensions, cultural default assumptions, and contextualized distractors to align with Japanese linguistic conventions and Japanese societal norms. It relies on a localized knowledge base (e.g., Japanese demographic structures, legally protected groups, and media-perpetuated stereotypes), a bilingual expert collaborative annotation process, and culturally adaptive reconstruction of the original BBQ’s “plausible but incorrect” answers. It is not mere translation, but a full reconstruction of the entire bias-detection logical chain anchored in the Japanese sociocultural context.

Extraction rationale: Primarily drawn from the Benchmark diagnostic table notes: “Type: Japanese BBQ / Japan-context extension; included in comprehensive survey as a cultural and linguistic variant of BBQ. Strength: adds Japanese cultural biases; Weakness: still requires intersectional identity and open-generation evaluation.” Additionally, three high-scoring (4-point) items in strong_rubric_evidence all specifically highlight its capability to localize and reconstruct the BBQ structure—not generic benchmark construction.

## What it improves vs. baseline

Compared to the original BBQ (which covers only English/US contexts), it significantly enhances cultural relevance and linguistic authenticity: avoids semantic distortion or invisible bias caused by literal translation; compared to general multilingual benchmarks (e.g., X-CSR), its modular construction supports fine-grained control of cultural variables (e.g., “seniority-based hierarchy”, “family surname inheritance”—Japan-specific identity dimensions), enabling fairness evaluation to be genuinely embedded within local social structures.

## Adaptation example

In the Japanese elderly-focused medical QA dataset (e.g., JP-MedQA), this framework replaces “caregiver” in the original question with “介護者” and binds the identity label “female relative aged 65 or older”, while injecting typical bias distractors from Japan’s Long-Term Care Insurance system (e.g., implying “elderly patients are not worthy of priority treatment”), thereby constructing a reproducible, culturally embedded fairness diagnostic subset.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool is built upon the structured bias detection paradigm of the original BBQ (Bias Benchmark for QA), systematically rewriting question templates, social group dimensions, cultural default assumptions, and contextualized distractors to align with Japanese linguistic conventions and societal norms. It relies on a localized knowledge base (e.g., Japan’s demographic structure, legally protected groups, and media-perpetuated stereotypes), a bilingual expert collaborative annotation process, and culturally adapted reconstruction of the original BBQ’s “plausible but incorrect” answers. Rather than performing simple translation, it reconstructs the entire bias detection logic chain anchored in the Japanese sociocultural context.
- **Normative grounding**: It relies on a localized knowledge base (e.g., Japan’s demographic structure, legally protected groups, and common media stereotypes), a bilingual expert collaborative annotation process, and culturally adaptive reconstruction of the “plausible but incorrect” answers from the original BBQ; it is not a simple translation, but rather a full reconstruction of the entire bias-detection logical chain anchored in the Japanese sociocultural context.
- **Source provenance and evidence fitness**: It relies on a localized knowledge base (e.g., Japan’s demographic structure, legally protected groups, and common media stereotypes), a bilingual expert collaborative annotation process, and culturally adaptive reconstruction of the “plausible but incorrect” answers from the original BBQ; it is not a simple translation, but rather a full reconstruction of the entire bias-detection logical chain anchored in the Japanese sociocultural context.
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: —
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: leveraging a localized knowledge base (e.g., Japan’s demographic structure, legally protected groups, and media-perpetuated stereotypes), a bilingual expert collaborative annotation process, and culturally adapted reconstruction of the original BBQ’s “plausible but incorrect” answers.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —
