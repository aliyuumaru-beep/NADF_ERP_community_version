# NADF ERP MVP — Inspection Report
**Document:** NADF_MVP_INSPECTION_REPORT.md
**Version:** 1.0
**Date:** 2026-06-02
**Author:** AI Developer (Claude Code)
**Status:** COMPLETE — Awaiting Operator Review

---

## Purpose

This report records the findings of the pre-implementation inspection conducted before any Odoo configuration or database changes. It covers the GitHub repository state, local Odoo environment, existing database inventory, available modules, reusable assets from the Software Factory, and the proposed implementation plan.

No Odoo configuration has been made. No database has been created. This report is the sole deliverable of the inspection phase.

---

## 1. GitHub Repository Status

| Field              | Finding                                                        |
|--------------------|----------------------------------------------------------------|
| Repo URL           | https://github.com/aliyuumaru-beep/NADF_ERP_community_version |
| Repo Created       | 2026-06-02                                                     |
| Default Branch     | None (empty repo)                                              |
| Commits            | 0                                                              |
| Files              | 0                                                              |
| Governance Files   | None present                                                   |
| CI/CD Workflows    | None present                                                   |
| Branch Protection  | Not configured                                                 |

**Conclusion:** The GitHub repository exists but is completely empty. All governance structure, documentation, and configuration files must be created from scratch in this session. The Software Factory templates and FamOil patterns will be the primary source for governance scaffolding.

**Local project root created:** `/Users/mac/nadf_erp/`
**Remote linked:** `origin → https://github.com/aliyuumaru-beep/NADF_ERP_community_version.git`
**Branch:** `main`

---

## 2. Odoo Version and Edition

| Field            | Finding                                            |
|------------------|----------------------------------------------------|
| Version          | Odoo 17.0 (Community Edition)                     |
| Edition          | Community — confirmed                              |
| Binary Location  | `/Users/mac/odoo17/odoo/odoo-bin`                 |
| Venv             | `/Users/mac/odoo17/odoo/venv/`                    |
| Platform         | macOS (MacBook Air)                               |
| Database Server  | PostgreSQL 16.11                                  |
| Currently Running | Odoo 17.0 — FamOil on port 8069, WamaCare on port 8070 |

**NADF Assigned Port:** `8071` (8069 and 8070 are occupied by active instances)

---

## 3. Database Status

### Existing Databases (PostgreSQL)

| Database         | Owner | Purpose                              | Relevance to NADF        |
|------------------|-------|--------------------------------------|--------------------------|
| `Famoil`         | odoo  | FamOil ERP — active production       | Reference only           |
| `wamacare_local` | odoo  | WamaCare NGO — active                | HR/accounting reference  |
| `OdooClean`      | odoo  | Clean Odoo base (67 modules)         | Possible restore reference |
| `OdooTest`       | odoo  | Test environment                     | Not applicable           |
| `Odootest`       | mac   | Test environment                     | Not applicable           |
| `aedc_demo`      | odoo  | AEDC demo (power sector)             | Reference only           |
| `odoo`           | odoo  | Generic                              | Not applicable           |
| `odoo_farm`      | odoo  | Farm project                         | Not applicable           |
| `your_db_name`   | mac   | Unused                               | Not applicable           |
| `postgres`       | mac   | PostgreSQL system                    | Not applicable           |

### NADF Database

**No NADF database exists.** A fresh database named `NADF` must be created.

**Recommended database name:** `NADF`

**Rationale:** Consistent with `Famoil` naming convention (project name, not snake_case). Clean start avoids inheriting unintended module configurations from existing databases.

---

## 4. Available Odoo Addons

The following MVP-required modules are confirmed present in the local Odoo 17 installation at `/Users/mac/odoo17/odoo/odoo/addons/`:

### Finance

| Module                   | Status         | Notes                                     |
|--------------------------|----------------|-------------------------------------------|
| `account`                | Available      | Core accounting                           |
| `account_payment`        | Available      | Payment processing                        |
| `account_payment_term`   | Available      | Payment terms                             |
| `analytic`               | Available      | Analytic accounts / cost centres          |
| `l10n_ng`                | Installed (FamOil/WamaCare) | Nigeria chart of accounts, WHT, VAT |
| `om_account_accountant`  | Custom addon   | In `/Users/mac/odoo17/custom_addons/`     |
| `om_account_budget`      | Custom addon   | Budget management                         |
| `om_account_daily_reports` | Custom addon | Daily accounting reports                  |
| `om_fiscal_year`         | Custom addon   | Custom fiscal year management             |
| `om_recurring_payments`  | Custom addon   | Recurring payment schedules               |
| `accounting_pdf_reports` | Custom addon   | PDF accounting reports                    |

### Procurement

| Module                   | Status    | Notes                                          |
|--------------------------|-----------|------------------------------------------------|
| `purchase`               | Available | Core purchase management                       |
| `purchase_stock`         | Available | Links purchase orders to inventory             |
| `purchase_requisition`   | Available | **Purchase Agreements** — Community equivalent for purchase approval workflows |
| `stock`                  | Available | Inventory management                           |
| `stock_account`          | Available | Inventory valuation                            |
| `stock_landed_costs`     | Available | Landed cost allocation (optional)              |

### Human Resources

| Module          | Status    | Notes                                          |
|-----------------|-----------|------------------------------------------------|
| `hr`            | Available | Employee master data                           |
| `hr_holidays`   | Available | Time Off / Leave management                   |
| `hr_org_chart`  | Available | Organisational chart                           |
| `hr_contract`   | Available | Employment contracts (optional)                |
| `hr_skills`     | Available | Skills registry (optional)                    |
| `hr_expense`    | Available | Expense claims (optional for MVP)             |

### Platform / Core

| Module              | Status    | Notes                                          |
|---------------------|-----------|------------------------------------------------|
| `contacts`          | Available | Partner / contact management                  |
| `discuss`           | Available | Internal messaging (Discuss app)              |
| `base_automation`   | Available | Automated actions — critical for approval workarounds |
| `mail`              | Available | Email and chatter                              |
| `portal`            | Available | User portal access                             |
| `auth_signup`       | Available | User self-registration                         |

---

## 5. Missing Required Modules (Enterprise-Only — NOT Available)

The MVP product document references several features that are **Enterprise-only** and are **not available** in Odoo 17 Community Edition.

| Feature / Module       | Document Reference              | Enterprise? | Community Alternative                |
|------------------------|---------------------------------|-------------|--------------------------------------|
| `approvals`            | Phase 1 — Applications to Install | YES — Enterprise | See Section 6 below                |
| `sign`                 | Phase 3 — Optional demo         | YES — Enterprise | PDF attachments; external e-sign tool |
| `documents`            | Phase 3 — Optional demo         | YES — Enterprise | Chatter attachments; `mail` module  |
| `studio`               | Not mentioned but assumed       | YES — Enterprise | Not applicable to MVP               |
| `knowledge`            | Excluded from MVP               | YES — Enterprise | Not required                        |
| Multi-level approval routing (native) | Phase 3 — Workflows | Enterprise feature | See Section 6 |

---

## 6. Community Edition Limitations and Recommended Alternatives

### 6.1 Approvals App (Critical Gap)

The MVP document lists "Approvals" as a core application to install and describes multi-level approval workflows for procurement, leave, and payment. In Odoo 17 Community, there is **no dedicated Approvals app**. The Enterprise `approvals` module provides a configurable approval matrix UI.

**Community alternatives:**

| Approval Type     | Community Solution                                         | Configuration Method          |
|-------------------|------------------------------------------------------------|-------------------------------|
| Purchase approval | `purchase` settings: enable "Purchase Order Approval" + set approval threshold | System Settings > Purchase    |
| Purchase requisition | `purchase_requisition` (Community) — call for tenders, blanket orders | Native module                 |
| Leave approval    | `hr_holidays` — two-level: Manager → HR Manager approval  | Leave type configuration      |
| Payment/Invoice approval | Accounting journal lock + workflow states           | Manual with activity tracking |
| Multi-level routing | `base_automation` — automated email notifications and activity assignments | Configuration-based           |

**Risk note:** The Community purchase approval setting supports a single approval threshold (₦X → requires manager approval). It does **not** natively support the three-tier procurement approval ladder described in the MVP (₦500K / ₦5M / unlimited). This must be implemented via:
1. Single system-wide threshold for first-level approval.
2. `base_automation` rules to trigger escalation notifications to higher approvers.
3. Documented manual procedure for tier-2 and tier-3 approvals.

This is a known limitation and must be documented in the Decision Log.

### 6.2 Sign Module

The MVP mentions `Sign` as an optional demo module. This is Enterprise-only. For the MVP demo:
- PDF attachments to purchase orders and leave requests serve as an acceptable substitute.
- No action needed — simply exclude from module installation.

### 6.3 Documents Module

The MVP mentions `Documents` as an optional demo module. The Community edition includes chatter-based attachments on all records. For the MVP demo, this is sufficient.

### 6.4 Reporting

Community Edition has limited native reporting. The `om_account_daily_reports` and `accounting_pdf_reports` custom addons (already available from FamOil) provide acceptable supplementary reporting for the finance MVP.

### 6.5 Studio / View Customisation

Not available in Community. All view customisation must be done via custom module XML views. For MVP scope (Finance, Procurement, HR), this is not a blocker — the standard views are adequate.

---

## 7. Reusable Assets Found

### 7.1 From FamOil (`/Users/mac/odoo17/`)

| Asset | Type | Reusability | Notes |
|-------|------|-------------|-------|
| `l10n_ng` Nigeria CoA + WHT/VAT config | Module config | HIGH | Already validated for Nigerian NGN accounting |
| `om_account_accountant` | Custom addon | HIGH | Directly reusable — copy to NADF addons path |
| `om_account_budget` | Custom addon | HIGH | Budget management — directly applicable to NADF |
| `om_account_daily_reports` | Custom addon | HIGH | Daily report PDFs |
| `om_fiscal_year` | Custom addon | HIGH | Custom fiscal year (NADF may use Jan–Dec or government fiscal year) |
| `om_recurring_payments` | Custom addon | HIGH | Recurring payment schedules |
| `accounting_pdf_reports` | Custom addon | HIGH | PDF accounting reports |
| `.github/workflows/doc_lint.yml` | CI/CD | HIGH | Adapt for NADF repo |
| `.github/workflows/security_scan.yml` | CI/CD | HIGH | Directly applicable |
| `.github/workflows/ci_review.yml` | CI/CD | HIGH | Directly applicable |
| `.github/workflows/backup_check.yml` | CI/CD | HIGH | Adapt for NADF |
| `.claude/hooks/` (all 5 hooks) | Governance | HIGH | Directly portable to NADF |
| `scripts/backup_famoil.sh` | Script | HIGH | Adapt → `backup_nadf.sh` |
| `scripts/restore_famoil.sh` | Script | HIGH | Adapt → `restore_nadf.sh` |
| `docs/IMPLEMENTATION_STANDARDS.md` | Governance | HIGH | **Reference, do not duplicate** — NADF CLAUDE.md points to this |
| `docs/architecture/ARCHITECTURAL_PRINCIPLES.md` | Governance | HIGH | **Reference, do not duplicate** |
| `docs/famoil_erp_template/NIGERIA_COMPLIANCE.md` | Compliance | HIGH | Nigerian VAT/WHT/Pension — applicable to NADF accounting |
| `docs/famoil_erp_template/DECISION_LOG.md` (DEC-001) | Decision | HIGH | Community vs Enterprise decision — directly applicable |
| `csv_templates/product_categories.csv` | CSV template | MEDIUM | Adapt for NADF procurement categories |
| `csv_templates/locations.csv` | CSV template | MEDIUM | Adapt for NADF stores (Main Store, ICT Store, Consumables) |
| `csv_templates/warehouses.csv` | CSV template | MEDIUM | Adapt for NADF warehouse |

### 7.2 From WamaCare (`/Users/mac/Documents/Aliyu/ODOO/Projects/TIKO/WamaCare/`)

| Asset | Type | Reusability | Notes |
|-------|------|-------------|-------|
| `csv_templates/wamacare/hr_department.csv` | CSV template | HIGH | Adapt for NADF departments (Finance, Procurement, HR, Executive Office) |
| `csv_templates/wamacare/hr_employees.csv` | CSV template | HIGH | Adapt for NADF sample employees |
| `csv_templates/wamacare/wamacare_vendors.csv` | CSV template | HIGH | Adapt for NADF sample vendors |
| `csv_templates/wamacare/wamacare_products.csv` | CSV template | HIGH | Adapt for NADF service/goods products |
| `wamacare.conf` | Config | HIGH | Adapt → `nadf.conf` (change port to 8071, DB to NADF) |
| HR module configuration (hr_holidays leave types) | Config pattern | HIGH | WamaCare configured Annual, Sick, Casual leaves — replicate pattern |
| Nigerian NGO chart of accounts (68 accounts) | DB pattern | MEDIUM | Structure applicable; NADF is government body, will diverge in income/equity accounts |
| Purchase approval threshold config (₦200,000) | Config pattern | MEDIUM | NADF uses different thresholds — adapt |
| 5-user role setup (admin, finance, HR, field, officer) | Config pattern | HIGH | NADF role structure mirrors this |

### 7.3 From NADF Local Documents (`/Users/mac/Documents/Aliyu/NADF/`)

| Asset | Type | Reusability | Notes |
|-------|------|-------------|-------|
| `nadf_Import_User_Sample#1.csv` | Real data | HIGH | 22 NADF staff with @nadf.gov.ng emails — use as employee import source |
| `users_credentials.csv` | Real data | HIGH | Full names, departments — cross-reference for employee records |
| `NADF ERP.pdf` / `NADF ERP.pptx` | Reference | MEDIUM | Background business context (not imported to Odoo) |

**Privacy note:** The NADF staff names are real data. For the MVP demo environment, use these names with sample/demo credentials (not real passwords). Do not store credentials in Git.

### 7.4 From Software Factory Governance (`/Users/mac/software-factory-governance/`)

| Asset | Type | Reusability |
|-------|------|-------------|
| `templates/decision_log_template.md` | Template | HIGH — seed NADF DECISION_LOG.md |
| `templates/implementation_history_template.md` | Template | HIGH — seed NADF IMPLEMENTATION_HISTORY.md |
| `templates/roadmap_template.md` | Template | HIGH — seed NADF roadmap |
| `templates/onboarding_template.md` | Template | HIGH — seed NADF onboarding docs |
| `templates/project_readme_template.md` | Template | HIGH — seed NADF README |
| `templates/pull_request_template.md` | Template | HIGH — add to `.github/` |
| `templates/module_registry_template.md` | Template | HIGH — track NADF module state |
| `onboarding/AI_ONBOARDING_STANDARD.md` | Governance | HIGH — reference for NADF onboarding |

---

## 8. Assets Not Suitable for Reuse

| Asset | Source | Reason |
|-------|--------|--------|
| `mrp`, `mrp_account`, `mrp_landed_costs` | FamOil | Manufacturing-specific — NADF has no manufacturing |
| `stock_crude_oil_tank_restriction` | FamOil custom | Agro-processing-specific — not applicable |
| `stock_landed_cost_po_check` | FamOil custom | Agro-processing validation — not applicable |
| `custom_addons_farm/farm_layers` | FamOil | Agricultural farm layer — not applicable |
| `sale`, `sale_management`, `sale_mrp`, etc. | FamOil | Sales workflow — excluded from NADF MVP |
| FamOil BOM, work centre, routing CSVs | FamOil | Manufacturing data — not applicable |
| `wamacare_safeguarding` | WamaCare custom | NGO safeguarding module — not applicable |
| WamaCare beneficiary / programme data | WamaCare | NGO-specific — not applicable to NADF |
| FamOil costing configuration (FIFO, avg cost) | FamOil | Industrial costing — NADF uses simple cost allocation |
| WamaCare project/M&E modules | WamaCare | Excluded from NADF MVP scope |

---

## 9. Recommended Module Installation List for NADF MVP

The following modules should be installed on the fresh `NADF` database. They are all available in the local Odoo 17 Community installation.

### Platform / Core
- `base`
- `mail`
- `discuss`
- `contacts`
- `base_automation`
- `portal`
- `auth_signup`

### Finance
- `account`
- `account_payment`
- `account_payment_term`
- `analytic`
- `l10n_ng`
- `om_account_accountant`
- `om_account_budget`
- `om_account_daily_reports`
- `om_fiscal_year`
- `om_recurring_payments`
- `accounting_pdf_reports`

### Procurement
- `purchase`
- `purchase_stock`
- `purchase_requisition`
- `stock`
- `stock_account`

### Human Resources
- `hr`
- `hr_holidays`
- `hr_org_chart`
- `hr_contract`

### Not to Install (Enterprise / Out of Scope)
- `approvals` — Enterprise only; not installable
- `sign` — Enterprise only; not installable
- `documents` — Enterprise only; not installable
- `payroll`, `hr_payroll` — excluded from MVP
- `mrp`, `manufacturing` — not applicable
- `sale`, `sale_management` — not applicable to NADF

---

## 10. Community Edition Limitations Summary

| Limitation | Impact on MVP | Severity | Mitigation |
|------------|---------------|----------|------------|
| No `approvals` app | Cannot build configurable multi-level approval matrix UI | HIGH | Use `purchase` settings + `base_automation` + documented manual procedures |
| Single purchase approval threshold | Cannot configure 3-tier procurement ladder natively | MEDIUM | Set threshold at ₦500K; document escalation to Director/ES as manual with email notification via automated action |
| No `sign` module | Cannot demonstrate digital signature | LOW | Exclude from MVP scope; note as Phase 2 Enterprise feature |
| No `documents` module | Cannot demonstrate document management | LOW | Use chatter attachments; note as Phase 2 Enterprise feature |
| No `studio` | Cannot drag-and-drop customise views | LOW | No custom views needed for MVP |
| Limited HR payroll | No payroll processing | LOW | Payroll explicitly excluded from MVP |
| No `knowledge` module | No knowledge base | LOW | Knowledge excluded from MVP |
| No native audit log viewer | Audit trail via `account_audit_trail` only | LOW | Enable `account_audit_trail` for financial records; `mail` chatter provides activity log elsewhere |

---

## 11. Recommended Implementation Sequence

The following sequence is proposed for implementation after operator approval of this report.

### Phase 0 — Project Foundation (Pre-Configuration)

1. Create NADF project governance structure (CLAUDE.md, README, DECISION_LOG, IMPLEMENTATION_HISTORY, roadmap)
2. Create `nadf.conf` (port 8071, DB = NADF)
3. Adapt CI/CD workflows from FamOil for NADF repo
4. Adapt governance hooks from FamOil for NADF
5. Commit initial project structure to Git (`main` branch)

### Phase 1 — Database and Environment

6. Create fresh `NADF` PostgreSQL database
7. Install core modules (account, purchase, hr, hr_holidays, l10n_ng, etc.)
8. Configure company (NADF, Abuja FCT, Nigeria, NGN)
9. Create admin and role-based users (8 demo users per MVP doc)

### Phase 2 — Finance Configuration

10. Configure Chart of Accounts (adapt l10n_ng + NADF-specific: Grants, Pension Payables, etc.)
11. Set fiscal year (Jan–Dec or government fiscal year — confirm with operator)
12. Configure journals (Bank, Cash, Purchase, Sales, Miscellaneous)
13. Configure analytic accounts / cost centres (Finance Unit, Procurement Unit, HR Unit, Executive)
14. Configure payment terms
15. Create sample vendors (4 per MVP doc)
16. Configure budget (if `om_account_budget` is installed)

### Phase 3 — Procurement Configuration

17. Configure product categories (Office Supplies, ICT, Operations)
18. Create sample products (Laptop, Printer, Toner, Office Chair, Internet Subscription)
19. Configure warehouse and stores (Main Store, ICT Store, Consumables Store)
20. Enable and configure purchase order approval (set threshold)
21. Configure purchase requisition workflow

### Phase 4 — HR Configuration

22. Create departments (Finance, Procurement, HR, Executive Office)
23. Create job positions (Officer, Senior Officer, Manager, Head of Unit, Director, Executive Secretary)
24. Import/create sample employees (from NADF staff CSV)
25. Configure leave types (Annual, Sick, Casual, Maternity, Study)
26. Configure leave approval chains per leave type

### Phase 5 — Approval Workflow Configuration

27. Configure purchase order approval threshold
28. Configure `base_automation` rules for procurement escalation notifications
29. Configure leave manager assignments
30. Configure invoice approval procedure
31. Document all approval configurations in NADF_MVP_APPROVAL_WORKFLOWS.md

### Phase 6 — Demo Scenarios and Validation

32. Run Scenario 1: Laptop purchase (Requisition → Approval → RFQ → PO → Receipt)
33. Run Scenario 2: Annual leave request (Employee → Supervisor → HR)
34. Run Scenario 3: Vendor invoice payment (Invoice → Approval → Payment)
35. Run Scenario 4: Approval escalation demonstration
36. Document results in NADF_MVP_TEST_REPORT.md

### Phase 7 — Handover Preparation

37. Create backup and rollback procedure
38. Create handover note
39. Commit all docs to Git
40. Await instruction to push to GitHub

---

## 12. Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| `approvals` workaround insufficient for stakeholder expectations | MEDIUM | HIGH | Clearly demonstrate the Community-native approval flow; set expectations in handover note |
| Three-tier procurement approval not achievable natively | HIGH | MEDIUM | Configure single threshold + documented escalation procedure; log this as DEC-001 in NADF Decision Log |
| Performance degradation — 3 Odoo instances running simultaneously on MacBook Air | MEDIUM | MEDIUM | Run only the required instance during each work session; document in operations notes |
| Real NADF staff data used in demo environment | HIGH | MEDIUM | Use real names, demo passwords only; never commit credentials to Git |
| MVP document assumes some Enterprise features | CONFIRMED | MEDIUM | All Enterprise references identified in this report; alternatives documented |
| No NADF database backup plan before configuration | LOW | HIGH | Create `backup_nadf.sh` before any data is entered; run after each phase |
| GitHub repo empty — all governance work lost if local disk fails before first push | HIGH | HIGH | Push governance skeleton immediately after operator approval of inspection report |

---

## 13. Immediate Next Actions

The following actions are proposed pending operator approval of this report.

| # | Action | Type | Blocker? |
|---|--------|------|----------|
| 1 | Operator reviews and approves this inspection report | Decision | YES — gates all further work |
| 2 | Operator confirms: use fresh NADF database or restore from a base? | Decision | YES |
| 3 | Operator confirms: fiscal year Jan–Dec or Nigerian government Oct–Sep? | Decision | YES for finance config |
| 4 | Create NADF governance structure (CLAUDE.md, DECISION_LOG, IMPLEMENTATION_HISTORY, ROADMAP) | Foundation | After approval |
| 5 | Create `nadf.conf` (port 8071) | Foundation | After approval |
| 6 | Adapt and copy CI/CD workflows from FamOil | Foundation | After approval |
| 7 | Create initial Git commit and await push instruction | Foundation | After approval |
| 8 | Create `NADF` PostgreSQL database | Configuration | After foundation |
| 9 | Install required MVP modules | Configuration | After DB creation |
| 10 | Begin Phase 2 Finance Configuration | Configuration | After modules installed |

---

## 14. Findings Summary

| Category | Finding |
|----------|---------|
| GitHub repo | Empty — needs full setup |
| Odoo version | 17.0 Community — confirmed correct platform |
| NADF database | Does not exist — must be created fresh |
| Required modules | All available locally except Enterprise-only features |
| Enterprise gap (critical) | `approvals` app — Community workaround identified and documented |
| Enterprise gap (low) | `sign`, `documents` — exclude from MVP; note as Phase 2 |
| Reusable governance | FamOil: workflows, hooks, scripts, custom addons — HIGH reuse |
| Reusable HR config | WamaCare: HR CSV templates, leave config, user roles — HIGH reuse |
| Reusable compliance | FamOil: l10n_ng, Nigeria VAT/WHT config — HIGH reuse |
| Real NADF data available | 22 staff names/emails available for employee import |
| Port assignment | 8071 assigned to NADF (8069 = FamOil, 8070 = WamaCare) |
| Immediate risk | GitHub repo completely empty — first push should happen soon after approval |

---

## 15. Document Governance

This document must be superseded by implementation documents as work proceeds. Do not update this report with post-implementation findings — create new phase documents instead.

Next expected document: `docs/NADF_REUSABLE_ASSET_ASSESSMENT.md`

---

*Report produced by: AI Developer (Claude Code) | Inspection date: 2026-06-02*
*Onboarded from: Software Factory Executive Continuity Briefing v1.3, AI_ONBOARDING_V2.txt, NADF ERP MVP Product Document v1.0*
