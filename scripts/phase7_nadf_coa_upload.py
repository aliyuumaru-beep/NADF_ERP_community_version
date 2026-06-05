#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 7: Chart of Accounts Upload
Replaces the 71 generic Odoo-localization accounts with NADF's
official 8-digit Nigerian Government Economic Segment accounts.

Execution order:
  1. Read & clean NADF CoA from Excel (320 accounts)
  2. Extract 41 budget lines to CSV (for budget module later)
  3. Create all 320 NADF accounts with correct Odoo account_type
  4. Update journal default accounts to new codes
  5. Update all partner payable/receivable defaults to new codes
  6. Remap demo bill BILL/2026/06/0001 to new NADF accounts
  7. Deprecate all 71 old generic accounts

Special account assignments (required by Odoo for transactions):
  asset_receivable  → 31060401  REVENUE IN ARREARS (Trade Receivable)
  liability_payable → 41040105  OTHER GOODS & SERVICES (Trade Payable)
  asset_cash (Bank) → 31020103  CASH BALANCE: OVERHEAD
  asset_cash (Cash) → 31020104  CASH BALANCE: REVENUE
  asset_prepayments → 31080101  PREPAYMENT
  asset_prepayments → 31080102  MOBILIZATION FEE
  equity_unaffected → 53020101  ACCUMULATED SURPLUS/(DEFICIT)

Run: python3 scripts/phase7_nadf_coa_upload.py
"""

import xmlrpc.client, zipfile, xml.etree.ElementTree as ET, csv, sys
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
URL, DB, PW    = 'http://localhost:8071', 'NADF', 'admin'
EXCEL_PATH     = Path('/Users/mac/Documents/Aliyu/NADF/Digital Transformation/Client Data/NADF CoA localisation.xlsx')
BUDGET_CSV     = Path('/Users/mac/nadf_erp/csv_templates/nadf_budget_fy2026.csv')

uid = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common').authenticate(DB, 'admin', PW, {})
if not uid:
    print("ERROR: Authentication failed"); sys.exit(1)
m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, PW, model, method, args, kw or {})

def find_acc(code):
    ids = x('account.account', 'search', [[['code', '=', code]]])
    return ids[0] if ids else None

print("=" * 65)
print("  NADF ERP MVP — Phase 7: Chart of Accounts Upload")
print("=" * 65)

# ── Step 1: Read & clean Excel ────────────────────────────────────────────────
print("\n[Step 1] Reading NADF CoA from Excel...")

with zipfile.ZipFile(EXCEL_PATH) as z:
    strings = []
    if 'xl/sharedStrings.xml' in z.namelist():
        ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
        for si in ET.parse(z.open('xl/sharedStrings.xml')).getroot().iter(f'{ns}si'):
            strings.append(''.join(n.text or '' for n in si.iter(f'{ns}t')))
    # NADF CoA is the 3rd sheet (index 2)
    sf = sorted([n for n in z.namelist() if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')])[2]
    ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    raw_rows = []
    for row in ET.parse(z.open(sf)).getroot().iter(f'{ns}row'):
        cells = []
        for c in row.iter(f'{ns}c'):
            t, v = c.get('t', ''), c.find(f'{ns}v')
            val = v.text if v is not None else ''
            if t == 's' and val:
                try: val = strings[int(val)]
                except: pass
            cells.append(str(val).strip())
        raw_rows.append(cells)

accounts_raw = []
for r in raw_rows[1:]:  # skip header row
    if not r or not any(c.strip() for c in r) or len(r) < 7:
        continue
    code = r[0].strip()
    if not code or not r[1].strip():
        continue   # blank code or blank class = total/spacer row
    if code == 'ZIP':
        code = '23059901'   # Zonal Intervention Project — custom 8-digit code
    accounts_raw.append({
        'code':      code,
        'fin_class': r[1].strip(),
        'caption':   r[2].strip(),
        'name':      r[6].strip(),
        'budget':    r[7].strip() if len(r) > 7 else '0',
    })

print(f"  {len(accounts_raw)} accounts read and cleaned")

# ── Step 2: Export budget amounts to CSV ─────────────────────────────────────
print(f"\n[Step 2] Saving FY2026 budget amounts → {BUDGET_CSV.name}...")

BUDGET_CSV.parent.mkdir(parents=True, exist_ok=True)
budget_rows = [a for a in accounts_raw if a['budget'] not in ('', '0')]
with open(BUDGET_CSV, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['code', 'name', 'fin_class', 'caption', 'budget_ngn'])
    for a in budget_rows:
        w.writerow([a['code'], a['name'], a['fin_class'], a['caption'], a['budget']])
print(f"  {len(budget_rows)} budget lines → {BUDGET_CSV}")

# ── Step 3: Create accounts ───────────────────────────────────────────────────
print("\n[Step 3] Creating NADF accounts in Odoo...")

SPECIAL_TYPES = {
    '31060401': 'asset_receivable',   # REVENUE IN ARREARS — Trade Receivable
    '31020103': 'asset_cash',         # CASH BALANCE: OVERHEAD — primary Bank
    '31020104': 'asset_cash',         # CASH BALANCE: REVENUE  — Cash
    '31080101': 'asset_prepayments',  # PREPAYMENT (non-capital)
    '31080102': 'asset_prepayments',  # MOBILIZATION FEE (capital prepayment)
    '41040105': 'liability_payable',  # OTHER GOODS & SERVICES — Trade Payable
    '53020101': 'equity_unaffected',  # ACCUMULATED SURPLUS/(DEFICIT)
}

def get_odoo_type(code, fin_class, caption):
    if code in SPECIAL_TYPES:
        return SPECIAL_TYPES[code]
    if fin_class == 'INCOME':       return 'income'
    if fin_class == 'EXPENSES':     return 'expense'
    if fin_class == 'ASSET':
        return 'asset_current' if caption == 'CURRENTS ASSETS' else 'asset_non_current'
    if fin_class == 'LIABILITIES':
        return 'liability_current' if caption == 'CURRENT LIABILITIES' else 'liability_non_current'
    if fin_class == 'EQUITY':       return 'equity'
    return 'expense'

existing_codes = {
    a['code'] for a in x('account.account', 'search_read', [[]], {'fields': ['code']})
}

created = skipped = errors = 0
new_ids = {}   # code → Odoo account id

for a in accounts_raw:
    odoo_type = get_odoo_type(a['code'], a['fin_class'], a['caption'])
    if a['code'] in existing_codes:
        acc_id = find_acc(a['code'])
        if acc_id:
            new_ids[a['code']] = acc_id
        skipped += 1
        continue
    try:
        acc_id = x('account.account', 'create', [{
            'code':         a['code'],
            'name':         a['name'],
            'account_type': odoo_type,
            'reconcile':    odoo_type in ('asset_receivable', 'liability_payable'),
        }])
        new_ids[a['code']] = acc_id
        created += 1
    except Exception as e:
        print(f"  ERROR {a['code']} {a['name'][:40]}: {e}")
        errors += 1

# Fetch any remaining IDs (skipped accounts not yet in new_ids)
for a in accounts_raw:
    if a['code'] not in new_ids:
        acc_id = find_acc(a['code'])
        if acc_id:
            new_ids[a['code']] = acc_id

print(f"  Created: {created}  |  Skipped (exists): {skipped}  |  Errors: {errors}")
print(f"  Special accounts ready: {len([c for c in SPECIAL_TYPES if c in new_ids])}/7")

# ── Step 4: Update journal default accounts ───────────────────────────────────
print("\n[Step 4] Updating journal default accounts...")

journal_updates = [
    # (journal code, field, new account code, description)
    ('BNK1', 'default_account_id', '31020103', 'CASH BALANCE: OVERHEAD'),
    ('CSH1', 'default_account_id', '31020104', 'CASH BALANCE: REVENUE'),
    ('BNK1', 'loss_account_id',    '22020903', 'LOSS ON FOREIGN EXCHANGE'),
    ('BNK1', 'profit_account_id',  '14100101', 'GAIN ON FOREIGN EXCHANGE'),
    ('CSH1', 'loss_account_id',    '22020903', 'LOSS ON FOREIGN EXCHANGE'),
    ('CSH1', 'profit_account_id',  '14100101', 'GAIN ON FOREIGN EXCHANGE'),
    ('INV',  'default_account_id', '16010155', 'OTHER BUDGETARY APPROPRIATION'),
    ('BILL', 'default_account_id', '22020406', 'OTHER MAINTENANCE SERVICES'),
]

for jcode, field, acc_code, desc in journal_updates:
    acc_id = new_ids.get(acc_code)
    if not acc_id:
        print(f"  SKIP [{jcode}].{field} — account {acc_code} not found")
        continue
    j = x('account.journal', 'search', [[['code', '=', jcode]]])
    if j:
        x('account.journal', 'write', [[j[0]], {field: acc_id}])
        print(f"  [{jcode}] {field} → {acc_code} ({desc})")
    else:
        print(f"  SKIP [{jcode}] journal not found")

# ── Step 5: Update partner payable / receivable defaults ─────────────────────
print("\n[Step 5] Updating partner default accounts...")

payable_id    = new_ids.get('41040105')
receivable_id = new_ids.get('31060401')

partners = x('res.partner', 'search', [[]])
pay_ok = rcv_ok = 0
for pid in partners:
    try:
        vals = {}
        if payable_id:    vals['property_account_payable_id']    = payable_id
        if receivable_id: vals['property_account_receivable_id'] = receivable_id
        if vals:
            x('res.partner', 'write', [[pid], vals])
            pay_ok += 1
    except:
        pass

print(f"  {pay_ok} partners → payable:41040105 / receivable:31060401")

# ── Step 6: Remap demo bill to NADF accounts ──────────────────────────────────
print("\n[Step 6] Remapping BILL/2026/06/0001 to NADF accounts...")

# Look up old account IDs by code
old_634000 = find_acc('634000')  # Office & Admin Expenses
old_211000 = find_acc('211000')  # Account Payable

# New target accounts
furniture_id = new_ids.get('23010112')   # PURCHASE OF OFFICE FURNITURE AND FITTINGS
new_payable  = new_ids.get('41040105')   # OTHER GOODS & SERVICES (liability_payable)

bill_ids = x('account.move', 'search', [[['move_type','=','in_invoice'],['state','=','draft']]])
if bill_ids:
    for bid in bill_ids:
        lines = x('account.move.line', 'search_read',
                  [[['move_id','=',bid]]],
                  {'fields': ['id','account_id','display_type']})
        remapped = 0
        for line in lines:
            acc_id = line['account_id'][0] if line['account_id'] else None
            if acc_id == old_634000 and furniture_id:
                x('account.move.line', 'write', [[line['id']], {'account_id': furniture_id}])
                remapped += 1
            elif acc_id == old_211000 and new_payable:
                x('account.move.line', 'write', [[line['id']], {'account_id': new_payable}])
                remapped += 1
        bill_name = x('account.move', 'read', [[bid]], {'fields': ['name']})[0]['name']
        print(f"  {bill_name}: {remapped} lines remapped")
        print(f"    Expense lines → 23010112 (PURCHASE OF OFFICE FURNITURE AND FITTINGS)")
        print(f"    Payable line  → 41040105 (OTHER GOODS & SERVICES)")
else:
    print("  No draft bills found — skipping")

# ── Step 7: Deprecate old generic accounts ────────────────────────────────────
print("\n[Step 7] Deprecating old generic accounts...")

all_accounts = x('account.account', 'search_read', [[]], {'fields': ['id','code','name']})
# Old codes are 6-digit or fewer; all new NADF codes are exactly 8 digits
old_ids = [a['id'] for a in all_accounts if a['code'].isdigit() and len(a['code']) <= 6]

if old_ids:
    x('account.account', 'write', [old_ids, {'deprecated': True}])
    print(f"  {len(old_ids)} old accounts deprecated")
    for a in sorted(all_accounts, key=lambda r: r['code']):
        if a['id'] in old_ids:
            print(f"    deprecated: {a['code']:8s} {a['name']}")
else:
    print("  No old accounts found — may have been deprecated already")

# ── Summary ───────────────────────────────────────────────────────────────────
active_count = x('account.account', 'search_count', [[['deprecated','=',False]]])
dep_count    = x('account.account', 'search_count', [[['deprecated','=',True]]])

print("\n" + "=" * 65)
print("  Summary")
print("=" * 65)
print(f"\n  Active accounts (NADF CoA):  {active_count}")
print(f"  Deprecated (old generic):    {dep_count}")
print(f"  Budget CSV:                  {BUDGET_CSV}")
print(f"\n  Special account assignments:")
print(f"    asset_receivable  → 31060401  REVENUE IN ARREARS")
print(f"    liability_payable → 41040105  OTHER GOODS & SERVICES")
print(f"    asset_cash (Bank) → 31020103  CASH BALANCE: OVERHEAD")
print(f"    asset_cash (Cash) → 31020104  CASH BALANCE: REVENUE")
print(f"    equity_unaffected → 53020101  ACCUMULATED SURPLUS/(DEFICIT)")
print(f"\n  Verify at: http://localhost:8071/odoo/accounting")
