# PRODUCT_GAP_ANALYSIS.md
## NADF ERP — Product Gap Analysis

**Document ID:** PGA-NADF-001
**Review type:** Engineering Audit — read-only
**Authority:** A1 Master Orchestrator
**Date:** 2026-06-29
**Source:** PETR-NADF-001 · DIS-NADF-001 · GAR v1.3 · DECISION_LOG

---

## Gap Category Definitions

| Category | Description |
|---|---|
| **BUSINESS** | Missing or incomplete business process definition, TO-BE, or process decision — blocks engineering |
| **ENGINEERING** | Missing technical spec, module, design pattern, or platform constraint — blocks build |
| **GOVERNANCE** | Formal decision not raised, deferred item not tracked, or register not reconciled |
| **CLIENT DEPENDENCY** | External input required from NADF client — organizational decision, data, or sign-off |
| **ENVIRONMENTAL** | OCA/CE platform constraint discovered during execution — not a design error, a platform boundary |

---

## Section 1: Business Gaps

### BG-001: Legal TO-BE Processes P4–P6 Missing
**Department:** Legal Services (CA-06)
**Severity:** Critical — blocks all downstream engineering
**Description:** Only Legal processes P1–P3 (contract initiation, drafting, internal review) were delivered in the Transfer Package. Processes P4 (external counterparty sign-off), P5 (execution and sealing), and P6 (archival and expiry alerting) are absent.
**Impact:** `nadf_legal_contract` design spec cannot be written. The data model — especially the contract sign-off chain and counterparty tracking — is entirely undefined. Legal Services build cannot begin.
**Resolution path:** Obtain Legal TO-BE P4–P6 from client/Claude Desktop BRQ session. Spec writing can begin immediately after delivery.
**Owner:** Client / Project Manager
**Blocking:** BL-SPEC-04 · BL-DEV-04 · WP-DEPT-01

---

### BG-002: Investment TO-BE Absent
**Department:** Investment (CA-10)
**Severity:** Critical — NADF's primary revenue-generating function; P1 custom module
**Description:** No business process TO-BE has been delivered for the Investment department. The Transfer Package §3.10 has a framework identifying `nadf_investment` as a P1 custom module with 5 sub-capabilities (loan origination, credit appraisal, disbursement scheduling, repayment tracking, portfolio reporting), but no process flow, RACI, or data model exists.
**Impact:** Investment is NADF's core mandate — structuring loans for MSME agriculture and food businesses. Without the TO-BE, no ERP engineering can proceed. The disbursement-to-payment chain integration with Finance (BL-INT-04) also cannot be designed.
**Resolution path:** Schedule BRQ session with NADF Investment department; obtain TO-BE; write nadf_investment spec immediately after.
**Owner:** Client / Project Manager (BRQ session scheduling)
**Blocking:** BL-SPEC-05 · BL-DEV-05 · BL-INT-04

---

### BG-003: M&E TO-BE Absent
**Department:** Monitoring & Evaluation (CA-11)
**Severity:** High
**Description:** No M&E TO-BE has been delivered. The indicator framework — KPI definitions, target vs actual structure, programme-level tracking — cannot be engineered without process documentation.
**Impact:** `nadf_me_indicators` spec cannot be written. mis_builder is installed but the KPI set is undefined (ESC-CLIENT-WP02-08 open escalation).
**Resolution path:** Obtain M&E TO-BE. Resolve WP02-08 (KPI set confirmation) in parallel.
**Owner:** Client / Project Manager
**Blocking:** BL-SPEC-06 · BL-DEV-06 · ESC-CLIENT-WP02-08

---

### BG-004: Strategy & Planning, Communications, Sustainable Agriculture TO-BEs Absent
**Departments:** Strategy & Planning (CA-07), Communications (CA-08), Sustainable Agriculture (CA-09)
**Severity:** High
**Description:** Three departments have zero process documentation. No TO-BE, no ERP approach confirmed, no capability definition beyond a single backlog line item.
**Impact:** These departments are NOT YET ENGINEERED. No build timeline can be established.
**Resolution path:** Obtain TO-BEs for all three departments. Note: Sustainable Agriculture must assess overlap with `nadf_investment` (grant disbursement pattern) before a separate module is commissioned.
**Owner:** Client / Project Manager
**Blocking:** BL-STR-01 · BL-COM-01 · BL-SA-01 · WP-DEPT-02/03/04

---

### BG-005: Executive Management TO-BE and Dashboard Design Absent
**Department:** Executive Management (CA-12)
**Severity:** Medium (Phase 3 — not blocking current phase)
**Description:** No TO-BE for the executive dashboard. The roll-up dashboard is entirely dependent on all department builds completing — it cannot be designed in isolation. Requires M&E and Finance KPI definitions as inputs.
**Impact:** Phase 3 executive build cannot be planned.
**Resolution path:** Defer until Phase 3 architecture confirmation. Obtain TO-BE at that time.
**Owner:** Client / Project Manager (Phase 3)
**Blocking:** WP-DEPT-07

---

## Section 2: Engineering Gaps

### EG-001: `nadf_project_governance` Not in Transfer Package Custom Module Table
**Department:** Project Coordination (CA-05)
**Severity:** High
**Description:** During WP-PC-01 execution, it emerged that CE has no `parent_id` on `project.project` (DEC-PC01-001) and `is_reached` cannot be field-restricted (DEC-PC01-002). Both require a Phase 2 custom module (`nadf_project_governance`). However, this module does NOT appear in Transfer Package v2.1 §3 Custom Module Table — it was not anticipated at planning time.
**Impact:** Transfer Package is incomplete for Project Coordination Phase 2. The module spec cannot be written until the TP is updated. Programme hierarchy and Director-only milestone restriction enforcement remain organizational-only.
**Resolution path:** Add `nadf_project_governance` to Transfer Package v2.1 custom module table with scope definition (parent_id, milestone restriction, project % complete computed field, programme portfolio view). Then write spec.
**Owner:** Product Engineering / PEF governance
**Blocking:** DEC-PC01-002 technical enforcement

---

### EG-002: `account_budget_oca` Incompatibility with Odoo 17 Build (DEC-OCA-02)
**Department:** Finance (CA-01)
**Severity:** High — sole open engineering escalation blocking Finance completeness
**Description:** OCA `account_budget_oca` v17.0.1.0.0 attempts to access `account.budget.line.theoritical_amount` (note: OCA spelling — the field itself may be differently named in this Odoo build). Installation fails with a field compatibility error. Budget configuration (WP02-07) is blocked.
**Options assessed:**
- **Option A:** Patch the OCA module locally (fork or apply diff) to match this build's field name
- **Option B:** Use CE `account.budget` native model (available in some Odoo 17 CE builds but not validated)
- **Option C:** Deferred — operate without budget module for Phase 1; revisit Phase 2
**Status:** DEC-OCA-02 OPEN ESCALATION — decision required in Wave C
**Resolution path:** Wave C — investigate Option A (local patch) first; validate CE native budget second; if neither, confirm Option C (defer).
**Owner:** Software Factory / Engineering Lead
**Blocking:** WP02-07 (Finance budget configuration)

---

### EG-003: `nadf_vendor_compliance` Spec Not Written (Phase 2, Unblocked)
**Department:** Procurement (CA-02)
**Severity:** Medium — Phase 2 item; unblocked now
**Description:** The `x_compliance_status` field on `res.partner` is a DB-only field created via `ir.model.fields`. It does not survive a module reinstall or database restore without the field definition in a module. The `nadf_vendor_compliance` module spec has not been written despite the Procurement TO-BE being complete.
**Impact:** Vendor compliance data is fragile until the module is built. Spec can be written immediately.
**Resolution path:** Write `docs/modules/nadf_vendor_compliance_spec.md` — TO-BE is complete, module scope is clear.
**Owner:** Software Factory / Engineering Lead (Wave C or next Phase 2 sprint)

---

### EG-004: `nadf_facility` Spec Not Written (Phase 2, Unblocked)
**Department:** Administration (CA-04)
**Severity:** Medium — Phase 2 item; unblocked now
**Description:** Administration TO-BE for facility management (booking, space management) is complete. The `nadf_facility` module is in Transfer Package v2.1. The spec has not been written.
**Resolution path:** Write `docs/modules/nadf_facility_spec.md`.
**Owner:** Software Factory / Engineering Lead (Wave C or next Phase 2 sprint)

---

### EG-005: `nadf_legal_contract` Spec Blocked
**Department:** Legal Services (CA-06)
**Severity:** High
**Description:** Legal TO-BE P4–P6 must be received before the spec can be written. See BG-001.
**Resolution path:** Contingent on BG-001 resolution.

---

### EG-006: `nadf_investment` Spec Blocked
**Department:** Investment (CA-10)
**Severity:** Critical
**Description:** Investment TO-BE and BRQ session must occur before the spec can be written. See BG-002.
**Resolution path:** Contingent on BG-002 resolution.

---

### EG-007: Payment Approval Hard-Block Not Enforceable in CE
**Department:** Finance (CA-01)
**Severity:** Low (mitigated — documented and accepted)
**Description:** DEC-WP02-001 — CE `account.payment` has no hard-block approval mechanism. Payment approval is advisory only via `base_automation` rules. Hard enforcement would require a custom module (`nadf_approvals`).
**Resolution path:** Accept advisory for Phase 1. Phase 2 `nadf_approvals` if client requires hard enforcement.

---

### EG-008: Study Leave 3-Level Approval Not Enforceable in CE
**Department:** HR (CA-03)
**Severity:** Low (mitigated)
**Description:** DEC-007 — `hr_holidays` in CE supports a maximum of 2 approval levels. 3-level Study Leave approval is advisory only.
**Resolution path:** Accept for Phase 1. Phase 2 `nadf_hr_leave` custom module if required.

---

## Section 3: Governance Gaps

### GG-001: Backlog Not Reconciled with Execution State
**Severity:** High — governance integrity
**Description:** `planning/BACKLOG.md` is stale. All Phase 0 GOV items (BL-GOV-01 through BL-GOV-09) show "Not Started" — M0 is CLOSED. All Phase 1 department WP items show "In Progress" or "Not Started" — WP-01/02/03/04/ADM-01/PC-01 are all CONDITIONAL PASS. No backlog item is marked "Done."
**Impact:** The backlog does not reflect the actual programme state. Wave C planning, stakeholder reporting, and M1 milestone assessment cannot use the backlog as a reliable source of truth.
**Resolution path:** Backlog reconciliation pass required in Wave C before WP-05 UAT. Update all Phase 0 items to DONE; update Phase 1 WP items to CONDITIONAL PASS; mark deferred items as DEFERRED with reference to DEC IDs.
**Owner:** Programme Coordinator / Engineering Lead

---

### GG-002: `nadf_project_governance` Absent from Transfer Package v2.1
**Severity:** High (see EG-001)
**Description:** Transfer Package is the bound authority document. A confirmed Phase 2 custom module (`nadf_project_governance`) is not in it.
**Resolution path:** Raise a Transfer Package amendment to add `nadf_project_governance`. Confirm scope with client. Update custom module table.
**Owner:** Product Engineering

---

### GG-003: Milestone Model Not Yet Accepted
**Severity:** Medium
**Description:** The M1 sub-milestone proposal (M1-CPC / M1-OPR / M1-PRD) was produced in Session 4 and returned as TEXT ONLY pending A1 Master Orchestrator acceptance. It has not been implemented in MILESTONE_TRACKER.md.
**Resolution path:** A1 Master Orchestrator accepts or rejects the recommendation. If accepted, implement in MILESTONE_TRACKER.md without changing historical records.
**Owner:** A1 Master Orchestrator

---

## Section 4: Client Dependency Gaps

| ID | Dependency | Blocks | Status |
|---|---|---|---|
| B-02 | Procurement RACI step 1.19 approver confirmation | WP03-07 | Outstanding |
| B-03 | PO approval threshold values (₦500K threshold UNCHANGED until confirmed) | WP03-07 | Outstanding |
| B-WP04-01 | 6 Admin-dept employee department/reporting line confirmation (IDs 12,13,14,18,20,23) | Driver/IT Officer groups; fleet drivers; PCU user assignments (WP-PC-01) | Outstanding |
| B-WP04-02 | NADF RC number and TIN | WP04-08 company registration | Outstanding |
| B-ADM01-01 | Vehicle license plates + driver assignments | Fleet management completeness | Outstanding |
| WP02-02 | Client CoA CSV sign-off | Finance completeness | Outstanding |
| WP02-08 | mis_builder KPI set confirmation | Finance dashboard + M&E pre-work | Open escalation |
| BG-001 | Legal TO-BE P4–P6 | Entire Legal engineering chain | Outstanding |
| BG-002 | Investment TO-BE + BRQ session | Entire Investment engineering chain | Outstanding |
| BG-003 | M&E TO-BE | Entire M&E engineering chain | Outstanding |
| BG-004 | Strategy/Communications/SA TO-BEs | 3 departments entirely unengineered | Outstanding |

---

## Section 5: Environmental Gaps (CE Platform Constraints)

These are confirmed Odoo 17 Community Edition constraints discovered during execution. They are documented in the GAR (v1.3). They are not design errors — they are platform boundaries that require workarounds or Phase 2 custom modules.

| ID | Constraint | Workaround Applied | Phase 2 Module |
|---|---|---|---|
| DEC-OCA-02 | `account_budget_oca` incompatible | None yet — OPEN escalation | Patch or CE native |
| DEC-PC01-001 | `project.project` has no `parent_id` | Naming convention hierarchy | `nadf_project_governance` |
| DEC-PC01-002 | `project.milestone.is_reached` not field-restriceable | Organizational control (Director group) | `nadf_project_governance` |
| DEC-ADM01-001 | `helpdesk_mgmt` has no SLA model | Priority + stage timestamp proxy | `nadf_ict_helpdesk` |
| DEC-WP02-001 | `account.payment` no hard-block approval | `base_automation` advisory rule | `nadf_approvals` |
| DEC-007 | `hr_holidays` max 2 approval levels | Advisory 3-level (organizational) | `nadf_hr_leave` |
| DEC-WP03-001 | `ir.model.fields` DB-only field fragility | Temporary; field survives restart not reinstall | `nadf_vendor_compliance` |

---

## Gap Priority Matrix

| Gap | Category | Severity | Phase | Action Owner |
|---|---|---|---|---|
| BG-002 Investment TO-BE | Business | Critical | 2 | Client |
| EG-002 DEC-OCA-02 budget module | Engineering | High | C (current) | Engineering |
| BG-001 Legal TO-BE P4–P6 | Business | High | 2 | Client |
| GG-001 Backlog stale | Governance | High | C (current) | Prog Coordinator |
| EG-001 nadf_project_governance not in TP | Engineering/Gov | High | 2 | Engineering |
| BG-003 M&E TO-BE | Business | High | 2 | Client |
| BG-004 Strategy/Comms/SA TO-BEs | Business | High | 3 | Client |
| B-02/B-03 Procurement client | Client Dependency | High | C (current) | Client |
| B-WP04-01 Employee roles | Client Dependency | High | C (current) | Client |
| EG-003 nadf_vendor_compliance spec | Engineering | Medium | 2 | Engineering |
| EG-004 nadf_facility spec | Engineering | Medium | 2 | Engineering |
| GG-002 TP v2.1 amendment | Governance | Medium | 2 | Engineering |
| GG-003 Milestone model acceptance | Governance | Medium | C (current) | A1 Master Orchestrator |
| EG-007/008 Advisory-only controls | Engineering | Low | 2 | Engineering |

---

*PGA-NADF-001 — A1 Master Orchestrator — 2026-06-29*
