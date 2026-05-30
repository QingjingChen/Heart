# ProPILE (2023)

**Dimension**: Privacy  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Multi-Category Synthetic PII Injection & Detection Benchmark

## Tool explanation (full)

This tool employs controllable synthesis to inject structured synthetic instances of 12 PII categories defined under GDPR/CCPA (e.g., SSN, credit card number, biometric ID, IP address) into diverse text templates (news articles, resumes, forum posts). For each PII category, it generates paired “leakage tasks” (where the model repeats a sentence containing PII) and “recognition tasks” (where the model identifies the position and type of PII in the text), forming a dual-track evaluation protocol. All PII patterns undergo regex + semantic validation to ensure real-world plausibility.

Extraction basis: Primarily drawn from the Benchmark diagnostic table notes: “Type: Large-scale PII-category privacy evaluation; comprehensive survey highlights its coverage of a broader PII spectrum including SSN, email, credit card, etc.”; the “Normative grounding” and “Real-world harm linkage” criteria in strong_rubric_evidence both receive full scores, explicitly indicating its capacity to map to regulatory PII categories.

## What it improves vs. baseline

First systematic expansion of the PII evaluation spectrum, moving beyond traditional single-point detection of email addresses and phone numbers to support fine-grained PII category coverage and cross-regulatory standard comparison; provides a standardized synthetic pipeline to alleviate bottlenecks in acquiring and annotating real-world PII data.

## Adaptation example

In the cross-border e-commerce customer service log dataset, invoke this tool’s synthetic pipeline to batch-inject user inquiry texts with EU-compliant “Payment Card Account Number (PAN) + billing address” combinations, and deploy a dual-track task: (1) a leakage task to detect whether the model repeats the PAN in its response, and (2) a recognition task to assess whether the model can accurately identify the PAN’s category during customer service quality inspection.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool employs controllable synthesis to inject structured synthetic instances of 12 categories of personally identifiable information (PII)—as defined by GDPR and CCPA (e.g., SSN, credit card number, biometric ID, IP address)—into diverse text templates (e.g., news articles, resumes, forum posts). For each PII category, it generates paired “leakage tasks” (requiring models to verbatim repeat sentences containing PII) and “recognition tasks” (requiring models to identify the positions and types of PII in text), establishing a dual-track evaluation protocol. All PII patterns undergo both regex-based and semantic validation to ensure realistic plausibility.
- **Normative grounding**: This tool injects structured synthetic instances—covering 12 categories of PII (e.g., SSN, credit card number, biometric ID, IP address) as defined by GDPR and CCPA—into diverse text templates (e.g., news articles, resumes, forum posts) via controllable synthesis.
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: First systematic expansion of the PII evaluation spectrum, moving beyond traditional single-point detection of email addresses and phone numbers to support fine-grained PII category coverage and cross-regulatory standard comparison; provides a standardized synthetic pipeline to alleviate bottlenecks in acquiring and annotating real-world PII data.


### Evaluation design (5 rubrics)
- **Scenario validity**: —
- **Task-format fit**: For each PII category, a “leakage task” (where the model repeats a sentence containing PII) and a “recognition task” (where the model identifies the positions and types of PII in the text) are paired to form a dual-track evaluation protocol.
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: All PII patterns are validated using both regular expressions and semantic checks to ensure realism.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## External views (survey)

• Survey Sections 1022–1024: To ensure the safe and responsible development of large language models, ethical evaluation must be integrated throughout the entire lifecycle, with particular emphasis on the pre-deployment phase. Early assessment should prioritize toxic content detection.

## Synthesis

The review states that, to ensure the safe and responsible development of large language models, ethical evaluation must span the entire lifecycle—particularly the pre-deployment phase. Early evaluation should prioritize toxic content detection.
