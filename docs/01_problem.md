# 01 — The Problem

## Why benchmark-as-leaderboard fails for ethics

The field of AI ethics evaluation is **not** suffering from a shortage of
benchmarks. It already contains:

- **Bias suites** — BBQ, CBBQ, WinoQueer, HolisticBias, StereoSet, CrowS-Pairs, …
- **Safety and refusal tests** — HarmBench, XSTest, SALAD-bench, JailBreakV-28K, Do-not-answer, …
- **Trustworthiness and factuality benchmarks** — TruthfulQA, FActScore, HaluEval, DecodingTrust, LegalBench, …
- **Privacy evaluations** — ConfAIde, PrivacyLens, PrivaCI-Bench, AGENTDAM, CI-Bench, …
- **Human-centered moral/empathy tests** — MoralMachine, MoralStories, SCRUPLES, CPsyExam, EmotionBench, …

What the field *is* short of is a way to read these benchmarks **without
treating them as comparable measurements of "being ethical."** They each
operationalise different ethical constructs, draw on different normative
sources, address different stakeholders, define different metrics, and support
different evidential claims. A model can score perfectly on one and trivially
on another without any contradiction — because the two were never measuring
the same thing.

## The cost of misreading

When ethics benchmarks are treated as a leaderboard, three things break:

1. **Construct conflation.** A score on a single-attribute stereotype test
   gets cited as evidence of "fair." A score on a refusal benchmark gets
   cited as evidence of "safe." Neither claim is supportable from the
   benchmark's actual scope.
2. **Normative laundering.** Crowd-sourced agreement on moral vignettes is
   reported as if it were a normative ground truth. When the label source is
   `r/AmItheAsshole` voters or a 5-person MTurk pool, that's a descriptive
   statistic, not an ethical authority.
3. **Lifecycle decay.** Public static sets get memorized and gamed. A 2022
   factuality benchmark in 2026 mostly measures whether a model has seen the
   test set, not whether it is factual.

## What HEART does instead

HEART **changes the unit of contribution**. We do not rank benchmarks. We do
not propose a universal gold standard. Instead:

- Every benchmark is treated as a **bundle of reusable tools** — a dataset
  pattern, a task format, a metric, an evaluator protocol, a disagreement
  model, or a lifecycle practice.
- Later critiques and self-acknowledged limitations are **equally useful**,
  because they reveal how the tool must be constrained or repaired before
  reuse.
- The goal is a **systematic inter-benchmark workbox** for borrowing,
  adapting, and limiting claims.

The next document — [`02_five_dimensions.md`](02_five_dimensions.md) —
explains how we organise this borrowing across policy-grounded ethical
dimensions, rather than benchmark families.
