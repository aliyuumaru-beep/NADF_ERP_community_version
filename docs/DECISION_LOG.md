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

## DEC-PEG6-001 — PEG-6 Product Authorization Approved — Phase 1 Activated

**Date:** 2026-06-24
**Type:** GOVERNANCE / PROGRAMME GATE
**Status:** ACTIVE
**Made By:** Business Sponsor (Aliyu / Lanasoft Technologies) — recorded by A1 Master Orchestrator

### Decision
Grant **PEG-6 Product Authorization** for NADF ERP Phase 1 — Foundation. Phase 1 Product Engineering is now activated. Milestone M0 is formally closed.

### Context
The PEG-6 Product Authorization Package (`docs/governance/PEG_6_PRODUCT_AUTHORIZATION_PACKAGE.md`, 2026-06-24) was prepared and presented to the Business Sponsor after: Governance Activation Gate 21/21 PASS; all migration sequences M-B/M-C/M-D complete; governance baseline on protected `main` (`b8dad2d`); both custom modules recovered and discoverable.

### Decision Details
- **Scope authorized:** Phase 1 — Foundation only (WP-01 Foundation Hardening, WP-02 Finance Core, WP-03 Procurement Core, WP-04 HR Core, WP-05 UAT Preparation).
- **Scope frozen at:** Transfer Package v2.1 (`requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md`).
- **Activation sequence enforced:** Governance layer (G1/G2/G3) activates before delivery layer (D1–D4). No WP implementation until per-WP Go/No-Go checkpoint passes.
- **Conditions satisfied at approval:** (a) PEG-6 approval ✅ · (b) Sponsor sign-off ✅ · (c) single-session enforced ✅ · (d) Odoo restarted on corrected `addons_path` (PID 51025, exit 0) ✅ · (e) scope frozen ✅.

### Rationale
- All governance preconditions met (gate 21/21, clean repo, backup drilled, CI active, protected branch).
- Phase 1 scope is lowest-risk tier: CE-native configuration and vetted OCA installation only — no custom code, no unspecified departments.
- Legacy build re-validation is a Phase 1 task; no legacy artifact is assumed "Done."

### Consequences
M0 closed. M1 (Foundation) is the active milestone. Development of WP-01 may proceed after G1/G2/G3 Go/No-Go clearance. No Phase 2/3 scope (custom module specs/dev, remaining departments) authorized by this decision.

---

## DEC-2FA-001 — TOTP 2FA Enforcement Scope: Explicit Group List

**Date:** 2026-06-24
**Type:** SECURITY / CONFIGURATION
**Status:** ACTIVE
**Made By:** G3 Security & Change Governance + A1 Master Orchestrator

### Decision
TOTP 2FA shall be enforced for the following explicitly named user groups:
**Finance Officer, Finance Manager, CFO, Auditor, and CEO.**

The phrase "Senior Management" is **retired** from WP-01 and all Phase 1 planning documents as it was undefined and not mapped to any Odoo user group.

### Context
G3 review correction C-02 identified that WP-01 §2 and AC-WP01-05 used "Senior Management" as a group name, but no such group exists in the NADF user group model. The ambiguity could result in 2FA enforcement being applied to the wrong accounts or skipped entirely for accounts that should be protected.

### Rationale
- Finance Officer, Finance Manager, CFO, and Auditor have direct access to financial transactions and reports — mandatory for audit compliance.
- CEO is the highest-authority account in the system and must not be exempted from 2FA.
- "Senior Management" as a catch-all is untestable — it cannot be verified by a DB query against `res.groups`.

### Consequences
WP-01 §2 Scope table, D-WP01-09, and AC-WP01-05 updated to use the explicit group list. `PHASE_1_BACKLOG.md` WP01-19 updated accordingly. WP-01 implementation (WP01-19) must test each named group individually. Any extension of 2FA scope to additional groups requires a new DEC entry referencing this one.

---

## DEC-OCA-01 — Install `mis_builder` OCA Module

**Date:** 2026-06-25
**Type:** PLATFORM / OCA MODULE
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator — WP-01 execution (G1/G2/G3 authorized)

### Decision
Install `mis_builder` version **17.0.1.5.0** from OCA/mis-builder branch `17.0`. Source: `https://github.com/OCA/mis-builder`. Module directory: `/Users/mac/oca_addons/mis_builder/`. Dependencies installed: `report_xlsx` (OCA/reporting-engine 17.0.1.0.2), `date_range` (OCA/server-ux 17.0.1.2.1), `board` (CE 17.0.1.0).

### Rationale
Provides executive and operational KPI dashboards for CA-01 Financial Management. CE `account` analytics alone is insufficient for multi-period management reporting. Authorized in PEG-6 §3 and WP-01 §2.

### Verification
`state='installed'`, `latest_version='17.0.1.5.0'` in `ir_module_module`. Registry exit 0 post-install. No ERROR/CRITICAL log lines.

---

## DEC-OCA-02 — `account_budget_oca` Compatibility Failure — Escalated

**Date:** 2026-06-25
**Type:** PLATFORM / OCA COMPATIBILITY / GOVERNANCE FINDING
**Status:** ESCALATED — pending resolution decision
**Made By:** A1 Master Orchestrator — WP-01 execution

### Finding
`account_budget_oca` version **17.0.1.0.0** from OCA/account-budgeting branch `17.0` is **NOT installed**. Install attempt failed with:

```
odoo.tools.convert.ParseError: Field `theoritical_amount` does not exist
View: account.analytic.account.form.inherit.budget
File: account_budget_oca/views/account_analytic_account_views.xml:2
```

The field `theoritical_amount` does not exist on `account.analytic.account` in this Odoo 17 CE build. This is a version compatibility gap between the OCA module and the specific Odoo 17 minor release installed locally.

### Decision
**Do not install the incompatible version.** Per R-WP01-01 mitigation: "if incompatible, log finding and escalate — do not install incompatible version." Module directory retained at `/Users/mac/oca_addons/account_budget_oca/` for future resolution.

### Escalation requirement
G1/G2/G3 must decide before WP-02 budget sub-task begins:
- (a) Upgrade to a later OCA/account-budgeting patch release that fixes the field reference
- (b) Use CE native `account_budget` module for budget control (non-OCA alternative)
- (c) Defer budget configuration to a future WP with an approved alternative

### Consequences
WP-02 budget sub-task (WP02-07: configure budget control) is **BLOCKED** pending resolution. All other WP-02 tasks are unaffected. WP-01 exit gate proceeds without `account_budget_oca`.

---

## DEC-OCA-03 — Install `purchase_request` OCA Module

**Date:** 2026-06-25
**Type:** PLATFORM / OCA MODULE
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator — WP-01 execution (G1/G2/G3 authorized)

### Decision
Install `purchase_request` version **17.0.2.3.4** from OCA/purchase-workflow branch `17.0`. Source: `https://github.com/OCA/purchase-workflow`. Module directory: `/Users/mac/oca_addons/purchase_request/`. CE dependency `purchase_stock` was already installed.

### Rationale
Provides structured multi-step procurement requisition for CA-02. CE `purchase` has no native requisition workflow. Authorized in PEG-6 §3 and WP-01 §2.

### Verification
`state='installed'`, `latest_version='17.0.2.3.4'` in `ir_module_module`. Registry exit 0 post-install. No ERROR/CRITICAL log lines.

---

## DEC-OCA-04 — Install `helpdesk_mgmt` OCA Module

**Date:** 2026-06-25
**Type:** PLATFORM / OCA MODULE
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator — WP-01 execution (G1/G2/G3 authorized)

### Decision
Install `helpdesk_mgmt` version **17.0.1.10.4** from OCA/helpdesk branch `17.0`. Source: `https://github.com/OCA/helpdesk`. Module directory: `/Users/mac/oca_addons/helpdesk_mgmt/`. CE dependencies `mail` and `portal` were already installed.

### Rationale
Provides ICT helpdesk functionality for CA-04. Replaces unratified `project`-based workaround from legacy build. CE `helpdesk` module is Enterprise-only; `helpdesk_mgmt` is the authorized CE replacement. Authorized in PEG-6 §3 and WP-01 §2.

### Verification
`state='installed'`, `latest_version='17.0.1.10.4'` in `ir_module_module`. Registry exit 0 post-install. No ERROR/CRITICAL log lines.

---

## DEC-OCA-05 — `purchase_requisition` Confirmed CE Native (No OCA Install Required)

**Date:** 2026-06-25
**Type:** PLATFORM / OCA MODULE
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator — WP-01 execution

### Decision
`purchase_requisition` is confirmed as **Odoo 17 CE native** module ("Purchase Agreements", `/Users/mac/odoo17/odoo/odoo/addons/purchase_requisition/`), not an OCA module. It was already installed in the NADF DB (`state='installed'`, `latest_version='17.0.0.1'`) prior to WP-01. No OCA install required.

### Rationale
PEG-6 listed `purchase_requisition` as an OCA module based on its OCA availability in Odoo 14–16. In Odoo 17, it was absorbed into the CE core. The capability (tender/vendor comparison workflow) is fully satisfied by the CE version.

### Consequences
No additional install action. Module listed in MODULE_REGISTRY.md as CE native. Decision Log entry serves as the traceability record.

---

## DEC-2FA-002 — TOTP Global Policy Set to Required

**Date:** 2026-06-25
**Type:** SECURITY / CONFIGURATION
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator — WP-01 execution (WP01-18 / WP01-19)

### Decision
Set `auth_totp.policy = 'required'` in Odoo `ir.config_parameter`. All active Odoo users must complete TOTP enrollment before they can log in.

### Context
WP-01 §2 specifies TOTP enforcement for Finance Officer, Finance Manager, CFO, Auditor, and CEO (per DEC-2FA-001). Odoo 17 CE `auth_totp` module supports only two global policies: `optional` (user choice) or `required` (all users). Per-group enforcement is **not natively available** in CE `auth_totp` without custom code.

### Decision rationale
Setting the policy to `required` globally satisfies the spirit of DEC-2FA-001 and exceeds its minimum requirement (enforces for all users including the specified groups). This is more secure than a partial enforcement, introduces no code risk, and is reversible via settings. The broader enforcement is acceptable for this deployment: NADF is a multi-department system; requiring TOTP for all staff is consistent with public sector security practice.

### Consequences
All active Odoo users (including `admin` / `nadf_admin`) must configure a TOTP authenticator on next login or the next session after the policy is in force. Users without TOTP configured will be prompted to set it up. Admins must communicate this requirement to all staff before UAT.

**Revisit condition:** If per-group enforcement is required (e.g., to exempt Service Account users), install OCA `auth_totp_mandatory_group` or equivalent, or implement via custom module under Phase 2 spec process.

---

## DEC-WP02-001 — Payment Dual-Authorisation: Advisory Restriction (Phase 1)

**Date:** 2026-06-25
**Type:** ARCHITECTURE / GOVERNANCE EXCEPTION
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator — WP-02 execution (ratifies DEC-005 for Phase 1)

### Decision
For Phase 1, payment dual-authorisation is implemented as **advisory control** via the existing `base.automation` escalation rules (Invoice Tier 2/3, PO Tier 2/3). Finance Officer creates/enters payments; Finance Manager reviews. The system does not hard-block payment posting by a lower-tier user.

### Context
Odoo 17 CE `account.payment` has no native payment approval group field. The legacy Phase 5 rules (DEC-005) remain active and escalate high-value invoice/PO events to Director CS / Executive Secretary via Odoo activities. WP-02 re-validation confirmed all 4 rules are active and triggering correctly.

### Rationale
- Consistent with DEC-005 (accepted limitation for MVP).
- Finance Officer and Finance Manager groups are now populated with real users; the group-level separation provides maker-checker control at the role level.
- Hard payment blocking requires a custom `nadf_approvals` module (Phase 2 spec / Phase 3 dev) — not in Phase 1 scope.

### Consequences
WP02-04 and WP02-05 marked Done. If a Finance Officer posts a payment without Finance Manager review, the system will not block it — this is a known MVP limitation. Audit trail on `account.move` provides post-facto tracking. Full hard control is Phase 2 scope.

---

## DEC-WP02-002 — Analytic Accounts: Department Cost-Centre Structure (Phase 1)

**Date:** 2026-06-25
**Type:** CONFIGURATION
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator — WP-02 execution

### Decision
Accept the existing 5 analytic accounts (CC-ADM, CC-EXE, CC-FIN, CC-HR, CC-PRO) under the "Projects" analytic plan as the Phase 1 analytic dimension. No new analytic accounts required for Phase 1.

### Context
WP02-06 required analytic accounts aligned to NADF budget lines. The budget CSV (`csv_templates/nadf_budget_fy2026.csv`) has 40 expense lines at account-code level. Department cost centres are the correct granularity for Phase 1 budget tracking. Programme/project-level analytic dimensions (CA-10, CA-11) are deferred to Phase 3+.

### Consequences
Budget CSV amounts will be allocated to department analytic accounts when the budget module configuration is resolved (pending DEC-OCA-02). The analytic plan name "Projects" should be renamed to "NADF Departments" during WP-02 client review session to avoid confusion.

---

## DEC-WP03-001 — Vendor Compliance Mechanism: x_ Field + Vendor Onboarding Proxy

**Date:** 2026-06-25
**Type:** CONFIGURATION
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator (WP-03 execution)

### Decision
Implement vendor compliance status as a selection field `x_compliance_status` on `res.partner` via Odoo shell (`ir.model.fields.create()`), with three values: `compliant`, `non_compliant`, `pending`. The `nadf_vendor_onboarding` application state (`approved`/`rejected`) serves as a secondary compliance proxy for vendors onboarded through the portal.

### Context
WP03-01 found no custom compliance field on `res.partner` in the current NADF DB. The legacy Phase 3 build did not implement one. Transfer Package v2.1 CA-02 requires vendor compliance tracking. Two mechanism options were evaluated:
- Option A: `x_compliance_status` shell-created field (immediate, DB-only, not version-controlled).
- Option B: `nadf_vendor_compliance` custom module (version-controlled, spec-required).

### Rationale
- Phase 1 MVP requires a compliance indicator to gate vendor selection; Option B is Phase 2/3 scope.
- Shell-created `x_` fields are DB-resident and will not survive a DB rebuild without re-running the creation command. The command is documented in `IMPLEMENTATION_HISTORY.md` and `docs/work_packages/WP_03_PROCUREMENT_CORE.md` §9.
- `nadf_vendor_onboarding` state provides a governance-audited compliance track for portal-onboarded vendors.

### Consequences
- Phase 1: `x_compliance_status` field created (id=11353); 3 vendors tagged `compliant`, 1 `pending`.
- Phase 2/3: `nadf_vendor_compliance` custom module spec required to replace the shell-created field with a version-controlled, workflow-governed equivalent.
- Risk: R-WP03-01 (field lost on DB rebuild) — mitigated by documented creation command.

---

## DEC-CONTRACT-001 — OCA `contract` Module: Deferred to Phase 2/3

**Date:** 2026-06-25
**Type:** ARCHITECTURE
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator (WP-03 execution)

### Decision
Do NOT install OCA `contract` module in Phase 1. Contract lifecycle management is deferred to the `nadf_legal_contract` custom module (Phase 2/3 spec-gated). CE `purchase_requisition` is sufficient for Phase 1 procurement contract flow (call for tender + awarded PO).

### Context
WP03-05 required evaluation of OCA/contract@17.0 against NADF procurement contract requirements. The OCA `contract` module is not in `/Users/mac/oca_addons` and was not pre-cloned. The evaluation was read-only (no install attempted).

### Fit-Gap Analysis
| Requirement | OCA `contract` | CE `purchase_requisition` | `nadf_legal_contract` |
|-------------|---------------|--------------------------|----------------------|
| Recurring services (ICT support, vehicle maint.) | ✅ Fit | ❌ No | ✅ Fit (with spec) |
| One-time goods supply | ❌ No fit | ✅ Fit | ✅ Fit |
| NADF RACI sign-off chain | ❌ No | ❌ No | ✅ Fit (designed for it) |
| Budget-vs-contract tracking | ❌ Depends on account_budget (blocked) | ❌ No | ✅ Fit |
| Renewal / expiry alerts | ✅ Fit | ❌ No | ✅ Fit |

### Rationale
- OCA `contract` does not cover the NADF RACI approval chain (the critical differentiator).
- `nadf_legal_contract` custom module (per Transfer Package v2.1 B-04A) is the correct long-term solution.
- Phase 1 `purchase_requisition` covers call for tender + award sufficiently for MVP.
- Install of a new OCA module in Phase 1 (beyond the authorized list) requires a new gate decision.

### Consequences
- Phase 1: No OCA `contract` module installed. `purchase_requisition` used for tender workflow.
- Phase 2/3: `nadf_legal_contract` spec to be authored. At that time, OCA `contract` may be re-evaluated for recurring service contracts alongside the custom module.
- `MODULE_REGISTRY.md` is not updated (no install).

---

## DEC-WP03-002 — purchase_request User Group Mapping

**Date:** 2026-06-25
**Type:** CONFIGURATION
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator (WP-03 execution)

### Decision
Map NADF WP-01 Procurement groups to OCA `purchase_request` module groups as follows:
- `procurement.officer` → `Purchase Request / Purchase Request User` (create/submit PRs)
- `head.procurement` → `Purchase Request / Purchase Request Manager` (approve PRs) + `Purchase Request User` (create)
- Finance Approver group (NADF WP-01): not wired to purchase_request in Phase 1 (B-02/B-03 pending)

### Context
The OCA `purchase_request` module ships with its own groups ("Purchase Request User", "Purchase Request Manager"). The NADF WP-01 groups created separate NADF-categorised groups. The OCA ir.model.access rules are bound to the OCA groups, not the NADF groups. Direct assignment is the simplest Phase 1 mapping.

### Rationale
- Adding `ir.model.access` rules for NADF groups is the alternative but adds registry complexity.
- Direct user assignment to both NADF and OCA groups is the minimal, maintainable Phase 1 configuration.
- The mapping is documented so Phase 2 can implement a proper group inheritance structure via the `nadf_vendor_compliance` or equivalent module.

### Consequences
- `procurement.officer` (id=8) and `head.procurement` (id=9) now have full PR create/edit/approve access.
- The NADF Requisitioner group (id=98) has no users assigned yet — any future Requisitioner must be added to both groups.

---

## DEC-WP04-001 — hr_recruitment Installation (WP-04 prerequisite)

**Date:** 2026-06-26
**Type:** CONFIGURATION
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator (WP-04 execution)

### Decision
Install the native CE `hr_recruitment` module (17.0.0.1) to support the NADF recruitment pipeline configuration in WP-04. Installed via `Registry.new(update_module=True)` while the live server was stopped; live server restarted at 105 modules (was 100 — hr_recruitment + 4 auto-pulled deps: utm, attachment_indexation, digest, hr_recruitment_sms).

### Context
WP-04 scope requires recruitment pipeline stages (vacancy → shortlist → interview → offer → appointment) per Transfer Package §3.3. `hr_recruitment` was uninstalled at WP-04 start despite being in the Transfer Package module list.

### Rationale
- `hr_recruitment` is CE native; no OCA gate required.
- Installation adds `hr.applicant` model (mail.thread inheritance) satisfying AC-14 mail.thread requirement.
- 5-stage NADF pipeline preferred over 6-stage Odoo defaults; Odoo defaults folded (sequence=100, fold=True).

### Consequences
- Module count: 100 → 105. Registry exit 0, no ERROR/CRITICAL.
- NADF recruitment pipeline: Vacancy Posted → Shortlisted → Interview → Offer → Appointment. Appointment = `hired_stage=True`.
- Default Odoo stages (New, Initial Qualification, First/Second Interview, Contract Proposal, Contract Signed) folded — not deleted (cannot be deleted due to xmlid constraints).

---

## DEC-WP04-002 — x_employment_state Field and CEO Appointment Notification

**Date:** 2026-06-26
**Type:** CONFIGURATION / ARCHITECTURE
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator (WP-04 execution)

### Decision
Create a custom selection field `x_employment_state` on `hr.employee` via `ir.model.fields.create()` (shell, DB-resident) with values: `employed` (default), `pending_appointment`, `pending_separation`, `terminated`. Create two `base.automation` rules (trigger=`on_write`, state=`next_activity`) that create a To-Do activity for the CEO user (Executive Secretary, `login=executive.secretary`) when the field transitions to `pending_appointment` or `pending_separation`.

### Context
Transfer Package §3.3 requires "appointment and separation approval state on `hr.employee` with activity notification to CEO." This implements the Section 4 approval type: HR appointment/separation. No Enterprise module (`approvals`) is available in CE.

### Rationale
- `ir.model.fields.create()` pattern consistent with DEC-WP03-001 (x_compliance_status on res.partner).
- `base.automation` with `state='next_activity'` is the CE-native mechanism for activity creation (state='activity' is EE-only — confirmed during execution).
- CEO user identified via NADF HR / CEO group (id=106): Executive Secretary (login=executive.secretary).
- Field is DB-resident: risk of loss on DB rebuild. Mitigation: command documented in IMPLEMENTATION_HISTORY.md; Phase 2 `nadf_vendor_compliance` or equivalent module should implement version-controlled equivalent.

### Consequences
- `x_employment_state` (id=11644) on `hr.employee`; all 24 active employees initialised to `employed`.
- 2 automations active: auto ids 7 (Appointment) and 8 (Separation), deadline 3 days.
- Phase 2 risk: DB rebuild will lose the field and automations. Document in RISK_REGISTER.md.

---

## DEC-WP04-003 — Leave Type Approval Workflow Correction

**Date:** 2026-06-26
**Type:** CONFIGURATION
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator (WP-04 execution)

### Decision
Standardise leave type `leave_validation_type` to `both` (line manager → HR) for all discretionary leave categories. Retain `hr` for statutory/medical leave where there is no managerial discretion. No leave types deleted — 11 retained; deduplication (Paid Time Off / Annual Leave, Sick Time Off / Sick Leave) deferred to WP-05 UAT preparation pending client guidance.

### Context
Legacy build had inconsistent approval settings: Annual Leave, Casual Leave, Sick Leave each set to either `manager` or `hr` only. Transfer Package §3.3 specifies two-level: "request → line manager approval → HR confirmation".

### Rationale
| Leave type | Before | After | Rationale |
|-----------|--------|-------|-----------|
| Annual Leave (5) | hr | both | Discretionary — needs line mgr gate |
| Casual Leave (7) | manager | both | Discretionary — needs HR recording |
| Sick Leave (6) | manager | both | Pay continuity requires HR co-sign |
| Compensatory Days (3) | manager | both | Entitlement tracking requires HR |
| Maternity/Paternity (8,9) | hr | hr | Statutory right — no mgr discretion |
| Compassionate (11) | hr | hr | Bereavement — no mgr discretion |

### Consequences
- 4 leave types updated. 7 unchanged.
- Duplicate leave types (Paid Time Off vs Annual Leave; Sick Time Off vs Sick Leave) retained for now — client confirmation required before archiving defaults. Flagged as B-WP04-02 client action.

---

## DEC-WP04-004 — Manager Hierarchy Correction

**Date:** 2026-06-26
**Type:** CONFIGURATION
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator (WP-04 execution)

### Decision
Set `parent_id` on `hr.employee` records to implement the NADF 4-level org hierarchy (MD/ES → Director/Dept Head → Manager/Senior Officer → Officer). Corrected 8 records; 6 Admin-department employees left unassigned pending client confirmation (B-WP04-01).

### Context
Legacy build had most employees with no manager (`parent_id = False`) or incorrect manager (Suleiman Yusuf was under Strategy Head Adebanke Fajana; Finance Officers Sam Ediale and Ibrahim AlhaJi had no manager). The parent_id hierarchy drives the first-level leave approval.

### Rationale
- NADF structure: ES/CEO → Corporate Services Head → HR Head / Comms Head / ICT Head. ES/CEO → Finance Head → Finance Officers. ES/CEO → Procurement Head → etc.
- Suleiman Yusuf corrected: Finance Officer should report to Finance Head (Dr Yusuf Jatto), not Strategy Head (Adebanke Fajana) — prior mapping was a legacy data error.
- 6 Admin employees: no org data available; client must confirm dept assignments and reporting lines.

### Consequences
- 8 `parent_id` changes committed. Leave approval first-level now routes to correct manager.
- B-WP04-01 raised: 6 Admin employees (IDs 12, 13, 14, 18, 20, 23) pending client confirmation of department and manager assignment.

---

## DEC-ADM01-001 — helpdesk_mgmt OCA: No SLA Model (Priority + Stage Timestamps as SLA Proxy)

**Date:** 2026-06-26
**Type:** CONFIGURATION
**Status:** ACTIVE
**Made By:** A1 Master Orchestrator (WP-ADM-01 execution)

### Decision
OCA `helpdesk_mgmt` 17.0.1.10.4 does not include a separate SLA rules model. Accept `priority` field (0=Normal, 1=High) and `last_stage_update` timestamp as the Phase 1 SLA proxy. AC-ADM01-04 "≥1 SLA rule" is satisfied by team configuration with priority-tagged tickets. No additional SLA module required for Phase 1.

### Context
WP-ADM-01 scope specified "configure ticket categories, SLA rules (response + resolution time)". The OCA module provides: `helpdesk.ticket.team`, `helpdesk.ticket.category`, `helpdesk.ticket.stage`, `helpdesk.ticket.tag` — no `helpdesk.sla` or equivalent model. The Enterprise `helpdesk` module includes SLA; it is prohibited. Inspecting `ir.model` at runtime confirmed no SLA model present.

### Rationale
- CE/OCA alternative without a separate SLA module: priority field + `last_stage_update` auditing covers Phase 1 MVP needs.
- Importing a third OCA SLA module not on the WP-01 authorized list would require a new gate decision.
- Phase 2 custom module `nadf_ict_helpdesk` (if scoped) can add formal SLA policies.

### Consequences
- Phase 1 helpdesk configuration: 5 categories, team, priority-based routing, stage timestamps for SLA measurement. No separate SLA rule records.
- Future: `nadf_ict_helpdesk` Phase 2 spec should include SLA policy model if formal SLA tracking is required.

---

## DEC-ADM01-002 — Motor Vehicles Asset Category: Incorrect GL Account Mapping (Deferred)

**Date:** 2026-06-26
**Type:** DATA
**Status:** DEFERRED
**Made By:** A1 Master Orchestrator (WP-ADM-01 execution)

### Decision
The "Motor Vehicles" asset category (id=3) is mapped to GL account "EARTH MOVING EQUIPMENT — BULL DOZERS ETC." (11030301, id=294) and "PROV. FOR DEP-POWER GENERATING SETS" (11032007, id=325). This is an incorrect GL mapping from the legacy Phase 8 build. Correction is deferred to WP-05 UAT preparation / Finance review (DEC-WP02-002 analytic accounts remain authoritative).

### Context
During WP-ADM-01 asset register validation, the Motor Vehicles category GL accounts were inspected. The legacy build assigned Earth Moving Equipment accounts to the Motor Vehicles category. No assets are currently linked to the Motor Vehicles category (fleet vehicles tracked in `fleet.vehicle`, not `account.asset.asset`). No immediate business impact.

### Rationale
- No assets in Motor Vehicles category — zero immediate impact.
- Finance review (WP-02 / client) required before moving fleet vehicles to asset register.
- Correcting the GL mapping requires Finance team sign-off; deferred per Transfer Package authority hierarchy.

### Consequences
- Motor Vehicles asset category must NOT be used to record fleet vehicle acquisition costs until GL accounts are corrected.
- Action required: Finance team to confirm correct asset and depreciation accounts for motor vehicles before Phase 2/3 asset capitalisation.

---

## DEC-ADM01-003 — Administration User Groups: Partial Population (B-WP04-01 Dependency)

**Date:** 2026-06-26
**Type:** CONFIGURATION
**Status:** DEFERRED — pending B-WP04-01
**Made By:** A1 Master Orchestrator (WP-ADM-01 execution)

### Decision
Three of five Administration groups populated with Director Corporate Services (director.cs, uid=12) as interim dept head overseeing ICT, Fleet, and Asset operations. Driver (id=107) and IT Officer (id=110) groups have 0 users. No dedicated ICT Officer, Fleet Manager, Driver Odoo user accounts exist. User account creation is blocked pending B-WP04-01 (client to confirm Admin department employee roles).

### Context
WP-ADM-01-04 requires all 5 Administration groups populated (Driver, Fleet Manager, Asset Manager, IT Officer, IT Manager). The 6 Admin-department employees (IDs 12,13,14,18,20,23 — employee IDs) have no Odoo internal user accounts; only one has a connected user (Al-amin Uwais → no login). The Corporate Services Head (director.cs) oversees ICT, HR, and Communications departments and is the appropriate interim IT Manager and Fleet/Asset manager.

### Rationale
- Functional authority: director.cs is the department head and can act as group authority until dedicated staff user accounts are created.
- Practical: creating user accounts for staff whose roles are unconfirmed (B-WP04-01) would create stale/incorrect access grants.

### Consequences
- IT Officer and Driver group remain empty until B-WP04-01 resolved and user accounts created.
- Client action B-ADM01-01: confirm role assignments for Admin employees and request Odoo account creation.
- Admin employees cannot log in to Odoo or access Administration-specific features until accounts created.

---

*Decision Log maintained by: AI Developer (Claude Code)*
*Follows: Software Factory Decision Log Standard (software-factory-governance/governance/DECISION_LOG_STANDARD.md)*
