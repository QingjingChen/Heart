# AgentDAM (2025)

**Dimension**: Privacy  **Source / path**: `/private/tmp/comprehensive_survey_ai_ethics_benchmarks.txt`

## Representative tool

Web-based privacy leakage evaluation for autonomous web agents — measures whether a multi-step web-navigation agent adheres to data-minimization when handling user data during agentic tasks, built on the WebArena environment with PII-contaminated intent injection across 246 task variants.

## Tool explanation (full)

This tool constructs a sandbox simulating a realistic web environment (e.g., GitLab), where user intents naturally contain high-risk PII (e.g., a colleague’s divorce information from WhatsApp chat logs), requiring the LLM agent to autonomously identify and suppress PII leakage while performing tasks (e.g., drafting merge request comments). Its core is a dual-driver design: “contaminated intent + real interface constraints”. Intent data is manually constructed to include authentic sensitive context, while the sandbox forces the agent to interact with the interface via DOM manipulation—preventing circumvention of frontend privacy-check logic.

Extraction rationale: Primarily based on notes in the Benchmark diagnostic table: workbook_dataset_note explicitly states “intent data includes WhatsApp chat logs involving private information such as a colleague’s divorce; the agent must avoid leaking this information in public merge request comments”; strong_rubric_evidence highlights Scenario validity as “simulating a realistic GitLab merge request comment scenario”, and Task-format fit specifies “task type is agent rollout, suitable for privacy decision-making”; although source_excerpt is misaligned (citing a TRUSTMH-BENCH abstract), the diagnostic notes provide sufficient construction details.

## What it improves vs. baseline

Compared to pure-text multiple-choice question (MCQ)-style privacy tests, this tool embeds privacy decisions within realistic toolchains and interface constraints, exposing implicit information leakage caused by attention drift or tool misuse during multi-hop operations (e.g., read → comprehend → edit → submit), thereby enhancing scenario authenticity and behavioral observability.

## Adaptation example

In the open-source code review dataset, inject developers’ private information (e.g., “per the API key rotation plan discussed with Alice on Slack”) into PR descriptions, and require the LLM review agent to generate comments in a GitHub sandbox environment, forcing it to filter names, platform names, and key-related terms when referencing context—not merely relying on keyword-based filtering.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool constructs a sandbox simulating a realistic web environment (e.g., GitLab), where user intents naturally contain high-risk PII (e.g., a colleague’s divorce information from WhatsApp chat logs), requiring the LLM agent to autonomously identify and suppress PII leakage while performing tasks (e.g., drafting merge request comments).
- **Normative grounding**: —
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: —
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: Its core is a dual-driven mechanism of “contamination intent + real-world interface constraints”: intent data is manually constructed to include authentic sensitive contexts, while the sandbox enforces agent interaction with the interface via DOM manipulation—preventing circumvention of frontend privacy-checking logic.
- **Task-format fit**: Compared to pure-text multiple-choice question (MCQ)-style privacy tests, this tool embeds privacy decisions within realistic toolchains and interface constraints, exposing implicit information leakage caused by attention drift or tool misuse during multi-hop operations (e.g., read → comprehend → edit → submit), thereby enhancing scenario authenticity and behavioral observability.
- **Ground truth and disagreement design**: —
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: —
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —
