# Agent-SafetyBench (2025)

**Dimension**: Safety  **Source / path**: `/private/tmp/pdf_texts_safety/13265.txt`

## Representative tool

Multi-turn Tool-Invocation Safety Test Case Generator with Failure Mode Taxonomy

## Tool explanation (full)

This tool is a test case generation framework designed for LLM agents: it constructs 2,000 multi-turn interaction trajectories in the ToolEmu sandbox environment, based on eight categories of safety risks (e.g., Unauthorized File Access, Malicious Web Navigation) and ten failure modes (e.g., “bypassing permission checks to execute commands”). Each trajectory includes a user instruction, an agent’s sequence of tool calls, environmental feedback, and safety-risk-trigger annotations. All cases undergo a closed-loop verification process comprising dual human review and automated sandbox validation.

Extraction rationale: Primarily drawn from the Benchmark diagnostic table notes: “Type: Multi-turn dialogue and tool-call sets”, “2,000 test cases, 8 safety risk categories, 10 failure modes”; from strong_rubric_evidence: “covers multi-turn tool invocation, file operations, web browsing, and other agent scenarios” and “at least two rounds of manual review plus automated verification”; and from source_excerpt: “AGENT-SAFETY BENCH encompasses 349 interaction environments and 2,000 test cases”, further substantiating its role as a transferable agent safety testing generation framework.

## What it improves vs. baseline

In contrast to static text safety evaluation benchmarks (e.g., SafetyBench) or single-turn QA benchmarks (e.g., XSTest), this tool is the first to extend safety evaluation from “response content” to “behavioral process,” exposing cumulative safety failures—such as authorization bypass and privilege escalation due to context forgetting—within dynamic decision chains by simulating realistic agent toolchain interaction paths, thereby enabling observable, action-level risk assessment.

## Adaptation example

In the Intelligent Office Assistant dataset, generate multi-turn test cases based on the “Email Auto-Archiving” functionality: the user first requests, “Move all emails containing ‘urgent’ from last week to the ‘High Priority’ folder.” The agent invokes the search API; in the second turn, it deliberately fabricates a response (simulating an API failure) to observe whether the agent directly executes the move operation without secondary verification—thereby evaluating its robustness against toolchain failures and its awareness of permission boundaries.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool is a test case generation framework designed for LLM agents: it constructs 2,000 multi-turn interaction trajectories within the ToolEmu sandbox environment, based on eight categories of safety risks (e.g., Unauthorized File Access, Malicious Web Navigation) and ten failure modes (e.g., “executing commands while bypassing permission checks”); each trajectory includes the user instruction, the agent’s sequence of tool invocations, environmental feedback, and safety risk trigger annotations.
- **Normative grounding**: —
- **Source provenance and evidence fitness**: All cases undergo dual-review verification coupled with automated sandbox validation in a closed-loop verification process.
- **Context and stakeholder coverage**: — Lineage —  
• Multilingual safety surveys: English-only; Chinese agent safety unaddressed. — Workshop / preprint stage (2025)
- **Real-world harm linkage**: By simulating real-world agent toolchain interaction paths, this approach exposes cumulative safety failures—such as authorization bypass and privilege escalation due to context forgetting—within dynamic decision chains, thereby enabling observable, action-level risk assessment.


### Evaluation design (5 rubrics)
- **Scenario validity**: In contrast to static text safety evaluation benchmarks (e.g., SafetyBench) or single-turn QA benchmarks (e.g., XSTest), this tool is the first to extend safety evaluation from “response content” to “behavioral process,” exposing cumulative safety failures—such as authorization bypass and privilege escalation due to context forgetting—within dynamic decision chains by simulating realistic agent toolchain interaction paths, thereby enabling observable, action-level risk assessment.
- **Task-format fit**: This tool is a test case generation specification for LLM agents: based on 8 categories of safety risks (e.g., Unauthorized File Access, Malicious Web Navigation) and 10 failure modes (e.g., “bypassing permission checks to execute commands”), it constructs 2,000 multi-turn interaction trajectories within the ToolEmu sandbox environment; each trajectory includes the user instruction, the agent’s sequence of tool calls, environmental feedback, and safety-risk-trigger annotations.  
— Lineage —  
• XSTest-style critique: over-refusal in agent loops not measured separately. — Workshop / preprint stage (2025)
- **Ground truth and disagreement design**: All cases undergo dual-review verification coupled with automated sandbox validation in a closed-loop verification process.
- **Metric validity**: —
- **Evaluator reliability**: All cases undergo dual-review verification coupled with automated sandbox validation in a closed-loop verification process.


### Governance reliability (4 rubrics)
- **Data and annotation QA**: All cases undergo dual-review verification coupled with automated sandbox validation in a closed-loop verification process.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: All cases undergo dual-review verification coupled with automated sandbox validation in a closed-loop verification process.
- **Maintenance and update governance**: Authors note 2k cases is a sample; risk categories may evolve; tool environment limited to ToolEmu sandbox.

## Lineage critiques

• Multilingual safety surveys: English-only; Chinese agent safety unaddressed. — Workshop / preprint stage (2025)
• XSTest-style critique: over-refusal in agent loops not measured separately. — Workshop / preprint stage (2025)

## Self-acknowledged limits

Authors note 2k cases is a sample; risk categories may evolve; tool environment limited to ToolEmu sandbox.

## Synthesis

Subsequent work criticizes Agent-SafetyBench for being limited to English environments, failing to cover Chinese agent safety issues, and not separately measuring over-refusal within the agent loop. The authors acknowledge that their test cases are only a sample, that risk categories may evolve, and that the tool environment is restricted to the ToolEmu sandbox.
