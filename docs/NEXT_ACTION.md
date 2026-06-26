# NADF ERP — Next Action

**Last updated:** 2026-06-26 (WP-ADM-01 Administration Core — CONDITIONAL PASS · Wave B Session 3)

## Current Milestone
**M1 — Foundation** (ROADMAP Phase 1). M0 CLOSED. Wave A CLOSED. Wave B AUTHORIZED. WP-01/02/03/04/ADM-01 all CONDITIONAL PASS.

## Current State
- **main:** `be7ed8b` (PR #8 merged). Odoo PID 59090, 105 modules, exit 0.
- **PR #9 OPEN:** `docs/wp-02-governance-outputs-v2` — governance recovery; awaiting reviewer.
- **PR #10 OPEN:** `feat/wp-04-hr-core` — WP-04 HR Core CONDITIONAL PASS (pending merge).
- **PR #11 OPEN:** `feat/wp-adm-01-administration-core` — WP-ADM-01 Administration Core CONDITIONAL PASS (this branch).
- **Wave A CLOSED:** WAVE_A_COMPLETION_REPORT.md produced. M1 NOT ACHIEVED (WP-ADM-01 + WP-PC-01 pending).
- **WP-01 CONDITIONAL PASS:** 4/5 OCA installed; account_budget_oca blocked (DEC-OCA-02).
- **WP-02 CONDITIONAL PASS:** CoA ✅; bill workflow ✅; payment dual-auth ✅; analytic accounts ✅.
- **WP-03 CONDITIONAL PASS:** compliance field ✅; purchase_request ✅; Call for Tender ✅; WP03-07 BLOCKED (B-02/B-03).
- **WP-04 CONDITIONAL PASS:** hr_recruitment ✅; org hierarchy ✅; leave workflows ✅; x_employment_state ✅; WP04-08 DEFERRED (B-WP04-02).
- **WP-ADM-01 CONDITIONAL PASS:** fleet register ✅; asset register ✅; helpdesk_mgmt ✅; mail.thread ✅; Driver + IT Officer groups PENDING (B-WP04-01).
- **Single Claude Code session enforced.**

## WP-ADM-01 exit gate summary
| Item | Result |
|------|--------|
| WP-ADM-01-01 Fleet register | ✅ 5 vehicles Registered; years set. Plates PENDING (R-ADM01-03). Drivers PENDING (B-WP04-01) |
| WP-ADM-01-02 Fuel log | ✅ 5 service logs + odometer entries |
| WP-ADM-01-03 Asset register | ✅ 5 categories; 61 assets; 3 validated (open + depreciation lines) |
| WP-ADM-01-04 helpdesk_mgmt | ✅ 5 categories, NADF ICT Helpdesk team. SLA: priority proxy (DEC-ADM01-001) |
| WP-ADM-01-05 Test ticket | ✅ Created → Done; 3 mail.thread messages |
| WP-ADM-01-06 User groups | ✅ IT Mgr + Fleet Mgr + Asset Mgr assigned (director.cs). Driver + IT Officer PENDING |
| WP-ADM-01-07 mail.thread | ✅ fleet.vehicle + account.asset.asset + helpdesk.ticket — AC-14 PASS |
| WP-ADM-01-08 wkhtmltopdf | ⚠️ NOT INSTALLED — R-ENV-001 documented |

## ➡️ IMMEDIATE NEXT ACTION

**Begin WP-PC-01 Project Coordination (Wave B, Session 4) — while PR #11 awaits review.**

WP-PC-01 scope (Wave B Session 4):
- WP-PC-01-01: Re-validate Project Coordination groups (4 groups from WP-01: Project Team Member, Project Manager, PCU Head, Director)
- WP-PC-01-02: Configure project.project types and stages for NADF project lifecycle
- WP-PC-01-03: Re-validate project task/kanban workflow
- WP-PC-01-04: Verify mail.thread on project.project, project.task
- WP-PC-01-05: Configure programme/project hierarchy (parent project for NADF programme)

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
Wave A:  Session 1 → WP-03 → PR #8 [MERGED be7ed8b]   ✅ CLOSED
         Session 2 → WP-04 → PR #10 [open]             ✅ CLOSED
         WAVE_A_COMPLETION_REPORT.md produced
Wave B:  Session 3 → WP-ADM-01 → PR #11 [this branch]  ✅ CLOSED
         Session 4 → WP-PC-01 → PR #12 (while PR #11 reviewed)   🔄 NEXT
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
