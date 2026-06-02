#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 1 Foundation Setup
Configures: company identity, fiscal year, demo users
Run: python3 scripts/phase1_foundation_setup.py
"""

import xmlrpc.client
import sys

# ── Connection ────────────────────────────────────────────────────────────────
URL = 'http://localhost:8071'
DB  = 'NADF'
ADMIN_USER = 'admin'
ADMIN_PASS = 'admin'

common = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common')
uid    = common.authenticate(DB, ADMIN_USER, ADMIN_PASS, {})
if not uid:
    print("ERROR: Authentication failed"); sys.exit(1)

m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def execute(model, method, args, kwargs=None):
    return m.execute_kw(DB, uid, ADMIN_PASS, model, method, args, kwargs or {})

print("=" * 60)
print("  NADF ERP MVP — Phase 1 Foundation Setup")
print("=" * 60)

# ── 1. Company Identity ───────────────────────────────────────────────────────
print("\n[1/3] Configuring company identity...")

execute('res.company', 'write', [[1], {
    'name':       'National Agricultural Development Fund',
    'street':     'Bank of Agriculture Building, Central Business District',
    'city':       'Abuja',
    'zip':        '900001',
    'country_id': 163,           # Nigeria
    'phone':      '+234 9 870 0000',
    'email':      'info@nadf.gov.ng',
    'website':    'https://www.nadf.gov.ng',
    'vat':        '',            # FIRS TIN — update with real value
}])

# Activate NGN currency (ensure it is active)
execute('res.currency', 'write', [[120], {'active': True}])
execute('res.company', 'write', [[1], {'currency_id': 120}])

co = execute('res.company', 'read', [[1]], {'fields': ['name','city','email','currency_id']})
print(f"  Company : {co[0]['name']}")
print(f"  City    : {co[0]['city']}")
print(f"  Email   : {co[0]['email']}")
print(f"  Currency: {co[0]['currency_id'][1]}")

# ── 2. Fiscal Year (Jan–Dec 2026) ─────────────────────────────────────────────
print("\n[2/3] Configuring fiscal year (January–December)...")

# Create 2026 fiscal year
fy_existing = execute('account.fiscal.year', 'search', [[['date_from','=','2026-01-01']]])
if not fy_existing:
    fy_id = execute('account.fiscal.year', 'create', [{
        'name':      'FY 2026 (Jan–Dec)',
        'date_from': '2026-01-01',
        'date_to':   '2026-12-31',
        'company_id': 1,
    }])
    print(f"  Created FY 2026 (ID: {fy_id})")
else:
    print(f"  FY 2026 already exists (ID: {fy_existing[0]})")

# Create 2027 fiscal year (forward planning)
fy27 = execute('account.fiscal.year', 'search', [[['date_from','=','2027-01-01']]])
if not fy27:
    fy27_id = execute('account.fiscal.year', 'create', [{
        'name':      'FY 2027 (Jan–Dec)',
        'date_from': '2027-01-01',
        'date_to':   '2027-12-31',
        'company_id': 1,
    }])
    print(f"  Created FY 2027 (ID: {fy27_id})")

# ── 3. Demo Users ─────────────────────────────────────────────────────────────
print("\n[3/3] Creating demo users...")

# Resolve group IDs
def gid(xml_id):
    parts = xml_id.split('.')
    rec = execute('ir.model.data', 'search_read',
                  [[['module','=',parts[0]],['name','=',parts[1]]]],
                  {'fields': ['res_id']})
    return rec[0]['res_id'] if rec else None

G_ACCOUNT_USER    = gid('account.group_account_user')
G_ACCOUNT_MANAGER = gid('account.group_account_manager')
G_PURCHASE_USER   = gid('purchase.group_purchase_user')
G_PURCHASE_MGR    = gid('purchase.group_purchase_manager')
G_HR_USER         = gid('hr.group_hr_user')
G_HR_MANAGER      = gid('hr.group_hr_manager')
G_INTERNAL        = gid('base.group_user')

DEMO_PASS = 'Nadf@2026'

users = [
    {
        'name':     'Finance Officer',
        'login':    'finance.officer',
        'email':    'finance.officer@nadf.gov.ng',
        'groups':   [G_INTERNAL, G_ACCOUNT_USER],
        'job_title':'Finance Officer',
    },
    {
        'name':     'Head Finance',
        'login':    'head.finance',
        'email':    'head.finance@nadf.gov.ng',
        'groups':   [G_INTERNAL, G_ACCOUNT_MANAGER],
        'job_title':'Head of Finance Unit',
    },
    {
        'name':     'Procurement Officer',
        'login':    'procurement.officer',
        'email':    'procurement.officer@nadf.gov.ng',
        'groups':   [G_INTERNAL, G_PURCHASE_USER],
        'job_title':'Procurement Officer',
    },
    {
        'name':     'Head Procurement',
        'login':    'head.procurement',
        'email':    'head.procurement@nadf.gov.ng',
        'groups':   [G_INTERNAL, G_PURCHASE_MGR],
        'job_title':'Head of Procurement Unit',
    },
    {
        'name':     'HR Officer',
        'login':    'hr.officer',
        'email':    'hr.officer@nadf.gov.ng',
        'groups':   [G_INTERNAL, G_HR_USER],
        'job_title':'HR Officer',
    },
    {
        'name':     'Head HR',
        'login':    'head.hr',
        'email':    'head.hr@nadf.gov.ng',
        'groups':   [G_INTERNAL, G_HR_MANAGER],
        'job_title':'Head of HR Unit',
    },
    {
        'name':     'Director Corporate Services',
        'login':    'director.cs',
        'email':    'director.cs@nadf.gov.ng',
        'groups':   [G_INTERNAL, G_ACCOUNT_MANAGER, G_PURCHASE_MGR, G_HR_MANAGER],
        'job_title':'Director Corporate Services',
    },
    {
        'name':     'Executive Secretary',
        'login':    'executive.secretary',
        'email':    'executive.secretary@nadf.gov.ng',
        'groups':   [G_INTERNAL, G_ACCOUNT_MANAGER, G_PURCHASE_MGR, G_HR_MANAGER],
        'job_title':'Executive Secretary',
    },
]

for u in users:
    existing = execute('res.users', 'search', [[['login','=',u['login']]]])
    if existing:
        print(f"  SKIP (exists): {u['name']}")
        continue

    groups_cmd = [(4, gid) for gid in u['groups'] if gid]
    user_id = execute('res.users', 'create', [{
        'name':            u['name'],
        'login':           u['login'],
        'email':           u['email'],
        'password':        DEMO_PASS,
        'job_title':       u['job_title'],
        'company_id':      1,
        'company_ids':     [(4, 1)],
        'groups_id':       groups_cmd,
        'notification_type': 'email',
        'share':           False,
    }])
    print(f"  Created: {u['name']:35s} | login: {u['login']}")

# ── Summary ───────────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  Phase 1 Foundation Setup — COMPLETE")
print("=" * 60)
all_users = execute('res.users', 'search_read',
    [[['share','=',False],['active','=',True]]],
    {'fields': ['name','login','job_title']})
print(f"\n  Internal users ({len(all_users)} total):")
for u in all_users:
    print(f"    {u['name']:35s} | {u['login']}")
print(f"\n  Demo password : {DEMO_PASS}")
print("  URL           : http://localhost:8071")
print("  Admin login   : admin / admin")
