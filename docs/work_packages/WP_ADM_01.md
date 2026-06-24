# WP-ADM-01 — Administration Core Configuration
## NADF ERP Programme — Work Package Definition

**Work Package ID:** WP-ADM-01
**Title:** Administration Core Configuration
**Phase:** 1 — Foundation
**Complexity:** Medium
**Capability area:** CA-04 — Administration & Facilities (fleet, assets, ICT helpdesk; facility management excluded)
**Authority:** PEG-6 approval 2026-06-24 · Transfer Package v2.1
**Prepared by:** A1 Master Orchestrator · D1 Functional Architect
**Date:** 2026-06-24
**Status:** PLANNED — awaiting WP-01 completion and G1/G2/G3 Go/No-Go clearance before implementation

> **DO NOT BEGIN IMPLEMENTATION** until WP-01 exit gate is confirmed PASS and the Go/No-Go checkpoint (§8) is passed by G1, G2, and G3.

---

## 1. Objective

Configure the Administration department's operational tools in Odoo 17 CE:
- Establish the vehicle register and fuel/servicing log (CE `fleet`).
- Establish the asset register with depreciation schedules (CE `account_asset`).
- Install and configure the ICT helpdesk using OCA `helpdesk_mgmt` (replaces the unratified `project`-based workaround from the legacy build).
- Create the Administration user group hierarchy.

WP-ADM-01 addresses CA-04 — Administration & Facilities within Phase 1 scope. Facility management (`nadf_facility` custom module) is deferred to Phase 2 spec / Phase 3 development.

---

## 2. Scope

### In scope
| Item | Detail |
|------|--------|
| Vehicle register | Create vehicle records (type, plate, year, assigned driver); configure fuel log (date, litres, cost, odometer); enable servicing records; assign drivers to vehicles |
| Asset register | Create asset categories (office equipment, IT equipment, furniture, motor vehicles); configure straight-line depreciation; enter sample asset records with depreciation schedules |
| ICT helpdesk (`helpdesk_mgmt`) | Configure ticket categories (hardware, software, network, access request); define SLA rules (response + resolution time); configure team assignment rules; test ticket creation and escalation |
| Administration user groups | Create 5 groups: Driver, Fleet Manager, Asset Manager, IT Officer, IT Manager |
| Documentation | Update `MODULE_REGISTRY.md` if `helpdesk_mgmt` not yet recorded; update `DECISION_LOG.md` if configuration decisions required |

### Out of scope
| Item | Why excluded |
|------|-------------|
| `nadf_facility` custom module | Phase 2 spec required — no spec, no code; deferred to Phase 3 development |
| Facility management configuration | Dependent on `nadf_facility` — deferred |
| Vehicle procurement (purchase orders for vehicles) | WP-03 scope (Procurement) |
| Asset acquisition via purchase orders | WP-03 scope |
| Payroll-linked expense claims for drivers | Deferred pending `nadf_payroll_ng` (Phase 2/3) |
| ICT asset disposal or write-off approvals | Phase 3 custom workflow scope |

---

## 3. Deliverables

| ID | Deliverable | Verification |
|----|------------|--------------|
| D-ADM01-01 | Vehicle register live: ≥ 5 vehicle records with plate, type, assigned driver | `SELECT name, license_plate FROM fleet.vehicle` |
| D-ADM01-02 | Fuel log configured and test entry recorded per vehicle | UI: Fleet → Fuel Log — at least 1 log entry per vehicle |
| D-ADM01-03 | Asset register live: ≥ 3 asset categories, ≥ 3 asset records with depreciation schedule | `SELECT name, state FROM account.asset.asset` |
| D-ADM01-04 | `helpdesk_mgmt` configured: ≥ 3 ticket categories, ≥ 1 SLA rule, assignment rules active | UI: Helpdesk → Configuration |
| D-ADM01-05 | Test ICT helpdesk ticket created, assigned, and resolved | UI: Helpdesk → Tickets — 1 closed test ticket |
| D-ADM01-06 | 5 Administration user groups created and categorised | `SELECT name FROM res.groups WHERE category.name LIKE '%Administration%'` |
| D-ADM01-07 | Legacy `project`-based ICT helpdesk workaround documented before supersession | Note in `IMPLEMENTATION_HISTORY.md` |

---

## 4. Acceptance Criteria

| ID | Criterion | Test method |
|----|-----------|-------------|
| AC-ADM01-01 | Vehicle register contains ≥ 5 vehicle records; each has plate, type, assigned driver | DB query / UI |
| AC-ADM01-02 | Fuel log entries linked to vehicles; mileage and cost fields populated | UI: Fleet → Fuel Log |
| AC-ADM01-03 | Asset register contains ≥ 3 categories and ≥ 3 assets with computed depreciation schedules | UI: Accounting → Assets |
| AC-ADM01-04 | `helpdesk_mgmt` state='installed'; ≥ 3 ticket categories and ≥ 1 SLA rule defined | DB query + UI |
| AC-ADM01-05 | ICT helpdesk test ticket: created → assigned to IT Officer → resolved; `mail.thread` log present | UI verification |
| AC-ADM01-06 (= AC-04) | All CA-04 deliverables complete; `nadf_facility` exclusion documented; no Enterprise module used | Manual review + DB audit |

---

## 5. Risks

| ID | Risk | L | I | Mitigation |
|----|------|---|---|-----------|
| R-ADM01-01 | Legacy `project`-based helpdesk config conflicts with `helpdesk_mgmt` install | Med | Med | Document existing project helpdesk config before install; supersede cleanly |
| R-ADM01-02 | `account_asset` depreciation schedule mismatch with NADF accounting standards | Low | Med | Confirm asset categories and depreciation method with Finance before configuring |
| R-ADM01-03 | Fleet vehicle data not yet confirmed by Administration department | Med | Low | Use sample data for MVP; flag for client data entry before UAT |
| R-ADM01-04 | Administration user groups clash with existing group names from legacy build | Low | Low | Query existing groups before creation; update rather than duplicate |

---

## 6. Governance Reviews Required

| Reviewer | When | Scope |
|----------|------|-------|
| **G1 — Architecture & Odoo Governance** | Exit gate | `helpdesk_mgmt` configuration approach; no core modification; CE modules only |
| **G2 — Quality & Documentation Governance** | Exit gate | All deliverables evidenced; `MODULE_REGISTRY.md` and `DECISION_LOG.md` current |
| **G3 — Security & Change Governance** | Exit gate | Administration user groups correctly scoped; no privilege escalation |

---

## 7. Dependencies

| Dependency | Status | Notes |
|-----------|--------|-------|
| WP-01 complete (exit gate PASS) | ⏳ Not yet started | `helpdesk_mgmt` must be installed (D-WP01-06) before WP-ADM-01 begins |
| WP-GOV-03 (user group naming convention confirmed) | ⏳ | Follow naming pattern from WP-01 §9 implementation notes |
| Client confirmation: vehicle count and asset categories | Required | Minimum data set needed for D-ADM01-01 and D-ADM01-03 |

---

## 8. Go/No-Go Checkpoint (required before implementation begins)

**This checkpoint must be passed before D2 Solution Builder executes a single configuration command.**

G1, G2, and G3 must each confirm:

| Check | G1 | G2 | G3 |
|-------|----|----|-----|
| WP-01 exit gate confirmed PASS | ☐ | ☐ | ☐ |
| `helpdesk_mgmt` state='installed' confirmed | ☐ | ☐ | ☐ |
| Administration user group list approved | ☐ | ☐ | ☐ |
| `nadf_facility` exclusion acknowledged | ☐ | ☐ | ☐ |
| Branch created for WP-ADM-01 implementation | ☐ | ☐ | ☐ |

**Go/No-Go decision:** ☐ GO  ☐ NO-GO (record reason and remediation action)

**Decision recorded by:** ______________________  **Date:** ____________

---

## 9. Implementation Notes (for D2 Solution Builder — not to be actioned before Go/No-Go)

- **Fleet module:** Enable in Settings → Technical → Fleet if not already active. Vehicle types: Sedan, SUV, Pickup, Minibus (confirm with client).
- **Asset register:** `account_asset` is CE native. Categories must be created before asset records. Depreciation method: straight-line by default; confirm with Finance.
- **`helpdesk_mgmt`:** Already installed under WP-01 (D-WP01-06). WP-ADM-01 configures it — ticket categories, SLA rules, assignment rules. Do not reinstall.
- **Legacy helpdesk workaround:** The legacy Phase 8 build used the CE `project` module for ICT helpdesk tickets. Document the existing project-task configuration in `IMPLEMENTATION_HISTORY.md` before configuring `helpdesk_mgmt` as the replacement (D-ADM01-07).
- **User groups:** Prefix all Administration groups with `nadf_` in the technical name to avoid collision with CE default groups.

---

*This work package definition is a planning document only. Implementation does not begin until §8 Go/No-Go passes and WP-01 exit gate is confirmed. Authority: PEG-6 approval 2026-06-24 · Transfer Package v2.1.*
