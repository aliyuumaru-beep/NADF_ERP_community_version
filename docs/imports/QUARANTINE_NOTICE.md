# QUARANTINE NOTICE — Control Tower Scaffold (ARCHIVED ONLY)

**Status:** 🚫 QUARANTINED — archived for historical reference only. **NOT an authority source.**
**Applied:** 2026-06-21 (Migration Sequence M-B)
**Applied by:** A1 Software Factory Orchestrator

---

## Quarantined artifact
- `NADF_ERP_ControlTower_RepoScaffold_v2_2026-06-19.zip` (in this directory)

## Binding rulings
1. **Do NOT extract** this zip into the repository.
2. **Do NOT cite** it as an authority for project state, decisions, platform, milestones, or department status.
3. It may be read **only** as historical context, and must always be labelled as superseded.

## Why it is quarantined
1. **Platform-tainted.** Its internal `CONTROL_TOWER.md`, `DECISION_LOG.md`, `CHANGELOG.md`, and `IMPLEMENTATION_HISTORY.md` assert **Odoo 17 Enterprise**. The authoritative platform is **Odoo 17 Community Edition** (`docs/DECISION_LOG.md` DEC-002; Transfer Package v2.1; `PLATFORM_PROFILE_ODOO17_COMMUNITY.md`).
2. **Decision-log ID collision.** The scaffold's `DECISION_LOG.md` uses IDs **DEC-001…020 for swimlane rendering standards**, whereas the repository's authoritative `docs/DECISION_LOG.md` uses **DEC-001…008 for architecture/platform decisions**. Extracting the scaffold would overwrite or corrupt the real decision log.
3. **History blind-spot.** Its history files predate and omit the legacy MVP Odoo build (Phases 0–8) and both custom modules.

## Authoritative sources to use instead
| Concern | Authoritative source |
|---------|----------------------|
| Product definition | `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` |
| Current state | `PROJECT_STATE.md` |
| Milestones | `MILESTONE_TRACKER.md` |
| Backlog | `planning/BACKLOG.md` |
| Roadmap / scope | `planning/ROADMAP.md`, `planning/PRODUCT_SCOPE.md` |
| Decisions | `docs/DECISION_LOG.md` |
| Platform | `PLATFORM_PROFILE_ODOO17_COMMUNITY.md` |

> Note: the older `docs/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.md` (v2.0) is likewise **superseded** by v2.1 and must not be used as the active authority.
