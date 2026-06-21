# WORK_PACKAGES.md
## NADF ERP Programme — Execution Units for Claude Code

**Document type:** Operational — derived from NADF Full Product Transfer Package v2.1  
**Last updated:** 2026-06-21 (coverage closure — omissions 1–9 and reductions 1–3 addressed)  
**Authority:** NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md  
**Purpose:** Each work package is a discrete, executable unit of implementation work for Claude Code or the Software Factory Autonomous Agent Team

---

## Complexity Classification
- **Small:** Single-concern configuration or setup; low risk; 1–2 actions
- **Medium:** Multi-step configuration; 3–6 actions; moderate risk
- **Large:** Multiple interacting components; 7–12 actions; requires design decision
- **Very Large:** Custom module development or cross-department integration; requires approved spec; significant testing

---

## PHASE 0 — GOVERNANCE REMEDIATION

---

### WP-GOV-01 — Repository and Odoo Discovery
**Backlog items:** BL-GOV-01, BL-GOV-02  
**Phase:** 0  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Produce a complete, accurate picture of the current state of the repository and Odoo instance before any implementation work begins.

**Scope:**
- Confirm repository path, Git status, current branch, and commit history
- Confirm GitHub remote configuration
- Confirm Odoo version and Community vs Enterprise edition
- Identify all installed Odoo modules — flag any Enterprise-only modules
- Identify any existing custom modules
- Confirm database name and accessibility
- Check backup directory and last backup timestamp

**Dependencies:** Repository access; Odoo instance access

**Deliverables:**
- Discovery Report (formatted per Transfer Package v2.1 Section 15 template)
- List of any Enterprise modules found — with remediation recommendation

**Acceptance Criteria:**
- Discovery Report covers all fields in the standard template
- Enterprise module presence confirmed or denied with evidence (database query result)
- Report committed to `docs/` or presented to user before proceeding

**Governance Reviews Required:** User review of Discovery Report before WP-GOV-02 begins

---

### WP-GOV-02 — Platform Audit and Correction
**Backlog items:** BL-GOV-02, BL-GOV-08  
**Phase:** 0  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Formally confirm Odoo 17 Community Edition as the platform; remove or document any Enterprise modules; log the platform decision.

**Scope:**
- Review Discovery Report Enterprise module findings
- If Enterprise modules found: produce removal/replacement plan per Transfer Package v2.1 Section 6 ERP Mapping
- Log platform decision in `docs/DECISION_LOG.md` as DEC-PLATFORM-001
- Update any backlog items that referenced Enterprise modules — rewrite against CE/OCA equivalents

**Dependencies:** WP-GOV-01 completed and Discovery Report reviewed

**Deliverables:**
- `docs/DECISION_LOG.md` entry DEC-PLATFORM-001
- Enterprise module remediation plan (if applicable)
- Updated backlog items (if applicable)

**Acceptance Criteria:**
- DEC-PLATFORM-001 logged with date, decision, rationale, impact fields populated
- No backlog item references a blocked Enterprise module
- Remediation plan produced if any Enterprise modules were found

**Governance Reviews Required:** User sign-off on remediation plan (if Enterprise modules found)

---

### WP-GOV-03 — Governance Activation Gate
**Backlog items:** BL-GOV-03, BL-GOV-05, BL-GOV-06, BL-GOV-07  
**Phase:** 0  
**Complexity:** Large  
**Status:** Not Started

**Objective:** Run all five Governance Gates; fix all FAILs; certify the programme is ready for implementation.

**Scope:**
- Run Gate A (Repository): Git, remote, main branch, feature branch workflow
- Run Gate B (GitHub): branch protection, PR workflow, CI workflow
- Run Gate C (Governance Documents): all seven control documents present and populated
- Run Gate D (Backup): strategy documented, restore procedure documented, last backup confirmed
- Run Gate E (Product): capability map present, platform confirmed, no Enterprise modules
- Fix each FAIL — enable branch protection, create CI workflow, create `BACKUP_STRATEGY.md`, etc.
- Re-run gates after fixes
- Produce `docs/GOVERNANCE_GATE_REPORT.md`

**Dependencies:** WP-GOV-01, WP-GOV-02

**Deliverables:**
- `docs/GOVERNANCE_GATE_REPORT.md` — all five gates PASS
- `docs/BACKUP_STRATEGY.md` — daily schedule and restore procedure
- `.github/workflows/ci.yml` — basic CI workflow (lint + module manifest check)
- GitHub branch protection confirmed active

**Acceptance Criteria:**
- All 20 gate checks: PASS
- `GOVERNANCE_GATE_REPORT.md` committed to repository
- No FAILs remaining

**Governance Reviews Required:** User review of Gate Report before Phase 1 begins

---

### WP-GOV-04 — Repository Scaffold Commit
**Backlog items:** BL-GOV-04  
**Phase:** 0  
**Complexity:** Small  
**Status:** Not Started

**Objective:** Extract and commit the full repository governance scaffold to the repository.

**Scope:**
- Extract `NADF_ERP_ControlTower_RepoScaffold_v2.1_2026-06-20.zip` into repository root
- Update `docs/CONTROL_TOWER.md` with actual Git branch, Odoo DB name, backup status from Discovery Report
- Update `docs/NEXT_ACTION.md` to reflect current state post-discovery
- Add session start and end rules to `docs/PRODUCT_STATE_INDEX.md` (from Transfer Package v2.1 Sections 17 and 18) so they are permanently in-repo and available to any future session without requiring the transfer package
- Commit all scaffold files: `[SETUP] Add repository control tower v2.1 and governance scaffold`
- Push to GitHub remote

**Dependencies:** WP-GOV-03 (at least Gate A and Gate B passing)

**Deliverables:**
- All scaffold documents committed and pushed
- `docs/NEXT_ACTION.md` current
- Session start/end rules committed to `docs/PRODUCT_STATE_INDEX.md`

**Acceptance Criteria:**
- `git log` confirms scaffold commit on main
- `git push` successful
- All 7 governance documents present in `docs/`
- Session rules present in `docs/PRODUCT_STATE_INDEX.md`

**Governance Reviews Required:** None — routine commit

---

## PHASE 1 — FOUNDATION

---

### WP-OCA-01 — OCA Module Installation
**Backlog items:** BL-OCA-01 to BL-OCA-06  
**Phase:** 1  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Install, verify, and version-pin all required OCA modules for Phase 1.

**Scope:**
- Verify Odoo 17 compatibility for each module before installation: `mis_builder`, `account_budget_oca`, `purchase_request`, `purchase_requisition`, `helpdesk_mgmt`
- Install each module into the Odoo instance
- Pin each module version in `requirements.txt` or equivalent
- Log each installation in `docs/DECISION_LOG.md` with module name, version, source URL, rationale
- Confirm modules appear in installed state in Odoo database

**Dependencies:** WP-GOV-03 (Governance Gate passed)

**Deliverables:**
- Five OCA modules installed and active
- `requirements.txt` updated with pinned versions
- Five Decision Log entries (one per module)

**Acceptance Criteria:**
- `SELECT name, state FROM ir_module_module WHERE name IN ('mis_builder', 'account_budget_oca', 'purchase_request', 'purchase_requisition', 'helpdesk_mgmt') AND state='installed';` returns 5 rows
- Each module listed in `docs/DECISION_LOG.md`

**Governance Reviews Required:** None — routine installation with logging

---

### WP-FIN-01 — Finance Core Configuration
**Backlog items:** BL-FIN-01, BL-FIN-02, BL-FIN-03, BL-FIN-08  
**Phase:** 1  
**Complexity:** Large  
**Status:** In Progress

**Objective:** Configure the complete Finance accounting operation in Odoo.

**Scope:**
- Configure chart of accounts to NADF government structure
- Configure vendor bill workflow (draft → confirmed → posted)
- Configure payment workflow with dual-authorisation enforcement (restrict payment posting to Finance Manager group)
- Configure and verify native `account` financial reports: trial balance, profit & loss, balance sheet
- Verify `mail.thread` audit trail active on `account.move` and `account.payment`

**Dependencies:** WP-GOV-03, WP-OCA-01 (for `account_budget_oca`)

**Deliverables:**
- Chart of accounts configured and exported as reference CSV
- Vendor bill workflow confirmed functional
- Payment dual-authorisation tested with two user accounts
- Native financial reports (trial balance, P&L, balance sheet) rendering correctly

**Acceptance Criteria:** AC-01 (partial — chart of accounts, vendor bills, payments, native reporting)

**Governance Reviews Required:** Client review of chart of accounts structure before finalisation

---

### WP-FIN-02 — Finance Budget and Dashboard
**Backlog items:** BL-FIN-04, BL-FIN-05  
**Phase:** 1  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Configure budget control and executive financial dashboard.

**Scope:**
- Configure analytic accounts aligned to NADF budget lines
- Configure budget control via `account_budget_oca`
- Configure `mis_builder` with NADF financial KPI definitions (confirm KPI set with client)
- Test budget variance visibility

**Dependencies:** WP-FIN-01, WP-OCA-01

**Deliverables:**
- Budget control active against analytic accounts
- `mis_builder` dashboard rendering NADF financial KPIs

**Acceptance Criteria:** AC-01 (complete)

**Governance Reviews Required:** Client sign-off on KPI definitions before dashboard build

---

### WP-FIN-03 — Finance Security Configuration
**Backlog items:** BL-FIN-06, BL-FIN-07  
**Phase:** 1  
**Complexity:** Small  
**Status:** Not Started

**Objective:** Configure Finance user groups and enforce two-factor authentication.

**Scope:**
- Create user groups: Finance Officer, Finance Manager, CFO, Auditor
- Configure access rights per group on `account.move`, `account.payment`, `account.analytic`
- Enable TOTP 2FA in Odoo settings
- Enforce 2FA for Finance and Senior Management groups

**Dependencies:** WP-GOV-03

**Deliverables:**
- User groups created and access rights configured
- 2FA enforced for relevant groups

**Acceptance Criteria:** AC-14 (Finance component)

**Governance Reviews Required:** None

---

### WP-PROC-01 — Procurement Core Configuration
**Backlog items:** BL-PROC-01, BL-PROC-02, BL-PROC-04, BL-PROC-06, BL-PROC-07, BL-PROC-08  
**Phase:** 1  
**Complexity:** Large  
**Status:** In Progress

**Objective:** Configure the procurement pipeline from vendor records through to goods receipt.

**Scope:**
- Configure vendor record structure with compliance status field (custom selection field on `res.partner`)
- Install and configure `purchase_request` for structured requisitions
- Install and configure `purchase_requisition` for RFQ and tender workflow
- Configure goods receipt and stock flow
- Evaluate OCA `contract` module fit for PO-linked contract administration in Procurement context; document decision in `docs/DECISION_LOG.md` as DEC-CONTRACT-001 before `nadf_legal_contract` spec (BL-SPEC-04) is drafted
- Create user groups: Requisitioner, Procurement Officer, Procurement Manager, Finance Approver
- Verify `mail.thread` audit trail on `purchase.request`, `purchase.order`

**Dependencies:** WP-GOV-03, WP-OCA-01

**Deliverables:**
- Vendor records with compliance status field
- `purchase_request` workflow active
- RFQ and tender workflow active
- Goods receipt flow confirmed
- DEC-CONTRACT-001 logged in Decision Log

**Acceptance Criteria:** AC-02 (partial — approval chain blocked pending B-02, B-03)

**Governance Reviews Required:** None

---

### WP-PROC-02 — Procurement Approval Chain
**Backlog items:** BL-PROC-03, BL-PROC-05  
**Phase:** 1  
**Complexity:** Medium  
**Status:** Blocked (B-02, B-03)

**Objective:** Configure multi-level requisition approval chain and PO approval thresholds.

**Scope:**
- Configure `purchase_request` approval stages: initiator → department head → procurement officer → finance approval above threshold
- Configure purchase order approval limit thresholds (values from client — B-03)
- Confirm RACI on step 1.19 (B-02) and implement accordingly
- Test full approval chain end-to-end

**Dependencies:** WP-PROC-01; B-02 and B-03 resolved by client

**Deliverables:**
- Approval chain configured and tested end-to-end

**Acceptance Criteria:** AC-02 (complete)

**Governance Reviews Required:** Client sign-off on approval chain configuration before go-live

---

### WP-HR-01 — HR Core Configuration
**Backlog items:** BL-HR-01, BL-HR-02, BL-HR-03, BL-HR-04, BL-HR-05  
**Phase:** 1  
**Complexity:** Large  
**Status:** In Progress

**Objective:** Configure the full HR operation — employee records, leave, and recruitment.

**Scope:**
- Configure employee records with NADF 4-level org hierarchy (MD → Director → Manager → Officer) as job positions and manager hierarchy
- Configure leave types aligned to NADF leave policy
- Configure two-level leave approval: line manager → HR
- Configure recruitment pipeline stages: vacancy → shortlist → interview → offer → appointment
- Configure appointment and separation approval state on `hr.employee` with activity notification to CEO (implements Section 4 approval type: HR appointment / separation)
- Create user groups: Employee, Line Manager, HR Officer, HR Manager, CEO
- Verify `mail.thread` audit trail on `hr.employee`, `hr.leave`, `hr.applicant`
- Note: Performance management (BL-HR-06) is classified Deferred / Could Have — not in scope for this work package

**Dependencies:** WP-GOV-03

**Deliverables:**
- Employee record structure with org hierarchy
- Leave workflow active
- Recruitment pipeline active
- Appointment/separation approval state on `hr.employee` active with CEO notification
- User groups configured

**Acceptance Criteria:** AC-03 (payroll excluded — Phase 3; performance management excluded — Deferred)

**Governance Reviews Required:** Client review of leave types and org hierarchy before finalisation

---

### WP-ADM-01 — Administration Core Configuration
**Backlog items:** BL-ADM-01, BL-ADM-02, BL-ADM-03, BL-ADM-04  
**Phase:** 1  
**Complexity:** Medium  
**Status:** In Progress

**Objective:** Configure fleet, asset management, and ICT helpdesk.

**Scope:**
- Configure vehicle register: vehicle records, fuel log, servicing schedule, driver assignment
- Configure asset register: asset categories, depreciation methods aligned to NADF policy
- Install and configure `helpdesk_mgmt`: ticket categories (ICT), assignment rules, SLA configuration
- Create user groups: Driver, Fleet Manager, Asset Manager, IT Officer, IT Manager

**Dependencies:** WP-GOV-03, WP-OCA-01 (for `helpdesk_mgmt`)

**Deliverables:**
- Fleet register with at least one test vehicle record
- Asset register with test asset and depreciation schedule
- `helpdesk_mgmt` active with ICT category and SLA

**Acceptance Criteria:** AC-04 (facility management excluded — Phase 3)

**Governance Reviews Required:** None

---

### WP-PC-01 — Project Coordination Configuration
**Backlog items:** BL-PC-01, BL-PC-02, BL-PC-03, BL-PC-04  
**Phase:** 1  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Configure the `project` module to support NADF's 5-process project lifecycle.

**Scope:**
- Configure project record structure: phases (Initiation, Planning, Execution, M&C, Closure), task types, milestone model
- Configure phase gate: milestone sign-off restricted to Director group
- Configure project status dashboard (kanban + list views)
- Create user groups: Project Team Member, Project Manager, Director, PCU Head

**Dependencies:** WP-GOV-03

**Deliverables:**
- Project module configured with NADF phase structure
- Milestone sign-off restriction verified
- Dashboard view confirmed

**Acceptance Criteria:** AC-05

**Governance Reviews Required:** None

---

## PHASE 2 — CUSTOM MODULE SPECIFICATIONS

---

### WP-SPEC-01 — `nadf_payroll_ng` Specification
**Backlog items:** BL-SPEC-01  
**Phase:** 2  
**Complexity:** Large  
**Status:** Not Started

**Objective:** Produce an approved design specification for the Nigerian statutory payroll module.

**Scope:**
- Document: purpose, capability map reference (CA-03), data model (`hr.payslip` extension), Nigerian statutory deduction rules (PAYE bands, pension 8%+10%, NHF 2.5%, NSITF 1%), payslip UI, journal entry to `account`, test cases, acceptance criteria
- Circulate for legal/HR advisory input on statutory rates and rules
- Obtain client approval

**Dependencies:** WP-HR-01; Nigerian payroll legal/HR advisory input (E-01); OCA payroll base module must be installed (BL-OCA-07) before development begins

**Deliverables:**
- `docs/modules/nadf_payroll_ng_spec.md` — approved and committed

**Acceptance Criteria:**
- Spec contains all required sections
- Statutory rates confirmed by qualified adviser
- Client signature obtained

**Governance Reviews Required:** Legal/HR adviser review; client sign-off

---

### WP-SPEC-02 — `nadf_vendor_compliance` Specification
**Backlog items:** BL-SPEC-02  
**Phase:** 2  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Produce an approved design specification for the vendor compliance/pre-qualification module.

**Scope:**
- Document: compliance criteria fields on `res.partner`, scoring model, pre-qualification workflow, compliance status transitions, views and filters, test cases, acceptance criteria

**Dependencies:** WP-PROC-01

**Deliverables:**
- `docs/modules/nadf_vendor_compliance_spec.md` — approved

**Acceptance Criteria:** Spec approved by client; contains all required sections

**Governance Reviews Required:** Client sign-off

---

### WP-SPEC-03 — `nadf_facility` Specification
**Backlog items:** BL-SPEC-03  
**Phase:** 2  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Produce an approved design specification for the facility management module.

**Scope:**
- Document: facility record model, booking request workflow, maintenance request workflow, assignment to facility manager, status transitions, views, notifications, test cases, acceptance criteria

**Dependencies:** WP-ADM-01

**Deliverables:**
- `docs/modules/nadf_facility_spec.md` — approved

**Acceptance Criteria:** Spec approved by client; contains all required sections

**Governance Reviews Required:** Client sign-off

---

### WP-SPEC-04 — `nadf_legal_contract` Specification
**Backlog items:** BL-SPEC-04  
**Phase:** 2  
**Complexity:** Large  
**Status:** Not Started

**Objective:** Produce an approved design specification for the legal contract lifecycle module.

**Scope:**
- Document: contract model (type, counterparty, value, dates, status), sign-off workflow (LSU draft → review → ES/CEO approval → execution), contract register views, expiry alerting (scheduled action), link to `purchase.order` where applicable, document version control (contract drafts and amendments must be versioned — either as Odoo chatter attachments with explicit version naming convention, or as a dedicated version history model if chatter is insufficient), test cases, acceptance criteria

**Dependencies:** Legal Services Unit TO-BE P4–P6 delivered by Claude Desktop

**Deliverables:**
- `docs/modules/nadf_legal_contract_spec.md` — approved

**Acceptance Criteria:** Spec approved by client; consistent with Legal TO-BE specification

**Governance Reviews Required:** LSU review; client sign-off

---

### WP-SPEC-05 — `nadf_investment` Specification
**Backlog items:** BL-SPEC-05  
**Phase:** 2  
**Complexity:** Very Large  
**Status:** Not Started

**Objective:** Produce an approved design specification for the investment/loan portfolio management module.

**Scope:**
- Document: loan origination model, credit appraisal fields, disbursement schedule model, repayment tracking, portfolio performance report, journal entries to `account`, test cases, acceptance criteria
- Run business requirements session with NADF Investment department to confirm scope

**Dependencies:** Investment TO-BE delivered; client business requirements session (E-03)

**Deliverables:**
- `docs/modules/nadf_investment_spec.md` — approved

**Acceptance Criteria:** Spec approved by client after requirements session; all data model fields confirmed

**Governance Reviews Required:** Investment department requirements session; client sign-off

---

### WP-SPEC-06 — `nadf_me_indicators` Specification
**Backlog items:** BL-SPEC-06  
**Phase:** 2  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Produce an approved design specification for the M&E indicator framework module.

**Scope:**
- Document: indicator definition model, target vs actual tracking, period structure, linkage to `mis_builder` for dashboard rendering, cross-department indicator aggregation, test cases, acceptance criteria

**Dependencies:** M&E TO-BE delivered by Claude Desktop

**Deliverables:**
- `docs/modules/nadf_me_indicators_spec.md` — approved

**Acceptance Criteria:** Spec approved by client; consistent with M&E TO-BE

**Governance Reviews Required:** Client sign-off

---

## PHASE 3 — EXTENDED CAPABILITIES

---

### WP-DEV-01 — Develop `nadf_payroll_ng`
**Backlog items:** BL-DEV-01  
**Phase:** 3  
**Complexity:** Very Large  
**Status:** Not Started

**Objective:** Build and test the Nigerian statutory payroll module.

**Scope:**
- Create Odoo 17 CE module `nadf_payroll_ng` with correct `__manifest__.py`
- Extend OCA payroll base with Nigerian salary rule structure (PAYE, pension, NHF, NSITF)
- Implement payslip generation and payroll batch processing
- Implement journal entry creation to `account` on payroll confirmation
- Write unit tests for each salary rule
- Deploy to staging and validate against test payslips

**Dependencies:** WP-SPEC-01 approved; BL-OCA-07 complete (OCA payroll base installed)

**Deliverables:**
- `addons/nadf_payroll_ng/` — committed, tested, deployed to staging
- Unit test results committed

**Acceptance Criteria:** AC-03 (payroll component); all statutory deductions calculate correctly against test data

**Governance Reviews Required:** Test results reviewed; client payroll officer validates payslip output

---

### WP-DEV-02 — Develop `nadf_vendor_compliance`
**Backlog items:** BL-DEV-02  
**Phase:** 3  
**Complexity:** Large  
**Status:** Not Started

**Objective:** Build and test the vendor compliance module.

**Scope:** Per WP-SPEC-02 approved spec. Extend `res.partner` with compliance fields; implement scoring model; build pre-qualification workflow and views.

**Dependencies:** WP-SPEC-02 approved

**Deliverables:** `addons/nadf_vendor_compliance/` — committed, tested, deployed to staging

**Acceptance Criteria:** AC-02 (vendor compliance component)

**Governance Reviews Required:** Test results reviewed

---

### WP-DEV-03 — Develop `nadf_facility`
**Backlog items:** BL-DEV-03  
**Phase:** 3  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Build and test the facility management module.

**Scope:** Per WP-SPEC-03 approved spec. New `nadf.facility` and `nadf.facility.request` models; booking and maintenance request workflows; facility manager views.

**Dependencies:** WP-SPEC-03 approved

**Deliverables:** `addons/nadf_facility/` — committed, tested, deployed to staging

**Acceptance Criteria:** AC-04 (facility component)

**Governance Reviews Required:** Test results reviewed

---

### WP-DEV-04 — Develop `nadf_legal_contract`
**Backlog items:** BL-DEV-04  
**Phase:** 3  
**Complexity:** Large  
**Status:** Not Started

**Objective:** Build and test the legal contract lifecycle module.

**Scope:** Per WP-SPEC-04 approved spec. New `nadf.contract` model; sign-off workflow; contract register views; expiry scheduled action; PO linkage.

**Dependencies:** WP-SPEC-04 approved

**Deliverables:** `addons/nadf_legal_contract/` — committed, tested, deployed to staging

**Acceptance Criteria:** AC-06

**Governance Reviews Required:** LSU representative validates workflow; test results reviewed

---

### WP-DEV-05 — Develop `nadf_investment`
**Backlog items:** BL-DEV-05  
**Phase:** 3  
**Complexity:** Very Large  
**Status:** Not Started

**Objective:** Build and test the investment/loan portfolio management module.

**Scope:** Per WP-SPEC-05 approved spec. New models: `nadf.loan`, `nadf.disbursement`, `nadf.repayment`; origination workflow; disbursement scheduler; repayment tracker; portfolio report; journal entries to `account`.

**Dependencies:** WP-SPEC-05 approved

**Deliverables:** `addons/nadf_investment/` — committed, tested, deployed to staging

**Acceptance Criteria:** AC-10

**Governance Reviews Required:** Investment department representative validates loan lifecycle; test results reviewed; client sign-off

---

### WP-DEV-06 — Develop `nadf_me_indicators`
**Backlog items:** BL-DEV-06  
**Phase:** 3  
**Complexity:** Large  
**Status:** Not Started

**Objective:** Build and test the M&E indicator framework module.

**Scope:** Per WP-SPEC-06 approved spec. New `nadf.indicator` model; target vs actual tracking; period structure; `mis_builder` integration for dashboard; cross-department aggregation views.

**Dependencies:** WP-SPEC-06 approved; WP-OCA-01 (`mis_builder` installed)

**Deliverables:** `addons/nadf_me_indicators/` — committed, tested, deployed to staging

**Acceptance Criteria:** AC-11

**Governance Reviews Required:** M&E team validates indicator definitions; test results reviewed

---

### WP-INT-07 — Cross-department Notification and Escalation Matrix
**Backlog items:** BL-INT-07  
**Phase:** 3  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Configure automated notification triggers and escalation rules that operate across department boundaries.

**Scope:**
- Identify all cross-department notification events from TO-BE specifications (e.g. budget approval notifies Procurement; PO approval notifies Finance; contract execution notifies requesting department)
- Configure Odoo server actions and scheduled actions to fire notifications at correct approval stage transitions
- Configure escalation triggers for overdue approvals: identify escalation thresholds per department; configure scheduled action to notify line supervisor when approval is overdue beyond threshold
- Test notifications fire correctly on each configured event
- Test escalations trigger at correct time boundaries

**Dependencies:** Phase 1 department builds complete; remaining department builds complete for their notification events

**Deliverables:**
- Notification matrix documented in `docs/notification_matrix.md`
- Server actions and scheduled actions committed
- Test evidence of notifications and escalations firing

**Acceptance Criteria:** AC-13 (notification component); all configured notification events verified; escalation fires within correct threshold

**Governance Reviews Required:** Department heads confirm escalation thresholds before configuration

---

### WP-INT-08 — Cross-department Document Routing Workflows
**Backlog items:** BL-INT-08  
**Phase:** 3  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Implement document routing workflows that route records across department boundaries per the TO-BE specifications.

**Scope:** To be fully defined once remaining TO-BE specifications are delivered. Anticipated scope based on known processes:
- Finance payment advice routing to requesting department on payment confirmation
- Legal contract routing to Finance for payment scheduling on contract execution
- Procurement PO routing to Finance for budget commitment recording
- Investment disbursement routing to Finance for payment processing
- Configure routing as Odoo automated actions (server actions on state change) or `mail.thread` follower rules as appropriate per case

**Dependencies:** All department builds complete; remaining TO-BE specifications delivered (scope confirmation gate)

**Deliverables:**
- Document routing specification confirmed against TO-BE docs
- Routing workflows configured and committed
- Test evidence of routing working correctly end-to-end

**Acceptance Criteria:** AC-13 (document routing component); each routing workflow tested with a real document traversing the route without manual intervention

**Governance Reviews Required:** User review of routing specification before configuration

---

### WP-DEPT-01 through WP-DEPT-07 — Remaining Department Builds

Each remaining department build follows the same pattern. Work packages are created when the corresponding TO-BE specification is delivered by Claude Desktop.

| WP ID | Department | Capability | Dependency | Complexity |
|-------|-----------|-----------|-----------|-----------|
| WP-DEPT-01 | Legal Services Unit | CA-06 | Legal TO-BE complete + WP-DEV-04 | Large |
| WP-DEPT-02 | Strategy & Planning | CA-07 | Strategy TO-BE delivered | Medium |
| WP-DEPT-03 | Communications | CA-08 | Comms TO-BE delivered | Medium |
| WP-DEPT-04 | Sustainable Agriculture | CA-09 | SA TO-BE delivered; Investment module overlap (BL-DEV-05 / `nadf_investment`) must be assessed before build begins — SA disbursement logic may reuse Investment components, which would create a sequencing dependency | Medium |
| WP-DEPT-05 | Investment | CA-10 | Investment TO-BE + WP-DEV-05 | Very Large |
| WP-DEPT-06 | Monitoring & Evaluation | CA-11 | M&E TO-BE + WP-DEV-06 | Large |
| WP-DEPT-07 | Executive Management | CA-12 | Exec TO-BE + WP-OCA-01; dashboard must include pending-approval visibility view for CEO/MD across all departments | Medium |

**Standard template for each department work package:**
- Objective: Configure Odoo to implement the department's Detailed TO-BE specification
- Scope: Module configuration + user groups + access rights + workflow automation + dashboard/reporting view
- Deliverables: Working Odoo implementation; user groups committed; test results committed
- Acceptance Criteria: Per PRODUCT_SCOPE.md AC-0x for that department
- Governance Reviews Required: Department head validates workflow before marking Done

---

## PHASE 4 — INTEGRATIONS

---

### WP-INT-01 — Cross-functional Integration Testing
**Backlog items:** BL-INT-01 to BL-INT-08  
**Phase:** 4  
**Complexity:** Large  
**Status:** Not Started

**Objective:** Verify all cross-department workflows and data flows function correctly end-to-end.

**Scope:**
- Test and verify Budget → Procurement → Finance chain
- Test and verify HR appointment → CEO → payroll chain
- Test and verify Project → Finance budget consumption
- Test and verify Investment disbursement → Finance payment
- Test and verify cross-department notification and escalation matrix (configured in BL-INT-07 during Phase 3): notifications fire at correct approval stages; escalation triggers correctly on overdue items
- Test and verify cross-department document routing workflows (configured in BL-INT-08 during Phase 3): documents routed correctly between departments per TO-BE specs
- Verify Executive dashboard KPI roll-ups against source data — including the consolidated cross-department M&E view (BL-ME-01 + BL-INT-05): confirm indicator aggregation is accurate across all departments, not just within M&E module
- Produce integration test report

**Dependencies:** All Phase 3 department builds complete; BL-INT-07 and BL-INT-08 complete

**Deliverables:**
- Integration test results for each chain
- Notification/escalation matrix test evidence
- Document routing test evidence
- Cross-department M&E roll-up accuracy verified with source data comparison
- `docs/integration_test_report.md` committed

**Acceptance Criteria:** AC-13; all chains executable end-to-end without error; no data mismatch between departments; notifications fire correctly; cross-department M&E roll-up matches source department data

**Governance Reviews Required:** User review of integration test report

---

## PHASE 5 — TESTING & STABILISATION

---

### WP-UAT-01 — User Acceptance Testing
**Backlog items:** BL-UAT-01 to BL-UAT-04  
**Phase:** 5  
**Complexity:** Very Large  
**Status:** Not Started

**Objective:** Execute full UAT cycle with NADF users; resolve all defects; obtain sign-off.

**Scope:**
- Produce UAT test plan with one test case per acceptance criterion (AC-01 to AC-14)
- Coordinate UAT execution with NADF user representatives per department
- Log all defects in defect register; triage; resolve; retest
- Obtain signed UAT sign-off document from NADF

**Dependencies:** WP-INT-01 complete

**Deliverables:**
- UAT test plan
- UAT execution results
- Defect register (all resolved or formally deferred)
- Signed UAT sign-off

**Acceptance Criteria:** D-5.4 (signed UAT sign-off from NADF)

**Governance Reviews Required:** Lanasoft programme lead review of defect register before sign-off request

---

### WP-TRN-01 — Training Documentation
**Backlog items:** BL-TRN-01, BL-TRN-02  
**Phase:** 5  
**Complexity:** Medium  
**Status:** Not Started

**Objective:** Produce training documentation for super users and system administrators.

**Scope:**
- Super user guide per department (12 guides): how to use Odoo for their department's processes
- System administrator guide: user management, backup, module updates, basic troubleshooting

**Dependencies:** Phase 4 complete (stable system)

**Deliverables:**
- 12 department super user guides
- System administrator guide

**Acceptance Criteria:** D-5.5, D-5.6

**Governance Reviews Required:** Department heads review their department's super user guide

---

## PHASE 6 — DEPLOYMENT

---

### WP-DEP-01 — Production Deployment
**Backlog items:** BL-DEP-01 to BL-DEP-06  
**Phase:** 6  
**Complexity:** Very Large  
**Status:** Not Started

**Objective:** Deploy the complete system to production; migrate master data; confirm go-live.

**Scope:**
- Produce and approve cutover plan
- Execute master data migration: employees, vendors, chart of accounts values, asset register (client-provided data)
- Deploy to production environment
- Execute post-deployment smoke test (critical workflow per department)
- Obtain go-live confirmation signature
- Tag repository `v1.0-go-live`
- Begin hypercare period

**Dependencies:** WP-UAT-01 signed off; production server accessible

**Deliverables:**
- Cutover plan document
- Data migration executed and verified
- Production system live
- Go-live confirmation signed
- Repository tagged

**Acceptance Criteria:** D-6.1 to D-6.7

**Governance Reviews Required:** Lanasoft programme lead sign-off on cutover plan; NADF sign-off on go-live

---

## PHASE 7 — TEMPLATE EXTRACTION

---

### WP-TPL-01 — Public Sector ERP Template Extraction
**Backlog items:** BL-TPL-01 to BL-TPL-07  
**Phase:** 7  
**Complexity:** Large  
**Status:** Not Started

**Objective:** Extract and package all reusable assets as the Lanasoft Public Sector ERP Template.

**Scope:**
- Produce extraction report against PRODUCT_SCOPE.md Section 7 asset classification
- Strip NADF-specific data from all reusable assets
- Parameterise custom modules (remove NADF data; retain module architecture)
- Strip NADF references from governance scaffold
- Publish as new Software Factory repository

**Dependencies:** WP-DEP-01 complete; legal clearance for publication

**Deliverables:**
- Template extraction report
- Public Sector ERP Template repository (new)
- Template README and deployment guide

**Acceptance Criteria:** D-7.1 to D-7.7; zero NADF-specific data in template

**Governance Reviews Required:** Lanasoft legal/commercial review before publication
