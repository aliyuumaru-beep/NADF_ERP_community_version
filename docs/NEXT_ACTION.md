# NADF ERP — Next Action

**Last updated:** 2026-06-29 (Wave C: DEC-OCA-02 resolved, WP02-07 PASS, backlog reconciled, M1-CPC CONDITIONAL PASS, WP-05 UAT prep authored · PR pending)

## Current Milestone
**M1 — Foundation** (ROADMAP Phase 1). M0 CLOSED. Wave A CLOSED. Wave B COMPLETE (PR #12 merged `63879e9`). Wave C IN PROGRESS.

## Current State
- **main:** `63879e9` (all PRs #1–#12 merged). Odoo 106 modules, exit 0.
- **PR #12 MERGED:** `feat/wp-pc-01-project-coordination` — WP-PC-01 CONDITIONAL PASS (`63879e9`). Wave B COMPLETE.
- **Wave C branch:** `feat/wave-c-ops` from `63879e9` — all changes staged, PR pending.
- **WP-01 CONDITIONAL PASS:** 4/5 OCA installed + account_budget_oca NOW INSTALLED (DEC-OCA-02-RES). 106 modules total.
- **WP-02 CONDITIONAL PASS:** CoA ✅; bill workflow ✅; payment dual-auth ✅; analytic accounts ✅; FY2026 Budget ₦107.3B confirmed ✅.
- **WP-03 CONDITIONAL PASS:** compliance field ✅; purchase_request ✅; Call for Tender ✅; WP03-07 BLOCKED (B-02/B-03).
- **WP-04 CONDITIONAL PASS:** hr_recruitment ✅; org hierarchy ✅; leave workflows ✅; x_employment_state ✅; WP04-08 DEFERRED (B-WP04-02).
- **WP-ADM-01 CONDITIONAL PASS:** fleet register ✅; asset register ✅; helpdesk_mgmt ✅; mail.thread ✅; Driver + IT Officer groups PENDING (B-WP04-01).
- **WP-PC-01 CONDITIONAL PASS:** 5 PCU stages ✅; NADF Programme project ✅; milestone ✅; Director ACL ✅; Director-only field restriction DEFERRED (DEC-PC01-002).
- **M1-CPC CONDITIONAL PASS (2026-06-29):** G1/G2/G3 all PASS. All 6 WPs done. Remaining gaps are client/Phase 2.
- **Single Claude Code session enforced.**

## Wave C — Completed Deliverables
| Deliverable | Status |
|-------------|--------|
| Pre-work backup `nadf_20260629_144419` (6.5 MB + 38 MB) | ✅ DONE |
| DEC-OCA-02 investigation (Option A confirmed; no misspelling in local copy) | ✅ DONE |
| Drill DB install of account_budget_oca (exit 0, 289 queries) | ✅ DONE |
| NADF DB install of account_budget_oca (105→106 modules) | ✅ DONE |
| WP02-07: 3 budgetary positions created | ✅ DONE |
| WP02-07: FY2026 Budget id=1 state=confirm (₦107,321,826,467) | ✅ DONE |
| BACKLOG.md reconciled — Phase 0 (9 items) + Phase 1 (35 items) | ✅ DONE |
| CHANGELOG.md Wave C section | ✅ DONE |
| IMPLEMENTATION_HISTORY.md Wave C block | ✅ DONE |
| DECISION_LOG.md — DEC-OCA-02-RES + DEC-WP02C-001 | ✅ DONE |
| MODULE_REGISTRY.md — account_budget_oca ❌ → ✅ | ✅ DONE |
| GAR-NADF-001 updated to v1.4 (33 decisions; ESC-OCA-02 closed) | ✅ DONE |
| M1_CPC_GATE_REPORT.md created (G1/G2/G3 PASS; M1-CPC CONDITIONAL PASS) | ✅ DONE |
| MILESTONE_TRACKER.md Wave C state + M1-CPC entry | ✅ DONE |
| WP_05_UAT_PREPARATION.md — 11 test scenarios, defect register, exit criteria | ✅ DONE |
| NEXT_ACTION.md updated (this file) | ✅ DONE |
| PROJECT_STATE.md updated | ✅ DONE |

## ➡️ CURRENT ACTIVE WORK PACKAGE

**WP-05 — UAT / Operational Readiness.** Test plan authored (`docs/work_packages/WP_05_UAT_PREPARATION.md`). Execution requires client scheduling. Pre-conditions: Wave C PR merged; NADF client UAT participants identified; TOTP enrolled.

**Immediate next steps (A1):**
1. Commit `feat/wave-c-ops` with all Wave C deliverables
2. Open PR #13 → main; await reviewer approval
3. Dispatch client action items (B-02/B-03/B-WP04-01/B-WP04-02/WP02-02/WP02-08) to NADF contact
4. Schedule WP-05 UAT session with client once PR merged

## M1 Sub-Milestone Status
| Sub-Milestone | Description | Status |
|--------------|-------------|--------|
| M1-CPC | Core Product Capability — all 6 Foundation WPs | ✅ **CONDITIONAL PASS** 2026-06-29 |
| M1-OPR | Operational Readiness — WP-05 UAT execution | ⏳ In preparation (test plan authored) |
| M1-PRD | Production Readiness — client sign-offs + go/no-go | ⏳ Blocked (client actions) |

## Open Escalations
| ID | Description | Status |
|----|-------------|--------|
| ESC-CLIENT-B02 | Procurement RACI / approval thresholds (WP03-07) | OPEN — client |
| ESC-CLIENT-WP02-08 | mis_builder dashboard — client KPI sign-off | DEFERRED — client |
| ~~ESC-OCA-02~~ | ~~account_budget_oca~~ | **RESOLVED** — DEC-OCA-02-RES (Wave C) |

## Client Actions Required
| Item | Action | WP |
|------|--------|----|
| B-02 | Confirm procurement RACI step 1.19 (approver identity) | WP03-07 |
| B-03 | Confirm PO approval threshold(s) — current: ₦500K UNCHANGED | WP03-07 |
| B-WP04-01 | Confirm dept assignments + reporting lines for 6 Admin-dept employees | WP04-01/02, ADM01-06 |
| B-WP04-02 | Provide NADF RC number and TIN for company registration | WP04-08 |
| B-ADM01-01 | Provide vehicle license plates + confirm driver assignments | ADM01-01 |
| WP02-02 | Review and sign off `csv_templates/nadf_coa_revalidated_20260625.csv` | WP-02 |
| WP02-08 | Confirm NADF KPI set for mis_builder dashboard | WP-02 |

## Execution Wave Plan
```
Wave A:  Session 1 → WP-03 → PR #8  [MERGED be7ed8b]        ✅ CLOSED
         Session 2 → WP-04 → PR #10 [MERGED 5e3861e]        ✅ CLOSED
         WAVE_A_COMPLETION_REPORT.md produced
Wave B:  Session 3 → WP-ADM-01 → PR #11 [MERGED 6f7f4bb]   ✅ CLOSED
         Session 4 → WP-PC-01 → PR #12 [MERGED 63879e9]     ✅ COMPLETE
Wave C:  DEC-OCA-02 resolved ✅ · WP02-07 budget PASS ✅ ·
         backlog reconciled ✅ · M1-CPC CONDITIONAL PASS ✅ ·
         WP-05 UAT prep authored ✅ · PR #13 pending 🔄
Wave D:  WP-05 UAT execution — client scheduling required ⏳
```

## Single-Session Discipline
⚠️ Only one Claude Code session may be active at any time. Max safe concurrency: **1 executing + 1 in PR review**.

## Files to Read Before Starting (Any Session)
1. `docs/NEXT_ACTION.md` (this file)
2. `docs/governance/GOVERNANCE_APPROVAL_REGISTER.md` (open escalations + deferred decisions — mandatory)
3. `docs/PRODUCT_STATE_INDEX.md` (session protocol)
4. `PROJECT_STATE.md`
5. `MILESTONE_TRACKER.md`
6. `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (bound authority)
