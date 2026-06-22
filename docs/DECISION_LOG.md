# NADF ERP MVP — Decision Log
**Document:** DECISION_LOG.md
**Version:** 1.0
**Last Updated:** 2026-06-04
**Format:** Follows Software Factory Decision Log Standard

> Every major architectural, configuration, and governance decision is recorded here.
> Do not delete entries. To reverse a decision, add a new entry referencing the original.

---

## DEC-001 — Fresh Database Strategy

**Date:** 2026-06-02
**Type:** ARCHITECTURE
**Status:** ACTIVE
**Made By:** Operator + AI Developer

### Decision
Create a fresh `NADF` PostgreSQL database. Do not clone from FamOil, WamaCare, or OdooClean.

### Context
Three existing databases with working Odoo 17 installations were available locally. The question was whether to clone one as the base for NADF.

### Rationale
- Clean lineage: no inherited module state, demo data, or configuration debt
- Predictable: every module installed and every config made is traceable
- Template-repeatable: the setup process becomes a documented playbook for future public sector deployments
- Operator instruction confirmed this approach

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Clone FamOil | Carries manufacturing, sales, agro-processing modules not needed for NADF |
| Clone OdooClean | Missing hr_holidays, purchase, l10n_ng — would need many installs anyway |
| Restore from dump | Unknown module state; harder to document from scratch |

### Consequences
All configuration must be built from scratch. Compensated by reusable scripts (`phase1_`–`phase5_`) that make the setup reproducible.

---

## DEC-002 — Odoo Community Edition Over Enterprise

**Date:** 2026-06-02
**Type:** TECHNOLOGY
**Status:** ACTIVE
**Made By:** Operator (project constraint)

### Decision
Use Odoo 17 Community Edition. Do not install Enterprise modules or paid third-party modules.

### Context
The NADF MVP product document was written assuming some Enterprise features (Approvals app, Sign, Documents). The local installation is Community Edition.

### Rationale
- Existing infrastructure is Community Edition (shared with FamOil and WamaCare)
- Zero licence cost is appropriate for MVP/demo stage
- Community covers Finance, Procurement, HR adequately for the MVP objective
- Enterprise features can be added in Phase 2 (production) if needed

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Install Enterprise `approvals` | Not available on Community — not installable |
| Install `sign` module | Enterprise only |
| Install `documents` module | Enterprise only |
| Purchase OCA approval module | Not approved for MVP; requires written justification |

### Consequences
Multi-level approval workflows require `base.automation` workaround (see DEC-005). Sign and Documents excluded from MVP scope.

---

## DEC-003 — Shared Addons Path Strategy

**Date:** 2026-06-02
**Type:** ARCHITECTURE
**Status:** ACTIVE
**Made By:** AI Developer

### Decision
NADF `nadf.conf` references `/Users/mac/odoo17/custom_addons/` directly rather than copying addons into `/Users/mac/nadf_erp/custom_addons/`.

### Context
Six OCA/community custom addons (`om_account_*`, `accounting_pdf_reports`) are installed in the FamOil addons directory and are needed for NADF.

### Rationale
- Avoids duplication of addon code
- NADF benefits from any fixes applied to the shared addons
- NADF is an MVP/demo — not a production environment with strict isolation needs

### Alternatives Considered

| Alternative | Reason Rejected |
|-------------|----------------|
| Copy addons to nadf_erp/custom_addons | Duplication; maintenance burden if addons are updated |
| Install addons via pip/git | Unnecessary complexity for local dev environment |

### Consequences
If shared addons are modified incompatibly for FamOil, NADF may be affected. Risk is low given MVP/demo nature of NADF and the maturity of these addons.

**Revisit condition:** If NADF moves to production or a separate server, isolate the addons.

---

## DEC-004 — January–December Fiscal Year

**Date:** 2026-06-02
**Type:** OPERATIONAL
**Status:** ACTIVE
**Made By:** Operator (confirmed explicitly)

### Decision
Configure NADF fiscal year as January 1 – December 31 (calendar year). FY 2026 and FY 2027 created.

### Context
Nigerian government agencies may use October–September fiscal year (aligned with the Federal Government budget cycle). NADF as a development fund may follow either convention.

### Rationale
Operator confirmed January–December. Consistent with many parastatal/development fund practice of using calendar year for management accounts even when budget is government-cycle.

### Consequences
If NADF's actual financial reporting uses a different fiscal year, the `account.fiscal.year` records must be recreated and the accounting lock dates adjusted.

---

## DEC-005 — Activity-Based Approval Workaround (Community Edition)

**Date:** 2026-06-04
**Type:** ARCHITECTURE / GOVERNANCE_EXCEPTION
**Status:** ACTIVE
**Made By:** AI Developer (approved by operator blanket approval for Phase 5)

### Decision
Implement multi-level procurement and payment approval using `base.automation` + `ir.actions.server` activity scheduling instead of the Enterprise `approvals` app.

### Context
The NADF approval matrix specifies three-tier procurement approval (₦500K / ₦5M thresholds) and three-tier payment approval (₦1M / ₦10M thresholds). Odoo Community Edition has:
- Purchase module: one configurable approval threshold (configured at ₦500K)
- No native multi-level approval matrix

### Implementation
Five automated rules created:
1. PO Tier 2 (₦500K–₦5M): activity for Director CS
2. PO Tier 3 (>₦5M): activity for Executive Secretary + Director CS FYI
3. Invoice Tier 2 (₦1M–₦10M): activity for Director CS on bill posting
4. Invoice Tier 3 (>₦10M): activity for Executive Secretary + Director CS FYI
5. Study Leave ES: activity for Executive Secretary after HR validates Study Leave

### Limitation Accepted
Activities are advisory — the system does not hard-block confirmation of a high-value PO or payment by a lower-tier user. This is an accepted limitation for the MVP demo stage.

### Revisit Conditions
- Production deployment: develop `nadf_approvals` custom module with Python-level permission checks on `action_confirm` methods
- OR upgrade to Odoo Enterprise for native `approvals` app

---

## DEC-006 — Head HR as Universal Leave Time Off Officer

**Date:** 2026-06-04
**Type:** OPERATIONAL
**Status:** ACTIVE
**Made By:** AI Developer (approved by operator blanket approval for Phase 5)

### Decision
Set all employees' `leave_manager_id` to Head HR (Kabir Haruna, uid=11). Head HR's own leave manager is set to Director CS.

### Context
Odoo's `leave_manager_id` field is the "Time Off Officer" — the person who gives HR-level leave approval. The choice was whether to cascade approvals through line managers or centralise at HR.

### Rationale
- For a public sector organisation, leave is centrally controlled by HR
- Casual/Sick leave still routes through the line manager via `leave_validation_type = 'manager'`
- Annual/Maternity/Study routes through HR via `leave_validation_type = 'hr'` or `'both'`
- Simple, predictable, easy to demonstrate

### Consequences
If NADF wishes to route Annual Leave through line managers first, change `leave_validation_type` for Annual Leave from `'hr'` to `'both'`.

---

## DEC-007 — Study Leave Three-Level Workaround

**Date:** 2026-06-04
**Type:** ARCHITECTURE
**Status:** ACTIVE
**Made By:** AI Developer (approved by operator blanket approval for Phase 5)

### Decision
Study Leave is configured as `leave_validation_type = 'both'` (Manager + Head HR), with an additional `base.automation` activity to Executive Secretary after final HR validation.

### Context
The NADF approval matrix requires Study Leave to go to Executive Secretary. Odoo Community `hr_holidays` supports maximum 2 approval levels (manager + Time Off Officer). A third level requires custom code or automation.

### Limitation Accepted
The Executive Secretary activity is created after HR has already given final approval (state = 'validate'). This means the leave is technically approved before the ES activity is completed. For production, this flow should be reversed (ES approves before HR final validation).

### Revisit Conditions
Production deployment: develop `nadf_hr_leave` custom module to add a third approval state before final validation.

---

## DEC-008 — Port 8071 for NADF Instance

**Date:** 2026-06-02
**Type:** OPERATIONAL
**Status:** ACTIVE
**Made By:** AI Developer

### Decision
Assign port 8071 to the NADF Odoo instance.

### Context
Port 8069 is used by FamOil. Port 8070 is used by WamaCare. All three instances run simultaneously on the same macOS machine during development.

### Consequences
nadf.conf sets `http_port = 8071`. All NADF access uses `http://localhost:8071`.

---

## DEC-RECOVERY-001 — Recover `nadf_vendor_onboarding` into the NADF Deployment Layer

**Date:** 2026-06-22
**Type:** GOVERNANCE / LAYERING
**Status:** ACTIVE
**Made By:** A1 Software Factory Orchestrator (M-C)

### Decision
Recover the `nadf_vendor_onboarding` custom module from the FamOil working tree (where it existed only as **untracked** files, in no repository and with no backup) into `nadf_erp/custom_addons/nadf_vendor_onboarding/`, and commit it to the NADF deployment repository.

### Context
The module was built during legacy Phase 9 but was never committed to any repository — it lived as untracked files under `/Users/mac/odoo17/custom_addons/` (the FamOil repo's working tree). This was the single CRITICAL data-loss exposure recorded as risk MR-01.

### Rationale
- Closes MR-01 (orphaned production code, no backup).
- Restores the Project Layering Model: NADF (Layer 4) assets belong in the NADF deployment repository, not in another client's working tree.
- Recovery verified byte-identical by SHA-256 manifest comparison (12/12 files) — see `docs/MC_RECOVERY_INTEGRITY.md`.

### Consequences
Module is now version-controlled in NADF and will be pushed offsite (Step 9). The untracked FamOil copy is removed in M-C Section C **after** integrity PASS was recorded. No functional re-validation (install) was performed in M-C — that is deferred to M1 ratification.

---

## DEC-RECOVERY-002 — Relocate `nadf_facilities_management` out of the FamOil Repository

**Date:** 2026-06-22
**Type:** GOVERNANCE / LAYERING
**Status:** ACTIVE
**Made By:** A1 Software Factory Orchestrator (M-C)

### Decision
Relocate the `nadf_facilities_management` custom module from the **famoil-erp** repository (committed at `odoo17@55c1787`, unpushed) into `nadf_erp/custom_addons/nadf_facilities_management/`, and remove it from the FamOil repository via a forward `git rm` removal commit (Decision D-1: forward removal, not history rewrite).

### Context
A NADF (Layer 4) module had been committed inside the FamOil (Layer 4) deployment repository — a cross-layer contamination breach of the Project Layering Model, recorded as risk MR-02. The contaminating commit `55c1787` had not been pushed to any remote, so removal is local-only and low-risk.

### Rationale
- Closes MR-02 (cross-contamination breach).
- Forward removal preserves FamOil history and avoids rewriting another pod's repository.
- Recovery verified byte-identical by SHA-256 manifest comparison (33/33 files, matching the 33-file footprint of `55c1787`) — see `docs/MC_RECOVERY_INTEGRITY.md`.
- A `.gitignore` guard (`custom_addons/nadf_*`) is added to the FamOil repo to prevent recurrence.

### Consequences
Provenance recorded as `odoo17@55c1787`. FamOil HEAD no longer contains the module; `55c1787` remains in FamOil history/reflog as the audit trail. No functional re-validation performed in M-C (deferred to M1).

---

## DEC-PLATFORM-001 — Odoo 17 Community Edition Confirmed and Version-Locked

**Date:** 2026-06-22
**Type:** PLATFORM / TECHNOLOGY
**Status:** ACTIVE
**Made By:** A1 Software Factory Orchestrator (M-C) — supersedes the assumption-level confirmation in DEC-002 with audited evidence

### Decision
Confirm and version-lock the platform as **Odoo 17 Community Edition**. The platform profile `23_PLATFORM_PROFILE_ODOO17_COMMUNITY.md` is the bound profile for POD-NADF. Zero prohibited Enterprise modules are installed.

### Context
Governance Activation Gate E requires an audited confirmation that the platform is Community and free of Enterprise modules, recorded in the Decision Log.

### Evidence (read-only audit of the `NADF` database, 2026-06-22)
- 94 modules installed; query against the prohibited Enterprise list returned only `spreadsheet` and `spreadsheet_dashboard`.
- Both are **author = Odoo S.A., license = LGPL-3, category = Hidden**, shipped in the **Community core addons path** (`odoo/odoo/addons/`) — i.e. CE technical modules, **not** Enterprise. The Enterprise-only `documents_spreadsheet` is **not** installed.
- `account_accountant` (an Enterprise marker module) is **absent**, confirming Community Edition.

### Decision outcome
**No prohibited Enterprise modules present. Gate E: PASS.** No removal action required. Any future need for Enterprise-only capability must follow the platform profile approach order (Native → Config → OCA → SF modules → Custom) and be escalated, never assumed.

### Consequences
Platform locked to Odoo 17 CE. The blueprint's name-based caution on `spreadsheet_dashboard` is resolved: the installed variant is the LGPL-3 CE base, not the Enterprise edition.

---

## DEC-BACKUP-001 — Backup Cadence and Recovery Objectives (RPO/RTO)

**Date:** 2026-06-22
**Type:** OPERATIONS / GOVERNANCE
**Status:** ACTIVE
**Made By:** A1 Software Factory Orchestrator (M-C)

### Decision
Adopt the backup cadence and recovery objectives defined in `docs/BACKUP_STRATEGY.md`:
- **Cadence:** daily automated backup of the `NADF` database **coordinated with** the filestore (`~/Library/Application Support/Odoo/filestore/NADF`); 30-day retention.
- **RPO (Recovery Point Objective):** ≤ 24 hours (maximum acceptable data loss).
- **RTO (Recovery Time Objective):** ≤ 4 hours (maximum acceptable downtime to restore service).

### Context
Risk MR-05: the `NADF` database (10 phases of configuration) had never been backed up and no restore had ever been drilled. Governance Activation Gate D requires a documented backup strategy, a documented restore procedure, and a recent verified backup.

### Rationale
- Closes MR-05; satisfies Gate D.
- Database-and-filestore coordination is mandatory per the Backup & Recovery Governance Standard (`20`) — a DB backup without the matching filestore is an incomplete backup.

### Consequences
First full backup taken and a restore drill performed during M-C (recorded in the `BACKUP_STRATEGY.md` Drill Log; migrates to `IMPLEMENTATION_HISTORY.md` in M-D). Backups are stored under `backups/` (gitignored — never committed).

---

*Decision Log maintained by: AI Developer (Claude Code)*
*Follows: Software Factory Decision Log Standard (software-factory-governance/governance/DECISION_LOG_STANDARD.md)*
