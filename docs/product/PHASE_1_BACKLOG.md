# Phase 1 — Foundation Backlog
## NADF ERP Programme

**Document type:** Phase planning — prioritised backlog
**Phase:** 1 — Foundation
**Authority:** `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` · parent backlog: `planning/BACKLOG.md`
**Prepared by:** A1 Master Orchestrator · D1 Functional Architect
**Date:** 2026-06-24
**Status:** PLANNING — implementation blocked until G1/G2/G3 Go/No-Go clearance

> This document is a Phase 1 view of `planning/BACKLOG.md`. It does not replace or duplicate the master backlog — it provides the Phase 1 implementation team with a focused, sequenced view of the items they are authorized to work on.

---

## Priority Classification
- **MH** Must Have — required for Phase 1 exit gate; implementation fails without it
- **SH** Should Have — important; Phase 1 incomplete without it but workaround possible
- **CH** Could Have — desirable; defer if time/session-count constrained

## Status Values
`Not Started` | `In Progress` | `Blocked` | `Done` | `Deferred`

---

## WP-01 — Foundation Hardening

| ID | Item | Priority | Status | Dependency | AC |
|----|------|---------|--------|-----------|-----|
| WP01-01 | Confirm single Claude Code session — no concurrent sessions | MH | Not Started | — | — |
| WP01-02 | Take pre-work backup of NADF database + filestore | MH | Not Started | WP01-01 | — |
| WP01-03 | Verify Odoo-17-CE compatibility for `mis_builder` | MH | Not Started | — | — |
| WP01-04 | Verify Odoo-17-CE compatibility for `account_budget_oca` | MH | Not Started | — | — |
| WP01-05 | Verify Odoo-17-CE compatibility for `purchase_request` | MH | Not Started | — | — |
| WP01-06 | Verify Odoo-17-CE compatibility for `purchase_requisition` | MH | Not Started | — | — |
| WP01-07 | Verify Odoo-17-CE compatibility for `helpdesk_mgmt` | MH | Not Started | — | — |
| WP01-08 | Install and version-pin `mis_builder`; log DEC entry | MH | Not Started | WP01-03 | AC-01 |
| WP01-09 | Install and version-pin `account_budget_oca`; log DEC entry | MH | Not Started | WP01-04 | AC-01 |
| WP01-10 | Install and version-pin `purchase_request`; log DEC entry | MH | Not Started | WP01-05 | AC-02 |
| WP01-11 | Install and version-pin `purchase_requisition`; log DEC entry | MH | Not Started | WP01-06 | AC-02 |
| WP01-12 | Install and version-pin `helpdesk_mgmt`; log DEC entry | MH | Not Started | WP01-07 | AC-04 |
| WP01-13 | Create Finance user groups (Officer, Manager, CFO, Auditor) | MH | Not Started | WP01-08…12 | AC-14 |
| WP01-14 | Create Procurement user groups (Requisitioner, Proc Officer, Proc Manager, Finance Approver) | MH | Not Started | WP01-08…12 | AC-14 |
| WP01-15 | Create HR user groups (Employee, Line Manager, HR Officer, HR Manager, CEO) | MH | Not Started | WP01-08…12 | AC-14 |
| WP01-16 | Create Administration user groups (Driver, Fleet Manager, Asset Manager, IT Officer, IT Manager) | MH | Not Started | WP01-08…12 | AC-14 |
| WP01-17 | Create Project Coord user groups (Team Member, Project Manager, Director, PCU Head) | MH | Not Started | WP01-08…12 | AC-14 |
| WP01-18 | Enable TOTP 2FA in Odoo settings | MH | Not Started | WP01-08…12 | AC-14 |
| WP01-19 | Enforce 2FA for Finance + Senior Management groups | MH | Not Started | WP01-18 | AC-14 |
| WP01-20 | Run `--stop-after-init` exit-0 check after OCA installs | MH | Not Started | WP01-08…12 | — |

---

## WP-02 — Finance Core

| ID | Item | Priority | Status | Dependency | AC |
|----|------|---------|--------|-----------|-----|
| WP02-01 | Re-validate legacy CoA (319 accounts) against NADF structure | MH | Not Started | WP01 done | AC-01 |
| WP02-02 | Export CoA as reference CSV; obtain client review record | MH | Not Started | WP02-01 | AC-01 |
| WP02-03 | Re-validate vendor-bill workflow (draft → confirmed → posted) | MH | Not Started | WP01 done | AC-01 |
| WP02-04 | Re-validate payment workflow; verify dual-auth restriction | MH | Not Started | WP01 done | AC-01 |
| WP02-05 | Test dual-authorisation with two user accounts | MH | Not Started | WP02-04 | AC-01 |
| WP02-06 | Configure analytic accounts aligned to NADF budget lines | MH | Not Started | WP01-09 | AC-01 |
| WP02-07 | Configure budget control via `account_budget_oca` | MH | Not Started | WP02-06 | AC-01 |
| WP02-08 | Confirm `mis_builder` KPI set with client; configure dashboard | SH | Not Started | WP01-08; client KPI sign-off | AC-01 |
| WP02-09 | Verify native financial reports (trial balance, P&L, balance sheet) | SH | Not Started | WP02-01 | AC-01 |
| WP02-10 | Verify `mail.thread` audit trail on `account.move` and `account.payment` | MH | Not Started | WP02-03 | AC-14 |
| WP02-11 | Verify WHT (41030102) and VAT (41030103) tax accounts; confirm with client before changes | MH | Not Started | WP02-01 | AC-01 |

---

## WP-03 — Procurement Core

| ID | Item | Priority | Status | Dependency | AC |
|----|------|---------|--------|-----------|-----|
| WP03-01 | Re-validate vendor compliance-status field on `res.partner` | MH | Not Started | WP01 done | AC-02 |
| WP03-02 | Configure and validate `purchase_request` multi-step requisition | MH | Not Started | WP01-10 | AC-02 |
| WP03-03 | Configure and validate `purchase_requisition` RFQ/tender workflow | MH | Not Started | WP01-11 | AC-02 |
| WP03-04 | Re-validate goods receipt and stock flow | MH | Not Started | WP01 done | AC-02 |
| WP03-05 | Evaluate OCA `contract` fit; log DEC-CONTRACT-001 | MH | Not Started | WP03-01 | — |
| WP03-06 | Verify `mail.thread` audit on `purchase.request` and `purchase.order` | MH | Not Started | WP03-02 | AC-14 |
| WP03-07 | Configure multi-level approval chain (WP-PROC-02) | MH | **Blocked** | B-02 + B-03 resolved by client | AC-02 |

---

## WP-04 — HR Core

| ID | Item | Priority | Status | Dependency | AC |
|----|------|---------|--------|-----------|-----|
| WP04-01 | Re-validate employee records with 4-level org hierarchy | MH | Not Started | WP01 done | AC-03 |
| WP04-02 | Refine department assignments (11 staff currently set to Administration) | SH | Not Started | WP04-01 | AC-03 |
| WP04-03 | Re-validate leave workflow (line manager → HR two-level) | MH | Not Started | WP01 done | AC-03 |
| WP04-04 | Re-validate recruitment pipeline stages | MH | Not Started | WP01 done | AC-03 |
| WP04-05 | Configure appointment/separation approval + CEO activity notification | MH | Not Started | WP04-01 | AC-03 |
| WP04-06 | Verify `mail.thread` audit on `hr.employee`, `hr.leave`, `hr.applicant` | MH | Not Started | WP04-01 | AC-14 |
| WP04-07 | Obtain client review record: leave types + org hierarchy | MH | Not Started | WP04-03 | AC-03 |
| WP04-08 | Set NADF company VAT/RC number (currently empty) | SH | Not Started | WP04-01 | — |
| WP04-09 | Set Claude API key in System Parameters for `nadf_vendor_onboarding` AI analysis | CH | Not Started | WP04-01 | — |

---

## WP-05 — UAT Preparation

| ID | Item | Priority | Status | Dependency | AC |
|----|------|---------|--------|-----------|-----|
| WP05-01 | Produce UAT test plan skeleton (one case per AC-01..05, AC-14) | MH | Not Started | WP02/03/04 done | D-5.1 |
| WP05-02 | Document UAT entry/exit criteria | MH | Not Started | WP05-01 | D-5.1 |
| WP05-03 | Prepare defect register template | MH | Not Started | WP05-01 | D-5.3 |
| WP05-04 | Produce UAT readiness checklist | SH | Not Started | WP05-01 | D-5.1 |

---

## Deferred / Out of Phase 1 Scope

| Item | Reason deferred | Target phase |
|------|----------------|-------------|
| `nadf_payroll_ng` spec + dev | Requires legal/HR advisory (E-01); no spec, no code | Phase 2/3 |
| `nadf_vendor_compliance` spec + dev | Phase 2 spec required | Phase 2/3 |
| `nadf_facility` spec + dev | Phase 2 spec required | Phase 2/3 |
| `nadf_legal_contract` spec + dev | Legal TO-BE P4–P6 pending (B-04A) | Phase 2/3 |
| `nadf_investment` spec + dev | Investment TO-BE + BRQ session (B-04E, E-03) | Phase 2/3 |
| `nadf_me_indicators` spec + dev | M&E TO-BE pending (B-04F) | Phase 2/3 |
| 7 remaining department builds | TO-BE-gated (B-04A…G) | Phase 3 |
| Cross-dept integration testing | Phase 4 | Phase 4 |
| UAT execution | Phase 5 | Phase 5 |
| Production deployment | Phase 6 | Phase 6 |
| Template extraction | Phase 7 | Phase 7 |

---

*Phase 1 backlog frozen at PEG-6 approval 2026-06-24. Scope changes require a new gate decision.*
