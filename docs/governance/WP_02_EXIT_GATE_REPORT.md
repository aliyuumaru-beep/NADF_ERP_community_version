# WP-02 — Finance Core: Exit Gate Report
## NADF ERP Programme — Governance Document

**Document ID:** WP-02-EGR-001
**Work Package:** WP-02 — Finance Core
**Phase:** 1 — Foundation
**Prepared by:** A1 Master Orchestrator (G1/G2/G3 consolidated)
**Date:** 2026-06-25
**Status:** CONDITIONAL PASS

> This report is the authoritative exit gate record for WP-02. It supersedes any interim status notes in `NEXT_ACTION.md` for the purposes of milestone closure. All three governance reviewers (G1 Architecture, G2 Quality, G3 Security) have contributed findings below.

---

## 1. Scope Delivered

WP-02 Finance Core re-validated all legacy Phase 2 Finance configuration against the NADF 8-digit government Chart of Accounts loaded in Phase 7, and established the financial workflows, user assignments, and analytic structures required for Phase 1 UAT readiness.

| Deliverable ID | Deliverable | Delivered? |
|---------------|------------|-----------|
| D-WP02-01 | CoA re-validated against NADF 8-digit structure | ✅ Yes |
| D-WP02-02 | CoA exported as reference CSV | ✅ Yes (client review pending) |
| D-WP02-03 | Vendor bill workflow validated (draft → post → reverse) | ✅ Yes |
| D-WP02-04 | Payment workflow validated; dual-auth mechanism confirmed | ✅ Yes (advisory) |
| D-WP02-05 | Finance user accounts assigned to correct groups | ✅ Yes |
| D-WP02-06 | Analytic accounts aligned to NADF budget lines | ✅ Yes |
| D-WP02-07 | Budget control via `account_budget_oca` | ❌ No — blocked (DEC-OCA-02) |
| D-WP02-08 | mis_builder KPI dashboard configured | ❌ No — deferred (client action) |
| D-WP02-09 | Native CE financial reports verified | ✅ Yes |
| D-WP02-10 | mail.thread audit trail confirmed on account.move | ✅ Yes |
| D-WP02-11 | WHT/VAT tax accounts verified; client sign-off route confirmed | ✅ Yes |

**Delivered:** 9 of 11. **Blocked:** 1 (D-WP02-07). **Deferred:** 1 (D-WP02-08).

---

## 2. Acceptance Criteria Status

| AC ID | Criterion | Result | Evidence |
|-------|-----------|--------|---------|
| AC-WP02-01 | 319 NADF 8-digit accounts active; 71 CE legacy accounts deprecated | **PASS** | DB query: `SELECT COUNT(*) FROM account_account WHERE active=true` → 319; deprecated count confirmed |
| AC-WP02-02 | CoA reference CSV exported; client review record initiated | **PASS (partial)** | `csv_templates/nadf_coa_revalidated_20260625.csv` — 319 rows + header present; client signature not yet received |
| AC-WP02-03 | Vendor bill draft → posted cycle validated; reversal executed cleanly | **PASS** | BILL/2026/06/0002 created (draft), posted, reversed via `account.move.reversal` wizard with date 2026-06-25; no orphan moves |
| AC-WP02-04 | Payment dual-auth advisory mechanism active | **PASS (advisory)** | 4 base.automation rules active: Invoice Tier 2, Invoice Tier 3, PO Tier 2, PO Tier 3 — DEC-WP02-001; hard block deferred to Phase 2 custom module |
| AC-WP02-05 | Finance staff assigned to correct user groups | **PASS** | `finance.officer` → Finance Officer; `head.finance` → Finance Manager + CFO; both confirmed via DB query |
| AC-WP02-06 | 5 analytic accounts active and named per NADF department cost-centre convention | **PASS** | CC-ADM, CC-EXE, CC-FIN, CC-HR, CC-PRO under "Projects" analytic plan — DEC-WP02-002; plan rename to "NADF Departments" deferred to client review |
| AC-WP02-07 | Budget control active via `account_budget_oca` | **FAIL (blocked)** | DEC-OCA-02: `account_budget_oca` 17.0.1.0.0 incompatible — field `theoritical_amount` missing from `account.analytic.account` in this Odoo 17 build; installation blocked; escalated to G1/G2/G3 (see §6) |
| AC-WP02-08 | mis_builder dashboard configured with NADF KPI set | **DEFERRED** | Client KPI sign-off required before dashboard configuration; module installed and operational; configuration blocked on client action |
| AC-WP02-09 | CE native financial reports accessible (Trial Balance, P&L, Balance Sheet, aged reports) | **PASS** | 5 `account.report` records confirmed in NADF DB (CE `account` module) |
| AC-WP02-10 | mail.thread audit trail on account.move confirmed | **PASS** | `account.move` has `mail.thread` mixin; message history confirmed on BILL/2026/06/0002 |
| AC-WP02-11 | WHT (41030102) and VAT (41030103) tax accounts correct; no changes required pending client sign-off | **PASS** | WHT: 14 tax lines; VAT: 8 tax lines — correct accounts confirmed. No amendment made; client sign-off route documented |

**Overall AC result:** 9 PASS · 1 FAIL (blocked) · 1 DEFERRED

---

## 3. Deferred Items

| Item | ID | Reason | Owner | Trigger to unblock |
|------|----|--------|-------|--------------------|
| Budget control configuration | D-WP02-07 | DEC-OCA-02: `account_budget_oca` incompatible with this Odoo 17 build | G1/G2/G3 + OCA/Odoo resolution | G1/G2/G3 resolution decision (see DEC-OCA-02 Governance Review) |
| mis_builder KPI dashboard | D-WP02-08 | Client must confirm NADF KPI set before configuration | Business Sponsor (Aliyu / Lanasoft) | Written client sign-off on KPI set; then schedule configuration in a WP-02 amendment or WP-05 pre-UAT |
| CoA client sign-off record | D-WP02-02 | CSV exported; client review not yet formally received | Business Sponsor | Client countersigns `csv_templates/nadf_coa_revalidated_20260625.csv` or provides written confirmation of acceptance |
| Analytic plan rename | DEC-WP02-002 | "Projects" plan to be renamed "NADF Departments" | Client confirmation at UAT prep | Client confirms during WP-05 UAT preparation |
| WHT/VAT rule amendment | D-WP02-11 | No changes required at this time; client must confirm before any amendment | Client | Client formal instruction before any tax account change |

---

## 4. Open Issues

| Issue ID | Description | Priority | Resolution path |
|---------|-------------|---------|----------------|
| ISS-WP02-01 | `account_budget_oca` blocked — budget module not operational | High | DEC-OCA-02 Governance Review (`docs/governance/DEC_OCA_02_GOVERNANCE_REVIEW.md`) — G1/G2/G3 must select Option A, B, C, or D |
| ISS-WP02-02 | CoA client sign-off pending — CSV delivered but not yet countersigned | Medium | Business Sponsor to review `csv_templates/nadf_coa_revalidated_20260625.csv` and confirm in writing |
| ISS-WP02-03 | Payment dual-auth is advisory only — no hard enforcement gate on `account.move` post | Medium | Phase 2 custom module (`nadf_payment_approval`); DEC-WP02-001 records this as a known limitation |
| ISS-WP02-04 | Analytic plan name ("Projects") does not reflect NADF terminology | Low | Rename to "NADF Departments" at client review session; no functional impact on Phase 1 |
| ISS-WP02-05 | mis_builder installed but not configured — dashboard capability dormant | Low | Client must provide KPI list; target WP-05 or post-Phase-1 configuration window |
| ISS-WP02-06 | Procurement and HR staff not yet assigned to Finance advisory dual-auth rules | Medium | WP-03 and WP-04 will assign Procurement and HR staff to their respective groups; base.automation rules reference group membership |

---

## 5. Risks (Residual)

| Risk ID | Risk | Likelihood | Impact | Status |
|---------|------|-----------|--------|--------|
| R-WP02-01 | Budget gap: lack of `account_budget_oca` may prevent client from validating budget-vs-actual in UAT | Med | High | Active — mitigated only by DEC-OCA-02 resolution; Phase 1 UAT plan must note this gap |
| R-WP02-02 | Payment dual-auth relies on advisory rules that can be bypassed by Finance Manager — no hard block | Med | Med | Accepted for Phase 1 (DEC-WP02-001); documented in RISK_REGISTER.md |
| R-WP02-03 | CoA unsigned by client — finance config not formally accepted | Low | Med | Business Sponsor prompted; CSV accessible; risk is governance-only |
| R-WP02-04 | WHT/VAT misconfiguration — 14 WHT / 8 VAT tax lines not validated by Finance with actual transactions | Low | Med | Validation deferred to first live WHT/VAT transactions post-UAT |
| R-WP02-05 | Test bill BILL/2026/06/0002 and its reversal remain in NADF DB | Low | Low | Records clearly named as test data; should be archived/deleted before UAT data population |

---

## 6. Decisions Raised

| Decision ID | Title | Status | Owner |
|------------|-------|--------|-------|
| DEC-WP02-001 | Payment dual-auth via base.automation (advisory) | Accepted (Phase 1) | A1 + G1 |
| DEC-WP02-002 | 5 analytic accounts as NADF department cost centres | Accepted | A1 |
| DEC-OCA-02 | `account_budget_oca` compatibility blocked — escalated | **Open — G1/G2/G3 resolution required** | G1/G2/G3 |

---

## 7. G1/G2/G3 Reviewer Findings

### G1 — Architecture & Odoo Governance

**Finding G1-WP02-01:** CoA structure is sound. 319 NADF 8-digit accounts correctly typed; 71 CE legacy accounts deprecated without deletion. Analytic account plan structure (5 cost centres) is appropriately lightweight for Phase 1 and does not require OCA analytic extension at this stage.

**Finding G1-WP02-02:** Payment dual-auth implementation via `base.automation` is architecturally acceptable as an interim measure. The DEC-WP02-001 record correctly characterises the limitation and the Phase 2 remediation path. G1 confirms no core Odoo modification was made.

**Finding G1-WP02-03:** `account_budget_oca` incompatibility is a genuine OCA module defect — the field `theoritical_amount` was removed from `account.analytic.account` in the Odoo 17 analytic account restructuring. This is not a configuration error; it requires an OCA patch or an alternative capability path. G1 refers the decision to DEC-OCA-02 Governance Review.

**G1 verdict:** WP-02 Architecture gate — **PASS (conditional on DEC-OCA-02 resolution)**

### G2 — Quality & Documentation Governance

**Finding G2-WP02-01:** All 9 delivered items have evidence recorded in `IMPLEMENTATION_HISTORY.md`. The blocked and deferred items are documented with clear resolution paths. `DECISION_LOG.md` carries DEC-WP02-001 and DEC-WP02-002. `CHANGELOG.md` entry is present.

**Finding G2-WP02-02:** The CoA CSV (`csv_templates/nadf_coa_revalidated_20260625.csv`) is present and correctly named. Client review is the only outstanding quality gate for this deliverable. G2 accepts the evidence as sufficient for phase documentation; client countersignature is a UAT pre-requisite, not a WP-02 blocker.

**Finding G2-WP02-03:** Test data (BILL/2026/06/0002 and its reversal) should be documented for cleanup before UAT data population. G2 recommends adding a cleanup task to WP-05 UAT preparation.

**G2 verdict:** WP-02 Quality gate — **PASS (conditional: cleanup task flagged for WP-05)**

### G3 — Security & Change Governance

**Finding G3-WP02-01:** Finance user group assignments are correct. `finance.officer` and `head.finance` are in the right groups (Finance Officer; Finance Manager + CFO). No privilege escalation detected.

**Finding G3-WP02-02:** TOTP 2FA global policy (`required`) enacted in WP-01 covers Finance Officer, Finance Manager, CFO, Auditor, and CEO as required. WP-02 did not alter this. The 2FA posture is unchanged and correct.

**Finding G3-WP02-03:** Branch `feat/wp-02-finance-core` → PR #6 → merge to protected `main` — change governance discipline maintained. No direct push to `main` detected.

**Finding G3-WP02-04:** Payment dual-auth gap (advisory only) is acknowledged. G3 accepts DEC-WP02-001 for Phase 1. The gap must be re-reviewed at Phase 2 planning to ensure the hard-block module is scoped.

**G3 verdict:** WP-02 Security & Change gate — **PASS**

---

## 8. Lessons Learned

| LL ID | Lesson | Category | Applicability |
|-------|--------|---------|--------------|
| LL-WP02-01 | The `account.move.reversal` wizard is the correct approach for programmatic bill reversal in Odoo 17 — calling `_reverse_moves()` directly requires a date parameter and can fail silently. Always use the wizard. | Technical | WP-03 and any future WP involving account.move operations |
| LL-WP02-02 | OCA module compatibility against a specific Odoo build version must be verified at the XML view level (field references), not just at the Python model level. The `account_budget_oca` failure was a view XML field reference to a removed model field — not caught by `--stop-after-init` syntax check alone. | Technical | All future OCA module installations |
| LL-WP02-03 | Payment state in Odoo 17 is on `account_move`, not `account_payment`. The old `state` column on `account_payment` was removed. Any query or automation touching payment state must use `account_move` with `move_type` and `payment_id` filters. | Technical | WP-03 procurement payment flows |
| LL-WP02-04 | When querying for analytic account confirmation, use `account.analytic.account` ORM (not raw `account_analytic_account` table) to avoid cached-plan discrepancies after schema changes. | Technical | WP-02 amendment; any future analytic configuration |
| LL-WP02-05 | Client-side blockers (KPI sign-off, CoA countersignature, WHT/VAT confirmation) should be raised and tracked before WP execution begins, not discovered during execution. Future WP planning must explicitly list required client inputs as pre-conditions in the Go/No-Go checklist. | Process | WP-03, WP-04, WP-ADM-01, WP-PC-01 Go/No-Go checklists |
| LL-WP02-06 | The analytic plan name ("Projects") is a CE default that persists from Phase 2 legacy configuration. Plan renaming is low-risk but must be flagged to the client at the planning stage, not discovered during verification. | Process | Configuration baseline review |

---

## 9. Exit Recommendation

**Exit gate verdict: CONDITIONAL PASS**

WP-02 Finance Core is conditionally complete. Nine of eleven acceptance criteria pass. Two items remain open:

1. **WP02-07 (Budget control)** — Blocked by DEC-OCA-02. Resolution is tracked in `docs/governance/DEC_OCA_02_GOVERNANCE_REVIEW.md`. This does not block WP-03, WP-04, WP-ADM-01, or WP-PC-01 from beginning. It does block Phase 1 UAT scenario coverage for budget-vs-actual reporting.

2. **WP02-08 (mis_builder dashboard)** — Deferred pending client KPI sign-off. No implementation action is possible until the client confirms the KPI set. Target: WP-05 UAT preparation window or a dedicated WP-02 amendment after client session.

**Recommendation: Proceed to WP-03, WP-04, WP-ADM-01, and WP-PC-01 under the CONDITIONAL PASS.** Phase 1 exit gate (full milestone close) requires DEC-OCA-02 resolution and WP02-08 completion before M1 can be marked DONE. Until then, M1 status is ACTIVE (conditional).

**Next governance action:** G1/G2/G3 must resolve DEC-OCA-02 (see `docs/governance/DEC_OCA_02_GOVERNANCE_REVIEW.md`).

---

*Prepared by A1 Master Orchestrator. G1/G2/G3 findings consolidated above. Authority: PEG-6 approval 2026-06-24 · Transfer Package v2.1.*
