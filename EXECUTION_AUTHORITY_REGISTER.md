# Execution Authority Register — NADF Project Pod

---

**Document:** EAR-NADF-LIVE-001
**Project:** NADF ERP MVP
**Version:** 1.0
**Date Initialised:** 2026-06-25
**Pilot Mode:** Advisory (WP-03 and WP-04 window)
**Maintained by:** A1-NADF Master Orchestrator
**Status:** Active — AOP-013 Advisory Pilot

---

## 1. Purpose

This is the live Execution Authority Register for the NADF project pod. It records all authority grants, denials, and revocations under the AOP-013 Execution Authority Framework. During the advisory pilot (WP-03/WP-04 window), all decisions carry Mode: Advisory and are non-binding. D2 continues under v1.0 Human Sponsor approval flow.

This register is append-only. Records are never deleted. Status transitions are logged with date and reason.

---

## 2. Register Format

```
Authority ID         : EA-{PROJECT}-WP{XX}-{NNN}
Authority Class      : EA-{N} — {Class Name}
Project              : {PROJECT}
Work Package         : WP-{XX} — {WP Name}
Requested By         : D2
Request Date         : ISO date
Authorized Actions   :
  - {action}
G1 Review            : {APPROVED | DENIED | CONDITIONAL | N/A} — {date} — {brief rationale}
G2 Review            : {APPROVED | DENIED | CONDITIONAL | N/A} — {date} — {brief rationale}
G3 Review            : {APPROVED | DENIED | CONDITIONAL | N/A} — {date} — {brief rationale}
A1 Decision          : {EXECUTION AUTHORITY GRANTED | DENIED | REVOKED}
A1 Decision Date     : ISO date
A1 Rationale         : {rationale}
Validity Scope       : WP-{XX} only
Conditions           : {any conditions, or NONE}
Mode                 : Pre-Pilot | Advisory | Binding
Status               : {Active | Executed | Revoked | Expired | Denied | Pending Review}
Execution Date       : ISO date (when executed) or —
Outcome              : {result description} or —
```

**Mode field values:**
- `Pre-Pilot` — retrospective entry for v1.0 operations before the advisory pilot window
- `Advisory` — entry during WP-03/WP-04 pilot window; decision is non-binding; D2 proceeds under v1.0 Human Sponsor approval
- `Binding` — entry after Sponsor activates binding mode; decision gates D2 execution

---

## 3. Authority Register

---

### Entry 001 — Pre-Pilot: WP-01 Module Installation

```
Authority ID         : EA-NADF-WP01-001
Authority Class      : EA-4 — Module Installation Authority
Project              : NADF
Work Package         : WP-01 — Foundation Hardening
Requested By         : D2
Request Date         : 2026-06-25 (retrospective)
Authorized Actions   :
  - Install mis_builder 17.0.1.5.0
  - Install purchase_request 17.0.2.3.4
  - Install helpdesk_mgmt 17.0.1.10.4
  - Install report_xlsx 17.0.1.0.2 (dependency)
  - Install date_range 17.0.1.2.1 (dependency)
G1 Review            : APPROVED — 2026-06-25 — All OCA modules approved; deps verified; no conflicts
G2 Review            : APPROVED — 2026-06-25 — Traceable to WP-01 AC-WP01-01/02; MODULE_REGISTRY updated
G3 Review            : APPROVED — 2026-06-25 — No new external integrations; rollback confirmed
A1 Decision          : EXECUTION AUTHORITY GRANTED
A1 Decision Date     : 2026-06-25
A1 Rationale         : Retrospective grant; all reviews approved; actual execution confirmed successful under v1.0
Validity Scope       : WP-01 only
Conditions           : NONE
Mode                 : Pre-Pilot
Status               : Executed
Execution Date       : 2026-06-25
Outcome              : mis_builder, purchase_request, helpdesk_mgmt + deps installed; registry exit 0; AC-WP01-06 PASS
```

---

### Entry 002 — Pre-Pilot: WP-01 2FA Configuration

```
Authority ID         : EA-NADF-WP01-002
Authority Class      : EA-3 — Configuration Authority
Project              : NADF
Work Package         : WP-01 — Foundation Hardening
Requested By         : D2
Request Date         : 2026-06-25 (retrospective)
Authorized Actions   :
  - Set auth_totp.policy = required (global 2FA enforcement)
G1 Review            : APPROVED — 2026-06-25 — Consistent with platform profile; no arch side effects
G2 Review            : APPROVED — 2026-06-25 — Traceable to WP-01 security AC; documented in IMPLEMENTATION_HISTORY
G3 Review            : APPROVED — 2026-06-25 — Strengthens security posture; reversible via ir.config_parameter
A1 Decision          : EXECUTION AUTHORITY GRANTED
A1 Decision Date     : 2026-06-25
A1 Rationale         : Retrospective grant; security configuration; execution confirmed; DEC-2FA-002 logged
Validity Scope       : WP-01 only
Conditions           : NONE
Mode                 : Pre-Pilot
Status               : Executed
Execution Date       : 2026-06-25
Outcome              : TOTP 2FA enabled globally; DEC-2FA-002 logged; AC passed
```

---

### Entry 003 — WP-03 Documentation Authority

```
Authority ID         : EA-NADF-WP03-001
Authority Class      : EA-1 — Documentation Authority
Project              : NADF
Work Package         : WP-03 — Procurement Core
Requested By         : D2
Request Date         : 2026-06-25
Authorized Actions   :
  - Create DEC-WP03-001 in docs/DECISION_LOG.md (vendor compliance mechanism decision)
  - Create DEC-CONTRACT-001 in docs/DECISION_LOG.md (OCA contract vs nadf_legal_contract evaluation)
  - Update IMPLEMENTATION_HISTORY.md with WP-03 delivery record
  - Update CHANGELOG.md with WP-03 changelog entry
  - Document WP03-07 BLOCKED status in IMPLEMENTATION_HISTORY.md
G1 Review            : APPROVED — 2026-06-25 — Documentation artifacts are low-risk; WP-03 deliverables
                       D-WP03-02 and D-WP03-07 require these entries; architecturally sound
G2 Review            : APPROVED — 2026-06-25 (optional) — DEC-WP03-001 and DEC-CONTRACT-001 are mandatory
                       WP-03 deliverables; documentation plan traceable to acceptance criteria
G3 Review            : N/A — optional for EA-1
A1 Decision          : EXECUTION AUTHORITY GRANTED
A1 Decision Date     : 2026-06-25
A1 Rationale         : EA-1 auto-grant after G1 approval; low-risk documentation; all actions are
                       mandatory WP-03 deliverables; no escalation trigger
Validity Scope       : WP-03 only
Conditions           : NONE
Mode                 : Advisory
Status               : Active
Execution Date       : —
Outcome              : —
```

---

### Entry 004 — WP-03 Repository Authority

```
Authority ID         : EA-NADF-WP03-002
Authority Class      : EA-2 — Repository Authority
Project              : NADF
Work Package         : WP-03 — Procurement Core
Requested By         : D2
Request Date         : 2026-06-25
Authorized Actions   :
  - Branch feat/wp-03-procurement-core from main@e58e15c (already created per Go/No-Go 2026-06-25)
  - Commit WP-03 deliverables to feat/wp-03-procurement-core
  - Raise PR: feat/wp-03-procurement-core → main using PR template
G1 Review            : APPROVED — 2026-06-25 — Branch already created from protected main@e58e15c
                       per Go/No-Go PASS; naming convention correct (feat/wp-XX-name); architecturally sound
G2 Review            : APPROVED — 2026-06-25 — PR will use NADF PR template; commits will follow
                       conventional commits format; documentation completeness gate at PR review
G3 Review            : N/A — optional for EA-2
A1 Decision          : EXECUTION AUTHORITY GRANTED
A1 Decision Date     : 2026-06-25
A1 Rationale         : EA-2 auto-grant after G1+G2 approval; branch already created correctly; no
                       escalation trigger; no production impact
Validity Scope       : WP-03 only
Conditions           : NONE
Mode                 : Advisory
Status               : Active
Execution Date       : —
Outcome              : —
```

---

### Entry 005 — WP-03 Configuration Authority

```
Authority ID         : EA-NADF-WP03-003
Authority Class      : EA-3 — Configuration Authority
Project              : NADF
Work Package         : WP-03 — Procurement Core
Requested By         : D2
Request Date         : 2026-06-25
Authorized Actions   :
  - Configure purchase_request: set default picking_type_id to "Receipts" (NADF Main Warehouse)
  - Configure Procurement Officer group as approver for purchase_request approval step
  - Test purchase_request state machine: draft → to_approve → approved → in_progress → done
  - Verify Call for Tender requisition type approval workflow (requisition → RFQ → award → PO)
  - Test goods receipt flow: test PO → confirm → validate receipt in NADF Main Warehouse
  - Verify mail.thread audit trail on purchase.request and purchase.order after state transitions
G1 Review            : APPROVED — 2026-06-25 — CE-native module configuration; no new modules
                       required; picking_type assignment to NADF Main Warehouse is correct
                       platform approach; approval group assignment is standard CE pattern;
                       no architectural concerns; consistent with WP-03 Go/No-Go G1 verdict
G2 Review            : APPROVED — 2026-06-25 — All 6 configuration actions traceable to
                       AC-WP03-02, AC-WP03-03, AC-WP03-04, AC-WP03-05, AC-WP03-06;
                       documentation requirements defined in WP-03 deliverable set
G3 Review            : APPROVED — 2026-06-25 — 4 Procurement user groups confirmed existing
                       from WP-01 (Requisitioner, Officer, Manager, Finance Approver);
                       no new privilege grants; configuration reversible via Odoo Settings;
                       ₦500K PO approval threshold write-protected until B-03 client confirmation
                       per WP-03 R-WP03-03; no security risk in scope
A1 Decision          : EXECUTION AUTHORITY GRANTED
A1 Decision Date     : 2026-06-25
A1 Rationale         : EA-3 explicit grant; all three required reviews approved; configuration
                       scope is CE-native; consistent with Go/No-Go verdicts; ₦500K threshold
                       write-protection acknowledged; no escalation trigger
Validity Scope       : WP-03 only
Conditions           : NONE
Mode                 : Advisory
Status               : Active
Execution Date       : —
Outcome              : —
```

---

### Entry 006 — WP-03 Database Mutation Authority

```
Authority ID         : EA-NADF-WP03-004
Authority Class      : EA-5 — Database Mutation Authority
Project              : NADF
Work Package         : WP-03 — Procurement Core
Requested By         : D2
Request Date         : 2026-06-25
Authorized Actions   :
  - Create x_compliance_status selection field on res.partner via Odoo shell
    (ir.model.fields create; values: compliant / non_compliant / pending)
  - Tag minimum 2 existing vendors (supplier_rank > 0) with x_compliance_status = 'compliant'
  - Create purchase.requisition.type record: 'Call for Tender'
    (exclusive=True, quantity_copy='copy') via Odoo shell
G1 Review            : APPROVED — 2026-06-25 — x_compliance_status via ir.model.fields shell
                       command is Phase 1 acceptable approach (confirmed in G1 Go/No-Go verdict §8);
                       requisition type record creation is a standard Odoo data operation; both
                       mutations are low-complexity shell writes with clear rollback paths;
                       R-WP03-01 (shell field not version-controlled) acknowledged — creation
                       command must be documented in IMPLEMENTATION_HISTORY.md
G2 Review            : APPROVED — 2026-06-25 — Actions traceable to D-WP03-01 (compliance field),
                       D-WP03-02 (DEC-WP03-001), D-WP03-05 (Call for Tender requisition type);
                       R-WP03-01 mitigation documented (creation command in IMPLEMENTATION_HISTORY);
                       documentation requirements complete
G3 Review            : CONDITIONAL — 2026-06-25 — Pre-work backup is mandatory before first
                       mutating shell command. Latest backup (nadf_20260624_160329) predates WP-01
                       execution and does not reflect current DB state. A fresh backup must be
                       created and confirmed before WP03-01 shell command runs. Condition: D2
                       executes scripts/backup_nadf.sh and confirms new backup file exists before
                       executing any shell write command. This condition is consistent with the
                       WP-03 Go/No-Go requirement (Pre-work backup — plan confirmed ⚠️ in §3).
                       Once condition is met, G3 approves without further review.
A1 Decision          : EXECUTION AUTHORITY GRANTED
A1 Decision Date     : 2026-06-25
A1 Rationale         : EA-5 explicit grant; G1+G2 approved; G3 conditional with backup requirement.
                       Condition is well-scoped, pre-acknowledged in WP-03 Go/No-Go §3, and
                       resolvable by D2 before first shell command. Granting with condition recorded.
                       Advisory mode: D2 proceeds under v1.0 Human Sponsor approval; advisory grant
                       accuracy assessed after WP-03 execution.
Validity Scope       : WP-03 only
Conditions           : G3-WP03-CON-001 — D2 must take and confirm new backup via
                       scripts/backup_nadf.sh before executing WP03-01 shell command.
                       Condition acknowledged in WP-03 Go/No-Go §3 pre-work backup requirement.
Reclassified         : No — EA-5 confirmed by G1 for both shell mutations
Mode                 : Advisory
Status               : Active
Execution Date       : —
Outcome              : —
```

---

## 4. WP-04 Prospective Entries (Pending Work Package Definition)

---

### Entry 007 — WP-04 Documentation Authority (Prospective)

```
Authority ID         : EA-NADF-WP04-001
Authority Class      : EA-1 — Documentation Authority
Project              : NADF
Work Package         : WP-04 — HR Core
Requested By         : D2
Request Date         : 2026-06-25 (prospective — WP-04 definition pending)
Authorized Actions   :
  - Decision log entries for WP-04 architectural decisions (TBC from WP-04 definition)
  - IMPLEMENTATION_HISTORY.md update with WP-04 delivery record
  - CHANGELOG.md WP-04 entry
G1 Review            : PENDING — awaiting WP-04 work package definition
G2 Review            : PENDING
G3 Review            : N/A (optional for EA-1)
A1 Decision          : PENDING
A1 Decision Date     : —
A1 Rationale         : —
Validity Scope       : WP-04 only
Conditions           : —
Mode                 : Advisory
Status               : Pending Review
Execution Date       : —
Outcome              : —
```

---

### Entry 008 — WP-04 Repository Authority (Prospective)

```
Authority ID         : EA-NADF-WP04-002
Authority Class      : EA-2 — Repository Authority
Project              : NADF
Work Package         : WP-04 — HR Core
Requested By         : D2
Request Date         : 2026-06-25 (prospective)
Authorized Actions   :
  - Create feat/wp-04-hr-core branch from main (post WP-03 merge)
  - Commit WP-04 deliverables
  - Raise PR: feat/wp-04-hr-core → main
G1 Review            : PENDING — awaiting WP-04 work package definition
G2 Review            : PENDING
G3 Review            : N/A (optional for EA-2)
A1 Decision          : PENDING
A1 Decision Date     : —
A1 Rationale         : —
Validity Scope       : WP-04 only
Conditions           : —
Mode                 : Advisory
Status               : Pending Review
Execution Date       : —
Outcome              : —
```

---

### Entry 009 — WP-04 Configuration Authority (Prospective)

```
Authority ID         : EA-NADF-WP04-003
Authority Class      : EA-3 — Configuration Authority
Project              : NADF
Work Package         : WP-04 — HR Core
Requested By         : D2
Request Date         : 2026-06-25 (prospective)
Authorized Actions   :
  - Configure HR departments: Finance, Procurement, HR, Administration, IT, Project Coordination
  - Configure job positions and org chart structure for 25 active employees
  - Configure hr_holidays leave types: Annual Leave, Sick Leave, Public Holiday,
    Maternity Leave, Paternity Leave (NADF-standard set per Transfer Package CA-03)
  - Configure leave accrual plans per employee tier
  - Configure HR security group assignments: HR Officer, HR Manager, HR User
  - Validate employee records: department assignments, job positions, work email addresses
  - Configure work schedules and time off approval workflows
G1 Review            : PENDING — awaiting WP-04 work package definition and G1 review
G2 Review            : PENDING
G3 Review            : PENDING
A1 Decision          : PENDING
A1 Decision Date     : —
A1 Rationale         : —
Validity Scope       : WP-04 only
Conditions           : —
Mode                 : Advisory
Status               : Pending Review
Execution Date       : —
Outcome              : —
```

---

## 5. Denied Authorities

No denied authorities.

---

## 6. Revoked Authorities

No revoked authorities.

---

## 7. Register Statistics

| Metric | Value |
|--------|-------|
| Total grants issued (active) | 4 (EA-NADF-WP03-001 through 004, all Advisory) |
| Pre-Pilot grants (executed) | 2 (EA-NADF-WP01-001 and 002) |
| WP-03 Advisory grants | 4 |
| WP-04 Advisory (pending review) | 3 |
| Denied | 0 |
| Revoked | 0 |
| Conditional grants | 1 (EA-NADF-WP03-004 — backup condition) |

---

## 8. Template for New Entries

```
Authority ID         : EA-{PROJECT}-WP{XX}-{NNN}
Authority Class      : EA-{N} — {Class Name}
Project              : {PROJECT}
Work Package         : WP-{XX} — {WP Name}
Requested By         : D2
Request Date         : YYYY-MM-DD
Authorized Actions   :
  - {action 1}
  - {action 2}
G1 Review            : PENDING
G2 Review            : PENDING
G3 Review            : PENDING
A1 Decision          : PENDING
A1 Decision Date     : —
A1 Rationale         : —
Validity Scope       : WP-{XX} only
Conditions           : —
Mode                 : Advisory
Status               : Pending Review
Execution Date       : —
Outcome              : —
```

---

*Execution Authority Register — NADF Project Pod (Live)*
*Maintained by A1-NADF Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
