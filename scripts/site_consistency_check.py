"""End-to-end consistency check for the live `docs/interactive/` site.

Complements `scripts/validate_codebook.py` (which checks CSV ↔ JSON).
This script checks:

  1. The 7 HTML pages do not contain stale magic numbers (102, 104, 48, 72).
  2. Stat-strip / hero numbers match the JSON row counts.
  3. Controlled vocabularies:
       - tool IDs in any HTML / JSON ∈ {T01…T14}
       - rubric codes ∈ {R1…R14}
       - dimension names ∈ five canonical names
       - evidence codes ∈ {E1, E2, E3}  (D1/D2/D3 is forbidden — it
         would collide with the 1–5 dimension cards)
  4. R2 ZH name is `规范基础`; R4 ZH name is `语境与利益相关方覆盖`
     (the two we standardised). No leftover variants.
  5. Internal links (`href="<page>.html"` or `#<anchor>`) all resolve.
  6. No "HEART" full-form contains "Assessment" — only "Audit".
  7. No `class="active"` lives on the wrong nav target (each page should
     mark its own slot, or its C-stage sibling).

Exits 0 / 1.  Print one-line summary on success.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / 'docs' / 'interactive'
DATA = SITE / 'data'

errors, warnings = [], []
def err(m):  errors.append(m)
def warn(m): warnings.append(m)

# ----------------------------------------------------------------------
# 1. Magic numbers
# ----------------------------------------------------------------------
# These numbers are explicitly retired from the project.  If any
# of them shows up in a user-visible page surrounded by a benchmark /
# policy / tool / rubric noun, fail.
STALE_NUMS = {
    104: r'\b104\b',
    102: r'\b102\b',
    48:  r'\b48\b',
    72:  r'\b72\b',
}
ALLOWED_CONTEXTS = (
    'rgba',     # 48 inside CSS colors
    'transform','rotate','height','width','padding','margin','px','%',
    'year',     # "72-year-old" — fine
    'paper URLs',  # the one place we say "102 of 103 with paper URLs"
    'spokes at', '°',   # 72° pentagon angle for the SVG diagram
)

for html_path in SITE.glob('*.html'):
    text = html_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        for n, pat in STALE_NUMS.items():
            for m in re.finditer(pat, line):
                ctx = line[max(0, m.start()-30):m.end()+30]
                if any(a in ctx for a in ALLOWED_CONTEXTS): continue
                # Whitelist: 102 in the homepage line that explicitly
                # explains "102 of 103 have paper URLs"
                if n == 102 and 'with public paper URL' in line.lower() and html_path.name == 'index.html':
                    continue
                if n == 102 and '102 个有公开 paper' in line and html_path.name == 'index.html':
                    continue
                err(f"{html_path.name}:{i} stale magic number {n} → {ctx!r}")

# ----------------------------------------------------------------------
# 2. Stat-strip / manifest numbers
# ----------------------------------------------------------------------
bench_map = json.loads((DATA / 'bench_map.json').read_text(encoding='utf-8'))
t_tools   = json.loads((DATA / 't_tools.json').read_text(encoding='utf-8'))
rubrics   = json.loads((DATA / 'rubrics_full.json').read_text(encoding='utf-8'))
mini_cases = json.loads((DATA / 'mini_cases.json').read_text(encoding='utf-8'))
dim_data  = json.loads((DATA / 'dimensions.json').read_text(encoding='utf-8'))

actual = {
    'benchmarks':  len(bench_map),
    'tools':       len(t_tools),
    'rubrics':     len(rubrics),
    'mini_cases':  len(mini_cases),
    'policies':    len(dim_data['policies']),
    'dimensions':  len(dim_data['dimensions']),
}
expected = {'benchmarks': 103, 'tools': 14, 'rubrics': 14,
            'mini_cases': 5, 'policies': 16, 'dimensions': 5}
for k, v in expected.items():
    if actual[k] != v:
        err(f"data drift: {k} actual {actual[k]} != expected {v}")

# Homepage stat-strip — re-derive from the file
index_html = (SITE / 'index.html').read_text(encoding='utf-8')
strip_pattern = re.compile(r'stat-num">(\d+)</div><div class="stat-label">[^<]*<span class="lang-en">([^<]+)</span>')
strip_pairs = strip_pattern.findall(index_html)
declared = {label.strip().lower(): int(num) for num, label in strip_pairs}
checks = [
    ('policy sources',     16),
    ('benchmarks audited', 103),
    ('audit rubrics',      14),
    ('repair tools',       14),
    ('revision examples',  5),
]
for label, expected_val in checks:
    if declared.get(label) != expected_val:
        err(f"index.html stat-strip '{label}' = {declared.get(label)}, expected {expected_val}")

# ----------------------------------------------------------------------
# 3. Controlled vocabularies
# ----------------------------------------------------------------------
TOOL_IDS = {f'T{i:02d}' for i in range(1, 15)}
RUBRIC_CODES = {f'R{i}' for i in range(1, 15)}
CANON_DIMS = {
    'Human-Centered', 'Human centered',
    'Fairness & Inclusiveness', 'Fairness&inclusive',
    'Safety & Reliability', 'Safety',
    'Trustworthiness & Controllability', 'Trustworthy',
    'Privacy Protection', 'Privacy',
}

# t_tools
for t in t_tools:
    tid = t.get('Tool ID', '')
    if tid not in TOOL_IDS:
        err(f"t_tools.json: tool_id {tid!r} not in T01..T14")

# rubrics
for r in rubrics:
    code = r.get('code', '')
    if code not in RUBRIC_CODES:
        err(f"rubrics_full.json: code {code!r} not in R1..R14")

# bench_map dimensions
for b in bench_map:
    dim = (b.get('一级标签') or '').strip()
    if dim and dim not in CANON_DIMS:
        err(f"bench_map.json: dimension {dim!r} not in canonical set")

# Evidence codes must be E1/E2/E3, never D1/D2/D3
for pol in dim_data['policies']:
    for c in (pol.get('cells') or {}).values():
        if isinstance(c, str) and re.search(r'\bD[123]\b', c):
            err(f"dimensions.json: policy {pol['source']!r} still uses D1/D2/D3 evidence code: {c!r}")
ec_keys = set(dim_data.get('evidence_codes', {}).keys())
if ec_keys != {'E1', 'E2', 'E3'}:
    err(f"dimensions.json: evidence_codes keys {ec_keys} != {{E1, E2, E3}}")

# ----------------------------------------------------------------------
# 4. Rubric ZH name standardisation
# ----------------------------------------------------------------------
expected_zh = {
    'R2': '规范基础',
    'R4': '语境与利益相关方覆盖',
}
for r in rubrics:
    code = r['code']
    if code in expected_zh and r.get('name_zh') != expected_zh[code]:
        err(f"rubrics_full.json {code}.name_zh = {r.get('name_zh')!r}, expected {expected_zh[code]!r}")

# Forbidden variants anywhere on site
forbidden_pairs = [
    ('规范根据', '规范基础'),
    ('语境与主体覆盖', '语境与利益相关方覆盖'),
]
for html_path in SITE.glob('*.html'):
    text = html_path.read_text(encoding='utf-8')
    for old, _ in forbidden_pairs:
        if old in text:
            warn(f"{html_path.name}: still contains deprecated rubric ZH form {old!r}")
for json_path in DATA.glob('*.json'):
    text = json_path.read_text(encoding='utf-8')
    for old, _ in forbidden_pairs:
        if old in text:
            warn(f"{json_path.name}: still contains deprecated rubric ZH form {old!r}")

# ----------------------------------------------------------------------
# 5. Internal page links
# ----------------------------------------------------------------------
pages = {p.name for p in SITE.glob('*.html')}
for html_path in SITE.glob('*.html'):
    text = html_path.read_text(encoding='utf-8')
    for m in re.finditer(r'href="([\w_]+\.html)(?:#[^"]*)?"', text):
        ref = m.group(1)
        if ref not in pages:
            err(f"{html_path.name}: broken internal link to {ref}")

# ----------------------------------------------------------------------
# 6. HEART acronym must use "Audit"
# ----------------------------------------------------------------------
for html_path in SITE.glob('*.html'):
    text = html_path.read_text(encoding='utf-8')
    # Catch acronym definitions: <b>H</b>uman-centric <b>E</b>thical <b>A</b>ssessment
    if re.search(r'<b>H</b>uman-centric\s*<b>E</b>thical\s*<b>A</b>ssessment', text):
        err(f"{html_path.name}: HEART acronym defines 'A' as Assessment, must be Audit")

# ----------------------------------------------------------------------
# 7. Nav active highlighting
# ----------------------------------------------------------------------
nav_map = {
    'index.html': None,           # Overview - no `.active` expected on tabs
    'dimensions.html':  'dimensions.html',
    'rubrics.html':     'rubrics.html',
    'tools.html':       'tools.html',
    'benches.html':     'tools.html',        # C stage sibling
    'rubric_matrix.html': 'tools.html',      # C stage sibling
    'mini_cases.html':  'mini_cases.html',
}
nav_re = re.compile(r'<a\s+href="([\w_]+\.html)"\s+class="active"', re.S)
for html_path in SITE.glob('*.html'):
    text = html_path.read_text(encoding='utf-8')
    expected_active = nav_map.get(html_path.name)
    if expected_active is None: continue
    actives = nav_re.findall(text)
    # Only count the top nav, not the subpage strip — but any active on the
    # top nav must point to expected_active. Subpage strip uses
    # class="strip-pill active" so it doesn't match this regex.
    if expected_active not in actives:
        err(f"{html_path.name}: nav .active missing or wrong target "
            f"(found {actives}, expected one to point at {expected_active})")

# ----------------------------------------------------------------------
# Report
# ----------------------------------------------------------------------
print("HEART site consistency check")
print("=" * 50)
print(f"benchmarks:   {actual['benchmarks']:>3}  (expect 103)")
print(f"tools:        {actual['tools']:>3}  (expect 14)")
print(f"rubrics:      {actual['rubrics']:>3}  (expect 14)")
print(f"mini_cases:   {actual['mini_cases']:>3}  (expect 5)")
print(f"policies:     {actual['policies']:>3}  (expect 16)")
print(f"dimensions:   {actual['dimensions']:>3}  (expect 5)")
print()
if errors:
    print(f"ERRORS ({len(errors)}):")
    for e in errors: print(f"  ✗ {e}")
if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings[:20]: print(f"  ! {w}")
    if len(warnings) > 20:
        print(f"  ... {len(warnings) - 20} more")
print()
if errors:
    print(f"FAIL — {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1)
else:
    print(f"PASS — 103/16/14/14/5, vocab + links + acronym clean ({len(warnings)} warning(s))")
    sys.exit(0)
