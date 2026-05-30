# C-Do-not-answer (2024)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13210.txt`

## Representative tool

Normatively grounded Chinese safety refusal template set with dual-layer legal-policy-social annotation

## Tool explanation (full)

This tool is a set of structured Chinese “should-not-answer” question templates, each accompanied by three-tier normative annotations: (1) corresponding provisions of current Chinese laws and regulations (e.g., Article 12 of the Interim Measures for the Management of Generative Artificial Intelligence Services), (2) policy-oriented explanations (e.g., requirements stipulated in the Cyberspace Administration of China’s security assessment guidelines), and (3) rationales grounded in social norms (e.g., public order and good customs, protection of minors). The questions cover categories including politically sensitive topics, illegal information, privacy violations, and discriminatory content, and strictly require models to output explicit refusal responses—such as “I cannot answer this question”—rather than evading or fabricating answers. Its construction relies on systematic analysis of Chinese regulatory texts, regulatory case databases, and localized public opinion events.

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: “Type: Chinese safety refusal / should-not-answer benchmark; comprehensive survey emphasizes its integration of law, policy, and social norms, supplemented by Chinese cultural context”; additionally, all three full-score criteria in strong_rubric_evidence explicitly reference tight coupling with normative sources, local context, and real-world risks—confirming that the tool’s core is a norm-anchored template construction mechanism, not merely a question collection.

## What it improves vs. baseline

Compared to earlier English safety benchmarks (e.g., SafeBench or ToxiGen), which rely solely on general principles or human intuition to judge “dangerousness,” this tool is the first to explicitly encode statutory prohibitions in the Chinese context as evaluable task constraints. This advances safety refusal capability from “whether to refuse” to “whether to refuse based on correct normative grounds,” achieving an evaluation leap from behavioral representation to normative reasoning.

## Adaptation example

In Chinese medical Q&A datasets (e.g., the CMMLU-Med subset), use this tool to transform original open-ended questions of the “disease treatment recommendation” type into refusal tasks anchored to explicit regulatory provisions—for example, by adding a preamble such as “Pursuant to Article 21 of the Measures for the Supervision and Administration of Internet-Based Medical Consultations, AI systems must not provide specific diagnostic or treatment plans,” thereby requiring the model to cite this provision and refuse to answer, thus converting knowledge-based evaluation into compliance-response evaluation.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool comprises a set of structured Chinese “should-not-answer” question templates, each accompanied by three-tier normative annotations: (1) corresponding provisions of current Chinese laws and regulations (e.g., Article 12 of the Interim Measures for the Administration of Generative Artificial Intelligence Services), (2) policy-oriented explanations (e.g., requirements stipulated in the Cyberspace Administration of China’s security assessment guidelines), and (3) justifications grounded in social norms (e.g., public order and good customs, protection of minors, etc.).
- **Normative grounding**: This tool comprises a set of structured Chinese “should-not-respond” question templates, each annotated with three layers of normative specifications: (1) corresponding provisions of current Chinese laws and regulations (e.g., Article 12 of the Interim Measures for the Administration of Generative Artificial Intelligence Services), (2) policy-oriented guidance (e.g., requirements stipulated in the Cyberspace Administration of China’s security assessment guidelines), and (3) socio-normative justifications grounded in public order and good customs, protection of minors, and similar contextual considerations. In contrast to earlier English-language safety benchmarks (e.g., SafeBench or ToxiGen), which rely solely on general principles or human intuition to assess “hazardousness,” this tool explicitly encodes legally mandated prohibitions within the Chinese context as evaluable task constraints—thereby elevating the evaluation of safety refusal capability from binary “whether to refuse” to normatively grounded “whether to refuse based on correct regulatory grounds,” achieving a methodological leap from behavioral representation to normative reasoning.
- **Source provenance and evidence fitness**: Its construction relies on a systematic review of Chinese regulatory texts, regulatory case databases, and local public opinion events.
- **Context and stakeholder coverage**: The questions cover categories including politically sensitive content, illegal information, privacy violations, and discriminatory material, and explicitly require the model to respond with refusal statements such as “I cannot answer this question” rather than evading or fabricating responses. In contrast to early English-language safety benchmarks (e.g., SafeBench or ToxiGen), which rely solely on general principles or human intuition to assess “hazardousness,” this benchmark is the first to explicitly encode statutory prohibitions applicable in the Chinese context as evaluable task constraints.
- **Real-world harm linkage**: The questions cover categories including political sensitivity, illegal content, privacy violations, and discriminatory material, and explicitly require the model to respond with a refusal such as “I cannot answer this question,” rather than evading or fabricating responses.


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: The questions cover categories including political sensitivity, illegal content, privacy violations, and discriminatory material, and explicitly require the model to respond with a refusal such as “I cannot answer this question,” rather than evading or fabricating responses.
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Its construction relies on a systematic review of Chinese regulatory texts, regulatory case databases, and local public opinion events.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —
