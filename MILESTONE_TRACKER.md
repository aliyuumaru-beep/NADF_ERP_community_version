# MILESTONE_TRACKER.md
## NADF ERP Programme — Milestone Tracker (POD-NADF)

**Document type:** Mandatory Project Pod artifact (Agent OS — `04_PROJECT_POD_OPERATING_MODEL.md`, `24_PROJECT_POD_TEMPLATE.md`)
**Project Pod:** POD-NADF
**Authority:** `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md`
**Platform Profile:** `PLATFORM_PROFILE_ODOO17_COMMUNITY.md`
**Last updated:** 2026-06-29 (Wave C: DEC-OCA-02 resolved, WP02-07 PASS, backlog reconciled, M1-CPC CONDITIONAL PASS; WP-05 UAT preparation in progress)
**Maintained by:** A1 Software Factory Orchestrator (update on every milestone state change)

**Linked artifacts:** `PROJECT_STATE.md` · `planning/ROADMAP.md` · `planning/BACKLOG.md` · `planning/WORK_PACKAGES.md`

---

## 1. Milestone Model Mapping

This tracker overlays the **Agent OS Standard Milestone Model**
(`11_SOFTWARE_FACTORY_STANDARD_MILESTONE_MODEL.md`) onto the NADF **ROADMAP** phases
and the **legacy MVP build phases** recorded in Git history. The three numbering schemes
are distinct; this table is the single reconciliation point.

| Agent OS Milestone | ROADMAP Phase (`planning/ROADMAP.md`) | Legacy MVP build phase (Git history) | Status |
|--------------------|----------------------------------------|--------------------------------------|--------|
| **M0 — Initiation** | Phase 0 — Governance Remediation | Phase 0 — inspection/foundation docs (`48f1738`) | 🔄 **ACTIVE** |
| **M1 — Foundation** | Phase 1 — Foundation | Phases 1–8 — foundation, finance, procurement, HR, approvals, demo, CoA, assets/fleet/helpdesk (`4479b0e`…`05568b4`) | ⚠️ Delivered out-of-sequence; **not governance-ratified** |
| **M2 — Configuration** | Phase 1 (OCA install/config) + access-rights matrix | Partially covered within legacy Phases 2–8 | ⏳ Partial / pending ratification |
| **M3 — Development** | Phase 2 (custom-module specs) + Phase 3 (custom-module dev + remaining depts) | Phases 9–11 — `nadf_vendor_onboarding`, `nadf_facilities_management`, org-chart restructure | ⚠️ 2 modules built **ahead of spec/governance** |
| **M4 — Testing** | Phase 4 — Integrations + Phase 5 — Testing & Stabilisation | — | ⏳ Not started |
| **M5 — Deployment** | Phase 6 — Deployment | — | ⏳ Not started |
| **M6 — Closure** | Phase 7 — Template Extraction + go-live closure | — | ⏳ Not started |

### Out-of-sequence delivery note (authoritative)
The legacy MVP delivered **M1-level configuration and even M3-level custom modules before M0
governance was completed**. This is the central finding of `docs/GOVERNANCE_COMPLIANCE_AUDIT.md`
(Maturity Level 0). This tracker records that work **honestly but unratified**: the
configuration and modules exist, but **no milestone is marked closed**, because none has passed
the milestone gate (`07_MILESTONE_GATE_STANDARD.md`). M0 must complete before any downstream
milestone can be formally closed.

---

## 2. Current Milestone

| Field | Value |
|-------|-------|
| Active milestone | **M1 — Foundation** / ROADMAP Phase 1 |
| Milestone ID | M1 |
| Active Work Package | Wave C in progress: WP-05 UAT preparation (current); client sign-offs outstanding |
| Wave | Wave B COMPLETE (PR #12 merged `63879e9`). Wave C IN PROGRESS — DEC-OCA-02 resolved ✅; WP02-07 budget control PASS ✅; backlog reconciled ✅; M1-CPC CONDITIONAL PASS ✅; WP-05 UAT preparation ⏳ |
| Status | 🔄 **In progress** — WP-01/02/03/04/ADM-01/PC-01 all CONDITIONAL PASS (PRs #5/6/8/10/11/12 all merged); M1-CPC CONDITIONAL PASS 2026-06-29 |
| M0 predecessor | ✅ **CLOSED 2026-06-24** — PEG-6 approved (`DEC-PEG6-001`); Governance Gate 21/21 PASS; PR #1–#3 merged |
| Exit criteria | WP-01..04, WP-ADM-01, WP-PC-01 all PASS ✅ done; DEC-OCA-02 resolved ✅; WP-05 UAT preparation ⏳ in progress; client CoA sign-off ⏳; client B-02/B-03/WP02-08 ⏳ |

---

## 3. Milestone Register

| Milestone | Phase | Scope summary | Status | Governance ratified | Evidence |
|-----------|-------|---------------|--------|---------------------|----------|
| M0 Initiation | Phase 0 | Governance remediation, platform correction, repository activation | ✅ **CLOSED 2026-06-24** | Yes — Gate 21/21 PASS; PEG-6 approved | PRs #1–#4 merged; `docs/GOVERNANCE_GATE_REPORT.md`; `DEC-PEG6-001` |
| M1 Foundation | Phase 1 | CE core config ratified: Finance (WP-02), Procurement (WP-03 in progress), HR (WP-04), Admin (WP-ADM-01), PCU (WP-PC-01) | 🔄 **ACTIVE** | Partial — WP-01/02 CONDITIONAL PASS | PRs #5–#6; `docs/governance/WP_02_EXIT_GATE_REPORT.md` |
| M2 Configuration | Phase 1 | OCA modules extended config; access-rights matrix finalised; approval workflows hardened | ⏳ Not started | — | — |
| M3 Development | Phase 2–3 | Custom-module specs + development; remaining-department builds | ⚠️ 2 modules built ahead of spec (recovered M-C) | No | `nadf_vendor_onboarding` (12/12); `nadf_facilities_management` (33/33) — both unratified |
| M4 Testing | Phase 4–5 | Integration tests + full UAT | ⏳ Not started | — | — |
| M5 Deployment | Phase 6 | Production cutover + go-live | ⏳ Not started | — | — |
| M6 Closure | Phase 7 | Template extraction + closure | ⏳ Not started | — | — |

---

## 4. Completed Milestones (formally closed under governance)

| Milestone | Closed date | Closing evidence |
|-----------|------------|-----------------|
| **M0 — Initiation** | 2026-06-24 | PEG-6 approved (`DEC-PEG6-001`); Governance Gate 21/21 PASS; all M0 PRs (#1–#4) merged to protected `main`; backup + restore drill PASS; CI active |

---

## 5. Milestone Closure Rule

Per `07_MILESTONE_GATE_STANDARD.md`, a milestone may be marked **closed** in this tracker only when **all** of the following hold:
1. All its Work Packages are closed (see `planning/WORK_PACKAGES.md`).
2. Governance reviews G1 (Architecture & Odoo), G2 (Quality & Documentation), G3 (Security & Change) have passed.
3. `PROJECT_STATE.md` is updated to reflect closure.
4. Documentation (DECISION_LOG / IMPLEMENTATION_HISTORY / CHANGELOG / MODULE_REGISTRY as applicable) is complete.
5. For client-production milestones (M5), human sponsor approval is recorded per `03_ESCALATION_POLICY.md` / `02_AUTHORITY_MATRIX.md`.

Until then, downstream work is tracked as **"built / unratified,"** never as **"closed."**

---

## 6. Change Log (this file)

| Date | Change | By |
|------|--------|-----|
| 2026-06-21 | File created during Migration Sequence M-B; triple milestone mapping established; legacy build recorded as built-but-unratified | A1 Orchestrator |
| 2026-06-22 | **M-C executed**: both custom modules recovered; backup + restore drill PASS; `main` pushed + protected; Gates A/D/E PASS; RISK_REGISTER + 4 DEC entries added. | A1 Orchestrator |
| 2026-06-23 | **M-D executed**: closure-tier docs authored; CI added; Governance Gate 21/21 PASS. Open: fold PR merge + PEG-6. | A1 Orchestrator |
| 2026-06-24 | **M0 CLOSED**: PEG-6 approved (DEC-PEG6-001); PR #4 merged; Phase 1 activated. M1 Foundation active. | A1 Orchestrator |
| 2026-06-25 | **WP-01 CONDITIONAL PASS** (PR #5 merged `93551ba`): 4/5 OCA installed; 22 user groups; TOTP global required. **WP-02 CONDITIONAL PASS** (PR #6 merged `e58e15c`): CoA validated; bill workflow; analytic accounts; 8 staff assigned. DEC-OCA-02 open (account_budget_oca). WP-03 Go/No-Go PASS — execution authorised on branch `feat/wp-03-procurement-core`. PR #7 open (governance docs). | A1 Orchestrator |
| 2026-06-25 | **WP-03 CONDITIONAL PASS** (PR #8 merged `be7ed8b`): compliance field; purchase_request workflow; Call for Tender; goods receipt; mail.thread. WP03-07 BLOCKED (B-02/B-03). Wave A Session 1 CLOSED. | A1 Orchestrator |
| 2026-06-26 | **WP-04 CONDITIONAL PASS** (PR #10 merged `5e3861e`): hr_recruitment 105 modules; manager hierarchy 8 corrections; leave approvals 4 types→both; recruitment 5-stage; x_employment_state + CEO automations; mail.thread PASS; HR groups populated. WP04-08 DEFERRED (B-WP04-02). Wave A Session 2 CLOSED. | A1 Orchestrator |
| 2026-06-26 | **Wave A CLOSED** — WAVE_A_COMPLETION_REPORT.md produced. M1 NOT ACHIEVED (WP-ADM-01 + WP-PC-01 + WP-05 + client sign-offs outstanding). Wave B AUTHORIZED. | A1 Orchestrator |
| 2026-06-26 | **WP-ADM-01 CONDITIONAL PASS** (Wave B Session 3, PR #11 merged `6f7f4bb`): fleet register 5 vehicles; asset register 61 assets / 3 validated; helpdesk_mgmt 5 categories + team; mail.thread PASS; Admin groups 3/5 populated. DEC-ADM01-001/002/003. | A1 Orchestrator |
| 2026-06-26 | **WP-PC-01 CONDITIONAL PASS** (Wave B Session 4, PR #12 pending): 5 PCU stages ✅; NADF Programme project id=2 ✅; NADF Phase 1 id=3 ✅; milestone id=1 is_reached=True ✅; Director ACL id=1062 ✅; mail.thread ✅. DEC-PC01-001/002. **Wave B COMPLETE.** Wave C next: DEC-OCA-02 + WP-05 UAT. | A1 Orchestrator |
| 2026-06-29 | **PR #12 merged** `63879e9` (Wave B COMPLETE). **Wave C executed:** Pre-work backup PASS; DEC-OCA-02 resolved (Option A — drill exit 0; NADF install 105→106 modules); WP02-07 budget control PASS (3 positions; FY2026 Budget ₦107.3B confirmed); BACKLOG.md reconciled (44 items updated); GAR v1.4 (33 decisions; ESC-OCA-02 closed). **M1-CPC CONDITIONAL PASS** (G1/G2/G3 all PASS; all 6 WPs done; gaps are client/Phase 2). Wave C PR pending. | A1 Orchestrator |
