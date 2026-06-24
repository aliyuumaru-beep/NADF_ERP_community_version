# NADF ERP — Next Action

**Last updated:** 2026-06-24 (PEG-6 package prepared)

## Current Milestone
M0 — Governance Remediation (ROADMAP Phase 0). Agent OS migration M-B → M-C → **M-D complete**; governance baseline folded into `main` (`989b65f`). Governance Activation Gate: **21/21 PASS**. **PEG-6 Product Authorization package prepared** — awaiting review/approval.

## Current State
- Both custom modules recovered and version-controlled in `nadf_erp/custom_addons/`; FamOil contamination removed.
- Backup + restore drill PASS; `main` pushed and branch-protected; CI active.
- All mandatory governance + Repository-Standard docs present.
- Legacy build (Phases 0–10) remains **built / unratified**.
- `docs/governance/PEG_6_PRODUCT_AUTHORIZATION_PACKAGE.md` prepared (recommendation: CONDITIONAL GO).

## Next Recommended Action
**➡️ PEG-6 review and approval is the next action.** Route `docs/governance/PEG_6_PRODUCT_AUTHORIZATION_PACKAGE.md` to the Business Sponsor + Governance for sign-off. This is the sole remaining item to close milestone M0 and the precondition for any Phase-1 development.

PEG-6 recommendation is **CONDITIONAL GO**, effective only after: (a) PEG-6 approval; (b) business sponsor sign-off; (c) single active Claude Code session enforced; (d) live Odoo service restarted onto the corrected `addons_path`; (e) product scope baseline frozen at Transfer Package v2.1.

**Until PEG-6 is approved, no new ERP configuration, module install/upgrade, or business feature may begin — development remains blocked.**

## Not yet started (gated)
- Phase 1 foundation ratification + OCA installs (no install without compatibility check + Decision Log entry).
- Custom-module specs (Phase 2) — no spec, no code.
- Department builds — gated on TO-BE delivery.

## Files to read before starting (any session)
1. `docs/NEXT_ACTION.md` (this file)
2. `docs/PRODUCT_STATE_INDEX.md` (session protocol)
3. `PROJECT_STATE.md`
4. `MILESTONE_TRACKER.md`
5. `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (bound authority)
