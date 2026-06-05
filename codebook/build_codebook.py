"""Rebuild the HEART codebook artifacts (CSVs + xlsx) from the website's
canonical JSON data in docs/interactive/data/.

Outputs (all written into codebook/):
  benchmarks.csv        — 103 audited benchmarks (full rubric scores + EN/ZH labels)
  tools.csv             — 14 generic repair tools (T01–T14, EN/ZH)
  sub_tools.csv         — 103 specific repair sub-tools (one per audited bench), EN/ZH
  rubrics.csv           — 14 calibrated rubrics (anchors + score distribution + key question), EN/ZH
  policies.csv          — 16 policy / governance sources × 5 dimension support codes
  mini_cases.csv        — 5 mini cases (id, dimension, title, source dataset)
  rubric_tool_matrix.csv — 14 × 14 evidence-score matrix
  gap_detection.csv     — 14 rubrics × typical symptoms / red flags / evidence-to-inspect
  heart_codebook.xlsx   — bundle of all CSVs as a multi-sheet workbook

Run from the repo root after editing site data:
  python3 codebook/build_codebook.py
"""
import csv, json, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'docs' / 'interactive' / 'data'
OUT = ROOT / 'codebook'
OUT.mkdir(exist_ok=True)

def load(name):
    with open(DATA / name) as f:
        return json.load(f)

def write_csv(name, rows, fieldnames):
    path = OUT / name
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"  ✓ {name} ({len(rows)} rows)")

def main():
    bench_map = load('bench_map.json')
    t_tools = load('t_tools.json')
    rubrics_full = load('rubrics_full.json')
    dimensions = load('dimensions.json')
    mini_cases = load('mini_cases.json')
    bench_urls = load('bench_urls.json')
    matrix = load('matrix.json')
    gap_detection = load('gap_detection.json')

    rubric_codes_in_order = [r['code'] for r in rubrics_full]
    rubric_names = [r['name'] for r in rubrics_full]
    tool_ids = [t['Tool ID'] for t in t_tools]

    print(f"Source data: {len(bench_map)} benches, {len(t_tools)} tools, "
          f"{len(rubrics_full)} rubrics, {len(dimensions['policies'])} policies, "
          f"{len(mini_cases)} mini cases")

    # ---------- benchmarks.csv ----------
    # The audit unit is (benchmark × primary_dimension): a benchmark scored
    # under two dimensions appears as two rows.  Disambiguate the few
    # repeating names by suffixing the dimension short-code in the
    # `benchmark` column so it stays a primary key.
    name_counts = {}
    for b in bench_map:
        n = b.get('Benchmark / Source', '')
        name_counts[n] = name_counts.get(n, 0) + 1
    dim_short = {
        'Human centered': 'HC', 'Human-Centered': 'HC',
        'Fairness&inclusive': 'F', 'Fairness & Inclusiveness': 'F',
        'Safety': 'S', 'Safety & Reliability': 'S',
        'Trustworthy': 'T', 'Trustworthiness & Controllability': 'T',
        'Privacy': 'P', 'Privacy Protection': 'P',
    }
    bench_rows = []
    for b in bench_map:
        name = b.get('Benchmark / Source', '')
        dim_raw = (b.get('一级标签') or '').strip()
        if name_counts.get(name, 0) > 1:
            suffix = dim_short.get(dim_raw, dim_raw[:2].upper())
            name = f'{name} [{suffix}]'
        urls = bench_urls.get(b.get('Benchmark / Source', '')) or bench_urls.get((b.get('Benchmark / Source','')).split(' (')[0]) or {}
        row = {
            'benchmark': name,
            'dimension_en': b.get('一级标签_en', '') or b.get('一级标签', ''),
            'dimension_zh': b.get('一级标签_zh', '') or b.get('一级标签', ''),
            'expert_tag_en': b.get('专家标签_en', '') or b.get('专家标签', ''),
            'expert_tag_zh': b.get('专家标签', ''),
            'paper_url': urls.get('paper', ''),
            'code_url': urls.get('code', ''),
            'primary_tool_id': b.get('主整合工具ID', ''),
            'primary_tool_en': b.get('主整合工具', ''),
            'primary_tool_zh': b.get('主整合工具_zh', ''),
            'primary_subtool_en': b.get('主细分工具_en', '') or b.get('主细分工具', ''),
            'primary_subtool_zh': b.get('主细分工具_zh', '') or b.get('主细分工具', ''),
            'secondary_tool_id': b.get('次整合工具ID', ''),
            'secondary_tool_en': b.get('次整合工具', ''),
            'secondary_tool_zh': b.get('次整合工具_zh', ''),
            'secondary_subtool_en': b.get('次细分工具_en', '') or b.get('次细分工具', ''),
            'secondary_subtool_zh': b.get('次细分工具_zh', '') or b.get('次细分工具', ''),
            'rubrics_improved': b.get('索引用rubrics（精简口径）', ''),
            'adaptation_prompt_en': b.get('改编Prompt指导_en', '') or b.get('改编Prompt指导', ''),
            'adaptation_prompt_zh': b.get('改编Prompt指导', ''),
            'adaptation_example_en': b.get('改编示例（微改）_en', '') or b.get('改编示例（微改）', ''),
            'adaptation_example_zh': b.get('改编示例（微改）', ''),
        }
        bench_rows.append(row)
    write_csv('benchmarks.csv', bench_rows, list(bench_rows[0].keys()))

    # ---------- tools.csv (14 generic repair tools) ----------
    tool_rows = []
    for t in t_tools:
        row = {
            'tool_id': t.get('Tool ID', ''),
            'name_en': t.get('Toolbox 英文名', ''),
            'name_zh': t.get('中文译名', ''),
            'layer': t.get('rubric_layer', ''),
            'category_en': t.get('所属类别_en', '') or t.get('所属类别', ''),
            'category_zh': t.get('所属类别', ''),
            'core_practice_en': t.get('核心做法_en', '') or t.get('核心做法', ''),
            'core_practice_zh': t.get('核心做法', ''),
            'problem_fixed_en': t.get('解决的 benchmark 问题_en', '') or t.get('解决的 benchmark 问题', ''),
            'problem_fixed_zh': t.get('解决的 benchmark 问题', ''),
            'core_rubrics_lifted': t.get('核心提升rubrics（精简）', ''),
            'applicable_scope_en': t.get('适用伦理场景_en', '') or t.get('适用伦理场景', ''),
            'applicable_scope_zh': t.get('适用伦理场景', ''),
            'boundary_vs_neighbors_en': t.get('工具边界 / 与相近工具区别_en', '') or t.get('工具边界 / 与相近工具区别', ''),
            'boundary_vs_neighbors_zh': t.get('工具边界 / 与相近工具区别', ''),
            'evidence_count': t.get('证据条数', ''),
            'primary_match_count': t.get('主匹配条数', ''),
            'automatable_en': t.get('自动化可做部分_en', '') or t.get('自动化可做部分', ''),
            'automatable_zh': t.get('自动化可做部分', ''),
            'needs_human_en': t.get('需人工校验/治理部分_en', '') or t.get('需人工校验/治理部分', ''),
            'needs_human_zh': t.get('需人工校验/治理部分', ''),
            'limitations_en': t.get('局限 / 避免过度声称_en', '') or t.get('局限 / 避免过度声称', ''),
            'limitations_zh': t.get('局限 / 避免过度声称', ''),
        }
        tool_rows.append(row)
    write_csv('tools.csv', tool_rows, list(tool_rows[0].keys()))

    # ---------- sub_tools.csv (103 specific repair sub-tools) ----------
    sub_rows = []
    for b in bench_map:
        for role, id_key, name_key, en_key, zh_key in [
            ('primary', '主整合工具ID', '主整合工具', '主细分工具_en', '主细分工具_zh'),
            ('secondary', '次整合工具ID', '次整合工具', '次细分工具_en', '次细分工具_zh'),
        ]:
            if not b.get(id_key): continue
            sub_rows.append({
                'role': role,
                'benchmark': b.get('Benchmark / Source', ''),
                'parent_tool_id': b.get(id_key, ''),
                'parent_tool_en': b.get(name_key, ''),
                'parent_tool_zh': b.get(name_key.replace('工具', '工具_zh'), '') or b.get(name_key + '_zh', ''),
                'subtool_name_en': b.get(en_key, '') or b.get(en_key.replace('_en',''), ''),
                'subtool_name_zh': b.get(zh_key, '') or b.get(zh_key.replace('_zh',''), ''),
            })
    write_csv('sub_tools.csv', sub_rows, list(sub_rows[0].keys()))

    # ---------- rubrics.csv (14 rubrics, full calibration) ----------
    rubric_rows = []
    for r in rubrics_full:
        cnts = r.get('counts', {})
        total = r.get('total', 0)
        dist = ';'.join(f"{s}={cnts.get(str(s), cnts.get(s, 0))}" for s in range(6))
        row = {
            'code': r.get('code', ''),
            'layer': r.get('layer', ''),
            'name_en': r.get('name', ''),
            'name_zh': r.get('name_zh', ''),
            'key_question_en': r.get('key_question_en', '') or r.get('key_question', ''),
            'key_question_zh': r.get('key_question', ''),
            'anchor_0_en': r.get('anchor_0_en', '') or r.get('anchor_0', ''),
            'anchor_0_zh': r.get('anchor_0', ''),
            'anchor_1_2_en': r.get('anchor_1_2_en', '') or r.get('anchor_1_2', ''),
            'anchor_1_2_zh': r.get('anchor_1_2', ''),
            'anchor_3_4_en': r.get('anchor_3_4_en', '') or r.get('anchor_3_4', ''),
            'anchor_3_4_zh': r.get('anchor_3_4', ''),
            'anchor_5_en': r.get('anchor_5_en', '') or r.get('anchor_5', ''),
            'anchor_5_zh': r.get('anchor_5', ''),
            'calibrated_anchors_en': r.get('calibrated_anchors_en', '') or r.get('calibrated_anchors', ''),
            'calibrated_anchors_zh': r.get('calibrated_anchors', ''),
            'revision_notes_en': r.get('revision_notes_en', '') or r.get('revision_notes', ''),
            'revision_notes_zh': r.get('revision_notes', ''),
            'total_audited': total,
            'score_distribution': dist,
            'mean': round(r.get('mean', 0), 3),
        }
        rubric_rows.append(row)
    write_csv('rubrics.csv', rubric_rows, list(rubric_rows[0].keys()))

    # ---------- policies.csv (16 policy / governance sources) ----------
    pol_rows = []
    dim_order = ['Human-Centered', 'Fairness & Inclusiveness', 'Safety & Reliability',
                 'Trustworthiness & Controllability', 'Privacy Protection']
    for p in dimensions['policies']:
        row = {
            'source': p.get('source', ''),
            'type': p.get('type', ''),
            'url': dimensions['policy_links'].get(p['source'], ''),
        }
        for d in dim_order:
            row[f'support_{d.replace(" & ", "_").replace(" ", "_")}'] = p.get('cells', {}).get(d, '')
        pol_rows.append(row)
    write_csv('policies.csv', pol_rows, list(pol_rows[0].keys()))

    # ---------- mini_cases.csv ----------
    mc_rows = []
    for c in mini_cases:
        mc_rows.append({
            'id': c.get('id', ''),
            'dimension_en': c.get('dimension', ''),
            'dimension_zh': c.get('dim_zh', ''),
            'title_en': c.get('title_en', ''),
            'title_zh': c.get('title_zh', ''),
            'source_dataset': c.get('source_dataset', ''),
            'source_dataset_url': c.get('source_dataset_url', ''),
            'source_entry': c.get('source_entry', ''),
            'rubrics_lifted_en': '; '.join(c.get('rubrics_lifted', [])),
            'rubrics_lifted_zh': '; '.join(c.get('rubrics_lifted_zh', [])),
            'tools_applied': '; '.join(t.get('id','') for t in c.get('tools_applied', [])),
            'why_improved_en': c.get('why_improved_en', ''),
            'why_improved_zh': c.get('why_improved_zh', ''),
        })
    write_csv('mini_cases.csv', mc_rows, list(mc_rows[0].keys()))

    # ---------- rubric_tool_matrix.csv (14 rubrics × 14 tools) ----------
    mtx_rows = []
    for r_name in rubric_names:
        row = {'rubric': r_name}
        for tid in tool_ids:
            m = next((x for x in matrix['rows'] if x['Tool ID'] == tid), None)
            row[tid] = (m or {}).get(r_name, '')
        mtx_rows.append(row)
    write_csv('rubric_tool_matrix.csv', mtx_rows, ['rubric'] + tool_ids)

    # ---------- gap_detection.csv ----------
    gap_rows = []
    for code, e in gap_detection.items():
        domain_symptoms_en = e.get('domain_symptoms_en') or {}
        domain_symptoms_zh = e.get('domain_symptoms') or {}
        gap_rows.append({
            'code': code,
            'name_en': e.get('name_en', ''),
            'name_zh': e.get('name_zh', ''),
            'typical_symptoms_en': e.get('typical_symptoms_en', ''),
            'typical_symptoms_zh': e.get('typical_symptoms_zh', ''),
            'red_flags_en': '; '.join(e.get('red_flags_en', []) or []),
            'red_flags_zh': '; '.join(e.get('red_flags_zh', []) or []),
            'evidence_to_inspect': '; '.join(e.get('evidence_to_inspect', []) or []),
            'diagnostic_questions_en': '; '.join(e.get('diagnostic_questions_en', []) or []),
            'diagnostic_questions_zh': '; '.join(e.get('diagnostic_questions_zh', []) or []),
            'domain_symptoms_en_json': json.dumps(domain_symptoms_en, ensure_ascii=False),
            'domain_symptoms_zh_json': json.dumps(domain_symptoms_zh, ensure_ascii=False),
            'common_misdiagnosis_en': e.get('common_misdiagnosis_en', ''),
            'common_misdiagnosis_zh': e.get('common_misdiagnosis_zh', ''),
            'default_tools': '; '.join(e.get('default_tools_web14', []) or []),
        })
    write_csv('gap_detection.csv', gap_rows, list(gap_rows[0].keys()))

    # ---------- heart_codebook.xlsx ----------
    try:
        import openpyxl
    except ImportError:
        print("openpyxl missing — skipping xlsx bundle. Install with `pip install openpyxl` to enable.")
        return
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    sheets = [
        ('benchmarks', 'benchmarks.csv'),
        ('tools', 'tools.csv'),
        ('sub_tools', 'sub_tools.csv'),
        ('rubrics', 'rubrics.csv'),
        ('policies', 'policies.csv'),
        ('mini_cases', 'mini_cases.csv'),
        ('rubric_tool_matrix', 'rubric_tool_matrix.csv'),
        ('gap_detection', 'gap_detection.csv'),
    ]
    for sheet_name, csv_name in sheets:
        ws = wb.create_sheet(sheet_name)
        with open(OUT / csv_name, encoding='utf-8') as f:
            for row in csv.reader(f):
                ws.append(row)
    out_xlsx = OUT / 'heart_codebook.xlsx'
    wb.save(out_xlsx)
    print(f"  ✓ heart_codebook.xlsx ({len(sheets)} sheets)")

if __name__ == '__main__':
    main()
