# NADF FULL PRODUCT TRANSFER PACKAGE — v2.0

**Status:** AUTHORITATIVE — supersedes all prior versions of this document  
**Prepared by:** Claude Desktop (NADF BPOGS Project Folder)  
**Date:** 2026-06-19  
**Destination:** Claude Code — NADF ERP Local Repository  
**Supersedes:** `NADF_FULL_PRODUCT_TRANSFER_PACKAGE.md` (v1.0, 2026-06-16)

**Authority statement:** All information in this document is based exclusively on NADF project materials available in the Claude Desktop project folder — BPOGS outputs, process refinement outputs, ERP mappings, swimlane outputs, decision registers, QA outputs, department workbooks, and the prior transfer package and control tower scaffold. Claude Desktop has not inspected and does not claim to have inspected the local repository, the Odoo instance, the GitHub repository, or the database. All repository-side and Odoo-instance-side facts must be independently verified by Claude Code via the discovery sequence in Section 17 before any implementation proceeds.

---

## ⚠️ CRITICAL PLATFORM CORRECTION — READ FIRST

**The v1.0 package incorrectly assumed Odoo 17 Enterprise with a planned Odoo 18 Enterprise migration. This was wrong and is now corrected.**

**The authoritative platform is: Odoo 17 Community Edition.**

This correction invalidates every Enterprise-only module assumption made previously. The following Enterprise modules/features **must not** be assumed available and **must not** appear in any module mapping, roadmap, or implementation prompt unless explicitly re-confirmed by the user with evidence of an Enterprise licence:

- Enterprise Approvals (`approvals`)
- Enterprise Documents (`documents`)
- Enterprise Sign (`sign`)
- Enterprise Spreadsheet (`spreadsheet_dashboard`, `documents_spreadsheet`)
- Enterprise Knowledge (`knowledge`)
- Enterprise Studio (`web_studio`)
- Enterprise Payroll (`hr_payroll` Enterprise edition — Community has only the base/limited payroll structure, often insufficient for Nigerian payroll and typically replaced entirely)

**Resolution protocol for every Enterprise-shaped requirement identified in this package:**
1. **Identify the gap** — name the Enterprise feature that would normally satisfy the requirement.
2. **Recommend the Community alternative** — native Odoo 17 CE functionality that covers some or all of the requirement.
3. **Recommend the OCA alternative** — a named, real OCA (Odoo Community Association) module/repository that closes the remaining gap.
4. **Recommend custom development only if justified** — only when neither Community core nor OCA closes the gap, and only with an explicit justification.

This four-step protocol is applied throughout Section 6 (ERP Mapping) and Section 8 (Capability Map) below. Every previous reference to an Enterprise module elsewhere in NADF project documentation should be treated as provisional pending this re-mapping.

---

## SECTION 1 — PRODUCT VISION

**Client:** National Agricultural Development Fund (NADF)  
**Consultant:** Lanasoft Technologies  
**Product:** NADF Business Process Optimisation and Governance System (BPOGS) — implemented on **Odoo 17 Community Edition**  
**Platform strategy:** Community Edition core, extended with vetted OCA modules, with custom development reserved for genuine gaps (e.g. investment/loan management, M&E KPI dashboards, Nigerian-specific payroll)

**Vision:** Replace all manual, paper-based, and siloed departmental workflows at NADF with a unified, auditable, automated ERP system built on Odoo 17 Community Edition — fully aligned with documented and optimised business processes across all 12 NADF departments, governed by BPMN-standard swimlane process maps, and engineered from day one to yield a reusable Public Sector ERP Template for future government-sector deployments.

**Non-negotiable constraints:**
- Odoo Enterprise features must never be assumed, specified, or referenced as available in any client-facing document, report, diagram, module mapping, or code comment, unless the user explicitly confirms an Enterprise licence with evidence.
- Where Enterprise functionality is conceptually needed, the four-step resolution protocol above must be followed and documented.
- NADF is **Reference Implementation #1** of a future Public Sector ERP Template — not the template itself (see Section 13, Product Hierarchy).

---

## SECTION 2 — BUSINESS SCOPE

### Methodology
Each department's processes are documented in three layers:
1. **Refined AS-IS** — current state (workbook sheet `1_Refined_AS-IS`)
2. **Detailed TO-BE** — future optimised state with Odoo integration (workbook sheet `3_Detailed_TO-BE`)
3. **Executive TO-BE** — summary layer (workbook sheet `2_Executive_TO-BE`) — never used for production diagrams

### Deliverable per process
- Browser-rendered HTML swimlane diagram (AS-IS and Detailed TO-BE), built on the custom inline SwimEngine v3.0
- RACI matrix embedded in workbook (Responsible / Accountable / Consulted / Informed)
- Odoo system step badges on all automated TO-BE steps ("AUTOMATED — NO USER ACTION")

### Total scope
- **12 departments**
- **61+ processes** (exact count to be reconciled by Claude Code against the workbook inventory once repository access is confirmed)
- **~120+ HTML swimlane files** (AS-IS + TO-BE per process)

### Scope boundary
This package covers business process documentation (swimlanes + workbooks) and ERP configuration/build (Odoo 17 CE + OCA + custom modules). It does not cover infrastructure provisioning, network architecture, or hardware procurement, which are out of scope for Claude Desktop and Claude Code and remain Lanasoft/NADF IT responsibilities unless stated otherwise.

---

## SECTION 3 — DEPARTMENT REQUIREMENTS

### 3.1 HR
- **Processes:** P1–P8 (8 processes)
- **AS-IS swimlanes:** Complete (all 8 approved)
- **TO-BE swimlanes:** Complete (all 8 approved)
- **Platform correction:** Payroll requirement previously mapped to Enterprise Payroll — now re-mapped to Community `hr` + `hr_holidays` (CE leave module name) + OCA payroll modules (see Section 6/8)
- **Status:** Swimlanes done; Odoo Phase 1 build in progress under corrected module set
- **Outstanding:** Confirm actual Phase 1 installed modules against this corrected mapping; benefits/retirement (HR-P6) configuration; UAT

### 3.2 Finance
- **Processes:** P1–P7 (7 processes)
- **AS-IS swimlanes:** Complete (all 7 approved)
- **TO-BE swimlanes:** Complete (all 7 approved)
- **Platform correction:** Executive financial dashboard previously implied Enterprise Spreadhseet/Dashboard — now re-mapped to Community `account` reporting + OCA dashboard modules or custom
- **Status:** Core accounting build in progress under corrected module set
- **Outstanding:** Executive financial dashboard (re-scoped); 2FA enforcement; UAT

### 3.3 Procurement
- **Processes:** P1–P6 (6 processes)
- **AS-IS swimlanes:** Complete (all 6 approved)
- **TO-BE swimlanes:** Complete (all 6 approved — two open blockers)
- **Platform correction:** Multi-level approval workflow previously implied Enterprise Approvals — now re-mapped to Community `purchase` approval limits + OCA `purchase_request`/approval workflow modules
- **Status:** Core purchase build in progress under corrected module set
- **Open blockers:**
  - B-02: RACI inversion on step 1.19 (DEC-PROC-01) — awaiting client confirmation
  - B-03: Missing priority/timeline data on DEC-PROC-03/04 — awaiting client data

### 3.4 Administration
- **Processes:** ~5
- **AS-IS swimlanes:** Complete
- **TO-BE swimlanes:** Complete
- **Modules:** `fleet`, `maintenance` (Community-native), `helpdesk` — **correction:** Odoo's native `helpdesk` module is Enterprise-only in 17; Community alternative is OCA `helpdesk_mgmt` or a custom ticketing model
- **Status:** Fleet and assets on native Community modules; helpdesk approach must be re-confirmed under OCA `helpdesk_mgmt`; facility management and fuel tracking in progress

### 3.5 Project Coordination
- **Processes:** P1–P5 (5 processes)
- **AS-IS swimlanes:** Complete (all 5: v1.0–v1.3)
- **TO-BE swimlanes:** Complete (all 5: v2.0)
- **Process list:** P1 Project Initiation, P2 Project Planning, P3 Project Execution, P4 Monitoring & Control, P5 Project Closure
- **Modules:** `project` (Community-native, fully featured for this use case)
- **Status:** Swimlanes done; Odoo Project module not yet configured

### 3.6 Strategy & Planning
- **Processes:** ~5 (exact count pending workbook upload)
- **AS-IS swimlanes:** Not started
- **TO-BE swimlanes:** Not started
- **Status:** Queued — workbooks not yet uploaded

### 3.7 Legal Services Unit (LSU) — ACTIVE DEPARTMENT
- **Processes:** P1–P6 (P6 existence to be confirmed)
- **AS-IS swimlanes:** P1–P4 approved; P5 in production; P6 not started
- **TO-BE swimlanes:** P1–P3 approved; P4–P6 not started
- **Platform correction:** Contract sign-off previously implied Enterprise Sign — now re-mapped to Community manual approval step + OCA `sign` alternative if e-signature is genuinely required (verify need; manual sign-off may suffice given NADF's governance model)
- **Key design rules (locked):**
  - Counterparties share ES/CEO lane — no standalone counterparty column
  - HLSU does not receive a separate lane; accountability note used instead
  - Dual START triggers permitted in P5
  - END marker in column of final acting party
- **Outstanding:** P5 AS-IS; P4–P6 TO-BE

### 3.8 Communications
- **Processes:** ~5 (pending workbook upload)
- **Status:** Not started; queued after Strategy

### 3.9 Sustainable Agriculture
- **Processes:** ~5 (pending workbook upload)
- **Status:** Not started

### 3.10 Investment
- **Processes:** ~5 (pending workbook upload)
- **Platform note:** Investment/loan management has no Community or OCA equivalent of sufficient depth — custom module justified (see Section 8)
- **Status:** Not started

### 3.11 Monitoring & Evaluation (M&E)
- **Processes:** ~5 (pending workbook upload)
- **Platform note:** KPI dashboard previously implied Enterprise Spreadsheet Dashboard — re-mapped to OCA `bi_view_editor`/`mis_builder` or custom (see Section 8)
- **Status:** Not started

### 3.12 Executive Management
- **Processes:** ~4 (pending workbook upload)
- **Platform note:** Executive dashboard previously implied Enterprise Spreadsheet — re-mapped to OCA `mis_builder` (Management Information System Builder, the standard OCA solution for executive financial/KPI dashboards in Community deployments) or custom
- **Status:** Not started (swimlanes); ERP dashboard re-scoping in progress

---

## SECTION 4 — REFINED AS-IS / TO-BE SUMMARY

### Swimlane production standards (all locked — do not deviate)
| Rule | Standard |
|------|----------|
| Diagram format | Browser-rendered HTML with SVG arrow overlay (SwimEngine v3.0) |
| Arrow orientation | Orthogonal only — no diagonals |
| Loop-back routing | Through left corridor (x=80); loopLeft label vertical on right side |
| Handover steps | Always two boxes in two lanes |
| END marker | In column of final acting party |
| Automated Odoo boxes | Must carry "AUTOMATED — NO USER ACTION" lime badge; badge count audited against box count |
| AS-IS Odoo references | Must be stripped entirely — no ERP mention in AS-IS diagrams |
| SVG fill syntax | `fill="#ffffff" fill-opacity="0.93"` — never `rgba()` |
| Ampersands in SVG | Must be `&amp;` or replaced with "and" |
| Arrow z-index | `z-index:9999` + `will-change:transform` |
| JS validation | `sed -n '/<script>/,/<\/script>/p' file.html \| grep -v '<script>' \| grep -v '</script>' > /tmp/check.js && node --check /tmp/check.js` |
| Workbook extraction | `openpyxl` with `data_only=True` |
| Sheet targets | AS-IS: `1_Refined_AS-IS`; TO-BE: `3_Detailed_TO-BE` |
| TO-BE step ID confirmation | Step IDs carry `-TO` suffix (e.g. `1.0A-TO`) |
| Circular RACI | Flagged and corrected before diagram production |
| Counterparties | Share ES/CEO lane — no standalone column unless owning an independent RACI step |
| Column order (TO-BE) | Initiating actor leftmost; Odoo System lane always rightmost |

### Gold-standard reference
A canonical gold-standard HTML swimlane file (NADF Legal P2 On-Lending TO-BE diagram) exists and was approved by the client. All new diagrams must visually match it. Claude Code should request this file from the outputs folder if not present in the repository.

---

## SECTION 5 — SWIMLANE REFERENCES

### Completed and approved swimlane files (Claude Desktop knowledge)
| Department | Files |
|-----------|-------|
| HR | HR-P1 through HR-P8 AS-IS + TO-BE (16 files) |
| Finance | FIN-P1 through FIN-P7 AS-IS + TO-BE (14 files) |
| Procurement | PROC-P1 through PROC-P6 AS-IS + TO-BE (12 files) |
| Administration | ADM all processes AS-IS + TO-BE |
| Project Coordination | NADF_PC_Process1 through Process5 AS-IS (v1.x) + TO-BE (v2.0) — 10 files |
| Legal | NADF_Legal_Process1–4 AS-IS; NADF_Legal_Process1–3 TO-BE (v2.0) — 7 files |

### File naming convention
`NADF_[Dept]_Process[N]_[ProcessName]_[ASIS/TOBE]_Swimlane_v[X.Y].html`

Examples:
- `NADF_PC_Process5_ProjectClosure_ASIS_Swimlane_v1.0.html`
- `NADF_Legal_Process1_ProcurementContracts_Swimlane_v2.0.html`

### Reference documents
- `NADF_SWIMLANE_MASTER_GUIDE.md` — canonical standards reference
- `NADF_BPOGS_Swimlane_Production_Manual_v2.0.docx` — 27-page onboarding manual
- `NADF_BPOGS_Examples_Section10_v2.0.docx` — worked examples
- `NADF_BPOGS_PendingActions_ClientClarifications.docx` — outstanding gaps

---

## SECTION 6 — ERP MAPPING (Odoo 17 Community Edition — corrected)

This section replaces all prior Enterprise-based module mappings. Every row follows the four-step resolution protocol where an Enterprise gap exists.

| Department | Requirement | Community Native | OCA Module | Custom Justified? |
|-----------|-------------|------------------|-----------|-------------------|
| Finance | Chart of accounts, vendor bills, invoicing | `account` (fully featured in CE) | — | No |
| Finance | Budget management/control | Partial via `account` analytic budgets | `account_budget_oca` (if richer budget control needed) | No |
| Finance | Executive financial dashboard | Basic `account` reporting views | `mis_builder` (OCA — the standard Community dashboard/KPI builder) | Only if `mis_builder` insufficient for NADF's specific KPI set |
| Finance | Two-factor authentication | Odoo CE supports TOTP-based 2FA natively (Settings → Users) | — | No |
| Procurement | Vendor management, RFQs, purchase orders | `purchase` (fully featured in CE) | — | No |
| Procurement | Multi-level approval workflow | Purchase order approval limits (native, basic) | `purchase_request` + `purchase_requisition` (OCA, for richer multi-step approval chains) | Only if OCA chain still insufficient for NADF's governance depth |
| Procurement | Vendor compliance / pre-qualification | Partial via `purchase` vendor records | OCA `partner_compliance` or similar vendor-vetting module (verify availability) | Possible — vendor compliance scoring is often NADF/government-specific |
| HR | Employee records, org chart | `hr` (fully featured in CE) | — | No |
| HR | Leave management | `hr_holidays` (CE leave module, fully featured) | — | No |
| HR | Recruitment | `hr_recruitment` (Community-native) | — | No |
| HR | Payroll | Odoo CE payroll is minimal/structure-only | OCA `payroll` (Salure or OCA `hr-payroll` repo) — still typically requires local customisation for Nigerian PAYE, pension, NHF | Yes — Nigerian statutory payroll customisation is justified |
| HR | Performance management | No CE native module | OCA `hr_appraisal` equivalent (verify current OCA repo state) | Possible |
| Administration | Fleet management | `fleet` (Community-native) | — | No |
| Administration | Asset management | `account_asset` (Community-native, basic) | OCA asset modules for richer depreciation schedules if needed | Possible, low priority |
| Administration | ICT helpdesk / ticketing | Odoo's native `helpdesk` app is **Enterprise-only** | OCA `helpdesk_mgmt` (Community alternative) | No — OCA module sufficient |
| Administration | Facility management | No CE native module | No mature OCA equivalent identified | Yes — custom lightweight facility request module justified |
| Administration | Fuel/energy tracking | Partial via `fleet` (fuel logs supported natively) | — | No |
| Project Coordination | Project/task management, milestones | `project` (fully featured in CE) | — | No |
| Legal | Contract lifecycle, document tracking | No dedicated CE contract module | OCA `contract` module (subscription/recurring contract management) — partial fit; or `documents`-style tracking via custom model | Possible — legal contract workflow has process-specific structure (RACI, sign-off chain) not matched by OCA `contract` |
| Legal | E-signature (if genuinely required) | No CE native e-sign | OCA has no direct Enterprise Sign equivalent; manual sign-off step is the default recommendation | Only if client mandates digital signature — would require third-party integration (e.g. DocuSign API), not Odoo-native |
| Strategy | Strategic plan tracking | No CE native module | Possible via `project` repurposed for strategic initiatives | Possible — to be assessed once Strategy workbooks are uploaded |
| Communications | Comms request tracking | No CE native module | Possible via `project` or `helpdesk_mgmt` repurposed | TBD pending workbook upload |
| Sustainable Agriculture | Programme/grant tracking | No CE native module | TBD | TBD pending workbook upload |
| Investment | Loan/investment portfolio management | No CE or OCA equivalent of sufficient depth identified | None identified | **Yes — custom module justified.** Investment/loan lifecycle (origination, disbursement, repayment schedule, portfolio reporting) is a core NADF function with no off-the-shelf Odoo CE/OCA fit |
| M&E | KPI dashboard, indicator tracking | No CE native module | `mis_builder` (OCA) for financial/operational KPIs; may not cover programme-level M&E indicators | Possible — programme M&E indicator framework may need custom extension on top of `mis_builder` |
| Executive Management | Executive dashboard | No CE native module | `mis_builder` (OCA) | Only if `mis_builder` cannot represent NADF's specific executive KPI set |

### Odoo system step pattern (TO-BE diagrams) — unchanged by platform correction
Every fully automated step in the TO-BE diagrams is a system action. These steps:
- Appear in the **Odoo System** lane
- Carry the lime "AUTOMATED — NO USER ACTION" badge
- Are sourced from the `3_Detailed_TO-BE` workbook sheet
- Are tagged with the `-TO` step ID suffix

This pattern is independent of CE vs Enterprise — it describes workflow automation logic, not licensing tier, and remains valid.

---

## SECTION 7 — APPROVAL FRAMEWORK (corrected for Community Edition)

### Multi-level approval principles (from TO-BE workbooks)
- All procurement above threshold requires multi-level approval
- Finance expenditure requires dual authorisation (initiating department + Finance)
- Legal contract execution requires LSU review + ES/CEO sign-off
- HR actions (appointments, separations, promotions) require HR + CEO approval
- Project milestone approvals require PM + Director sign-off

### Platform correction
The v1.0 package assumed the Enterprise `approvals` module would provide a generic cross-department approval engine. **This module is Enterprise-only and is not available under Odoo 17 Community Edition.**

**Corrected approach:**
1. **Procurement approvals** — use `purchase` order approval limits (native CE, role-based) combined with OCA `purchase_requisition` for structured multi-step requisition approval where the native limit mechanism is too shallow for NADF's governance depth.
2. **Finance approvals** — use `account` payment/invoice approval states (native CE workflow states: draft → confirmed → posted) combined with user group restrictions to enforce dual authorisation.
3. **HR approvals** — use `hr_holidays` and `hr_recruitment` native approval states; for appointments/separations without a dedicated CE workflow, a lightweight custom approval model attached to `hr.employee` is justified.
4. **Legal approvals** — manual sign-off step recorded in a custom contract-tracking model (see Section 6); no Enterprise Sign equivalent assumed.
5. **Project approvals** — `project` native task/milestone state transitions, restricted by user group.

### Audit trail
Odoo Community Edition includes native mail/log tracking (`mail.thread`) on most business documents, which provides a baseline audit trail without any Enterprise dependency. This should be the default audit mechanism unless a specific compliance requirement exceeds it.

---

## SECTION 8 — NADF CAPABILITY MAP

This is the master product structure. **Every roadmap item, milestone, and module decision must trace back to a capability in this map.** Each sub-capability is classified as: **Native Odoo** (CE core, no extra work) / **Configuration** (CE core, requires setup) / **OCA** (named community module) / **Custom Module** (bespoke development) / **Future Phase** (deferred beyond current programme scope).

### Finance
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Budget Management | Configuration | `account` analytic accounts/budgets |
| Payments | Native Odoo | `account` payment processing |
| Expenditure Control | Configuration | Approval states + user groups |
| Financial Reporting | Native Odoo | `account` native reports |
| Executive Financial Dashboard | OCA | `mis_builder` |
| Audit Trail | Native Odoo | `mail.thread` logging |
| Two-Factor Authentication | Configuration | Native TOTP 2FA |

### Procurement
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Vendor Management | Native Odoo | `purchase` partner records |
| Requisitions | OCA | `purchase_request` |
| RFQs | Native Odoo | `purchase` |
| Evaluations | Custom Module | No CE/OCA vendor scoring fit identified |
| Purchase Orders | Native Odoo | `purchase` |
| Contract Administration | OCA / Custom | `contract` (partial fit) or custom |
| Multi-level Approval | OCA | `purchase_requisition` approval chain |
| Vendor Compliance | Custom Module | Pre-qualification/compliance scoring |

### HR
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Employee Records | Native Odoo | `hr` |
| Leave | Native Odoo | `hr_holidays` |
| Recruitment | Native Odoo | `hr_recruitment` |
| Training | Future Phase | No current workbook requirement confirmed |
| Performance | OCA | Appraisal-equivalent module (verify) |
| Payroll | Custom Module | Nigerian statutory payroll on OCA base |
| Org Chart | Native Odoo | `hr` reporting hierarchy |

### Administration
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Fleet Management | Native Odoo | `fleet` |
| Asset Management | Native Odoo | `account_asset` |
| ICT Helpdesk | OCA | `helpdesk_mgmt` |
| Facility Management | Custom Module | No CE/OCA fit identified |
| Fuel/Energy Tracking | Native Odoo | `fleet` fuel logs |

### Project Coordination
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Project Initiation | Native Odoo | `project` |
| Project Planning | Native Odoo | `project` |
| Project Execution | Native Odoo | `project` tasks |
| Monitoring & Control | Native Odoo | `project` milestones/reporting |
| Project Closure | Native Odoo | `project` |

### Strategy & Planning
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Strategic Plan Tracking | OCA (tentative) | `project` repurposed; confirm post-workbook upload |
| Strategic KPI Monitoring | Custom (tentative) | Pending workbook upload |

### Legal Services Unit
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Contract Lifecycle | OCA / Custom | `contract` partial fit; custom likely needed for RACI/sign-off structure |
| Legal Advisory Tracking | Custom Module | No CE/OCA fit |
| Document Sign-off | Configuration | Manual sign-off workflow; no e-sign assumed |
| Compliance Tracking | Custom Module | No CE/OCA fit confirmed |

### Communications
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Comms Request Tracking | OCA (tentative) | `helpdesk_mgmt` or `project` repurposed |
| Public Relations Workflow | Future Phase | Pending workbook upload |

### Sustainable Agriculture
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Programme Tracking | Custom (tentative) | Pending workbook upload |
| Grant/Disbursement Tracking | Custom (tentative) | Likely overlaps with Investment capability |

### Investment
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Loan Origination | Custom Module | No CE/OCA fit |
| Disbursement Scheduling | Custom Module | No CE/OCA fit |
| Repayment Tracking | Custom Module | No CE/OCA fit |
| Portfolio Reporting | Custom Module | No CE/OCA fit |

### Monitoring & Evaluation
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Indicator Tracking | Custom Module | Programme-level M&E indicators |
| KPI Dashboard | OCA | `mis_builder` base, custom extension likely |

### Executive Management
| Sub-Capability | Classification | Notes |
|----------------|----------------|-------|
| Executive Dashboard | OCA | `mis_builder` |
| Cross-department Reporting | OCA / Custom | `mis_builder` base; custom roll-ups likely |

**Capability Map governance rule:** No module, no roadmap item, and no milestone may be created without a corresponding row in this map. If a new requirement emerges that does not map to an existing sub-capability, the Capability Map must be updated first, before backlog or milestone entries are created.

---

## SECTION 9 — PUBLIC SECTOR TEMPLATE REGISTRY

Every capability and requirement is classified by reusability, to guide future template extraction (see Section 13, Product Hierarchy). Three categories are used: **Public Sector Core** (reusable across any government agency), **Agriculture Agency Extensions** (reusable across agriculture-sector agencies specifically), **NADF Specific** (not reusable — tied to NADF's identity, people, or data).

| Item | Classification | Category |
|------|---------------|----------|
| Procurement approval workflow (multi-level, threshold-based) | Reusable | Public Sector Core |
| Vendor compliance/pre-qualification management | Reusable | Public Sector Core |
| Government chart of accounts structure | Reusable | Public Sector Core |
| HR leave workflows | Reusable | Public Sector Core |
| HR recruitment workflow | Reusable | Public Sector Core |
| Approval matrices (Finance, Procurement, HR) | Reusable | Public Sector Core |
| Executive dashboard structure (`mis_builder` config pattern) | Reusable | Public Sector Core |
| Two-factor authentication policy | Reusable | Public Sector Core |
| Fleet/asset management configuration | Reusable | Public Sector Core |
| ICT helpdesk configuration (`helpdesk_mgmt`) | Reusable | Public Sector Core |
| Audit trail / mail.thread logging pattern | Reusable | Public Sector Core |
| Swimlane diagram methodology (SwimEngine, workbook structure) | Reusable | Public Sector Core |
| Grant/programme disbursement tracking pattern | Reusable (structure only) | Agriculture Agency Extensions |
| Loan/investment portfolio module (structure, not data) | Reusable (structure only) | Agriculture Agency Extensions |
| Agricultural programme M&E indicator framework | Reusable (structure only) | Agriculture Agency Extensions |
| Sustainable Agriculture programme workflow | Reusable (structure only) | Agriculture Agency Extensions |
| NADF organisational hierarchy (4-level structure) | Not reusable | NADF Specific |
| NADF staff names, roles, and personal data | Not reusable | NADF Specific |
| NADF vendor data and history | Not reusable | NADF Specific |
| NADF-specific RACI assignments (named individuals/titles) | Not reusable | NADF Specific |
| NADF branding (navy/gold report design, logos) | Not reusable | NADF Specific |
| NADF loan/investment portfolio data | Not reusable | NADF Specific |

**Registry governance rule:** Every custom module and every configuration pattern produced during the NADF engagement must be assessed against this registry at the point of completion and tagged accordingly. Items tagged "Public Sector Core" or "Agriculture Agency Extensions" are candidates for extraction into the Public Sector ERP Template (Section 13). Items tagged "NADF Specific" remain in the NADF deployment only and must never be included in template extraction.

---

## SECTION 10 — PRODUCT BACKLOG (SUMMARY)

Full backlog detail belongs in `docs/PRODUCT_BACKLOG.md` in the repository. Summary by category, restated under the corrected Community Edition platform:

| Category | Items | Done | In Progress | Not Started | Blocked |
|----------|-------|------|------------|-------------|---------|
| Swimlane diagrams (all depts) | ~120 | ~55 | 2 | ~65 | 2 |
| Odoo CE core configuration | ~20 | ~10 | ~6 | ~4 | 0 |
| OCA module integration | ~10 | 0 | ~2 | ~8 | 0 |
| Custom modules | ~8 | 0 | 0 | ~8 | 0 |
| Reporting/dashboards (mis_builder-based) | 5 | 0 | 1 | 4 | 0 |
| Security/access rights | 4 | 0 | 2 | 2 | 0 |
| Cross-functional workflows | 3 | 0 | 0 | 3 | 0 |
| UAT/deployment | 3 | 0 | 1 | 2 | 0 |
| Capability Map maintenance | Ongoing | — | 1 (this regeneration) | — | — |
| Template extraction tagging | ~22 (registry items) | 0 | 1 (registry created) | ~21 | 0 |

**Backlog correction note:** Any backlog item previously referencing an Enterprise module (Approvals, Documents, Sign, Spreadsheet, Knowledge, Studio, Payroll) must be re-written against the Section 6 ERP Mapping before further work proceeds. Claude Code must treat this as a mandatory backlog reconciliation task at the start of the next session.

---

## SECTION 11 — PRODUCT ROADMAP

### Phase 0 — Engagement Setup ✅ COMPLETE
- Workbook framework established
- Master guide and onboarding manual produced
- Swimlane construction standards locked
- **Now also includes:** Platform correction to Odoo 17 Community Edition; Capability Map v1 produced; Public Sector Template Registry v1 produced

### Phase 1 — Business Process Documentation 🔄 IN PROGRESS (~45%)
- All 12 departments mapped AS-IS + Detailed TO-BE
- All swimlane HTML files produced and approved
- Pending actions document maintained
- **Active:** Legal Services Unit (P5 AS-IS; P4–P6 TO-BE)
- **Next:** Strategy & Planning (P1–P5 AS-IS + TO-BE)
- **Queued:** Communications, Sustainable Agriculture, Investment, M&E, Executive Management

### Phase 2 — Odoo Community Edition Configuration & OCA Integration 🔄 IN PROGRESS (re-scoped)
- Finance, Procurement, HR, Admin: Core CE modules in progress under corrected mapping
- OCA modules to be evaluated and installed per Section 6/8 (`mis_builder`, `helpdesk_mgmt`, `purchase_requisition`, payroll OCA base)
- Project Coordination: Pending
- Legal, Strategy, remaining depts: Pending TO-BE completion
- **Re-scoping action required:** Audit current Odoo instance for any Enterprise module assumptions made before this correction and remove/replace them

### Phase 2.5 — Custom Module Development (new phase, platform-driven)
- Investment/Loan portfolio module (justified — no CE/OCA fit)
- Legal contract lifecycle module (justified — partial OCA fit only)
- Facility management module (justified — no CE/OCA fit)
- Vendor compliance/evaluation module (justified — no CE/OCA fit)
- Nigerian statutory payroll customisation on OCA payroll base (justified)
- M&E indicator framework extension on `mis_builder` (justified)

### Phase 3 — UAT & Super User Training ⏳ NOT STARTED
- Full UAT cycle, re-run against corrected CE + OCA + custom module set
- Super User Acceptance Testing
- Training documentation

### Phase 4 — Production Deployment ⏳ NOT STARTED
- Go-live
- Cutover plan
- Data migration validation

### Phase 5 — Hypercare & Template Extraction ⏳ NOT STARTED
- Post-go-live stabilisation
- **Public Sector ERP Template extraction** — using the Template Registry (Section 9) to extract "Public Sector Core" and "Agriculture Agency Extensions" items into a reusable Software Factory template (see Section 13)

---

## SECTION 12 — MILESTONE PLAN

| ID | Milestone | Status | Dependency |
|----|-----------|--------|-----------|
| M-PLATFORM-CORRECTION | Audit Odoo instance for Enterprise module assumptions; document corrected module list | ⏳ Urgent — first new milestone | Repository/Odoo discovery (Section 17) |
| M-CAPMAP-01 | Capability Map v1 ratified by client | 🔄 Drafted in this package — awaiting client review | — |
| M-TEMPLATE-REG-01 | Public Sector Template Registry v1 ratified | 🔄 Drafted in this package — awaiting client review | — |
| M-LSU-05 | Legal P5 AS-IS + P4–P6 TO-BE | 🔄 Active | — |
| M-STR-01 | Strategy P1–P5 AS-IS + TO-BE | ⏳ Next | Legal complete + workbooks uploaded |
| M-COM-01 | Communications all processes | ⏳ | Strategy complete |
| M-SA-01 | Sustainable Agriculture all processes | ⏳ | — |
| M-INV-01 | Investment all processes + custom module scoping | ⏳ | — |
| M-ME-01 | M&E all processes + `mis_builder` extension scoping | ⏳ | — |
| M-EXEC-01 | Executive Management all processes | ⏳ | — |
| M-ERP-PC | Project Coordination Odoo config | ⏳ | M-PC-05 done ✅ |
| M-OCA-01 | Install and configure `mis_builder`, `helpdesk_mgmt`, `purchase_requisition` | ⏳ | M-PLATFORM-CORRECTION |
| M-CUSTOM-01 | Investment/Loan custom module — design spec | ⏳ | M-INV-01 |
| M-CUSTOM-02 | Legal contract lifecycle custom module — design spec | ⏳ | M-LSU-TO-06 |
| M-UAT-01 | Full UAT cycle (corrected platform) | ⏳ | Phase 2 + 2.5 complete |
| M-DEPLOY-01 | Production go-live | ⏳ | UAT passed |
| M-TEMPLATE-EXTRACT-01 | First Public Sector ERP Template extraction pass | ⏳ | M-DEPLOY-01 |

---

## SECTION 13 — GOVERNANCE REQUIREMENTS

### Repository governance (Claude Code must implement and maintain)
- Git branching: feature branch per milestone; PRs required before merge to `main`
- Branch protection on `main`: no direct push; PR + at least one review required
- CI workflows: lint, `pylint` on custom modules, Odoo module manifest validation on each PR
- Commit message format: `[DEPT-MILESTONE] Brief description` (e.g. `[LSU-M05] Complete Legal P5 AS-IS swimlane`)
- All control documents updated and committed before any milestone branch is merged to `main`
- No milestone is closed until `docs/MILESTONE_REGISTER.md`, `docs/CONTROL_TOWER.md`, and `CHANGELOG.md` are updated in the same commit

### Document governance (seven mandatory files)
| File | When updated |
|------|-------------|
| `docs/CONTROL_TOWER.md` | After every milestone |
| `docs/PRODUCT_BACKLOG.md` | Every session (statuses) |
| `docs/MILESTONE_REGISTER.md` | On milestone completion |
| `docs/IMPLEMENTATION_HISTORY.md` | Entry added per milestone |
| `docs/DECISION_LOG.md` | Entry added per decision |
| `CHANGELOG.md` | Every session |
| `docs/session_logs/YYYY-MM-DD_SESSION_SUMMARY.md` | Created every session |

### Backup governance
- Odoo database backup status: unknown — Claude Code must verify and establish a documented schedule during discovery
- Minimum acceptable backup: daily automated backup of Odoo PostgreSQL database with documented restore test
- Repository backup: GitHub remote (verify remote is set; verify last push was successful)

### OCA module governance
- Only OCA modules from the official Odoo Community Association GitHub (`github.com/OCA`) may be installed without explicit user approval
- Each OCA module installed must be logged in `docs/DECISION_LOG.md` with rationale and version pinned
- OCA modules must be version-pinned in `requirements.txt` or equivalent to prevent uncontrolled upgrades

### Custom module governance
- Each custom module requires a design spec document before development begins: `docs/modules/[MODULE_NAME]_spec.md`
- Spec must include: purpose, capability map reference, data model, business rules, UI/UX description, test cases, acceptance criteria
- Custom modules are stored in the repository `addons/` or `custom_addons/` directory (Claude Code to verify actual path during discovery)
- All custom modules must carry the `NADF_` prefix and include a `__manifest__.py` with `author`, `version`, `license`, `depends` fully populated

---

## SECTION 14 — GOVERNANCE ACTIVATION GATE

**No new Software Factory project may begin implementation until all gates pass.** This gate must be run at the start of every new project — and re-run for NADF during the M-PLATFORM-CORRECTION milestone.

Claude Code must produce a `GOVERNANCE_GATE_REPORT.md` after running all checks. Output must be explicit PASS or FAIL per criterion.

### Gate A — Repository
| Check | Pass Criterion |
|-------|---------------|
| Git initialised | `git status` returns a valid repo |
| Remote configured | `git remote -v` shows a remote URL |
| `main` branch exists | `git branch` lists `main` |
| Feature branch workflow in use | At least one non-`main` branch exists or PR history exists |

### Gate B — GitHub
| Check | Pass Criterion |
|-------|---------------|
| Branch protection on `main` | Verified via `gh repo view` or GitHub UI |
| PR workflow enabled | PRs can be created; direct push to `main` is blocked |
| CI configured | `.github/workflows/` contains at least one workflow file |

### Gate C — Governance Documents
| Check | Pass Criterion |
|-------|---------------|
| Control Tower exists | `docs/CONTROL_TOWER.md` is present and populated |
| Product Backlog exists | `docs/PRODUCT_BACKLOG.md` is present and populated |
| Milestone Register exists | `docs/MILESTONE_REGISTER.md` is present and populated |
| Decision Log exists | `docs/DECISION_LOG.md` is present and populated |
| Changelog exists | `CHANGELOG.md` is present and populated |
| Product State Index exists | `docs/PRODUCT_STATE_INDEX.md` is present and populated |

### Gate D — Backup
| Check | Pass Criterion |
|-------|---------------|
| Backup strategy documented | `docs/BACKUP_STRATEGY.md` exists and describes schedule + storage location |
| Restore strategy documented | Same document includes a restore procedure |
| Last backup confirmed | Backup file exists and timestamp is within 24 hours |

### Gate E — Product
| Check | Pass Criterion |
|-------|---------------|
| Capability Map completed | Section 8 (this document) or a standalone `docs/CAPABILITY_MAP.md` exists and covers all departments |
| Product Roadmap completed | Section 11 (this document) or `docs/NADF_PRODUCT_ROADMAP.md` exists |
| Platform confirmed | `docs/DECISION_LOG.md` contains an entry confirming Odoo 17 Community Edition |

### Gate result format
```
GOVERNANCE ACTIVATION GATE REPORT
===================================
Date: YYYY-MM-DD
Project: NADF ERP Programme

Gate A — Repository
  Git initialised:          PASS
  Remote configured:        PASS / FAIL — [URL or reason]
  main branch exists:       PASS / FAIL
  Feature branch workflow:  PASS / FAIL

Gate B — GitHub
  Branch protection:        PASS / FAIL
  PR workflow:              PASS / FAIL
  CI configured:            PASS / FAIL — [workflow file names or NONE]

Gate C — Governance Documents
  Control Tower:            PASS / FAIL
  Product Backlog:          PASS / FAIL
  Milestone Register:       PASS / FAIL
  Decision Log:             PASS / FAIL
  Changelog:                PASS / FAIL
  Product State Index:      PASS / FAIL

Gate D — Backup
  Strategy documented:      PASS / FAIL
  Restore procedure:        PASS / FAIL
  Last backup confirmed:    PASS / FAIL — [timestamp or UNKNOWN]

Gate E — Product
  Capability Map:           PASS / FAIL
  Product Roadmap:          PASS / FAIL
  Platform confirmed:       PASS / FAIL

OVERALL RESULT: PASS / FAIL (n/n checks passed)

BLOCKERS (if any):
  [List each FAIL with required action]
```

---

## SECTION 15 — PRODUCT MEMORY SYSTEM

The NADF ERP product must not live inside a chat window. It must live inside the repository. Any future AI instance, developer, project manager, or operator must be able to inspect the repository and understand: what has been built, why it was built, what remains, and what to do next.

### Core memory files (all in `docs/`)
| File | Purpose | Authority |
|------|---------|-----------|
| `PRODUCT_STATE_INDEX.md` | Session initialisation sequence — what to read first | Entry point |
| `CONTROL_TOWER.md` | Current phase, milestone, blockers, risks, next 5 actions | Current state |
| `PRODUCT_BACKLOG.md` | All work items, priorities, statuses | Pending work |
| `MILESTONE_REGISTER.md` | Milestone history and upcoming milestone queue | Completed work |
| `DECISION_LOG.md` | All major product and architecture decisions | Decisions |
| `IMPLEMENTATION_HISTORY.md` | Chronological record of every completed milestone | History |
| `CHANGELOG.md` (root) | Programme-level changelog | Changes |

### New addition: NEXT_ACTION.md

Create `docs/NEXT_ACTION.md`. This file is the fastest possible answer to: **"What should we do next?"**

It must be a single, short, always-current file — maximum one page. Updated at the end of every session before any other file.

Required content:
```markdown
# NADF ERP — Next Action

**Last updated:** YYYY-MM-DD

## Current Phase
Phase [N] — [Phase Name]

## Current Department
[Department name] — [brief status]

## Current Milestone
[Milestone ID] — [Milestone name]

## Current Blocker (if any)
[Blocker description, or "None"]

## Next Recommended Action
[One paragraph — what Claude Code should do in the very next session. Specific, actionable, unambiguous.]

## Files to read before starting
1. [file path]
2. [file path]
3. [file path]
```

`NEXT_ACTION.md` must be the **first file read** at the start of every new Claude Code session — before even `CONTROL_TOWER.md`. It provides the immediate answer; the other files provide the context.

### Mandatory update sequence (end of every session)
1. `docs/NEXT_ACTION.md` — update first
2. `docs/CONTROL_TOWER.md`
3. `docs/PRODUCT_BACKLOG.md`
4. `docs/MILESTONE_REGISTER.md`
5. Relevant department status file
6. `docs/IMPLEMENTATION_HISTORY.md`
7. `docs/DECISION_LOG.md` (if any decision was made)
8. `CHANGELOG.md`
9. `docs/session_logs/YYYY-MM-DD_SESSION_SUMMARY.md`

No session is complete until all nine files are updated and committed.

---

## SECTION 16 — CONTROL TOWER STRUCTURE

The repository memory scaffold (delivered as `NADF_ERP_ControlTower_RepoScaffold_2026-06-16.zip`) must be placed in the repository root and updated to include `NEXT_ACTION.md`. Full directory structure:

```
[repo root]/
├── CHANGELOG.md
├── docs/
│   ├── PRODUCT_STATE_INDEX.md       ← Mandatory first read each session
│   ├── NEXT_ACTION.md               ← What to do next (new — add this)
│   ├── CONTROL_TOWER.md             ← Programme cockpit
│   ├── PRODUCT_BACKLOG.md           ← All work items
│   ├── MILESTONE_REGISTER.md        ← Milestone history + queue
│   ├── DECISION_LOG.md              ← All decisions
│   ├── IMPLEMENTATION_HISTORY.md    ← Completed milestone records
│   ├── CAPABILITY_MAP.md            ← (extract from Section 8 if desired as standalone)
│   ├── GOVERNANCE_GATE_REPORT.md    ← Gate result (created by Claude Code)
│   ├── BACKUP_STRATEGY.md           ← (create during discovery)
│   ├── NADF_PRODUCT_ROADMAP.md      ← (extract from Section 11 if desired as standalone)
│   ├── departments/
│   │   └── status/
│   │       ├── legal_status.md
│   │       ├── hr_status.md
│   │       ├── finance_status.md
│   │       ├── procurement_status.md
│   │       ├── admin_status.md
│   │       ├── project_coordination_status.md
│   │       ├── strategy_status.md
│   │       ├── communications_status.md
│   │       ├── sustainable_agriculture_status.md
│   │       ├── investment_status.md
│   │       ├── me_status.md
│   │       └── executive_management_status.md
│   ├── modules/
│   │   └── [MODULE_NAME]_spec.md   ← One per custom module (created before dev begins)
│   └── session_logs/
│       └── YYYY-MM-DD_SESSION_SUMMARY.md
```

---

## SECTION 17 — DISCOVERY REQUIREMENTS FOR CLAUDE CODE

Claude Code must complete ALL of the following before any implementation. No exceptions.

### Step 1 — Repository discovery
```bash
# Confirm repo location
ls /Users/mac/nadf_erp

# Git status and recent history
cd /Users/mac/nadf_erp && git status && git log --oneline -20

# GitHub remote
git remote -v

# Existing branches
git branch -a

# Existing governance docs
ls docs/ 2>/dev/null || echo "docs/ not found"

# Existing custom modules
ls addons/ 2>/dev/null || ls custom_addons/ 2>/dev/null || echo "No addons dir found"

# Existing config files
ls *.conf 2>/dev/null && cat *.conf | grep addons_path
```

### Step 2 — GitHub governance check
```bash
# Requires GitHub CLI (gh)
gh repo view --json defaultBranchRef,branchProtectionRules
ls .github/workflows/ 2>/dev/null || echo "No CI workflows found"
```

### Step 3 — Odoo discovery
```bash
# Odoo version
python3 /Users/mac/odoo17/odoo-bin --version 2>/dev/null

# Odoo config / addons path
find /Users/mac/odoo17 -name "*.conf" 2>/dev/null | head -5
grep -i addons_path /Users/mac/odoo17/*.conf 2>/dev/null

# Database name
psql -U odoo -l 2>/dev/null | grep -i nadf

# Installed modules — run in psql
# psql -U odoo -d [DB_NAME] -c "SELECT name, state FROM ir_module_module WHERE state='installed' ORDER BY name;"

# CRITICAL: Check for any Enterprise modules currently installed
# psql -U odoo -d [DB_NAME] -c "SELECT name FROM ir_module_module WHERE state='installed' AND name IN ('approvals','documents','sign','web_studio','knowledge','hr_payroll','spreadsheet_dashboard','documents_spreadsheet');"
```

### Step 4 — Backup check
```bash
ls ~/odoo_backups/ 2>/dev/null || ls /var/backups/odoo/ 2>/dev/null || echo "No backup dir found"
```

### Step 5 — Discovery report format

After all checks, Claude Code must produce this report before touching anything:

```
NADF ERP — DISCOVERY REPORT
============================
Date: YYYY-MM-DD

REPOSITORY
  Path confirmed:          YES / NO — [actual path]
  Git status:              [clean / uncommitted changes]
  Current branch:          [branch name]
  GitHub remote:           [URL / not configured]
  Branch protection:       [YES / NO / UNKNOWN]
  CI workflows:            [file names / NONE]
  Governance docs present: [list what exists / NONE]
  Custom addons path:      [path / not found]

ODOO INSTANCE
  Odoo version:            [version / not found]
  Community vs Enterprise: [CE / EE / UNKNOWN]
  Database name:           [name / not found]
  Enterprise modules found:[list / NONE — this is the critical platform check]
  OCA modules installed:   [list / NONE]
  Addons path:             [path]

BACKUP
  Backup dir found:        [YES/NO — path]
  Last backup timestamp:   [timestamp / UNKNOWN]
  Restore procedure:       [documented / not documented]

GOVERNANCE GATE (preliminary)
  Gate A (Repo):           PASS / FAIL
  Gate B (GitHub):         PASS / FAIL
  Gate C (Docs):           PASS / FAIL
  Gate D (Backup):         PASS / FAIL
  Gate E (Product):        PASS / FAIL

CRITICAL ALERTS
  [List anything requiring immediate attention — especially Enterprise modules found]

RECOMMENDED FIRST ACTION
  [One specific action]
```

Only after this report is reviewed and confirmed by the user may Claude Code proceed to any implementation work.

---

## SECTION 18 — IMPLEMENTATION SEQUENCE

After discovery and governance gate:

1. **M-PLATFORM-CORRECTION** — Audit Odoo instance for any Enterprise modules currently installed; document findings; produce corrected module list; update `docs/DECISION_LOG.md` with platform confirmation entry; update all backlog items that referenced Enterprise modules
2. **Commit repo scaffold** — place `docs/` structure from transfer package into repo; create `docs/NEXT_ACTION.md`; commit to `main` as `[SETUP] Add repository control tower v2 and governance scaffold`
3. **Governance Gate Report** — run all five gates; produce `docs/GOVERNANCE_GATE_REPORT.md`; fix all FAILs before proceeding
4. **M-LSU-05** — Legal P5 AS-IS + P4–P6 TO-BE swimlanes (active Claude Desktop milestone)
5. **M-STR-01** — Strategy P1–P5 AS-IS + TO-BE (requires workbook upload)
6. **Remaining departments** — Communications → Sustainable Agriculture → Investment → M&E → Executive Management
7. **M-OCA-01** — Install and configure `mis_builder`, `helpdesk_mgmt`, `purchase_requisition`; log each in Decision Log
8. **M-ERP-PC** — Project Coordination Odoo `project` module configuration
9. **M-CUSTOM-01** — Investment/Loan custom module design spec then development
10. **M-CUSTOM-02** — Legal contract lifecycle custom module design spec then development
11. **Remaining custom modules** — Facility management, vendor compliance, Nigerian payroll extension, M&E extension
12. **M-UAT-01** — Full UAT cycle
13. **M-DEPLOY-01** — Production go-live
14. **M-TEMPLATE-EXTRACT-01** — Public Sector ERP Template extraction

---

## SECTION 19 — SESSION START RULES

At the start of every new Claude Code session, read files in this exact order:

1. `docs/NEXT_ACTION.md` — immediate answer: what to do
2. `docs/PRODUCT_STATE_INDEX.md` — full initialisation sequence
3. `docs/CONTROL_TOWER.md` — current phase, milestone, blockers
4. `docs/PRODUCT_BACKLOG.md` — work item statuses
5. `docs/MILESTONE_REGISTER.md` — milestone context
6. Current department status file (`docs/departments/status/`)
7. Latest `docs/IMPLEMENTATION_HISTORY.md`
8. Latest `CHANGELOG.md`
9. Run `git status` + `git log --oneline -10`

Then state explicitly before beginning any work:
- Current phase
- Current milestone
- Current blockers
- Next recommended action

**Do not begin work until this state is confirmed.**

---

## SECTION 20 — SESSION END RULES

At the end of every Claude Code session, complete all nine steps in order:

1. Update `docs/NEXT_ACTION.md` — write exactly what the next session should do
2. Update `docs/CONTROL_TOWER.md` — current phase, milestone, completion %, blockers
3. Update `docs/PRODUCT_BACKLOG.md` — change statuses for all items touched this session
4. Update `docs/MILESTONE_REGISTER.md` — mark any completed milestones
5. Update relevant department status file
6. Update `docs/IMPLEMENTATION_HISTORY.md` — add entry for completed milestone(s)
7. Update `docs/DECISION_LOG.md` — add entry for any decision made this session
8. Update `CHANGELOG.md` — add session summary entry
9. Create `docs/session_logs/YYYY-MM-DD_SESSION_SUMMARY.md` with:
   - Work completed
   - Files changed
   - Tests run
   - Git status (branch, commits pushed)
   - Pending work
   - Risks identified
   - Next recommended action

Commit all nine files in a single commit: `[SESSION-END] YYYY-MM-DD governance update`

**No milestone is closed until all nine files are updated and the commit is pushed.**

---

## SECTION 21 — CLAUDE DESKTOP / CLAUDE CODE BOUNDARY

This boundary is non-negotiable and must be respected at all times.

| Responsibility | Claude Desktop | Claude Code |
|---------------|----------------|-------------|
| Business process materials (workbooks, BPOGS outputs) | ✅ Primary | Read-only via transfer package |
| Swimlane diagram production (HTML files) | ✅ Primary | No |
| ERP mapping and requirements analysis | ✅ Primary | Executes based on this package |
| Transfer package creation and maintenance | ✅ Primary | Receives and loads |
| Local repository (`/Users/mac/nadf_erp`) | ❌ No access | ✅ Primary |
| Odoo instance (`/Users/mac/odoo17`) | ❌ No access | ✅ Primary |
| GitHub remote, PRs, CI | ❌ No access | ✅ Primary |
| Odoo database | ❌ No access | ✅ Primary |
| Custom module development | ❌ No | ✅ Primary |
| Control document commits to repo | Provides content | Commits to repo |
| Git history inspection | ❌ Cannot inspect | ✅ Primary |

### What Claude Desktop may claim
Claude Desktop may only state:
> *"Based on the NADF project materials available in this Claude Desktop project folder…"*

### What Claude Desktop must never claim
Claude Desktop must never claim to have inspected:
- `/Users/mac/nadf_erp` or any local repository path
- `/Users/mac/odoo17` or any local Odoo installation
- The GitHub repository state, branch protection, CI, or PRs
- The Odoo database, installed modules, or running instance
- Local addons, configs, or Git history

unless the user has explicitly pasted that information into the project folder or current conversation.

### Transfer mechanism
The transfer package (`NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.md`) is the only sanctioned channel from Claude Desktop to Claude Code. When a new Claude Code session begins, this document is pasted in full. Claude Code then runs discovery (Section 17) and converts this package into repository memory.

---

*End of NADF Full Product Transfer Package v2.0 — 2026-06-19*  
*Prepared by Claude Desktop from NADF BPOGS project folder materials only.*  
*This document is authoritative. Supersedes all prior versions.*
