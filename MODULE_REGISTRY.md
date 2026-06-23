# MODULE_REGISTRY.md
## NADF ERP Programme — Module & Component Registry (POD-NADF)

**Document type:** Mandatory repository artifact (`17_MODULE_REGISTRY_STANDARD.md`, Repository Standard `10`)
**Layer:** Layer 4 — Client Deployment (`nadf_erp`)
**Platform:** Odoo 17 Community Edition · **Profile:** `23_PLATFORM_PROFILE_ODOO17_COMMUNITY.md`
**Created:** 2026-06-23 (Migration Sequence M-D) · **Maintained by:** A1 Software Factory Orchestrator
**Update rule:** Add/update an entry whenever a module, OCA dependency, script, or integration is added, recovered, or changed.

---

## 1. Custom modules (in `custom_addons/`, version-controlled here)

| Module | Version | Category | Depends on | Provenance | Status |
|--------|---------|----------|-----------|-----------|--------|
| `nadf_vendor_onboarding` | 17.0.1.0.0 | Procurement | `base`, `mail`, `purchase` | Built legacy Phase 9; recovered to this repo in M-C (`a9738b4`, `DEC-RECOVERY-001`) from FamOil untracked tree | Installed in `NADF` DB; **built / unratified** (governance ratification at M1) |
| `nadf_facilities_management` | 17.0.1.0.0 | Operations/Maintenance | `base`, `mail`, `hr`, `purchase`, `stock`, `account` | Built legacy Phase 10; relocated to this repo in M-C (`4ccb306`, `DEC-RECOVERY-002`) from `famoil-erp@55c1787` | Installed in `NADF` DB; **built / unratified** |

### `nadf_vendor_onboarding` — detail
- **Purpose:** Public vendor registration portal (`/vendor/register`, auth=public) with AI/Claude PDF compliance analysis.
- **Models:** `nadf.vendor.application`, `nadf.vendor.document.line`. **Controllers:** `controllers/portal.py`.
- **Security:** `group_vendor_officer`, `group_vendor_manager`; `security/ir.model.access.csv`.
- **External dependency:** `anthropic` Python SDK (model `claude-opus-4-8`); API key via `ir.config_parameter` `nadf.claude.api.key`. **License:** LGPL-3.
- **Files:** 12. **Install helper:** `scripts/install_vendor_onboarding.py`.

### `nadf_facilities_management` — detail
- **Purpose:** Facilities Management — Process 1 Reactive Maintenance (Job Complaint → Job Order → Repair → Monthly Batch), Process 2 Preventive Maintenance (Plan → Schedule → Execution → Payment), Process 3 Inventory Visibility & Quarterly Reporting.
- **Models:** `fm_job_complaint`, `fm_job_order`, `fm_contractor`, `fm_consumable_request`, `fm_maintenance_plan`, `fm_maintenance_schedule`, `fm_inventory_report`, `fm_notification_mixin`. **Wizard:** `fm_satisfaction_feedback_wizard`.
- **Security:** 8 groups + 16 `ir.rule` record rules (`security/fm_security.xml`).
- **Reports:** Job Order, Monthly Batch, Inventory (QWeb PDF). **Tests:** `tests/test_fm_e2e.py` (TransactionCase E2E, 3 processes). **License:** LGPL-3.
- **Files:** 33. **Known gap:** wkhtmltopdf not installed → PDF print path validated via HTML render only.

## 2. OCA modules (planned — Phase 1, not yet installed)

| Module | Source | Purpose | Status |
|--------|--------|---------|--------|
| `mis_builder` | OCA/account-financial-reporting | Executive/operational KPI dashboards | Planned (WP-OCA-01) |
| `account_budget_oca` | OCA/account-budgeting | Budget control vs analytic accounts | Planned |
| `purchase_request` | OCA/purchase-workflow | Multi-step requisition/approval | Planned |
| `purchase_requisition` | OCA/purchase-workflow | RFQ / tender comparison | Planned |
| `helpdesk_mgmt` | OCA/helpdesk | ICT helpdesk (CE replacement for EE helpdesk) | Planned |
| OCA payroll base | OCA/payroll | Foundation for `nadf_payroll_ng` | Planned (BL-OCA-07) |

> No OCA module is installed yet; each requires Odoo 17 CE compatibility check + version pin + Decision Log entry before installation (MR-12).

## 3. Future custom modules (specification-gated — not built)
`nadf_payroll_ng`, `nadf_vendor_compliance`, `nadf_facility`, `nadf_legal_contract`, `nadf_investment`, `nadf_me_indicators` — see `planning/WORK_PACKAGES.md` (Phase 2 specs → Phase 3 dev). No spec, no code.

## 4. Native Odoo 17 CE modules in scope (configuration, not custom code)
`account`, `account_asset`, `fleet`, `hr`, `hr_holidays`, `hr_recruitment`, `purchase`, `stock`, `project`.

## 5. Operational scripts (`scripts/`)
| Script | Purpose |
|--------|---------|
| `backup_nadf.sh` | DB + filestore backup (read-safe) — M-C |
| `restore_nadf.sh` | Restore **drill** to a temp DB (refuses live `NADF`) — M-C |
| `install_vendor_onboarding.py` | Install helper for `nadf_vendor_onboarding` |
| `phase11_org_chart_restructure.py` | Legacy HR org-chart script (tracked; not part of M-D execution) |
| `phase1_`–`phase8_*` | Legacy reproducible configuration scripts (Phases 1–8) |

## 6. Prohibited (Enterprise) — never in this registry
`web_studio`, `sign`, `documents`, `documents_spreadsheet`, `knowledge`, `hr_payroll` (EE), `helpdesk` (EE), `industry_fsm`, `account_accountant`. Audit 2026-06-22: none installed (`DEC-PLATFORM-001`). Note: `spreadsheet`/`spreadsheet_dashboard` present are **LGPL-3 CE core**, not Enterprise.
