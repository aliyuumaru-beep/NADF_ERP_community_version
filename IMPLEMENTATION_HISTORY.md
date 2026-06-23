# IMPLEMENTATION_HISTORY.md
## NADF ERP Programme — Implementation History (POD-NADF)

**Document type:** Mandatory repository artifact (`18_IMPLEMENTATION_HISTORY_STANDARD.md`, Repository Standard `10`)
**Created:** 2026-06-23 (Migration Sequence M-D) · **Maintained by:** A1 Software Factory Orchestrator
**Scope:** Milestones, phases, recoveries, backups/restore events, and significant operational changes. Append-only.

---

## 1. Legacy MVP build (out of governance sequence) — author `MAC`

| Date | Phase | Summary | Commit |
|------|-------|---------|--------|
| 2026-06-02 | Phase 0 | Inspection & foundation documents | `48f1738` |
| 2026-06-02 | Phase 1 | Company, fiscal year, users | `4479b0e` |
| 2026-06-03 | Phase 2 | Finance configuration | `44d3d33` |
| 2026-06-03 | Phase 3–4 | Procurement & HR configuration | `0c22549` |
| 2026-06-04 | Phase 5 | Approval workflows (base.automation) + decisions | `ec2fc32` |
| 2026-06-04 | Phase 6 | Demo scenarios live in `NADF` DB | `038ed67` |
| 2026-06-05 | Phase 7 | NADF government chart of accounts (319 accts) | `59feda0` |
| 2026-06-08 | Phase 8 | Assets, fleet, ICT helpdesk, staff roster | `05568b4` |
| 2026-06-09 | Phase 9 | `nadf_vendor_onboarding` built (then untracked in FamOil tree) | — |
| 2026-06-13 | Phase 10 | `nadf_facilities_management` built (then committed in famoil-erp `55c1787`) | — |

> All legacy work is **built / unratified** — delivered before M0 governance completed (see `docs/GOVERNANCE_COMPLIANCE_AUDIT.md`, Maturity Level 0). No milestone is closed.

## 2. Agent OS migration — author `A1 Software Factory Orchestrator`

### M-B — Bootstrap-enable (2026-06-21)
- Stood up `PROJECT_STATE.md`, `MILESTONE_TRACKER.md`, reconciled `planning/`; quarantined the stale Control-Tower scaffold zip. Commits `16c8cf7`, `d15b30d`.

### M-C — Governance Certification & Recovery (2026-06-22)
| Item | Evidence |
|------|----------|
| Recovered `nadf_vendor_onboarding` (MR-01, integrity 12/12) | `a9738b4` |
| Relocated `nadf_facilities_management` from `famoil-erp@55c1787` (MR-02, integrity 33/33) | `4ccb306` |
| FamOil contamination removed + `nadf_*` guard (local-only) | famoil `9a16f74` |
| RISK_REGISTER + DEC-PLATFORM-001/RECOVERY-001/002/BACKUP-001 | `c21cfd8` |
| Backup strategy + first restore drill | `ad43fa4` |
| Governance gate baseline (16/21) | `b52d15d` |
| PROJECT_STATE/MILESTONE_TRACKER reconcile | `a63cf99` |

### M-C incident stabilization (2026-06-22)
- **Configuration drift:** relocation left `nadf.conf` `addons_path` pointing only at the old `odoo17/custom_addons`; relocated modules undiscoverable. Corrected `addons_path` (added `nadf_erp/custom_addons`). Verified: `odoo-bin --stop-after-init` loaded 94 modules, exit 0. Commit `f53304c`. Second concurrent writer session later self-terminated; `f53304c` pushed.

### M-D — Closure-tier docs, CI, main fold (2026-06-23)
- Authored mandatory root docs (`README`, `CLAUDE.md`, `CHANGELOG`, `IMPLEMENTATION_HISTORY`, `MODULE_REGISTRY`, root `ROADMAP`), `docs/PRODUCT_STATE_INDEX.md` (session rules, BL-GOV-09), and CI (`.github/workflows/ci.yml`). Governance Gate re-run to full 21/21. PR opened to fold `phase/0-governance` → `main`.

## 3. RESTORE_EVENT log
*(Migrated from `docs/BACKUP_STRATEGY.md` §9 per Backup & Recovery Standard `20`.)*

| Date | Type | Backup set | Result | Verification |
|------|------|-----------|--------|--------------|
| 2026-06-22 | RESTORE_EVENT (first drill) | `nadf_20260622_114439` (dump 6,215,346 B; filestore 38,265,886 B) | **PASS** | Restored to `NADF_restore_drill`; installed_modules 94 = live 94; res_partner 40 = live 40; both NADF modules present; drill DB dropped |

**Backup-set SHA-256:** dump `48615c6d…641622` · filestore `f49c766b…6c69db1`.

## 4. Pending operational note
- Live Odoo instance (PID observed 7732) was running on the pre-fix in-memory `addons_path`; a graceful restart is advised so it adopts the corrected `nadf.conf`. The next restart is verified clean (§2 M-C incident).
