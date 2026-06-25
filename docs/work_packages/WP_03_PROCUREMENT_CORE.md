# WP-03 — Procurement Core
## NADF ERP Programme — Work Package Definition

**Work Package ID:** WP-03
**Title:** Procurement Core
**Phase:** 1 — Foundation
**Complexity:** Medium
**Capability area:** CA-02 — Procurement (requisition, RFQ/tender, goods receipt, compliance, contract evaluation)
**Authority:** PEG-6 approval 2026-06-24 · Transfer Package v2.1
**Prepared by:** A1 Master Orchestrator · D1 Functional Architect · G1/G2/G3
**Date:** 2026-06-25
**Status:** GO — G1/G2/G3 Go/No-Go PASS (see §8). Implementation authorised pending pre-work backup.

> **GO confirmed.** G1/G2/G3 Go/No-Go checkpoint cleared 2026-06-25. D2 Solution Builder must take a pre-work backup before executing the first mutating operation. WP03-07 remains blocked pending client confirmation of B-02/B-03.

---

## 1. Objective

Configure the Procurement department's operational tools in Odoo 17 CE:
- Establish and validate the vendor compliance mechanism on `res.partner`.
- Configure the OCA `purchase_request` multi-step requisition workflow (Requisitioner → Procurement Officer approval).
- Configure the CE native `purchase_requisition` RFQ/tender workflow (Call for Tender type + award flow).
- Re-validate goods receipt and stock flow against NADF Main Warehouse.
- Evaluate the OCA `contract` module fit for NADF procurement contracts; log DEC-CONTRACT-001.
- Verify `mail.thread` audit trail on `purchase.request` and `purchase.order`.
- WP03-07 (multi-level approval chain) is blocked on client confirmation; document as BLOCKED with the existing Phase 3 interim approval threshold.

---

## 2. Scope

### In scope
| Item | Detail |
|------|--------|
| Vendor compliance mechanism | Create `x_compliance_status` selection field on `res.partner` via Odoo shell (`ir.model.fields`); document that `nadf_vendor_onboarding` approval state also serves as a compliance proxy |
| `purchase_request` requisition | Configure picking type, department field, approval user group (Procurement Officer); test draft→to_approve→approved→in_progress→done flow |
| `purchase_requisition` RFQ/tender | Create "Call for Tender" requisition type (`exclusive=True`); test requisition→RFQ distribution→vendor lines→award→PO generation |
| Goods receipt / stock flow | Create test PO → confirm → validate receipt in NADF Main Warehouse → verify `stock.move` lines |
| OCA contract evaluation | Review OCA/contract@17.0 capability; compare to `nadf_legal_contract` custom module (Phase 2/3 spec); log DEC-CONTRACT-001 |
| mail.thread audit | Verify message posting works on `purchase.request` and `purchase.order` (functional test of confirmed model capability) |
| Documentation | Update `DECISION_LOG.md` (DEC-CONTRACT-001, DEC-WP03-001 for compliance mechanism); update `IMPLEMENTATION_HISTORY.md`; update `CHANGELOG.md` |

### Out of scope
| Item | Why excluded |
|------|-------------|
| WP03-07 multi-level approval chain | Blocked — client must confirm B-02 (RACI step 1.19) and B-03 (threshold amounts) first |
| `nadf_vendor_compliance` custom module | Phase 2 spec required — no spec, no code |
| `nadf_legal_contract` custom module | Phase 2/3 spec required — OCA contract evaluation is a fit-gap analysis only |
| Payroll-linked expense claims | Deferred pending `nadf_payroll_ng` (Phase 2/3) |
| Multi-currency procurement | Not in Phase 1 scope |
| Import of vendor master data | Client data responsibility; WP-03 only validates the mechanism |

---

## 3. Pre-existing System State (from Go/No-Go check — 2026-06-25)

| Item | State | Implication |
|------|-------|-------------|
| `purchase_request` module | ✅ `installed` | No reinstall needed; configure only |
| `purchase_requisition` module | ✅ `installed` (CE native 17.0.0.1) | 1 type exists: "Blanket Order" (`exclusive=multiple`); "Call for Tender" type to be added |
| `purchase` module | ✅ `installed` | — |
| `stock` module | ✅ `installed` | — |
| `purchase.purchase_order_approval` | ✅ `True` (Phase 3 legacy) | PO approval enabled — existing threshold |
| `purchase.purchase_order_approval_min_amount` | ✅ `500,000.00` (Phase 3 legacy) | **Client must confirm via B-03** — ₦500K may not match NADF-approved threshold |
| `purchase.request` records | 0 | Clean slate |
| `purchase.requisition` records | 0 | Clean slate |
| `purchase.order` records | 9 (Phase 3/6 demos) | P00005, P00006 in `to_approve`; P00007, P00008 confirmed; P00009 cancelled |
| Custom `x_` fields on `res.partner` | None | Compliance field does not exist — WP03-01 must create it |
| `mail.thread` on `purchase.request` | ✅ True | AC-WP03-06 pre-confirmed |
| `mail.thread` on `purchase.order` | ✅ True | AC-WP03-06 pre-confirmed |
| Stock picking type (receipts) | ✅ "Receipts" — NADF Main Warehouse | Goods receipt available |
| Done stock receipts | 0 | No existing receipts; clean test environment |
| Vendors (supplier_rank > 0) | 4 | From Phase 3/6 demos — sufficient for testing |
| Latest backup | `nadf_20260624_160329` (pre-WP-01) | **New backup required before WP-03 execution begins** |

---

## 4. Deliverables

| ID | Deliverable | Verification |
|----|------------|--------------|
| D-WP03-01 | `x_compliance_status` field created on `res.partner`; at least 2 existing vendors tagged | `env['res.partner'].search([('x_compliance_status','!=',False)])` |
| D-WP03-02 | DEC-WP03-001 logged: compliance mechanism decision (x_ field vs vendor_onboarding proxy) | `docs/DECISION_LOG.md` |
| D-WP03-03 | `purchase_request` workflow configured; picking type and Procurement Officer group assigned | UI: Purchase → Purchase Requests; test draft→approved cycle |
| D-WP03-04 | Test purchase request created, approved by Procurement Officer, converted to PO | UI: Purchase Requests — 1 test PR in `done` state |
| D-WP03-05 | "Call for Tender" requisition type created; test requisition with 2 vendor RFQs; award generates PO | UI: Purchase → Requisitions — 1 test requisition in `done` state |
| D-WP03-06 | Test PO created from PR/requisition → received in NADF Main Warehouse → `stock.move` lines confirmed | UI: Inventory → Receipts — 1 done transfer linked to PO |
| D-WP03-07 | DEC-CONTRACT-001 logged: OCA `contract` vs `nadf_legal_contract` fit-gap decision | `docs/DECISION_LOG.md` |
| D-WP03-08 | `mail.thread` functional test: message posted on `purchase.request` and `purchase.order` | UI: message history on test records |
| D-WP03-09 | WP03-07 approval chain documented as BLOCKED with interim state (₦500K threshold, B-02/B-03 client pending) | `IMPLEMENTATION_HISTORY.md` |

---

## 5. Acceptance Criteria

| ID | Criterion | Test method |
|----|-----------|-------------|
| AC-WP03-01 | `x_compliance_status` field exists on `res.partner`; selection values: 'compliant', 'non_compliant', 'pending' | `env['ir.model.fields'].search([('model','=','res.partner'),('name','=','x_compliance_status')])` |
| AC-WP03-02 | `purchase.request` full workflow cycle completed: draft → to_approve → approved → in_progress → done | Test purchase request record in `done` state |
| AC-WP03-03 | Procurement Requisitioner group can create PRs; Procurement Officer group can approve; Finance Approver group can approve POs | Role-based shell test |
| AC-WP03-04 | `purchase.requisition` "Call for Tender" type exists; test requisition generates ≥ 2 RFQs to separate vendors | DB query `purchase.requisition.type` + UI test |
| AC-WP03-05 | Test goods receipt: PO confirmed → stock.picking validated in NADF Main Warehouse → stock.move lines present | `env['stock.picking'].search([('state','=','done'),('purchase_id','!=',False)])` |
| AC-WP03-06 (= AC-14) | `mail.thread` audit: message history populated on both `purchase.request` and `purchase.order` after state transitions | UI: chatter section on test records |
| AC-WP03-07 | DEC-CONTRACT-001 logged with recommendation (OCA vs custom vs defer) | `docs/DECISION_LOG.md` |
| AC-WP03-08 (= AC-02) | All CA-02 Phase 1 deliverables delivered or formally BLOCKED with documented rationale; no Enterprise module used | Manual review + DB audit |

---

## 6. Risks

| ID | Risk | L | I | Mitigation |
|----|------|---|---|-----------|
| R-WP03-01 | `x_compliance_status` field created via shell is DB-only — not version-controlled; will not survive DB rebuild without re-running the shell command | Med | Med | Document the creation command in `IMPLEMENTATION_HISTORY.md`; add a `scripts/` helper; consider Phase 2 `nadf_vendor_compliance` module for a proper field definition |
| R-WP03-02 | Phase 3 demo POs (P00005, P00006 in `to_approve`) may interfere with approval workflow testing | Low | Low | Leave demo POs as-is; create new test PRs for WP-03 validation |
| R-WP03-03 | ₦500,000 PO approval threshold (Phase 3 legacy) may not match NADF-approved B-03 threshold | High | Med | Document as interim; flag to client for B-03 confirmation; do NOT change threshold without B-03 client sign-off |
| R-WP03-04 | `purchase_request` picking_type assignment may not default to NADF Main Warehouse "Receipts" | Low | Low | Set picking_type_id explicitly during configuration; verify before test |
| R-WP03-05 | "Call for Tender" requisition type award may not generate PO automatically if no vendor is selected | Low | Low | Test with 2 vendor lines; award explicitly before testing PO generation |
| R-WP03-06 | OCA `contract` module evaluation may surface a dependency conflict with existing `purchase_requisition` settings | Low | Low | Evaluation is read-only (no install in Phase 1); conflict risk is theoretical only |

---

## 7. Governance Reviews Required

| Reviewer | When | Scope |
|----------|------|-------|
| **G1 — Architecture & Odoo Governance** | Exit gate | compliance field approach (shell vs module); `purchase_request` configuration approach; CE-only compliance; OCA contract evaluation rationale |
| **G2 — Quality & Documentation Governance** | Exit gate | All deliverables evidenced; DEC-WP03-001 and DEC-CONTRACT-001 in `DECISION_LOG.md`; IMPLEMENTATION_HISTORY and CHANGELOG updated; WP03-07 BLOCKED status documented |
| **G3 — Security & Change Governance** | Exit gate | Procurement user group access model correct; no privilege escalation; `x_compliance_status` field not exposing PII; branch/PR discipline maintained |

---

## 8. Go/No-Go Checkpoint — **PASS (2026-06-25)**

System state verified by A1 Master Orchestrator via Odoo shell query (pre-WP-03, main@`e58e15c`).

| Check | Status | Evidence |
|-------|--------|---------|
| WP-01 exit gate CONDITIONAL PASS confirmed | ✅ | `IMPLEMENTATION_HISTORY.md` §WP-01; `WP_02_EXIT_GATE_REPORT.md` §1 |
| WP-02 exit gate CONDITIONAL PASS confirmed | ✅ | `docs/governance/WP_02_EXIT_GATE_REPORT.md` — CONDITIONAL PASS |
| Single Claude Code session confirmed | ✅ | One active session (PID confirmed via ps) |
| `purchase_request` state='installed' | ✅ | DB query: `state='installed'` |
| `purchase_requisition` state='installed' | ✅ | DB query: `state='installed'` (CE native) |
| `purchase` and `stock` installed | ✅ | Both confirmed installed |
| `mail.thread` on `purchase.request` | ✅ | `message_post` method present |
| `mail.thread` on `purchase.order` | ✅ | `message_post` method present |
| Branch created from protected main | ✅ | `feat/wp-03-procurement-core` from `e58e15c` |
| Working tree clean at branch creation | ✅ | `git status --short` = empty |
| Pre-work backup — plan confirmed | ⚠️ | Latest backup: `nadf_20260624_160329` (pre-WP-01). **New backup required before first mutating operation.** |
| No Enterprise modules in scope | ✅ | Scope is CE `purchase`, `stock`, OCA `purchase_request`; no Enterprise |
| WP03-07 blocker acknowledged | ✅ | B-02/B-03 client confirmation outstanding; WP03-07 will be documented as BLOCKED |
| ₦500K PO threshold documented | ✅ | Pre-existing Phase 3 config; client must confirm via B-03 before changing |

**G1 verdict:** GO — OCA `purchase_request` and CE `purchase_requisition` approach is architecturally sound. `x_compliance_status` via Odoo shell is acceptable for Phase 1 MVP (document creation command; revisit in Phase 2 custom module). OCA contract evaluation is read-only analysis only — no install authorised in Phase 1.

**G2 verdict:** GO — Deliverable set is complete and testable. WP03-07 BLOCKED status must be documented in IMPLEMENTATION_HISTORY before the PR is raised. DEC-CONTRACT-001 and DEC-WP03-001 are required entries.

**G3 verdict:** GO — Branch from protected main; pre-work backup planned; Procurement user groups exist from WP-01 (WP01-14); no privilege escalation risk in scope. Change confirmed: ₦500K approval threshold must not be changed without B-03 client sign-off — this is a write-protection constraint on that config parameter.

**Go/No-Go decision: GO** — D2 Solution Builder authorised to begin. First action: take pre-work backup.

---

## 9. Implementation Notes (for D2 Solution Builder)

### WP03-01 — Vendor compliance field

No custom compliance field exists on `res.partner` in the current NADF DB. Create via Odoo shell:

```python
env['ir.model.fields'].sudo().create({
    'model_id': env['ir.model'].search([('model','=','res.partner')]).id,
    'name': 'x_compliance_status',
    'field_description': 'Compliance Status',
    'ttype': 'selection',
    'selection': "[('compliant','Compliant'),('non_compliant','Non-Compliant'),('pending','Pending Review')]",
    'store': True,
})
env.cr.commit()
```

Tag at least 2 existing vendors (supplier_rank > 0) with `x_compliance_status = 'compliant'`. The `nadf_vendor_onboarding` `state='approved'` on `nadf.vendor.application` also serves as a compliance proxy — document this dual mechanism in DEC-WP03-001.

### WP03-02 / WP03-03 — purchase_request and purchase_requisition

- **purchase_request**: Set the default `picking_type_id` to the "Receipts" picking type (ID 1 from Go/No-Go check). In `purchase_request`, this is set at the purchase request line level. Test the full state machine.
- **purchase_requisition "Call for Tender"**: Create type via:
  ```python
  env['purchase.requisition.type'].create({
      'name': 'Call for Tender',
      'exclusive': 'exclusive',
      'quantity_copy': 'copy',
  })
  ```
  Then test: create a requisition → assign the type → send to 2 vendors → compare quotations → award → verify PO generated.

### WP03-04 — Goods receipt

Create a test PO (≥ 1 product line), confirm it, create the receipt (stock.picking auto-generated), validate the transfer. Verify `stock.move` lines show `state='done'`.

### WP03-05 — OCA contract evaluation

Do NOT install OCA `contract` module in Phase 1. Evaluation is a read-only assessment:
- Check OCA/contract@17.0 models: `contract.contract`, `contract.line`
- Assess whether NADF procurement contracts (per Transfer Package CA-02) need contract lifecycle management
- Compare to planned `nadf_legal_contract` custom module (Phase 2/3)
- Log recommendation in DEC-CONTRACT-001

### WP03-06 — mail.thread verification

Pre-confirmed by Go/No-Go (`message_post` present). Functional test: after state transitions on the test PR and test PO, verify the chatter shows automated state-change messages.

### WP03-07 — BLOCKED

Do not configure the multi-level approval chain. Document the current state:
- `purchase.purchase_order_approval = True` (enabled)
- `purchase.purchase_order_approval_min_amount = 500,000.00` (₦500K — Phase 3 legacy)
- Approver: The CE approval uses the "Purchase Manager" group as the approver for POs above threshold
- NADF RACI step 1.19 (B-02) has not been confirmed by client — the specific approver role chain is unknown
- B-03 threshold confirmation outstanding — ₦500K may change

**Constraint:** Do NOT change `purchase.purchase_order_approval_min_amount` until B-03 is confirmed by the Business Sponsor. Write-protect this parameter until then.

---

*Work package definition prepared 2026-06-25. Go/No-Go PASS recorded above (§8). Authority: PEG-6 approval 2026-06-24 · Transfer Package v2.1.*
