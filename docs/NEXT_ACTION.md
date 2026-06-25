# NADF ERP — Next Action

**Last updated:** 2026-06-25 (WP-03 Procurement Core — CONDITIONAL PASS)

## Current Milestone
**M1 — Foundation** (ROADMAP Phase 1). M0 CLOSED (PEG-6 2026-06-24). WP-01 CONDITIONAL PASS (PR #5 merged). WP-02 CONDITIONAL PASS (PR #6 merged `e58e15c`).

## Current State
- **main:** `e58e15c` (PR #6 merged). Branch: `feat/wp-03-procurement-core` (Go/No-Go PASS).
- **PR #7 OPEN:** `docs/wp-02-governance-outputs` — governance exit gate + DEC-OCA-02 + execution strategy; awaiting reviewer.
- **100 modules loaded**, registry exit 0. Odoo PID 54258.
- **WP-01 CONDITIONAL PASS:** 4/5 OCA installed; `account_budget_oca` blocked (DEC-OCA-02).
- **WP-02 CONDITIONAL PASS:** CoA validated; bill workflow ✅; payment dual-auth advisory ✅; analytic accounts ✅; reports ✅; tax accounts ✅.
- **WP-03 CONDITIONAL PASS:** compliance field ✅; purchase_request workflow ✅; Call for Tender + award ✅; goods receipt ✅; OCA contract deferred ✅; mail.thread ✅; WP03-07 BLOCKED (B-02/B-03).
- **Single Claude Code session enforced.**

## WP-03 exit gate summary
| Item | Result |
|------|--------|
| WP03-01 Compliance field | ✅ `x_compliance_status` on res.partner (3 compliant, 1 pending) |
| WP03-02 purchase_request | ✅ draft→to_approve→approved cycle — PASS |
| WP03-03 Call for Tender | ✅ T/REQ/001 → 2 RFQs → award → done |
| WP03-04 Goods receipt | ✅ NADF/IN/00004 state=done; stock.move confirmed |
| WP03-05 OCA contract | ✅ Evaluated — DEFERRED Phase 2/3 (DEC-CONTRACT-001) |
| WP03-06 mail.thread | ✅ 2 + 5 messages (AC-14 PASS) |
| WP03-07 Approval chain | ❌ BLOCKED — B-02/B-03 client pending; ₦500K untouched |

## ➡️ IMMEDIATE NEXT ACTION

**Merge PR #8 (WP-03), then begin WP-04 HR Core (Wave A, Session 2).**

WP-04 scope (Wave A Session 2 — while PR #8 in review):
- WP04-01: Re-validate employee records with 4-level org hierarchy
- WP04-02: Refine department assignments (11 staff at Administration — client input needed)
- WP04-03: Re-validate leave workflow (line manager → HR two-level)
- WP04-04: Re-validate recruitment pipeline stages
- WP04-05: Configure appointment/separation approval + CEO activity notification
- WP04-06: Verify mail.thread on `hr.employee`, `hr.leave`, `hr.applicant`
- WP04-07: Obtain client review record for leave types + org hierarchy
- WP04-08: Set NADF company VAT/RC number (currently empty)
- WP04-09: Set Claude API key in System Parameters for nadf_vendor_onboarding AI analysis (CH)

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
Wave A:  Session 1 → WP-03 execute → PR #8 [COMPLETE — awaiting merge]
         Session 2 → WP-04 execute → PR #9  (while PR #8 reviewed)
Wave B:  Session 3 → WP-ADM-01 execute → PR #10
         Session 4 → WP-PC-01 execute → PR #11 (after/while PR #10 reviewed)
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
