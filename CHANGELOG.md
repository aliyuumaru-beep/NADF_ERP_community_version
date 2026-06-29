# Changelog

All notable changes to the NADF ERP deployment (`nadf_erp`, Layer 4) are recorded here.
Format follows the Software Factory Release & Git Governance Standard (`14`); commit types: `feat`, `fix`, `governance`, `docs`, `ops`, `chore`. Dates are absolute.

## [Unreleased]

### AOP-015 — Governance Approval Register (2026-06-26)
- **governance:** `docs/governance/GOVERNANCE_APPROVAL_REGISTER.md` (GAR-NADF-001 v1.0) created — 25 decisions, 7 departments, 3 open escalations, 9 AOP-013 authority entries. Backward-populated from all existing NADF decisions. Validation: 5/5 checks PASS.
- **governance:** `docs/governance/GOVERNANCE_APPROVAL_REGISTER_V1_VALIDATION.md` created — all checks PASS.
- **governance:** Software Factory template `software-factory-governance/templates/GOVERNANCE_APPROVAL_REGISTER_TEMPLATE.md` created (AOP-015 standard).
- **governance:** SF `GOVERNANCE_STANDARD.md`, `AI_ONBOARDING_STANDARD.md`, `PROJECT_CONTINUITY_BRIEFING_TEMPLATE.md`, `PEF_WORK_PACKAGE_TEMPLATE.md` updated per AOP-015.
- **governance:** `software-factory-governance/DECISION_LOG.md` DEC-018 (AOP-015) logged.

### WP-ADM-01 — Administration Core executed (2026-06-26)
- **feat(admin):** Fleet register: 5 Toyota vehicles state=Registered; model years set (2019–2021); Fuel Refueling service type created; 5 odometer readings + fuel service log entries per vehicle — AC-ADM01-02 PASS.
- **feat(admin):** Asset register: 5 categories confirmed with GL accounts + journals; 61 assets in DB; 3 assets validated (state→open, depreciation lines active: Projector ₦700K/5m, Sofa ₦1M/5m, A/C ₦52.6M/5m) — AC-ADM01-03 PASS.
- **feat(admin):** helpdesk_mgmt configured: 5 ticket categories (Hardware, Software, Network, Access/Identity, Service Outage); "NADF ICT Helpdesk" team (lead=director.cs); test ticket id=1 created→resolved (Done), 3 mail.thread messages — AC-ADM01-05 PASS.
- **feat(security):** Administration user groups: IT Manager (id=111) + Fleet Manager (id=108) + Asset Manager (id=109) → director.cs interim; Driver (107) + IT Officer (110) PENDING B-WP04-01.
- **governance:** mail.thread confirmed: fleet.vehicle (4 msgs) ✅ account.asset.asset (2 msgs) ✅ helpdesk.ticket (3 msgs) ✅ — AC-14 PASS.
- **governance:** D-ADM01-07 legacy ICT helpdesk documented: project.project id=1, 6 stages, 10 tags, 77 tasks (70 closed) — superseded by helpdesk_mgmt.
- **governance:** DEC-ADM01-001: OCA helpdesk_mgmt 17.0.1.10.4 has no SLA model — priority + stage timestamps as proxy.
- **governance(deferred):** DEC-ADM01-002: Motor Vehicles category GL accounts incorrect (Earth Moving Equipment mapping) — deferred to Finance review.
- **governance(deferred):** AC-ADM01-01 fleet plates/drivers — PENDING R-ADM01-03 (plates) + B-WP04-01 (drivers).
- **ops:** GOVERNANCE_APPROVAL_REGISTER.md Administration section updated: 3 DEC-ADM01 entries added.

### WP-04 — HR Core executed (2026-06-26)
- **feat(hr):** `hr_recruitment` 17.0.0.1 installed (CE native); 105 modules total — DEC-WP04-001.
- **feat(hr):** Manager hierarchy (`parent_id`) set on 24 employees for 4-level NADF org structure (ES → Director → Manager → Officer). 8 corrections committed — DEC-WP04-004.
- **feat(hr):** Leave type approval workflows corrected to two-level (`both`): Annual Leave, Casual Leave, Sick Leave, Compensatory Days. Statutory leave types retain `hr` — DEC-WP04-003.
- **feat(hr):** Recruitment pipeline configured: Vacancy Posted → Shortlisted → Interview → Offer → Appointment (hired_stage=True). Odoo defaults folded — DEC-WP04-001.
- **feat(hr):** `x_employment_state` selection field (id=11644) on `hr.employee`; 24 employees initialised to `employed` — DEC-WP04-002.
- **feat(hr):** 2 `base.automation` CEO activity rules: `pending_appointment` and `pending_separation` → To-Do activity on Executive Secretary — DEC-WP04-002.
- **feat(security):** NADF HR groups populated: Employee (8 users), Line Manager (5 users), HR Officer (1), HR Manager (1), CEO (1). Time Off Officer + Responsible groups wired for two-level approval.
- **governance:** mail.thread verified on `hr.employee`, `hr.leave`, `hr.applicant` — AC-14 PASS.
- **governance(deferred):** WP04-08 company RC/TIN — client must provide registration number (B-WP04-02).
- **governance(deferred):** 6 Admin-dept employees — dept and reporting line pending client confirmation (B-WP04-01).
- **governance(deferred):** Duplicate leave type deduplication (Paid Time Off/Annual Leave, Sick Time Off/Sick Leave) deferred to WP-05 UAT pending client guidance.

### WP-03 — Procurement Core executed (2026-06-25)
- **feat(procurement):** `x_compliance_status` selection field created on `res.partner` (compliant/non_compliant/pending); 4 vendors tagged — DEC-WP03-001.
- **feat(procurement):** `purchase_request` workflow configured: `procurement.officer` → PR User; `head.procurement` → PR Manager. Full draft→to_approve→approved cycle validated.
- **feat(procurement):** `purchase_requisition` "Call for Tender" type created (exclusive=exclusive, qty_copy=copy); full tender → 2 RFQs → award → PO confirmed → loser cancelled → requisition closed — validated.
- **feat(procurement):** Goods receipt validated: PO P00011 → NADF/IN/00004 (5× HP Toner, stock.move state=done).
- **governance:** OCA `contract` fit-gap analysis: RACI requirement unmet; deferred to Phase 2/3 (`nadf_legal_contract` spec required) — DEC-CONTRACT-001.
- **governance:** mail.thread audit confirmed on `purchase.request` (2 msgs) and `purchase.order` (5 msgs) — AC-14 PASS.
- **governance(blocked):** WP03-07 multi-level approval chain — ₦500K threshold UNCHANGED; B-02/B-03 client confirmation outstanding.

### WP-02 — Finance Core re-validated (2026-06-25)
- **governance:** CoA re-validated: 319 NADF 8-digit accounts active, 71 CE legacy deprecated. Exported to `csv_templates/nadf_coa_revalidated_20260625.csv`.
- **feat(security):** Finance users assigned — `finance.officer` → Finance Officer; `head.finance` → Finance Manager + CFO.
- **governance:** Vendor bill workflow validated (draft → posted → reversed) — BILL/2026/06/0002 test.
- **governance:** Payment dual-auth: advisory control via 4 legacy base.automation rules confirmed active — DEC-WP02-001.
- **governance:** 5 analytic accounts (CC-ADM..CC-PRO) confirmed aligned to department cost-centre structure — DEC-WP02-002.
- **governance:** Financial reports (CE native, 5 account.report records), tax accounts WHT/VAT confirmed.
- **governance(blocked):** WP02-07 budget control — pending DEC-OCA-02 resolution.
- **governance(deferred):** WP02-08 mis_builder dashboard — pending client KPI sign-off.

### WP-01 — Foundation Hardening executed (2026-06-25)
- **ops:** OCA addons directory established at `/Users/mac/oca_addons`; `nadf.conf` `addons_path` updated.
- **feat(oca):** `mis_builder` 17.0.1.5.0 installed (OCA/mis-builder@17.0); deps `report_xlsx` 17.0.1.0.2 + `date_range` 17.0.1.2.1 + CE `board` — DEC-OCA-01.
- **feat(oca):** `purchase_request` 17.0.2.3.4 installed (OCA/purchase-workflow@17.0) — DEC-OCA-03.
- **feat(oca):** `helpdesk_mgmt` 17.0.1.10.4 installed (OCA/helpdesk@17.0) — DEC-OCA-04.
- **governance(oca):** `purchase_requisition` confirmed CE native 17.0.0.1 (pre-installed) — DEC-OCA-05.
- **governance(blocked):** `account_budget_oca` NOT installed — field `theoritical_amount` compatibility error; escalated to G1/G2/G3 — DEC-OCA-02. WP02-07 budget task blocked.
- **feat(security):** 22 Phase 1 user groups created (Finance×4, Procurement×4, HR×5, Administration×5, Project Coordination×4).
- **feat(security):** TOTP 2FA policy set to `required` globally; `auth_totp.policy` in `ir.config_parameter` — DEC-2FA-002.
- **governance:** `MODULE_REGISTRY.md` updated with all OCA installs (D-WP01-11). `DECISION_LOG.md` updated (DEC-OCA-01..05, DEC-2FA-002).
- **ops:** Registry exit 0, 100 modules loaded, no ERROR/CRITICAL lines for Phase 1 modules — AC-WP01-06 PASS. Odoo restarted PID 54258.

### Phase 1 activation — PEG-6 approved (2026-06-24)
- **governance:** PEG-6 approved by Business Sponsor (Aliyu / Lanasoft Technologies); `DEC-PEG6-001` logged. M0 formally closed.
- **ops:** Live Odoo service restarted (PID 51025) on corrected `addons_path`; `nadf_vendor_onboarding` and `nadf_facilities_management` confirmed discoverable (exit 0).
- **docs:** Phase 1 planning documents prepared — `docs/product/PHASE_1_PRODUCT_CAPABILITY_MAP.md`, `docs/product/PHASE_1_ROADMAP.md`, `docs/product/PHASE_1_BACKLOG.md`, `docs/work_packages/WP_01_FOUNDATION_HARDENING.md`.
- **docs:** `docs/governance/PEG_6_PRODUCT_AUTHORIZATION_PACKAGE.md` §15 approval record added; business authorization updated to APPROVED.
- **scope:** Phase 1 scope frozen at Transfer Package v2.1. No coding, no module install, no functional config change in this activation step. Governance layer (G1/G2/G3) activates before delivery layer (D1–D4).

### PEG-6 — Product Authorization package prepared (2026-06-24)
- **docs:** Added `docs/governance/PEG_6_PRODUCT_AUTHORIZATION_PACKAGE.md` — 14-section Product Authorization Package (baseline, legacy ratification, Phase-1 scope, risks, governance/repository/backup/platform status, WP-01..05, governance reviews, agent activation, Go/No-Go, approval statement). Recommendation: **CONDITIONAL GO** pending PEG-6 approval + sponsor sign-off + single-session + Odoo restart + scope freeze.
- **docs:** Updated `docs/NEXT_ACTION.md` to point to PEG-6 review/approval as the next action; `IMPLEMENTATION_HISTORY.md` governance-only entry added.
- **scope:** No ERP development authorized; no functional Odoo module or configuration changed. Development remains blocked pending PEG-6 approval.

### M-D — Closure-tier documentation & CI (2026-06-23)
- **docs:** Added mandatory repository files — `README.md`, `CLAUDE.md`, `CHANGELOG.md`, `IMPLEMENTATION_HISTORY.md`, `MODULE_REGISTRY.md`, root `ROADMAP.md` summary.
- **docs:** Added `docs/PRODUCT_STATE_INDEX.md` with session start/end rules (BL-GOV-09) — closes Gate C7.
- **ci:** Added `.github/workflows/ci.yml` (manifest parse + `py_compile` + XML well-formedness) and PR template — closes Gate B.
- **governance:** Governance Activation Gate re-run to full **21/21 PASS**; PR opened to fold `phase/0-governance` → `main`.

### M-C incident stabilization (2026-06-22)
- **fix(stabilization):** `nadf.conf` `addons_path` now includes `nadf_erp/custom_addons` so the relocated modules are discoverable; verified `odoo-bin --stop-after-init` loads 94 modules, exit 0 (`f53304c`).

### M-C — Governance certification & recovery (2026-06-22)
- **fix(recovery):** Recovered `nadf_vendor_onboarding` from the FamOil untracked tree into `custom_addons/` (integrity 12/12, MR-01) (`a9738b4`).
- **fix(recovery):** Relocated `nadf_facilities_management` from `famoil-erp@55c1787` into `custom_addons/` (integrity 33/33, MR-02) (`4ccb306`).
- **governance:** Added `RISK_REGISTER.md`; logged `DEC-PLATFORM-001`, `DEC-RECOVERY-001/002`, `DEC-BACKUP-001` (`c21cfd8`).
- **ops:** Added backup strategy + tooling; first DB+filestore backup and restore drill **PASS** (MR-05) (`ad43fa4`).
- **governance:** Governance gate baseline report 16/21; `main` pushed and branch-protected (`b52d15d`, `a63cf99`).
- **docs:** `docs/MC_RECOVERY_INTEGRITY.md` — SHA-256 recovery integrity evidence.

### M-B — Bootstrap-enable (2026-06-21)
- **governance:** Stood up `PROJECT_STATE.md`, `MILESTONE_TRACKER.md`; reconciled `planning/`; quarantined stale scaffold (`16c8cf7`, `d15b30d`).

## Legacy MVP build (Phases 0–10, 2026-06-02 → 2026-06-13) — pre-governance, unratified
- Phase 0–8 Odoo 17 CE configuration (Finance, Procurement, HR, Administration, CoA, assets/fleet/helpdesk) — commits `48f1738`…`05568b4`.
- Phase 9 `nadf_vendor_onboarding`; Phase 10 `nadf_facilities_management` (recovered under M-C).
- Status: **built / unratified** — delivered out of governance sequence; no milestone closed.

---
*No release tag yet. First tag will be `v1.0-go-live` at Phase 6 deployment (see `planning/ROADMAP.md`).*
