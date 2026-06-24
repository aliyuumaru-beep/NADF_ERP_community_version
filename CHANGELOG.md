# Changelog

All notable changes to the NADF ERP deployment (`nadf_erp`, Layer 4) are recorded here.
Format follows the Software Factory Release & Git Governance Standard (`14`); commit types: `feat`, `fix`, `governance`, `docs`, `ops`, `chore`. Dates are absolute.

## [Unreleased]

### PEG-6 — Product Authorization package prepared (2026-06-24)
- **docs:** Added `docs/governance/PEG_6_PRODUCT_AUTHORIZATION_PACKAGE.md` — 14-section Product Authorization Package (baseline, legacy ratification, Phase-1 scope, risks, governance/repository/backup/platform status, WP-01..05, governance reviews, agent activation, Go/No-Go, approval statement). Recommendation: **CONDITIONAL GO** pending PEG-6 approval + sponsor sign-off + single-session + Odoo restart + scope freeze.
- **docs:** Updated `docs/NEXT_ACTION.md` to point to PEG-6 review/approval as the next action; `IMPLEMENTATION_HISTORY.md` governance-only entry added.
- **scope:** No ERP development authorized; no functional Odoo module or configuration changed. Development remains blocked pending PEG-6 approval.

### M-D — Closure-tier documentation & CI (2026-06-23)
- **docs:** Added mandatory repository files — `README.md`, `CLAUDE.md`, `CHANGELOG.md`, `IMPLEMENTATION_HISTORY.md`, `MODULE_REGISTRY.md`, root `ROADMAP.md` summary.
- **docs:** Added `docs/PRODUCT_STATE_INDEX.md` with session start/end rules (BL-GOV-09) — closes Gate C7.
- **ci:** Added `.github/workflows/ci.yml` (manifest parse + `py_compile` + XML well-formedness) and PR template — closes Gate B.
- **governance:** Governance Activation Gate re-run to full **21/21 PASS**; PR opened to fold `phase/0-governance` → `main`.

### M-C incident stabilization (2026-06-22)
- **fix(stabilization):** `nadf.conf` `addons_path` now includes `nadf_erp/custom_addons` so the relocated modules are discoverable; verified `odoo-bin --stop-after-init` loads 94 modules, exit 0 (`f53304c`).

### M-C — Governance certification & recovery (2026-06-22)
- **fix(recovery):** Recovered `nadf_vendor_onboarding` from the FamOil untracked tree into `custom_addons/` (integrity 12/12, MR-01) (`a9738b4`).
- **fix(recovery):** Relocated `nadf_facilities_management` from `famoil-erp@55c1787` into `custom_addons/` (integrity 33/33, MR-02) (`4ccb306`).
- **governance:** Added `RISK_REGISTER.md`; logged `DEC-PLATFORM-001`, `DEC-RECOVERY-001/002`, `DEC-BACKUP-001` (`c21cfd8`).
- **ops:** Added backup strategy + tooling; first DB+filestore backup and restore drill **PASS** (MR-05) (`ad43fa4`).
- **governance:** Governance gate baseline report 16/21; `main` pushed and branch-protected (`b52d15d`, `a63cf99`).
- **docs:** `docs/MC_RECOVERY_INTEGRITY.md` — SHA-256 recovery integrity evidence.

### M-B — Bootstrap-enable (2026-06-21)
- **governance:** Stood up `PROJECT_STATE.md`, `MILESTONE_TRACKER.md`; reconciled `planning/`; quarantined stale scaffold (`16c8cf7`, `d15b30d`).

## Legacy MVP build (Phases 0–10, 2026-06-02 → 2026-06-13) — pre-governance, unratified
- Phase 0–8 Odoo 17 CE configuration (Finance, Procurement, HR, Administration, CoA, assets/fleet/helpdesk) — commits `48f1738`…`05568b4`.
- Phase 9 `nadf_vendor_onboarding`; Phase 10 `nadf_facilities_management` (recovered under M-C).
- Status: **built / unratified** — delivered out of governance sequence; no milestone closed.

---
*No release tag yet. First tag will be `v1.0-go-live` at Phase 6 deployment (see `planning/ROADMAP.md`).*
