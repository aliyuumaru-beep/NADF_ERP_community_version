# NADF ERP — Next Action

**Last updated:** 2026-06-25 (WP-02 Finance Core — CONDITIONAL PASS)

## Current Milestone
**M1 — Foundation** (ROADMAP Phase 1). WP-01 complete (CONDITIONAL PASS). WP-02 Finance Core re-validated (CONDITIONAL PASS). WP-02 exit gate: 9/11 done; WP02-07 blocked (DEC-OCA-02); WP02-08 deferred pending client KPI sign-off.

## Current State
- **100 modules loaded**, registry exit 0. Odoo PID 54258.
- **WP-01 CONDITIONAL PASS:** 4/5 OCA installed; `account_budget_oca` blocked.
- **WP-02 CONDITIONAL PASS:** CoA validated (319 accounts); bill workflow ✅; payment advisory dual-auth ✅; analytic accounts ✅; financial reports ✅; tax accounts ✅.
- **Finance users assigned:** `finance.officer` → Finance Officer; `head.finance` → Finance Manager + CFO.
- **Open escalations:**
  - **DEC-OCA-02** — `account_budget_oca` incompatible; blocks WP02-07 only; G1/G2/G3 resolution required.
  - **WP02-08** — mis_builder dashboard deferred; client KPI sign-off required.
- **CoA CSV exported:** `csv_templates/nadf_coa_revalidated_20260625.csv` — pending client review record.
- **Single Claude Code session enforced.**

## Open escalation: DEC-OCA-02 — account_budget_oca

G1/G2/G3 must decide:
- **(a)** Upgrade to later OCA/account-budgeting patch release (check if newer 17.0.x fixes the field)
- **(b)** Use CE native `account_budget` (conflicts with OCA version — mutual exclusion; acceptable if OCA version not required)
- **(c)** Defer budget configuration to a future WP

## Client actions required
- **WP02-02:** Client review of `csv_templates/nadf_coa_revalidated_20260625.csv` — sign-off required
- **WP02-08:** Client to confirm mis_builder KPI set before dashboard configuration
- **WP02-11:** Client to confirm WHT/VAT tax rule configuration before any amendment
- **WP03-07:** Procurement approval chain — client confirmation of RACI step 1.19 (B-02) and thresholds (B-03) required

## Next Recommended Actions (in order)

**➡️ 1. Merge PR #6** (WP-02 implementation) — requires independent reviewer.

**➡️ 2. Implement WP-03 — Procurement Core** (`purchase_request` requisition, `purchase_requisition` RFQ/tender, vendor compliance field, goods receipt).

**➡️ 3. Implement WP-04 — HR Core** (employee records, leave workflow, recruitment pipeline, org hierarchy refinement).

**➡️ 4. Implement WP-ADM-01** (fleet register, asset register, helpdesk_mgmt ICT configuration).

**➡️ 5. Implement WP-PC-01** (project structure, milestone model, PCU groups).

**➡️ 6. G1/G2/G3 resolve DEC-OCA-02** (account_budget_oca) — unblocks WP02-07.

## Single-session discipline
⚠️ Only one Claude Code session may be active at any time.

## Files to read before starting (any session)
1. `docs/NEXT_ACTION.md` (this file)
2. `docs/PRODUCT_STATE_INDEX.md` (session protocol)
3. `PROJECT_STATE.md`
4. `MILESTONE_TRACKER.md`
5. `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (bound authority)
