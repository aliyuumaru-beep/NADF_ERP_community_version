# NADF FULL PRODUCT TRANSFER PACKAGE — v2.1

**Status:** AUTHORITATIVE — supersedes v2.0 and all prior versions  
**Prepared by:** Claude Desktop (NADF BPOGS Project Folder)  
**Date:** 2026-06-20  
**Destination:** Claude Code — NADF ERP Local Repository

**Authority statement:** All information in this document is based on NADF project materials in the Claude Desktop project folder. Claude Desktop has not inspected and does not claim to have inspected the local repository, the Odoo instance, GitHub, or the database. All repository-side facts must be verified by Claude Code via the discovery sequence in Section 15 before any implementation proceeds.

---

## ⚠️ CRITICAL PLATFORM DECLARATION

**Authoritative platform: Odoo 17 Community Edition.**

The following Enterprise modules/features are **unavailable** and must never be assumed, specified, or referenced:
- `approvals` (Enterprise Approvals)
- `documents` (Enterprise Documents)
- `sign` (Enterprise Sign)
- `spreadsheet_dashboard`, `documents_spreadsheet` (Enterprise Spreadsheet)
- `knowledge` (Enterprise Knowledge)
- `web_studio` (Enterprise Studio)
- `hr_payroll` Enterprise edition

**For every Enterprise-shaped requirement:**
1. Identify the gap
2. Recommend the Community native alternative
3. Recommend the OCA alternative
4. Justify custom development only if neither CE nor OCA closes the gap

---

## ⚠️ NOTE ON SWIMLANE DIAGRAMS

Swimlane diagrams are business process documentation outputs produced by Claude Desktop. They are **not built, deployed, or maintained by Claude Code.**

Their sole relevance to Claude Code is this: **the Detailed TO-BE swimlane diagrams are the functional specification that Claude Code implements in Odoo.** When a TO-BE diagram shows a step as automated in the Odoo System lane, Claude Code configures or builds the corresponding Odoo workflow, automation rule, or module feature.

Claude Code must not produce swimlane files, reference swimlane production rules, or count swimlane outputs. Those are entirely Claude Desktop responsibilities.

---

## SECTION 1 — PRODUCT VISION

**Client:** National Agricultural Development Fund (NADF)  
**Consultant:** Lanasoft Technologies  
**Platform:** Odoo 17 Community Edition — extended with OCA modules; custom development reserved for genuine gaps

**Vision:** Build a unified, auditable, automated ERP system on Odoo 17 Community Edition that implements the optimised business processes documented across all 12 NADF departments — replacing manual, paper-based, siloed workflows with governed, traceable, system-enforced operations.

**Secondary objective:** Engineer the implementation as Reference Implementation #1 of a reusable Public Sector ERP Template, to be extracted and packaged for future government-sector deployments (Phase 5).

**Non-negotiable constraints:**
- Odoo Enterprise features must never be assumed or referenced unless the user explicitly confirms an Enterprise licence with evidence
- Every capability, module, and milestone must trace back to the Capability Map (Section 6)
- NADF is the reference implementation — not the template itself

---

## SECTION 2 — BUSINESS SCOPE

### What Claude Code is building

Claude Code builds and maintains the NADF Odoo ERP system. This means:

- Installing, configuring, and extending Odoo 17 Community Edition modules
- Installing and configuring vetted OCA modules
- Developing custom Odoo modules where CE and OCA do not close the gap
- Configuring multi-level approval workflows in Odoo
- Setting up user roles, access rights, and security groups
- Implementing automated business rules (scheduled actions, server actions, triggers)
- Building dashboards and reports
- Writing and running tests
- Managing the Git repository, PRs, CI, and governance documents
- Supporting UAT and production deployment

### What Claude Code is NOT building

Claude Code does not produce:
- Swimlane HTML diagram files
- Process workbooks
- BPMN documentation
- RACI matrices

These are Claude Desktop deliverables. Claude Code reads the TO-BE process specifications as input and implements the corresponding Odoo system behaviour.

### Specification source

The functional specification for every Odoo automation is the **Detailed TO-BE process documentation** produced by Claude Desktop. When Claude Desktop delivers a completed TO-BE process, it will identify:
- Which steps are automated (system actions)
- What triggers each automation
- What data is created, updated, or routed
- What approvals are required
- What notifications are sent

Claude Code implements these in Odoo. The TO-BE document is the requirement; Odoo is the implementation.

### Scope by department

| Department | Processes | TO-BE Status | Odoo Build Status |
|-----------|-----------|-------------|------------------|
| Finance | 7 | ✅ Complete | 🔄 Phase 1 in progress |
| Procurement | 6 | ✅ Complete (2 open queries) | 🔄 Phase 1 in progress |
| HR | 8 | ✅ Complete | 🔄 Phase 1 in progress |
| Administration | ~5 | ✅ Complete | 🔄 Phase 1 in progress |
| Project Coordination | 5 | ✅ Complete | ⏳ Not started |
| Legal Services Unit | 6 | 🔄 P1–P3 done; P4–P6 pending | ⏳ Pending TO-BE completion |
| Strategy & Planning | ~5 | ⏳ Pending | ⏳ Pending TO-BE |
| Communications | ~5 | ⏳ Pending | ⏳ Pending TO-BE |
| Sustainable Agriculture | ~5 | ⏳ Pending | ⏳ Pending TO-BE |
| Investment | ~5 | ⏳ Pending | ⏳ Pending TO-BE |
| Monitoring & Evaluation | ~5 | ⏳ Pending | ⏳ Pending TO-BE |
| Executive Management | ~4 | ⏳ Pending | ⏳ Pending TO-BE |

---

## SECTION 3 — DEPARTMENT BUILD REQUIREMENTS

For each department, the Odoo build requirement is defined by the TO-BE functional specification. The following summarises what Claude Code must build per department.

### 3.1 Finance
**Odoo modules:** `account`, `account_payment`  
**OCA modules:** `account_budget_oca` (richer budget control), `mis_builder` (executive financial dashboard)  
**Custom:** Nigerian-specific financial reporting format if `mis_builder` standard reports are insufficient  
**Build scope:**
- Chart of accounts configured to NADF's government account structure
- Vendor bill and payment workflows with dual-authorisation enforcement
- Budget control against analytic accounts
- Executive financial dashboard (KPI views via `mis_builder`)
- Two-factor authentication (native TOTP, CE-supported)
- User groups: Finance Officer, Finance Manager, CFO, Auditor — with appropriate access rights per TO-BE RACI

**Open queries:** 2FA enforcement method to confirm; dashboard KPI set to be confirmed with client before build

### 3.2 Procurement
**Odoo modules:** `purchase`, `stock`  
**OCA modules:** `purchase_request` (structured multi-step requisition and approval), `purchase_requisition` (call for tenders)  
**Custom:** Vendor pre-qualification/compliance scoring module (no CE/OCA fit identified)  
**Build scope:**
- Vendor records with compliance status field
- Purchase requisition workflow: initiator → department head → procurement officer → Finance approval above threshold
- RFQ generation and vendor bid capture
- Purchase order confirmation with approval gate
- Contract record linked to PO (custom or OCA `contract` — evaluate fit)
- User groups: Requisitioner, Procurement Officer, Procurement Manager, Finance Approver

**Open queries:**
- B-02: RACI on one procurement step pending client confirmation — do not build that step's approval chain until confirmed
- B-03: Approval threshold values pending client data — use placeholder until confirmed

### 3.3 HR
**Odoo modules:** `hr`, `hr_holidays`, `hr_recruitment`  
**OCA modules:** Payroll base (OCA `payroll` repo) as foundation for Nigerian statutory payroll  
**Custom:** Nigerian statutory payroll (PAYE, pension, NHF, NSITF) on OCA payroll base — justified, no CE/OCA standard covers Nigerian legislation  
**Build scope:**
- Employee record structure matching NADF 4-level org hierarchy (MD → Director → Manager → Officer)
- Leave workflow: request → line manager approval → HR confirmation
- Recruitment pipeline: vacancy → shortlist → interview → offer → appointment
- Payroll: statutory deductions, payslip generation, payroll journal entry to `account`
- User groups: Employee, Line Manager, HR Officer, HR Manager, CEO (for appointment approvals)

### 3.4 Administration
**Odoo modules:** `fleet`, `account_asset`  
**OCA modules:** `helpdesk_mgmt` (ICT helpdesk — note: native `helpdesk` is Enterprise-only)  
**Custom:** Facility management module (no CE/OCA fit — lightweight request/scheduling model justified)  
**Build scope:**
- Vehicle register with fuel log, servicing schedule, driver assignment
- Asset register with depreciation schedule
- ICT helpdesk: ticket creation, assignment, resolution, SLA tracking via `helpdesk_mgmt`
- Facility booking/maintenance request workflow (custom)
- User groups: Driver, Fleet Manager, Asset Manager, IT Officer, IT Manager, Facility Manager

### 3.5 Project Coordination
**Odoo modules:** `project`  
**OCA modules:** None required — `project` CE module is fully sufficient for NADF's 5-process scope  
**Build scope:**
- Project record: initiation form, objectives, budget, stakeholders
- Task structure per project phase (Initiation, Planning, Execution, M&C, Closure)
- Milestone tracking with approval gate at each phase gate
- Project status reporting view (kanban + list)
- User groups: Project Team Member, Project Manager, Director, PCU Head

### 3.6 Legal Services Unit
**Status:** Pending TO-BE completion (P4–P6) before Odoo build can begin  
**Odoo modules:** None native for legal contract management  
**OCA modules:** `contract` (recurring/subscription contract — partial fit, evaluate)  
**Custom:** Legal contract lifecycle module — likely justified given NADF's specific RACI sign-off structure, counterparty management, and document version control requirements  
**Build scope (once TO-BE complete):**
- Contract record: type, counterparty, value, dates, status
- Sign-off workflow: LSU drafts → review → ES/CEO approval → execution
- Contract register view with status filters
- Alerting for expiry/renewal deadlines

### 3.7 Strategy & Planning
**Status:** Pending TO-BE  
**Tentative approach:** `project` module repurposed for strategic plan tracking (confirm after TO-BE delivered)

### 3.8 Communications
**Status:** Pending TO-BE  
**Tentative approach:** `helpdesk_mgmt` or `project` repurposed (confirm after TO-BE delivered)

### 3.9 Sustainable Agriculture
**Status:** Pending TO-BE  
**Tentative approach:** Likely overlaps with Investment module (grant disbursement pattern) — assess after TO-BE

### 3.10 Investment
**Status:** Pending TO-BE  
**Custom module required:** Investment/Loan Portfolio Management — no CE or OCA equivalent identified  
**Anticipated scope:** Loan origination, credit appraisal, disbursement scheduling, repayment tracking, portfolio performance reporting  
**This is a significant custom development item.** Design spec required before any code is written.

### 3.11 Monitoring & Evaluation
**Status:** Pending TO-BE  
**OCA modules:** `mis_builder` as base  
**Custom:** M&E indicator framework extension — programme-level KPI tracking not covered by `mis_builder` standard financial indicators

### 3.12 Executive Management
**Status:** Pending TO-BE  
**OCA modules:** `mis_builder` for executive dashboard  
**Build scope:** Cross-department KPI roll-up dashboard; executive-level approval views

---

## SECTION 4 — APPROVAL FRAMEWORK

The TO-BE process documentation defines multi-level approval requirements across all departments. Claude Code implements these in Odoo as follows.

**Enterprise `approvals` module is unavailable.** Approval chains are implemented using:

| Approval type | Implementation approach |
|--------------|------------------------|
| Procurement requisition | OCA `purchase_request` multi-step approval chain |
| Purchase order above threshold | `purchase` native approval limits + manager group restriction |
| Finance payment | `account` payment workflow states + user group access restriction |
| HR leave | `hr_holidays` two-level approval (line manager → HR) |
| HR appointment / separation | Custom approval state on `hr.employee` + activity/notification to CEO |
| Project milestone sign-off | `project` task stage restriction by user group |
| Legal contract execution | Custom approval state on contract record |

**Audit trail:** All Odoo business documents inherit `mail.thread` (native CE), providing a full audit log of state changes, approvals, and comments. No Enterprise module required.

---

## SECTION 5 — CUSTOM MODULES REQUIRED

These modules require design specs before development begins. Each spec lives at `docs/modules/[MODULE_NAME]_spec.md`.

| Module | Justification | Priority | Status |
|--------|--------------|---------|--------|
| `nadf_payroll_ng` | Nigerian statutory payroll (PAYE, pension, NHF, NSITF) on OCA payroll base — no CE/OCA standard covers Nigerian legislation | P1 | Not started |
| `nadf_investment` | Loan/investment portfolio management — no CE/OCA equivalent identified | P1 | Not started |
| `nadf_legal_contract` | Legal contract lifecycle with NADF-specific RACI sign-off chain | P2 | Not started |
| `nadf_facility` | Facility management — booking, maintenance requests, scheduling | P2 | Not started |
| `nadf_vendor_compliance` | Vendor pre-qualification and compliance scoring | P2 | Not started |
| `nadf_me_indicators` | M&E indicator framework on `mis_builder` base | P3 | Not started |

Each module must carry the `nadf_` prefix. Each `__manifest__.py` must include `author`, `version`, `license`, `depends` fully populated. No development begins without an approved spec.

---

## SECTION 6 — CAPABILITY MAP

Every milestone and module traces back to this map. Classification: **Native** / **Config** / **OCA** / **Custom** / **Future**.

### Finance
| Sub-Capability | Classification | Module/Approach |
|----------------|----------------|-----------------|
| Chart of accounts | Config | `account` |
| Payments & vendor bills | Native | `account` |
| Budget management | OCA | `account_budget_oca` |
| Financial reporting | Native | `account` |
| Executive dashboard | OCA | `mis_builder` |
| Two-factor authentication | Config | Native TOTP (CE) |
| Audit trail | Native | `mail.thread` |

### Procurement
| Sub-Capability | Classification | Module/Approach |
|----------------|----------------|-----------------|
| Vendor management | Native | `purchase` |
| Purchase requisitions | OCA | `purchase_request` |
| RFQs & tenders | OCA | `purchase_requisition` |
| Purchase orders | Native | `purchase` |
| Vendor evaluation | Custom | `nadf_vendor_compliance` |
| Contract administration | OCA/Custom | `contract` (evaluate); `nadf_legal_contract` |
| Multi-level approval | OCA | `purchase_request` approval chain |

### HR
| Sub-Capability | Classification | Module/Approach |
|----------------|----------------|-----------------|
| Employee records & org chart | Native | `hr` |
| Leave management | Native | `hr_holidays` |
| Recruitment | Native | `hr_recruitment` |
| Payroll | Custom | `nadf_payroll_ng` on OCA base |
| Performance management | Future | Post-phase-1 |

### Administration
| Sub-Capability | Classification | Module/Approach |
|----------------|----------------|-----------------|
| Fleet management | Native | `fleet` |
| Asset management | Native | `account_asset` |
| ICT helpdesk | OCA | `helpdesk_mgmt` |
| Facility management | Custom | `nadf_facility` |
| Fuel tracking | Native | `fleet` fuel logs |

### Project Coordination
| Sub-Capability | Classification | Module/Approach |
|----------------|----------------|-----------------|
| Project/task management | Native | `project` |
| Milestone tracking | Native | `project` |
| Phase gate approvals | Config | `project` stage restrictions |

### Legal Services Unit
| Sub-Capability | Classification | Module/Approach |
|----------------|----------------|-----------------|
| Contract lifecycle | Custom | `nadf_legal_contract` |
| Sign-off workflow | Custom | State machine on `nadf_legal_contract` |
| Contract register | Custom | Views on `nadf_legal_contract` |
| Expiry alerting | Custom | Scheduled action on `nadf_legal_contract` |

### Strategy & Planning
| Sub-Capability | Classification | Module/Approach |
|----------------|----------------|-----------------|
| Strategic plan tracking | OCA/Config (tentative) | `project` repurposed — confirm post-TO-BE |

### Investment
| Sub-Capability | Classification | Module/Approach |
|----------------|----------------|-----------------|
| Loan origination | Custom | `nadf_investment` |
| Disbursement scheduling | Custom | `nadf_investment` |
| Repayment tracking | Custom | `nadf_investment` |
| Portfolio reporting | Custom | `nadf_investment` + `mis_builder` |

### Monitoring & Evaluation
| Sub-Capability | Classification | Module/Approach |
|----------------|----------------|-----------------|
| KPI dashboard | OCA + Custom | `mis_builder` + `nadf_me_indicators` |
| Programme indicator tracking | Custom | `nadf_me_indicators` |

### Executive Management
| Sub-Capability | Classification | Module/Approach |
|----------------|----------------|-----------------|
| Executive dashboard | OCA | `mis_builder` |
| Cross-department reporting | OCA/Custom | `mis_builder` + custom roll-ups |

**Governance rule:** No module, milestone, or backlog item may be created without a corresponding row in this map. If a new requirement emerges, update the Capability Map first.

---

## SECTION 7 — PUBLIC SECTOR TEMPLATE REGISTRY

Every item is tagged for future template extraction in Phase 5.

| Item | Reusable? | Category |
|------|-----------|----------|
| Procurement multi-level approval workflow | ✅ Reusable | Public Sector Core |
| Government chart of accounts structure | ✅ Reusable | Public Sector Core |
| HR leave workflow | ✅ Reusable | Public Sector Core |
| HR recruitment pipeline | ✅ Reusable | Public Sector Core |
| Vendor management configuration | ✅ Reusable | Public Sector Core |
| Fleet/asset management configuration | ✅ Reusable | Public Sector Core |
| OCA `helpdesk_mgmt` configuration pattern | ✅ Reusable | Public Sector Core |
| OCA `mis_builder` dashboard configuration pattern | ✅ Reusable | Public Sector Core |
| Two-factor authentication policy | ✅ Reusable | Public Sector Core |
| `mail.thread` audit trail pattern | ✅ Reusable | Public Sector Core |
| Repository governance scaffold (Control Tower, Backlog, etc.) | ✅ Reusable | Public Sector Core |
| `nadf_payroll_ng` module (structure, not statutory rates) | ✅ Reusable | Public Sector Core |
| Grant/programme disbursement pattern | ✅ Reusable | Agriculture Agency Extensions |
| Investment/loan lifecycle module structure | ✅ Reusable | Agriculture Agency Extensions |
| M&E indicator framework structure | ✅ Reusable | Agriculture Agency Extensions |
| NADF org hierarchy, staff, role data | ❌ Not reusable | NADF Specific |
| NADF vendor data | ❌ Not reusable | NADF Specific |
| NADF-specific RACI assignments | ❌ Not reusable | NADF Specific |
| NADF branding | ❌ Not reusable | NADF Specific |

**Registry rule:** At completion of each milestone, Claude Code tags its outputs against this registry. Items tagged reusable are candidates for Phase 5 template extraction.

---

## SECTION 8 — PRODUCT BACKLOG (SUMMARY)

Full detail in `docs/PRODUCT_BACKLOG.md` in the repository.

| Category | Total Items | Done | In Progress | Not Started | Blocked |
|----------|------------|------|------------|-------------|---------|
| Odoo CE core configuration | ~20 | ~10 | ~6 | ~4 | 0 |
| OCA module integration | ~10 | 0 | ~2 | ~8 | 0 |
| Custom module development | 6 | 0 | 0 | 6 | 0 |
| Dashboards/reporting | 5 | 0 | 1 | 4 | 0 |
| Security/access rights | 4 | 0 | 2 | 2 | 0 |
| Cross-functional workflows | 3 | 0 | 0 | 3 | 0 |
| UAT & deployment | 3 | 0 | 1 | 2 | 0 |

**Immediate backlog correction required:** Any existing backlog item referencing an Enterprise module must be rewritten against the Section 6 Capability Map before that item is actioned. This is task M-PLATFORM-CORRECTION in the milestone plan.

---

## SECTION 9 — PRODUCT ROADMAP

### Phase 0 — Engagement Setup ✅ Complete
Governance framework, process documentation methodology, swimlane standards established. Platform corrected to Odoo 17 CE.

### Phase 1 — Core ERP Build 🔄 In Progress
Configure and extend CE core modules for Finance, Procurement, HR, Administration, Project Coordination. Install and configure OCA modules (`purchase_request`, `purchase_requisition`, `mis_builder`, `helpdesk_mgmt`). Complete once all five departments have working Odoo flows aligned to their TO-BE specifications.

### Phase 2 — Remaining Departments
Build Odoo implementations for Legal, Strategy, Communications, Sustainable Agriculture, Investment, M&E, Executive Management — each initiated once the corresponding TO-BE specification is delivered by Claude Desktop.

### Phase 2.5 — Custom Module Development
Design, build, test, and deploy: `nadf_investment`, `nadf_legal_contract`, `nadf_payroll_ng`, `nadf_facility`, `nadf_vendor_compliance`, `nadf_me_indicators`. Each requires an approved spec before development begins.

### Phase 3 — UAT & Training
Full user acceptance testing against TO-BE specifications. Super user training. Training documentation.

### Phase 4 — Production Deployment
Go-live. Cutover plan. Data migration. Hypercare period.

### Phase 5 — Template Extraction
Extract reusable Public Sector Core and Agriculture Agency Extension items into a standalone Software Factory public sector Odoo template.

---

## SECTION 10 — MILESTONE PLAN

| ID | Milestone | Status | Dependency |
|----|-----------|--------|-----------|
| M-PLATFORM-CORRECTION | Audit Odoo instance for installed Enterprise modules; document findings; rewrite affected backlog items | ⏳ URGENT — first milestone | Discovery (Section 15) |
| M-GOVERNANCE-GATE | Run all five Governance Activation Gate checks; produce `GOVERNANCE_GATE_REPORT.md`; fix all FAILs | ⏳ URGENT — before implementation | M-PLATFORM-CORRECTION |
| M-OCA-01 | Install and configure `mis_builder`, `helpdesk_mgmt`, `purchase_request`, `purchase_requisition` | ⏳ | M-GOVERNANCE-GATE |
| M-FIN-01 | Finance CE configuration complete: accounts, payments, budget, dashboard, 2FA, user groups | 🔄 In progress | — |
| M-PROC-01 | Procurement CE + OCA configuration complete: requisition, RFQ, PO, approval chain | 🔄 In progress | B-02, B-03 unblocked |
| M-HR-01 | HR CE configuration complete: employee records, leave, recruitment, org hierarchy | 🔄 In progress | — |
| M-ADM-01 | Administration configuration complete: fleet, assets, helpdesk (OCA), facility (custom spec) | 🔄 In progress | — |
| M-PC-01 | Project Coordination `project` module configuration complete | ⏳ | TO-BE delivered ✅ |
| M-CUSTOM-SPEC-01 | `nadf_payroll_ng` design spec approved | ⏳ | M-HR-01 |
| M-CUSTOM-SPEC-02 | `nadf_investment` design spec approved | ⏳ | Investment TO-BE delivered |
| M-CUSTOM-SPEC-03 | `nadf_legal_contract` design spec approved | ⏳ | Legal TO-BE complete |
| M-CUSTOM-SPEC-04 | `nadf_facility` design spec approved | ⏳ | Admin TO-BE delivered ✅ |
| M-CUSTOM-SPEC-05 | `nadf_vendor_compliance` design spec approved | ⏳ | Procurement TO-BE delivered ✅ |
| M-CUSTOM-SPEC-06 | `nadf_me_indicators` design spec approved | ⏳ | M&E TO-BE delivered |
| M-CUSTOM-DEV-01 through 06 | Custom module development for each spec | ⏳ | Corresponding spec approved |
| M-LSU-BUILD | Legal Odoo build (after TO-BE complete) | ⏳ | Legal TO-BE complete |
| M-STR-BUILD | Strategy Odoo build | ⏳ | Strategy TO-BE complete |
| M-COM-BUILD | Communications Odoo build | ⏳ | Communications TO-BE complete |
| M-SA-BUILD | Sustainable Agriculture Odoo build | ⏳ | SA TO-BE complete |
| M-INV-BUILD | Investment Odoo build (`nadf_investment`) | ⏳ | Investment TO-BE + M-CUSTOM-DEV-02 |
| M-ME-BUILD | M&E Odoo build | ⏳ | M&E TO-BE + M-CUSTOM-DEV-06 |
| M-EXEC-BUILD | Executive Management build | ⏳ | Exec TO-BE complete |
| M-UAT-01 | Full UAT cycle | ⏳ | All Phase 2 builds complete |
| M-DEPLOY-01 | Production go-live | ⏳ | UAT passed |
| M-TEMPLATE-01 | Public Sector ERP Template extraction | ⏳ | M-DEPLOY-01 |

---

## SECTION 11 — GOVERNANCE REQUIREMENTS

### Repository
- Feature branch per milestone; PRs required to merge to `main`
- Branch protection on `main`: no direct push
- Commit format: `[DEPT-MILESTONE] Description` (e.g. `[PROC-M01] Configure purchase_request approval chain`)
- All control documents updated and committed before milestone branch is merged

### OCA module governance
- Only modules from `github.com/OCA` installed without explicit user approval
- Each OCA module logged in `docs/DECISION_LOG.md` with rationale and version pinned
- OCA modules version-pinned in `requirements.txt`

### Custom module governance
- Design spec at `docs/modules/[MODULE_NAME]_spec.md` approved before development
- Spec includes: purpose, capability map reference, data model, business rules, UI, test cases, acceptance criteria
- Stored in `addons/` or `custom_addons/` (verify path during discovery)
- Module name: `nadf_` prefix; `__manifest__.py` fully populated

### Backup
- Daily automated PostgreSQL backup with documented restore procedure at `docs/BACKUP_STRATEGY.md`
- Repository: GitHub remote confirmed pushing

---

## SECTION 12 — GOVERNANCE ACTIVATION GATE

Run before any implementation begins. Produce `docs/GOVERNANCE_GATE_REPORT.md`.

### Gate A — Repository
| Check | Pass Criterion |
|-------|---------------|
| Git initialised | `git status` returns valid repo |
| Remote configured | `git remote -v` shows remote URL |
| `main` branch exists | confirmed |
| Feature branch workflow | at least one non-main branch or PR history |

### Gate B — GitHub
| Check | Pass Criterion |
|-------|---------------|
| Branch protection on `main` | confirmed |
| PR workflow enabled | direct push to `main` blocked |
| CI configured | `.github/workflows/` contains workflow file(s) |

### Gate C — Governance Documents
| Check | Pass Criterion |
|-------|---------------|
| Control Tower | `docs/CONTROL_TOWER.md` present and populated |
| Product Backlog | `docs/PRODUCT_BACKLOG.md` present and populated |
| Milestone Register | `docs/MILESTONE_REGISTER.md` present and populated |
| Decision Log | `docs/DECISION_LOG.md` present and populated |
| Changelog | `CHANGELOG.md` present and populated |
| Product State Index | `docs/PRODUCT_STATE_INDEX.md` present |
| Next Action | `docs/NEXT_ACTION.md` present and current |

### Gate D — Backup
| Check | Pass Criterion |
|-------|---------------|
| Backup strategy documented | `docs/BACKUP_STRATEGY.md` exists |
| Restore procedure documented | included in same doc |
| Last backup confirmed | file exists; timestamp within 24 hours |

### Gate E — Product
| Check | Pass Criterion |
|-------|---------------|
| Capability Map present | Section 6 loaded or `docs/CAPABILITY_MAP.md` exists |
| Platform confirmed as CE | Entry in `docs/DECISION_LOG.md` confirming Odoo 17 CE |
| No Enterprise modules installed | Odoo DB audit confirms zero Enterprise-only modules |

**Report format:**
```
GOVERNANCE ACTIVATION GATE REPORT
===================================
Date: YYYY-MM-DD

Gate A — Repository:    PASS / FAIL ([n]/4 checks)
Gate B — GitHub:        PASS / FAIL ([n]/3 checks)
Gate C — Documents:     PASS / FAIL ([n]/7 checks)
Gate D — Backup:        PASS / FAIL ([n]/3 checks)
Gate E — Product:       PASS / FAIL ([n]/3 checks)

OVERALL: PASS / FAIL ([n]/20 checks)

BLOCKERS:
  [Each FAIL with required action]
```

---

## SECTION 13 — PRODUCT MEMORY SYSTEM

The NADF ERP product lives in the repository, not in a chat window.

### Core files
| File | Purpose |
|------|---------|
| `docs/NEXT_ACTION.md` | First file read each session — immediate answer to "what next?" |
| `docs/PRODUCT_STATE_INDEX.md` | Session initialisation sequence |
| `docs/CONTROL_TOWER.md` | Current phase, milestone, blockers, completion |
| `docs/PRODUCT_BACKLOG.md` | All work items and statuses |
| `docs/MILESTONE_REGISTER.md` | Milestone history and queue |
| `docs/DECISION_LOG.md` | All decisions with rationale |
| `docs/IMPLEMENTATION_HISTORY.md` | Completed milestone records |
| `CHANGELOG.md` | Programme-level changelog |

### NEXT_ACTION.md format
```markdown
# NADF ERP — Next Action
**Last updated:** YYYY-MM-DD

## Current Phase
Phase [N] — [Name]

## Current Department/Module
[Name and brief status]

## Current Milestone
[ID] — [Name]

## Current Blocker
[Description, or "None"]

## Next Recommended Action
[One paragraph — specific, actionable, unambiguous — what Claude Code does in the very next session]

## Files to read before starting
1. [path]
2. [path]
```

---

## SECTION 14 — PRODUCT HIERARCHY

```
Software Factory
└── Odoo Platform (Odoo 17 Community Edition)
    └── Public Sector ERP Template  ← extracted from NADF in Phase 5
        └── NADF Deployment         ← Reference Implementation #1 (current engagement)
```

NADF is not the template. It is the reference implementation from which the template is extracted. The template is the reusable, client-agnostic layer. Every deliverable produced for NADF should be engineered with this extraction in mind.

---

## SECTION 15 — DISCOVERY REQUIREMENTS FOR CLAUDE CODE

**Claude Code must complete all discovery steps and produce the discovery report before writing a single line of implementation code.**

### Discovery commands
```bash
# Repository
ls /Users/mac/nadf_erp
cd /Users/mac/nadf_erp && git status && git log --oneline -20
git remote -v && git branch -a
ls docs/ 2>/dev/null
ls addons/ 2>/dev/null || ls custom_addons/ 2>/dev/null

# GitHub
gh repo view --json defaultBranchRef,branchProtectionRules 2>/dev/null
ls .github/workflows/ 2>/dev/null

# Odoo version and config
python3 /Users/mac/odoo17/odoo-bin --version 2>/dev/null
find /Users/mac/odoo17 -name "*.conf" | head -5 | xargs grep -i addons_path 2>/dev/null

# Database
psql -U odoo -l 2>/dev/null | grep -i nadf

# Installed modules — run after confirming DB name
# psql -U odoo -d [DBNAME] -c "SELECT name, state FROM ir_module_module WHERE state='installed' ORDER BY name;"

# CRITICAL — Enterprise module audit
# psql -U odoo -d [DBNAME] -c "SELECT name FROM ir_module_module WHERE state='installed' AND name IN ('approvals','documents','sign','web_studio','knowledge','hr_payroll','spreadsheet_dashboard','documents_spreadsheet');"

# Backup
ls ~/odoo_backups/ 2>/dev/null || ls /var/backups/odoo/ 2>/dev/null
```

### Discovery report format
```
NADF ERP — DISCOVERY REPORT
============================
Date: YYYY-MM-DD

REPOSITORY
  Path:                    [confirmed / not found]
  Git status:              [clean / uncommitted changes]
  Branch:                  [name]
  GitHub remote:           [URL / not set]
  Branch protection:       [YES / NO / UNKNOWN]
  CI workflows:            [file names / NONE]
  Governance docs present: [list]
  Addons path:             [path / not found]

ODOO
  Version:                 [x.x.x / not found]
  CE vs EE:                [CE / EE / UNKNOWN]
  Database:                [name / not found]
  Enterprise modules found:[list / NONE]  ← critical
  OCA modules installed:   [list / NONE]
  Custom modules found:    [list / NONE]

BACKUP
  Dir found:               [YES / NO — path]
  Last backup:             [timestamp / UNKNOWN]

GATE PRELIMINARY
  Gate A (Repo):           PASS / FAIL
  Gate B (GitHub):         PASS / FAIL
  Gate C (Docs):           PASS / FAIL
  Gate D (Backup):         PASS / FAIL
  Gate E (Product):        PASS / FAIL

FIRST RECOMMENDED ACTION:
  [One specific action]
```

---

## SECTION 16 — IMPLEMENTATION SEQUENCE

After discovery and governance gate:

1. **M-PLATFORM-CORRECTION** — Audit Enterprise modules; rewrite affected backlog items; log CE platform decision in Decision Log
2. **M-GOVERNANCE-GATE** — Produce Gate Report; fix all FAILs; commit scaffold to repo
3. **M-OCA-01** — Install `mis_builder`, `helpdesk_mgmt`, `purchase_request`, `purchase_requisition`; log each in Decision Log
4. **M-FIN-01, M-HR-01, M-ADM-01, M-PROC-01** — Phase 1 CE configuration (can overlap where not dependent)
5. **M-PC-01** — Project Coordination module configuration
6. **Custom module specs** — M-CUSTOM-SPEC-01 through 06 (sequenced against their TO-BE dependencies)
7. **Custom module development** — M-CUSTOM-DEV-01 through 06 (against approved specs)
8. **Phase 2 department builds** — Legal, Strategy, Communications, SA, Investment, M&E, Executive (each triggered when corresponding TO-BE is delivered by Claude Desktop)
9. **M-UAT-01** — Full UAT
10. **M-DEPLOY-01** — Production go-live
11. **M-TEMPLATE-01** — Template extraction

---

## SECTION 17 — SESSION START RULES

1. Read `docs/NEXT_ACTION.md`
2. Read `docs/PRODUCT_STATE_INDEX.md`
3. Read `docs/CONTROL_TOWER.md`
4. Read `docs/PRODUCT_BACKLOG.md` (scan statuses)
5. Read current department/module status file
6. Run `git status` + `git log --oneline -10`

Then state:
- Current phase
- Current milestone
- Current blockers
- Next action

**Do not begin work until state is confirmed.**

---

## SECTION 18 — SESSION END RULES

Update in this order, commit before closing:

1. `docs/NEXT_ACTION.md`
2. `docs/CONTROL_TOWER.md`
3. `docs/PRODUCT_BACKLOG.md`
4. `docs/MILESTONE_REGISTER.md`
5. Relevant department status file
6. `docs/IMPLEMENTATION_HISTORY.md`
7. `docs/DECISION_LOG.md` (if decision made)
8. `CHANGELOG.md`
9. `docs/session_logs/YYYY-MM-DD_SESSION_SUMMARY.md`

Commit: `[SESSION-END] YYYY-MM-DD governance update`

**No milestone is closed until all files are updated and pushed.**

---

## SECTION 19 — CLAUDE DESKTOP / CLAUDE CODE BOUNDARY

| Responsibility | Claude Desktop | Claude Code |
|---------------|----------------|-------------|
| Business process documentation | ✅ Primary | Reads as spec input only |
| TO-BE functional specification | ✅ Produces | Implements in Odoo |
| Swimlane HTML diagrams | ✅ Produces | Does not produce |
| ERP module mapping & requirements | ✅ Analyses | Implements |
| Transfer package | ✅ Produces & maintains | Receives and loads |
| Local repository | ❌ No access | ✅ Primary |
| Odoo instance | ❌ No access | ✅ Primary |
| GitHub, PRs, CI | ❌ No access | ✅ Primary |
| Database | ❌ No access | ✅ Primary |
| Custom module code | ❌ No | ✅ Primary |
| Repository governance documents | Provides content | Commits to repo |

**What Claude Desktop may claim:**
> *"Based on the NADF project materials available in this Claude Desktop project folder…"*

**What Claude Desktop must never claim:**
Direct knowledge of the local repository, Odoo instance, installed modules, Git history, database state, or GitHub configuration — unless the user has explicitly pasted that information into the conversation.

---

*End of NADF Full Product Transfer Package v2.1 — 2026-06-20*
*Prepared by Claude Desktop from NADF BPOGS project folder materials only.*
*This document is authoritative. Supersedes v2.0 and all prior versions.*
