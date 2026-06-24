# PEG-6 Product Authorization Package — NADF ERP Programme

**Document type:** Governance — Product Engineering Gate 6 (Product Authorization)
**Project Pod:** POD-NADF · **Layer:** Layer 4 — Client Deployment
**Repository:** `NADF_ERP_community_version`
**Prepared by:** A1 Master Orchestrator (Software Factory Autonomous Agent Team)
**Date prepared:** 2026-06-24
**Authority:** Software Factory Governance · PEF v1.1 · Agent OS v1 · `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md`
**Bound platform profile:** `PLATFORM_PROFILE_ODOO17_COMMUNITY.md` (Agent OS platform-profiles/23)
**Decision sought:** Authorization to commence **Phase 1 — Foundation** ERP delivery under governance

> **NO ERP DEVELOPMENT IS AUTHORIZED YET.**
> **PEG-6 approval is required before Phase 1 development begins.**
> This package was prepared in authorization-preparation mode only: no functional Odoo module
> was modified, no business feature created, no functional configuration changed.

---

## Readiness Summary (as confirmed at preparation)

| Readiness dimension | Status |
|---------------------|--------|
| BPOGS (business process baseline) | ✅ Complete (requirements-source history only) |
| PEF v1.1 | ✅ Approved |
| Agent OS v1 | ✅ Complete |
| Migration M-B (bootstrap-enable) | ✅ Complete |
| Migration M-C (certification & recovery) | ✅ Complete |
| Migration M-D (closure-tier docs + CI) | ✅ Complete |
| Governance Activation Gate | ✅ **21/21 PASS** |
| Technical readiness | ✅ PASS |
| Governance readiness | ✅ PASS |
| Repository readiness | ✅ PASS |
| **Business authorization** | ⏳ **PENDING — this gate** |

---

## 1. Current Product Baseline

| Field | Value |
|-------|-------|
| Programme | NADF Business Process Optimisation & Governance System (BPOGS) — ERP Implementation |
| Client | National Agricultural Development Fund (NADF) |
| Consultant | Lanasoft Technologies |
| Implementation agent | Software Factory Autonomous Agent Team (POD-NADF) |
| Platform | Odoo 17 **Community Edition** only — DB `NADF`, port `8071` |
| Programme reference | Reference Implementation #1 — Public Sector ERP Template |
| Bound product authority | NADF Full Product Transfer Package **v2.1** (v2.0 superseded) |

**Full product scope (v2.1):** 12 departments · ~61 business processes · **14 capability areas (CA-01…CA-14)** · **6 required custom modules** · CE core + vetted OCA · zero Enterprise features.

**Governance milestone:** **M0 — Initiation** (ROADMAP Phase 0, `M-PLATFORM-CORRECTION`). Migration sub-sequences M-B, M-C, M-D complete; Governance Activation Gate 21/21 PASS; PR #1 folded the governance baseline into `main`. The **sole remaining M0-closure item is this PEG-6 signed approval.**

**Programme completion vs full v2.1 scope:** ~20% — legacy MVP covers the foundation of ~4 departments plus 2 custom modules, all **built but not governance-ratified**.

**Baseline integrity statement:** No milestone is yet formally closed. All delivered build work is recorded honestly as **"built / unratified."**

---

## 2. Legacy Build Ratification Summary

The legacy MVP delivered substantial Odoo 17 CE configuration **out of governance sequence** (M1/M3-level work before M0 completed). `docs/GOVERNANCE_COMPLIANCE_AUDIT.md` (2026-06-13) graded it **Maturity Level 0 (Ad Hoc)**. M-C/M-D remediated the governance, repository, and recovery gaps; **functional ratification of the legacy build itself remains pending and is scheduled inside Phase 1.**

| Legacy asset | What exists | Status | Ratification route |
|--------------|-------------|--------|--------------------|
| Finance config (CoA 319 accts, vendor bills, payments, fiscal year) | Built (legacy Phases 0–7) | **Unratified** | WP-02 re-validation |
| Procurement config (purchase pipeline, `base.automation` approvals) | Built (legacy Phases 3–6) | **Unratified** | WP-03; approval chain blocked on B-02/B-03 |
| HR config (employees, 4-level org, leave) | Built (legacy Phases 4–8) | **Unratified** | WP-04 re-validation |
| Administration (assets, fleet ×5, ICT helpdesk via `project`) | Built (legacy Phase 8) | **Unratified** | re-validation under Phase 1 (Admin foundation) |
| `nadf_vendor_onboarding` (custom) | Recovered to `custom_addons/` (`a9738b4`); integrity 12/12 | **Recovered, unratified** | Re-validate; retrospective spec required |
| `nadf_facilities_management` (custom) | Recovered to `custom_addons/` (`4ccb306`); integrity 33/33; removed from `famoil-erp` (`9a16f74`) | **Recovered, unratified** | Re-validate; retrospective spec required |

**Incidents closed by M-C:** MR-01 data-loss (`nadf_vendor_onboarding` orphaned — recovered, `DEC-RECOVERY-001`); MR-02 layering breach (`nadf_facilities_management` in `famoil-erp` — relocated, `DEC-RECOVERY-002`, gitignore guard). **Module source of truth is now `nadf_erp/custom_addons/`.**

**Ratification ruling (D1/D3/G1):** The legacy build is accepted as a **baseline to be re-validated**, not as completed Phase 1. No legacy artifact may be marked "Done" until re-tested against its Work Package acceptance criteria under governance. The two recovered custom modules predate the PEF "no spec, no code" rule and require **retrospective design specs** before ratification.

---

## 3. Scope Authorized for Phase 1

Phase 1 — Foundation is the **only** scope this package seeks to authorize, bounded to CE-native configuration and vetted OCA installation for the foundation capability areas plus system-wide security.

| Capability | Department | Phase-1 Work Package |
|-----------|-----------|----------------------|
| CA-01 Financial Management | Finance | WP-02 |
| CA-02 Procurement Management | Procurement | WP-03 (approval chain deferred — blocked) |
| CA-03 Human Resource Management | HR | WP-04 (payroll excluded) |
| CA-04 Administration & Facilities | Administration | within Phase-1 foundation (facility module excluded) |
| CA-05 Project & Programme Management | Project Coordination | within Phase-1 foundation |
| CA-14 Security & Access Control | All (Phase-1 groups) | WP-01 + per-WP groups + TOTP 2FA |
| OCA enablement | Platform | WP-01 |

**Authorized OCA modules (Phase 1, compatibility verification required first):** `mis_builder`, `account_budget_oca`, `purchase_request`, `purchase_requisition`, `helpdesk_mgmt` — each Odoo-17-CE-verified, version-pinned, and logged in `docs/DECISION_LOG.md` before install.

Phase 1 explicitly includes **re-validation and governance ratification of the legacy Finance/Procurement/HR/Administration configuration** (see §2).

---

## 4. Scope Not Yet Authorized

Out of scope for this authorization; each requires its own gate / input:

- **All six custom modules — specification AND development** (`nadf_payroll_ng`, `nadf_vendor_compliance`, `nadf_facility`, `nadf_legal_contract`, `nadf_investment`, `nadf_me_indicators`). "No spec, no code."
- **Retrospective spec + ratification of the two recovered legacy custom modules** (`nadf_vendor_onboarding`, `nadf_facilities_management`).
- **The 7 remaining department builds** (TO-BE-gated, B-04A…B-04G): Legal (CA-06), Strategy & Planning (CA-07), Communications (CA-08), Sustainable Agriculture (CA-09), Investment (CA-10), M&E (CA-11), Executive Management (CA-12).
- **Procurement multi-level approval chain** — blocked on client confirmation of RACI step 1.19 (B-02) and approval thresholds (B-03).
- **Cross-department integration, UAT execution, production deployment, template extraction** (Phases 4–7).
- **Anything Enterprise** — `web_studio`, `sign`, `documents`, `documents_spreadsheet`, `knowledge`, EE `hr_payroll`, EE `helpdesk`, `industry_fsm`, `account_accountant`: permanently prohibited.
- **Out-of-remit work** (PRODUCT_SCOPE §9): swimlane/process-workbook production (Claude Desktop — **requirements-source history only**), infrastructure/hardware, master-data entry, training delivery, third-party integrations.

---

## 5. Open Risks

| ID | Risk | L | I | Status / Mitigation |
|----|------|---|---|---------------------|
| R-01 | Enterprise modules present | — | — | **CLOSED** — 0 prohibited modules; `DEC-PLATFORM-001` |
| R-02 | 7 departments lack TO-BE — sequencing gap | Med | High | Builds triggered only on TO-BE delivery (B-04A…G) |
| R-03 | OCA modules not yet Odoo-17-CE-verified | Med | Med | Compatibility check mandatory in WP-01 before install |
| R-04 | Nigerian payroll statutory rules need local legal input | High | High | `nadf_payroll_ng` spec gated on adviser (E-01) |
| R-05 | `nadf_investment` large custom scope, no reference impl | Med | High | Spec + client BRQ session before code (E-03) |
| R-06 | UAT not started; go-live date unconfirmed | Med | High | Phase 5 gate not opened until Phase 4 complete |
| R-07 | Backup/CI not confirmed at start | — | — | **CLOSED** — backup + restore drill PASS; CI live |
| R-08 | PR not merged; M0 not closed | — | — | **CLOSED** — governance baseline folded into `main` |
| R-09 | Recovered custom modules carry no PEF design spec | Med | Med | Retrospective specs required before ratification |
| R-10 | `main` protection requires 0 approving reviews (docs assume 1) | Low | Med | **OPEN** — reconcile to require ≥1 non-author approval |
| R-11 | Concurrent Claude Code session detected during M-C stabilization | Med | High | **Single active session must be enforced** before Phase 1 (Go/No-Go condition c) |
| R-12 | Live Odoo instance not restarted after `addons_path` correction | Med | Med | **Graceful restart required** before Phase 1 (Go/No-Go condition d); next restart verified clean |

**Open escalations:** E-01 (payroll legal input → Aliyu/Lanasoft), E-02 (Procurement B-02/B-03 → NADF client), E-03 (Investment BRQ session → Aliyu/NADF). Phase 2/3 dependencies; do not block Phase 1 other than the procurement approval chain.

---

## 6. Governance Status

**Governance Activation Gate: ✅ 21/21 PASS** (`docs/GOVERNANCE_GATE_REPORT.md`).

| Gate | Domain | Status |
|------|--------|--------|
| A | Repository + branch protection | ✅ PASS |
| B | CI (`.github/workflows/ci.yml` + `scripts/ci_validate.py`) | ✅ PASS |
| C | Governance + Repository-Standard docs | ✅ PASS |
| D | Backup strategy + restore drill | ✅ PASS |
| E | Platform / coverage — 0 Enterprise modules | ✅ PASS |

**Mandatory Pod files (8/8 present):** `PROJECT_STATE.md`, `MILESTONE_TRACKER.md`, `planning/BACKLOG.md`, `docs/DECISION_LOG.md`, `RISK_REGISTER.md`, `CHANGELOG.md`, `IMPLEMENTATION_HISTORY.md`, `MODULE_REGISTRY.md`.
**Repository-Standard docs present:** `README.md`, `CLAUDE.md`, `ROADMAP.md`, `docs/PRODUCT_STATE_INDEX.md`, `docs/NEXT_ACTION.md`, `docs/GOVERNANCE_GATE_REPORT.md`.
**Scaffold quarantine upheld:** `docs/imports/…` zip is non-authoritative — never extracted/cited.

**M0 closure status:** sole remaining item = **PEG-6 signed Product Approval (§14).** M0 closes on signature.

---

## 7. Repository Status

| Field | Value (verified at preparation) |
|-------|----------------------------------|
| Repo path | `/Users/mac/nadf_erp` |
| Default branch | `main` @ `989b65f` — carries M-B/M-C/M-D governance baseline (gate 21/21) |
| GitHub remote | `github.com/aliyuumaru-beep/NADF_ERP_community_version` (pushed; `main` current) |
| Branch protection | `enforce_admins: true`; **required approving reviews: 0** (R-10 — recommend ≥1) |
| Working branch (this package) | `docs/peg-6-product-authorization` — PR required (no direct `main` push) |
| CI | `.github/workflows/ci.yml` + `scripts/ci_validate.py` |
| Custom addons (source of truth) | `custom_addons/nadf_vendor_onboarding`, `custom_addons/nadf_facilities_management` |
| Working-tree cleanliness at start | clean (no unrelated changes) |

---

## 8. Backup / Recovery Status

| Field | Value |
|-------|-------|
| Backup tooling | `scripts/backup_nadf.sh` / `scripts/restore_nadf.sh` |
| Strategy doc | `docs/BACKUP_STRATEGY.md` (daily schedule + restore procedure) |
| Backups on disk | `~/odoo_backups/nadf_20260622_114439`, `~/odoo_backups/nadf_20260622_113326` |
| Restore drill | ✅ **PASSED** (M-C, drill DB — live `NADF` never mutated; 94=94 modules, 40=40 partners) |
| Recovery integrity | `docs/MC_RECOVERY_INTEGRITY.md` — SHA-256 evidence; module integrity 12/12 + 33/33 |
| Decision record | `DEC-BACKUP-001` |

**Recoverability statement (G3/D3):** DB and both custom modules are backed up, version-controlled, pushed, and restore-verified. The programme is recoverable. *Operational:* take a fresh backup immediately before the first Phase-1 schema/data-mutating operation (CLAUDE.md rule).

---

## 9. Platform Status

| Field | Value |
|-------|-------|
| Current runtime | **Local Mac** (development) |
| Target platform | **Odoo 17 Community Edition** (DB `NADF`, port `8071`) |
| Long-term source of truth | **GitHub** (`NADF_ERP_community_version`) — authoritative across all infrastructure stages |
| Enterprise modules | **0 present** — `DEC-PLATFORM-001` |
| Approach order (bound profile) | Native CE → Configuration → OCA (vetted, pinned) → existing SF modules → Custom; core modification prohibited unless escalated + logged |
| Interpreter (Odoo deps) | `/Users/mac/odoo17/odoo/venv/bin/python` |
| Known platform gap | `wkhtmltopdf` not installed (PDF render) — affects only the unratified facilities module; not a Phase-1 blocker |
| Isolation | NADF layer isolated from FamOil and WamaCare; MR-02 cross-contamination closed |

**Future infrastructure progression (planning context only — not authorized work):**
- **Stage 1 — Local development** (current).
- **Stage 2 — Single VPS for Dev/Test.**
- **Stage 3 — Separate Production** environment.
- **Stage 4 — Dedicated physical infrastructure** only if justified by load, compliance, or sovereignty requirements.

GitHub remains the long-term source of truth at every stage; environments are deployment targets, not authority.

---

## 10. Recommended Phase 1 Work Packages

> All Phase-1 work packages are **gated behind PEG-6 approval and the §13 conditions.** None may begin until business authorization is granted.

### WP-01 — Foundation Hardening
- **Objective:** Establish the Phase-1 technical and access foundation — enforce single-session discipline, restart the live Odoo service onto the corrected `addons_path`, install and version-pin the five authorized OCA modules, and stand up the baseline security model (user groups + TOTP 2FA).
- **Deliverables:** Verified single live Odoo instance on corrected `nadf.conf`; five OCA modules installed, Odoo-17-CE-compatibility-verified, version-pinned, and logged in `docs/DECISION_LOG.md`; baseline security groups; 2FA enforced for Finance + Senior Management; fresh pre-work backup recorded.
- **Acceptance criteria:** OCA modules report `state='installed'`; each logged with version + source URL; 2FA active for required groups; `odoo-bin --stop-after-init` exit 0; backup timestamped within 24h of work start. (Supports AC-14.)
- **Governance review required:** **G1** (architecture/approach-order), **G3** (security + change discipline).

### WP-02 — Finance Core
- **Objective:** Re-validate and ratify the legacy Finance configuration under governance; confirm chart of accounts, vendor-bill workflow, dual-authorisation payments, native financial reports, and audit trail.
- **Deliverables:** CoA confirmed against NADF government structure (exported reference CSV); vendor-bill workflow verified; payment dual-authorisation tested with two user accounts; trial balance / P&L / balance sheet rendering; `mail.thread` audit verified on `account.move` / `account.payment`.
- **Acceptance criteria:** AC-01 (CoA, vendor bills, payments, native reporting) evidenced; dual-auth blocks unauthorised posting; audit trail present. Client review of CoA structure recorded.
- **Governance review required:** **G1**, **G2** (acceptance evidence + doc updates); client CoA review.

### WP-03 — Procurement Core
- **Objective:** Re-validate and ratify the legacy Procurement pipeline; configure vendor records with compliance status, structured requisitions, RFQ/tender workflow, and goods receipt. (Multi-level approval chain deferred — blocked on B-02/B-03.)
- **Deliverables:** Vendor compliance-status field on `res.partner`; `purchase_request` and `purchase_requisition` workflows active; goods-receipt/stock flow verified; `DEC-CONTRACT-001` (OCA `contract` fit decision) logged; `mail.thread` audit on `purchase.request` / `purchase.order`.
- **Acceptance criteria:** AC-02 (partial — pipeline through goods receipt); approval chain explicitly **excluded** from this WP's completion bar until B-02/B-03 resolved.
- **Governance review required:** **G1**, **G2**.

### WP-04 — HR Core
- **Objective:** Re-validate and ratify the legacy HR configuration; confirm employee records with the NADF 4-level org hierarchy, two-level leave approval, recruitment pipeline, and appointment/separation approval with CEO notification. (Payroll excluded — Phase 3.)
- **Deliverables:** Employee records on 4-level hierarchy; leave workflow (line manager → HR); recruitment pipeline stages; appointment/separation approval state with CEO activity; HR user groups; `mail.thread` audit on `hr.employee` / `hr.leave` / `hr.applicant`.
- **Acceptance criteria:** AC-03 (payroll excluded; performance management deferred); leave and recruitment flows verified. Client review of leave types + org hierarchy recorded.
- **Governance review required:** **G1**, **G2**; client review.

### WP-05 — UAT Preparation
- **Objective:** Prepare (not execute) the Phase-1 UAT scaffolding so that ratified foundation capabilities can be validated by NADF users — test plan skeleton, per-capability test cases, and defect-register template. No UAT execution under Phase 1 authorization.
- **Deliverables:** UAT test-plan skeleton mapping one case per Phase-1 acceptance criterion (AC-01..05, AC-14); defect-register template; UAT readiness checklist; documented entry/exit criteria.
- **Acceptance criteria:** Test plan covers every Phase-1 AC; defect register template present; readiness checklist agreed. (Preparation only; execution is Phase 5 / WP-UAT-01.)
- **Governance review required:** **G2** (quality/coverage), **G3** (access for UAT users).

---

## 11. Governance Reviews Required

Per the Milestone Closure Rule (`07_MILESTONE_GATE_STANDARD.md`), no Phase-1 milestone can be ratified without:

| Gate | Reviewer | Phase-1 review scope |
|------|----------|----------------------|
| **G1** | Architecture & Odoo Governance | CE-only approach order; OCA vetted/pinned; no core modification; layering intact |
| **G2** | Quality & Documentation Governance | Each WP acceptance criterion evidenced; DECISION_LOG / MODULE_REGISTRY / IMPLEMENTATION_HISTORY / CHANGELOG updated before PR |
| **G3** | Security & Change Governance | Access-rights matrix; 2FA enforced; `mail.thread` audit coverage; branch/PR discipline (incl. R-10 reconciliation); single-session enforcement; backup-before-mutation |

Per-change discipline: feature branch → conventional commit → PR → G-review → merge into protected `main`. No direct pushes to `main`.

---

## 12. Agent Activation Plan

**Governance layer activates FIRST. Delivery layer activates ONLY AFTER the governance layer is active and PEG-6 is approved.**

### Governance layer (activate first)
| Role | Mandate |
|------|---------|
| **G1 — Architecture & Odoo Governance** | Enforce CE-only approach order, OCA vetting, layering; gate WP-01..05 architecture |
| **G2 — Quality & Documentation Governance** | Enforce acceptance evidence and governance-doc currency before any PR merges |
| **G3 — Security & Change Governance** | Enforce access model, 2FA, change discipline, single-session, backup-before-mutation |

### Delivery layer (activate only after governance layer + PEG-6 approval)
| Role | Mandate |
|------|---------|
| **D1 — Functional Architect** | Translate v2.1 capability specs into Odoo config designs |
| **D2 — Solution Builder** | Execute WP-01..05 config; never mutate live DB for verification |
| **D3 — QA & Validation** | Re-validate legacy build; test each AC; restore-drill before mutations |
| **D4 — Knowledge & Documentation** | Keep DECISION_LOG / MODULE_REGISTRY / IMPLEMENTATION_HISTORY / CHANGELOG / PROJECT_STATE current |

**Activation constraint:** D-agents must not install/upgrade modules, change Odoo configuration, or create modules until the governance layer is active and PEG-6 is signed.

---

## 13. Go / No-Go Recommendation

**Recommendation: 🟡 CONDITIONAL GO** — authorize **Phase 1 — Foundation only**, effective **only after all of the following are satisfied:**

- **a.** PEG-6 approval is obtained (§14 signed).
- **b.** Business sponsor sign-off is obtained.
- **c.** A **single active Claude Code session** is enforced (a concurrent session was detected during M-C stabilization — see Warnings).
- **d.** The **live Odoo service is restarted** to pick up the corrected `nadf.conf` `addons_path` (not yet restarted — see Warnings).
- **e.** The **product scope baseline is frozen** at Transfer Package v2.1 (no scope drift into Phase 1).

**Bounded conditions carried into Phase 1:** procurement approval chain stays blocked (B-02/B-03); legacy build re-validated, not assumed; recovered custom modules require retrospective specs before ratification; branch protection reconciled to ≥1 non-author approval (R-10); no Phase 2/3 work under this authorization.

**No-Go applies if** any condition a–e is unmet, or the sponsor declines the foundation scope.

### Current known warnings
- ⚠️ **A second Claude Code session was detected during M-C stabilization** (it later self-terminated). Single-session discipline must be confirmed before Phase 1 (condition c; risk R-11).
- ⚠️ **The live Odoo service has not yet been restarted after the `addons_path` correction.** The running instance still holds the pre-fix in-memory path; a graceful restart is required before Phase 1 (condition d; risk R-12). The next restart is verified clean.

---

## 14. PEG-6 Approval Statement

> **PEG-6 — Product Authorization Decision (NADF ERP Programme)**
>
> I, as Business Sponsor for the NADF ERP Programme, having reviewed this PEG-6 Product Authorization Package (2026-06-24), confirm:
>
> 1. Governance Activation Gate **21/21 PASS**; platform is **Odoo 17 Community Edition with zero Enterprise modules**; repository protected, pushed, CI-enabled, backed up, restore-verified; governance baseline folded into `main`.
> 2. I acknowledge that **no ERP development is authorized until this statement is signed**, and that this signature is the **sole remaining item to close milestone M0**.
> 3. I authorize commencement of **Phase 1 — Foundation only** (WP-01 Foundation Hardening, WP-02 Finance Core, WP-03 Procurement Core, WP-04 HR Core, WP-05 UAT Preparation) — **CONDITIONAL** on: (a) this approval; (b) business sponsor sign-off; (c) single active Claude Code session enforced; (d) live Odoo service restarted onto the corrected `addons_path`; (e) product scope baseline frozen at Transfer Package v2.1.
> 4. I confirm that **no custom module specification or development, no remaining-department build, no Enterprise feature, and no scope change** is authorized by this decision.
> 5. I direct that all Phase-1 work proceed governance-layer-first (G1/G2/G3), with the delivery layer (D1–D4) activating only afterward, under the Milestone Closure Rule, with legacy build work re-validated — not assumed — before ratification.
>
> **Decision:** ☐ CONDITIONAL GO (Phase 1)  ☐ NO-GO  ☐ GO with amendments
>
> **Conditions cleared:** ☐ a PEG-6 ☐ b sponsor sign-off ☐ c single session ☐ d Odoo restart ☐ e scope frozen
>
> **Sponsor name:** ______________________  **Signature:** ______________________  **Date:** ____________
>
> **Conditions / amendments (if any):**
> _______________________________________________________________________________

---

*End of PEG-6 Product Authorization Package. Prepared in authorization-preparation mode; no ERP build, install, upgrade, functional configuration change, module creation, or business feature was performed. **Development remains blocked pending PEG-6 approval.***
