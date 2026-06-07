#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 8a: Asset Categories
Creates accounting asset categories (om_account_asset) and
physical equipment categories (maintenance) mapped to NADF COA.
"""
import xmlrpc.client, sys

URL, DB, PW = 'http://localhost:8071', 'NADF', 'admin'
uid = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common').authenticate(DB, 'admin', PW, {})
if not uid: print("ERROR: Auth failed"); sys.exit(1)
m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, PW, model, method, args, kw or {})

def acc(code):
    ids = x('account.account', 'search', [[['code','=',code],['deprecated','=',False]]])
    return ids[0] if ids else None

def find_or_create(model, domain, vals):
    ids = x(model, 'search', [domain])
    if ids:
        return ids[0], False
    return x(model, 'create', [vals]), True

print("=" * 60)
print("  Phase 8a — Asset Categories")
print("=" * 60)

misc_j = x('account.journal', 'search', [[['code','=','MISC']]])[0]

# ── Accounting Asset Categories (om_account_asset) ───────────────────────────
print("\n[1] Accounting asset categories (om_account_asset)...")

# Category: (name, asset_32x, accum_dep_44x, dep_exp_24x, months)
ACCT_CATS = [
    ('IT Equipment',
     acc('32010501'),   # COMPUTERS (balance sheet)
     acc('44010501'),   # PROV. FOR DEP-COMPUTERS
     acc('24010501'),   # DEPRECIATION CHARGES - COMPUTERS
     60),              # 5 years
    ('Office Furniture & Fittings',
     acc('32010602'),   # TABLES (general furniture balance sheet)
     acc('44010602'),   # PROV. FOR DEP-TABLES
     acc('24010602'),   # DEPRECIATION CHARGES - TABLES
     120),             # 10 years
    ('Motor Vehicles',
     acc('32010301'),   # EARTH MOVING EQUIPMENT (closest non-current asset for vehicles)
     acc('44010305'),   # PROV. FOR DEP-POWER GENERATING SETS (best available)
     acc('24010305'),   # DEPRECIATION CHARGES - POWER GENERATING SETS
     60),              # 5 years
    ('A/C & Power Equipment',
     acc('32010305'),   # POWER GENERATING SETS
     acc('44010305'),   # PROV. FOR DEP-POWER GENERATING SETS
     acc('24010305'),   # DEPRECIATION CHARGES - POWER GENERATING SETS
     120),             # 10 years
    ('Office Appliances',
     acc('32010610'),   # REFRIDGERATORS (general appliances proxy)
     acc('44010610'),   # PROV. FOR DEP-REFRIDGERATORS
     acc('24010610'),   # DEPRECIATION CHARGES - REFRIGERATORS
     60),              # 5 years
]

for name, asset_id, dep_id, exp_id, months in ACCT_CATS:
    if not all([asset_id, dep_id, exp_id]):
        print(f"  SKIP {name} — missing account IDs")
        continue
    cat_id, created = find_or_create('account.asset.category',
        [['name','=',name]],
        {
            'name':                         name,
            'account_asset_id':             asset_id,
            'account_depreciation_id':      dep_id,
            'account_depreciation_expense_id': exp_id,
            'journal_id':                   misc_j,
            'method':                       'linear',
            'method_time':                  'number',
            'method_number':                months,
            'method_period':                1,
            'type':                         'purchase',
        })
    status = 'Created' if created else 'Exists'
    print(f"  {status}: {name} (id={cat_id}, {months} months)")

# ── Physical Equipment Categories (maintenance) ───────────────────────────────
print("\n[2] Maintenance equipment categories...")

MAINT_CATS = [
    'IT Equipment',
    'Office Furniture & Fittings',
    'A/C & Power Equipment',
    'Office Appliances',
    'ICT Infrastructure',
]
for name in MAINT_CATS:
    cat_id, created = find_or_create('maintenance.equipment.category',
        [['name','=',name]], {'name': name})
    print(f"  {'Created' if created else 'Exists'}: {name} (id={cat_id})")

print("\n  Done — asset categories ready.")
