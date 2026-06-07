#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 8d: ICT Help Desk (Project workaround)
Creates an "ICT Help Desk" project with stages and fault-category tags,
then imports all 77 historical tickets from the ICT Issue Log Tracker.
"""
import xmlrpc.client, zipfile, xml.etree.ElementTree as ET, sys
from datetime import datetime, timedelta

URL, DB, PW = 'http://localhost:8071', 'NADF', 'admin'
EXCEL = '/Users/mac/Documents/Aliyu/NADF/Digital Transformation/Client Data/NADF ICT Issue Log Tracker.xlsx'

uid = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common').authenticate(DB, 'admin', PW, {})
if not uid: print("ERROR: Auth failed"); sys.exit(1)
m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, PW, model, method, args, kw or {})

def find_or_create(model, domain, vals):
    ids = x(model, 'search', [domain])
    return (ids[0], False) if ids else (x(model, 'create', [vals]), True)

def excel_date(s):
    try:
        n = float(s)
        if n > 40000:
            return (datetime(1899,12,30) + timedelta(days=n)).strftime('%Y-%m-%d')
    except: pass
    return None

print("=" * 60)
print("  Phase 8d — ICT Help Desk Project")
print("=" * 60)

# ── Create project ────────────────────────────────────────────────────────────
proj_id, created = find_or_create('project.project',
    [['name','=','ICT Help Desk']],
    {'name': 'ICT Help Desk', 'description': 'NADF ICT Department — Help Desk & Issue Tracker'})
print(f"\n  {'Created' if created else 'Exists'}: ICT Help Desk project (id={proj_id})")

# ── Stages ────────────────────────────────────────────────────────────────────
STAGES = [
    ('New',         False),
    ('Assigned',    False),
    ('In Progress', False),
    ('On Hold',     False),
    ('Resolved',    False),
    ('Closed',      True),   # fold = True in kanban
]
stage_ids = {}
print("\n  Stages:")
for seq, (name, fold) in enumerate(STAGES, start=1):
    sid, created_s = find_or_create('project.task.type',
        [['name','=',name], ['project_ids','in',[proj_id]]],
        {'name': name, 'sequence': seq * 10, 'project_ids': [(4, proj_id)]})
    # Ensure stage is linked to this project
    x('project.task.type', 'write', [[sid], {'project_ids': [(4, proj_id)]}])
    stage_ids[name] = sid
    print(f"    {'Created' if created_s else 'Exists'}: {name} (id={sid})")

# ── Fault category tags ───────────────────────────────────────────────────────
FAULT_CATS = {
    '101': 'Hardware Faults',
    '102': 'Software/Application Faults',
    '103': 'Network Faults',
    '104': 'Security Faults',
    '105': 'Performance-Related Faults',
    '106': 'Access and Identity Faults',
    '107': 'Data and Database Faults',
    '108': 'Environmental & Infrastructure Faults',
    '109': 'Process or Configuration Faults',
    '110': 'Service Outage',
}
tag_ids = {}
print("\n  Tags:")
for code, label in FAULT_CATS.items():
    full = f"[{code}] {label}"
    tid, created_t = find_or_create('project.tags', [['name','=',full]], {'name': full})
    tag_ids[code] = tid
    print(f"    {'Created' if created_t else 'Exists'}: {full}")

# ── Read Excel ────────────────────────────────────────────────────────────────
print("\n  Reading ICT Issue Log...")
with zipfile.ZipFile(EXCEL) as z:
    strings = []
    if 'xl/sharedStrings.xml' in z.namelist():
        ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
        for si in ET.parse(z.open('xl/sharedStrings.xml')).getroot().iter(f'{ns}si'):
            strings.append(''.join(n.text or '' for n in si.iter(f'{ns}t')))
    sf = sorted([n for n in z.namelist() if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')])[0]
    ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    all_rows = []
    for row in ET.parse(z.open(sf)).getroot().iter(f'{ns}row'):
        cells = []
        for c in row.iter(f'{ns}c'):
            t, v = c.get('t',''), c.find(f'{ns}v')
            val = v.text if v is not None else ''
            if t == 's' and val:
                try: val = strings[int(val)]
                except: pass
            cells.append(str(val).strip())
        all_rows.append(cells)

# Tickets start at row index 17 (0-based)
tickets = []
for row in all_rows[17:]:
    if not row or not row[0].strip() or not row[0].strip().isdigit():
        continue
    while len(row) < 18: row.append('')
    tickets.append({
        'no':          row[0],
        'fault_code':  row[1].strip(),
        'raised_by':   row[2].strip(),
        'department':  row[3].strip(),
        'ref':         row[4].strip(),
        'call_type':   row[5].strip(),
        'description': row[6].strip(),
        'priority':    row[7].strip().upper(),
        'opened_on':   row[8].strip(),
        'status':      row[15].strip().upper(),
        'resolution':  row[16].strip(),
    })

print(f"  {len(tickets)} tickets found")

# ── Import tickets as tasks ───────────────────────────────────────────────────
print("\n  Importing tickets as project tasks...")

def map_stage(status_str):
    if 'CLOSE' in status_str:  return stage_ids['Closed']
    if 'UNHOLD' in status_str or 'ON HOLD' in status_str: return stage_ids['On Hold']
    if 'OPEN' in status_str:   return stage_ids['New']
    if status_str == '':       return stage_ids['On Hold']  # no status = still open
    return stage_ids['Closed']

def map_priority(p):
    return '1' if p == 'HIGH' else '0'  # Odoo: '1'=urgent/high, '0'=normal

created_t = skipped_t = 0
for t in tickets:
    task_name = f"[{t['ref']}] {t['description'][:80]}"
    existing = x('project.task', 'search', [[['name','=',task_name],['project_id','=',proj_id]]])
    if existing:
        skipped_t += 1
        continue

    tag_list = []
    if t['fault_code'] and t['fault_code'] in tag_ids:
        tag_list = [(4, tag_ids[t['fault_code']])]

    stage = map_stage(t['status'])
    desc_html = (
        f"<p><b>Reference:</b> {t['ref']}<br/>"
        f"<b>Raised by:</b> {t['raised_by']} ({t['department']})<br/>"
        f"<b>Type:</b> {t['call_type']}<br/>"
        f"<b>Priority:</b> {t['priority']}</p>"
        f"<p><b>Description:</b> {t['description']}</p>"
        + (f"<p><b>Resolution:</b> {t['resolution']}</p>" if t['resolution'] else '')
    )

    x('project.task', 'create', [{
        'name':        task_name,
        'project_id':  proj_id,
        'stage_id':    stage,
        'priority':    map_priority(t['priority']),
        'tag_ids':     tag_list,
        'description': desc_html,
    }])
    created_t += 1

print(f"  Created: {created_t}  |  Skipped (exists): {skipped_t}")

# ── Toner inventory products ──────────────────────────────────────────────────
print("\n  Setting up toner inventory products...")

TONERS = [
    ('HP Toner 207A Color',  'HPCOLOR236', 8,  8),
    ('HP Toner 106A Black',  'HP133',       4,  4),
    ('HP Toner 415A Color',  'HPCOLOR480', 4,  4),
]

icto_cat_id = None
cats = x('product.category', 'search', [[['name','ilike','All']]])
if cats: icto_cat_id = cats[0]

for name, sku, qty_on_hand, reorder_qty in TONERS:
    existing = x('product.template', 'search', [[['default_code','=',sku]]])
    if existing:
        print(f"  EXISTS : {name} ({sku})")
        continue
    prod_id = x('product.template', 'create', [{
        'name':         name,
        'default_code': sku,
        'type':         'consu',   # consumable — tracks stock
        'categ_id':     icto_cat_id,
    }])
    print(f"  Created: {name} ({sku}) id={prod_id}")

total_tasks = x('project.task', 'search_count', [[['project_id','=',proj_id]]])
print(f"\n  ICT Help Desk: {total_tasks} tasks total")
print("  Done.")
