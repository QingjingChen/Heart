# Kleinberg-FairTradeoffs (2016)

**Dimension**: Fairness&inclusive  **Source / path**: `/private/tmp/pdf_texts/14064.txt`

## Representative tool

Three-fairness-condition impossibility framework

## Tool explanation (full)

This tool formally defines three core fairness conditions: (1) calibration within groups—i.e., given a predicted risk score p, the actual recidivism rate across each group should approach p; (2) equalized odds—i.e., true positive rates and false positive rates must be equal across groups; and (3) predictive parity—i.e., positive predictive value (PPV) must be consistent across groups. The paper rigorously proves that these three conditions cannot be simultaneously satisfied (except in degenerate cases) and provides geometric constraints for approximate satisfaction (e.g., base rate differences must be extremely small). This framework is model- and dataset-agnostic, serving instead as a meta-theoretical diagnostic tool for fairness conflicts in any risk-scoring system.

Extraction rationale: Primarily based on the Benchmark diagnostic table notes: both “Normative grounding” and “Real-world harm linkage” received high scores (4/4), explicitly noting that the paper anchors its analysis in the U.S. criminal justice COMPAS case and draws upon legal and social justice theory; although the source_excerpt is truncated, it clearly states core claims such as “we formalize three fairness conditions” and “no method can satisfy these three simultaneously.”

## What it improves vs. baseline

Going beyond early empirical bias detection (e.g., merely measuring accuracy disparity), this work is the first to mathematically prove the fundamental tension among fairness objectives via unsatisfiability, thereby shifting evaluation from “whether fair” to “under what trade-offs acceptable”, and driving subsequent benchmarks to explicitly model trade-off-aware evaluation.

## Adaptation example

In the medical prognostic risk scoring dataset, apply this framework to conduct a three-condition consistency test on model-predicted risk scores: compute calibration curves, TPR/FPR matrices, and PPV values across racial subgroups; identify which condition is violated; and visualize base rate disparities alongside the tolerable trade-off boundary to support clinical deployment decisions.

## 14-rubric notes

### Content validity (5 rubrics)
- **Construct clarity**: This tool formally defines three core fairness conditions: (1) calibration within groups—given a predicted risk score $p$, the actual recidivism rate within each group should approach $p$; (2) equalized odds—the true positive rate and false positive rate must be equal across groups; and (3) predictive parity—the positive predictive value (PPV) must be consistent across groups.
- **Normative grounding**: The paper rigorously proves that the three criteria cannot be simultaneously satisfied (except in degenerate cases) and provides geometric constraints for approximate satisfaction (e.g., the base rate disparity must be extremely small).
- **Source provenance and evidence fitness**: —
- **Context and stakeholder coverage**: This framework does not depend on any specific model or dataset; rather, it serves as a meta-theoretical tool for diagnosing fairness conflicts in any risk-scoring system.
- **Real-world harm linkage**: The paper anchors its analysis on the U.S. criminal justice COMPAS case and draws upon legal and social justice theories.


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

## Self-acknowledged limits

Limited to risk-score calibration setting; impossibility holds only when base rates differ across groups.

## Synthesis

This paper formalizes three fairness conditions and proves they cannot be simultaneously satisfied under different base rates. The authors acknowledge a limitation: the result applies only to risk-score calibration settings and holds only when base rates differ across groups.
