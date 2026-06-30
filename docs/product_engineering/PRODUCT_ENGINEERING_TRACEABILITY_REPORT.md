# PRODUCT_ENGINEERING_TRACEABILITY_REPORT.md
## NADF ERP — Full Product Engineering Traceability Review

**Document ID:** PETR-NADF-001
**Review type:** Engineering Audit — read-only traceability assessment
**Authority:** A1 Master Orchestrator
**Date:** 2026-06-29
**Sources validated:** Transfer Package v2.1 · PRODUCT_SCOPE · BACKLOG · WORK_PACKAGES · ROADMAP · GAR (v1.3) · DECISION_LOG · IMPLEMENTATION_HISTORY · All WP execution files

> This is an engineering audit, not a governance audit. Its purpose is to determine exactly where each department capability sits within the Software Factory lifecycle and what remains before implementation can complete.

---

## Traceability Key

| Code | Meaning |
|------|---------|
| C | Complete — fully defined/executed |
| P | Partial — exists but incomplete |
| M | Missing — not yet produced |
| CP | Conditional Pass — executed with deferred items |
| NS | Not Started |
| BLK | Blocked — dependent on external input |

---

## 1. EXECUTIVE MANAGEMENT (CA-12)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **M** | TO-BE not delivered. No process documentation exists for executive dashboard, approval visibility, or cross-department KPI governance. |
| Refined TO-BE | **M** | No TO-BE received. |
| ERP Mapping | **P** | Tentative: `mis_builder` (OCA, already installed) + custom roll-ups. Dependency on all department builds completing before KPI set can be confirmed. |
| Capability Definition | **P** | Transfer Package §3.12: cross-department KPI roll-up dashboard; executive-level approval views. Sub-capabilities listed at high level only; no detailed data model. |
| Product Scope Coverage | **P** | In scope (BL-EXEC-01, Phase 3). No sub-items defined beyond the top-level backlog entry. |
| Product Package | **M** | No design spec, no WP with acceptance criteria. Transfer Package §3.12 is a placeholder. |
| Work Package Definition | **P** | WP-DEPT-07 placeholder defined in WORK_PACKAGES. No acceptance criteria, no deliverables list. |
| Implementation | **NS** | Not started. |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. Executive Management TO-BE — not delivered (blocks all downstream)
2. All department Phase 3 builds must complete before the executive roll-up dashboard is meaningful
3. `mis_builder` KPI set sign-off (ESC-CLIENT-WP02-08 — open escalation)
4. `nadf_me_indicators` must be complete before M&E KPIs feed the executive dashboard

### Implementation Readiness: NOT YET ENGINEERED

**Justification:** No TO-BE, no product package, no design spec. The ERP approach is tentative and the capability cannot be defined in isolation — it depends on all other department builds completing.

**Recommendation:** Defer specification until Phase 3 architecture is established. Obtain client confirmation on executive dashboard requirements alongside M&E and Investment TO-BE delivery.

---

## 2. FINANCE (CA-01)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **C** | 7 processes fully documented. TO-BE complete. |
| Refined TO-BE | **C** | Transfer Package §3.1 complete. Finance processes mapped to Odoo flows. |
| ERP Mapping | **C** | CE: `account`, `account_payment`. OCA: `account_budget_oca` (DEC-OCA-02 — blocked), `mis_builder` (installed). Custom: none required. |
| Capability Definition | **C** | CA-01 fully mapped: CoA, payments, bills, budget, reports, dashboard, 2FA, audit trail. |
| Product Scope Coverage | **C** | BL-FIN-01 through BL-FIN-09 fully defined. Phase 1. |
| Product Package | **C** | Transfer Package §3.1 complete. WP-FIN-01/02/03 defined with acceptance criteria. |
| Work Package Definition | **C** | WP-FIN-01 (core config) + WP-FIN-02 (budget + dashboard) + WP-FIN-03 (security). All have acceptance criteria. WP-FIN-02 is blocked by DEC-OCA-02. |
| Implementation | **CP** | WP-02 CONDITIONAL PASS (PR #6 merged `e58e15c`). Exit gate 9/11. WP02-07 (budget) blocked; WP02-08 (dashboard) deferred client. |
| Testing | **NS** | WP-05 UAT not yet started. |

### Outstanding Dependencies

1. **DEC-OCA-02** — `account_budget_oca` incompatibility blocks WP02-07 (budget configuration). G1/G2/G3 must choose Option A/B/C.
2. **ESC-CLIENT-WP02-08** — `mis_builder` KPI dashboard deferred pending client KPI sign-off
3. **WP02-02** — Client CoA CSV sign-off outstanding
4. Motor Vehicles GL account correction (DEC-ADM01-002) affects Finance; requires Finance review

### Implementation Readiness: PARTIALLY READY

**Justification:** Core Finance (CoA, bills, payments, analytic accounts, reports, 2FA, user groups) is CONDITIONAL PASS. Two items blocked: budget module (DEC-OCA-02 — engineering dependency) and dashboard (client decision). Core is production-capable pending UAT.

**Recommendation:** Proceed directly to DEC-OCA-02 resolution (Wave C). Dashboard pending client. Budget follows DEC-OCA-02 outcome.

---

## 3. PROCUREMENT (CA-02)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **C** | 6 processes documented. 2 open queries (RACI step 1.19 B-02; threshold values B-03). Core processes complete. |
| Refined TO-BE | **C** | Transfer Package §3.2 complete. OCA module fit analysis done (DEC-CONTRACT-001, DEC-OCA-03/04/05). |
| ERP Mapping | **C** | CE: `purchase`, `stock`. OCA: `purchase_request`, `purchase_requisition` (CE native in 17). Custom: `nadf_vendor_compliance` (Phase 2), `nadf_legal_contract` (deferred). |
| Capability Definition | **C** | CA-02 fully mapped: vendor mgmt, requisitions, tenders, POs, vendor evaluation, contracts, approval chain. |
| Product Scope Coverage | **C** | BL-PROC-01 through BL-PROC-09 + BL-SPEC-02 + BL-DEV-02 defined. |
| Product Package | **C** | Transfer Package §3.2 complete. WP-PROC-01/02 defined; WP-SPEC-02 defined. |
| Work Package Definition | **C** | WP-PROC-01 (executed), WP-PROC-02 (blocked on B-02/B-03), WP-SPEC-02 (nadf_vendor_compliance spec — unblocked). |
| Implementation | **CP** | WP-03 CONDITIONAL PASS (PR #8 merged `be7ed8b`). Exit gate 6/7. WP03-07 BLOCKED. |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. **B-02** — RACI step 1.19 approver identity confirmation (blocks WP03-07 approval chain)
2. **B-03** — PO threshold values (₦500K threshold write-protected; must not change without B-03)
3. **nadf_vendor_compliance** — Phase 2 spec required (BL-SPEC-02 unblocked since TO-BE complete)
4. `x_compliance_status` field is DB-only shell (DEC-WP03-001) — survives only if DB intact; Phase 2 module required

### Implementation Readiness: PARTIALLY READY

**Justification:** Core procurement flow (vendor records, purchase_request, tender, goods receipt, mail.thread) is CONDITIONAL PASS. Approval chain (WP03-07) is hard-blocked on client. `nadf_vendor_compliance` spec can begin immediately.

**Recommendation:** Prepare nadf_vendor_compliance specification now (Phase 2, unblocked). Obtain B-02/B-03 client clarification to unblock WP03-07.

---

## 4. HR — Human Resources (CA-03)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **C** | 8 processes documented. Payroll explicitly excluded to Phase 3. Performance management deferred to future phase. |
| Refined TO-BE | **C** | Transfer Package §3.3 complete. Nigerian statutory payroll requirement confirmed (PAYE, pension 8%+10%, NHF 2.5%, NSITF 1%). |
| ERP Mapping | **C** | CE: `hr`, `hr_holidays`, `hr_recruitment`. OCA: OCA payroll base (Phase 3). Custom: `nadf_payroll_ng` (confirmed required). |
| Capability Definition | **C** | CA-03 mapped: employee records, leave, recruitment, payroll, performance (deferred). |
| Product Scope Coverage | **C** | BL-HR-01 through BL-HR-06 + BL-SPEC-01 + BL-OCA-07 + BL-DEV-01 defined. |
| Product Package | **C** | Transfer Package §3.3 complete. WP-HR-01 + WP-SPEC-01 defined with acceptance criteria. |
| Work Package Definition | **C** | WP-HR-01 (executed), WP-SPEC-01 (nadf_payroll_ng spec — Phase 2), WP-DEV-01 (Phase 3). |
| Implementation | **CP** | WP-04 CONDITIONAL PASS (PR #10 open). HR core config complete; payroll excluded. |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. **B-WP04-01** — 6 Admin-dept employees (IDs 12,13,14,18,20,23) reporting line confirmation — blocks Driver/IT Officer groups, fleet driver assignments, PCU group population
2. **B-WP04-02** — NADF RC number and TIN (company registration)
3. **nadf_payroll_ng** — Nigerian payroll legal input required before spec can be finalized; OCA payroll base must be installed before development
4. **DEC-007** — Study Leave 3-level approval advisory only (CE limitation); technical fix deferred
5. **Performance management** — formally deferred to future phase (HR-06 = Could Have)

### Implementation Readiness: PARTIALLY READY

**Justification:** HR Core (org hierarchy, leave workflow, recruitment) is CONDITIONAL PASS. Payroll is Phase 3 — correctly deferred. Phase 1 HR is production-capable pending B-WP04-01/02 resolution and UAT.

**Recommendation:** Prepare nadf_payroll_ng specification (requires Nigerian payroll legal advisory input). Obtain B-WP04-01/02 from client.

---

## 5. ADMINISTRATION (CA-04) — including ICT Helpdesk

### Note on ICT
ICT is not a separate department build in the Transfer Package. ICT helpdesk capability (CA-04) is implemented as part of Administration via OCA `helpdesk_mgmt`. The GAR "ICT" department column tracks platform and module decisions (DEC-OCA-xx, DEC-2FA-xx, DEC-ADM01-xx), not a separate departmental Odoo build.

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **C** | Fleet management, asset management, ICT helpdesk — all TO-BE complete. Facility management deferred (no CE/OCA fit). |
| Refined TO-BE | **C** | Transfer Package §3.4 complete. ICT helpdesk explicitly mapped to `helpdesk_mgmt` (native `helpdesk` is EE-only). |
| ERP Mapping | **C** | CE: `fleet`, `account_asset` (model: `account.asset.asset`). OCA: `helpdesk_mgmt` 17.0.1.10.4. Custom: `nadf_facility` (Phase 2 spec, unblocked). |
| Capability Definition | **C** | CA-04 fully mapped: fleet, assets, ICT helpdesk, fuel tracking, facility (deferred). |
| Product Scope Coverage | **C** | BL-ADM-01 through BL-ADM-04 + BL-SPEC-03 + BL-DEV-03 defined. |
| Product Package | **C** | Transfer Package §3.4 complete. WP-ADM-01 + WP-SPEC-03 defined. |
| Work Package Definition | **C** | WP-ADM-01 (executed), WP-SPEC-03 (nadf_facility spec — Phase 2, unblocked). |
| Implementation | **CP** | WP-ADM-01 CONDITIONAL PASS (PR #11 open). Fleet ✅, assets ✅, helpdesk ✅, mail.thread ✅. 4 items deferred. |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. **B-ADM01-01** — Vehicle license plates + driver assignments
2. **B-WP04-01** — Driver and IT Officer group population blocked on employee role confirmation
3. **DEC-ADM01-001** — `helpdesk_mgmt` has no SLA model; priority + stage timestamp proxy only; SLA enforcement deferred to Phase 2
4. **DEC-ADM01-002** — Motor Vehicles GL account mapping incorrect; Finance review required
5. **nadf_facility** — Spec can begin (Administration TO-BE complete); Phase 2

### Implementation Readiness: PARTIALLY READY

**Justification:** Fleet, asset register, and ICT helpdesk are CONDITIONAL PASS. Facility management is correctly deferred to Phase 2 (no CE/OCA fit). Administration user groups are partially populated (Driver/IT Officer pending B-WP04-01). GL account correction (DEC-ADM01-002) is a data integrity risk requiring Finance sign-off.

**Recommendation:** Prepare nadf_facility specification now (TO-BE complete, unblocked). Resolve B-ADM01-01 and B-WP04-01 to complete user group population. Raise DEC-ADM01-002 GL correction with Finance before UAT.

---

## 6. PROJECT COORDINATION (CA-05)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **C** | 5 processes: project initiation, planning, execution, monitoring, closure. TO-BE complete. |
| Refined TO-BE | **C** | Transfer Package §3.5 complete. CE `project` confirmed sufficient for Phase 1 scope. |
| ERP Mapping | **C** | CE: `project` only. No OCA or custom module required for Phase 1. Phase 2: `nadf_project_governance` (emerged from execution — not in Transfer Package v2.1 custom module table). |
| Capability Definition | **C** | CA-05 mapped: project/task management, milestone tracking, phase gate approvals. |
| Product Scope Coverage | **C** | BL-PC-01 through BL-PC-04 defined. |
| Product Package | **C** | Transfer Package §3.5 complete. WP-PC-01 defined with acceptance criteria. |
| Work Package Definition | **C** | WP-PC-01 executed. |
| Implementation | **CP** | WP-PC-01 CONDITIONAL PASS (PR #12 open). 7 PASS · 4 DEFERRED · 0 FAIL. |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. **B-WP04-01** — PCU Head, PM, PTM user assignments pending employee role confirmation
2. **DEC-PC01-002** — Director-only milestone restriction is organizational only; technical enforcement deferred to `nadf_project_governance` Phase 2
3. **DEC-PC01-001** — Programme hierarchy via naming convention (no `parent_id` on `project.project` in CE 17)
4. **nadf_project_governance** — Phase 2 custom module required for: (a) Director-only milestone restriction, (b) project portfolio hierarchy, (c) % complete computed field — NOT in Transfer Package v2.1 custom module table; must be added

### Implementation Readiness: PARTIALLY READY

**Justification:** Project structure, 5 lifecycle stages, milestone tracking, and user groups are CONDITIONAL PASS. Phase 2 custom module required for governance-enforcement features. Phase 1 PCU oversight is operational pending user assignment.

**Recommendation:** Add `nadf_project_governance` to the custom module table in Transfer Package v2.1 (gap identified). Proceed to Wave C UAT preparation. Prepare nadf_project_governance spec in Phase 2.

---

## 7. LEGAL SERVICES (CA-06)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **P** | 6 processes total. P1–P3 (contract initiation, drafting, internal review) are complete. P4–P6 (external sign-off, execution, archival) are missing. |
| Refined TO-BE | **P** | Transfer Package §3.6 partial. P4–P6 not yet delivered by Claude Desktop. |
| ERP Mapping | **P** | Custom: `nadf_legal_contract` confirmed as required (DEC-CONTRACT-001 — OCA `contract` evaluated and rejected as insufficient for NADF RACI structure). No CE equivalent. |
| Capability Definition | **P** | High-level: contract lifecycle, sign-off workflow, contract register, expiry alerting. Data model not yet defined (blocked on P4–P6). |
| Product Scope Coverage | **P** | BL-SPEC-04, BL-DEV-04, BL-LSU-01, BL-LSU-02 defined in backlog but none can proceed. |
| Product Package | **P** | Transfer Package §3.6 has framework only. No design spec (`docs/modules/nadf_legal_contract_spec.md` does not exist). |
| Work Package Definition | **P** | WP-SPEC-04 (spec), WP-DEV-04 (dev), WP-DEPT-01 (LSU build) defined as placeholders; none have executable acceptance criteria. |
| Implementation | **NS** | Not started. |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. **Legal TO-BE P4–P6** — must be delivered before any spec or build work
2. **nadf_legal_contract design spec** — BL-SPEC-04; Phase 2; gated on TO-BE P4–P6
3. **nadf_legal_contract module development** — BL-DEV-04; Phase 3
4. **Legal Services Unit Odoo build** — BL-LSU-01; Phase 3
5. DEC-CONTRACT-001 (OCA `contract` rejected) — custom module is the only path

### Gap Type

- **Business Gap:** TO-BE P4–P6 missing (external party sign-off, execution mechanics, archival procedure)
- **Engineering Gap:** Design spec not written; data model not defined

### Implementation Readiness: BLOCKED

**Justification:** Legal TO-BE P4–P6 are the minimum prerequisite for writing the design spec. Without the TO-BE, the contract sign-off chain and data model cannot be defined. Custom module development cannot begin without an approved spec.

**Recommendation:** Obtain client clarification on Legal processes P4–P6. Once delivered, prepare `nadf_legal_contract` specification immediately (Phase 2).

---

## 8. STRATEGY & PLANNING (CA-07)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **M** | TO-BE not delivered. No process documentation. |
| Refined TO-BE | **M** | Not delivered. |
| ERP Mapping | **M** | Tentative only: `project` module repurposed. Actual approach requires TO-BE. |
| Capability Definition | **M** | No sub-capability entries in Transfer Package §6 Capability Map. |
| Product Scope Coverage | **P** | BL-STR-01 exists in Phase 3 backlog as a single line item. No sub-items. |
| Product Package | **M** | No design spec, no acceptance criteria, no data model. |
| Work Package Definition | **P** | WP-DEPT-02 placeholder in WORK_PACKAGES. No content. |
| Implementation | **NS** | Not started. |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. **Strategy & Planning TO-BE** — complete and entire chain blocked on delivery
2. **ERP module approach decision** — cannot be made without TO-BE
3. **Custom module assessment** — unknown until TO-BE delivered

### Implementation Readiness: NOT YET ENGINEERED

**Justification:** Zero product engineering has been completed for Strategy & Planning. No TO-BE, no capability definition, no spec. Cannot be estimated, scoped, or built.

**Recommendation:** Obtain Strategy & Planning TO-BE from client/Claude Desktop. All engineering follows.

---

## 9. COMMUNICATIONS (CA-08)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **M** | TO-BE not delivered. |
| Refined TO-BE | **M** | Not delivered. |
| ERP Mapping | **M** | No approach confirmed. Tentative: `helpdesk_mgmt` or `project` repurposed. |
| Capability Definition | **M** | No sub-capability entries in Transfer Package §6 Capability Map. |
| Product Scope Coverage | **P** | BL-COM-01 in Phase 3 backlog as a single item. |
| Product Package | **M** | No design spec or acceptance criteria. |
| Work Package Definition | **P** | WP-DEPT-03 placeholder only. |
| Implementation | **NS** | Not started. |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. **Communications TO-BE** — entirely blocks the chain
2. **ERP approach determination** — unknown; likely overlap with helpdesk_mgmt or a simple project structure

### Implementation Readiness: NOT YET ENGINEERED

**Recommendation:** Obtain Communications TO-BE. Assess overlap with Administration (helpdesk_mgmt) before creating a separate module or configuration.

---

## 10. SUSTAINABLE AGRICULTURE (CA-09)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **M** | TO-BE not delivered. |
| Refined TO-BE | **M** | Not delivered. |
| ERP Mapping | **M** | Transfer Package §3.8 notes possible overlap with Investment module (grant disbursement pattern is reusable). |
| Capability Definition | **M** | No sub-capability entries in §6 Capability Map for Sustainable Agriculture. |
| Product Scope Coverage | **P** | BL-SA-01 in Phase 3 backlog as a single item. Note: assess investment overlap before beginning build. |
| Product Package | **M** | No design spec or acceptance criteria. |
| Work Package Definition | **P** | WP-DEPT-04 placeholder only. |
| Implementation | **NS** | Not started. |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. **Sustainable Agriculture TO-BE** — entirely blocks the chain
2. **Investment module completion** — must assess `nadf_investment` reuse potential before SA build
3. **Grant disbursement pattern** — Transfer Package §7 flags this as a reusable asset

### Implementation Readiness: NOT YET ENGINEERED

**Recommendation:** Obtain SA TO-BE. Defer build definition until `nadf_investment` scope is confirmed to understand reuse opportunity. Do not create a separate custom module if `nadf_investment` covers the grant disbursement pattern.

---

## 11. INVESTMENT (CA-10)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **M** | TO-BE not delivered. A client BRQ session with Investment department is required. |
| Refined TO-BE | **M** | Not delivered. |
| ERP Mapping | **P** | Transfer Package §3.10: `nadf_investment` custom module confirmed as required (no CE/OCA equivalent). Sub-capabilities defined at high level: loan origination, credit appraisal, disbursement scheduling, repayment tracking, portfolio reporting. |
| Capability Definition | **P** | High-level sub-capabilities in §6: loan origination (Custom), disbursement scheduling (Custom), repayment tracking (Custom), portfolio reporting (Custom + `mis_builder`). No data model. |
| Product Scope Coverage | **P** | BL-INV-01, BL-SPEC-05, BL-DEV-05 defined. |
| Product Package | **P** | Transfer Package §3.10 has framework and confirms `nadf_investment` is required with Priority P1. No design spec exists. |
| Work Package Definition | **P** | WP-SPEC-05 (spec) and WP-DEV-05 (dev) defined as placeholders; WP-DEPT-05 defined; none executable. |
| Implementation | **NS** | Not started. |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. **Investment TO-BE** — entire engineering chain blocked
2. **BRQ session** with NADF Investment department — required before spec can be written
3. **nadf_investment design spec** — BL-SPEC-05; Priority P1; gated on TO-BE
4. **nadf_investment development** — BL-DEV-05; Priority P1; gated on spec approval
5. Integration with Finance (disbursement → payment chain) — BL-INT-04

### Implementation Readiness: BLOCKED

**Justification:** `nadf_investment` is correctly identified as the highest-priority remaining custom module (P1). The capability definition and ERP approach are partially complete but no engineering work can proceed without the TO-BE and a BRQ session with the Investment department. This is NADF's most business-critical remaining gap.

**Recommendation:** Obtain Investment TO-BE and schedule BRQ session. Prepare nadf_investment specification immediately after. This is the highest-priority Phase 2 item.

---

## 12. MONITORING & EVALUATION (CA-11)

### Traceability Chain

| Chain Element | Status | Evidence / Notes |
|---|---|---|
| Business Process | **M** | TO-BE not delivered. |
| Refined TO-BE | **M** | Not delivered. |
| ERP Mapping | **P** | OCA: `mis_builder` (already installed) as base. Custom: `nadf_me_indicators` for programme-level KPI tracking beyond financial indicators. |
| Capability Definition | **P** | §6: KPI dashboard (OCA + Custom), programme indicator tracking (Custom). No indicator definition model or target/actual structure defined. |
| Product Scope Coverage | **P** | BL-ME-01, BL-SPEC-06, BL-DEV-06 defined. |
| Product Package | **P** | Transfer Package §3.11 has framework. `nadf_me_indicators` confirmed Priority P3. No design spec. |
| Work Package Definition | **P** | WP-SPEC-06, WP-DEV-06, WP-DEPT-06 defined as placeholders. |
| Implementation | **NS** | Not started. `mis_builder` is installed (WP-01). |
| Testing | **NS** | Not started. |

### Outstanding Dependencies

1. **M&E TO-BE** — entire chain blocked
2. **nadf_me_indicators design spec** — BL-SPEC-06; Priority P3
3. **mis_builder KPI set** — client confirmation pending (ESC-CLIENT-WP02-08 — open escalation)
4. Integration with Executive dashboard

### Implementation Readiness: BLOCKED

**Justification:** Base OCA module (`mis_builder`) is already installed — a meaningful head start. The custom indicator framework cannot be specified without the M&E TO-BE. Priority P3 (lowest) — correctly sequenced after Investment and Legal.

**Recommendation:** Obtain M&E TO-BE. Resolve mis_builder KPI set with client (ESC-CLIENT-WP02-08) in parallel. Prepare nadf_me_indicators spec after TO-BE is received.

---

## 13. CROSS-CUTTING INFRASTRUCTURE

### Platform Engineering Constraints (Factual — Discovered During Execution)

These are confirmed CE 17 capability gaps, not assumptions:

| Constraint | Discovered In | Impact | Resolution Path |
|---|---|---|---|
| `project.project` has no `parent_id` | WP-PC-01 | No enforced programme hierarchy | `nadf_project_governance` Phase 2 |
| `project.milestone.is_reached` not field-restriceable | WP-PC-01 | Director-only sign-off is organizational only | `nadf_project_governance` Phase 2 |
| `auth_totp` global policy only | WP-01 | Cannot exempt service accounts from TOTP | OCA `auth_totp_mandatory_group` or custom |
| `account_budget_oca` incompatible | WP-01 | Budget configuration blocked | DEC-OCA-02 — must resolve |
| `helpdesk_mgmt` has no SLA model | WP-ADM-01 | SLA enforcement is priority proxy only | `nadf_ict_helpdesk` Phase 2 custom |
| `hr_holidays` max 2 approval levels | DEC-007 | 3-level Study Leave approval advisory | `nadf_hr_leave` Phase 2 custom |
| `account.payment` no hard-block | DEC-WP02-001 | Payment approval advisory only | `nadf_approvals` Phase 2 custom |
| OCA `purchase_request` own group hierarchy | WP-03 | Direct user assignment required | Group inheritance in Phase 2 module |
| `purchase_requisition` is CE native in 17 | WP-01 | No OCA install needed | Clarify Transfer Package v2.1 reference |

---

## Summary: Traceability Chain Completion Matrix

| Department | Biz Process | TO-BE | ERP Map | Capability Def | Scope | Package | WP Defined | Implementation | Testing |
|---|---|---|---|---|---|---|---|---|---|
| Executive Mgmt | M | M | P | P | P | M | P | NS | NS |
| Finance | C | C | C | C | C | C | C | CP | NS |
| Procurement | C | C | C | C | C | C | C | CP | NS |
| HR | C | C | C | C | C | C | C | CP | NS |
| Administration | C | C | C | C | C | C | C | CP | NS |
| ICT | C* | C* | C* | C* | C* | C* | C* | CP* | NS |
| Project Coord | C | C | C | C | C | C | C | CP | NS |
| Legal Services | P | P | P | P | P | P | P | NS | NS |
| Strategy | M | M | M | M | P | M | P | NS | NS |
| Communications | M | M | M | M | P | M | P | NS | NS |
| Sustainable Ag | M | M | M | M | P | M | P | NS | NS |
| Investment | M | M | P | P | P | P | P | NS | NS |
| M&E | M | M | P | P | P | P | P | NS | NS |

*ICT is covered within Administration (CA-04) — not a separate departmental build.

---

## Backlog Reconciliation Gap

**Critical finding:** The `planning/BACKLOG.md` statuses are stale. All Phase 0 items (BL-GOV-01 through BL-GOV-09) are marked "Not Started" — but M0 is formally CLOSED (2026-06-24, PR #1–#4 merged). Phase 1 department items (BL-FIN-01, BL-HR-01, BL-ADM-01, etc.) are marked "In Progress" or "Not Started" — but WP-01 through WP-PC-01 are all CONDITIONAL PASS. No backlog item is marked "Done." This is a governance gap that must be resolved before Wave C begins. The backlog does not reflect the programme's actual execution state.

---

*PRODUCT_ENGINEERING_TRACEABILITY_REPORT.md — PETR-NADF-001 — A1 Master Orchestrator — 2026-06-29*
*Sources: Transfer Package v2.1 · BACKLOG · WORK_PACKAGES · ROADMAP · GAR v1.3 · DECISION_LOG · IMPLEMENTATION_HISTORY · WP Execution Files*
