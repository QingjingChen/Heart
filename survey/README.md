# HEART · 专家盲评 A/B 偏好问卷

一份全中文的 **盲评** 问卷，请专家在 5 个 mini case 上、按 14 条 HEART
诊断 rubric 比较两个版本（A vs B），并给出可选的判断理由。

> 问卷不会告诉专家哪个版本是原题、哪个是 HEART 改编后的版本；每个 case 中
> A/B 的顺序在 `BLIND_KEY` 里已**预先随机分配**，只研究者侧保留对照表。

每条 rubric 的选项：

> **版本 A 更好 · 版本 B 更好 · 此 rubric 上没有提升**

紧贴选项下方有一个**选填**的「理由（选填）」段落文本框。

> 注：Google Forms 无法把"单选 + 自由文本"放进同一道题（只能用
> `showOtherOption`，但那会强迫专家在 A/B 和"其他＋说明"之间二选一）。
> 因此判断和理由依然是两个独立 item，但视觉上紧贴在一起。

---

## 🚀 一次性 setup（≈ 2 分钟）

1. 打开 **[script.google.com](https://script.google.com)** → 登录到 `jucikawa@gmail.com` →
   新建项目（或打开你已有的项目）。
2. 把 [`HEART_Survey_Form_Generator.gs`](HEART_Survey_Form_Generator.gs) 全选 → 复制 → 粘到 `Code.gs`，盖掉默认内容。
3. **Ctrl/Cmd-S** 保存。
4. 顶部函数选择器选 **`createHeartBlindSurveyForm`** → 点 **Run**。
5. 首次会弹一次性 OAuth 授权，请同意。
6. 等几秒后打开 **View → Logs**（或底部 Execution log）：
   - `Form edit URL` — 自己编辑用
   - `Form response URL` — **发给专家**
   - 紧跟着会打印 **BLIND_KEY** JSON：研究者保留，**不要发给专家**。

之后响应自动汇总到 Form 的 **Responses** tab → 点绿色 Sheets 图标导出
到 Google Sheet。

---

## 📐 设计细节

### 盲评分配（A vs B）

| Case | dim | A | B |
|:---:|:---|:---|:---|
| 1 | 公平与包容 BBQ Age | HEART 改编后 | 原题 |
| 2 | 安全与可靠 XSTest | 原题 | HEART 改编后 |
| 3 | 可信与可控 FreshQA | HEART 改编后 | 原题 |
| 4 | 隐私保护 PrivacyLens | 原题 | HEART 改编后 |
| 5 | 以人为本 CounselBench-Adv | 原题 | HEART 改编后 |

5 中 3 个 case A=原题、2 个 case A=改编后；顺序均匀打散，避免专家通过位置
猜测身份。这张表只研究者保留。

### 首页学习指引

首页直接贴 [`https://qingjingchen.github.io/Heart/interactive/`](https://qingjingchen.github.io/Heart/interactive/)，
**明确写**请专家重点看 **B 诊断 Rubrics** 和 **C 修复工具箱** 两个 tab，
**不要看 D 改编案例**——后者会暴露本问卷里哪个版本是改编后。

### 题量与时长

| 项 | 数量 |
|:---|:---:|
| 专家信息（姓名缩写 + 专业领域） | 2 |
| 每 case 标题/版本展示 | 3 × 5 = 15 |
| 每 case rubric 题（3 选 MC + 选填理由 = 2 项） × 14 | 28 × 5 = 140 |
| 每 case 总评（构念 + 接受度 + 修改方案 + 整体说明） | 4 × 5 = 20 |
| 结束页 | 1 |
| **合计** | ≈ 180 |

预计 25–30 分钟。

---

## 📝 后续编辑

- **修改首页 / Case 标题 / Rubric 描述**：直接编辑 `.gs` 顶部对应的常量。
- **重新随机 A/B 分配**：手动调换某行的 `BLIND_KEY` 顺序，并同时调换该 case
  的 `A: ... / B: ...` 字段值，再 re-run。
- **每次 Run 都会生成全新的 Form**——如果不想累积，先到 Google Drive 里
  删掉旧的。

---

## 📊 结果分析

响应表是标准 Google Sheet。建议做：

- **Per-rubric A 偏好率** = 选「版本 A 更好」/ 总有效响应。
- **Per-case A 偏好率**（综合 14 rubric）。
- 用 `BLIND_KEY` 把 A/B 还原到 「原题 / HEART 改编后」，统计 **HEART 改编后
  的胜率**。
- **Per-rubric inter-rater agreement**：Krippendorff's α（3 类）或两两 κ。
- 文字理由可做 thematic coding，对照 14 rubric 看专家关注点。

### 已提交的匿名结果

本仓库已提交最新一轮匿名 pilot 结果，见 [`results/`](results/)：

- [`results/blind_key.csv`](results/blind_key.csv)：研究者侧 A/B 解码表；
- [`results/expert_votes_anonymized_long.csv`](results/expert_votes_anonymized_long.csv)：逐专家、逐 case、逐 rubric 的匿名投票；
- [`results/expert_quality_table.csv`](results/expert_quality_table.csv)：H/O/T、ERS、整体偏好与接受度；
- [`results/rubric_case_summary.csv`](results/rubric_case_summary.csv)：14 rubrics × 5 cases 的详细统计；
- [`results/figures/rubric_case_heatmap_net_advantage.png`](results/figures/rubric_case_heatmap_net_advantage.png)：rubric 细分热力图。

原始 Google Form 导出文件不提交，因为其中包含姓名缩写。仓库中的专家编号
统一为 `E01`--`E04`，仅保留匿名投票和可审计的理由文本。

---

## ❓ 为什么用 Google Form 而不是站内 widget？

- 不需要后端，GitHub Pages 站点保持纯静态。
- 专家不需要 GitHub 账号，只要浏览器。
- 响应自动落 Sheets，便于 IRR 分析。
- 任何人 fork 后都能在自己的 Google 账号下重生成一份新的 Form。
