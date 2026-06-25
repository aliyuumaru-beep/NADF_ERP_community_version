# DEC-OCA-02 — Governance Resolution Review
## `account_budget_oca` Compatibility Failure: Options Analysis

**Document ID:** DEC-OCA-02-GRR-001
**Decision reference:** DEC-OCA-02 (logged 2026-06-25 in `docs/DECISION_LOG.md`)
**Prepared by:** A1 Master Orchestrator — G1, G2, G3 consolidated
**Date:** 2026-06-25
**Status:** OPEN — awaiting G1/G2/G3 resolution selection

> **Purpose:** This document provides the governance resolution for the blocked `account_budget_oca` installation. It evaluates four resolution options, provides G1/G2/G3 findings for each, and issues a consolidated recommendation. No implementation is authorised until the resolution decision is ratified.

---

## 1. Background

During WP-01 Foundation Hardening (2026-06-25), the installation of `account_budget_oca` 17.0.1.0.0 from OCA/account-budgeting@17.0 failed with the following error:

```
odoo.tools.convert.ParseError: Field 'theoritical_amount' does not exist on model account.analytic.account
  File: account_analytic_account_views.xml
  Module: account_budget_oca
```

**Root cause analysis:**

In Odoo 17, the `account.analytic.account` model was substantially restructured as part of a broader analytic accounting overhaul. The field `theoritical_amount` (note: the original OCA field name itself contains a spelling error — "theoritical" instead of "theoretical") was a computed display field that existed on `account.analytic.account` in older Odoo versions. It was removed or relocated in Odoo 17 CE. The OCA module `account_budget_oca` 17.0.1.0.0 contains an XML view definition that references this field, making the module non-installable on this Odoo 17 build without a patch to the view XML.

**Impact on WP-02:**
- WP02-07 (budget control configuration) is blocked — no budget module is operational.
- Budget CSV `csv_templates/nadf_budget_fy2026.csv` (40 lines from Phase 7) is prepared but cannot be loaded.
- All other WP-02 items were unaffected and completed.

**Impact on Phase 1 UAT:**
- Budget-vs-actual reporting scenario cannot be executed in UAT.
- All other Finance UAT scenarios (CoA, AP/AR workflow, dual-auth, analytic tracking) are unaffected.

---

## 2. Options Evaluated

### Option A — Upgrade to a Later OCA Patch Release

**Description:** Check whether OCA/account-budgeting@17.0 has released a version later than 17.0.1.0.0 that removes or replaces the `theoritical_amount` field reference in `account_analytic_account_views.xml`. If such a version exists, update the sparse checkout and reinstall.

**Investigation required:**
- Inspect OCA/account-budgeting GitHub commits on the `17.0` branch since 17.0.1.0.0.
- Check release tags for 17.0.1.1.0, 17.0.1.2.0, or later.
- If a newer version exists, review the diff for `account_analytic_account_views.xml` to confirm the field reference is removed.
- If confirmed, re-attempt install on a drill DB before NADF DB.

**Architectural impact:** Low. Same module family; no change to the budget data model or module dependency chain. If the OCA patch resolves the view XML, the installation proceeds as originally planned. `MODULE_REGISTRY.md` and `DECISION_LOG.md` require version update only.

**Governance impact:** Low. If the patch works, DEC-OCA-02 is resolved with a version change. Standard WP-01 amendment PR required. G1/G2/G3 exit gate for the amended WP-01 sub-task is a lightweight review.

**Technical risk:** Low-Medium. The newer OCA patch may fix the view XML but introduce other incompatibilities with the current Odoo 17 build (e.g., model field renames, API changes between Odoo 17 minor versions). The fix must be validated on a drill DB before the NADF DB.

**Long-term maintainability:** Good. OCA modules on the 17.0 branch are expected to receive ongoing maintenance; a patched release is the intended upgrade path.

**G1 finding (Option A):** Architecturally preferred if the patch exists. OCA is the authorized source for this capability (Transfer Package v2.1). Checking for a patch before committing to alternatives is the correct first step. G1 recommends Option A as the primary investigation path.

**G2 finding (Option A):** Documentation overhead is minimal — version number update in `MODULE_REGISTRY.md` and a DEC-OCA-02 resolution note in `DECISION_LOG.md`. Acceptable.

**G3 finding (Option A):** No security concern. Patch upgrade follows the same vetting path as the original install. Drill DB validation required before NADF DB install.

**Option A verdict: RECOMMENDED AS FIRST INVESTIGATION STEP.** If a working patch exists, execute Option A. If no patch exists or the patch fails drill DB validation, escalate to Option C.

---

### Option B — Use Odoo 17 CE Native `account_budget`

**Description:** In Odoo 16 CE, a native `account_budget` module existed for basic budget management. Evaluate whether this native module is available in Odoo 17 CE on this installation.

**Investigation finding (pre-decisional):**

Based on the Odoo 17 Community Edition module set loaded on this system (100 modules at WP-01 registry check), `account_budget` was not present in the installed module list. Odoo 17 moved budget management capabilities into the `account_accountant` module, which is part of Odoo Enterprise (`account_accountant` is listed as a prohibited Enterprise module in `CLAUDE.md`). The native CE `account_budget` module was deprecated in Odoo 17 and is no longer distributed as a standalone CE module.

**Architectural impact:** High (negative). Attempting to use `account_accountant` or any Enterprise budget feature violates the CE-only constraint in `CLAUDE.md` and PEG-6 governance terms. This option is not viable under current platform governance.

**Governance impact:** Critical blocker. Installing an Enterprise module is prohibited. Any attempt would trigger a governance breach and require G3 emergency reversal.

**Technical risk:** Very High. The `account_accountant` Enterprise module would conflict with the CE `account` module on the same installation. Recovery would require a full DB restore.

**Long-term maintainability:** N/A — prohibited.

**G1 finding (Option B):** G1 confirms that native CE `account_budget` does not exist as a standalone Odoo 17 CE module. The budget capability was consolidated into `account_accountant` (Enterprise). Option B is **not viable** under the CE-only platform constraint.

**G2 finding (Option B):** No documentation path exists for a prohibited module install.

**G3 finding (Option B):** Option B constitutes a platform governance violation. G3 formally rejects Option B.

**Option B verdict: REJECTED. CE-only platform constraint prohibits this path.**

---

### Option C — Defer Budget Configuration to Phase 2

**Description:** Accept that budget-vs-actual capability will not be available in Phase 1. Document the gap in the UAT test plan. Schedule budget module configuration — either via a repaired OCA version or a custom module — as a Phase 2 deliverable. The budget CSV (`csv_templates/nadf_budget_fy2026.csv`) is preserved for future use.

**Architectural impact:** Low. Phase 1 Finance configuration is fully operational without budget control. The analytic accounts (CC-ADM..CC-PRO) are in place and can serve as cost-centre tracking even without a budget comparison layer. The budget CSV is a ready-made input for Phase 2.

**Governance impact:** Low. WP02-07 is formally deferred; the WP-02 exit gate remains CONDITIONAL PASS. Phase 1 UAT scope is adjusted to exclude budget-vs-actual scenarios. A Phase 2 work package specification is required before budget configuration resumes.

**Technical risk:** Low. No module is installed or modified. Existing configuration is unchanged.

**Long-term maintainability:** Acceptable. Phase 2 can revisit Option A (OCA patch) or Option D (custom) with a full specification and budget data. The analytic structure already in place provides a compatible foundation.

**G1 finding (Option C):** Architecturally clean. Phase 1 is a foundation milestone; budget control is a Phase 2 operational capability. The CE analytic account infrastructure established in WP-02-06 is the correct Phase 1 deliverable. G1 accepts Option C if Option A investigation yields no working patch.

**G2 finding (Option C):** Requires the UAT test plan (WP-05) to explicitly document the budget-vs-actual scenario as OUT OF SCOPE for Phase 1 UAT. The WP-05 defect register template should include a pre-logged known gap entry. G2 accepts Option C with this documentation condition.

**G3 finding (Option C):** No security implications. Option C does not introduce any change to the running system. G3 accepts.

**Option C verdict: ACCEPTED AS FALLBACK. Proceed if Option A investigation yields no working OCA patch within one session. Option C is the safe floor — it does not degrade what is already working.**

---

### Option D — Custom Extension (`nadf_budget`)

**Description:** Build a custom Odoo module (`nadf_budget`) that implements NADF-specific budget management: budget line upload from CSV, budget-vs-actual comparison against analytic accounts, and a budget approval workflow matching the NADF RACI.

**Architectural impact:** Medium-High. A custom budget module would depend on `account` and `account_analytic`. It would not conflict with OCA `account_budget_oca` (since that module is not installed). However, it requires a full design specification before any development (CLAUDE.md: "No spec, no code").

**Governance impact:** High. A custom module requires:
- A Phase 2 product specification (BRQ session with NADF Finance)
- G1 architecture approval of the spec
- G2 quality review of spec documentation
- G3 security review of the data access model
- Full development → test → UAT cycle

This is a Phase 2/3 deliverable, not a Phase 1 task.

**Technical risk:** Medium. Custom module development carries the risk of incorrect budget calculations, analytic account mapping errors, or workflow mis-alignment with the NADF approval structure. Full testing cycle required.

**Long-term maintainability:** High (if well specified). A NADF-specific module can be tailored to the exact budget line structure from the CoA and FY2026 CSV. However, it creates a maintenance obligation that OCA modules do not.

**G1 finding (Option D):** Option D is the correct long-term path only if OCA cannot provide a working module (Option A fails and OCA@17.0 remains broken). Phase 1 does not authorize custom module development beyond the two ratified modules (`nadf_vendor_onboarding`, `nadf_facilities_management`). Option D is a Phase 2/3 deliverable.

**G2 finding (Option D):** A spec document (`nadf_budget_spec.md`) would need to be authored and reviewed before development. G2 accepts Option D as a future option; rejects it for Phase 1 scope.

**G3 finding (Option D):** No objection to the concept; objects to doing it in Phase 1 without a spec. Budget data is financial data — access rules require careful design.

**Option D verdict: DEFERRED TO PHASE 2/3. Not in Phase 1 scope. Requires a full product specification.**

---

## 3. G1/G2/G3 Consolidated Recommendation

**Resolved path (two-stage):**

**Stage 1 — Option A investigation (next session):**
Check OCA/account-budgeting@17.0 for any patch release newer than 17.0.1.0.0. Specifically, inspect `account_analytic_account_views.xml` in the latest commit on the `17.0` branch. If a working patch exists:
- Install on drill DB; validate `--stop-after-init` exit 0.
- Update sparse checkout in `/Users/mac/oca_addons/account_budget_oca/`.
- Install on NADF DB; configure WP02-07.
- Update `MODULE_REGISTRY.md` with new version; log DEC-OCA-02 resolution in `DECISION_LOG.md`.
- Raise a WP-02 amendment PR.

**Stage 2 — Option C (fallback, triggered if Stage 1 yields no working patch):**
- Formally close WP02-07 as DEFERRED (Phase 2).
- Add a pre-logged budget gap entry to the WP-05 UAT defect register.
- Log DEC-OCA-02 resolution decision as "Option C — Deferred" in `DECISION_LOG.md`.
- Amend WP-02 exit gate status from CONDITIONAL PASS (budget blocked) to CONDITIONAL PASS (budget deferred to Phase 2) — no functional change, but the tracking entry is cleaner.
- Add `nadf_budget` custom module spec to Phase 2 planning inputs as a carry-forward item.

**Option D** is registered as the Phase 2/3 fallback if OCA never ships a working 17.0 patch.

**Option B** is permanently rejected.

---

## 4. Action Register

| Action ID | Action | Owner | Status | Target |
|-----------|--------|-------|--------|--------|
| ACT-OCA02-01 | Investigate OCA/account-budgeting@17.0 for patch release > 17.0.1.0.0 | D2 Solution Builder | **OPEN** | Next session |
| ACT-OCA02-02 | If patch found: install on drill DB, validate, install on NADF DB, update MODULE_REGISTRY | D2 Solution Builder | Pending ACT-OCA02-01 | After patch confirmed |
| ACT-OCA02-03 | If no patch: formally log Option C decision in DECISION_LOG.md; update WP-02 exit gate status | A1 Orchestrator | Pending ACT-OCA02-01 | After investigation |
| ACT-OCA02-04 | Add budget gap to WP-05 UAT defect register template (known gap entry) | D1 Functional Architect | **OPEN** | WP-05 authoring |
| ACT-OCA02-05 | Add nadf_budget spec requirement to Phase 2 planning inputs | A1 Orchestrator | **OPEN** | Phase 2 planning |

---

## 5. Decision Authority

This resolution document requires ratification by the Business Sponsor (Aliyu / Lanasoft Technologies) for Stage 2 (Option C) if the budget gap affects Phase 1 UAT scope. Stage 1 (Option A investigation and patch install if successful) is within A1 normal operating authority and does not require fresh sponsor approval.

---

*Prepared by A1 Master Orchestrator. G1/G2/G3 findings consolidated. No implementation authorised pending ratification. Authority: PEG-6 approval 2026-06-24 · Transfer Package v2.1.*
