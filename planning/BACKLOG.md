# BACKLOG.md
## NADF ERP Programme — Prioritised Implementation Inventory

**Document type:** Operational — derived from NADF Full Product Transfer Package v2.1  
**Last updated:** 2026-06-21 (coverage closure — 9 omissions and 3 scope reductions addressed)  
**Authority:** NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md  
**Update rule:** Status must be updated after every session. No item is marked Done until its acceptance criteria are verified.

---

## Priority Classification
- **Must Have (MH):** Required for go-live; programme fails without it
- **Should Have (SH):** Important but go-live possible with workaround; must be delivered post-go-live if deferred
- **Could Have (CH):** Desirable enhancement; may be deferred to Phase 5 or later

## Status Values
`Not Started` | `In Progress` | `Blocked` | `Done` | `Deferred`

---

## PHASE 0 — GOVERNANCE REMEDIATION

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-GOV-01 | Repository discovery and audit | CA-14 | MH | 0 | Not Started | Repo access | D-0.1 |
| BL-GOV-02 | Odoo instance Enterprise module audit | CA-14 | MH | 0 | Not Started | Odoo access | D-0.5 |
| BL-GOV-03 | Governance Activation Gate — run all five gates | CA-14 | MH | 0 | Not Started | BL-GOV-01, BL-GOV-02 | D-0.2 |
| BL-GOV-04 | Repository scaffold committed to main | CA-14 | MH | 0 | Not Started | BL-GOV-03 | D-0.4 |
| BL-GOV-05 | Backup strategy documented and verified | CA-14 | MH | 0 | Not Started | Odoo access | D-0.3 |
| BL-GOV-06 | GitHub branch protection enabled | CA-14 | MH | 0 | Not Started | Repo access | D-0.2 |
| BL-GOV-07 | CI workflow created and active | CA-14 | SH | 0 | Not Started | BL-GOV-06 | D-0.2 |
| BL-GOV-08 | DEC-PLATFORM-001 logged in Decision Log | CA-14 | MH | 0 | Not Started | BL-GOV-02 | D-0.5 |
| BL-GOV-09 | Document session start and end rules in `docs/PRODUCT_STATE_INDEX.md` | CA-14 | MH | 0 | Not Started | BL-GOV-04 | Session rules committed to repo |

---

## PHASE 1 — FOUNDATION

### Finance (CA-01)

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-FIN-01 | Configure government chart of accounts | CA-01 | MH | 1 | In Progress | Phase 0 complete | AC-01 |
| BL-FIN-02 | Configure vendor bill workflow | CA-01 | MH | 1 | In Progress | BL-FIN-01 | AC-01 |
| BL-FIN-03 | Configure payment workflow with dual authorisation | CA-01 | MH | 1 | In Progress | BL-FIN-01 | AC-01 |
| BL-FIN-04 | Configure analytic accounts and budget control (`account_budget_oca`) | CA-01 | MH | 1 | Not Started | BL-OCA-02 | AC-01 |
| BL-FIN-05 | Install and configure `mis_builder` financial dashboard | CA-01 | SH | 1 | Not Started | BL-OCA-01 | AC-01 |
| BL-FIN-06 | Configure Finance user groups and access rights | CA-14 | MH | 1 | Not Started | Phase 0 complete | AC-14 |
| BL-FIN-07 | Enable and enforce TOTP two-factor authentication | CA-14 | MH | 1 | Not Started | Phase 0 complete | AC-14 |
| BL-FIN-08 | Verify `mail.thread` audit trail on all Finance records | CA-14 | MH | 1 | Not Started | BL-FIN-01 | AC-14 |
| BL-FIN-09 | Configure and verify native `account` financial reports (trial balance, P&L, balance sheet) | CA-01 | SH | 1 | Not Started | BL-FIN-01 | AC-01 |

### Procurement (CA-02)

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-PROC-01 | Configure vendor record structure with compliance status field | CA-02 | MH | 1 | In Progress | Phase 0 complete | AC-02 |
| BL-PROC-02 | Install and configure `purchase_request` multi-step requisition | CA-02 | MH | 1 | Not Started | BL-OCA-03 | AC-02 |
| BL-PROC-03 | Configure multi-level requisition approval chain | CA-02 | MH | 1 | Blocked | BL-PROC-02 + B-02, B-03 resolved | AC-02 |
| BL-PROC-04 | Configure RFQ and tender workflow (`purchase_requisition`) | CA-02 | MH | 1 | Not Started | BL-OCA-04 | AC-02 |
| BL-PROC-05 | Configure purchase order approval with threshold limits | CA-02 | MH | 1 | Blocked | B-03 resolved | AC-02 |
| BL-PROC-06 | Configure goods receipt and stock flow | CA-02 | MH | 1 | Not Started | Phase 0 complete | AC-02 |
| BL-PROC-07 | Configure Procurement user groups and access rights | CA-14 | MH | 1 | Not Started | Phase 0 complete | AC-14 |
| BL-PROC-08 | Verify `mail.thread` audit trail on all Procurement records | CA-14 | MH | 1 | Not Started | BL-PROC-01 | AC-14 |
| BL-PROC-09 | Evaluate OCA `contract` module fit for PO-linked contract records; decide and log in Decision Log | CA-02 | MH | 1 | Not Started | BL-PROC-01 | Decision Log entry DEC-CONTRACT-001 |

### HR (CA-03)

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-HR-01 | Configure employee records with NADF 4-level org hierarchy | CA-03 | MH | 1 | In Progress | Phase 0 complete | AC-03 |
| BL-HR-02 | Configure leave request and approval workflow (`hr_holidays`) | CA-03 | MH | 1 | In Progress | BL-HR-01 | AC-03 |
| BL-HR-03 | Configure recruitment pipeline (`hr_recruitment`) | CA-03 | MH | 1 | Not Started | BL-HR-01 | AC-03 |
| BL-HR-04 | Configure HR user groups and access rights | CA-14 | MH | 1 | Not Started | Phase 0 complete | AC-14 |
| BL-HR-05 | Verify `mail.thread` audit trail on HR records | CA-14 | MH | 1 | Not Started | BL-HR-01 | AC-14 |
| BL-HR-06 | HR performance management (appraisal workflow) | CA-03 | CH | Future | Deferred | OCA appraisal module availability confirmed | AC-03 (future extension) |

### Administration (CA-04)

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-ADM-01 | Configure vehicle register and fuel log (`fleet`) | CA-04 | MH | 1 | In Progress | Phase 0 complete | AC-04 |
| BL-ADM-02 | Configure asset register and depreciation schedule (`account_asset`) | CA-04 | MH | 1 | In Progress | Phase 0 complete | AC-04 |
| BL-ADM-03 | Install and configure `helpdesk_mgmt` ICT helpdesk | CA-04 | MH | 1 | Not Started | BL-OCA-05 | AC-04 |
| BL-ADM-04 | Configure Administration user groups and access rights | CA-14 | MH | 1 | Not Started | Phase 0 complete | AC-14 |

### Project Coordination (CA-05)

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-PC-01 | Configure `project` module: project record, phases, tasks | CA-05 | MH | 1 | Not Started | Phase 0 complete | AC-05 |
| BL-PC-02 | Configure milestone tracking with phase gate approval | CA-05 | MH | 1 | Not Started | BL-PC-01 | AC-05 |
| BL-PC-03 | Configure project status dashboard view | CA-05 | SH | 1 | Not Started | BL-PC-01 | AC-05 |
| BL-PC-04 | Configure Project Coordination user groups and access rights | CA-14 | MH | 1 | Not Started | Phase 0 complete | AC-14 |

### OCA Module Installation (Phase 1)

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-OCA-01 | Install and version-pin `mis_builder` | CA-01, CA-11, CA-12 | MH | 1 | Not Started | Phase 0 complete | AC-01 |
| BL-OCA-02 | Install and version-pin `account_budget_oca` | CA-01 | MH | 1 | Not Started | Phase 0 complete | AC-01 |
| BL-OCA-03 | Install and version-pin `purchase_request` | CA-02 | MH | 1 | Not Started | Phase 0 complete | AC-02 |
| BL-OCA-04 | Install and version-pin `purchase_requisition` | CA-02 | MH | 1 | Not Started | Phase 0 complete | AC-02 |
| BL-OCA-05 | Install and version-pin `helpdesk_mgmt` | CA-04 | MH | 1 | Not Started | Phase 0 complete | AC-04 |
| BL-OCA-06 | Log all OCA installations in Decision Log | CA-14 | MH | 1 | Not Started | BL-OCA-01 to 05 | — |
| BL-OCA-07 | Install and version-pin OCA payroll base module | CA-03 | MH | 2 | Not Started | BL-SPEC-01 approved | OCA payroll base confirmed installed before BL-DEV-01 |

---

## PHASE 2 — CUSTOM MODULE SPECIFICATIONS

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-SPEC-01 | Draft and approve `nadf_payroll_ng` spec | CA-03 | MH | 2 | Not Started | Nigerian payroll legal input | D-2.1 |
| BL-SPEC-02 | Draft and approve `nadf_vendor_compliance` spec | CA-02 | SH | 2 | Not Started | Phase 1 Procurement complete | D-2.2 |
| BL-SPEC-03 | Draft and approve `nadf_facility` spec | CA-04 | SH | 2 | Not Started | Phase 1 Admin complete | D-2.3 |
| BL-SPEC-04 | Draft and approve `nadf_legal_contract` spec | CA-06 | MH | 2 | Not Started | Legal TO-BE P4–P6 delivered | D-2.4 |
| BL-SPEC-05 | Draft and approve `nadf_investment` spec | CA-10 | MH | 2 | Not Started | Investment TO-BE + client BRQ session | D-2.5 |
| BL-SPEC-06 | Draft and approve `nadf_me_indicators` spec | CA-11 | SH | 2 | Not Started | M&E TO-BE delivered | D-2.6 |

---

## PHASE 3 — EXTENDED CAPABILITIES

### Custom Module Development

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-DEV-01 | Develop `nadf_payroll_ng` | CA-03 | MH | 3 | Not Started | BL-SPEC-01 approved + BL-OCA-07 complete | AC-03 |
| BL-DEV-02 | Develop `nadf_vendor_compliance` | CA-02 | SH | 3 | Not Started | BL-SPEC-02 approved | AC-02 |
| BL-DEV-03 | Develop `nadf_facility` | CA-04 | SH | 3 | Not Started | BL-SPEC-03 approved | AC-04 |
| BL-DEV-04 | Develop `nadf_legal_contract` | CA-06 | MH | 3 | Not Started | BL-SPEC-04 approved | AC-06 |
| BL-DEV-05 | Develop `nadf_investment` | CA-10 | MH | 3 | Not Started | BL-SPEC-05 approved | AC-10 |
| BL-DEV-06 | Develop `nadf_me_indicators` | CA-11 | SH | 3 | Not Started | BL-SPEC-06 approved | AC-11 |

### Remaining Department Builds

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-LSU-01 | Configure Legal Services Unit Odoo build | CA-06 | MH | 3 | Not Started | Legal TO-BE complete + BL-DEV-04 | AC-06 |
| BL-LSU-02 | Configure Legal user groups and access rights | CA-14 | MH | 3 | Not Started | BL-LSU-01 | AC-14 |
| BL-STR-01 | Configure Strategy & Planning Odoo build | CA-07 | SH | 3 | Not Started | Strategy TO-BE delivered | AC-07 |
| BL-COM-01 | Configure Communications Odoo build | CA-08 | SH | 3 | Not Started | Comms TO-BE delivered | AC-08 |
| BL-SA-01 | Configure Sustainable Agriculture Odoo build | CA-09 | MH | 3 | Not Started | SA TO-BE delivered; assess overlap with BL-DEV-05 (`nadf_investment`) before build begins | AC-09 |
| BL-INV-01 | Configure Investment Odoo build | CA-10 | MH | 3 | Not Started | Investment TO-BE + BL-DEV-05 | AC-10 |
| BL-ME-01 | Configure M&E Odoo build | CA-11 | SH | 3 | Not Started | M&E TO-BE + BL-DEV-06 | AC-11 |
| BL-EXEC-01 | Configure Executive Management dashboard (including pending-approval visibility for CEO/MD) | CA-12 | MH | 3 | Not Started | Exec TO-BE + BL-OCA-01 | AC-12 |

---

## PHASE 4 — INTEGRATIONS

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-INT-01 | Budget → Procurement → Finance end-to-end chain | CA-13 | MH | 4 | Not Started | Phase 3 complete | AC-13 |
| BL-INT-02 | HR appointment → CEO → payroll integration | CA-13 | MH | 4 | Not Started | BL-DEV-01, Phase 3 HR complete | AC-13 |
| BL-INT-03 | Project → Finance budget consumption linkage | CA-13 | SH | 4 | Not Started | Phase 3 PC + Finance complete | AC-13 |
| BL-INT-04 | Investment disbursement → Finance payment chain | CA-13 | MH | 4 | Not Started | BL-DEV-05, Phase 1 Finance complete | AC-13 |
| BL-INT-05 | Executive cross-department KPI roll-up verification | CA-12, CA-13 | MH | 4 | Not Started | All department builds complete | AC-12, AC-13 |
| BL-INT-06 | Integration test report | CA-13 | MH | 4 | Not Started | BL-INT-01 to BL-INT-08 | D-4.7 |
| BL-INT-07 | Configure cross-department notification and escalation matrix | CA-13 | MH | 3 | Not Started | Phase 1 department builds complete | AC-13 |
| BL-INT-08 | Implement cross-department document routing workflows | CA-13 | SH | 3 | Not Started | Department builds complete; scope confirmed from remaining TO-BE specs | AC-13 |

---

## PHASE 5 — TESTING & STABILISATION

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-UAT-01 | UAT test plan and test cases | All | MH | 5 | Not Started | Phase 4 complete | D-5.1 |
| BL-UAT-02 | UAT execution with NADF users | All | MH | 5 | Not Started | BL-UAT-01 | D-5.2 |
| BL-UAT-03 | UAT defect resolution | All | MH | 5 | Not Started | BL-UAT-02 | D-5.3 |
| BL-UAT-04 | UAT sign-off | All | MH | 5 | Not Started | BL-UAT-03 | D-5.4 |
| BL-TRN-01 | Super user training documentation | All | SH | 5 | Not Started | Phase 4 complete | D-5.5 |
| BL-TRN-02 | System administrator guide | CA-14 | SH | 5 | Not Started | Phase 4 complete | D-5.6 |

---

## PHASE 6 — DEPLOYMENT

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-DEP-01 | Cutover plan produced and approved | All | MH | 6 | Not Started | BL-UAT-04 | D-6.1 |
| BL-DEP-02 | Master data migration (employees, vendors, assets, CoA) | All | MH | 6 | Not Started | BL-DEP-01 | D-6.2 |
| BL-DEP-03 | Production deployment | All | MH | 6 | Not Started | BL-DEP-02 | D-6.3 |
| BL-DEP-04 | Post-deployment smoke test | All | MH | 6 | Not Started | BL-DEP-03 | D-6.4 |
| BL-DEP-05 | Go-live confirmation signed | All | MH | 6 | Not Started | BL-DEP-04 | D-6.5 |
| BL-DEP-06 | Repository tagged `v1.0-go-live` | CA-14 | MH | 6 | Not Started | BL-DEP-05 | D-6.7 |

---

## PHASE 7 — TEMPLATE EXTRACTION

| ID | Title | Capability | Priority | Phase | Status | Dependency | AC Reference |
|----|-------|-----------|---------|-------|--------|-----------|-------------|
| BL-TPL-01 | Template extraction report | All | SH | 7 | Not Started | BL-DEP-05 | D-7.1 |
| BL-TPL-02 | Anonymise repository scaffold | CA-14 | SH | 7 | Not Started | BL-TPL-01 | D-7.2 |
| BL-TPL-03 | Parameterise and strip custom modules | All | SH | 7 | Not Started | BL-TPL-01 | D-7.3 |
| BL-TPL-04 | Government chart of accounts template | CA-01 | SH | 7 | Not Started | BL-TPL-01 | D-7.4 |
| BL-TPL-05 | OCA integration pattern guides | All | CH | 7 | Not Started | BL-TPL-01 | D-7.5 |
| BL-TPL-06 | Public Sector ERP Template repository created | All | SH | 7 | Not Started | BL-TPL-02 to 05 | D-7.6 |
| BL-TPL-07 | Template README and deployment guide | All | SH | 7 | Not Started | BL-TPL-06 | D-7.7 |
