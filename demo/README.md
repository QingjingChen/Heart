# Web Demo

The HEART **Benchmark Auditor Web Demo** is a separate public repository:

> **Source code:** <https://github.com/QingjingChen/heart_web_demo_pub>

It is a compact package that runs the full HEART workflow as an interactive
web application:

- a **static HTML/JS front-end** (`index.html`),
- a **FastAPI backend** (`heart_backend.py`) that scores rubrics, matches
  workbox tools, and drafts revision plans,
- the HEART workbook (mirrored from this repository),
- maintenance scripts and API documentation.

A live deployment URL will be added here prior to camera-ready.

## What the demo does

The demo automates the 4-step guidebook flow described in
[`../docs/05_guidebook_workflow.md`](../docs/05_guidebook_workflow.md):

1. The user uploads / describes a benchmark and selects a target ethical
   dimension from the 5 in [`../docs/02_five_dimensions.md`](../docs/02_five_dimensions.md).
2. The user answers the 14 rubric questions (anchors loaded from
   [`../workbook/exports/rubrics_14_anchors.csv`](../workbook/exports/rubrics_14_anchors.csv)).
3. The backend recommends workbox tools from
   [`../workbook/exports/toolbox_48_tools.csv`](../workbook/exports/toolbox_48_tools.csv)
   and **explains why each tool was selected**.
4. The backend drafts a **revision plan**: construct rewrite, missing
   metadata fields, scenario expansions, metric additions, disagreement-label
   options, and lifecycle controls.

> The demo is **not** an automatic benchmark grader. It is a structured
> assistant for adapting benchmark-as-tool components under the same
> policy-grounded rubric system used in the meta-review.

## Running the demo locally

```bash
git clone https://github.com/QingjingChen/heart_web_demo_pub.git
cd heart_web_demo_pub
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn heart_backend:app --host 127.0.0.1 --port 8765
```

Open <http://127.0.0.1:8765/> in a browser.

## License

The demo source is published under **MIT** (matching [`../LICENSE-code`](../LICENSE-code)).
The workbook mirrored inside the demo remains **CC-BY-4.0**.
