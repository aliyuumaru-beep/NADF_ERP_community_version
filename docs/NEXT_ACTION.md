# NADF ERP — Next Action

**Last updated:** 2026-06-26 (WP-PC-01 Project Coordination — CONDITIONAL PASS · Wave B COMPLETE · Session 4)

## Current Milestone
**M1 — Foundation** (ROADMAP Phase 1). M0 CLOSED. Wave A CLOSED. Wave B COMPLETE. WP-01/02/03/04/ADM-01/PC-01 all CONDITIONAL PASS.

## Current State
- **main:** `6f7f4bb` (PRs #9 + #10 + #11 merged). Odoo PID 59090, 105 modules, exit 0.
- **PR #10 MERGED:** `feat/wp-04-hr-core` — WP-04 HR Core CONDITIONAL PASS (`5e3861e`).
- **PR #11 MERGED:** `feat/wp-adm-01-administration-core` — WP-ADM-01 Administration Core CONDITIONAL PASS (`6f7f4bb`).
- **PR #12 OPEN:** `feat/wp-pc-01-project-coordination` — WP-PC-01 Project Coordination CONDITIONAL PASS (this branch).
- **Wave A CLOSED:** WAVE_A_COMPLETION_REPORT.md produced.
- **Wave B COMPLETE:** WP-ADM-01 + WP-PC-01 both CONDITIONAL PASS.
- **WP-01 CONDITIONAL PASS:** 4/5 OCA installed; account_budget_oca blocked (DEC-OCA-02).
- **WP-02 CONDITIONAL PASS:** CoA ✅; bill workflow ✅; payment dual-auth ✅; analytic accounts ✅.
- **WP-03 CONDITIONAL PASS:** compliance field ✅; purchase_request ✅; Call for Tender ✅; WP03-07 BLOCKED (B-02/B-03).
- **WP-04 CONDITIONAL PASS:** hr_recruitment ✅; org hierarchy ✅; leave workflows ✅; x_employment_state ✅; WP04-08 DEFERRED (B-WP04-02).
- **WP-ADM-01 CONDITIONAL PASS:** fleet register ✅; asset register ✅; helpdesk_mgmt ✅; mail.thread ✅; Driver + IT Officer groups PENDING (B-WP04-01).
- **WP-PC-01 CONDITIONAL PASS:** 5 PCU stages ✅; NADF Programme project ✅; milestone ✅; Director ACL ✅; mail.thread ✅; Director-only field restriction DEFERRED (DEC-PC01-002).
- **Single Claude Code session enforced.**

## WP-PC-01 exit gate summary
| Item | Result |
|------|--------|
| WP-PC-01-01 User groups | ✅ 4 groups confirmed — Director (1 user), PCU Head (0), PM (0), PTM (0) |
| WP-PC-01-02 NADF ERP Programme | ✅ id=2, status=on_track; NADF ERP Phase 1 id=3 (naming hierarchy) |
| WP-PC-01-02 5 PCU task stages | ✅ Initiation (14), Planning (15), Execution (16), M&C (17), Closure (18) |
| WP-PC-01-03 Test milestone | ✅ id=1, is_reached=True, reached_date=2026-06-26 |
| WP-PC-01-04 Director ACL | ✅ id=1062 'nadf.project.milestone.director' — full CRUD on project.milestone |
| WP-PC-01-04 Director-only restriction | ⚠️ DEFERRED — DEC-PC01-002; organizational control; Phase 2 technical enforcement |
| WP-PC-01-05 mail.thread | ✅ project.project (3 msgs) + project.task — AC-14 PASS |

## ➡️ CURRENT ACTIVE WORK PACKAGE

**Repository governance: PR #12 awaiting merge.** PRs #10 and #11 merged. PR #12 (WP-PC-01, this branch) pending reviewer approval.

**Wave C — next session after PR #12 merges:**
- DEC-OCA-02 resolution: investigate `account_budget_oca` patch (Option A)
- WP-05 UAT preparation
- M1-CPC sub-milestone closure assessment (per milestone model recommendation pending approval)

## Milestone model recommendation (pending approval)
A recommendation to split M1 into three sub-milestones has been produced in the Wave B Session 4 response:
- **M1-CPC** (Core Product Capability) — closes upon WP-PC-01 PASS: IMMINENT
- **M1-OPR** (Operational Readiness) — closes after WP-05 + DEC-OCA-02: Wave C
- **M1-PRD** (Production Readiness) — closes after client sign-offs: client-dependent
No implementation until recommendation is accepted by A1 Master Orchestrator.

## Open escalations
| ID | Description | Status |
|----|-------------|--------|
| DEC-OCA-02 | `account_budget_oca` — Option A investigate patch in Wave C | OPEN |
| WP02-08 | mis_builder dashboard — client KPI sign-off required | DEFERRED |

## Client actions required
| Item | Action | WP |
|------|--------|----|
| B-02 | Confirm procurement RACI step 1.19 (approver identity) | WP03-07 |
| B-03 | Confirm PO approval threshold(s) — current: ₦500K | WP03-07 |
| B-WP04-01 | Confirm dept assignments + reporting lines for 6 Admin-dept employees (IDs 12,13,14,18,20,23) | WP04-01/02, ADM01-06 |
| B-WP04-02 | Provide NADF RC number and TIN for company registration | WP04-08 |
| B-ADM01-01 | Provide vehicle license plates + confirm driver assignments | ADM01-01 |
| WP02-02 | Review and sign off `csv_templates/nadf_coa_revalidated_20260625.csv` | WP-02 |
| WP02-08 | Confirm NADF KPI set for mis_builder dashboard | WP-02 |

## Execution wave plan
```
Wave A:  Session 1 → WP-03 → PR #8 [MERGED be7ed8b]        ✅ CLOSED
         Session 2 → WP-04 → PR #10 [MERGED 5e3861e]        ✅ CLOSED
         WAVE_A_COMPLETION_REPORT.md produced
Wave B:  Session 3 → WP-ADM-01 → PR #11 [MERGED 6f7f4bb]    ✅ CLOSED
         Session 4 → WP-PC-01 → PR #12 [this branch — pending merge]   🔄 WAVE B COMPLETE
Wave C:  DEC-OCA-02 Option A investigation + WP-05 UAT preparation
```

## Single-session discipline
⚠️ Only one Claude Code session may be active at any time. Max safe concurrency: **1 executing + 1 in PR review**.

## Files to read before starting (any session)
1. `docs/NEXT_ACTION.md` (this file)
2. `docs/governance/GOVERNANCE_APPROVAL_REGISTER.md` (open escalations + deferred decisions — mandatory)
3. `docs/product/PHASE_1_EXECUTION_STRATEGY_REPORT.md` (execution model)
4. `docs/PRODUCT_STATE_INDEX.md` (session protocol)
5. `PROJECT_STATE.md`
6. `MILESTONE_TRACKER.md`
7. `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (bound authority)
