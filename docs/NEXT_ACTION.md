# NADF ERP — Next Action

**Last updated:** 2026-06-25 (Post-WP-02 governance outputs complete)

## Current Milestone
**M1 — Foundation** (ROADMAP Phase 1). WP-01 CONDITIONAL PASS. WP-02 CONDITIONAL PASS. WP-02 exit gate report issued (`docs/governance/WP_02_EXIT_GATE_REPORT.md`). DEC-OCA-02 governance review issued (`docs/governance/DEC_OCA_02_GOVERNANCE_REVIEW.md`). Execution strategy confirmed (`docs/product/PHASE_1_EXECUTION_STRATEGY_REPORT.md`).

## Current State
- **100 modules loaded**, registry exit 0. Odoo PID 54258.
- **WP-01 CONDITIONAL PASS:** 4/5 OCA installed; `account_budget_oca` blocked.
- **WP-02 CONDITIONAL PASS:** CoA validated (319 accounts); bill workflow ✅; payment advisory dual-auth ✅; analytic accounts ✅; financial reports ✅; tax accounts ✅.
- **Finance users assigned:** `finance.officer` → Finance Officer; `head.finance` → Finance Manager + CFO.
- **PR #6 merged** (`feat/wp-02-finance-core`). Main is clean.
- **Single Claude Code session enforced.**

## Governance Documents Issued (this session)

| Document | Path | Status |
|---------|------|--------|
| WP-02 Exit Gate Report | `docs/governance/WP_02_EXIT_GATE_REPORT.md` | ISSUED — CONDITIONAL PASS |
| DEC-OCA-02 Governance Review | `docs/governance/DEC_OCA_02_GOVERNANCE_REVIEW.md` | ISSUED — Option A (investigate patch) recommended first; Option C fallback |
| Phase 1 Execution Strategy | `docs/product/PHASE_1_EXECUTION_STRATEGY_REPORT.md` | ISSUED — Hybrid Wave model; Level 2 concurrency |

## Recommended Execution Model
**Hybrid, two-wave, Level 2 concurrency** (see `docs/product/PHASE_1_EXECUTION_STRATEGY_REPORT.md`).

```
Wave A:   Session 1 → WP-03 execute → PR #7
          Session 2 → WP-04 execute → PR #8  (while PR #7 in review)
          [PRs #7 + #8 merged]

Wave B:   Session 3 → WP-ADM-01 execute → PR #9
          Session 4 → WP-PC-01 execute → PR #10  (after/while PR #9 reviewed)
          [PRs #9 + #10 merged]

Session 5:  DEC-OCA-02 Option A investigation + WP-05 UAT preparation
```

## ➡️ IMMEDIATE NEXT ACTION (awaiting user confirmation)

**Confirm PR #6 is merged, then begin WP-03 Procurement Core — Session 1, Wave A.**

WP-03 scope:
- WP03-01: Re-validate vendor compliance-status field on `res.partner`
- WP03-02: Configure `purchase_request` multi-step requisition
- WP03-03: Configure `purchase_requisition` RFQ/tender workflow
- WP03-04: Re-validate goods receipt and stock flow
- WP03-05: Evaluate OCA `contract` fit; log DEC-CONTRACT-001
- WP03-06: Verify `mail.thread` audit on `purchase.request` and `purchase.order`
- WP03-07: **BLOCKED** — client must confirm B-02 (RACI step 1.19) and B-03 (approval thresholds) first

## Open Escalations

| ID | Description | Owner | Status |
|----|-------------|-------|--------|
| DEC-OCA-02 | `account_budget_oca` incompatible — Option A investigation required | D2 / G1 | OPEN — see `docs/governance/DEC_OCA_02_GOVERNANCE_REVIEW.md` |
| WP02-08 | mis_builder dashboard — client KPI sign-off required | Business Sponsor | DEFERRED |

## Client Actions Required

| Item | Action required | WP affected |
|------|----------------|------------|
| WP02-02 | Review and countersign `csv_templates/nadf_coa_revalidated_20260625.csv` | WP-02 amendment |
| WP02-08 | Confirm NADF KPI set for mis_builder dashboard | WP-02 amendment |
| WP02-11 | Confirm WHT/VAT configuration before any amendment | WP-02 amendment |
| WP03-07 | Confirm RACI step 1.19 (B-02) and approval thresholds (B-03) | WP-03 |
| WP04-02 | Confirm department assignments for 11 Administration-tagged staff | WP-04 |
| WP04-07 | Confirm leave types and org hierarchy for HR UAT | WP-04 |

## Single-session discipline
⚠️ Only one Claude Code session may be active at any time. Maximum safe concurrency: **1 WP executing + 1 WP in PR review**.

## Files to read before starting (any session)
1. `docs/NEXT_ACTION.md` (this file)
2. `docs/product/PHASE_1_EXECUTION_STRATEGY_REPORT.md` (execution model)
3. `docs/PRODUCT_STATE_INDEX.md` (session protocol)
4. `PROJECT_STATE.md`
5. `MILESTONE_TRACKER.md`
6. `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (bound authority)
