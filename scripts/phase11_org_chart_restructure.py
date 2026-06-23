#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 11: Org Chart Restructure
Reshapes hr.department into: ES/CEO -> OES -> (Units | 5 Departments) -> Divisions
Colour-codes by hierarchy level and adjusts affected hr.job / hr.employee records.
Run: python3 scripts/phase11_org_chart_restructure.py
"""

import xmlrpc.client, sys

URL, DB, PW = 'http://localhost:8071', 'NADF', 'admin'
uid = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common').authenticate(DB, 'admin', PW, {})
if not uid:
    print("ERROR: Auth failed"); sys.exit(1)
m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, PW, model, method, args, kw or {})

COMPANY_ID = 1

# Colour levels per spec
C_ESCEO   = 0   # Level 1 - ES/CEO
C_OES     = 1   # Level 2 - OES + Units
C_UNIT    = 3   # Level 3 - Units sub-items
C_DEPT    = 5   # Level 4 - the 5 Departments
C_DIV     = 9   # Level 5 - Divisions

def get_or_create_dept(name, parent_id, color):
    existing = x('hr.department', 'search', [[['name', '=', name], ['parent_id', '=', parent_id]]])
    if existing:
        x('hr.department', 'write', [[existing[0]], {'color': color}])
        return existing[0]
    did = x('hr.department', 'create', [{
        'name': name, 'parent_id': parent_id, 'color': color, 'company_id': COMPANY_ID,
    }])
    print(f"  Created dept: {name} (id={did}, parent={parent_id})")
    return did

print("=" * 60)
print("  NADF ERP — Phase 11 Org Chart Restructure")
print("=" * 60)

# ── Level 1: ES/CEO (rename Executive Office, id=2) ────────────────────────────
print("\n[1] Level 1 — ES/CEO")
x('hr.department', 'write', [[2], {'name': 'ES/CEO', 'color': C_ESCEO}])

# ── Level 2: OES + Units grouping ───────────────────────────────────────────────
print("\n[2] Level 2 — OES, Units")
oes_id = get_or_create_dept('OES', 2, C_OES)
units_id = get_or_create_dept('Units', oes_id, C_OES)

# ── Level 3: Units children ─────────────────────────────────────────────────────
print("\n[3] Level 3 — Units children (Legal, Audit, Procurement, Strategy & MEL, Sustainability)")
x('hr.department', 'write', [[10], {'parent_id': units_id, 'color': C_UNIT}])  # Legal
x('hr.department', 'write', [[4],  {'parent_id': units_id, 'color': C_UNIT}])  # Procurement
audit_id    = get_or_create_dept('Audit', units_id, C_UNIT)
strategy_id = get_or_create_dept('Strategy & MEL', units_id, C_UNIT)
sustain_id  = get_or_create_dept('Sustainability (ESG & CF)', units_id, C_UNIT)

# ── Level 4: Partnerships & Investor Relations Department ──────────────────────
print("\n[4] Level 4 — Partnerships & Investor Relations Department")
x('hr.department', 'write', [[7], {
    'name': 'Partnerships & Investor Relations Department', 'parent_id': oes_id, 'color': C_DEPT,
}])
for div in ['Policy + Advocacy', 'Strategic + Knowledge', 'Implementation', 'Financial']:
    get_or_create_dept(div, 7, C_DIV)

# ── Level 4: Technical Department ───────────────────────────────────────────────
print("\n[5] Level 4 — Technical Department")
tech_id = get_or_create_dept('Technical Department', oes_id, C_DEPT)
for div in ['Inputs', 'Mechanisation', 'Emergency Support']:
    get_or_create_dept(div, tech_id, C_DIV)
x('hr.department', 'write', [[11], {'parent_id': tech_id, 'color': C_DIV}])  # Infrastructure

# ── Level 4: Investment Management Department ──────────────────────────────────
print("\n[6] Level 4 — Investment Management Department")
x('hr.department', 'write', [[6], {
    'name': 'Investment Management Department', 'parent_id': oes_id, 'color': C_DEPT,
}])
for div in ['Debt', 'Equity', 'Grant']:
    get_or_create_dept(div, 6, C_DIV)

# ── Level 4: Corporate Services Department ──────────────────────────────────────
print("\n[7] Level 4 — Corporate Services Department")
x('hr.department', 'write', [[8], {
    'name': 'Corporate Services Department', 'parent_id': oes_id, 'color': C_DEPT,
}])
x('hr.department', 'write', [[1], {'name': 'Admin', 'color': C_DIV}])  # Administration -> Admin
x('hr.department', 'write', [[5], {'name': 'HR', 'color': C_DIV}])     # Human Resources -> HR
x('hr.department', 'write', [[12], {'color': C_DIV}])  # ICT
x('hr.department', 'write', [[9], {'color': C_DIV}])   # Communications

# ── Level 4: Finance & Accounts Department ───────────────────────────────────────
print("\n[8] Level 4 — Finance & Accounts Department")
x('hr.department', 'write', [[3], {
    'name': 'Finance & Accounts Department', 'parent_id': oes_id, 'color': C_DEPT,
}])
for div in ['Accounts', 'Treasury', 'Budget']:
    get_or_create_dept(div, 3, C_DIV)

# ── hr.job adjustments ────────────────────────────────────────────────────────
print("\n[9] hr.job adjustments")
x('hr.job', 'write', [[22], {'name': 'Exec. Assistant', 'department_id': oes_id}])  # was "PA to ES"
x('hr.job', 'write', [[20], {'department_id': strategy_id}])  # Head of Strategy -> Strategy & MEL
x('hr.job', 'write', [[14], {'department_id': 6}])             # Head of Investments -> Investment Mgmt Dept
x('hr.job', 'write', [[2],  {'active': False}])                # archive unused "Director Corporate Services"
print("  Updated: Exec. Assistant, Head of Strategy, Head of Investments; archived Director Corporate Services")

for title, recruit in [('Policy Adviser', 1), ('SAS (1&2)', 2), ('Technical Assistant', 1)]:
    existing = x('hr.job', 'search', [[['name', '=', title], ['department_id', '=', oes_id]]])
    if existing:
        print(f"  SKIP (exists): {title}")
        continue
    x('hr.job', 'create', [{
        'name': title, 'department_id': oes_id, 'company_id': COMPANY_ID, 'no_of_recruitment': recruit,
    }])
    print(f"  Created job: {title} (OES)")

# ── hr.employee reassignments ────────────────────────────────────────────────
print("\n[10] hr.employee reassignments")
x('hr.employee', 'write', [[4], {'department_id': strategy_id}])  # Adebanke Fajana -> Strategy & MEL
x('hr.employee', 'write', [[31], {'department_id': oes_id}])      # Daniella Daniel -> OES
print("  Adebanke Fajana -> Strategy & MEL")
print("  Daniella Daniel -> OES")

print("\n" + "=" * 60)
print("  Phase 11 Org Chart Restructure — COMPLETE")
print("=" * 60)
