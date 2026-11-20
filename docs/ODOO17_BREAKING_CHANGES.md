# NADF ERP — Odoo 17 Breaking Changes Reference

**Pod:** POD-NADF  
**Date:** 2026-11-20  
**Authority:** WP-GOV-02 / DEC-GOV-02  
**Maintained by:** A1-NADF Orchestrator

This document is the reference for `scripts/pre_review_check.py` (check 4) and the
G1 reviewer checklist (`g1_checklist.odoo17_compat` in `.governance.json`).

---

## Patterns flagged by `make pre-review`

| # | Pattern | Reason |
|---|---------|--------|
| 1 | `portal.portal_my_home_entry` | View ID removed in Odoo 17; use `portal.portal_docs_entry`. Root cause of OQ-24 on FERMA pod. |
| 2 | `inherit_id="portal.portal_my_home_entry"` | XML form of pattern 1 — also flagged explicitly for richer diagnostics. |
| 3 | `<tree` in view XML | Odoo 17 renames list views to `<list>`. |
| 4 | `//tree` in XPath expressions | Same rename — XPath must use `//list`. |
| 5 | `fields.Boolean.convert_to_cache` | Method removed in Odoo 17. |
| 6 | `import openerp` / `from openerp` | Odoo 8/9 era import alias; not valid in Odoo 17. |

---

## Project-specific exceptions

None. All patterns are genuine Odoo 17 incompatibilities in this codebase.

If a pattern is intentionally used (e.g., the FERMA pod has a build that pre-dates
the `<tree>`→`<list>` rename), it must be documented here with:
- The module and file path
- The WP that established the exception
- Why the false positive is safe

---

## Known pre-existing violations

The following patterns exist in NADF custom modules before WP-GOV-02. They are
acknowledged, documented here, and tracked for remediation under future work
packages. `make pre-review` will NOT flag them on the WP-GOV-02 diff (the
diff-scoped check only inspects *changed* files); if the checker is ever run with
no diff (e.g., from main after merge), these may surface.

| Module | Files | Pattern | Violation count | Remediation |
|--------|-------|---------|-----------------|-------------|
| `nadf_vendor_onboarding` | `views/vendor_application_views.xml` | `<tree` | 2 | Track for `<list>` rename — future portal/vendor WP |
| `nadf_facilities_management` | `views/fm_maintenance_plan_views.xml`, `fm_maintenance_schedule_views.xml`, `fm_contractor_views.xml`, `fm_job_complaint_views.xml`, `fm_consumable_request_views.xml`, `fm_inventory_report_views.xml`, `fm_job_order_views.xml` | `<tree` | 11+ | Track for `<list>` rename — future FM WP |

These are pre-WP-GOV-02 technical debt items, not new regressions introduced by
this work package. Odoo 17 currently accepts both `<tree>` and `<list>` (the
rename is complete but `<tree>` is not yet hard-removed). These will become errors
in a future Odoo minor release.

---

## Discovery log

| Date | Discovery | Source |
|------|-----------|--------|
| 2026-11-20 | Patterns 1–6 documented from FERMA OQ-24 post-mortem and Odoo 17 upgrade notes | WP-GOV-02 |
| 2026-11-20 | NADF codebase scanned with `make pre-review` — no violations in *changed files* (diff-scoped check). Pre-existing `<tree>` usages in `nadf_vendor_onboarding` and `nadf_facilities_management` documented above as known technical debt. | WP-GOV-02 |
