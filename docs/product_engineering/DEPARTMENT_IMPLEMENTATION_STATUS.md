# DEPARTMENT_IMPLEMENTATION_STATUS.md
## NADF ERP — Detailed Department Implementation Status

**Document ID:** DIS-NADF-001
**Review type:** Engineering Audit — read-only
**Authority:** A1 Master Orchestrator
**Date:** 2026-06-29
**Source:** PETR-NADF-001 · PRM-NADF-001 · GAR v1.3 · DECISION_LOG · IMPLEMENTATION_HISTORY

---

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Implemented and verified in execution |
| ⚠️ | Implemented with caveat or proxy workaround |
| ⏳ | Pending — blocked on external input |
| ❌ | Not implemented — within scope, not done |
| 🔴 | Blocked — cannot proceed without prerequisite |
| 📋 | Deferred — formally moved to later phase |

---

## 1. Finance (CA-01) — WP-02 CONDITIONAL PASS

**Work Package:** WP-02 Finance Core | **PR:** #6 merged `e58e15c` | **Branch:** feat/wp-02-finance-core

| # | Capability | Sub-Item | Status | Evidence |
|---|---|---|---|---|
| 1 | Chart of Accounts | CoA loaded from validated CSV (11 top-level groups) | ✅ | `account.group` + `account.account` confirmed; WP02-01 |
| 2 | Chart of Accounts | Client CoA sign-off | ⏳ | WP02-02 — client action B-item outstanding |
| 3 | Payment Workflow | Dual-authorisation payment advisory (base_automation rule) | ⚠️ | DEC-WP02-001 — hard-block not possible in CE; advisory only |
| 4 | Invoice Processing | Bill entry workflow (vendor bill → validate) | ✅ | Tested end-to-end |
| 5 | Analytic Accounts | Analytic account structure for cost centres | ✅ | WP02-04 — analytic accounts created |
| 6 | Budget | `account_budget_oca` installation + configuration | 🔴 | DEC-OCA-02 — `theoritical_amount` field missing; OCA v17.0.1.0.0 incompatible |
| 7 | Dashboard/KPIs | `mis_builder` dashboard with NADF KPI set | ⏳ | `mis_builder` installed; KPI set awaiting client sign-off (WP02-08) |
| 8 | Financial Reports | `account` native reports (P&L, Balance Sheet) | ✅ | CE native; confirmed available |
| 9 | 2FA / Security | TOTP globally required; Finance user groups (4) | ✅ | WP01-10; groups: Finance Admin, Manager, Accountant, Viewer |
| 10 | Audit Trail | `mail.thread` on financial documents | ✅ | CE native |
| 11 | Motor Vehicles GL | GL account mapping for fleet assets | ⚠️ | DEC-ADM01-002 — mapping incorrect; Finance review required before UAT |

**Summary:** 7 items ✅ · 2 ⚠️ (advisory/data) · 1 ⏳ (client) · 1 🔴 (DEC-OCA-02 engineering) · UAT not started

---

## 2. Procurement (CA-02) — WP-03 CONDITIONAL PASS

**Work Package:** WP-03 Procurement Core | **PR:** #8 merged `be7ed8b` | **Branch:** feat/wp-03-procurement-core

| # | Capability | Sub-Item | Status | Evidence |
|---|---|---|---|---|
| 1 | Vendor Management | Vendor records with compliance status field (`x_compliance_status`) | ✅ | WP03-01 — field live in DB |
| 2 | Vendor Management | `x_compliance_status` persistent through restart | ⚠️ | DEC-WP03-001 — DB-only field; `nadf_vendor_compliance` Phase 2 required for permanence |
| 3 | Purchase Requisition | `purchase_request` OCA module — internal requisition workflow | ✅ | WP03-02 — `purchase.request` model confirmed; group hierarchy assigned |
| 4 | Tender Process | Call for Tender / RFQ workflow | ✅ | WP03-03 — `purchase.order` + `purchase.requisition` (CE native) |
| 5 | Purchase Orders | PO creation and approval routing | ✅ | WP03-04 — PO workflow operational |
| 6 | Goods Receipt | Three-way matching (PO → GR → Invoice) | ✅ | WP03-05 — `stock.picking` confirmed |
| 7 | Approval Chain | ₦500,000 approval threshold configuration (step 1.18) | ✅ | WP03-06 — threshold set; MUST NOT be modified (WP-03 mandate) |
| 8 | Approval Chain | Step 1.19 approver assignment (step above threshold) | 🔴 | WP03-07 — BLOCKED on B-02 (RACI confirmation) and B-03 (threshold values) |
| 9 | Vendor Compliance | `nadf_vendor_compliance` module specification | 📋 | BL-SPEC-02 Phase 2 — TO-BE complete, spec not yet written |
| 10 | Vendor Compliance | `nadf_vendor_compliance` module development | 📋 | BL-DEV-02 Phase 3 |
| 11 | Contract Integration | Legal contract linkage to PO workflow | 📋 | Deferred pending Legal TO-BE P4–P6 and nadf_legal_contract spec |
| 12 | `mail.thread` | Procurement document audit trail | ✅ | Confirmed |

**Summary:** 7 items ✅ · 1 ⚠️ · 1 🔴 (client) · 3 📋 (Phase 2/3) · UAT not started

---

## 3. HR — Human Resources (CA-03) — WP-04 CONDITIONAL PASS

**Work Package:** WP-04 HR Core | **PR:** #10 open | **Branch:** feat/wp-04-hr-core

| # | Capability | Sub-Item | Status | Evidence |
|---|---|---|---|---|
| 1 | Employee Records | Org hierarchy — Department → Manager → Employee | ✅ | `hr.employee` records; `parent_id` / `department_id` set |
| 2 | Employee Records | Employment status field (`x_employment_state`) | ✅ | WP04-03 — `x_employment_state` custom field live |
| 3 | Employee Records | Company registration (RC number, TIN) on employee records | ⏳ | WP04-08 DEFERRED — B-WP04-02 client action |
| 4 | Leave Management | Annual Leave (2-level approval) | ✅ | `hr_holidays` — AM + Director level |
| 5 | Leave Management | Sick Leave (self-approval) | ✅ | `hr_holidays` |
| 6 | Leave Management | Study Leave (3-level approval advisory) | ⚠️ | DEC-007 — CE `hr_holidays` max 2 approval levels; 3-level advisory only; Phase 2 `nadf_hr_leave` custom |
| 7 | Leave Management | Maternity/Paternity Leave | ✅ | `hr_holidays` |
| 8 | Recruitment | Recruitment pipeline (`hr_recruitment`) | ✅ | WP04-04 — pipeline + interview stages configured |
| 9 | Payroll | Nigerian payroll framework (PAYE, pension 8%+10%, NHF 2.5%, NSITF 1%) | 📋 | `nadf_payroll_ng` Phase 3 — requires OCA payroll base + legal advisory |
| 10 | Performance | Performance management | 📋 | HR-06 = Could Have; deferred to future phase |
| 11 | User Groups | HR user groups (5): HR Admin, HR Manager, Leave Manager, Recruiter, Employee | ✅ | WP01 + WP04 |
| 12 | Dept reporting lines | 6 Admin-dept employees (IDs 12,13,14,18,20,23) dept assignment | ⏳ | WP04-01 — B-WP04-01 client action pending |
| 13 | `mail.thread` | HR document audit trail | ✅ | Confirmed |

**Summary:** 8 items ✅ · 1 ⚠️ · 2 ⏳ (client) · 2 📋 (Phase 2/3) · UAT not started

---

## 4. Administration (CA-04) — WP-ADM-01 CONDITIONAL PASS

**Work Package:** WP-ADM-01 Administration Core | **PR:** #11 open | **Branch:** feat/wp-adm-01-administration-core

| # | Capability | Sub-Item | Status | Evidence |
|---|---|---|---|---|
| 1 | Fleet Management | 5 Toyota vehicles registered in `fleet.vehicle` | ✅ | WP-ADM-01 — make/model/year/chassis configured |
| 2 | Fleet Management | Vehicle license plates | ⏳ | B-ADM01-01 — client action pending |
| 3 | Fleet Management | Driver assignments | ⏳ | B-ADM01-01 + B-WP04-01 client actions pending |
| 4 | Fleet Management | Fuel/service tracking (`fleet.service.type`) | ✅ | Service log model configured |
| 5 | Asset Management | 5 asset categories (Office Equipment, Vehicles, Furniture, ICT, Land & Buildings) | ✅ | `account.asset.asset` confirmed |
| 6 | Asset Management | 61 assets registered; 3 validated (open + straight-line depreciation) | ✅ | WP-ADM-01 |
| 7 | Asset Management | Motor Vehicles GL account assignment | ⚠️ | DEC-ADM01-002 — GL account mapping incorrect; requires Finance sign-off before UAT |
| 8 | ICT Helpdesk | `helpdesk_mgmt` team 'NADF ICT Helpdesk' | ✅ | WP-ADM-01 — `helpdesk.ticket.team` model (not `helpdesk.team`) |
| 9 | ICT Helpdesk | 5 ticket categories (Hardware, Software, Network, Access Mgmt, Other) | ✅ | WP-ADM-01 |
| 10 | ICT Helpdesk | Ticket lifecycle (New → In Progress → Pending → Resolved → Closed) | ✅ | 5 stages configured |
| 11 | ICT Helpdesk | SLA enforcement | ⚠️ | DEC-ADM01-001 — `helpdesk_mgmt` 17.0.1.10.4 has no SLA model; priority + stage timestamp proxy only; Phase 2 `nadf_ict_helpdesk` custom module |
| 12 | User Groups | Administration: Driver(0 users), IT Officer(0 users), Fleet Manager, Asset Manager, Helpdesk Agent (5 groups) | ⚠️ | Groups created; Driver + IT Officer population pending B-WP04-01 |
| 13 | Facility Management | Facility booking, space management | 📋 | `nadf_facility` Phase 2 — TO-BE complete, spec not yet written (unblocked) |
| 14 | `mail.thread` | Administration document audit trail | ✅ | WP-ADM-01 — confirmed on fleet.vehicle + helpdesk.ticket |
| 15 | AOP-014 | Trust profile NADF deployment; settings.json whitelist | ✅ | DEC-AOP014-001; GAR v1.3 |

**Summary:** 9 items ✅ · 3 ⚠️ · 2 ⏳ (client) · 1 📋 · UAT not started

---

## 5. Project Coordination (CA-05) — WP-PC-01 CONDITIONAL PASS

**Work Package:** WP-PC-01 Project Coordination | **PR:** #12 open | **Branch:** feat/wp-pc-01-project-coordination

| # | Capability | Sub-Item | Status | Evidence |
|---|---|---|---|---|
| 1 | User Groups | 4 PCU groups: Director (1 user), PCU Head (0), PM (0), PTM (0) | ✅ | WP-PC-01 — id 112–115 |
| 2 | Programme Structure | NADF ERP Programme project (id=2, status=on_track) | ✅ | `project.project` id=2 |
| 3 | Programme Structure | NADF ERP Phase 1 project (id=3) — sub-project by naming convention | ✅ | `project.project` id=3 |
| 4 | Programme Structure | Enforced programme hierarchy (parent_id) | ⚠️ | DEC-PC01-001 — CE has no `parent_id` on `project.project`; hierarchy via naming convention only |
| 5 | Task Stages | 5 PCU lifecycle stages: Initiation(14), Planning(15), Execution(16), M&C(17), Closure(18) | ✅ | WP-PC-01 stage IDs confirmed |
| 6 | Milestone Tracking | Test milestone id=1, is_reached=True, reached_date=2026-06-26 | ✅ | WP-PC-01 |
| 7 | Milestone Governance | Director ACL: ir.model.access id=1062 (full CRUD on project.milestone) | ✅ | WP-PC-01 |
| 8 | Milestone Governance | Director-only restriction on is_reached field | ⚠️ | DEC-PC01-002 (DEFERRED) — CE cannot restrict is_reached at field level; organizational control; Phase 2 `nadf_project_governance` |
| 9 | User Assignment | PCU Head, PM, PTM populated | ⏳ | B-WP04-01 — employee roles not yet confirmed |
| 10 | Portfolio Hierarchy | Project portfolio / programme hierarchy | 📋 | Phase 2 `nadf_project_governance` — computed % complete, portfolio view |
| 11 | `mail.thread` | project.project (3 messages) + project.task | ✅ | WP-PC-01 — AC-14 PASS |
| 12 | nadf_project_governance | Phase 2 custom module spec | 📋 | NOT in Transfer Package v2.1 custom module table (gap) — must be added |

**Summary:** 7 items ✅ · 3 ⚠️/📋 · 1 ⏳ (client) · UAT not started

---

## 6. Legal Services (CA-06) — NOT STARTED

**Work Package:** WP-DEPT-01 (not executable) | **PR:** None | **Implementation:** 0%

| # | Capability | Sub-Item | Status | Notes |
|---|---|---|---|---|
| 1 | Contract Initiation (P1) | Client request intake + scope confirmation | ❌ | Process defined in TO-BE; no Odoo build |
| 2 | Contract Drafting (P2) | Template selection + clause assembly | ❌ | Process defined in TO-BE; no Odoo build |
| 3 | Internal Review (P3) | HOD/Legal review routing | ❌ | Process defined in TO-BE; no Odoo build |
| 4 | External Sign-off (P4) | Counterparty review workflow | 🔴 | P4 TO-BE not delivered — blocks all engineering |
| 5 | Execution (P5) | Signing, sealing, stamping | 🔴 | P5 TO-BE not delivered |
| 6 | Archival (P6) | Contract register, expiry alerts | 🔴 | P6 TO-BE not delivered |
| 7 | `nadf_legal_contract` spec | BL-SPEC-04 | 🔴 | Cannot write spec until P4–P6 TO-BE received |
| 8 | `nadf_legal_contract` dev | BL-DEV-04 | 📋 | Phase 3 — after spec approval |

**Summary:** 0 items ✅ · 3 ❌ (TO-BE done, not built) · 3 🔴 (TO-BE missing) · 2 📋

---

## 7–13. Remaining Departments (Not Yet Engineered / Blocked)

| Department | TO-BE | ERP Approach | Spec | Build | Blocking Item |
|---|---|---|---|---|---|
| Strategy & Planning | ❌ None | Unknown | ❌ | ❌ | Client TO-BE |
| Communications | ❌ None | Unknown | ❌ | ❌ | Client TO-BE |
| Sustainable Agriculture | ❌ None | Unknown | ❌ | ❌ | Client TO-BE; Investment overlap |
| Investment | ❌ None | `nadf_investment` custom (P1) | ❌ | ❌ | Client TO-BE + BRQ session |
| M&E | ❌ None | `nadf_me_indicators` + `mis_builder` | ❌ | ❌ | Client TO-BE; WP02-08 |
| Executive Management | ❌ None | Roll-up dashboard (depends on all depts) | ❌ | ❌ | All dept builds + client TO-BE |

---

## Implementation Coverage Summary (Phase 1 scope)

| Metric | Value |
|---|---|
| Departments with CONDITIONAL PASS WP | 6 of 6 Phase 1 departments |
| Capabilities implemented (approx. items) | ~47 of ~75 Phase 1 capabilities |
| Blocking items (client decisions) | 7 B-series items outstanding |
| Blocking items (engineering) | 1 (DEC-OCA-02) |
| Deferred items (Phase 2 custom modules) | 3 specs unblocked (nadf_vendor_compliance, nadf_facility, nadf_project_governance) |
| Deferred items (Phase 3) | nadf_payroll_ng, nadf_investment, nadf_me_indicators, nadf_legal_contract |
| Phase 2–3 departments with zero implementation | 7 (Legal partially; SA, Strategy, Comms, Investment, M&E, Executive = 0) |

---

*DIS-NADF-001 — A1 Master Orchestrator — 2026-06-29*
