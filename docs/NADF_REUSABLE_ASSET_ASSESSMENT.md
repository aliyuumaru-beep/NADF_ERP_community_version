# NADF ERP MVP — Reusable Asset Assessment
**Document:** NADF_REUSABLE_ASSET_ASSESSMENT.md
**Version:** 1.0
**Date:** 2026-06-02
**Status:** DRAFT — Awaiting Operator Review
**Supersedes:** Section 7 of NADF_MVP_INSPECTION_REPORT.md (informal asset list)

---

## Purpose

This document formally classifies every governance, configuration, script, template, and module asset that may be inherited or adapted for the NADF ERP MVP. It is produced before any implementation begins, in compliance with the Software Factory reuse-before-build principle.

Assets are classified into three categories:

- **Category A — Direct Reuse:** Asset can be copied or referenced without modification. Use as-is.
- **Category B — Adapted Reuse:** Asset provides the pattern and structure; content must be adapted for NADF-specific context.
- **Category C — New Assets:** No suitable existing asset exists. Must be created for NADF and considered for promotion to Public Sector Template.

All Category C assets should be evaluated for promotion to the Public Sector ERP Template layer or the Software Factory governance layer as appropriate.

---

## 1. Software Factory Governance Layer Assets

Source: `/Users/mac/software-factory-governance/`

### 1.1 Governance Standards

| Asset | Path | Category | Rationale |
|-------|------|----------|-----------|
| Architectural Principles | `principles/ARCHITECTURAL_PRINCIPLES.md` | **A** | Binding across all projects — reference directly; do not copy |
| Governance Standard | `governance/GOVERNANCE_STANDARD.md` | **A** | Apply as inherited standard |
| Documentation Standard | `governance/DOCUMENTATION_STANDARD.md` | **A** | Apply as inherited standard |
| Decision Log Standard | `governance/DECISION_LOG_STANDARD.md` | **A** | Apply as inherited standard |
| Implementation History Standard | `governance/IMPLEMENTATION_HISTORY_STANDARD.md` | **A** | Apply as inherited standard |
| Backup Recovery Standard | `governance/BACKUP_RECOVERY_STANDARD.md` | **A** | Apply as inherited standard |
| Security Standard | `governance/SECURITY_STANDARD.md` | **A** | Apply as inherited standard |
| PR Governance Standard | `governance/PR_GOVERNANCE_STANDARD.md` | **A** | Apply as inherited standard |
| Registry Standard | `governance/REGISTRY_STANDARD.md` | **A** | Apply as inherited standard |
| Roadmap Standard | `governance/ROADMAP_STANDARD.md` | **A** | Apply as inherited standard |

**Action:** NADF `CLAUDE.md` and governance files must reference these standards by path, not duplicate them.

### 1.2 Governance Templates

| Asset | Path | Category | NADF Adaptation Required |
|-------|------|----------|--------------------------|
| Decision Log Template | `templates/decision_log_template.md` | **B** | Seed `docs/DECISION_LOG.md`; populate DEC-001 (fresh DB), DEC-002 (approvals workaround) |
| Implementation History Template | `templates/implementation_history_template.md` | **B** | Seed `docs/IMPLEMENTATION_HISTORY.md`; add IMP-001 (inspection phase) |
| Roadmap Template | `templates/roadmap_template.md` | **B** | Seed `docs/NADF_ROADMAP.md`; populate MVP phases |
| Onboarding Template | `templates/onboarding_template.md` | **B** | Seed NADF onboarding guide; change project identity, port, DB name |
| Project README Template | `templates/project_readme_template.md` | **B** | Seed `README.md`; NADF identity, scope, access instructions |
| Pull Request Template | `templates/pull_request_template.md` | **A** | Copy directly to `.github/pull_request_template.md` |
| Module Registry Template | `templates/module_registry_template.md` | **B** | Seed `docs/MODULE_REGISTRY.md`; populate with NADF MVP module list |

### 1.3 Onboarding Standards

| Asset | Path | Category | Adaptation |
|-------|------|----------|------------|
| AI Onboarding Standard | `onboarding/AI_ONBOARDING_STANDARD.md` | **A** | Reference from NADF CLAUDE.md — do not copy |
| Developer Onboarding Standard | `onboarding/DEVELOPER_ONBOARDING_STANDARD.md` | **A** | Reference — do not copy |
| Project Continuity Briefing Template | `onboarding/PROJECT_CONTINUITY_BRIEFING_TEMPLATE.md` | **B** | Adapt to create NADF-specific continuity briefing |

---

## 2. FamOil ERP Assets

Source: `/Users/mac/odoo17/`

### 2.1 Governance Documents

| Asset | Path | Category | NADF Adaptation |
|-------|------|----------|----------------|
| CLAUDE.md | `/Users/mac/odoo17/CLAUDE.md` | **B** | Use structure and sections; replace FamOil identity with NADF; update port, DB name, phase status |
| PROJECT_FACTORY_MANUAL.md | `/Users/mac/odoo17/PROJECT_FACTORY_MANUAL.md` | **B** | Use structure; adapt to NADF project boundaries and scope |
| IMPLEMENTATION_STANDARDS.md | `/Users/mac/odoo17/docs/IMPLEMENTATION_STANDARDS.md` | **B** | Inherit core rules; note NADF does not have manufacturing — remove manufacturing-specific sections |
| ARCHITECTURAL_PRINCIPLES.md | `/Users/mac/odoo17/docs/architecture/ARCHITECTURAL_PRINCIPLES.md` | **B** | Principles 1–7 apply directly; add public-sector-specific principle on approval transparency |
| NIGERIA_COMPLIANCE.md | `/Users/mac/odoo17/docs/famoil_erp_template/NIGERIA_COMPLIANCE.md` | **B** | VAT 7.5%, WHT, Pension sections directly applicable; remove agro-processing-specific notes |
| DECISION_LOG.md (DEC-001 Community vs Enterprise) | `/Users/mac/odoo17/docs/famoil_erp_template/DECISION_LOG.md` | **B** | DEC-001 reasoning applies verbatim; re-record as NADF DEC-001 with NADF-specific rationale |
| BACKUP_AND_RESTORE.md | `/Users/mac/odoo17/docs/famoil_erp_template/BACKUP_AND_RESTORE.md` | **B** | Structure reusable; adapt for NADF DB name, paths, port 8071 |
| KNOWN_ISSUES.md | `/Users/mac/odoo17/docs/famoil_erp_template/KNOWN_ISSUES.md` | **B** | Use as template; seed with NADF-specific known constraints (approval gap) |

### 2.2 CI/CD Workflows

| Asset | Path | Category | NADF Adaptation |
|-------|------|----------|----------------|
| `doc_lint.yml` | `/Users/mac/odoo17/.github/workflows/doc_lint.yml` | **B** | Copy; update mandatory docs list to NADF governance files; update job names |
| `security_scan.yml` | `/Users/mac/odoo17/.github/workflows/security_scan.yml` | **A** | Copy directly; patterns are project-agnostic |
| `ci_review.yml` | `/Users/mac/odoo17/.github/workflows/ci_review.yml` | **B** | Copy; update project references in messages |
| `backup_check.yml` | `/Users/mac/odoo17/.github/workflows/backup_check.yml` | **B** | Copy; update backup manifest path and project name |

### 2.3 Claude Governance Hooks

| Asset | Path | Category | NADF Adaptation |
|-------|------|----------|----------------|
| `pre_tool_guard.sh` | `/Users/mac/odoo17/.claude/hooks/pre_tool_guard.sh` | **B** | Copy; update project name in banner; patterns are project-agnostic |
| `post_tool_validator.sh` | `/Users/mac/odoo17/.claude/hooks/post_tool_validator.sh` | **B** | Copy; update project name |
| `audit_logger.sh` | `/Users/mac/odoo17/.claude/hooks/audit_logger.sh` | **B** | Copy; update log path and project name |
| `file_protection_guard.sh` | `/Users/mac/odoo17/.claude/hooks/file_protection_guard.sh` | **B** | Copy; update protected file list for NADF |
| `session_start_loader.sh` | `/Users/mac/odoo17/.claude/hooks/session_start_loader.sh` | **B** | Copy; update project name, port, DB name in banner |
| `session_end_reporter.sh` | `/Users/mac/odoo17/.claude/hooks/session_end_reporter.sh` | **B** | Copy; update project name |
| `.claude/settings.json` | `/Users/mac/odoo17/.claude/settings.json` | **B** | Copy; update tool permissions and project references |

### 2.4 Operational Scripts

| Asset | Path | Category | NADF Adaptation |
|-------|------|----------|----------------|
| `backup_famoil.sh` | `/Users/mac/odoo17/scripts/backup_famoil.sh` | **B** | Adapt → `backup_nadf.sh`; change DB_NAME=NADF, ODOO_ROOT, port, backup dir prefix |
| `restore_famoil.sh` | `/Users/mac/odoo17/scripts/restore_famoil.sh` | **B** | Adapt → `restore_nadf.sh`; same variable substitutions |
| `inspect_famoil_config.sh` | `/Users/mac/odoo17/scripts/inspect_famoil_config.sh` | **B** | Adapt → `inspect_nadf_config.sh`; update target DB and paths |
| `local_secret_scan.sh` | `/Users/mac/odoo17/scripts/local_secret_scan.sh` | **A** | Copy directly; project-agnostic |
| `com.famoil.backup.daily.plist` | `/Users/mac/odoo17/scripts/com.famoil.backup.daily.plist` | **B** | Adapt → `com.nadf.backup.daily.plist`; update label, script path |

### 2.5 Custom Odoo Addons

| Addon | Path | Category | NADF Use |
|-------|------|----------|----------|
| `om_account_accountant` | `/Users/mac/odoo17/custom_addons/` | **A** | Add to NADF addons path; no modification needed |
| `om_account_budget` | `/Users/mac/odoo17/custom_addons/` | **A** | Add to NADF addons path; budget management directly applicable |
| `om_account_daily_reports` | `/Users/mac/odoo17/custom_addons/` | **A** | Add to NADF addons path; daily reports applicable |
| `om_fiscal_year` | `/Users/mac/odoo17/custom_addons/` | **A** | Add to NADF addons path; fiscal year management |
| `om_recurring_payments` | `/Users/mac/odoo17/custom_addons/` | **A** | Add to NADF addons path; recurring payments applicable |
| `accounting_pdf_reports` | `/Users/mac/odoo17/custom_addons/` | **A** | Add to NADF addons path; PDF reports applicable |
| `maintenance_spareparts_v6` | `/Users/mac/odoo17/custom_addons/` | **EXCLUDE** | Manufacturing/maintenance-specific; not needed for NADF MVP |
| `mrp_component_availability_check` | `/Users/mac/odoo17/custom_addons/` | **EXCLUDE** | Manufacturing-specific |
| `stock_crude_oil_tank_restriction` | `/Users/mac/odoo17/custom_addons/` | **EXCLUDE** | Agro-processing-specific |
| `stock_landed_cost_po_check` | `/Users/mac/odoo17/custom_addons/` | **EXCLUDE** | Agro-processing-specific |

**Addons strategy:** NADF will reference FamOil's `custom_addons` directory in its addons path rather than copying modules. This avoids duplication and ensures NADF benefits from any upstream fixes.

`nadf.conf` addons path will include:
```
/Users/mac/odoo17/odoo/odoo/addons,/Users/mac/odoo17/custom_addons,/Users/mac/nadf_erp/custom_addons
```

### 2.6 CSV Templates

| Asset | Path | Category | NADF Adaptation |
|-------|------|----------|----------------|
| `product_categories.csv` | `/Users/mac/odoo17/csv_templates/` | **B** | Adapt for NADF categories (Office Supplies, ICT, Operations) — remove oil/agro categories |
| `locations.csv` | `/Users/mac/odoo17/csv_templates/` | **B** | Adapt for NADF stores (Main Store, ICT Store, Consumables Store) |
| `warehouses.csv` | `/Users/mac/odoo17/csv_templates/` | **B** | Adapt for NADF single warehouse |
| `products.csv` | `/Users/mac/odoo17/csv_templates/` | **B** | Adapt for NADF products (Laptop, Printer, Toner, Chair, Internet Sub) |

---

## 3. WamaCare NGO/CBO Assets

Source: `/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/`

### 3.1 Governance Documents

| Asset | Category | NADF Adaptation |
|-------|----------|----------------|
| `CLAUDE.md` (WamaCare) | **B** | Use section structure; NADF identity is government/public-sector, not NGO |
| `wamacare.conf` | **B** | Adapt → `nadf.conf`; change port 8070→8071, db_name→NADF, addons path |

### 3.2 CSV Templates

| Asset | Category | NADF Adaptation |
|-------|----------|----------------|
| `hr_department.csv` | **B** | Adapt: Finance, Procurement, HR, Executive Office (instead of WamaCare departments) |
| `hr_employees.csv` | **B** | Adapt: use real NADF staff names from local NADF data; add Employee ID column |
| `wamacare_vendors.csv` | **B** | Adapt: Office Supplies Vendor, ICT Vendor, Training Vendor, Logistics Vendor |
| `wamacare_products.csv` | **B** | Adapt: map to NADF product list |
| `vendor.csv` | **B** | Structural template — populate with NADF vendor data |

### 3.3 Module Configuration Patterns

| Pattern | Category | Adaptation |
|---------|----------|------------|
| `hr_holidays` leave type configuration (Annual, Sick, Casual) | **B** | Add Maternity Leave, Study Leave per NADF MVP spec |
| Leave approval chain config (2-level: Manager → HR Manager) | **B** | Adapt: Casual→Supervisor; Annual→Head HR; Study→Executive Secretary |
| Purchase approval threshold (₦200,000) | **B** | Adapt: NADF threshold is ₦500,000 for first level |
| 5-user role setup (admin, finance, HR, officer) | **B** | Adapt to 8 NADF demo users per MVP spec |
| l10n_ng + Nigerian chart of accounts (68 accounts) | **B** | Use as base; add NADF-specific accounts (Grants, Pension Payables, Accumulated Funds) |
| Nigerian VAT 7.5% and WHT configuration | **A** | Apply directly; same regulatory environment |

---

## 4. NADF Local Source Data

Source: `/Users/mac/Documents/Aliyu/NADF/`

| Asset | File | Category | Use |
|-------|------|----------|-----|
| Real NADF staff names + emails | `nadf_Import_User_Sample#1.csv` | **B** | Adapt → Odoo employee import format (add Employee ID, Department, Job Position, Supervisor) |
| MS365 user export with full names | `users_credentials.csv` | **B** | Cross-reference for full names; use emails as Odoo login names |

**Privacy note:** Odoo user passwords must be demo-safe values (not real passwords). Never commit credentials to Git.

---

## 5. Category C — New Assets (No Existing Source)

These assets must be created for NADF. All are candidates for promotion to the Public Sector ERP Template layer.

| Asset | File | Purpose | Template Promotion Candidate |
|-------|------|---------|------------------------------|
| NADF company configuration | (Odoo UI config) | NADF company identity, Abuja, NGN, logo | YES — public sector company setup pattern |
| Nigerian government CoA additions | CSV / Odoo config | Grants income, Pension payables, Accumulated Funds, Gov-specific accounts | YES — public sector chart of accounts template |
| Public sector procurement approval workaround | `docs/NADF_MVP_APPROVAL_WORKFLOWS.md` | 3-tier approval with Community Edition | YES — Public Sector ERP Template standard pattern |
| NADF-specific leave types | Odoo config | Maternity, Study Leave config | YES — general HR template |
| Public sector vendor classification | Odoo config | Government supplier categories | YES |
| Procurement threshold documentation | `docs/NADF_MVP_APPROVAL_WORKFLOWS.md` | ₦500K / ₦5M / unlimited tiers | YES — template for any Nigerian public sector org |
| NADF demo scenarios | `docs/NADF_MVP_DEMO_SCENARIOS.md` | Walkthrough scripts for 4 demo scenarios | YES — reusable public sector demo template |
| NADF test report | `docs/NADF_MVP_TEST_REPORT.md` | Validation evidence | YES — template for public sector MVP acceptance |
| `backup_nadf.sh` | `scripts/backup_nadf.sh` | NADF backup script | YES — parametrised backup pattern for public sector |
| `nadf.conf` | `nadf.conf` | NADF server configuration | YES — public sector server config template |
| `NADF_TEMPLATE_STRATEGY.md` | `docs/NADF_TEMPLATE_STRATEGY.md` | Captures public sector template strategy | YES — Software Factory layer asset |

---

## 6. Assets Explicitly Excluded

The following assets from existing projects are NOT suitable for NADF and must not be copied:

| Asset | Source | Reason |
|-------|--------|--------|
| `mrp`, `mrp_account`, manufacturing BOM/routing CSVs | FamOil | Manufacturing — not in NADF scope |
| `stock_crude_oil_tank_restriction` | FamOil | Agro-processing logic |
| `stock_landed_cost_po_check` | FamOil | Agro-processing validation |
| `custom_addons_farm/farm_layers` | FamOil | Agricultural vertical |
| FamOil costing model (FIFO/Average, work centre rates) | FamOil | Industrial costing — NADF uses simple expense accounting |
| FamOil sales modules (sale, sale_mrp, etc.) | FamOil | Sales workflow — excluded from NADF MVP |
| `wamacare_safeguarding` custom module | WamaCare | NGO safeguarding — not applicable |
| WamaCare beneficiary / programme / M&E data | WamaCare | NGO programme management — not in NADF scope |
| WamaCare project management modules | WamaCare | Project M&E — excluded from NADF MVP |

---

## 7. Asset Classification Summary

| Category | Count | Action |
|----------|-------|--------|
| A — Direct Reuse | 18 | Copy or reference without modification |
| B — Adapted Reuse | 38 | Use structure; adapt content for NADF |
| C — New Assets | 11 | Create; evaluate each for template promotion |
| Excluded | 9 | Do not use |

---

## 8. Governance Inheritance Principle

NADF **inherits** from the Software Factory governance layer. It does **not** recreate governance.

The following files in the NADF repo will **reference** rather than duplicate Software Factory standards:

```
NADF CLAUDE.md
  └── References: software-factory-governance principles (by path in briefing)
  └── References: AI_ONBOARDING_V2.txt (pasted by operator at session start)

NADF DECISION_LOG.md
  └── Follows: Decision Log Standard (governance/DECISION_LOG_STANDARD.md)
  └── Format from: software-factory-governance templates/decision_log_template.md

NADF .github/workflows/
  └── Adapted from: FamOil .github/workflows/ (B-level adaptation)
  └── Principle source: governance/GITHUB_RULESET_BASELINE.md

NADF .claude/hooks/
  └── Adapted from: FamOil .claude/hooks/ (B-level adaptation)
  └── Logic is project-agnostic; only project name and paths differ
```

No new governance philosophy is invented for NADF. All deviations from inherited governance must be logged in the NADF DECISION_LOG.

---

*Document produced by: AI Developer (Claude Code) | Date: 2026-06-02*
*Sources inspected: software-factory-governance, FamOil (/Users/mac/odoo17), WamaCare, NADF local data*
