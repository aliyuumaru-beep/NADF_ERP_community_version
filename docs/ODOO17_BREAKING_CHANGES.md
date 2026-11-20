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

## Discovery log

| Date | Discovery | Source |
|------|-----------|--------|
| 2026-11-20 | Patterns 1–6 documented from FERMA OQ-24 post-mortem and Odoo 17 upgrade notes | WP-GOV-02 |
| 2026-11-20 | NADF codebase scanned — no existing violations found | `make pre-review` on HEAD |
