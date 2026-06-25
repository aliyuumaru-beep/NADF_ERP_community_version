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

## 2. OCA modules (Phase 1 — installed under WP-01, 2026-06-25)

| Module | Source repo | Odoo 17 version | Install date | Capability | Decision | Status |
|--------|-------------|-----------------|--------------|-----------|----------|--------|
| `mis_builder` | OCA/mis-builder@17.0 | 17.0.1.5.0 | 2026-06-25 | CA-01 executive dashboard | DEC-OCA-01 | ✅ Installed in `NADF` DB |
| `purchase_request` | OCA/purchase-workflow@17.0 | 17.0.2.3.4 | 2026-06-25 | CA-02 multi-step requisition | DEC-OCA-03 | ✅ Installed in `NADF` DB |
| `helpdesk_mgmt` | OCA/helpdesk@17.0 | 17.0.1.10.4 | 2026-06-25 | CA-04 ICT helpdesk | DEC-OCA-04 | ✅ Installed in `NADF` DB |
| `purchase_requisition` | **Odoo 17 CE native** | 17.0.0.1 | Pre-existing | CA-02 RFQ/tender | DEC-OCA-05 | ✅ CE native; installed |
| `account_budget_oca` | OCA/account-budgeting@17.0 | 17.0.1.0.0 | — | CA-01 budget control | DEC-OCA-02 | ❌ **BLOCKED** — field `theoritical_amount` not in `account.analytic.account` on this Odoo build; escalated |

### OCA dependency modules (installed as prerequisites of mis_builder)

| Module | Source repo | Odoo 17 version | Install date | Purpose |
|--------|-------------|-----------------|--------------|---------|
| `report_xlsx` | OCA/reporting-engine@17.0 | 17.0.1.0.2 | 2026-06-25 | XLSX export engine (mis_builder dep) |
| `date_range` | OCA/server-ux@17.0 | 17.0.1.2.1 | 2026-06-25 | Date range objects (mis_builder dep) |

> `account_budget_oca` installation blocked by a compatibility error in OCA/account-budgeting 17.0.1.0.0. Finding logged under DEC-OCA-02. Escalated to G1/G2/G3 for resolution decision before WP-02 budget sub-task begins.

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
