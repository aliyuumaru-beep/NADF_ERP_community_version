# NADF ERP — Next Action

**Last updated:** 2026-06-23 (M-D)

## Current Milestone
M0 — Governance Remediation (ROADMAP Phase 0). Agent OS migration M-B → M-C → **M-D complete**. Governance Activation Gate: **21/21 PASS**.

## Current State
- Both custom modules recovered and version-controlled in `nadf_erp/custom_addons/`; FamOil contamination removed.
- Backup + restore drill PASS; `main` pushed and branch-protected; CI active.
- All mandatory governance + Repository-Standard docs present.
- Legacy build (Phases 0–10) remains **built / unratified**.

## Next Recommended Actions
1. **Merge the `phase/0-governance → main` PR** — requires one non-author approval (branch protection; `enforce_admins=true`). This folds M-B/M-C/M-D governance work into `main`.
2. **Obtain the PEG-6 signed Product Approval** (Product Owner + Governance) — authorises Phase-1 development and ratification of the legacy build. Until then, no new ERP configuration.
3. **Operational:** schedule a graceful restart of the live NADF Odoo instance so it adopts the corrected `nadf.conf` `addons_path` (next restart verified clean).

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
