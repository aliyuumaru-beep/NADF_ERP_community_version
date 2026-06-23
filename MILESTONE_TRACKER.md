# MILESTONE_TRACKER.md
## NADF ERP Programme — Milestone Tracker (POD-NADF)

**Document type:** Mandatory Project Pod artifact (Agent OS — `04_PROJECT_POD_OPERATING_MODEL.md`, `24_PROJECT_POD_TEMPLATE.md`)
**Project Pod:** POD-NADF
**Authority:** `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md`
**Platform Profile:** `PLATFORM_PROFILE_ODOO17_COMMUNITY.md`
**Last updated:** 2026-06-21 (created during Migration Sequence M-B)
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
| Active milestone | **M0 — Initiation** / ROADMAP Phase 0 — Governance Remediation |
| Milestone ID | `M-PLATFORM-CORRECTION` |
| Active Work Package | `WP-GOV-01` (→ `BL-GOV-01`, `BL-GOV-02`) |
| Status | 🔄 In progress (M-B ✅; M-C ✅; **M-D ✅** — CI + closure-tier docs; Governance Gate **21/21 PASS**). Awaiting: `main`-fold PR merge + PEG-6 Product Approval to formally close M0. |
| Exit criteria | Zero Enterprise modules ✅; **Governance Gate 21/21 PASS** ✅; `DEC-PLATFORM-001` ✅; remote pushed + `main` protected ✅; backup + restore drill ✅; closure-tier docs + CI ✅. **Open:** PR merge to `main`; PEG-6 signed Product Approval. |

---

## 3. Milestone Register

| Milestone | Phase | Scope summary | Status | Governance ratified | Evidence |
|-----------|-------|---------------|--------|---------------------|----------|
| M0 Initiation | Phase 0 | Governance remediation, platform correction, repository activation | 🔄 Active | No | This tracker; `PROJECT_STATE.md`; `WP-GOV-01` |
| M1 Foundation | Phase 1 | CE core config: Finance, Procurement, HR, Administration foundation | ⚠️ Built, unratified | No | Git `48f1738`→`05568b4` |
| M2 Configuration | Phase 1 | OCA modules, access-rights matrix, approval workflows | ⏳ Partial | No | base.automation approvals (`ec2fc32`) |
| M3 Development | Phase 2–3 | Custom-module specs + development; remaining-department builds | ⚠️ 2 modules ahead of spec | No | `nadf_vendor_onboarding` (untracked); `nadf_facilities_management` (in `famoil-erp` `55c1787`) |
| M4 Testing | Phase 4–5 | Integration tests + full UAT | ⏳ Not started | — | — |
| M5 Deployment | Phase 6 | Production cutover + go-live | ⏳ Not started | — | — |
| M6 Closure | Phase 7 | Template extraction + closure | ⏳ Not started | — | — |

---

## 4. Completed Milestones (formally closed under governance)

**None.** No milestone has yet passed the milestone gate. Legacy build work (M1/M2 config,
M3 custom modules) is delivered but **awaiting governance ratification** under M0.

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
| 2026-06-22 | **M-C executed**: both custom modules recovered to NADF layer (integrity PASS 12/12 + 33/33); FamOil contamination removed; backup + restore drill PASS; `main` pushed + protected; Gates A/D/E PASS; `RISK_REGISTER` + 4 DEC entries added. M-C complete; M-D pending (CI + closure-tier docs). | A1 Orchestrator |
| 2026-06-23 | **M-D executed**: closure-tier docs authored (`README`, `CLAUDE.md`, `CHANGELOG`, `IMPLEMENTATION_HISTORY`, `MODULE_REGISTRY`, root `ROADMAP`, `docs/PRODUCT_STATE_INDEX.md`); CI added (`ci.yml` + `ci_validate.py`, validated exit 0); Governance Gate re-run to **21/21 PASS**. M-D complete. Open: `main`-fold PR merge + PEG-6. | A1 Orchestrator |
