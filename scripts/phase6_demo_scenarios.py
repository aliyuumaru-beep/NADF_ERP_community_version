#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 6 Demo Scenarios
Creates realistic demo data for all 4 scenarios and leaves each
at the correct state for live demonstration.

Scenario 1: Laptop purchase — PO submitted, awaiting Director CS approval
Scenario 2: Annual leave — submitted, awaiting Head HR approval
Scenario 3: Vendor invoice — draft, ready for Finance Officer to post
Scenario 4: Consultancy contract — high-value PO awaiting Executive Secretary

Run: python3 scripts/phase6_demo_scenarios.py
"""

import xmlrpc.client, sys
from datetime import datetime, timedelta

URL, DB = 'http://localhost:8071', 'NADF'
ADMIN_PASS = 'admin'
uid = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common').authenticate(DB, 'admin', ADMIN_PASS, {})
if not uid:
    print("ERROR: Auth failed"); sys.exit(1)
m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, ADMIN_PASS, model, method, args, kw or {})

def exists(model, domain):
    return bool(x(model, 'search', [domain], {'limit': 1}))

today = datetime.now()
next_month_start = (today.replace(day=1) + timedelta(days=32)).replace(day=1)
leave_from = next_month_start.strftime('%Y-%m-%d 08:00:00')
leave_to   = (next_month_start + timedelta(days=4)).strftime('%Y-%m-%d 17:00:00')
leave_from_date = next_month_start.strftime('%Y-%m-%d')
leave_to_date   = (next_month_start + timedelta(days=4)).strftime('%Y-%m-%d')
po_delivery = (today + timedelta(days=14)).strftime('%Y-%m-%d 00:00:00')

print("=" * 60)
print("  NADF ERP MVP — Phase 6 Demo Data Creation")
print("=" * 60)

# ── SCENARIO 1 — Laptop Purchase (₦2,250,000 — Tier 2) ───────────────────────
print("\n[Scenario 1] Laptop Purchase — 5 units × ₦450,000 = ₦2,250,000")
print("             Expected: Director CS To-Do activity auto-created")

if exists('purchase.order', [['name','ilike','DEMO-S1']]):
    po1 = x('purchase.order','search_read',
        [[['name','ilike','DEMO-S1']]], {'fields':['id','name','state','amount_total']})
    print(f"  SKIP (exists): {po1[0]['name']} | ₦{po1[0]['amount_total']:,.0f} | {po1[0]['state']}")
    po1_id = po1[0]['id']
else:
    po1_id = x('purchase.order','create',[{
        'partner_id':  16,    # TechLink ICT Solutions
        'date_order':  today.strftime('%Y-%m-%d %H:%M:%S'),
        'notes':       'ICT Equipment — New Staff Onboarding Batch 2026. Approved under NADF Annual Procurement Plan.',
        'order_line': [(0,0,{
            'product_id':   1,       # Laptop
            'name':         'Laptop (15" Business) — New Staff Onboarding',
            'product_qty':  5.0,
            'price_unit':   450000.0,
            'date_planned': po_delivery,
        })],
    }])
    # Submit for approval — amount > ₦500K threshold → goes to 'to approve'
    x('purchase.order', 'button_confirm', [[po1_id]])
    po1 = x('purchase.order','read',[[po1_id]],{'fields':['name','state','amount_total']})
    print(f"  Created & submitted: {po1[0]['name']} | ₦{po1[0]['amount_total']:,.0f} | state={po1[0]['state']}")
    print(f"  ✓ Director CS should have received a To-Do approval activity")

# ── SCENARIO 4 — High-Value Consultancy (₦7,500,000 — Tier 3) ────────────────
# (Created before Scenario 3 so the invoice scenario stays as the 3rd demo)
print("\n[Scenario 4] High-Value Consultancy PO — ₦7,500,000 (Tier 3: ES + Dir CS)")
print("             Expected: Executive Secretary + Director CS activities")

if exists('purchase.order', [['name','ilike','DEMO-S4']]):
    po4 = x('purchase.order','search_read',
        [[['name','ilike','DEMO-S4']]], {'fields':['id','name','state','amount_total']})
    print(f"  SKIP (exists): {po4[0]['name']} | ₦{po4[0]['amount_total']:,.0f} | {po4[0]['state']}")
    po4_id = po4[0]['id']
else:
    po4_id = x('purchase.order','create',[{
        'partner_id':  17,    # ProLearn Training Institute
        'date_order':  today.strftime('%Y-%m-%d %H:%M:%S'),
        'notes':       'Strategic Capacity Building Programme — Senior Management. '
                       'Covers 3-day residential workshop for 10 directors + facilitation fees. '
                       'Ref: NADF/TRAINING/2026/001',
        'order_line': [(0,0,{
            'product_id':   7,       # Consultancy Services
            'name':         'Senior Management Capacity Building Programme (3 Days × 10 Participants)',
            'product_qty':  50.0,    # 50 person-days at ₦150K/day
            'price_unit':   150000.0,
            'date_planned': po_delivery,
        })],
    }])
    x('purchase.order', 'button_confirm', [[po4_id]])
    po4 = x('purchase.order','read',[[po4_id]],{'fields':['name','state','amount_total']})
    print(f"  Created & submitted: {po4[0]['name']} | ₦{po4[0]['amount_total']:,.0f} | state={po4[0]['state']}")
    print(f"  ✓ Executive Secretary + Director CS should have received activities")

# ── SCENARIO 2 — Annual Leave Request ────────────────────────────────────────
print(f"\n[Scenario 2] Annual Leave — Suleiman Yusuf, {leave_from_date} to {leave_to_date}")
print("             Expected: Leave awaiting Head HR approval")

if exists('hr.leave', [['employee_id','=',5],['holiday_status_id','=',5],['state','in',['confirm','validate1','validate']]]):
    lv = x('hr.leave','search_read',
        [[['employee_id','=',5],['holiday_status_id','=',5]]],
        {'fields':['id','name','state','date_from','date_to'],'limit':1})
    print(f"  SKIP (exists): {lv[0].get('name','Leave')} | {lv[0]['state']}")
else:
    leave_id = x('hr.leave','create',[{
        'holiday_status_id': 5,       # Annual Leave
        'employee_id':       5,       # Suleiman Yusuf
        'date_from':         leave_from,
        'date_to':           leave_to,
        'request_date_from': leave_from_date,
        'request_date_to':   leave_to_date,
        'name':              'Annual Leave — Rest & Recuperation',
        'private_note':      'Annual rest leave. Family commitment.',
    }])
    # Submit for approval
    x('hr.leave', 'action_confirm', [[leave_id]])
    lv = x('hr.leave','read',[[leave_id]],{'fields':['name','state','number_of_days']})
    print(f"  Created & submitted: {lv[0]['name']} | {lv[0]['number_of_days']} days | state={lv[0]['state']}")
    print(f"  ✓ Leave awaiting Head HR (Kabir Haruna) approval")

# ── SCENARIO 3 — Vendor Invoice for Payment ───────────────────────────────────
print("\n[Scenario 3] Vendor Invoice — Abuja Office Supplies, ₦3,500,000")
print("             Expected: Invoice in draft — Finance Officer posts → Dir CS activity")

if exists('account.move', [['partner_id','=',15],['move_type','=','in_invoice'],['state','=','draft'],['ref','ilike','DEMO-S3']]):
    inv = x('account.move','search_read',
        [[['partner_id','=',15],['ref','ilike','DEMO-S3']]],
        {'fields':['id','name','state','amount_total'],'limit':1})
    print(f"  SKIP (exists): {inv[0]['name']} | ₦{inv[0]['amount_total']:,.0f} | {inv[0]['state']}")
else:
    # Get income/expense accounts
    payable_acc = x('account.account','search',[[['code','=','211000']]])  # Account Payable
    expense_acc = x('account.account','search',[[['code','=','634000']]])  # Office & Admin

    inv_id = x('account.move','create',[{
        'move_type':    'in_invoice',
        'partner_id':   15,      # Abuja Office Supplies Ltd
        'invoice_date': today.strftime('%Y-%m-%d'),
        'ref':          'DEMO-S3-INV-2026-0147',
        'narration':    'Supply of office furniture and equipment per LPO NADF/PRO/2026/031. '
                        'Payment due within 30 days of delivery.',
        'invoice_line_ids': [
            (0,0,{
                'name':        '5 Executive Office Chairs',
                'quantity':    5.0,
                'price_unit':  75000.0,
                'account_id':  expense_acc[0] if expense_acc else False,
            }),
            (0,0,{
                'name':        '10 Office Work Tables',
                'quantity':    10.0,
                'price_unit':  120000.0,
                'account_id':  expense_acc[0] if expense_acc else False,
            }),
            (0,0,{
                'name':        'Office Partitioning & Installation',
                'quantity':    1.0,
                'price_unit':  2075000.0,
                'account_id':  expense_acc[0] if expense_acc else False,
            }),
        ],
    }])
    inv = x('account.move','read',[[inv_id]],{'fields':['name','state','amount_total']})
    print(f"  Created: {inv[0]['name']} | ₦{inv[0]['amount_total']:,.0f} | state={inv[0]['state']}")
    print(f"  ✓ Finance Officer posts this during demo → triggers Dir CS activity")

# ── Final Verification ────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("  Demo Data Summary")
print("=" * 60)

pos = x('purchase.order','search_read',
    [[['state','=','to approve']]], {'fields':['name','amount_total','partner_id']})
leaves = x('hr.leave','search_read',
    [[['state','=','confirm']]], {'fields':['employee_id','holiday_status_id','number_of_days']})
invoices = x('account.move','search_read',
    [[['move_type','=','in_invoice'],['state','=','draft']]], {'fields':['name','amount_total','partner_id']})
activities = x('mail.activity','search_read',
    [[['res_model','in',['purchase.order','account.move','hr.leave']]]], {'fields':['summary','user_id','res_model']})

print(f"\n  Purchase Orders pending approval : {len(pos)}")
for p in pos:
    print(f"    {p['name']:15s}  ₦{p['amount_total']:>12,.0f}  {p['partner_id'][1]}")

print(f"\n  Leave requests pending approval  : {len(leaves)}")
for l in leaves:
    print(f"    {l['employee_id'][1]:25s}  {l['holiday_status_id'][1]}  ({l['number_of_days']} days)")

print(f"\n  Draft vendor invoices            : {len(invoices)}")
for i in invoices:
    print(f"    {i['name']:15s}  ₦{i['amount_total']:>12,.0f}  {i['partner_id'][1]}")

print(f"\n  Approval activities created      : {len(activities)}")
for a in activities:
    print(f"    [{a['res_model'].split('.')[-1]:15s}]  {a['summary'][:55]}  → {a['user_id'][1]}")

print("\n  All demo data ready. See docs/NADF_MVP_DEMO_SCENARIOS.md for walkthrough.")
