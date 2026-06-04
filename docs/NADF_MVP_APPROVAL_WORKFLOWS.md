# NADF ERP MVP — Approval Workflow Configuration
**Document:** NADF_MVP_APPROVAL_WORKFLOWS.md
**Version:** 1.0
**Date:** 2026-06-04
**Status:** IMPLEMENTED — Phase 5 Complete

---

## 1. Overview

This document records the approval workflow design, implementation decisions, and operational procedures for the NADF ERP MVP.

All workflows are implemented on **Odoo 17 Community Edition**. The Enterprise `approvals` app is not available. This document records the Community Edition alternatives used and the limitations they introduce.

---

## 2. Procurement Approval Workflow

### 2.1 Approval Matrix

| Amount | Approving Authority | Method |
|--------|---------------------|--------|
| ≤ ₦500,000 | Head of Procurement | System threshold — PO auto-blocked; Head Procurement confirms |
| ₦500,001 – ₦5,000,000 | Director Corporate Services | Automated activity created on submission; Director CS approves PO manually |
| > ₦5,000,000 | Executive Secretary | Automated activity created; Director CS receives awareness notification |

### 2.2 Process Flow

```
Procurement Officer
    └── Creates Purchase Order (draft)
            │
            ▼
    Submits for Approval (state → 'to approve')
            │
            ├── Amount ≤ ₦500K ──→ Head Procurement reviews and confirms
            │
            ├── Amount ₦500K–₦5M ──→ Automated To-Do activity created for Director CS
            │                         Director CS opens PO, reviews, approves/rejects
            │
            └── Amount > ₦5M ──→ Automated To-Do activity for Executive Secretary
                                  Awareness activity for Director CS
                                  ES opens PO, reviews, approves/rejects
```

### 2.3 How to Process a Tier 2/3 Approval

1. Approving officer logs in → sees To-Do activity on dashboard
2. Clicks activity → opens the Purchase Order
3. Reviews: vendor, items, amounts, justification (in notes/chatter)
4. **Approve:** clicks "Confirm Order" — PO state moves to 'Purchase Order'
5. **Reject:** clicks "Cancel" — add rejection reason in chatter
6. Marks the To-Do activity as Done

### 2.4 Technical Implementation

- **Tier 1 (≤₦500K):** Native Odoo `purchase` module setting — `purchase.purchase_order_approval = True`, threshold `= 500000.0`
- **Tier 2 (₦500K–₦5M):** `base.automation` rule `NADF: PO Escalation — Tier 2 Director CS` — triggers `on_write` when `state = 'to approve'` and `amount_total` in range
- **Tier 3 (>₦5M):** `base.automation` rule `NADF: PO Escalation — Tier 3 Executive Secretary` — same trigger, higher threshold; also notifies Director CS

### 2.5 Limitation

The Community Edition does not provide a configurable approval matrix UI (Enterprise `approvals` app). Tier 2 and Tier 3 approvals are **activity-based**: the system notifies the approver via a To-Do activity, but the approver must manually confirm the PO. There is no system-enforced block preventing a lower-tier user from approving a high-value PO without the activity being completed.

**Mitigation for MVP demo:** Role-based access ensures only Accounting/Purchase Managers can confirm POs. Operational policy requires approvers to act only after activity receipt.

**Recorded as:** DEC-002 in NADF Decision Log.

---

## 3. Invoice Payment Approval Workflow

### 3.1 Approval Matrix

| Amount | Approving Authority | Method |
|--------|---------------------|--------|
| ≤ ₦1,000,000 | Head Finance | Role-based — Head Finance is Accounting Manager; can post/pay directly |
| ₦1,000,001 – ₦10,000,000 | Director Corporate Services | Activity created on invoice posting |
| > ₦10,000,000 | Executive Secretary | Activity on posting + Director CS awareness |

### 3.2 Process Flow

```
Finance Officer
    └── Creates Vendor Bill (draft)
    └── Attaches invoice document
    └── Confirms and Posts bill (state → 'posted')
            │
            ├── Amount ≤ ₦1M ──→ Head Finance reviews payment run directly
            │
            ├── Amount ₦1M–₦10M ──→ Activity created for Director CS
            │                        Director CS reviews and marks done
            │                        Head Finance proceeds with payment
            │
            └── Amount > ₦10M ──→ Activity for Executive Secretary
                                   Awareness activity for Director CS
                                   Payment only after ES sign-off activity marked done
```

### 3.3 How to Process an Invoice Approval

1. Director CS / Executive Secretary receives To-Do activity notification
2. Opens vendor bill via activity link
3. Reviews bill details, vendor, supporting documents in chatter
4. **Approved:** marks activity Done with note "Approved — proceed with payment"
5. **Rejected:** marks activity Done with note "Rejected — reason: ..." and informs Finance
6. Finance Officer proceeds with payment only after activity is marked done

### 3.4 Technical Implementation

- **Tier 2 (₦1M–₦10M):** `base.automation` rule `NADF: Invoice Escalation — Tier 2 Director CS` — triggers `on_write` when `state = 'posted'`, `move_type = 'in_invoice'`, amount in range
- **Tier 3 (>₦10M):** `base.automation` rule `NADF: Invoice Escalation — Tier 3 Executive Secretary` — same trigger; also notifies Director CS

---

## 4. Leave Approval Workflow

### 4.1 Approval Matrix by Leave Type

| Leave Type | Approval Path | Supporting Doc |
|------------|---------------|----------------|
| Casual Leave | Direct Manager only | No |
| Sick Leave | Direct Manager only | Yes — medical certificate |
| Annual Leave | Head HR (Kabir Haruna) | No |
| Maternity Leave | Head HR | Yes |
| Paternity Leave | Head HR | Yes |
| Compassionate Leave | Head HR | No |
| Study Leave | Direct Manager → Head HR → Executive Secretary activity | Yes |

### 4.2 Leave Manager Assignments

| Employee | Leave Manager | Notes |
|----------|---------------|-------|
| All staff (default) | Head HR — Kabir Haruna | Time Off Officer for HR-validated leaves |
| Head HR (Kabir Haruna) | Director CS — Nasir Ingawa | Escalation for HR's own leaves |
| Director CS, Exec Secretary | Admin | Self-service demo accounts |

### 4.3 Study Leave Process

Study Leave requires three levels of sign-off:

```
Employee submits Study Leave
    └── Step 1: Direct Manager approves (validate1)
    └── Step 2: Head HR approves (validate — final Odoo approval)
    └── Step 3: Automated activity created for Executive Secretary
                ES reviews and marks activity Done as confirmation
                (Recorded in chatter as audit trail)
```

### 4.4 Technical Implementation

- **Leave validation types** set per leave type:
  - `manager` — Casual Leave, Sick Leave
  - `hr` — Annual, Maternity, Paternity, Compassionate
  - `both` — Study Leave (requires both manager + HR Officer sign-off)
- **Leave manager** (`hr.employee.leave_manager_id`): set to `head.hr` (uid=11) for all employees
- **Study Leave ES escalation:** `base.automation` rule `NADF: Study Leave — Executive Secretary Sign-Off` — triggers when leave state changes to `validate`, creates ES To-Do activity

---

## 5. All Automated Rules Summary

| Rule Name | Model | Trigger | Approver Notified |
|-----------|-------|---------|-------------------|
| NADF: PO Escalation — Tier 2 Director CS (₦500K–₦5M) | purchase.order | on_write → state=to approve | Director CS |
| NADF: PO Escalation — Tier 3 Executive Secretary (>₦5M) | purchase.order | on_write → state=to approve | Executive Secretary + Director CS (FYI) |
| NADF: Invoice Escalation — Tier 2 Director CS (₦1M–₦10M) | account.move | on_write → state=posted | Director CS |
| NADF: Invoice Escalation — Tier 3 Executive Secretary (>₦10M) | account.move | on_write → state=posted | Executive Secretary + Director CS (FYI) |
| NADF: Study Leave — Executive Secretary Sign-Off | hr.leave | on_write → state=validate | Executive Secretary |

**Total active rules: 5**
All rules use `base.automation` with `ir.actions.server` code actions that call `record.activity_schedule('mail.mail_activity_data_todo', ...)`.

---

## 6. Decisions Taken — Phase 5

### DEC-P5-001 — Activity-Based Approval for Community Edition

**Decision:** Use `base.automation` + `ir.actions.server` activity scheduling as the Community Edition substitute for the Enterprise `approvals` app.

**Why:** The `approvals` module is Enterprise-only. Community Edition has no native multi-level approval matrix. Activity-based escalation is the highest-capability alternative available.

**Trade-offs accepted:**
- No hard system block on high-value approvals (activity is advisory, not enforced)
- Approver must manually open and confirm the record; system does not prevent action by unauthorised users
- Adequate for MVP demo; would need stronger controls in production

**How to revisit:** Upgrade to Odoo Enterprise, or develop a custom `nadf_approvals` module with Python-level permission checks on PO/invoice confirmation actions. Requires written justification per Implementation Standards.

### DEC-P5-002 — Head HR as Universal Leave Manager

**Decision:** All employees' `leave_manager_id` is set to Head HR (Kabir Haruna), not to their line manager.

**Why:** In Odoo 17, `leave_manager_id` is the "Time Off Officer" — the HR-level approver. For leaves with `leave_validation_type = 'hr'`, this is who approves. Direct manager approval (for Casual/Sick) is handled separately via the `parent_id` (reporting line) relationship.

**Exception:** Head HR's own leave manager is Director CS.

### DEC-P5-003 — Study Leave Three-Level Workaround

**Decision:** Study Leave is configured as `leave_validation_type = 'both'` (Manager + Head HR), with an additional `base.automation` activity to Executive Secretary after final HR validation.

**Why:** Odoo Community hr_holidays supports maximum 2 approval levels. The NADF approval matrix requires 3 levels for Study Leave. The third level (ES sign-off) is implemented as a non-blocking activity.

**Limitation:** The ES activity is created after leave is already approved by HR. For stronger control, ES approval would need to happen before HR final validation. This is a known MVP limitation.

---

## 7. Audit Trail

All approval actions are recorded in Odoo's chatter (message log) on each record. This provides:
- Who submitted the request
- When activities were assigned
- Who marked activities done
- Any comments or rejection reasons

The chatter is visible to all users with access to the record and is immutable (cannot be deleted by regular users).

---

## 8. Community Edition Limitations Summary

| Feature | Enterprise | Community MVP Equivalent |
|---------|------------|--------------------------|
| Configurable approval matrix UI | `approvals` app | base.automation rules + manual procedure |
| Hard approval blocks | Native enforcement | Role-based access + activity-based advisory |
| Approval delegation | Built-in delegation | Manual user substitution |
| Escalation timer | Auto-escalate if no response | Not implemented (manual follow-up) |
| Approval audit report | Built-in report | Chatter log (manual review) |

---

*Configured by: AI Developer (Claude Code) | Date: 2026-06-04*
*Phase 5 implementation complete. Next: Phase 6 — Demo Scenarios*
