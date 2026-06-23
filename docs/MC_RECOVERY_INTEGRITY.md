# M-C Module Recovery — Source-vs-Destination Integrity Evidence

**Milestone:** M-C Governance Certification & Recovery
**Date:** 2026-06-22
**Method:** SHA-256 per-file manifest of source tree vs recovered destination tree (relative paths, `__pycache__`/`*.pyc`/`.DS_Store` excluded), compared with `diff`. Empty diff = byte-identical recovery.
**Rule honoured:** Integrity PASS is recorded **before** the source copy is deleted from the FamOil repository (operator requirement, M-C approval).

---

## A. `nadf_vendor_onboarding`

- **Source:** `/Users/mac/odoo17/custom_addons/nadf_vendor_onboarding/` (untracked in `famoil-erp` working tree)
- **Destination:** `/Users/mac/nadf_erp/custom_addons/nadf_vendor_onboarding/`
- **Files compared:** 12 source / 12 destination
- **SHA-256 diff result:** empty
- **VERDICT: PASS ✅**

| SHA-256 | File |
|---------|------|
| ccd4f636…aa8709 | `__init__.py` |
| 23ac234a…686e60 | `__manifest__.py` |
| a5b42ae4…0176c3 | `controllers/__init__.py` |
| 21a91389…5367f8 | `controllers/portal.py` |
| b3394ac2…6329c2 | `models/__init__.py` |
| b2608d3b…00f8a6 | `models/vendor_application.py` |
| c15b3a11…109c44a | `models/vendor_document_line.py` |
| 940bb821…b71b4 | `security/ir.model.access.csv` |
| 393f312a…0f3bf0 | `security/nadf_vendor_security.xml` |
| 74621ecd…d8ca50 | `templates/vendor_portal.xml` |
| 4f9b805c…436615 | `views/menus.xml` |
| 3daeeb06…2c0b83e | `views/vendor_application_views.xml` |

*(Full untruncated manifest captured at run time; hashes above abbreviated for the record.)*

---

## B. `nadf_facilities_management`

- **Source:** `/Users/mac/odoo17/custom_addons/nadf_facilities_management/` (committed in `famoil-erp` at `55c1787`, unpushed)
- **Destination:** `/Users/mac/nadf_erp/custom_addons/nadf_facilities_management/`
- **Files compared:** 33 source / 33 destination (matches the 33-file footprint of commit `55c1787`)
- **SHA-256 diff result:** empty
- **VERDICT: PASS ✅**

Representative anchors (full 33-file manifest verified identical):

| SHA-256 | File |
|---------|------|
| a5de7a65…c48da0 | `README.md` |
| 86b5770d…220d8 | `__manifest__.py` |
| d01b7129…927650 | `models/fm_job_order.py` |
| 9cba7f2f…104b0b | `security/fm_security.xml` |
| c40bd786…b50f938 | `tests/test_fm_e2e.py` |
| e06f5af0…197b0c | `wizards/fm_satisfaction_feedback_wizard.py` |

---

## Outcome

Both modules recovered byte-identically into the NADF deployment layer. Integrity PASS recorded.
FamOil cleanup (Section C of the M-C runbook) is authorised to proceed for **both** modules on the strength of this evidence.
