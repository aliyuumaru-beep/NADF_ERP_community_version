# NADF ERP — National Agricultural Development Fund

Public-sector ERP implementation on **Odoo 17 Community Edition**, delivered by Lanasoft Technologies via the Software Factory Autonomous Agent Team. This repository is the **Layer 4 — Client Deployment** for NADF (`nadf_erp`), the first reference implementation for the Lanasoft Public-Sector ERP Template.

## Status

- **Platform:** Odoo 17 Community Edition (Enterprise modules prohibited). DB `NADF`, port `8071`.
- **Governance:** Agent OS migration — M-B/M-C/M-C-stabilization/M-D complete; **M0 governance gate 21/21**; legacy build (Phases 0–10) is **built / unratified** pending milestone ratification.
- **Programme completion:** ~20% of the full v2.1 scope (12 departments / 6 custom modules).

## Repository layout

| Path | Contents |
|------|----------|
| `PROJECT_STATE.md` | Operational cockpit — single source of current status (read first) |
| `MILESTONE_TRACKER.md` | Agent OS ↔ ROADMAP ↔ legacy milestone mapping |
| `RISK_REGISTER.md` · `CHANGELOG.md` · `IMPLEMENTATION_HISTORY.md` · `MODULE_REGISTRY.md` | Mandatory governance artifacts |
| `ROADMAP.md` | Summary → delegates to `planning/ROADMAP.md` |
| `planning/` | `PRODUCT_SCOPE.md`, `ROADMAP.md`, `BACKLOG.md`, `WORK_PACKAGES.md` |
| `requirements/PRODUCT_SCOPE/` | **Bound authority** — `NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` |
| `custom_addons/` | `nadf_vendor_onboarding`, `nadf_facilities_management` |
| `docs/` | Decision log, backup strategy, gate report, integrity evidence, session index |
| `scripts/` | Backup/restore + legacy configuration scripts |
| `.github/workflows/` | CI (manifest + python + XML checks) |

## Custom modules

- **`nadf_vendor_onboarding`** — public vendor portal with Claude AI PDF compliance analysis.
- **`nadf_facilities_management`** — reactive + preventive maintenance and inventory reporting.

See `MODULE_REGISTRY.md` for full detail.

## Running locally

```
/Users/mac/odoo17/odoo/venv/bin/python /Users/mac/odoo17/odoo/odoo-bin -c nadf.conf -d NADF
```
`addons_path` in `nadf.conf` includes `nadf_erp/custom_addons` (the authoritative module location). Backups: `scripts/backup_nadf.sh`; restore drill: `scripts/restore_nadf.sh`.

## Governance

Work follows the Software Factory Governance + Product Engineering Framework v1.1. Changes go through feature branches and PRs into the protected `main`. See `CLAUDE.md` for agent operating rules and `docs/PRODUCT_STATE_INDEX.md` for the session protocol.

## Authority hierarchy

`requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` (bound) → `planning/PRODUCT_SCOPE.md` → `ROADMAP` → `BACKLOG` → `WORK_PACKAGES`.
