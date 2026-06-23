# PRODUCT_SCOPE.md
## NADF ERP Programme — Implementation Authority

**Document type:** Operational — derived from NADF Full Product Transfer Package v2.1  
**Last updated:** 2026-06-20  
**Authority:** NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md  
**Purpose:** Primary build reference for Claude Code and the Software Factory Autonomous Agent Team

---

## 1. EXECUTIVE SUMMARY

The National Agricultural Development Fund (NADF) is implementing Odoo 17 Community Edition as its enterprise resource planning system, covering 12 departments and approximately 61 business processes. The implementation replaces manual, paper-based, siloed departmental workflows with governed, automated, system-enforced operations.

The platform is Odoo 17 Community Edition, extended with vetted OCA modules and purpose-built custom modules for requirements that neither CE nor OCA can satisfy. Six custom modules are required. No Enterprise features are in scope.

NADF is Reference Implementation #1 of a Public Sector ERP Template that Lanasoft Software Factory will extract and package for future government-sector deployments.

---

## 2. PRODUCT VISION

Build a unified, auditable, automated ERP system on Odoo 17 Community Edition that implements the optimised business processes documented across all 12 NADF departments — replacing manual workflows with governed, traceable, system-enforced operations — and engineered from day one to yield a reusable Public Sector ERP Template.

---

## 3. PRODUCT OBJECTIVES

| # | Objective |
|---|-----------|
| O-01 | Configure Odoo 17 CE core modules to support Finance, Procurement, HR, Administration, and Project Coordination operations |
| O-02 | Install and configure vetted OCA modules to close gaps between CE capability and NADF requirements |
| O-03 | Develop six custom Odoo modules to cover requirements not met by CE or OCA |
| O-04 | Implement multi-level approval workflows aligned to NADF governance model across all departments |
| O-05 | Configure role-based access rights and security groups for all user types across all departments |
| O-06 | Build executive and operational dashboards using OCA `mis_builder` |
| O-07 | Implement audit trail coverage on all business-critical records using native `mail.thread` |
| O-08 | Establish a governed repository with CI, branch protection, and complete documentation |
| O-09 | Deliver a production-ready Odoo instance successfully validated through full UAT |
| O-10 | Extract and package reusable Public Sector Core and Agriculture Agency Extension components as a Software Factory template |

---

## 4. MAJOR CAPABILITY AREAS

| # | Capability Area | Departments |
|---|----------------|------------|
| CA-01 | Financial Management | Finance |
| CA-02 | Procurement Management | Procurement |
| CA-03 | Human Resource Management | HR |
| CA-04 | Administration & Facilities | Administration |
| CA-05 | Project & Programme Management | Project Coordination |
| CA-06 | Legal & Contract Management | Legal Services Unit |
| CA-07 | Strategy & Planning | Strategy & Planning |
| CA-08 | Communications Management | Communications |
| CA-09 | Agriculture Programme Management | Sustainable Agriculture |
| CA-10 | Investment & Loan Portfolio Management | Investment |
| CA-11 | Monitoring & Evaluation | Monitoring & Evaluation |
| CA-12 | Executive Management | Executive Management |
| CA-13 | Cross-functional Workflows | All departments |
| CA-14 | Security & Access Control | All departments |

---

## 5. CAPABILITY DESCRIPTIONS

### CA-01 — Financial Management
Configure NADF's full accounting operation in Odoo `account`. Sub-capabilities: government chart of accounts, vendor bill processing, payment workflows with dual-authorisation, budget control against analytic accounts, financial reporting, executive financial dashboard via `mis_builder`, two-factor authentication, audit trail.

**Implementation:** CE `account` + OCA `account_budget_oca` + OCA `mis_builder`

### CA-02 — Procurement Management
Implement end-to-end procurement from requisition through to purchase order and goods receipt. Sub-capabilities: vendor records and compliance status, structured multi-step requisition and approval, RFQs and tenders, purchase order confirmation with approval gate, vendor compliance/pre-qualification scoring, contract record linked to PO.

**Implementation:** CE `purchase` + CE `stock` + OCA `purchase_request` + OCA `purchase_requisition` + Custom `nadf_vendor_compliance`

### CA-03 — Human Resource Management
Implement full HR lifecycle. Sub-capabilities: employee records with NADF 4-level org hierarchy, leave request and approval, recruitment pipeline, Nigerian statutory payroll.

**Implementation:** CE `hr` + CE `hr_holidays` + CE `hr_recruitment` + Custom `nadf_payroll_ng` (on OCA payroll base)

### CA-04 — Administration & Facilities
Manage NADF's physical and operational assets. Sub-capabilities: vehicle register and fuel logs, asset register and depreciation, ICT helpdesk ticketing, facility booking and maintenance requests.

**Implementation:** CE `fleet` + CE `account_asset` + OCA `helpdesk_mgmt` + Custom `nadf_facility`

### CA-05 — Project & Programme Management
Track NADF projects through full lifecycle. Sub-capabilities: project initiation and planning, task and milestone management, phase gate approvals, project status reporting.

**Implementation:** CE `project` (fully sufficient for this scope)

### CA-06 — Legal & Contract Management
Manage NADF's legal contract lifecycle. Sub-capabilities: contract record creation, multi-party sign-off workflow aligned to NADF RACI, contract register with status views, expiry and renewal alerting.

**Implementation:** Custom `nadf_legal_contract` (OCA `contract` is insufficient for NADF's RACI sign-off structure)

### CA-07 — Strategy & Planning
Track NADF's strategic plans and initiatives. Sub-capabilities: strategic plan records, initiative tracking, progress monitoring.

**Implementation:** CE `project` repurposed (confirm once TO-BE specification delivered)

### CA-08 — Communications Management
Track and manage NADF communications requests and workflows.

**Implementation:** OCA `helpdesk_mgmt` or CE `project` repurposed (confirm once TO-BE specification delivered)

### CA-09 — Agriculture Programme Management
Track NADF's agricultural programme activities, grants, and disbursements.

**Implementation:** To be determined once TO-BE specification delivered; likely overlaps with CA-10

### CA-10 — Investment & Loan Portfolio Management
Manage NADF's full investment and loan portfolio. Sub-capabilities: loan origination, credit appraisal, disbursement scheduling, repayment tracking, portfolio performance reporting.

**Implementation:** Custom `nadf_investment` (no CE or OCA equivalent exists)

### CA-11 — Monitoring & Evaluation
Track programme KPIs and outcome indicators. Sub-capabilities: indicator definition and tracking, programme M&E dashboards, cross-department performance reporting.

**Implementation:** OCA `mis_builder` + Custom `nadf_me_indicators`

### CA-12 — Executive Management
Provide executive-level visibility across all NADF operations. Sub-capabilities: cross-department KPI dashboard, executive-level approval visibility.

**Implementation:** OCA `mis_builder` (custom roll-up views if standard views are insufficient)

### CA-13 — Cross-functional Workflows
Multi-department approval and notification chains that span more than one capability area. Sub-capabilities: budget-to-procurement-to-finance approval chain, cross-department escalation and notification, document routing between departments.

**Implementation:** Native Odoo workflow states + `mail.thread` notifications + user group access controls across relevant modules

### CA-14 — Security & Access Control
System-wide security configuration. Sub-capabilities: role-based access rights by department and seniority, two-factor authentication enforcement, audit log coverage on all business documents.

**Implementation:** Native Odoo user groups and access rights configuration + native TOTP 2FA + `mail.thread`

---

## 6. ACCEPTANCE CRITERIA

| ID | Capability | Acceptance Criterion |
|----|-----------|---------------------|
| AC-01 | CA-01 Finance | Chart of accounts reflects NADF government account structure; vendor bills process correctly; payments require dual authorisation above threshold; budget variances are visible; `mis_builder` dashboard renders NADF financial KPIs |
| AC-02 | CA-02 Procurement | Requisition initiated by staff; routed through department head → procurement → finance approval at correct thresholds; RFQ generated and sent; PO confirmed; goods receipt recorded |
| AC-03 | CA-03 HR | All NADF staff on employee records; leave requests flow through line manager → HR approval; recruitment pipeline active; payslips generated with correct statutory deductions (PAYE, pension, NHF, NSITF) |
| AC-04 | CA-04 Admin | All vehicles on fleet register with fuel log; all assets on asset register with depreciation schedule; ICT helpdesk tickets created, assigned, and resolved; facility requests tracked |
| AC-05 | CA-05 Project | Projects created with phases, tasks, and milestones; milestone sign-off restricted to authorised users; project status visible in dashboard view |
| AC-06 | CA-06 Legal | Contracts created with counterparty, value, dates, type; sign-off workflow routes to LSU → ES/CEO; contract register filterable by status; expiry alerts fire at configured lead time |
| AC-07 | CA-07 Strategy | Strategic plans recorded and trackable (confirm criteria once TO-BE delivered) |
| AC-08 | CA-08 Comms | Communications requests tracked and routed (confirm criteria once TO-BE delivered) |
| AC-09 | CA-09 Agriculture | Programme activities and disbursements tracked (confirm criteria once TO-BE delivered) |
| AC-10 | CA-10 Investment | Loans originated with full appraisal record; disbursements scheduled and recorded; repayments tracked against schedule; portfolio report renders summary across all active loans |
| AC-11 | CA-11 M&E | Indicators defined with targets and actuals; M&E dashboard renders programme performance; cross-department indicators consolidated |
| AC-12 | CA-12 Executive | Executive dashboard renders cross-department KPIs; all key metrics visible in single view |
| AC-13 | CA-13 Cross-functional | Budget-procurement-finance chain executable end-to-end without manual routing; notifications fire at each approval stage |
| AC-14 | CA-14 Security | All users assigned correct groups; no user can access data outside their role; 2FA active for Finance and Senior Management; audit log present on all business documents |

---

## 7. ASSET CLASSIFICATION

Every deliverable is classified for reusability.

### Generic Reusable Assets (applicable to any Odoo deployment)
- Governed repository scaffold (Control Tower, Backlog, Milestone Register, Decision Log, NEXT_ACTION.md)
- Governance Activation Gate framework and checklist
- OCA module integration patterns (`mis_builder`, `helpdesk_mgmt`, `purchase_request`)
- CE access rights and user group configuration methodology
- `mail.thread` audit trail pattern
- CI workflow templates
- Session start/end governance protocol

### Government ERP Assets (applicable to public sector Odoo deployments)
- Government chart of accounts structure
- Multi-level procurement approval workflow (threshold-based, role-enforced)
- HR leave and recruitment workflow configurations
- Fleet and asset management configuration for government context
- Executive KPI dashboard structure (`mis_builder` configuration)
- Two-factor authentication enforcement pattern
- `nadf_payroll_ng` module structure (without Nigerian-specific statutory rates)
- `nadf_investment` module structure (without NADF portfolio data)
- `nadf_legal_contract` module structure (without NADF-specific RACI assignments)
- `nadf_facility` module (fully reusable)
- `nadf_vendor_compliance` module structure
- M&E indicator framework structure (`nadf_me_indicators`)

### NADF Specific Assets (not for extraction)
- NADF organisational hierarchy, staff names, role assignments
- NADF vendor data and history
- NADF-specific RACI assignments and approval thresholds
- NADF branding and report templates
- NADF loan/investment portfolio data
- NADF chart of accounts specific code values

---

## 8. TEMPLATE EXTRACTION OPPORTUNITIES

At programme completion (Phase 7), the following will be extracted and packaged as the Lanasoft Public Sector ERP Template:

| Component | Category | Extraction Method |
|-----------|---------|------------------|
| Repository governance scaffold | Generic Reusable | Copy as-is; strip NADF references |
| Governance Activation Gate | Generic Reusable | Copy as-is |
| Government chart of accounts structure | Government ERP | Anonymise account codes; retain structure |
| Multi-level procurement approval chain | Government ERP | Parameterise thresholds; strip NADF specifics |
| HR leave and recruitment config | Government ERP | Strip NADF staff data; retain workflow config |
| `mis_builder` dashboard config | Government ERP | Strip NADF KPIs; retain dashboard structure |
| `nadf_payroll_ng` (structure) | Government ERP | Remove statutory rate values; retain module architecture |
| `nadf_investment` (structure) | Government ERP | Remove NADF portfolio data; retain module architecture |
| `nadf_legal_contract` (structure) | Government ERP | Remove NADF-specific RACI; retain module architecture |
| `nadf_facility` | Government ERP | Copy as-is — fully generic |
| `nadf_vendor_compliance` (structure) | Government ERP | Remove NADF-specific scoring criteria; retain module architecture |

---

## 9. OUT OF SCOPE

The following are explicitly out of scope for Claude Code under this programme:

- Swimlane diagram production (Claude Desktop responsibility)
- Process workbook creation or maintenance (Claude Desktop responsibility)
- Infrastructure provisioning, server configuration, network architecture
- Hardware procurement
- Data entry (master data population is a client responsibility; Claude Code configures the structure)
- End-user training delivery (training documentation may be produced; delivery is client/Lanasoft responsibility)
- Integration with third-party systems not identified in the transfer package
- Odoo Enterprise features

---

## 10. ASSUMPTIONS

| # | Assumption |
|---|-----------|
| A-01 | Odoo 17 Community Edition is installed and accessible at `/Users/mac/odoo17` |
| A-02 | A PostgreSQL database exists for NADF — name to be confirmed during discovery |
| A-03 | A Git repository exists at `/Users/mac/nadf_erp` |
| A-04 | GitHub remote access is configured or will be configured in Phase 0 |
| A-05 | The client will provide confirmation of Procurement blockers B-02 and B-03 before the procurement approval chain is built |
| A-06 | TO-BE specifications for the remaining 7 departments will be delivered by Claude Desktop before Odoo builds for those departments are initiated |
| A-07 | Nigerian payroll statutory requirements (PAYE, pension, NHF, NSITF rates and rules) will be provided by a qualified adviser before `nadf_payroll_ng` spec is finalised |
| A-08 | The `nadf_investment` module scope will be confirmed with NADF through a business requirements session before spec is drafted |
| A-09 | All OCA modules are assumed to be Odoo 17 compatible — compatibility must be verified during M-OCA-01 before installation |
| A-10 | Master data (employee records, vendor records, chart of accounts values) will be provided by the client for data migration; Claude Code configures the structure and import mechanism |

---

## 11. SUCCESS CRITERIA

| # | Criterion |
|---|-----------|
| S-01 | All five Governance Activation Gates pass before implementation begins |
| S-02 | Zero Enterprise modules in the production Odoo instance |
| S-03 | All 14 capability areas delivered and accepted against their acceptance criteria |
| S-04 | All six custom modules built, tested, and deployed |
| S-05 | Full UAT cycle completed with sign-off from NADF |
| S-06 | Production deployment completed without data loss or critical system failure |
| S-07 | Public Sector ERP Template extracted and packaged as a reusable Software Factory asset |
| S-08 | All governance documents current and committed to the repository at go-live |
