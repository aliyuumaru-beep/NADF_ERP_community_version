# PRODUCT_READINESS_MATRIX.md
## NADF ERP — Department Product Readiness Matrix

**Document ID:** PRM-NADF-001
**Review type:** Engineering Audit — read-only
**Authority:** A1 Master Orchestrator
**Date:** 2026-06-29
**Source:** Synthesized from PETR-NADF-001 traceability chains

---

## Readiness Classification Definitions

| Classification | Criteria |
|---|---|
| **PRODUCTION READY** | All chain elements complete; WP PASS; UAT complete; no blocking gaps. |
| **PARTIALLY READY** | Core implementation CONDITIONAL PASS; deferred items exist; UAT not started; production-capable for defined scope. |
| **BLOCKED** | Implementation cannot proceed — dependent on missing TO-BE, client decision, or missing custom module spec. |
| **NOT YET ENGINEERED** | No TO-BE, no product package, no capability definition at implementation level. A planning entry exists, nothing more. |

---

## Product Readiness Matrix

| # | Department | Capability Area | Business Processes Defined | Product Package | Implementation Status | Readiness | Remaining Gap | Blocking Item | Next Action |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Finance** | CA-01 | 7/7 Complete | Transfer Package §3.1 Complete | WP-02 CONDITIONAL PASS | **PARTIALLY READY** | Budget module (DEC-OCA-02); Dashboard (WP02-08 client); UAT | DEC-OCA-02 engineering | Resolve DEC-OCA-02 in Wave C; client CoA sign-off (WP02-02) |
| 2 | **Procurement** | CA-02 | 6/6 Complete (2 client queries) | Transfer Package §3.2 Complete | WP-03 CONDITIONAL PASS | **PARTIALLY READY** | WP03-07 approval chain (B-02/B-03); nadf_vendor_compliance spec; UAT | B-02 + B-03 client decisions | Obtain B-02/B-03; begin nadf_vendor_compliance spec (unblocked) |
| 3 | **HR** | CA-03 | 8/8 Complete (payroll Phase 3) | Transfer Package §3.3 Complete | WP-04 CONDITIONAL PASS | **PARTIALLY READY** | B-WP04-01 employee roles; B-WP04-02 company registration; nadf_payroll_ng (Phase 3); UAT | B-WP04-01 + B-WP04-02 client | Obtain B-WP04-01/02; begin nadf_payroll_ng legal advisory |
| 4 | **Administration** | CA-04 | 4/4 Complete (facility deferred) | Transfer Package §3.4 Complete | WP-ADM-01 CONDITIONAL PASS | **PARTIALLY READY** | Driver/IT Officer groups (B-WP04-01); DEC-ADM01-002 GL correction; nadf_facility spec; UAT | B-WP04-01; B-ADM01-01 | Obtain B-ADM01-01; resolve DEC-ADM01-002 with Finance; begin nadf_facility spec |
| 5 | **ICT Helpdesk** | CA-04 (sub) | Within Administration | Within WP-ADM-01 | WP-ADM-01 CONDITIONAL PASS | **PARTIALLY READY** | SLA enforcement deferred (DEC-ADM01-001); IT Officer group population | B-WP04-01 | Same as Administration. ICT is not a separate departmental build. |
| 6 | **Project Coordination** | CA-05 | 5/5 Complete | Transfer Package §3.5 Complete | WP-PC-01 CONDITIONAL PASS | **PARTIALLY READY** | PCU Head/PM/PTM user assignment (B-WP04-01); Director-only milestone restriction Phase 2; nadf_project_governance spec missing from Transfer Package | B-WP04-01; DEC-PC01-002 | Obtain B-WP04-01; add nadf_project_governance to Transfer Package v2.1; prepare spec Phase 2 |
| 7 | **Legal Services** | CA-06 | 3/6 Partial (P4–P6 missing) | Transfer Package §3.6 Partial | Not Started | **BLOCKED** | Legal TO-BE P4–P6 missing; nadf_legal_contract spec not written; no data model | Legal TO-BE P4–P6 | Obtain Legal TO-BE P4–P6; write nadf_legal_contract spec immediately after |
| 8 | **Strategy & Planning** | CA-07 | 0/6 Missing | None | Not Started | **NOT YET ENGINEERED** | Entire chain absent — no TO-BE, no capability definition, no spec, no WP | Client — TO-BE entirely missing | Obtain Strategy & Planning TO-BE |
| 9 | **Communications** | CA-08 | 0/5 Missing | None | Not Started | **NOT YET ENGINEERED** | Entire chain absent — no TO-BE, no capability definition, no spec | Client — TO-BE entirely missing | Obtain Communications TO-BE; assess overlap with helpdesk_mgmt |
| 10 | **Sustainable Agriculture** | CA-09 | 0/5 Missing | None | Not Started | **NOT YET ENGINEERED** | Entire chain absent — no TO-BE; possible overlap with nadf_investment | Client — TO-BE entirely missing; Investment module scope unresolved | Obtain SA TO-BE; assess nadf_investment reuse first |
| 11 | **Investment** | CA-10 | 0/7 Missing | Transfer Package §3.10 Framework | Not Started | **BLOCKED** | TO-BE missing; nadf_investment spec not written; no data model; highest-priority Phase 2 custom module | Investment TO-BE + BRQ session required | Obtain Investment TO-BE; schedule BRQ session; begin nadf_investment spec immediately |
| 12 | **M&E** | CA-11 | 0/4 Missing | Transfer Package §3.11 Framework | Not Started | **BLOCKED** | TO-BE missing; nadf_me_indicators spec not written; mis_builder KPI set unconfirmed (WP02-08) | M&E TO-BE; ESC-CLIENT-WP02-08 | Obtain M&E TO-BE; resolve WP02-08 in parallel |
| 13 | **Executive Management** | CA-12 | 0/3 Missing | None | Not Started | **NOT YET ENGINEERED** | Entire chain absent; no TO-BE; dashboard entirely dependent on all dept builds completing | All department builds must complete first; client TO-BE absent | Defer until Phase 3 architecture confirmed; obtain TO-BE |

---

## Readiness Summary Counts

| Readiness Level | Count | Departments |
|---|---|---|
| PRODUCTION READY | **0** | None |
| PARTIALLY READY | **6** | Finance, Procurement, HR, Administration, ICT (within Admin), Project Coordination |
| BLOCKED | **3** | Legal Services, Investment, M&E |
| NOT YET ENGINEERED | **4** | Strategy & Planning, Communications, Sustainable Agriculture, Executive Management |
| **TOTAL** | **13** | 6 build streams; ICT within Admin |

> Note: ICT counted separately in matrix but shares WP-ADM-01 readiness. True department count = 12 independent builds + 1 (ICT within Admin).

---

## Critical Path to M1-CPC Closure

M1-CPC (Core Product Capability) closes when all 6 Phase 1 WPs are CONDITIONAL PASS with PRs merged:

| WP | Status | PR |
|---|---|---|
| WP-01 Foundation Hardening | CONDITIONAL PASS | #5 merged ✅ |
| WP-02 Finance Core | CONDITIONAL PASS | #6 merged ✅ |
| WP-03 Procurement Core | CONDITIONAL PASS | #8 merged ✅ |
| WP-04 HR Core | CONDITIONAL PASS | #10 open ⏳ |
| WP-ADM-01 Administration Core | CONDITIONAL PASS | #11 open ⏳ |
| WP-PC-01 Project Coordination | CONDITIONAL PASS | #12 open ⏳ |

**M1-CPC closure gate:** Merge PRs #10 → #11 → #12. No additional implementation required.

---

## Custom Module Readiness (Phase 2 and 3)

| Module | Priority | Trigger | Status | Blocking Item |
|---|---|---|---|---|
| `nadf_vendor_compliance` | P2 | Procurement TO-BE complete | **UNBLOCKED — can specify now** | None |
| `nadf_facility` | P2 | Administration TO-BE complete | **UNBLOCKED — can specify now** | None |
| `nadf_project_governance` | P2 | Project Coord Phase 1 complete | **UNBLOCKED — can specify now**; not in Transfer Package v2.1 (gap) | None (gap: add to TP v2.1) |
| `nadf_legal_contract` | P2 | Legal TO-BE P4–P6 | Blocked — TO-BE P4–P6 missing | Legal TO-BE P4–P6 |
| `nadf_investment` | P1 | Investment TO-BE + BRQ | Blocked — TO-BE + BRQ session required | Investment TO-BE |
| `nadf_payroll_ng` | P1 | Payroll legal advisory + OCA base | Partially unblocked — legal advisory needed | Payroll legal advisory input |
| `nadf_me_indicators` | P3 | M&E TO-BE + mis_builder KPI set | Blocked — TO-BE missing | M&E TO-BE; WP02-08 |

---

*PRM-NADF-001 — A1 Master Orchestrator — 2026-06-29*
