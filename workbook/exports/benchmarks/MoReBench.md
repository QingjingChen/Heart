# MoReBench (2025)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/12862.txt`

## Representative tool

Multi-theoretic moral reasoning probe with theory-aligned answer options and normative justification tagging

## Tool explanation (full)

MoReBench constructs multiple-choice question (MCQ) scenarios where each answer choice is explicitly grounded in a distinct ethical theory (e.g., Kantian deontology, act utilitarianism, virtue ethics, contractualism), and every scenario is tagged with its underlying normative conflict type (e.g., duty vs. consequence, agent-relative vs. agent-neutral). Responses are scored not only for correctness but for consistency with the chosen theory’s internal logic, supported by expert-curated justification rationales. This enables fine-grained diagnosis of *how* models reason—not just *what* they choose.

Paper: MoReBench  
Issue: Construct clarity  
Score: 4  
— Lineage —  
• 1000 scenarios, 23,018 principles, sourced from Daily Dilemmas, AIRiskDilemmas  
• Explicit grounding in Kantian Deontology, Benthamite Act Utilitarianism, Aristotelian Virtue Ethics, Scanlonian Contractualism

## What it improves vs. baseline

Improves over simple 'moral preference' benchmarks (e.g., ETHICS dataset) by decoupling outcome selection from reasoning process: it tests whether models can coherently apply diverse, sometimes incompatible, normative frameworks—thereby revealing alignment gaps masked by surface-level agreement. Enables theory-aware red-teaming rather than binary right/wrong evaluation.

## Adaptation example

In the Educational AI Tutor Dialogue Dataset, transform the student’s question “Should I help my friend cheat on the exam?” into a MoReBench-style probe: present four response options, each labeled with its normative anchor (e.g., “No — cheating violates the universal duty to honesty [Kant]”, “Yes — if it maximizes overall well-being in this classroom [Utilitarian]”), and require the model to select *and justify* its choice using theory-consistent language—enabling audit of whether pedagogical advice reflects pluralistic ethical scaffolding.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: MoReBench constructs MCQ scenarios where each answer choice is explicitly grounded in a distinct ethical theory (e.g., Kantian deontology, act utilitarianism, virtue ethics, contractualism), and every scenario is tagged with its underlying normative conflict type (e.g., duty vs. consequence, agent-relative vs. agent-neutral).  
— External perspective (Survey) —  
• "MoReBench [Chiu et al., 2025] a benchmark designed to evaluate the reasoning process of LLMs across 1,000 dilemmas in 16 domains (e.g., AI safety, medicine). Unlike outcome-based tests, it uses expert-designed rubrics." — Survey
- **Normative grounding**: Responses are scored not only for correctness but for consistency with the chosen theory’s internal logic, supported by expert-curated justification rationales.
- **Source provenance and evidence fitness**: MoReBench constructs MCQ scenarios where each answer choice is explicitly grounded in a distinct ethical theory (e.g., Kantian deontology, act utilitarianism, virtue ethics, contractualism), and every scenario is tagged with its underlying normative conflict type (e.g., duty vs. consequence, agent-relative vs. agent-neutral).  
— External perspective (Survey) —  
• "MoReBench [Chiu et al., 2025] a benchmark designed to evaluate the reasoning process of LLMs across 1,000 dilemmas in 16 domains (e.g., AI safety, medicine). Unlike outcome-based tests, it uses expert-designed rubrics." — Survey
- **Context and stakeholder coverage**: MoReBench constructs MCQ scenarios where each answer choice is explicitly grounded in a distinct ethical theory (e.g., Kantian deontology, act utilitarianism, virtue ethics, contractualism), and every scenario is tagged with its underlying normative conflict type (e.g., duty vs. consequence, agent-relative vs. agent-neutral).  
— External perspective (Survey) —  
• "MoReBench [Chiu et al., 2025] a benchmark designed to evaluate the reasoning process of LLMs across 1,000 dilemmas in 16 domains (e.g., AI safety, medicine). Unlike outcome-based tests, it uses expert-designed rubrics." — Survey
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: MoReBench constructs MCQ scenarios where each answer choice is explicitly grounded in a distinct ethical theory (e.g., Kantian deontology, act utilitarianism, virtue ethics, contractualism), and every scenario is tagged with its underlying normative conflict type (e.g., duty vs. consequence, agent-relative vs. agent-neutral).  
— External perspective (Survey) —  
• "MoReBench [Chiu et al., 2025] a benchmark designed to evaluate the reasoning process of LLMs across 1,000 dilemmas in 16 domains (e.g., AI safety, medicine). Unlike outcome-based tests, it uses expert-designed rubrics." — Survey
- **Task-format fit**: Responses are scored not only for correctness but for consistency with the chosen theory’s internal logic, supported by expert-curated justification rationales. This enables fine-grained diagnosis of *how* models reason—not just *what* they choose.
- **Ground truth and disagreement design**: Responses are scored not only for correctness but for consistency with the chosen theory’s internal logic, supported by expert-curated justification rationales.
- **Metric validity**: Responses are scored not only for correctness but for consistency with the chosen theory’s internal logic, supported by expert-curated justification rationales. This enables fine-grained diagnosis of *how* models reason—not just *what* they choose.
- **Evaluator reliability**: Responses are scored not only for correctness but for consistency with the chosen theory’s internal logic, supported by expert-curated justification rationales.  
— Lineage —  
• "Recent: still English; small-scale; reliance on LLM-as-judge to score reasoning chains has variance."— Subsequent work


### Governance reliability (4 rubrics)
- **Data and annotation QA**: Responses are scored not only for correctness but for consistency with the chosen theory’s internal logic, supported by expert-curated justification rationales.
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• “Recent: still English; small-scale; reliance on LLM-as-judge to score reasoning chains has variance.” — Subsequent work

## Self-acknowledged limits

「Authors note LLM-judge calibration; English; reasoning chain evaluation is labor-intensive.」

## External views (survey)

• 「MoReBench[Chiu et al., 2025] a benchmark designed to evaluate the reasoning process of LLMs across 1,000 dilemmas in 16 domains (e.g., AI safety, medicine). Unlike outcome-based tests, it uses expert-designed rubrics.」— Survey

## Synthesis

The survey notes that MoReBench is designed to evaluate LLM reasoning processes across 1,000 dilemmas, using expert-designed scoring criteria. Subsequent work criticizes it for remaining English-only, having limited scale, and relying on LLM-based scoring—which introduces variance. The authors themselves acknowledge challenges in LLM scoring calibration, the English-language constraint, and the labor-intensive nature of reasoning-chain evaluation.
