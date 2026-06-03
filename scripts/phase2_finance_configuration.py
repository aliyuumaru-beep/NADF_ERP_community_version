#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 2 Finance Configuration
Configures: Chart of Accounts extensions, analytic accounts,
            payment terms cleanup, sample vendors, bank account
Run: python3 scripts/phase2_finance_configuration.py
"""

import xmlrpc.client, sys

URL, DB = 'http://localhost:8071', 'NADF'
ADMIN_PASS = 'admin'
uid = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common').authenticate(DB, 'admin', ADMIN_PASS, {})
if not uid:
    print("ERROR: Auth failed"); sys.exit(1)
m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, ADMIN_PASS, model, method, args, kw or {})

def ensure_account(code, name, account_type, tag_ids=None):
    existing = x('account.account', 'search', [[['code','=',code]]])
    if existing:
        print(f"  SKIP (exists) : {code} — {name}")
        return existing[0]
    vals = {'code': code, 'name': name, 'account_type': account_type, 'company_id': 1}
    if tag_ids:
        vals['tag_ids'] = tag_ids
    aid = x('account.account', 'create', [vals])
    print(f"  Created       : {code} — {name}")
    return aid

def ensure_analytic(name, code):
    existing = x('account.analytic.account', 'search', [[['name','=',name]]])
    if existing:
        print(f"  SKIP (exists) : {name}")
        return existing[0]
    aid = x('account.analytic.account', 'create', [{'name': name, 'code': code, 'company_id': 1}])
    print(f"  Created       : {name} ({code})")
    return aid

def ensure_vendor(name, ref, phone='', email=''):
    existing = x('res.partner', 'search', [[['name','=',name],['supplier_rank','>',0]]])
    if existing:
        print(f"  SKIP (exists) : {name}")
        return existing[0]
    pid = x('res.partner', 'create', [{
        'name':          name,
        'ref':           ref,
        'company_type':  'company',
        'supplier_rank': 1,
        'customer_rank': 0,
        'country_id':    163,
        'phone':         phone,
        'email':         email,
        'city':          'Abuja',
    }])
    print(f"  Created       : {name}")
    return pid

print("=" * 60)
print("  NADF ERP MVP — Phase 2 Finance Configuration")
print("=" * 60)

# ── 1. Chart of Accounts — NADF Extensions ───────────────────────────────────
print("\n[1/5] Extending Chart of Accounts for NADF...")

# Assets
ensure_account('120000', 'Staff & Programme Advances', 'asset_current')
ensure_account('120100', 'Travel Advances', 'asset_current')
ensure_account('120200', 'Programme Advances', 'asset_current')

# Liabilities
ensure_account('253000', 'Pension Payables (PENCOM)', 'liability_current')
ensure_account('253100', 'NHF Payables', 'liability_current')
ensure_account('254000', 'Withholding Tax Payable (Staff)', 'liability_current')

# Equity — Public Sector
ensure_account('311000', 'Accumulated Funds', 'equity')
ensure_account('312000', 'Grant Reserves', 'equity')

# Income — Public Sector
ensure_account('410000', 'Grant Income',         'income')
ensure_account('410100', 'Federal Government Grants', 'income')
ensure_account('410200', 'Donor Grants',          'income')
ensure_account('420000', 'Recoveries',            'income')
ensure_account('430000', 'Interest Income',       'income_other')

# Expenses — NADF-Specific
ensure_account('631000', 'Training & Capacity Building', 'expense')
ensure_account('632000', 'Travel & Transportation',      'expense')
ensure_account('633000', 'Utilities',                    'expense')
ensure_account('634000', 'Office & Administrative Expenses', 'expense')
ensure_account('635000', 'Consultancy Fees',             'expense')
ensure_account('636000', 'Medical & Staff Welfare',      'expense')
ensure_account('637000', 'Printing & Stationery',        'expense')
ensure_account('638000', 'Repairs & Maintenance',        'expense')
ensure_account('639000', 'Depreciation',                 'expense')

# Rename generic accounts to NADF-appropriate names
renames = [
    ('630000', 'Salaries & Staff Costs'),
    ('301000', 'Capital Contribution'),
    ('450000', 'Other Income'),
    ('400000', 'Programme Income'),
]
for code, new_name in renames:
    acc = x('account.account', 'search', [[['code','=',code]]])
    if acc:
        x('account.account', 'write', [acc, {'name': new_name}])
        print(f"  Renamed       : {code} → {new_name}")

# ── 2. Analytic Accounts (Cost Centres) ──────────────────────────────────────
print("\n[2/5] Creating analytic accounts (cost centres)...")

# Analytic plan — required in Odoo 17 before creating analytic accounts
plans = x('account.analytic.plan', 'search_read', [[]], {'fields': ['id','name']})
if not plans:
    plan_id = x('account.analytic.plan', 'create', [{'name': 'NADF Cost Centres', 'company_id': 1}])
    print(f"  Created analytic plan: NADF Cost Centres (ID: {plan_id})")
else:
    plan_id = plans[0]['id']
    print(f"  Using analytic plan: {plans[0]['name']} (ID: {plan_id})")

cost_centres = [
    ('Executive Office',    'CC-EXE'),
    ('Finance Unit',        'CC-FIN'),
    ('Procurement Unit',    'CC-PRO'),
    ('Human Resources Unit','CC-HR'),
    ('Administration',      'CC-ADM'),
]
for name, code in cost_centres:
    existing = x('account.analytic.account', 'search', [[['name','=',name]]])
    if existing:
        print(f"  SKIP (exists) : {name}")
        continue
    aid = x('account.analytic.account', 'create', [{
        'name':    name,
        'code':    code,
        'plan_id': plan_id,
        'company_id': 1,
    }])
    print(f"  Created       : {name} ({code})")

# ── 3. Payment Terms — Trim to NADF-relevant set ─────────────────────────────
print("\n[3/5] Configuring payment terms...")

nadf_terms = ['Immediate Payment', '30 Days', 'End of Following Month']
all_terms = x('account.payment.term', 'search_read', [[]], {'fields': ['id','name']})
for t in all_terms:
    print(f"  Available: {t['name']}")

# ── 4. Sample Vendors ─────────────────────────────────────────────────────────
print("\n[4/5] Creating sample vendors...")

ensure_vendor('Abuja Office Supplies Ltd',   'VEN-001',
              phone='+234 9 123 4001', email='sales@abujaoffice.com.ng')
ensure_vendor('TechLink ICT Solutions',       'VEN-002',
              phone='+234 9 123 4002', email='info@techlink.ng')
ensure_vendor('ProLearn Training Institute',  'VEN-003',
              phone='+234 9 123 4003', email='admin@prolearn.ng')
ensure_vendor('SwiftMove Logistics Ltd',      'VEN-004',
              phone='+234 9 123 4004', email='ops@swiftmove.ng')

# ── 5. Bank Account Setup ─────────────────────────────────────────────────────
print("\n[5/5] Configuring bank account...")

existing_banks = x('res.partner.bank', 'search_read',
    [[['company_id','=',1]]], {'fields': ['acc_number','bank_id']})
if existing_banks:
    print(f"  Bank account already exists: {existing_banks[0]['acc_number']}")
else:
    # Find or create CBN / bank record
    bank = x('res.bank', 'search', [[['name','ilike','First Bank']]])
    if not bank:
        bank_id = x('res.bank', 'create', [{
            'name':    'First Bank of Nigeria',
            'bic':     'FBNINGLA',
            'country': 163,
            'city':    'Abuja',
        }])
        print(f"  Created bank: First Bank of Nigeria")
    else:
        bank_id = bank[0]

    # Get company partner ID
    co = x('res.company', 'read', [[1]], {'fields': ['partner_id']})
    partner_id = co[0]['partner_id'][0]

    x('res.partner.bank', 'create', [{
        'acc_number':  '2024001234567',
        'bank_id':     bank_id,
        'partner_id':  partner_id,
        'company_id':  1,
    }])
    print("  Created: Account No. 2024001234567 — First Bank of Nigeria")

# ── Summary ───────────────────────────────────────────────────────────────────
total_accounts = x('account.account', 'search_count', [[]])
total_vendors  = x('res.partner', 'search_count', [[['supplier_rank','>',0]]])
total_analytic = x('account.analytic.account', 'search_count', [[]])

print("\n" + "=" * 60)
print("  Phase 2 Finance Configuration — COMPLETE")
print("=" * 60)
print(f"  Chart of accounts : {total_accounts} accounts")
print(f"  Cost centres      : {total_analytic} analytic accounts")
print(f"  Vendors           : {total_vendors}")
print("\n  Next: Phase 3 — Procurement Configuration")
