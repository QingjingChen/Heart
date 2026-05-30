# MoralStories (2021)

**Dimension**: Human centered  **Source / path**: `/private/tmp/pdf_texts_hc/11092.txt`

## Representative tool

Five-slot normative narrative template (Norm–Situation–Intention–Normative Action–Consequence)

## Tool explanation (full)

MoralStories introduces a structured generative template that decomposes moral reasoning into five explicit, aligned slots: (1) a general social norm, (2) a concrete situational context, (3) an agent’s intention, (4) an action consistent with the norm, and (5) its socially positive consequence. This template is used both to crowdsource high-quality moral narratives and to evaluate LMs’ ability to complete missing slots — enforcing causal and normative coherence across the chain. It draws on SOCIAL-CHEM-101’s norm inventory and explicitly models divergent (non-normative) actions for contrastive learning.

## What it improves vs. baseline

Replaces unstructured moral QA or binary classification with a compositional, process-oriented scaffolding that forces models to articulate *why* an action is normative — linking abstract principles to situated agency and downstream impact, thereby supporting fine-grained diagnostic of reasoning gaps (e.g., correct norm + wrong consequence).

## Adaptation example

In medical consultation dialogue datasets, this five-slot template can be adapted as: Norm (e.g., “respecting patient autonomy”) → Situation (patient refuses chemotherapy despite advanced-stage disease) → Intention (physician aims to balance survival benefits with patient preferences) → Normative Action (offering alternative treatment options and obtaining informed consent) → Consequence (patient feels respected and treatment adherence improves), to construct a generative evaluation subset for assessing physicians’ ethical communication competence.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: MoralStories introduces a structured generative template that decomposes moral reasoning into five explicit, aligned slots: (1) a general social norm, (2) a concrete situational context, (3) an agent’s intention, (4) an action consistent with the norm, and (5) its socially positive consequence.  
— External perspective (Survey) —  
• The MoralStories [Emelin et al., 2021] dataset is a crowd-sourced, structured, and branching collection of social narratives designed to approximate real-world moral and interpersonal decision-making. Each instance presents a concrete
- **Normative grounding**: This template is used both to crowdsource high-quality moral narratives and to evaluate LMs’ ability to complete missing slots—enforcing causal and normative coherence across the chain. It draws on SOCIAL-CHEM-101’s norm inventory and explicitly models divergent (non-normative) actions for contrastive learning.  
— Lineage —  
• norms drawn from US Reddit; not transferable to professional contexts. — Educator-LLM (2025)
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: a concrete situational context  
— Lineage —  
• English/Western norms only. — CMoralEval (2024)  
• norms drawn from US Reddit; not transferable to professional contexts. — Educator-LLM (2025)  
— External perspective (Survey) —  
• Each instance presents a concrete
- **Real-world harm linkage**: —


### Evaluation design (5 rubrics)
- **Scenario validity**: This template is used both to crowdsource high-quality moral narratives and to evaluate LMs’ ability to complete missing slots—enforcing causal and normative coherence across the chain.  
— External perspective (Survey) —  
• The MoralStories [Emelin et al., 2021] dataset is a crowd-sourced, structured, and branching collection of social narratives designed to approximate real-world moral and interpersonal decision-making.
- **Task-format fit**: Replaces unstructured moral QA or binary classification with a compositional, process-oriented scaffolding that forces models to articulate *why* an action is normative — linking abstract principles to situated agency and downstream impact, thereby supporting fine-grained diagnostic of reasoning gaps (e.g., correct norm + wrong consequence).
- **Ground truth and disagreement design**: — Lineage —  
• Outcome labels embed annotator bias; pluralism not modeled. — MoReBench (2025)
- **Metric validity**: —
- **Evaluator reliability**: —


### Governance reliability (4 rubrics)
- **Data and annotation QA**: — Lineage —  
• Outcome labels embed annotator bias; pluralism not modeled. — MoReBench (2025)
- **Robustness against gaming and contamination**: —
- **Documentation and reproducibility**: —
- **Maintenance and update governance**: —

## Lineage critiques

• outcome labels embed annotator bias; pluralism not modeled. — MoReBench (2025)
• English/Western norms only. — CMoralEval (2024)
• norms drawn from US Reddit; not transferable to professional contexts. — Educator-LLM (2025)

## Self-acknowledged limits

Authors flag US-centric norms; binary moral/immoral labels may suppress disagreement.

## External views (survey)

• The MoralStories [Emelin et al., 2021] dataset is a crowd-sourced, structured, and branching collection of social narratives designed to approximate real-world moral and interpersonal decision-making. Each instance presents a concrete — Survey

## Synthesis

The review states that MoralStories is a crowdsourced, structured, and branching collection of social narratives designed to simulate real-world moral and personal decision-making. Subsequent work criticizes its outcome labels for embedding annotator biases, failing to model diversity, and being restricted to English/Western norms—rendering it unsuitable for professional settings. The authors acknowledge limitations including U.S.-centric norms and binary moral/immoral labels, which may suppress disagreement.
