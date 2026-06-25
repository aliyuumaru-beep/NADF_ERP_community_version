# NADF ERP — Next Action

**Last updated:** 2026-06-25 (WP-01 Foundation Hardening — CONDITIONAL PASS)

## Current Milestone
**M1 — Foundation** (ROADMAP Phase 1). M0 formally closed (PEG-6 approved 2026-06-24). WP-01 executed (2026-06-25): 4/5 OCA modules installed, 22 user groups created, TOTP 2FA enforced, registry exit 0.

## Current State
- **WP-01 CONDITIONAL PASS** — 4/5 OCA modules installed; `account_budget_oca` blocked (DEC-OCA-02).
- **100 modules loaded**, registry exit 0, no ERROR/CRITICAL lines for Phase 1 modules.
- **22 user groups created**: Finance×4, Procurement×4, HR×5, Administration×5, Project Coordination×4.
- **TOTP 2FA policy = `required`** globally (DEC-2FA-002).
- **`account_budget_oca` BLOCKED** — escalated to G1/G2/G3. Blocks WP02-07 (budget config only). All other WP-02 tasks unaffected.
- Odoo running PID 54258 on updated `nadf.conf` (addons_path includes `/Users/mac/oca_addons`).
- **Single Claude Code session enforced** — only one active session permitted at any time.

## Open escalation: DEC-OCA-02 — account_budget_oca

`account_budget_oca` 17.0.1.0.0 failed with `Field 'theoritical_amount' does not exist` on `account.analytic.account`. G1/G2/G3 must decide before WP02-07:
- **(a)** Upgrade to a later OCA patch release that fixes the field reference
- **(b)** Use CE native `account_budget` module (non-OCA alternative, conflicts with OCA — mutual exclusion)
- **(c)** Defer budget configuration to a future WP with an approved alternative

## Next Recommended Actions (in order)

**➡️ 1. G1/G2/G3 resolve DEC-OCA-02** (account_budget_oca compatibility) — decision required before WP02-07 budget configuration.

**➡️ 2. Merge PR #5** (WP-01 implementation commit) — requires independent reviewer approval.

**➡️ 3. Implement WP-02 — Finance Core** (re-validate legacy CoA, vendor-bill and payment workflows, analytic accounts; budget config deferred pending DEC-OCA-02 resolution).

**➡️ 4. Implement WP-ADM-01** (fleet, assets, helpdesk_mgmt configuration) — parallel with WP-02 after WP-01 exit gate.

**➡️ 5. Implement WP-PC-01** (project coordination structure, milestone model, user groups) — parallel with WP-02/ADM-01.

**➡️ 6. Proceed to WP-03 (Procurement) → WP-04 (HR) → WP-05 (UAT Preparation).**

## Remaining blockers
- **DEC-OCA-02** — `account_budget_oca` compatibility resolution (blocks WP02-07 only).
- **WP-PROC-02** — Procurement approval chain still blocked on B-02/B-03 (client confirmation required).
- **Retrospective specs** — `nadf_vendor_onboarding` and `nadf_facilities_management` require specs before ratification.

## Single-session discipline
⚠️ **Only one Claude Code session may be active at any time.** Confirm before starting any WP implementation.

## Files to read before starting (any session)
1. `docs/NEXT_ACTION.md` (this file)
2. `docs/PRODUCT_STATE_INDEX.md` (session protocol)
3. `PROJECT_STATE.md`
4. `MILESTONE_TRACKER.md`
5. `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (bound authority)
