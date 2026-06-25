# NADF ERP — Next Action

**Last updated:** 2026-06-25 (WP-03 Go/No-Go PASS — execution authorised)

## Current Milestone
**M1 — Foundation** (ROADMAP Phase 1). M0 CLOSED (PEG-6 2026-06-24). WP-01 CONDITIONAL PASS (PR #5 merged). WP-02 CONDITIONAL PASS (PR #6 merged `e58e15c`).

## Current State
- **main:** `e58e15c` (PR #6 merged). Branch: `feat/wp-03-procurement-core` (Go/No-Go PASS).
- **PR #7 OPEN:** `docs/wp-02-governance-outputs` — governance exit gate + DEC-OCA-02 + execution strategy; awaiting reviewer.
- **100 modules loaded**, registry exit 0. Odoo PID 54258.
- **WP-01 CONDITIONAL PASS:** 4/5 OCA installed; `account_budget_oca` blocked (DEC-OCA-02).
- **WP-02 CONDITIONAL PASS:** CoA validated; bill workflow ✅; payment dual-auth advisory ✅; analytic accounts ✅; reports ✅; tax accounts ✅.
- **WP-03 Go/No-Go: PASS** — `purchase_request` and `purchase_requisition` installed; `mail.thread` confirmed; branch clean; G1/G2/G3 cleared. **Pre-work backup required before first mutating operation.**
- **Single Claude Code session enforced.**

## Governance documents issued
| Document | Path | Status |
|---------|------|--------|
| WP-02 Exit Gate Report | `docs/governance/WP_02_EXIT_GATE_REPORT.md` | ISSUED — in PR #7 |
| DEC-OCA-02 Governance Review | `docs/governance/DEC_OCA_02_GOVERNANCE_REVIEW.md` | ISSUED — Option A investigate; Option C fallback |
| Phase 1 Execution Strategy | `docs/product/PHASE_1_EXECUTION_STRATEGY_REPORT.md` | ISSUED — Hybrid Wave model |
| WP-03 Work Package Definition | `docs/work_packages/WP_03_PROCUREMENT_CORE.md` | ISSUED — Go/No-Go PASS |

## ➡️ IMMEDIATE NEXT ACTION

**Begin WP-03 Procurement Core implementation. Pre-work backup first.**

WP-03 scope (6 active items; 1 blocked):
- WP03-01: Create `x_compliance_status` on `res.partner` (no field exists — must create)
- WP03-02: Configure `purchase_request` multi-step requisition (picking type, approval groups)
- WP03-03: Configure `purchase_requisition` "Call for Tender" type + RFQ award flow
- WP03-04: Validate goods receipt — PO → receipt → stock.move in NADF Main Warehouse
- WP03-05: Evaluate OCA `contract` fit; log DEC-CONTRACT-001
- WP03-06: Functional mail.thread test on purchase.request and purchase.order
- WP03-07: **BLOCKED** — client must confirm B-02 (RACI 1.19) and B-03 (thresholds). Existing ₦500K threshold must NOT be changed without B-03 sign-off.

## Open escalations
| ID | Description | Status |
|----|-------------|--------|
| DEC-OCA-02 | `account_budget_oca` — Option A investigate patch in Session 5 | OPEN |
| WP02-08 | mis_builder dashboard — client KPI sign-off required | DEFERRED |

## Client actions required
| Item | Action | WP |
|------|--------|----|
| B-02 | Confirm procurement RACI step 1.19 (approver identity) | WP03-07 |
| B-03 | Confirm PO approval threshold(s) — current: ₦500K (Phase 3 legacy) | WP03-07 |
| WP02-02 | Review and sign off `csv_templates/nadf_coa_revalidated_20260625.csv` | WP-02 amendment |
| WP02-08 | Confirm NADF KPI set for mis_builder dashboard | WP-02 amendment |
| WP04-02 | Confirm department assignments for 11 Administration-tagged staff | WP-04 |
| WP04-07 | Confirm leave types and org hierarchy | WP-04 |

## Execution wave plan
```
Wave A [active]:  Session 1 → WP-03 execute → PR #8
                  Session 2 → WP-04 execute → PR #9  (while PR #8 reviewed)
Wave B [pending]: Session 3 → WP-ADM-01 execute → PR #10
                  Session 4 → WP-PC-01 execute → PR #11 (after/while PR #10 reviewed)
Wave C [pending]: DEC-OCA-02 Option A investigation + WP-05 UAT preparation
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
