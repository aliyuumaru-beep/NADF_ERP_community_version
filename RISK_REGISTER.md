# RISK_REGISTER.md
## NADF ERP Programme — Risk Register (POD-NADF)

**Document type:** Mandatory Project Pod artifact (Agent OS) · Governance Activation Gate C input
**Authority:** `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md`
**Created:** 2026-06-22 (Migration Sequence M-C) · **Maintained by:** A1 Software Factory Orchestrator
**Sources:** `NADF_AGENT_OS_MIGRATION_BLUEPRINT.md` §8 (MR-01…MR-12); `PROJECT_STATE.md` §7 (R-01…R-07)
**Update rule:** Status updated on every milestone state change. Closed risks are retained (not deleted) with closure evidence.

**Likelihood / Impact:** High / Medium / Low · **Status:** Open · Mitigating · Mitigated · Closed

---

## 1. Migration & governance risks (MR-series)

| ID | Risk | L | I | Status | Mitigation / evidence |
|----|------|---|---|--------|-----------------------|
| MR-01 | `nadf_vendor_onboarding` orphaned & un-backed-up — total loss on disk failure | High | **Critical** | ✅ **Mitigated (M-C)** | Recovered into `nadf_erp/custom_addons/` (commit `a9738b4`); integrity PASS 12/12 (`DEC-RECOVERY-001`); pushed offsite (Step 9) |
| MR-02 | `nadf_facilities_management` mis-located in famoil-erp repo (Layering breach) | High | High | ✅ **Mitigated (M-C)** | Relocated to NADF layer (commit `4ccb306`); integrity PASS 33/33; removed from FamOil (`9a16f74`) + `nadf_*` guard (`DEC-RECOVERY-002`) |
| MR-03 | Governance Gate fails on first run (Gate B & residual C) | High | Medium | 🟡 Mitigating | Expected at baseline; B (CI) + closure-tier docs owned by M-D; A/D/E green in M-C |
| MR-04 | Legacy build ratified retroactively without G1/G2/G3 evidence | Medium | High | 🟡 Open | Kept "built/unratified"; no closure until per-dept G-reviews pass |
| MR-05 | DB `NADF` never backed up (10 phases unprotected) | High | High | ✅ **Mitigated (M-C)** | First backup `nadf_20260622_114439` + restore drill PASS (`BACKUP_STRATEGY.md` §9; `DEC-BACKUP-001`) |
| MR-06 | `phase/0-governance` work stranded off `main` | Medium | Medium | 🟡 Open | M-D: fold via PR; `main` protected in M-C (D-3) |
| MR-07 | Enterprise module silently present in instance | Medium | High | ✅ **Mitigated (M-C)** | Audit: 0 prohibited EE modules; `spreadsheet*` verified LGPL-3 CE core (`DEC-PLATFORM-001`); Gate E PASS |
| MR-08 | 7 departments lack TO-BE specs — sequencing gap | Medium | High | 🟡 Open | Build triggered only on TO-BE delivery; queued in BACKLOG; no unspecified build |
| MR-09 | Nigerian payroll statutory rates need legal input (`nadf_payroll_ng`) | High | High | 🟡 Open (E-01) | Spec gated on qualified adviser sign-off |
| MR-10 | `nadf_investment` large custom scope, no reference impl | Medium | High | 🟡 Open (E-03) | Client requirements session before any code |
| MR-11 | Quarantined scaffold accidentally extracted as authority | Low | High | 🟡 Open | Quarantine notice stands; author fresh artifacts only |
| MR-12 | OCA modules unverified for Odoo 17 CE compatibility | Medium | Medium | 🟡 Open | Compatibility check + version-pin + Decision Log entry per module before install (Phase 1) |

## 2. Programme risks carried from PROJECT_STATE §7 (R-series)

| ID | Risk | L | I | Status | Mitigation |
|----|------|---|---|--------|-----------|
| R-01 | Enterprise modules discovered requiring removal/replacement | Medium | High | ✅ Closed (M-C) | Audit found none (see MR-07 / `DEC-PLATFORM-001`) |
| R-02 | Remaining 7 departments without TO-BE specification | Medium | High | 🟡 Open | = MR-08; builds gated on TO-BE delivery |
| R-03 | OCA modules not yet evaluated for Odoo 17 CE compatibility | Medium | Medium | 🟡 Open | = MR-12; check during M-OCA-01 before install |
| R-04 | Nigerian payroll statutory rates require local legal input | High | High | 🟡 Open | = MR-09; E-01 |
| R-05 | `nadf_investment` large-scope custom work, no reference | Medium | High | 🟡 Open | = MR-10; E-03 |
| R-06 | UAT not started; go-live date unconfirmed | Medium | High | 🟡 Open | Phase 5 gate not opened until Phase 3 complete |
| R-07 | Governance gate likely to FAIL on first run (backup/CI) | High | Medium | 🟢 Largely addressed (M-C) | Backup ✅ (MR-05); CI remains M-D (MR-03) |

---

**M-C net effect:** MR-01, MR-02, MR-05, MR-07 and R-01 mitigated/closed; the Critical data-loss exposure is eliminated. Residual open risks are tracked above with owners; CI (MR-03/R-07 remainder) and branch-fold (MR-06) are M-D.
