# NADF ERP MVP — Phase 0 Foundation Plan
**Document:** NADF_PHASE0_FOUNDATION_PLAN.md
**Version:** 1.0
**Date:** 2026-06-02
**Status:** DRAFT — Awaiting Operator Review

---

## Purpose

This document defines all work that must be completed before the NADF Odoo database is created and any modules are installed. Phase 0 is the foundation layer. Nothing is built on an unstable foundation.

Phase 0 is complete only when all implementation gates in Section 9 are satisfied.

---

## 1. Governance Import Plan

NADF inherits governance from the Software Factory. It does not create new governance philosophy.

The following governance assets must be put in place before any configuration work. Each entry identifies the source, the adaptation required, and the target location in the NADF repo.

### 1.1 Core Governance Documents

| Document | Source | Adaptation Level | Target Path |
|----------|--------|-----------------|-------------|
| `CLAUDE.md` | FamOil pattern (B-level) | Update project identity, port=8071, DB=NADF, phase status, start command | `/Users/mac/nadf_erp/CLAUDE.md` |
| `README.md` | Software Factory template (B-level) | NADF project identity, MVP scope, access instructions, port | `/Users/mac/nadf_erp/README.md` |
| `CHANGELOG.md` | FamOil pattern (B-level) | Initialise with v0.1.0-foundation entry | `/Users/mac/nadf_erp/CHANGELOG.md` |
| `PROJECT_FACTORY_MANUAL.md` | FamOil pattern (B-level) | Update repo structure, layer position, project scope | `/Users/mac/nadf_erp/PROJECT_FACTORY_MANUAL.md` |
| `docs/DECISION_LOG.md` | Software Factory template (B-level) | Seed with DEC-001, DEC-002 (see Section 1.2) | `/Users/mac/nadf_erp/docs/DECISION_LOG.md` |
| `docs/IMPLEMENTATION_HISTORY.md` | Software Factory template (B-level) | Seed with IMP-001 (inspection phase) | `/Users/mac/nadf_erp/docs/IMPLEMENTATION_HISTORY.md` |
| `docs/IMPLEMENTATION_STANDARDS.md` | FamOil (B-level) | Inherit core rules; note no manufacturing; add public sector context | `/Users/mac/nadf_erp/docs/IMPLEMENTATION_STANDARDS.md` |
| `docs/NADF_ROADMAP.md` | Software Factory template (B-level) | MVP phases, timeline, deliverables | `/Users/mac/nadf_erp/docs/NADF_ROADMAP.md` |
| `docs/MODULE_REGISTRY.md` | Software Factory template (B-level) | Populate with NADF MVP module list and status | `/Users/mac/nadf_erp/docs/MODULE_REGISTRY.md` |
| `docs/BACKUP_AND_RECOVERY.md` | FamOil (B-level) | Update for NADF DB, paths, port 8071 | `/Users/mac/nadf_erp/docs/BACKUP_AND_RECOVERY.md` |
| `docs/ONBOARDING_GUIDE.md` | Software Factory template (B-level) | NADF project identity; how to start the instance | `/Users/mac/nadf_erp/docs/ONBOARDING_GUIDE.md` |

### 1.2 Pre-Seeded Decision Log Entries

The following decisions are known before implementation begins and must be recorded in `docs/DECISION_LOG.md` during Phase 0:

**DEC-001 — Fresh Database Strategy**
- Decision: Create a fresh `NADF` PostgreSQL database rather than cloning from FamOil, WamaCare, or OdooClean.
- Rationale: Clean lineage, predictable configuration, no inherited module state or demo data, better template repeatability.
- Alternatives rejected: Clone FamOil (carries manufacturing modules); clone OdooClean (carries irrelevant modules); restore from dump (unknown state).

**DEC-002 — Odoo Community Edition Approval Workaround**
- Decision: Use `purchase` module approval settings + `base_automation` rules + documented manual procedure as the Community Edition alternative to the Enterprise `approvals` app.
- Rationale: `approvals` module is Enterprise-only; not installable on Community. The workaround satisfies the MVP's demonstration objective.
- Limitation: Three-tier procurement approval ladder cannot be configured natively; tier-2 and tier-3 escalation is semi-manual with email notifications.

**DEC-003 — Shared Addons Path Strategy**
- Decision: NADF `nadf.conf` will reference `/Users/mac/odoo17/custom_addons/` directly rather than copying addons to `/Users/mac/nadf_erp/custom_addons/`.
- Rationale: Avoids duplication of `om_account_*` modules; ensures NADF benefits from any upstream fixes applied to FamOil's addons.
- Risk: If FamOil addons are modified incompatibly, NADF may be affected. Mitigated by: (a) NADF is MVP/demo not production; (b) changes to shared addons require documentation and testing.

### 1.3 Pre-Seeded Implementation History Entry

**IMP-001 — Inspection and Foundation Phase**
- Phase: Phase 0 — Foundation
- Status: IN PROGRESS
- Covers: Repository inspection, reusable asset assessment, template strategy, phase 0 planning.
- Deliverables: NADF_MVP_INSPECTION_REPORT.md, NADF_REUSABLE_ASSET_ASSESSMENT.md, NADF_TEMPLATE_STRATEGY.md, NADF_PHASE0_FOUNDATION_PLAN.md.

---

## 2. CI/CD Workflows

All workflows are adapted from FamOil (B-level adaptation). Only project names, file paths, and mandatory doc lists are changed.

### 2.1 Workflows to Create

| Workflow | Source | Target Path | Key Adaptations |
|----------|--------|-------------|----------------|
| `doc_lint.yml` | FamOil | `.github/workflows/doc_lint.yml` | Update MANDATORY_DOCS list to NADF files; update job name and project references |
| `security_scan.yml` | FamOil | `.github/workflows/security_scan.yml` | Copy directly (A-level) |
| `ci_review.yml` | FamOil | `.github/workflows/ci_review.yml` | Update project name in output messages |
| `backup_check.yml` | FamOil | `.github/workflows/backup_check.yml` | Update backup manifest path to NADF |

### 2.2 NADF Mandatory Documents for `doc_lint.yml`

The doc_lint workflow will enforce the existence of:
```
CLAUDE.md
CHANGELOG.md
docs/IMPLEMENTATION_STANDARDS.md
docs/BACKUP_AND_RECOVERY.md
docs/ONBOARDING_GUIDE.md
docs/MODULE_REGISTRY.md
docs/DECISION_LOG.md
docs/IMPLEMENTATION_HISTORY.md
.claude/settings.json
```

### 2.3 Branch Protection

After first push to GitHub, configure:
- `main` branch protection: require PR, no direct push
- Required status checks: `doc-lint`, `secret-scan`
- Human review count: 0 (solo-governed — consistent with Software Factory standard)

---

## 3. Claude Governance Hooks

All hooks are adapted from FamOil (B-level). Only project name, port, and DB name differ.

### 3.1 Hooks to Create

| Hook | Source | Target Path | Adaptation |
|------|--------|-------------|------------|
| `pre_tool_guard.sh` | FamOil | `.claude/hooks/pre_tool_guard.sh` | Update project name in banner |
| `post_tool_validator.sh` | FamOil | `.claude/hooks/post_tool_validator.sh` | Update project name |
| `audit_logger.sh` | FamOil | `.claude/hooks/audit_logger.sh` | Update log path prefix |
| `file_protection_guard.sh` | FamOil | `.claude/hooks/file_protection_guard.sh` | Update protected file list for NADF |
| `session_start_loader.sh` | FamOil | `.claude/hooks/session_start_loader.sh` | Update project name=NADF, port=8071, DB=NADF |
| `session_end_reporter.sh` | FamOil | `.claude/hooks/session_end_reporter.sh` | Update project name |

### 3.2 `.claude/settings.json`

Adapted from FamOil. Must include:
- Hook file references
- Tool permission allowlist appropriate for NADF (read, edit, write; bash with restrictions)
- No push-to-remote permissions without operator confirmation

---

## 4. Environment Setup

### 4.1 Server Configuration (`nadf.conf`)

Adapted from WamaCare `wamacare.conf`.

```ini
[options]
admin_passwd = admin

db_host = False
db_port = False
db_user = odoo
db_password = odoo

db_name = NADF
dbfilter = ^NADF$

addons_path = /Users/mac/odoo17/odoo/odoo/addons,/Users/mac/odoo17/custom_addons,/Users/mac/nadf_erp/custom_addons

server_wide_modules = base,web,http_routing

log_level = info
http_port = 8071

logfile = /Users/mac/odoo_logs/nadf.log
```

**Target path:** `/Users/mac/nadf_erp/nadf.conf`
**Note:** `nadf.conf` must be added to `.gitignore` only if it contains credentials. In this configuration (local trust auth, demo passwords), it may be committed. Never commit real passwords.

### 4.2 Start Command

```bash
source /Users/mac/odoo17/odoo/venv/bin/activate
python /Users/mac/odoo17/odoo/odoo-bin \
  -d NADF \
  -r odoo \
  --addons-path=/Users/mac/odoo17/odoo/odoo/addons,/Users/mac/odoo17/custom_addons,/Users/mac/nadf_erp/custom_addons \
  --http-port=8071 \
  --config=/Users/mac/nadf_erp/nadf.conf
```

This command is recorded in `CLAUDE.md` as the canonical NADF start command.

### 4.3 Port Allocation Summary

| Port | Instance | Database |
|------|----------|----------|
| 8069 | FamOil | Famoil |
| 8070 | WamaCare | wamacare_local |
| **8071** | **NADF** | **NADF** |

### 4.4 Database Naming

- Database name: `NADF` (capitalised, consistent with `Famoil` convention)
- Created by: `createdb -O odoo NADF` or via Odoo database manager
- Odoo user: `odoo` (existing PostgreSQL role)
- Locale: `C` (consistent with other databases)

---

## 5. Documentation Structure

The following directory and file structure must exist before Phase 1 begins.

```
/Users/mac/nadf_erp/
├── .claude/
│   ├── hooks/
│   │   ├── audit_logger.sh
│   │   ├── file_protection_guard.sh
│   │   ├── post_tool_validator.sh
│   │   ├── pre_tool_guard.sh
│   │   ├── session_end_reporter.sh
│   │   └── session_start_loader.sh
│   └── settings.json
├── .github/
│   ├── pull_request_template.md
│   └── workflows/
│       ├── backup_check.yml
│       ├── ci_review.yml
│       ├── doc_lint.yml
│       └── security_scan.yml
├── .gitignore
├── CHANGELOG.md
├── CLAUDE.md
├── PROJECT_FACTORY_MANUAL.md
├── README.md
├── csv_templates/
│   └── nadf/               ← NADF-specific templates added in Phase 2+
├── custom_addons/          ← empty at Phase 0; NADF custom modules go here if needed
├── docs/
│   ├── BACKUP_AND_RECOVERY.md
│   ├── DECISION_LOG.md
│   ├── IMPLEMENTATION_HISTORY.md
│   ├── IMPLEMENTATION_STANDARDS.md
│   ├── MODULE_REGISTRY.md
│   ├── NADF_MVP_INSPECTION_REPORT.md         ← DONE
│   ├── NADF_PHASE0_FOUNDATION_PLAN.md        ← THIS DOCUMENT
│   ├── NADF_REUSABLE_ASSET_ASSESSMENT.md     ← DONE
│   ├── NADF_ROADMAP.md
│   ├── NADF_TEMPLATE_STRATEGY.md             ← DONE
│   └── ONBOARDING_GUIDE.md
├── logs/                   ← gitignored
├── nadf.conf
└── scripts/
    ├── backup_nadf.sh
    └── restore_nadf.sh
```

---

## 6. Backup Strategy

### 6.1 Backup Script (`backup_nadf.sh`)

Adapted from `backup_famoil.sh`. Key differences:

| Variable | FamOil Value | NADF Value |
|----------|-------------|------------|
| `DB_NAME` | `Famoil` | `NADF` |
| `ODOO_ROOT` | `/Users/mac/odoo17` | `/Users/mac/odoo17` (shared) |
| `CUSTOM_ADDONS` | `/Users/mac/odoo17/custom_addons` | `/Users/mac/nadf_erp/custom_addons` |
| `BACKUP_BASE` | `/Users/mac/odoo_backups` | `/Users/mac/odoo_backups` |
| `REPO_ROOT` | `/Users/mac/odoo17` | `/Users/mac/nadf_erp` |
| Backup prefix | `famoil_` | `nadf_` |
| Filestore path | `.../Famoil` | `.../NADF` |

### 6.2 Backup Schedule

- **Frequency:** Daily, triggered by launchd plist (`com.nadf.backup.daily.plist`)
- **Retention:** 7-day local retention (same as FamOil)
- **Target:** `/Users/mac/odoo_backups/nadf_YYYYMMDD_HHMM/`
- **Offsite:** Google Drive sync via rclone (same mechanism as FamOil) — activate after first stable configuration

### 6.3 Restore Validation

A restore drill must be performed before the MVP is presented to any NADF users. This is a non-negotiable gate inherited from the Software Factory restore-validation principle.

The restore drill procedure will be documented in `docs/BACKUP_AND_RECOVERY.md`.

Steps:
1. Run `backup_nadf.sh` to create a known-good backup
2. Create a test database `NADF_restore_test`
3. Run `restore_nadf.sh` against `NADF_restore_test`
4. Validate all configured data is present
5. Drop `NADF_restore_test`
6. Log the result in `IMPLEMENTATION_HISTORY.md`

### 6.4 Backup Before Each Phase

A backup must be run and confirmed before:
- Module installation
- Finance configuration
- Procurement configuration
- HR configuration
- Approval workflow configuration
- Any destructive data operation

---

## 7. Git Strategy

### 7.1 Branch Model

| Branch | Purpose |
|--------|---------|
| `main` | Stable, reviewed state only |
| `phase/0-foundation` | Phase 0 foundation work (current) |
| `phase/1-database` | Database creation and module installation |
| `phase/2-finance` | Finance configuration |
| `phase/3-procurement` | Procurement configuration |
| `phase/4-hr` | HR configuration |
| `phase/5-approvals` | Approval workflow configuration |
| `phase/6-demo` | Demo scenarios and validation |

### 7.2 Commit Conventions

Follow FamOil conventions (consistent with Software Factory standard):

```
<type>(<scope>): <short description>

Types: feat, fix, docs, config, chore, governance
Scope: foundation, finance, procurement, hr, approvals, demo
```

Examples:
```
governance(foundation): add CLAUDE.md and project governance structure
config(env): add nadf.conf for port 8071 configuration
docs(foundation): add DECISION_LOG with DEC-001 fresh database decision
feat(hr): configure NADF departments and job positions
```

### 7.3 PR Conventions

- All merges to `main` via PR only (no direct push after branch protection is active)
- PR must reference the phase document
- PR description from `.github/pull_request_template.md`

### 7.4 What Is Never Committed

- Database dumps (PostgreSQL `.dump` files)
- Filestore archives
- Real credentials or passwords
- `odoo_backups/` directory contents
- `logs/` directory
- `*.pyc` and Python cache files

These are enforced by `.gitignore` and `security_scan.yml`.

---

## 8. Module Installation Plan (Post-Phase-0)

This plan is prepared in Phase 0 but executed in Phase 1.

### Installation Order

Install modules in this sequence to avoid dependency failures:

**Batch 1 — Platform Base**
```
base, mail, bus, web, portal, auth_signup
contacts, discuss, analytic
```

**Batch 2 — Localization**
```
l10n_ng, base_vat
```

**Batch 3 — Finance**
```
account, account_payment, account_payment_term
om_fiscal_year, om_account_accountant, om_account_budget
om_account_daily_reports, om_recurring_payments
accounting_pdf_reports
```

**Batch 4 — Procurement**
```
purchase, purchase_stock, purchase_requisition
stock, stock_account
```

**Batch 5 — Human Resources**
```
hr, hr_org_chart, hr_contract
hr_holidays
```

**Batch 6 — Automation**
```
base_automation
```

### Modules NOT to Install

| Module | Reason |
|--------|--------|
| `approvals` | Enterprise-only — not available |
| `sign` | Enterprise-only |
| `documents` | Enterprise-only |
| `mrp`, `sale`, `fleet` | Out of MVP scope |
| `hr_payroll` | Excluded from MVP |
| Any third-party paid module | Not approved |

---

## 9. Implementation Gates

### Gate 0A — Documentation Complete

All the following files must exist and be non-empty before any Odoo work begins:

- [ ] `CLAUDE.md`
- [ ] `README.md`
- [ ] `CHANGELOG.md`
- [ ] `PROJECT_FACTORY_MANUAL.md`
- [ ] `docs/DECISION_LOG.md` (DEC-001, DEC-002, DEC-003 recorded)
- [ ] `docs/IMPLEMENTATION_HISTORY.md` (IMP-001 recorded)
- [ ] `docs/IMPLEMENTATION_STANDARDS.md`
- [ ] `docs/BACKUP_AND_RECOVERY.md`
- [ ] `docs/ONBOARDING_GUIDE.md`
- [ ] `docs/MODULE_REGISTRY.md`
- [ ] `docs/NADF_ROADMAP.md`
- [ ] `nadf.conf`

### Gate 0B — Governance Enforcement Active

All the following must be in place:

- [ ] `.claude/hooks/` — all 6 hooks present and executable
- [ ] `.claude/settings.json` — configured
- [ ] `.github/workflows/` — all 4 workflows present
- [ ] `.gitignore` — configured to exclude dumps, credentials, logs
- [ ] `scripts/backup_nadf.sh` — present and tested (dry run)
- [ ] `scripts/restore_nadf.sh` — present

### Gate 0C — Git State Clean

- [ ] All Phase 0 documents committed to `phase/0-foundation` branch
- [ ] `git status` is clean (no uncommitted changes)
- [ ] Commit messages follow convention
- [ ] Ready for operator to approve push to GitHub

### Gate 0D — Operator Approval

- [ ] Operator has reviewed and approved this Phase 0 Foundation Plan
- [ ] Operator has answered: fiscal year (Jan–Dec or Oct–Sep)?
- [ ] Operator has confirmed: proceed to Phase 1 (database creation)

**Only after all Gate 0 checks are satisfied may Phase 1 begin.**

---

## 10. Phase 1 Entry Criteria (For Reference)

Phase 1 begins with database creation. Its entry criteria are:

- All Gate 0 checks passed
- `backup_nadf.sh` tested (even though no DB exists yet — test script syntax and path validity)
- `nadf.conf` in place and validated
- Operator approval received

Phase 1 first action: `createdb -O odoo -E UTF8 -l C NADF`

---

## 11. Estimated Phase 0 Effort

| Activity | Effort |
|----------|--------|
| Adapt governance docs (CLAUDE.md, README, CHANGELOG, etc.) | 1–2 hours |
| Adapt and create CI/CD workflows (4 files) | 30 minutes |
| Adapt Claude hooks (6 files) | 45 minutes |
| Create nadf.conf | 10 minutes |
| Create backup_nadf.sh and restore_nadf.sh | 30 minutes |
| Seed DECISION_LOG, IMPLEMENTATION_HISTORY | 20 minutes |
| Create MODULE_REGISTRY, ONBOARDING_GUIDE, ROADMAP | 45 minutes |
| Initial git commit | 15 minutes |
| **Total estimated** | **~4 hours** |

---

*Document produced by: AI Developer (Claude Code) | Date: 2026-06-02*
*Governance source: software-factory-governance, FamOil implementation patterns*
*Awaiting operator review before Phase 0 execution begins*
