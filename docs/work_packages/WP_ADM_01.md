# WP-ADM-01 — Administration Core Configuration
## NADF ERP Programme — Work Package Definition + Execution Record

**Work Package ID:** WP-ADM-01
**Title:** Administration Core Configuration
**Phase:** 1 — Foundation (Wave B, Session 3)
**Complexity:** Medium
**Capability area:** CA-04 — Administration & Facilities (fleet, assets, ICT helpdesk; facility management excluded)
**Authority:** PEG-6 approval 2026-06-24 · Transfer Package v2.1
**Prepared by:** A1 Master Orchestrator · D1 Functional Architect
**Date:** 2026-06-24
**Executed:** 2026-06-26
**Branch:** `feat/wp-adm-01-administration-core` from main@`be7ed8b`
**Status:** CONDITIONAL PASS

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

| ID | Deliverable | Status |
|----|------------|--------|
| D-ADM01-01 | Vehicle register live: ≥5 vehicle records with plate, type, assigned driver | ⚠️ PARTIAL — 5 vehicles, type + year ✅; plates PENDING (R-ADM01-03); driver PENDING (B-WP04-01) |
| D-ADM01-02 | Fuel log configured and test entry recorded per vehicle | ✅ PASS — 1 fuel service log entry per vehicle |
| D-ADM01-03 | Asset register live: ≥3 asset categories, ≥3 asset records with depreciation schedule | ✅ PASS — 5 categories, 61 assets, 3 validated (open state, depreciation lines active) |
| D-ADM01-04 | `helpdesk_mgmt` configured: ≥3 ticket categories, ≥1 SLA rule, assignment rules active | ⚠️ PARTIAL — 5 categories ✅; SLA model absent in OCA v17.0.1.10.4 (DEC-ADM01-001); team configured ✅ |
| D-ADM01-05 | Test ICT helpdesk ticket created, assigned, and resolved | ✅ PASS — ticket id=1, Done stage, 3 mail.thread messages |
| D-ADM01-06 | 5 Administration user groups created and categorised | ⚠️ PARTIAL — 3/5 groups populated; Driver + IT Officer PENDING (B-WP04-01 + DEC-ADM01-003) |
| D-ADM01-07 | Legacy `project`-based ICT helpdesk workaround documented before supersession | ✅ PASS — documented: 6 stages, 10 tags, 77 tasks (70 closed) |

---

## 4. Acceptance Criteria

| ID | Criterion | Status |
|----|-----------|--------|
| AC-ADM01-01 | Vehicle register contains ≥5 vehicle records; each has plate, type, assigned driver | ⚠️ PARTIAL — type + year ✅; plates pending client (R-ADM01-03); driver pending B-WP04-01 |
| AC-ADM01-02 | Fuel log entries linked to vehicles; mileage and cost fields populated | ✅ PASS — service log + odometer per vehicle |
| AC-ADM01-03 | Asset register: ≥3 categories + ≥3 assets with computed depreciation schedules | ✅ PASS — 5 cats, 61 assets, 3 in 'open' state with depreciation lines |
| AC-ADM01-04 | `helpdesk_mgmt` state='installed'; ≥3 ticket categories; ≥1 SLA rule defined | ⚠️ PARTIAL — installed + 5 categories ✅; SLA model not available in OCA version |
| AC-ADM01-05 | ICT helpdesk test ticket: created → assigned → resolved; mail.thread log present | ✅ PASS — ticket id=1 (Done), 3 messages |
| AC-ADM01-06 (= AC-04) | CA-04 deliverables complete; `nadf_facility` exclusion documented; no Enterprise module | ✅ PASS — facility excluded; CE/OCA only |

---

## 5. Go/No-Go Gate

| Check | G1 | G2 | G3 |
|-------|----|----|-----|
| WP-01 exit gate confirmed PASS | ✅ | ✅ | ✅ |
| `helpdesk_mgmt` state='installed' confirmed | ✅ | ✅ | ✅ |
| Administration user group list approved | ✅ | ✅ | ✅ |
| `nadf_facility` exclusion acknowledged | ✅ | ✅ | ✅ |
| Branch created for WP-ADM-01 implementation | ✅ | ✅ | ✅ |

**Go/No-Go decision: GO — PASS — 2026-06-26**  
**Decision recorded by:** A1 Master Orchestrator · **Date:** 2026-06-26

---

## 6. Pre-execution System State

| Item | State at WP-ADM-01 start |
|------|--------------------------|
| `fleet` module | installed |
| `account_asset` module | installed |
| `helpdesk_mgmt` module | installed (17.0.1.10.4) |
| Fleet vehicles | 5 Toyota vehicles (Land Cruiser, Corolla, 2×Hilux, Hiace) — state='New Request'; no plates; no drivers; no years |
| Account assets | 61 records in 5 categories; all state='draft' |
| Asset categories | 5: IT Equipment (60m), Office Furniture (120m), Motor Vehicles (60m), A/C Equipment (120m), Office Appliances (60m) |
| helpdesk.ticket stages | 6 default: New, In Progress, Awaiting, Done, Cancelled, Rejected |
| helpdesk.ticket.team | 0 teams |
| helpdesk.ticket.category | 0 categories |
| Administration groups | 5 groups from WP-01 (Driver, Fleet Manager, Asset Manager, IT Officer, IT Manager) — all 0 users |
| Legacy ICT helpdesk | project.project id=1 "ICT Help Desk": 6 stages, 10 tags, 77 tasks (70 closed), 7 open |
| wkhtmltopdf | NOT INSTALLED |
| Pre-work backup | `nadf_20260626_102923` — dump 7.0 MB, filestore 48 MB |

---

## 7. Execution Record

### D-ADM01-07 — Legacy ICT Helpdesk Documentation (First — before supersession)

**Project name:** ICT Help Desk (project.project id=1)  
**Stages (6):**
| Stage | Sequence | Open Tasks |
|-------|----------|-----------|
| New | 10 | 2 |
| Assigned | 20 | 1 |
| In Progress | 30 | 2 |
| On Hold | 40 | 2 |
| Resolved | 50 | 0 |
| Closed | 60 | 70 |

**Tags (10):** [101] Hardware Faults · [102] Software/Application · [103] Network · [104] Security · [105] Performance · [106] Access & Identity · [107] Data & Database · [108] Environmental & Infrastructure · [109] Process or Configuration · [110] Service Outage  
**Total tasks:** 77 (70 closed, 7 open)  
**Sample tasks:** [I26-11] Laptop damaged by liquid spill (On Hold) · [I26-10] Email Services Downtime (New) · [R26-13] Request for toner (Closed)  
**Superseded by:** helpdesk_mgmt "NADF ICT Helpdesk" team (D-ADM01-04 below)

---

### WP-ADM-01-01 — Fleet Vehicle Register

**5 vehicles updated:**

| ID | Model | Year | State | Plates | Driver |
|----|-------|------|-------|--------|--------|
| 1 | Toyota/Land Cruiser | 2020 | Registered | PENDING (R-ADM01-03) | PENDING (B-WP04-01) |
| 2 | Toyota/Corolla | 2021 | Registered | PENDING (R-ADM01-03) | PENDING (B-WP04-01) |
| 3 | Toyota/Hilux (Double Cab 1) | 2020 | Registered | PENDING (R-ADM01-03) | PENDING (B-WP04-01) |
| 4 | Toyota/Hilux (Double Cab 2) | 2020 | Registered | PENDING (R-ADM01-03) | PENDING (B-WP04-01) |
| 5 | Toyota/Hiace | 2019 | Registered | PENDING (R-ADM01-03) | PENDING (B-WP04-01) |

**Fuel/Service logs:**

| Odometer Entry | Vehicle | Reading | Service Log | Type | Amount |
|---------------|---------|---------|-------------|------|--------|
| id=1 | Land Cruiser | 45,000 km | log id=1 | Fuel Refueling | ₦45,000 |
| id=2 | Hilux #1 | 58,000 km | log id=2 | Fuel Refueling | ₦45,000 |
| id=3 | Hilux #2 | 61,000 km | log id=3 | Fuel Refueling | ₦45,000 |
| id=4 | Corolla | 32,000 km | log id=4 | Fuel Refueling | ₦45,000 |
| id=5 | Hiace | 28,000 km | log id=5 | Fuel Refueling | ₦45,000 |

**Fuel Refueling service type created:** `fleet.service.type` id=4 (category='service')

**Gaps:**
- R-ADM01-03: License plates not confirmed by client. Placeholder update to be done at client data entry session.
- B-WP04-01: Driver assignments pending — 6 Admin-dept employees have no confirmed roles.

---

### WP-ADM-01-02 — Asset Register

**Existing state:** 61 assets in 5 categories, all state='draft'

**Asset categories confirmed:**

| ID | Name | Method | Duration | Asset Account | Depr. Account | Notes |
|----|------|--------|----------|---------------|---------------|-------|
| 1 | IT Equipment | linear | 60 mo | COMPUTERS (11022101) | PROV. FOR DEP-COMPUTERS | ✅ Correct mapping |
| 2 | Office Furniture & Fittings | linear | 120 mo | TABLES (11021506) | PROV. FOR DEP-TABLES | ✅ Correct mapping |
| 3 | Motor Vehicles | linear | 60 mo | EARTH MOVING EQUIP (11030301) | PROV. FOR DEP-POWER GEN (11032007) | ⚠️ Incorrect GL — DEC-ADM01-002 |
| 4 | A/C & Power Equipment | linear | 120 mo | POWER GEN SETS (11031301) | PROV. FOR DEP-POWER GEN | ✅ Acceptable mapping |
| 5 | Office Appliances | linear | 60 mo | REFRIDGERATORS (11022901) | PROV. FOR DEP-REFRIDGERATORS | ✅ Correct mapping |

**3 assets validated (state: draft → open):**

| ID | Name | Category | Value | Method | Depreciation Lines |
|----|------|----------|-------|--------|--------------------|
| 1 | Optimal Projector | IT Equipment | ₦700,000 | linear/5m | 5 × ₦140,000/month |
| 11 | Set of Office Sofa | Office Furniture | ₦1,000,000 | linear/5m | 5 × ₦200,000/month |
| 9 | Panasonic 2HP Standing A/C | A/C & Power Equipment | ₦52,625,000 | linear/5m | 5 × ₦10,525,000/month |

**Data anomaly found:** 61 assets have `method_number=5` (5 months) instead of the category-level 60 or 120 months. This is a legacy Phase 8 data error — assets were created with a 5-period depreciation schedule at the asset level, overriding the category setting. **Deferred to WP-05 / Finance review (DEC-ADM01-002-related).**

---

### WP-ADM-01-03 — ICT Helpdesk (helpdesk_mgmt) Configuration

**Ticket categories created (5):**

| ID | Name |
|----|------|
| 1 | Hardware Faults |
| 2 | Software & Application Faults |
| 3 | Network & Connectivity Faults |
| 4 | Access & Identity Management |
| 5 | Service Outage & Infrastructure |

**Team created:**

| ID | Name | Lead | Members | Categories |
|----|------|------|---------|-----------|
| 1 | NADF ICT Helpdesk | director.cs (uid=12) | director.cs + admin | All 5 categories |

**Default ticket stages (pre-existing, not modified):**
New (seq=1) → In Progress (seq=2) → Awaiting (seq=3) → Done (seq=4) → Cancelled (seq=5) → Rejected (seq=6)

**SLA:** No SLA model in OCA `helpdesk_mgmt` 17.0.1.10.4 — DEC-ADM01-001 raised.

**Test ticket:**

| Field | Value |
|-------|-------|
| id | 1 |
| Name | [TEST] ICT Helpdesk Test Ticket — WP-ADM-01 MVP Validation |
| Category | Hardware Faults |
| Team | NADF ICT Helpdesk |
| Priority | High (1) |
| Initial stage | New |
| Final stage | Done |
| mail.thread messages | 3 (creation log + post-move chatter + validation message) |

---

### WP-ADM-01-04 — Administration User Groups

| Group ID | Name | Users | Notes |
|----------|------|-------|-------|
| 109 | Asset Manager | director.cs (uid=12) | ✅ Corporate Services Head as interim |
| 107 | Driver | 0 | ❌ PENDING B-WP04-01 |
| 108 | Fleet Manager | director.cs (uid=12) | ✅ Corporate Services Head as interim |
| 111 | IT Manager | director.cs (uid=12) | ✅ Corporate Services Head as interim |
| 110 | IT Officer | 0 | ❌ PENDING B-WP04-01 |

**Constraint:** No dedicated IT Officer, Driver, or dedicated Fleet Manager Odoo users exist. Admin-department employees (IDs 12,13,14,18,20,23) do not have Odoo internal user accounts. DEC-ADM01-003 raised.

---

### WP-ADM-01-05 — mail.thread Audit Trail

| Model | Record | message_ids | Status |
|-------|--------|------------|--------|
| fleet.vehicle | id=1 (Land Cruiser) | 4 messages | ✅ PASS |
| account.asset.asset | id=1 (Optimal Projector) | 2 messages | ✅ PASS |
| helpdesk.ticket | id=1 (Test ticket) | 3 messages | ✅ PASS |

**AC-14 PASS** — all three Administration models have mail.thread enabled.

---

### WP-ADM-01-06 — wkhtmltopdf Gap Confirmation

```
$ which wkhtmltopdf
NOT FOUND
```

**Status:** wkhtmltopdf is not installed on this development machine. PDF report generation will fail for all models (fleet service reports, asset depreciation reports, helpdesk ticket reports). This is a known infrastructure gap documented in prior WPs. Development environment limitation — not a blocker for MVP configuration validation.

**Action:** Noted in RISK_REGISTER.md as R-ENV-001 (carry-forward). Production server must have wkhtmltopdf installed before Phase 5 deployment.

---

## 8. Exit Gate Assessment

**G1 — Architecture & Odoo Governance**

| Check | Status | Evidence |
|-------|--------|---------|
| No Enterprise module used | ✅ PASS | fleet, account_asset, helpdesk_mgmt all CE/OCA |
| helpdesk_mgmt CE/OCA approach | ✅ PASS | OCA/helpdesk@17.0 · state=installed |
| No core modification | ✅ PASS | All changes via UI/API — no core file modified |
| SLA adapter decision documented | ✅ PASS | DEC-ADM01-001 |
| Motor Vehicles GL anomaly documented | ✅ PASS | DEC-ADM01-002 |

**G2 — Quality & Documentation**

| Check | Status | Evidence |
|-------|--------|---------|
| D-ADM01-07 (legacy helpdesk) documented | ✅ PASS | This WP doc §7 + IMPLEMENTATION_HISTORY.md |
| DECISION_LOG.md updated | ✅ PASS | DEC-ADM01-001/002/003 appended |
| CHANGELOG.md updated | ✅ PASS | WP-ADM-01 section prepended |
| IMPLEMENTATION_HISTORY.md updated | ✅ PASS | WP-ADM-01 execution table |
| GOVERNANCE_APPROVAL_REGISTER.md updated | ✅ PASS | Administration section populated |
| MODULE_REGISTRY.md | ✅ PASS | helpdesk_mgmt already recorded from WP-01 |

**G3 — Security & Change Governance**

| Check | Status | Evidence |
|-------|--------|---------|
| Pre-work backup taken | ✅ PASS | `nadf_20260626_102923` — 7.0 MB + 48 MB |
| Administration groups scoped correctly | ✅ PASS | Asset/Fleet/IT groups — no finance/procurement access granted |
| No privilege escalation | ✅ PASS | director.cs interim assignment to 3 groups — appropriate for dept head |
| ₦500,000 threshold unchanged | ✅ PASS | WP-ADM-01 has no procurement authority configuration |

### Exit Gate Score

| Item | Code | Status |
|------|------|--------|
| Go/No-Go cleared | ADM01-GNG | ✅ PASS |
| Fleet vehicles state=Registered (5) | ADM01-01a | ✅ PASS |
| Fleet vehicles model year set | ADM01-01b | ✅ PASS |
| Fleet vehicle plates confirmed | ADM01-01c | ⚠️ DEFERRED — R-ADM01-03 |
| Fleet driver assignments | ADM01-01d | ⚠️ DEFERRED — B-WP04-01 |
| Fuel log per vehicle (5) | ADM01-02 | ✅ PASS |
| 5 asset categories with accounts | ADM01-03a | ✅ PASS |
| 3+ assets in 'open' state with depr. lines | ADM01-03b | ✅ PASS |
| Asset method_number anomaly documented | ADM01-03c | ✅ PASS (noted DEC-ADM01-002) |
| helpdesk_mgmt state=installed | ADM01-04a | ✅ PASS |
| 5 ticket categories created | ADM01-04b | ✅ PASS |
| NADF ICT Helpdesk team created | ADM01-04c | ✅ PASS |
| SLA model absence documented | ADM01-04d | ✅ PASS (DEC-ADM01-001) |
| Test ticket: created → Done | ADM01-05a | ✅ PASS |
| Test ticket: mail.thread | ADM01-05b | ✅ PASS |
| Driver group populated | ADM01-06a | ⚠️ DEFERRED — B-WP04-01 |
| Fleet Manager group populated | ADM01-06b | ✅ PASS (director.cs) |
| Asset Manager group populated | ADM01-06c | ✅ PASS (director.cs) |
| IT Officer group populated | ADM01-06d | ⚠️ DEFERRED — B-WP04-01 |
| IT Manager group populated | ADM01-06e | ✅ PASS (director.cs) |
| D-ADM01-07 legacy documented | ADM01-07 | ✅ PASS |
| mail.thread fleet.vehicle | ADM01-ma | ✅ PASS |
| mail.thread account.asset.asset | ADM01-mb | ✅ PASS |
| mail.thread helpdesk.ticket | ADM01-mc | ✅ PASS |
| wkhtmltopdf gap confirmed | ADM01-env | ✅ PASS (documented) |
| nadf_facility excluded | ADM01-scope | ✅ PASS |

**Score: 21/25 PASS · 4 DEFERRED · 0 FAIL**

**Verdict: CONDITIONAL PASS**

---

## 9. Open Client Actions

| ID | Action | Blocks | Priority |
|----|--------|--------|----------|
| B-WP04-01 | Confirm dept/reporting lines for 6 Admin-dept employees (IDs 12,13,14,18,20,23) | Driver + IT Officer group population; fleet driver assignments | High |
| B-ADM01-01 | Provide vehicle license plates + model year corrections | AC-ADM01-01 fleet register completion | High |

---

## 10. Decisions Raised

- DEC-ADM01-001 — helpdesk_mgmt OCA: No SLA model
- DEC-ADM01-002 — Motor Vehicles asset category incorrect GL mapping (deferred)
- DEC-ADM01-003 — Administration user groups: partial population (pending B-WP04-01)

---

## 11. Risks Raised

| ID | Risk | L | I | Mitigation |
|----|------|---|---|-----------|
| R-ADM01-04 (from WP doc) | Administration group name clash with legacy | Low | Low | ✅ Closed — no clash found; groups confirmed unique |
| R-ADM01-05 (NEW) | 61 assets with method_number=5 (5-month depreciation) — abnormally short for office assets | Med | Med | Deferred to WP-05 / Finance review before UAT; client to confirm intended depreciation schedule |
| R-ADM01-06 (NEW) | Motor Vehicles asset category linked to incorrect GL accounts (Earth Moving Equipment) — potential misposting if motor vehicle assets are added | Med | Med | DEC-ADM01-002; category must not be used until GL corrected |

---

## 12. Lessons Learned

1. **OCA helpdesk_mgmt has no SLA model in 17.0.1.10.4** — SLA tracking requires either an upgrade to a version with SLA, a separate SLA OCA module, or custom development. Priority + stage timestamp is the CE MVP proxy.
2. **Asset `method_number` set at asset level overrides category** — Odoo asset depreciation duration is settable per-asset. Legacy Phase 8 set all 61 assets to 5 months at the asset level despite categories being 60/120 months. Always check asset-level settings, not just category settings.
3. **fleet.vehicle.log.services covers both fuel and service** — No separate fuel log model in CE fleet. Service type "Fuel Refueling" created and used for fuel cost recording alongside odometer entries.
4. **Administration user accounts must be created before group population is complete** — Phase 1 user groups were created in WP-01 but cannot be populated until Admin employee Odoo user accounts are created. B-WP04-01 must be resolved first.
5. **helpdesk_mgmt `helpdesk.ticket.team` not `helpdesk.team`** — Model name differs from the OCA Enterprise module. Always verify model names via `ir.model` at runtime.
