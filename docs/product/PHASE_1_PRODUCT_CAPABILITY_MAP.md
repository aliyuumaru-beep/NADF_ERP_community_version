# Phase 1 — Product Capability Map
## NADF ERP Programme

**Document type:** Phase planning — capability coverage map
**Phase:** 1 — Foundation
**Authority:** `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (frozen at PEG-6 approval 2026-06-24)
**Prepared by:** A1 Master Orchestrator · D1 Functional Architect
**Date:** 2026-06-24
**Status:** PLANNING — no implementation yet

> Phase 1 scope is bounded to CE-native configuration and vetted OCA installation.
> No custom module development, no unspecified departments. Scope frozen at Transfer Package v2.1.

---

## 1. Capability Coverage Summary

| Capability Area | Department | Phase 1 Coverage | Phase 1 Work Package | Full Acceptance Criterion |
|----------------|-----------|-----------------|----------------------|--------------------------|
| **CA-01** Financial Management | Finance | ✅ In scope — full foundation | WP-02 | AC-01 |
| **CA-02** Procurement Management | Procurement | ✅ In scope — pipeline (approval chain deferred) | WP-03 | AC-02 (partial) |
| **CA-03** Human Resource Management | HR | ✅ In scope — core (payroll deferred) | WP-04 | AC-03 (partial) |
| **CA-04** Administration & Facilities | Administration | ✅ In scope — fleet, assets, helpdesk | WP-01 / foundation | AC-04 (facility module deferred) |
| **CA-05** Project & Programme Management | Project Coord. | ✅ In scope — project structure + milestone gate | WP-01 / foundation | AC-05 |
| **CA-06** Legal & Contract Management | Legal Services | ❌ Deferred — Legal TO-BE P4–P6 pending (B-04A) | — | AC-06 |
| **CA-07** Strategy & Planning | Strategy | ❌ Deferred — TO-BE pending (B-04B) | — | AC-07 |
| **CA-08** Communications | Communications | ❌ Deferred — TO-BE pending (B-04C) | — | AC-08 |
| **CA-09** Agriculture Programme | Sust. Agriculture | ❌ Deferred — TO-BE pending (B-04D) | — | AC-09 |
| **CA-10** Investment & Loan Portfolio | Investment | ❌ Deferred — TO-BE + BRQ session pending (B-04E) | — | AC-10 |
| **CA-11** Monitoring & Evaluation | M&E | ❌ Deferred — TO-BE pending (B-04F) | — | AC-11 |
| **CA-12** Executive Management | Executive | ❌ Deferred — TO-BE pending (B-04G) | — | AC-12 |
| **CA-13** Cross-functional Workflows | All | ⏳ Foundation only — cross-dept integrations Phase 4 | — | AC-13 |
| **CA-14** Security & Access Control | All | ✅ In scope — Phase 1 groups, TOTP 2FA | WP-01 + per-WP | AC-14 (Phase 1) |

---

## 2. Phase 1 Capability Detail

### CA-01 — Financial Management (WP-02)
**Modules:** CE `account` · OCA `account_budget_oca` · OCA `mis_builder`
**Deliverables:**
- Government chart of accounts (NADF 8-digit structure, 319 accounts) — re-validate legacy CoA
- Vendor bill workflow (draft → confirmed → posted)
- Payment workflow with dual-authorisation (Finance Manager group restriction)
- Analytic accounts aligned to NADF budget lines
- Budget control via `account_budget_oca`
- Executive financial dashboard via `mis_builder` (KPI set — client sign-off required)
- Native financial reports: trial balance, P&L, balance sheet
- `mail.thread` audit trail on `account.move` and `account.payment`

**Deferred out of Phase 1:** Budget module full configuration (CSV ready at `csv_templates/nadf_budget_fy2026.csv` — loaded in WP-02 budget sub-task); WHT/VAT tax rules reviewed but not changed until client confirms.

---

### CA-02 — Procurement Management (WP-03)
**Modules:** CE `purchase` · CE `stock` · OCA `purchase_request` · OCA `purchase_requisition`
**Deliverables:**
- Vendor record structure with compliance status field (custom selection on `res.partner`)
- Structured multi-step requisition via `purchase_request`
- RFQ and tender workflow via `purchase_requisition`
- Goods receipt and stock flow
- `mail.thread` audit on `purchase.request` and `purchase.order`
- DEC-CONTRACT-001 logged (OCA `contract` fit assessment)

**Deferred out of Phase 1 (blocked):** Multi-level approval chain (WP-PROC-02) — blocked on B-02 (RACI step 1.19) and B-03 (threshold values) — client confirmation required.

---

### CA-03 — Human Resource Management (WP-04)
**Modules:** CE `hr` · CE `hr_holidays` · CE `hr_recruitment`
**Deliverables:**
- Employee records with NADF 4-level org hierarchy (MD → Director → Manager → Officer)
- Leave request and approval workflow (line manager → HR two-level)
- Recruitment pipeline (vacancy → shortlist → interview → offer → appointment)
- Appointment/separation approval state on `hr.employee` with CEO activity notification
- `mail.thread` audit on `hr.employee`, `hr.leave`, `hr.applicant`

**Deferred out of Phase 1:** Nigerian statutory payroll (`nadf_payroll_ng`) — requires Phase 2 spec + legal/HR advisory (E-01); performance management (BL-HR-06) — Could Have, deferred.

---

### CA-04 — Administration & Facilities (Phase 1 foundation component)
**Modules:** CE `fleet` · CE `account_asset` · OCA `helpdesk_mgmt`
**Deliverables:** Re-validate legacy: vehicle register + fuel log; asset register + depreciation; `helpdesk_mgmt` ICT ticketing (replaces unratified `project`-based workaround).
**Deferred:** `nadf_facility` custom module — Phase 2 spec, Phase 3 development.

---

### CA-05 — Project & Programme Management (Phase 1 foundation component)
**Module:** CE `project`
**Deliverables:** Project record with 5-phase structure (Initiation → Planning → Execution → M&C → Closure); milestone sign-off restricted to Director group; project status dashboard view.

---

### CA-14 — Security & Access Control (WP-01 + per-WP)
**Deliverables:** User groups for each Phase 1 department; TOTP 2FA enforced for Finance and Senior Management; `mail.thread` audit coverage verified across all Phase 1 modules.

---

## 3. OCA Module Enablement (WP-01)

| Module | Purpose | Capability | Compatibility check |
|--------|---------|-----------|---------------------|
| `mis_builder` | Executive + operational dashboards | CA-01, CA-11, CA-12 | Required before install |
| `account_budget_oca` | Richer budget control vs analytic accounts | CA-01 | Required before install |
| `purchase_request` | Structured multi-step procurement requisition | CA-02 | Required before install |
| `purchase_requisition` | Call for tenders / vendor comparison | CA-02 | Required before install |
| `helpdesk_mgmt` | ICT helpdesk (replaces EE-only `helpdesk`) | CA-04 | Required before install |

All five: Odoo-17-CE-compatibility verified → installed → version-pinned → logged in `docs/DECISION_LOG.md` before any dependent WP begins.

---

## 4. What Phase 1 Does Not Cover

- Custom module development (Phase 2 spec, Phase 3 dev — "no spec, no code")
- 7 remaining department builds (CA-06…CA-12 — all TO-BE-gated)
- Cross-department integration testing (Phase 4)
- UAT execution (Phase 5)
- Production deployment (Phase 6)
- Template extraction (Phase 7)
- Enterprise modules (permanently prohibited)

---

*Frozen at PEG-6 approval 2026-06-24. Scope changes require a new gate decision. Authority: Transfer Package v2.1.*
