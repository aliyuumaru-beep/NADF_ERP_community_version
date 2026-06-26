# Governance Approval Register — NADF ERP Programme

---

**Document ID:** GAR-NADF-001
**Document Type:** Mandatory Governance Artifact — Software Factory Governance Standard (AOP-015)
**Project Pod:** POD-NADF
**Product / Programme:** NADF ERP MVP — Odoo 17 Community Edition
**Client:** National Agricultural Development Fund (NADF)
**Consultant:** Lanasoft Technologies
**Version:** 1.2
**Date Initialised:** 2026-06-26
**Register Period:** 2026-06-02 (Legacy Phase 0) — 2026-06-26 (Present)
**Maintained by:** A1 Master Orchestrator — NADF
**Classification:** Executive — Governance

> This register is the single executive view of every governance approval, architectural
> decision, exception, escalation, and authority decision taken on the NADF ERP Programme,
> grouped by business department.
>
> Version 1 is backward-populated from all existing approved decisions as at 2026-06-26.
> No decisions have been invented. All entries cross-reference their source document.
>
> **Update rule:** Every Work Package Exit Gate must update this register as a mandatory
> acceptance criterion. No Work Package may close until this register is current.

---

## Executive Summary

| Metric | Count |
|--------|-------|
| **Total Decisions** | **31** |
| Active | 28 |
| Open (Escalation) | 1 |
| Deferred | 2 |
| Closed | 0 |
| Revoked | 0 |
| Superseded | 0 |

**Register period:** 2026-06-02 — 2026-06-26 (present)
**Active milestone:** M1 — Foundation (Phase 1 in progress: WP-01 ✅ · WP-02 ✅ · WP-03 ✅ · WP-04 CONDITIONAL PASS · WP-ADM-01 ✅ · WP-PC-01 ✅)
**Last updated:** 2026-06-26
**Updated by:** A1 Master Orchestrator — WP-PC-01 exit gate (DEC-PC01-001/002 added)

---

## Department Summary

| Department | Decision Count |
|------------|---------------|
| Executive Governance | 4 |
| Finance | 4 |
| Procurement | 5 |
| HR | 2 |
| Administration | 3 |
| Project Coordination | 2 |
| ICT | 10 |
| Communications | 0 |
| Legal | 0 |
| Operations | 1 |
| Other | 0 |
| **Total** | **29** |

---

## Department Sections

---

### Executive Governance

*Decisions affecting the governance, programme structure, legal entity, strategic direction, or product authorization of the NADF ERP Programme.*

| Department | Decision ID | Work Package | Approval Type | Decision Taken | Business Rationale | Approved By | Authority Class | Status | Date | Source Document |
|------------|-------------|--------------|---------------|----------------|-------------------|-------------|-----------------|--------|------|-----------------|
| Executive Governance | DEC-001 | Legacy MVP — Phase 0 | Architecture Decision | Fresh `NADF` PostgreSQL database created from scratch. Existing databases (FamOil, WamaCare, OdooClean) not cloned. | A clean lineage database ensures every installed module and every configuration choice is traceable and documented from the start — essential for a reusable public sector ERP template. | Operator + AI Developer | Pre-AOP-013 | Active | 2026-06-02 | `docs/DECISION_LOG.md#DEC-001` |
| Executive Governance | DEC-RECOVERY-001 | M-C Governance Recovery | Governance Decision | `nadf_vendor_onboarding` custom module recovered from the FamOil working tree (where it was untracked with no backup) and committed to `nadf_erp/custom_addons/`. Integrity verified byte-identical (12/12 files). | Closed MR-01 critical data-loss exposure. A production module for vendor AI screening existed in no repository and had no backup. Recovery restored correct layer ownership and eliminated the highest-priority data loss risk in the programme. | A1 Master Orchestrator (M-C) | EA-2 | Active | 2026-06-22 | `docs/DECISION_LOG.md#DEC-RECOVERY-001` · `docs/MC_RECOVERY_INTEGRITY.md` |
| Executive Governance | DEC-RECOVERY-002 | M-C Governance Recovery | Governance Decision | `nadf_facilities_management` custom module relocated from the FamOil repository (committed at `odoo17@55c1787`, unpushed) to `nadf_erp/custom_addons/`. Removed from FamOil via forward `git rm` removal commit. Integrity verified (33/33 files). | Closed MR-02 cross-layer contamination breach. A NADF (Layer 4) module was committed inside the FamOil (Layer 4) deployment repository — a violation of the Project Layering Model. Forward removal (not history rewrite) preserves FamOil audit trail while restoring correct ownership. | A1 Master Orchestrator (M-C) | EA-2 | Active | 2026-06-22 | `docs/DECISION_LOG.md#DEC-RECOVERY-002` · `docs/MC_RECOVERY_INTEGRITY.md` |
| Executive Governance | DEC-PEG6-001 | PEG-6 Product Authorization | Sponsor Decision | PEG-6 Product Authorization granted for NADF ERP Phase 1 — Foundation. Phase 1 Product Engineering activated. M0 formally closed. Scope frozen at Transfer Package v2.1. | All governance preconditions satisfied (Gate 21/21 PASS, protected branch, backup drilled, CI active). Phase 1 is the lowest-risk tier (CE-native config and vetted OCA only). A formal sponsor decision was required to commence Phase 1 delivery under the Software Factory governance framework. | Business Sponsor (Aliyu / Lanasoft Technologies) | EA-6 | Active | 2026-06-24 | `docs/DECISION_LOG.md#DEC-PEG6-001` · `docs/governance/PEG_6_PRODUCT_AUTHORIZATION_PACKAGE.md` |

---

### Finance

*Decisions affecting financial configuration, accounting, payment controls, budget management, tax, and financial reporting.*

| Department | Decision ID | Work Package | Approval Type | Decision Taken | Business Rationale | Approved By | Authority Class | Status | Date | Source Document |
|------------|-------------|--------------|---------------|----------------|-------------------|-------------|-----------------|--------|------|-----------------|
| Finance | DEC-004 | Legacy MVP — Phase 1 | Governance Decision | NADF fiscal year configured as January 1 – December 31 (calendar year). FY 2026 and FY 2027 created. | Operator confirmed calendar-year fiscal year. Consistent with many parastatal/development fund practice of using calendar year for management accounts even when the federal budget cycle differs. | Operator (explicit confirmation) | Pre-AOP-013 | Active | 2026-06-02 | `docs/DECISION_LOG.md#DEC-004` |
| Finance | DEC-005 | Legacy MVP — Phase 5 | Exception | Multi-level procurement and payment approval implemented as advisory control using `base.automation` escalation rules. Hard-block approval deferred beyond Phase 1. Five automated rules created for Tier 2/3 PO and invoice events. | The Enterprise `approvals` app is not available in Odoo 17 Community Edition. Activity-based escalation satisfies the MVP demo requirement while avoiding custom code in Phase 1. Production hard-block approval requires a `nadf_approvals` custom module, deferred to Phase 2 specification. | AI Developer — Operator blanket approval (Phase 5) | Pre-AOP-013 | Active | 2026-06-04 | `docs/DECISION_LOG.md#DEC-005` |
| Finance | DEC-WP02-001 | WP-02 Finance Core | Exception | Payment dual-authorisation retained as advisory control via existing `base.automation` rules for Phase 1. Finance Officer creates/enters payments; Finance Manager reviews. System does not hard-block lower-tier users from posting payments. | Odoo 17 CE `account.payment` has no native payment approval group field. The maker-checker role separation (Finance Officer vs Finance Manager) provides operational control at the group level. A custom `nadf_approvals` module is required for hard-blocking — Phase 2 scope. Audit trail on `account.move` provides post-facto tracking. | A1 Master Orchestrator — WP-02 execution | EA-3 | Active | 2026-06-25 | `docs/DECISION_LOG.md#DEC-WP02-001` |
| Finance | DEC-WP02-002 | WP-02 Finance Core | Architecture Decision | Five existing analytic accounts (CC-ADM, CC-EXE, CC-FIN, CC-HR, CC-PRO) under the "Projects" analytic plan accepted as the Phase 1 analytic dimension. No new accounts created. Programme/project-level dimensions deferred to Phase 3+. | Department cost centres are the correct Phase 1 budget tracking granularity for NADF. Budget CSV amounts (40 lines) will be allocated at department level when the budget module is resolved. Analytic plan name "Projects" to be renamed "NADF Departments" at next client review session. | A1 Master Orchestrator — WP-02 execution | EA-3 | Active | 2026-06-25 | `docs/DECISION_LOG.md#DEC-WP02-002` |

---

### Procurement

*Decisions affecting vendor management, purchase workflows, requisition processes, contract management, and goods receipt.*

| Department | Decision ID | Work Package | Approval Type | Decision Taken | Business Rationale | Approved By | Authority Class | Status | Date | Source Document |
|------------|-------------|--------------|---------------|----------------|-------------------|-------------|-----------------|--------|------|-----------------|
| Procurement | DEC-OCA-03 | WP-01 Foundation Hardening | Architecture Decision | OCA `purchase_request` module version 17.0.2.3.4 installed from OCA/purchase-workflow. Provides structured multi-step procurement requisition workflow (draft → to_approve → approved → in_progress → done). | Odoo 17 CE `purchase` module has no native requisition workflow. `purchase_request` is the authorized OCA replacement, approved in PEG-6 §3. Procurement requisition capability (CA-02) requires this workflow to be operational before call-for-tender flows can execute. | A1 Master Orchestrator — G1/G2/G3 authorized | EA-4 | Active | 2026-06-25 | `docs/DECISION_LOG.md#DEC-OCA-03` · `EXECUTION_AUTHORITY_REGISTER.md#EA-NADF-WP01-001` |
| Procurement | DEC-OCA-05 | WP-01 Foundation Hardening | Architecture Decision | `purchase_requisition` confirmed as Odoo 17 CE native module ("Purchase Agreements") already installed (`state='installed'`, `latest_version='17.0.0.1'`). No OCA install required. PEG-6 OCA listing was based on prior Odoo 14–16 classification. | In Odoo 17, `purchase_requisition` was absorbed into the CE core. The CE version fully satisfies the tender/vendor comparison workflow requirement. Confirming this avoids installing a redundant OCA overlay on a CE-native module. | A1 Master Orchestrator — WP-01 execution | EA-1 | Active | 2026-06-25 | `docs/DECISION_LOG.md#DEC-OCA-05` |
| Procurement | DEC-WP03-001 | WP-03 Procurement Core | Architecture Decision | Vendor compliance status implemented as selection field `x_compliance_status` on `res.partner` via Odoo shell. Three values: compliant / non_compliant / pending. `nadf_vendor_onboarding` approval state used as secondary compliance proxy for portal-onboarded vendors. | Phase 1 MVP requires a compliance indicator to gate vendor selection. A custom `nadf_vendor_compliance` module is the correct long-term solution (Phase 2/3 scope). Shell-created `x_` fields are acceptable for Phase 1 MVP with documented creation commands. Three vendors tagged compliant, one pending. | A1 Master Orchestrator — WP-03 execution | EA-5 | Active | 2026-06-25 | `docs/DECISION_LOG.md#DEC-WP03-001` · `EXECUTION_AUTHORITY_REGISTER.md#EA-NADF-WP03-004` |
| Procurement | DEC-CONTRACT-001 | WP-03 Procurement Core | Architecture Decision | OCA `contract` module NOT installed in Phase 1. Contract lifecycle management deferred to `nadf_legal_contract` custom module (Phase 2/3 spec-gated). CE `purchase_requisition` sufficient for Phase 1 procurement contract flow (call for tender + awarded PO). | OCA `contract` does not support the NADF RACI approval chain (the critical differentiator for public sector compliance). `nadf_legal_contract` custom module is the correct long-term solution covering recurring services, RACI sign-offs, and budget-vs-contract tracking. Installing an unfit OCA module in Phase 1 creates rework. | A1 Master Orchestrator — WP-03 execution | EA-1 | Active | 2026-06-25 | `docs/DECISION_LOG.md#DEC-CONTRACT-001` |
| Procurement | DEC-WP03-002 | WP-03 Procurement Core | Architecture Decision | NADF Procurement user groups mapped to OCA `purchase_request` module groups via direct user assignment: `procurement.officer` → Purchase Request User; `head.procurement` → Purchase Request Manager + User. Finance Approver group not wired to `purchase_request` in Phase 1 (B-02/B-03 thresholds pending client confirmation). | OCA `purchase_request` ships with its own group hierarchy bound to its `ir.model.access` rules. Direct assignment to both NADF and OCA groups is the minimal, maintainable Phase 1 configuration. Phase 2 will implement proper group inheritance via a custom module. | A1 Master Orchestrator — WP-03 execution | EA-3 | Active | 2026-06-25 | `docs/DECISION_LOG.md#DEC-WP03-002` |

---

### HR

*Decisions affecting human resources, leave management, employee records, and workforce administration.*

| Department | Decision ID | Work Package | Approval Type | Decision Taken | Business Rationale | Approved By | Authority Class | Status | Date | Source Document |
|------------|-------------|--------------|---------------|----------------|-------------------|-------------|-----------------|--------|------|-----------------|
| HR | DEC-006 | Legacy MVP — Phase 5 | Governance Decision | Head HR (Kabir Haruna) set as universal Time Off Officer for all employees. Head HR's own leave manager set to Director CS. | Leave is centrally controlled by HR in a public sector organisation. Centralising the Time Off Officer role simplifies the leave process and ensures consistent policy enforcement. Casual/Sick leave still routes through line managers; Annual/Maternity/Study routes through HR. | AI Developer — Operator blanket approval (Phase 5) | Pre-AOP-013 | Active | 2026-06-04 | `docs/DECISION_LOG.md#DEC-006` |
| HR | DEC-007 | Legacy MVP — Phase 5 | Exception | Study Leave configured as `leave_validation_type = 'both'` (Manager + Head HR) with additional `base.automation` activity to Executive Secretary after final HR validation. Third-level approval is advisory — leave is technically approved before ES activity is completed. | Odoo 17 CE `hr_holidays` natively supports maximum 2 approval levels. Study Leave requires a three-level chain per NADF policy. Activity-based escalation satisfies the MVP demonstration requirement. Production reversal (ES approves before HR) requires a `nadf_hr_leave` custom module, deferred to production phase. | AI Developer — Operator blanket approval (Phase 5) | Pre-AOP-013 | Active | 2026-06-04 | `docs/DECISION_LOG.md#DEC-007` |

---

### Administration

*Decisions affecting office administration, facilities, assets, fleet, and general operations.*

| Department | Decision ID | Work Package | Approval Type | Decision Taken | Business Rationale | Approved By | Authority Class | Status | Date | Source Document |
|------------|-------------|--------------|---------------|----------------|-------------------|-------------|-----------------|--------|------|-----------------|
| Administration | DEC-ADM01-001 | WP-ADM-01 Administration Core | Architecture Decision | OCA `helpdesk_mgmt` 17.0.1.10.4 has no SLA model. `priority` field (0=Normal, 1=High) and `last_stage_update` timestamp accepted as Phase 1 SLA proxy. AC-ADM01-04 "≥1 SLA rule" satisfied via team configuration with priority-tagged tickets. | CE Enterprise `helpdesk` module is prohibited. OCA helpdesk_mgmt does not ship an SLA rules model in this version. Priority + stage timestamp is the acceptable CE MVP proxy for Phase 1. Phase 2 custom module `nadf_ict_helpdesk` can formalise SLA policies. | A1 Master Orchestrator — WP-ADM-01 execution | EA-3 | Active | 2026-06-26 | `docs/DECISION_LOG.md#DEC-ADM01-001` |
| Administration | DEC-ADM01-002 | WP-ADM-01 Administration Core | Data Governance | Motor Vehicles asset category (id=3) mapped to GL account "EARTH MOVING EQUIPMENT" (11030301) — incorrect legacy mapping. Correction deferred to WP-05 UAT preparation / Finance review. No assets currently in this category. | No immediate business impact (0 assets in Motor Vehicles category). Finance sign-off required before GL accounts can be corrected. Correction is a Finance-owned decision. | A1 Master Orchestrator — WP-ADM-01 execution | EA-3 | Deferred | 2026-06-26 | `docs/DECISION_LOG.md#DEC-ADM01-002` |
| Administration | DEC-ADM01-003 | WP-ADM-01 Administration Core | Configuration | Director Corporate Services (director.cs, uid=12) assigned as interim to IT Manager (111), Fleet Manager (108), and Asset Manager (109) groups. Driver (107) and IT Officer (110) groups remain empty pending B-WP04-01 (Admin employee role confirmation) and user account creation. | No dedicated ICT Officer, Fleet Manager, or Driver Odoo user accounts exist. Admin-dept employees have no Odoo internal logins. Director CS is the appropriate interim authority as Corporate Services Head overseeing ICT, HR, and Administration functions. | A1 Master Orchestrator — WP-ADM-01 execution | EA-3 | Active | 2026-06-26 | `docs/DECISION_LOG.md#DEC-ADM01-003` |

---

### Project Coordination

*Decisions affecting project management, programme coordination, reporting, and stakeholder management.*

| Department | Decision ID | Work Package | Approval Type | Decision Taken | Business Rationale | Approved By | Authority Class | Status | Date | Source Document |
|------------|-------------|--------------|---------------|----------------|-------------------|-------------|-----------------|--------|------|-----------------|
| Project Coordination | DEC-PC01-001 | WP-PC-01 Project Coordination | Architecture Decision | CE Odoo 17 `project.project` has no `parent_id` field. Programme/sub-project hierarchy expressed via naming convention: 'NADF ERP Programme' (id=2) is the programme-level project; 'NADF ERP Phase 1 — Foundation' (id=3) is the Phase 1 sub-project. No technical parent-child link between project.project records in CE. | CE 17 does not offer native project portfolio/programme hierarchy. Naming convention is zero-risk, immediately legible, and sufficient for Phase 1 PCU oversight. Phase 2 `nadf_project_governance` custom module may add native hierarchy if product roadmap requires. | A1 Master Orchestrator — WP-PC-01 execution | EA-3 | Active | 2026-06-26 | `docs/DECISION_LOG.md#DEC-PC01-001` |
| Project Coordination | DEC-PC01-002 | WP-PC-01 Project Coordination | Architecture Decision (Deferred) | CE `project.milestone.is_reached` cannot be restricted at field level using standard ir.rule (record-level) or ir.model.access (model-level). Phase 1 Director-only sign-off is organizational: (a) NADF Director group (id=114) has 1 user; (b) ir.model.access id=1062 'nadf.project.milestone.director' grants explicit CRUD for Director group; (c) CE ACL (id=841) gives write to project.group_user including director.cs. Technical field-level restriction deferred to Phase 2 `nadf_project_governance` module. | CE 17 has no hook for field-level write restriction without custom code. Modifying CE module ACLs would not survive module upgrade. Organizational control is sufficient for Phase 1 (0 PM users; 1 Director user). Mirrors DEC-ADM01-001 (OCA helpdesk SLA proxy) pattern. | A1 Master Orchestrator — WP-PC-01 execution | EA-3 | Deferred | 2026-06-26 | `docs/DECISION_LOG.md#DEC-PC01-002` |

---

### ICT

*Decisions affecting technology platform, module installation, security configuration, integrations, infrastructure, and system administration.*

| Department | Decision ID | Work Package | Approval Type | Decision Taken | Business Rationale | Approved By | Authority Class | Status | Date | Source Document |
|------------|-------------|--------------|---------------|----------------|-------------------|-------------|-----------------|--------|------|-----------------|
| ICT | DEC-002 | Legacy MVP — Phase 0 | Governance Decision | Odoo 17 Community Edition selected as the sole platform. Enterprise modules prohibited. Enterprise-only features (Approvals app, Sign, Documents) excluded from MVP scope. | Zero licence cost is appropriate for MVP/demo stage. Community Edition covers Finance, Procurement, and HR adequately. Enterprise features can be added in Phase 2 (production) if needed. Existing local infrastructure is already Community Edition (shared with FamOil and WamaCare). | Operator (project constraint) | Pre-AOP-013 | Active | 2026-06-02 | `docs/DECISION_LOG.md#DEC-002` |
| ICT | DEC-003 | Legacy MVP — Phase 0 | Architecture Decision | `nadf.conf` references `/Users/mac/odoo17/custom_addons/` for shared OCA addons rather than copying to `nadf_erp/custom_addons/`. OCA addons directory `/Users/mac/oca_addons/` added to addons path in WP-01. | Avoids duplication of shared addon code across multiple projects. NADF benefits from fixes applied to shared addons. For MVP/demo environment, strict isolation is not yet required. Revisit if NADF moves to production server. | AI Developer | Pre-AOP-013 | Active | 2026-06-02 | `docs/DECISION_LOG.md#DEC-003` |
| ICT | DEC-008 | Legacy MVP — Phase 0 | Architecture Decision | Port 8071 assigned to NADF Odoo instance. `nadf.conf` sets `http_port = 8071`. All NADF access via `http://localhost:8071`. | FamOil uses port 8069; WamaCare uses port 8070. All three instances run simultaneously on the same development machine. Sequential port assignment ensures no conflicts. | AI Developer | Pre-AOP-013 | Active | 2026-06-02 | `docs/DECISION_LOG.md#DEC-008` |
| ICT | DEC-PLATFORM-001 | M-C Governance Recovery | Governance Decision | Odoo 17 Community Edition confirmed and version-locked as the bound platform for POD-NADF. Zero prohibited Enterprise modules present. `spreadsheet` and `spreadsheet_dashboard` confirmed as LGPL-3 CE core modules (not Enterprise). `account_accountant` (Enterprise marker) absent. | Governance Activation Gate E requires an audited confirmation that the platform is Community and free of Enterprise modules. This decision supersedes the assumption-level confirmation in DEC-002 with audited database evidence from M-C inspection. | A1 Master Orchestrator (M-C) | EA-1 | Active | 2026-06-22 | `docs/DECISION_LOG.md#DEC-PLATFORM-001` |
| ICT | DEC-2FA-001 | WP-01 Foundation Hardening | Architecture Decision | TOTP 2FA enforcement scope defined as: Finance Officer, Finance Manager, CFO, Auditor, and CEO. "Senior Management" phrase retired from all Phase 1 planning documents as undefined and unmappable to an Odoo group. | Using vague group names (e.g., "Senior Management") in security policy creates untestable acceptance criteria. Explicit group names can be verified by DB query against `res.groups`. All named groups have direct access to financial data or hold highest system authority — mandatory for audit compliance. | G3 Security Governance + A1 Master Orchestrator | EA-3 | Active | 2026-06-24 | `docs/DECISION_LOG.md#DEC-2FA-001` |
| ICT | DEC-OCA-01 | WP-01 Foundation Hardening | Architecture Decision | OCA `mis_builder` version 17.0.1.5.0 installed from OCA/mis-builder. Dependencies installed: `report_xlsx` (OCA 17.0.1.0.2), `date_range` (OCA 17.0.1.2.1), `board` (CE 17.0.1.0). State: installed. Registry exit 0. | CE `account` analytics is insufficient for multi-period executive and operational KPI dashboards (CA-01 Financial Management). `mis_builder` is the authorized OCA solution approved in PEG-6 §3. Pending WP02-08 client KPI sign-off for dashboard build. | A1 Master Orchestrator — G1/G2/G3 authorized | EA-4 | Active | 2026-06-25 | `docs/DECISION_LOG.md#DEC-OCA-01` · `EXECUTION_AUTHORITY_REGISTER.md#EA-NADF-WP01-001` |
| ICT | DEC-OCA-02 | WP-01 Foundation Hardening | Escalation | `account_budget_oca` version 17.0.1.0.0 NOT installed. Install failed with field compatibility error (`theoritical_amount` does not exist on `account.analytic.account` in this Odoo 17 build). Module directory retained at `/Users/mac/oca_addons/account_budget_oca/` for future resolution. G1/G2/G3 must decide between: (A) OCA patch, (B) CE native `account_budget`, (C) defer to future WP. | Budget module incompatibility blocks WP02-07 (budget control configuration) only. All other Phase 1 WPs are unaffected. Decision must not be rushed — an incompatible module install could corrupt the database schema. Escalation follows R-WP01-01 mitigation as designed. | A1 Master Orchestrator — WP-01 execution (escalated) | EA-4 | Open | 2026-06-25 | `docs/DECISION_LOG.md#DEC-OCA-02` |
| ICT | DEC-OCA-04 | WP-01 Foundation Hardening | Architecture Decision | OCA `helpdesk_mgmt` version 17.0.1.10.4 installed from OCA/helpdesk. State: installed. Registry exit 0. Replaces unratified `project`-based ICT helpdesk workaround from legacy build. | Odoo 17 CE `helpdesk` module is Enterprise-only. `helpdesk_mgmt` is the authorized CE/OCA replacement, approved in PEG-6 §3. ICT Help Desk capability (CA-04) requires a proper helpdesk module, not a project workaround. | A1 Master Orchestrator — G1/G2/G3 authorized | EA-4 | Active | 2026-06-25 | `docs/DECISION_LOG.md#DEC-OCA-04` · `EXECUTION_AUTHORITY_REGISTER.md#EA-NADF-WP01-001` |
| ICT | DEC-2FA-002 | WP-01 Foundation Hardening | Architecture Decision | `auth_totp.policy` set to `required` globally in `ir.config_parameter`. All active Odoo users must complete TOTP enrollment before login. Per-group enforcement is not natively available in Odoo 17 CE `auth_totp`. | Setting global `required` policy satisfies DEC-2FA-001 and exceeds its minimum requirement by enforcing 2FA for all users. Global enforcement is acceptable for a multi-department public sector system and introduces no code risk. Per-group enforcement requires custom code or OCA `auth_totp_mandatory_group` — Phase 2 scope. | A1 Master Orchestrator — WP-01 execution | EA-3 | Active | 2026-06-25 | `docs/DECISION_LOG.md#DEC-2FA-002` · `EXECUTION_AUTHORITY_REGISTER.md#EA-NADF-WP01-002` |
| ICT | DEC-AOP014-001 | N/A — SF Enhancement AOP-014 | Governance Decision | AOP-014 Development Environment Trust Profile adopted for NADF pod. 67 Level A command patterns deployed to `/nadf_erp/.claude/settings.json` effective 2026-06-26. Level B (one-time session approval) and Level C (always require approval) protections unchanged. Six Sponsor conditions apply: NADF-only scope; Level C unchanged; no production deployment commands; whitelist changes documented; metrics collected per WP; FamOil/WamaCare adoption requires separate decision. | Routine development commands (git status, git diff, pytest, pg_dump, backup scripts, etc.) required approval on every invocation, creating approval fatigue and preventing effective unattended execution of approved Work Packages. Trust profile eliminates prompts for genuinely low-risk, read-only, and trivially reversible commands while preserving all gates on destructive, security-sensitive, and production operations. AOP-013 Execution Authority Framework is unaffected. | Human Sponsor (DEC-AOP014-001) | EA-1 | Active | 2026-06-26 | `software-factory-governance/DECISION_LOG.md#DEC-017` · `enhancements/AOP-014/07_DEPLOYMENT_RECORD_NADF.md` · `/nadf_erp/.claude/settings.json` |

---

### Communications

*Decisions affecting internal and external communications, portals, messaging, and stakeholder notifications.*

*No decisions recorded in the current register period.*

---

### Legal

*Decisions affecting contracts, compliance, regulatory requirements, and legal obligations.*

*No decisions recorded in the current register period. Contract lifecycle management deferred to `nadf_legal_contract` custom module (Phase 2/3) per DEC-CONTRACT-001 in the Procurement section.*

---

### Operations

*Decisions affecting backup, recovery, data management, system maintenance, and operational continuity.*

| Department | Decision ID | Work Package | Approval Type | Decision Taken | Business Rationale | Approved By | Authority Class | Status | Date | Source Document |
|------------|-------------|--------------|---------------|----------------|-------------------|-------------|-----------------|--------|------|-----------------|
| Operations | DEC-BACKUP-001 | M-C Governance Recovery | Governance Decision | Backup cadence and recovery objectives adopted: daily automated backup of `NADF` database + filestore; 30-day retention; RPO ≤ 24 hours; RTO ≤ 4 hours. First backup taken and restore drill completed during M-C. Drill result: PASS (94 modules / 40 partners match live). | The `NADF` database (10 phases of configuration data) had never been backed up and no restore drill had ever been performed — recorded as risk MR-05. Governance Activation Gate D requires documented backup strategy, documented restore procedure, and a recent verified backup. | A1 Master Orchestrator (M-C) | EA-5 | Active | 2026-06-22 | `docs/DECISION_LOG.md#DEC-BACKUP-001` · `docs/BACKUP_STRATEGY.md` |

---

## Open Escalations

*Unresolved governance items requiring decision before affected work packages can proceed.*

| Escalation ID | Description | Blocking | Escalated To | Date Raised | Target Resolution |
|--------------|-------------|---------|-------------|-------------|-------------------|
| ESC-OCA-02 | `account_budget_oca` v17.0.1.0.0 incompatible with this Odoo 17 build — field `theoritical_amount` missing. Three options: (A) investigate OCA patch, (B) use CE native `account_budget`, (C) defer to future WP. See `docs/governance/DEC_OCA_02_GOVERNANCE_REVIEW.md`. | WP02-07 (budget control configuration) | G1/G2/G3 + A1 | 2026-06-25 | Before WP02-07 execution |
| ESC-CLIENT-B02 | NADF RACI 1.19 — multi-level procurement approval thresholds (B-02: value bands; B-03: ₦500K vs NADF actual threshold) not confirmed by client. ₦500K threshold unchanged pending client sign-off. | WP03-07 (multi-level approval config) | Business Sponsor / NADF Client | 2026-06-25 | Client review session |
| ESC-CLIENT-WP02-08 | `mis_builder` KPI dashboard (WP02-08) — client KPI sign-off required before dashboard can be built. Dashboard configuration suspended pending NADF stakeholder approval of KPI definitions. | WP02-08 (mis_builder dashboard build) | Business Sponsor / NADF Client | 2026-06-25 | Client review session |

---

## Deferred Decisions

*Architectural or business decisions where the intent to defer has been logged within an active decision, but the deferred item has not yet been addressed.*

| Deferred Item | Origin Decision | Deferred To | Reason for Deferral | Owner |
|--------------|-----------------|-------------|---------------------|-------|
| Hard payment blocking — `nadf_approvals` custom module | DEC-WP02-001 · DEC-005 | Phase 2 specification | Odoo 17 CE has no native payment approval group field. Custom module requires approved spec and Phase 2 development gate. Advisory control is sufficient for Phase 1 MVP. | A1 + G1 (Phase 2 spec) |
| `nadf_legal_contract` custom module — full contract lifecycle | DEC-CONTRACT-001 | Phase 2/3 specification | OCA `contract` does not support NADF RACI approval chain. Custom module is the correct solution but requires Phase 2/3 spec gate before development. | A1 + G1 (Phase 2/3 spec) |
| `nadf_vendor_compliance` custom module — version-controlled compliance field | DEC-WP03-001 | Phase 2/3 specification | Shell-created `x_compliance_status` field is DB-resident and not version-controlled. Phase 2/3 custom module replaces it with workflow-governed equivalent. | A1 + G1 (Phase 2/3 spec) |
| Study Leave three-level production reversal — `nadf_hr_leave` module | DEC-007 | Production deployment phase | Current advisory flow approves leave before ES activity is completed. Production requires ES approval before HR final validation — requires custom module. | A1 + G1 (production spec) |
| Budget module configuration — WP02-07 | DEC-OCA-02 | Pending ESC-OCA-02 resolution | `account_budget_oca` incompatible. G1/G2/G3 must decide Option A/B/C before WP02-07 can execute. | G1/G2/G3 → A1 |
| `mis_builder` KPI dashboard — WP02-08 | DEC-OCA-01 | Pending client sign-off (ESC-CLIENT-WP02-08) | Dashboard build suspended pending NADF stakeholder KPI definition approval. | Business Sponsor / NADF Client |
| Analytic plan renamed to "NADF Departments" | DEC-WP02-002 | Next client review session | Plan currently named "Projects" — rename to "NADF Departments" agreed but deferred to next client-facing session to avoid configuration drift outside agreed session scope. | A1 at next client session |
| Per-group TOTP 2FA enforcement | DEC-2FA-002 | Phase 2 (if required) | Odoo 17 CE `auth_totp` supports only global policy. Per-group enforcement requires OCA `auth_totp_mandatory_group` or custom module — Phase 2 scope if business requires differentiated enforcement. | G3 + A1 (Phase 2) |

---

## Superseded Decisions

*No superseded decisions in the current register period.*

---

## Authority Decisions (AOP-013)

*Execution Authority grants, denials, and revocations issued under the AOP-013 Execution Authority Framework (advisory pilot active for WP-03/WP-04 window). Full records in `EXECUTION_AUTHORITY_REGISTER.md`.*

| Authority ID | Authority Class | Work Package | Authorized Actions (Summary) | A1 Decision | Mode | Status | Date |
|-------------|----------------|-------------|------------------------------|-------------|------|--------|------|
| EA-NADF-WP01-001 | EA-4 — Module Installation | WP-01 Foundation Hardening | Install `mis_builder` 17.0.1.5.0 · `purchase_request` 17.0.2.3.4 · `helpdesk_mgmt` 17.0.1.10.4 · `report_xlsx` 17.0.1.0.2 · `date_range` 17.0.1.2.1 | GRANTED | Pre-Pilot (retrospective) | Executed | 2026-06-25 |
| EA-NADF-WP01-002 | EA-3 — Configuration | WP-01 Foundation Hardening | Set `auth_totp.policy = required` (global 2FA enforcement) | GRANTED | Pre-Pilot (retrospective) | Executed | 2026-06-25 |
| EA-NADF-WP03-001 | EA-1 — Documentation | WP-03 Procurement Core | Create DEC-WP03-001 and DEC-CONTRACT-001 in DECISION_LOG.md · Update IMPLEMENTATION_HISTORY.md · Update CHANGELOG.md | GRANTED | Advisory | Active | 2026-06-25 |
| EA-NADF-WP03-002 | EA-2 — Repository | WP-03 Procurement Core | Branch `feat/wp-03-procurement-core` from `main@e58e15c` · Commit WP-03 deliverables · Raise PR | GRANTED | Advisory | Active | 2026-06-25 |
| EA-NADF-WP03-003 | EA-3 — Configuration | WP-03 Procurement Core | Configure `purchase_request` picking type; map groups to OCA groups; test PR state machine; test Call for Tender flow; test goods receipt; verify mail.thread audit | GRANTED | Advisory | Active | 2026-06-25 |
| EA-NADF-WP03-004 | EA-5 — Database Mutation | WP-03 Procurement Core | Create `x_compliance_status` selection field on `res.partner` via Odoo shell · Tag vendors · Create Call for Tender requisition type record | GRANTED (conditional — backup pre-condition) | Advisory | Active | 2026-06-25 |
| EA-NADF-WP04-001 | EA-1 — Documentation | WP-04 HR Core | Decision log and IMPLEMENTATION_HISTORY.md updates for WP-04 | PENDING — WP-04 definition required | Advisory | Pending Review | 2026-06-25 |
| EA-NADF-WP04-002 | EA-2 — Repository | WP-04 HR Core | Create `feat/wp-04-hr-core` branch · Commit WP-04 deliverables · Raise PR | PENDING — WP-04 definition required | Advisory | Pending Review | 2026-06-25 |
| EA-NADF-WP04-003 | EA-3 — Configuration | WP-04 HR Core | Configure HR departments, job positions, leave types, accrual plans, group assignments, employee records, work schedules | PENDING — WP-04 definition required | Advisory | Pending Review | 2026-06-25 |

> Full G1/G2/G3 review details, conditions, and outcome records are in `EXECUTION_AUTHORITY_REGISTER.md`.
> AOP-013 pilot is in advisory mode — authority decisions are non-binding during WP-03/WP-04 window.
> Binding mode requires separate Sponsor activation decision after pilot exit criteria are met.

---

## Cross-Reference Index

| Decision ID | Decision Log Entry | Work Package Document | Source Documents |
|-------------|-------------------|-----------------------|-----------------|
| DEC-001 | `docs/DECISION_LOG.md#DEC-001` | Legacy MVP | — |
| DEC-002 | `docs/DECISION_LOG.md#DEC-002` | Legacy MVP | — |
| DEC-003 | `docs/DECISION_LOG.md#DEC-003` | Legacy MVP | — |
| DEC-004 | `docs/DECISION_LOG.md#DEC-004` | Legacy MVP | — |
| DEC-005 | `docs/DECISION_LOG.md#DEC-005` | Legacy MVP | — |
| DEC-006 | `docs/DECISION_LOG.md#DEC-006` | Legacy MVP | — |
| DEC-007 | `docs/DECISION_LOG.md#DEC-007` | Legacy MVP | — |
| DEC-008 | `docs/DECISION_LOG.md#DEC-008` | Legacy MVP | — |
| DEC-RECOVERY-001 | `docs/DECISION_LOG.md#DEC-RECOVERY-001` | M-C | `docs/MC_RECOVERY_INTEGRITY.md` |
| DEC-RECOVERY-002 | `docs/DECISION_LOG.md#DEC-RECOVERY-002` | M-C | `docs/MC_RECOVERY_INTEGRITY.md` |
| DEC-PLATFORM-001 | `docs/DECISION_LOG.md#DEC-PLATFORM-001` | M-C | `docs/GOVERNANCE_GATE_REPORT.md` |
| DEC-BACKUP-001 | `docs/DECISION_LOG.md#DEC-BACKUP-001` | M-C | `docs/BACKUP_STRATEGY.md` |
| DEC-PEG6-001 | `docs/DECISION_LOG.md#DEC-PEG6-001` | PEG-6 | `docs/governance/PEG_6_PRODUCT_AUTHORIZATION_PACKAGE.md` |
| DEC-2FA-001 | `docs/DECISION_LOG.md#DEC-2FA-001` | `docs/work_packages/WP_01_FOUNDATION_HARDENING.md` | — |
| DEC-OCA-01 | `docs/DECISION_LOG.md#DEC-OCA-01` | `docs/work_packages/WP_01_FOUNDATION_HARDENING.md` | `EXECUTION_AUTHORITY_REGISTER.md` |
| DEC-OCA-02 | `docs/DECISION_LOG.md#DEC-OCA-02` | `docs/work_packages/WP_01_FOUNDATION_HARDENING.md` | `docs/governance/DEC_OCA_02_GOVERNANCE_REVIEW.md` |
| DEC-OCA-03 | `docs/DECISION_LOG.md#DEC-OCA-03` | `docs/work_packages/WP_01_FOUNDATION_HARDENING.md` | `EXECUTION_AUTHORITY_REGISTER.md` |
| DEC-OCA-04 | `docs/DECISION_LOG.md#DEC-OCA-04` | `docs/work_packages/WP_01_FOUNDATION_HARDENING.md` | `EXECUTION_AUTHORITY_REGISTER.md` |
| DEC-OCA-05 | `docs/DECISION_LOG.md#DEC-OCA-05` | `docs/work_packages/WP_01_FOUNDATION_HARDENING.md` | — |
| DEC-2FA-002 | `docs/DECISION_LOG.md#DEC-2FA-002` | `docs/work_packages/WP_01_FOUNDATION_HARDENING.md` | `EXECUTION_AUTHORITY_REGISTER.md` |
| DEC-WP02-001 | `docs/DECISION_LOG.md#DEC-WP02-001` | WP-02 Finance Core | — |
| DEC-WP02-002 | `docs/DECISION_LOG.md#DEC-WP02-002` | WP-02 Finance Core | — |
| DEC-WP03-001 | `docs/DECISION_LOG.md#DEC-WP03-001` | `docs/work_packages/WP_03_PROCUREMENT_CORE.md` | `EXECUTION_AUTHORITY_REGISTER.md` |
| DEC-CONTRACT-001 | `docs/DECISION_LOG.md#DEC-CONTRACT-001` | `docs/work_packages/WP_03_PROCUREMENT_CORE.md` | — |
| DEC-WP03-002 | `docs/DECISION_LOG.md#DEC-WP03-002` | `docs/work_packages/WP_03_PROCUREMENT_CORE.md` | — |
| DEC-ADM01-001 | `docs/DECISION_LOG.md#DEC-ADM01-001` | `docs/work_packages/WP_ADM_01.md` | — |
| DEC-ADM01-002 | `docs/DECISION_LOG.md#DEC-ADM01-002` | `docs/work_packages/WP_ADM_01.md` | — |
| DEC-ADM01-003 | `docs/DECISION_LOG.md#DEC-ADM01-003` | `docs/work_packages/WP_ADM_01.md` | — |
| DEC-AOP014-001 | `software-factory-governance/DECISION_LOG.md#DEC-017` | N/A — SF Enhancement | `enhancements/AOP-014/07_DEPLOYMENT_RECORD_NADF.md` · `/nadf_erp/.claude/settings.json` |
| DEC-PC01-001 | `docs/DECISION_LOG.md#DEC-PC01-001` | `docs/work_packages/WP_PC_01.md` | — |
| DEC-PC01-002 | `docs/DECISION_LOG.md#DEC-PC01-002` | `docs/work_packages/WP_PC_01.md` | — |

---

## Register Maintenance Log

| Date | Updated By | Version | Change Description | Trigger |
|------|-----------|---------|-------------------|---------|
| 2026-06-26 | A1 Master Orchestrator | 1.0 | Initial creation — backward-populated from all NADF decisions as at 2026-06-26. 25 decisions across 7 departments. 3 open escalations. 8 deferred items. 9 AOP-013 authority entries. | AOP-015 Software Factory Governance Standard deployment |
| 2026-06-26 | A1 Master Orchestrator | 1.1 | WP-ADM-01 exit gate: Administration section populated — DEC-ADM01-001/002/003 added. Total 28 decisions. Executive Summary updated. | WP-ADM-01 Administration Core — CONDITIONAL PASS |
| 2026-06-26 | A1 Master Orchestrator | 1.2 | AOP-015 receipt review: DEC-AOP014-001 (trust profile NADF deployment) added to ICT section. Total 29 decisions. Cross-reference index updated. | AOP-015 delivery acknowledgement — post-deployment GAR gap identified and closed |
| 2026-06-26 | A1 Master Orchestrator | 1.3 | WP-PC-01 exit gate: Project Coordination section populated — DEC-PC01-001/002 added. Total 31 decisions. Executive Summary updated (Active 28, Deferred 2). | WP-PC-01 Project Coordination — CONDITIONAL PASS |

---

*Governance Approval Register — NADF ERP Programme*
*Document ID: GAR-NADF-001 · Version 1.3*
*Maintained by A1 Master Orchestrator — POD-NADF*
*Software Factory Governance Standard AOP-015 — Mandatory Artifact*
*Authority: `software-factory-governance/templates/GOVERNANCE_APPROVAL_REGISTER_TEMPLATE.md`*
