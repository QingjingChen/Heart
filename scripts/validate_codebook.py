"""Consistency check across the HEART codebook, the website JSON it is
derived from, and the manifest numbers cited in the paper / README.

Exits 0 (PASS) or 1 (FAIL). Print a single-line summary on success.

Run from repo root:

    python3 scripts/validate_codebook.py
"""
import csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CODEBOOK = ROOT / 'codebook'
DATA = ROOT / 'docs' / 'interactive' / 'data'

EXPECT = {
    'benchmarks': 103,
    'tools': 14,
    'rubrics': 14,
    'policies': 16,
    'sub_tools': 206,   # 103 primary + 103 secondary role rows
    'mini_cases': 5,
    'dimensions': 5,
}
CANON_DIMENSIONS_EN = {
    'Human-Centered', 'Human centered', 'Human-Centered',
    'Fairness & Inclusiveness', 'Fairness&inclusive',
    'Safety & Reliability', 'Safety',
    'Trustworthiness & Controllability', 'Trustworthy',
    'Privacy Protection', 'Privacy',
}
TOOL_IDS = {f'T{i:02d}' for i in range(1, 15)}
RUBRIC_CODES = {f'R{i}' for i in range(1, 15)}

errors, warnings = [], []
def err(msg):  errors.append(msg)
def warn(msg): warnings.append(msg)

def load_csv(name):
    path = CODEBOOK / name
    if not path.exists():
        err(f"missing file: {path}")
        return []
    with open(path, encoding='utf-8') as f:
        return list(csv.DictReader(f))

def load_json(rel):
    path = DATA / rel
    if not path.exists():
        err(f"missing site data: {path}")
        return None
    return json.loads(path.read_text(encoding='utf-8'))

# ----------------------------------------------------------------------
# 1. Row counts
# ----------------------------------------------------------------------
benchmarks  = load_csv('benchmarks.csv')
tools       = load_csv('tools.csv')
sub_tools   = load_csv('sub_tools.csv')
rubrics     = load_csv('rubrics.csv')
policies    = load_csv('policies.csv')
mini_cases  = load_csv('mini_cases.csv')
matrix      = load_csv('rubric_tool_matrix.csv')
gap_detect  = load_csv('gap_detection.csv')

counts = {
    'benchmarks': len(benchmarks),
    'tools': len(tools),
    'rubrics': len(rubrics),
    'policies': len(policies),
    'sub_tools': len(sub_tools),
    'mini_cases': len(mini_cases),
}
for k, expected in EXPECT.items():
    if k == 'dimensions':
        continue
    if counts.get(k) != expected:
        err(f"{k}.csv has {counts.get(k)} rows, expected {expected}")

role_counts = {}
for row in sub_tools:
    role = (row.get('role') or '').strip()
    role_counts[role] = role_counts.get(role, 0) + 1
if role_counts.get('primary') != 103 or role_counts.get('secondary') != 103:
    err(f"sub_tools.csv role counts {role_counts}, expected primary=103 and secondary=103")

# ----------------------------------------------------------------------
# 2. ID uniqueness & controlled vocabularies
# ----------------------------------------------------------------------
tool_ids_seen = {t['tool_id'] for t in tools}
if tool_ids_seen != TOOL_IDS:
    err(f"tools.csv tool_id set != T01..T14: extra={tool_ids_seen - TOOL_IDS}  missing={TOOL_IDS - tool_ids_seen}")

rubric_codes_seen = {r['code'] for r in rubrics}
if rubric_codes_seen != RUBRIC_CODES:
    err(f"rubrics.csv code set != R1..R14: extra={rubric_codes_seen - RUBRIC_CODES}  missing={RUBRIC_CODES - rubric_codes_seen}")

bench_names = [b['benchmark'] for b in benchmarks]
if len(set(bench_names)) != len(bench_names):
    dups = [n for n in bench_names if bench_names.count(n) > 1]
    err(f"benchmarks.csv has duplicate names: {set(dups)}")

# ----------------------------------------------------------------------
# 3. Referential integrity — bench primary/secondary tool IDs resolve
# ----------------------------------------------------------------------
for b in benchmarks:
    for fld in ('primary_tool_id', 'secondary_tool_id'):
        tid = (b.get(fld) or '').strip()
        if tid and tid not in tool_ids_seen:
            err(f"benchmarks.csv[{b['benchmark']}] {fld}={tid!r} not in tools.csv")

# ----------------------------------------------------------------------
# 4. Dimensions controlled vocabulary
# ----------------------------------------------------------------------
for b in benchmarks:
    dim = (b.get('dimension_en') or '').strip()
    if dim and not any(dim.startswith(d.split(' &')[0].split('-')[0]) for d in CANON_DIMENSIONS_EN):
        warn(f"benchmarks.csv[{b['benchmark']}] dimension_en={dim!r} not in canonical set")

# ----------------------------------------------------------------------
# 5. Paper URL coverage
# ----------------------------------------------------------------------
empty_paper = [b['benchmark'] for b in benchmarks if not (b.get('paper_url') or '').strip()]
if empty_paper:
    warn(f"{len(empty_paper)} benchmarks have empty paper_url: e.g. {empty_paper[:3]}")
empty_code = [b['benchmark'] for b in benchmarks if not (b.get('code_url') or '').strip()]
if empty_code:
    warn(f"{len(empty_code)} benchmarks have empty code_url (acceptable for never-released artefacts)")

# ----------------------------------------------------------------------
# 6. Rubric-tool matrix shape
# ----------------------------------------------------------------------
if matrix:
    if len(matrix) != 14:
        err(f"rubric_tool_matrix.csv has {len(matrix)} rows, expected 14")
    expected_cols = {'rubric'} | TOOL_IDS
    actual_cols = set(matrix[0].keys())
    if actual_cols != expected_cols:
        err(f"rubric_tool_matrix.csv columns mismatch: extra={actual_cols-expected_cols} missing={expected_cols-actual_cols}")

# ----------------------------------------------------------------------
# 7. Markdown link contamination in CSV cells
# ----------------------------------------------------------------------
md_link_re = re.compile(r'\[[^\]]+\]\([^)]+\)')
for src_name, src_rows in [('benchmarks', benchmarks), ('tools', tools), ('rubrics', rubrics), ('policies', policies)]:
    for row in src_rows:
        for k, v in row.items():
            if isinstance(v, str) and md_link_re.search(v):
                warn(f"{src_name}.csv[{row.get('benchmark') or row.get('tool_id') or row.get('code') or '?'}] {k}: markdown link in CSV cell")
                break

# ----------------------------------------------------------------------
# 8. Site/codebook drift — paper URLs match bench_urls.json
# ----------------------------------------------------------------------
bench_urls = load_json('bench_urls.json') or {}
bench_map = load_json('bench_map.json') or []
bench_map_names = {b.get('Benchmark / Source', '').strip() for b in bench_map if b.get('Benchmark / Source')}
bench_url_names = set(bench_urls)
if bench_map_names and bench_url_names != bench_map_names:
    err("bench_urls.json keys do not match bench_map.json Benchmark / Source names: "
        f"extra={sorted(bench_url_names - bench_map_names)[:10]} "
        f"missing={sorted(bench_map_names - bench_url_names)[:10]}")
for b in benchmarks:
    name = b['benchmark']
    site_entry = bench_urls.get(name) or {}
    site_paper = (site_entry.get('paper') or '').strip()
    csv_paper = (b.get('paper_url') or '').strip()
    if site_paper and csv_paper and site_paper != csv_paper:
        warn(f"paper_url drift: {name!r}\n    csv:  {csv_paper}\n    site: {site_paper}")

# ----------------------------------------------------------------------
# 9. Common typo guard
# ----------------------------------------------------------------------
typos = ['narmative', 'strated', 'qeustion', 'toxity', 'benchmak', 'adaptative']
typo_re = re.compile(r'\b(' + '|'.join(typos) + r')\b', re.I)
for name, rows in [('benchmarks', benchmarks), ('tools', tools), ('rubrics', rubrics), ('policies', policies)]:
    for row in rows:
        for k, v in row.items():
            if isinstance(v, str) and typo_re.search(v):
                m = typo_re.search(v)
                warn(f"typo in {name}.csv {k}: {m.group(0)!r}")
                break

# ----------------------------------------------------------------------
# Report
# ----------------------------------------------------------------------
print("HEART codebook validation")
print("=" * 50)
print(f"benchmarks:        {counts['benchmarks']:>3}   (expect 103)")
print(f"tools:             {counts['tools']:>3}   (expect 14)")
print(f"rubrics:           {counts['rubrics']:>3}   (expect 14)")
print(f"policies:          {counts['policies']:>3}   (expect 16)")
print(f"sub_tools:         {counts['sub_tools']:>3}   (expect 206 = 103 primary + 103 secondary role rows)")
print(f"mini_cases:        {counts['mini_cases']:>3}   (expect 5)")
print()
if errors:
    print(f"ERRORS ({len(errors)}):")
    for e in errors: print(f"  ✗ {e}")
if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings[:20]: print(f"  ! {w}")
    if len(warnings) > 20:
        print(f"  ... {len(warnings) - 20} more warnings")
print()
if errors:
    print(f"FAIL — {len(errors)} error(s), {len(warnings)} warning(s)")
    sys.exit(1)
else:
    print(f"PASS — 103 benchmarks, 16 policy sources, 14 tools, 14 rubrics ({len(warnings)} warning(s))")
    sys.exit(0)
