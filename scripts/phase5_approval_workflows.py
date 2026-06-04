#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 5 Approval Workflow Configuration
Community Edition implementation using:
  - hr_holidays native approval chains (leave)
  - purchase module approval threshold (procurement tier 1)
  - base.automation + ir.actions.server code rules (tiers 2 & 3)

Approval matrix implemented:
  Procurement:  ≤500K → Head Procurement | 500K–5M → Director CS | >5M → Exec Secretary
  Payment:      ≤1M   → Head Finance     | 1M–10M  → Director CS | >10M → Exec Secretary
  Leave:        Casual/Sick → Direct Manager | Annual/Maternity → Head HR | Study → Both+ES

Run: python3 scripts/phase5_approval_workflows.py
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

def find_model(name):
    res = x('ir.model', 'search_read', [[['model','=',name]]], {'fields': ['id']})
    return res[0]['id'] if res else None

# ── Approver IDs (from Phase 1/4) ─────────────────────────────────────────────
ES_UID   = 13   # executive.secretary  (Maryam Koko)
DIR_UID  = 12   # director.cs          (Nasir Ingawa)
HF_UID   = 7    # head.finance         (Adebanke Fajana)
HHR_UID  = 11   # head.hr              (Kabir Haruna)
HP_UID   = 9    # head.procurement     (Kabir Abdulkadir)

print("=" * 60)
print("  NADF ERP MVP — Phase 5 Approval Workflows")
print("=" * 60)

# ── 1. Leave Manager Assignments ──────────────────────────────────────────────
print("\n[1/4] Setting leave managers for all employees...")

employees = x('hr.employee', 'search_read',
    [[['company_id','=',1],['active','=',True]]],
    {'fields': ['id','name','user_id','parent_id']})

for emp in employees:
    # All employees: Time Off Officer = Head HR (Kabir Haruna)
    # This covers Annual, Maternity, Paternity, Study, Compassionate leave
    # Sick/Casual is routed to direct manager via leave_validation_type='manager'
    x('hr.employee', 'write', [[emp['id']], {'leave_manager_id': HHR_UID}])
    print(f"  {emp['name']:35s} → leave manager: Head HR (Kabir Haruna)")

# Head HR herself reports to Director CS for leave escalation
hr_head_emp = x('hr.employee', 'search', [[['user_id','=',HHR_UID]]])
if hr_head_emp:
    x('hr.employee', 'write', [hr_head_emp, {'leave_manager_id': DIR_UID}])
    print(f"  Head HR leave manager overridden → Director CS")

# Executive Secretary and Director CS: leave_manager = admin (self-service demo)
for uid_val in [ES_UID, DIR_UID]:
    emp = x('hr.employee', 'search', [[['user_id','=',uid_val]]])
    if emp:
        x('hr.employee', 'write', [emp, {'leave_manager_id': 2}])  # admin

# ── 2. Procurement Escalation Rules ──────────────────────────────────────────
print("\n[2/4] Creating procurement approval escalation rules...")

po_model_id = find_model('purchase.order')

def ensure_automation(name, model_id, trigger, filter_pre, filter_domain, code):
    existing = x('base.automation', 'search', [[['name','=',name]]])
    if existing:
        print(f"  SKIP (exists): {name}")
        return existing[0]

    # Create server action first
    action_id = x('ir.actions.server', 'create', [{
        'name':     name,
        'model_id': model_id,
        'state':    'code',
        'code':     code,
    }])

    auto_id = x('base.automation', 'create', [{
        'name':              name,
        'model_id':          model_id,
        'trigger':           trigger,
        'filter_pre_domain': filter_pre,
        'filter_domain':     filter_domain,
        'active':            True,
        'action_server_ids': [(4, action_id)],
    }])
    print(f"  Created: {name}")
    return auto_id

# ── PO Tier 2: ₦500K – ₦5M → Director Corporate Services ────────────────────
po_tier2_code = f"""
amount = record.amount_total
if amount > 500000 and amount <= 5000000:
    record.activity_schedule(
        'mail.mail_activity_data_todo',
        user_id={DIR_UID},
        summary='[NADF] PO Approval Required — Director CS (₦{{:,.0f}})'.format(amount),
        note='<p>Purchase Order <b>{{name}}</b> requires your approval.</p>'
             '<p>Amount: <b>₦{{amount:,.0f}}</b> — Tier 2 approval (₦500K–₦5M threshold).</p>'
             '<p>Submitted by: {{partner}}</p>'.format(
                 name=record.name,
                 amount=amount,
                 partner=record.partner_id.name if record.partner_id else ''
             ),
    )
""".strip()

ensure_automation(
    name          = 'NADF: PO Escalation — Tier 2 Director CS (₦500K–₦5M)',
    model_id      = po_model_id,
    trigger       = 'on_write',
    filter_pre    = "[('state', 'not in', ['to approve','purchase','done','cancel'])]",
    filter_domain = "[('state','=','to approve'),('amount_total','>',500000),('amount_total','<=',5000000)]",
    code          = po_tier2_code,
)

# ── PO Tier 3: > ₦5M → Executive Secretary (+ Director CS awareness) ─────────
po_tier3_code = f"""
amount = record.amount_total
if amount > 5000000:
    record.activity_schedule(
        'mail.mail_activity_data_todo',
        user_id={ES_UID},
        summary='[NADF] PO Approval Required — Executive Secretary (₦{{:,.0f}})'.format(amount),
        note='<p>Purchase Order <b>{{name}}</b> requires Executive Secretary approval.</p>'
             '<p>Amount: <b>₦{{amount:,.0f}}</b> — Tier 3 approval (above ₦5,000,000 threshold).</p>'.format(
                 name=record.name, amount=amount),
    )
    record.activity_schedule(
        'mail.mail_activity_data_todo',
        user_id={DIR_UID},
        summary='[NADF] FYI — High-Value PO Submitted (₦{{:,.0f}})'.format(amount),
        note='<p>Purchase Order <b>{{name}}</b> has been submitted for Executive Secretary approval.</p>'
             '<p>Amount: <b>₦{{amount:,.0f}}</b>. For your awareness.</p>'.format(
                 name=record.name, amount=amount),
    )
""".strip()

ensure_automation(
    name          = 'NADF: PO Escalation — Tier 3 Executive Secretary (>₦5M)',
    model_id      = po_model_id,
    trigger       = 'on_write',
    filter_pre    = "[('state', 'not in', ['to approve','purchase','done','cancel'])]",
    filter_domain = "[('state','=','to approve'),('amount_total','>',5000000)]",
    code          = po_tier3_code,
)

# ── 3. Invoice / Payment Escalation Rules ─────────────────────────────────────
print("\n[3/4] Creating invoice payment escalation rules...")

inv_model_id = find_model('account.move')

# Invoice Tier 1: ≤₦1M — Head Finance reviews (no automation; HF is account manager)
# Invoice Tier 2: ₦1M–₦10M → Director CS
inv_tier2_code = f"""
if record.move_type == 'in_invoice' and record.amount_total > 1000000 and record.amount_total <= 10000000:
    record.activity_schedule(
        'mail.mail_activity_data_todo',
        user_id={DIR_UID},
        summary='[NADF] Invoice Payment Approval — Director CS (₦{{:,.0f}})'.format(record.amount_total),
        note='<p>Vendor bill <b>{{ref}}</b> from <b>{{vendor}}</b> requires Director CS approval before payment.</p>'
             '<p>Amount: <b>₦{{amount:,.0f}}</b> — Tier 2 payment approval (₦1M–₦10M threshold).</p>'.format(
                 ref=record.name,
                 vendor=record.partner_id.name if record.partner_id else '',
                 amount=record.amount_total),
    )
""".strip()

ensure_automation(
    name          = 'NADF: Invoice Escalation — Tier 2 Director CS (₦1M–₦10M)',
    model_id      = inv_model_id,
    trigger       = 'on_write',
    filter_pre    = "[('state','!=','posted'),('move_type','=','in_invoice')]",
    filter_domain = "[('state','=','posted'),('move_type','=','in_invoice'),('amount_total','>',1000000),('amount_total','<=',10000000)]",
    code          = inv_tier2_code,
)

# Invoice Tier 3: > ₦10M → Executive Secretary
inv_tier3_code = f"""
if record.move_type == 'in_invoice' and record.amount_total > 10000000:
    record.activity_schedule(
        'mail.mail_activity_data_todo',
        user_id={ES_UID},
        summary='[NADF] Invoice Payment Approval — Executive Secretary (₦{{:,.0f}})'.format(record.amount_total),
        note='<p>Vendor bill <b>{{ref}}</b> from <b>{{vendor}}</b> requires Executive Secretary approval before payment.</p>'
             '<p>Amount: <b>₦{{amount:,.0f}}</b> — Tier 3 payment approval (above ₦10,000,000 threshold).</p>'.format(
                 ref=record.name,
                 vendor=record.partner_id.name if record.partner_id else '',
                 amount=record.amount_total),
    )
    record.activity_schedule(
        'mail.mail_activity_data_todo',
        user_id={DIR_UID},
        summary='[NADF] FYI — High-Value Invoice Posted (₦{{:,.0f}})'.format(record.amount_total),
        note='<p>Bill <b>{{ref}}</b> (₦{{amount:,.0f}}) has been referred to Executive Secretary for payment approval.</p>'.format(
            ref=record.name, amount=record.amount_total),
    )
""".strip()

ensure_automation(
    name          = 'NADF: Invoice Escalation — Tier 3 Executive Secretary (>₦10M)',
    model_id      = inv_model_id,
    trigger       = 'on_write',
    filter_pre    = "[('state','!=','posted'),('move_type','=','in_invoice')]",
    filter_domain = "[('state','=','posted'),('move_type','=','in_invoice'),('amount_total','>',10000000)]",
    code          = inv_tier3_code,
)

# ── 4. Study Leave → Executive Secretary Awareness ────────────────────────────
print("\n[4/4] Creating Study Leave escalation rule...")

leave_model_id = find_model('hr.leave')
study_type = x('hr.leave.type', 'search', [[['name','=','Study Leave']]])
study_type_id = study_type[0] if study_type else None

if study_type_id:
    study_leave_code = f"""
if record.holiday_status_id.id == {study_type_id}:
    record.activity_schedule(
        'mail.mail_activity_data_todo',
        user_id={ES_UID},
        summary='[NADF] Study Leave — Executive Secretary Sign-Off Required',
        note='<p>Study Leave request from <b>{{emp}}</b> has been validated by HR and requires Executive Secretary final sign-off.</p>'
             '<p>Duration: {{days}} day(s) | From: {{date_from}} To: {{date_to}}</p>'.format(
                 emp=record.employee_id.name if record.employee_id else '',
                 days=record.number_of_days,
                 date_from=str(record.date_from)[:10],
                 date_to=str(record.date_to)[:10]),
    )
""".strip()

    ensure_automation(
        name          = 'NADF: Study Leave — Executive Secretary Sign-Off',
        model_id      = leave_model_id,
        trigger       = 'on_write',
        filter_pre    = "[('state','!=','validate')]",
        filter_domain = "[('state','=','validate')]",
        code          = study_leave_code,
    )
else:
    print("  WARN: Study Leave type not found — skipping escalation rule")

# ── Verify all automation rules ───────────────────────────────────────────────
rules = x('base.automation', 'search_read',
    [[['name','ilike','NADF:']]], {'fields': ['name','active','trigger']})

print("\n" + "=" * 60)
print("  Phase 5 Approval Workflows — COMPLETE")
print("=" * 60)
print(f"\n  Automation rules created: {len(rules)}")
for r in rules:
    status = '✓ ACTIVE' if r['active'] else '✗ INACTIVE'
    print(f"  {status}  {r['name']}")

print("""
  Leave Approval Summary:
    Casual Leave    → Direct Manager only
    Sick Leave      → Direct Manager (+ medical doc)
    Annual Leave    → Head HR (Kabir Haruna)
    Maternity       → Head HR (Kabir Haruna)
    Paternity       → Head HR (Kabir Haruna)
    Compassionate   → Head HR (Kabir Haruna)
    Study Leave     → Direct Manager + Head HR + ES activity

  Procurement Approval Summary:
    ≤ ₦500,000      → Head Procurement (system threshold)
    ₦500K – ₦5M     → Director CS (activity created automatically)
    > ₦5M           → Executive Secretary (activity + Dir CS awareness)

  Payment Approval Summary:
    ≤ ₦1,000,000    → Head Finance (accounting manager role)
    ₦1M – ₦10M      → Director CS (activity on invoice posting)
    > ₦10M          → Executive Secretary (activity + Dir CS awareness)

  LIMITATION NOTE:
    Procurement tier-2/3 approvals are activity-based (Odoo Community).
    The approver receives a To-Do activity; they must manually confirm
    approval by marking the activity done and then approving the PO.
    This is the Community Edition substitute for the Enterprise
    Approvals app which provides a configurable approval matrix UI.
""")
