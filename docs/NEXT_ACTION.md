# NADF ERP — Next Action

**Last updated:** 2026-06-26 (WP-04 HR Core — CONDITIONAL PASS)

## Current Milestone
**M1 — Foundation** (ROADMAP Phase 1). M0 CLOSED (PEG-6 2026-06-24). WP-01 CONDITIONAL PASS (PR #5). WP-02 CONDITIONAL PASS (PR #6). WP-03 CONDITIONAL PASS (PR #8 merged `be7ed8b`). WP-04 CONDITIONAL PASS (PR #10 pending).

## Current State
- **main:** `be7ed8b` (PR #8 merged). Odoo PID 59090, 105 modules, exit 0.
- **PR #9 OPEN:** `docs/wp-02-governance-outputs-v2` — governance recovery; awaiting reviewer.
- **PR #10 PENDING:** `feat/wp-04-hr-core` — WP-04 HR Core CONDITIONAL PASS.
- **WP-01 CONDITIONAL PASS:** 4/5 OCA installed; `account_budget_oca` blocked (DEC-OCA-02).
- **WP-02 CONDITIONAL PASS:** CoA validated; bill workflow ✅; payment dual-auth ✅; analytic accounts ✅; reports ✅.
- **WP-03 CONDITIONAL PASS:** compliance field ✅; purchase_request workflow ✅; Call for Tender ✅; goods receipt ✅; mail.thread ✅; WP03-07 BLOCKED (B-02/B-03).
- **WP-04 CONDITIONAL PASS:** hr_recruitment installed ✅; org hierarchy ✅; leave workflows ✅; recruitment pipeline ✅; x_employment_state + CEO automations ✅; mail.thread ✅; WP04-08 DEFERRED (B-WP04-02); B-WP04-01 (6 Admin employees pending client).
- **Single Claude Code session enforced.**

## WP-04 exit gate summary
| Item | Result |
|------|--------|
| WP04-00 hr_recruitment install | ✅ 105 modules, exit 0 |
| WP04-01 Manager hierarchy | ✅ 8 corrections; ES → Dir → Mgr → Officer |
| WP04-02 Admin employees | ⚠️ 6 employees pending B-WP04-01 |
| WP04-03 Leave approval workflows | ✅ 4 types corrected to `both` |
| WP04-04 Recruitment pipeline | ✅ 5-stage NADF pipeline; Appointment=hired_stage |
| WP04-05 Employment state + CEO automation | ✅ x_employment_state id=11644; 2 automations active |
| WP04-06 mail.thread | ✅ hr.employee + hr.leave + hr.applicant — AC-14 PASS |
| WP04-07 HR group assignments | ✅ All 5 groups populated; leave workflow wired |
| WP04-08 Company RC/TIN | ⚠️ DEFERRED — B-WP04-02 client action |
| WP04-09 Claude API key | ✅ Pre-confirmed SET |

## ➡️ IMMEDIATE NEXT ACTION

**Push PR #10 (WP-04), then begin WP-ADM-01 Administration Core (Wave B, Session 3).**

WP-ADM-01 scope (Wave B Session 3):
- WP-ADM-01-01: Re-validate vehicle register (`fleet`) — 5 Toyota vehicles from legacy Phase 8
- WP-ADM-01-02: Re-validate asset register (`account_asset`) — 61 accounting assets, 421 maintenance.equipment records
- WP-ADM-01-03: Re-validate ICT helpdesk (`helpdesk_mgmt`) — 6 stages, 10 fault tags, 77 historical tickets
- WP-ADM-01-04: Configure Administration user groups and access rights (5 groups from WP-01)
- WP-ADM-01-05: Verify mail.thread on fleet.vehicle, account.asset, helpdesk.ticket
- WP-ADM-01-06: Confirm wkhtmltopdf gap (known from nadf_facilities_management Phase 8)

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
| B-WP04-01 | Confirm dept assignments + reporting lines for 6 Admin-dept employees (IDs 12,13,14,18,20,23) | WP04-01/02 |
| B-WP04-02 | Provide NADF RC number and TIN for company registration | WP04-08 |
| WP02-02 | Review and sign off `csv_templates/nadf_coa_revalidated_20260625.csv` | WP-02 amendment |
| WP02-08 | Confirm NADF KPI set for mis_builder dashboard | WP-02 amendment |

## Execution wave plan
```
Wave A:  Session 1 → WP-03 execute → PR #8 [MERGED be7ed8b]
         Session 2 → WP-04 execute → PR #10 [COMPLETE — push pending]
Wave B:  Session 3 → WP-ADM-01 execute → PR #11
         Session 4 → WP-PC-01 execute → PR #12 (after/while PR #11 reviewed)
Wave C:  DEC-OCA-02 Option A investigation + WP-05 UAT preparation
```

## Single-session discipline
⚠️ Only one Claude Code session may be active at any time. Max safe concurrency: **1 executing + 1 in PR review**.

## Files to read before starting (any session)
1. `docs/NEXT_ACTION.md` (this file)
2. `docs/product/PHASE_1_EXECUTION_STRATEGY_REPORT.md` (execution model)
3. `docs/PRODUCT_STATE_INDEX.md` (session protocol)
4. `PROJECT_STATE.md`
5. `MILESTONE_TRACKER.md`
6. `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (bound authority)
