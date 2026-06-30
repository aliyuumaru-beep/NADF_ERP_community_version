# Authority Decision Log — NADF Project Pod

---

**Document:** ADL-NADF-001
**Project:** NADF ERP MVP
**Version:** 1.0
**Date Initialised:** 2026-06-25
**Maintained by:** A1-NADF Master Orchestrator
**Status:** Active — AOP-013 Advisory Pilot

---

## Purpose

This log records every authority decision event for the NADF project pod in chronological order. It is append-only. Entries are never deleted or modified. Each entry is timestamped and tagged by event type.

Event types: `ACTIVATION` | `GRANT` | `DENY` | `REVOKE` | `ACKNOWLEDGEMENT` | `ESCALATION` | `CLOSURE` | `ROLLBACK`

---

## Entry 001 — Pilot Activation

```
Entry Number  : 001
Date          : 2026-06-25
Event Type    : ACTIVATION
Authority     : A1-NADF Master Orchestrator
Sponsor Ref   : AOP-013-SD-001 (ADOPT WITH CONDITIONS)

Event         : AOP-013 PILOT ACTIVATED — NADF Pod

Mode          : Advisory
Pilot Window  : WP-03 and WP-04
Phase B Status: CONDITIONAL PASS — G3-CON-001 and G3-CON-002 resolved (see Entry 002)

Detail        : The AOP-013 Execution Authority Framework enters advisory pilot on the
                NADF project pod. All authority decisions issued during WP-03 and WP-04
                are advisory and non-binding. D2 continues under v1.0 Human Sponsor
                approval flow. Advisory decisions are logged here and in the Execution
                Authority Register for validation against execution outcomes.

                Pilot activates subject to G3 confirmation of remediation closure.
                See Phase B Remediation Report for full condition resolution record.

Human Sponsor : Informed — no action required
```

---

## Entry 002 — Protocol Acknowledgement

```
Entry Number  : 002
Date          : 2026-06-25
Event Type    : ACKNOWLEDGEMENT
Authority     : A1-NADF Master Orchestrator
Resolves      : G3-CON-002 (Phase B Governance Review — blocking condition)
               Also addresses: VC-3 advisory mode gap (G2-OBS-003)
               Also addresses: G3-OBS-003 (misclassification tagging)

Event         : A1 PROTOCOL ACKNOWLEDGEMENT — ADVISORY PILOT OPERATING STANDARDS

A1 formally acknowledges the following operating standards for all advisory
authority decisions issued during the WP-03 and WP-04 pilot window.

---

1. APPROVED GRANT FORMAT

All EXECUTION AUTHORITY GRANTED decisions must use this exact format
(source: AOP-013 document 04_AGENT_OS_V2_DESIGN.md Section 4):

  EXECUTION AUTHORITY GRANTED

  Authority ID:        EA-{PROJECT}-WP{XX}-{NNN}
  Authority Class:     EA-{N}
  Project:             {PROJECT}
  Work Package:        WP-{XX}
  Authorized Actions:
    - {action 1}
    - {action 2}
  Approvals:
    G1: Approved — {brief rationale}
    G2: Approved — {brief rationale}
    G3: Approved — {brief rationale}
  Validity:            WP-{XX} only
  Issued:              {ISO date}
  Mode:                Advisory
  Status:              Active

  Advisory Note: This decision is non-binding during the AOP-013 pilot.
  D2 proceeds under v1.0 Human Sponsor approval. This grant is logged
  for accuracy validation against execution outcomes.

---

2. APPROVED DENY FORMAT

All EXECUTION AUTHORITY DENIED decisions must use this exact format
(source: AOP-013 document 04_AGENT_OS_V2_DESIGN.md Section 4):

  EXECUTION AUTHORITY DENIED

  Authority Request:   {description}
  Authority Class:     EA-{N}
  Blocking Review:     G{N} — {reviewer name}
  Reason:              {reason for denial}
  Resolution Required: {what must change before re-submission}
  Mode:                Advisory
  Status:              Denied

  Advisory Note: This decision is non-binding during the AOP-013 pilot.
  D2 proceeds under v1.0 Human Sponsor approval. The denial rationale
  is logged for accuracy validation.

---

3. APPROVED REVOKE FORMAT

All EXECUTION AUTHORITY REVOKED decisions must use this exact format
(source: AOP-013 document 04_AGENT_OS_V2_DESIGN.md Section 4):

  EXECUTION AUTHORITY REVOKED

  Authority ID:        EA-{PROJECT}-WP{XX}-{NNN}
  Revocation Reason:   {reason}
  Effective:           {ISO date}
  Mode:                Advisory
  Impact:              All active advisory execution tracking under this ID halted.
  Status:              Revoked

---

4. GOVERNANCE REVIEW CHECKLISTS

All advisory authority reviews by G1, G2, G3 must use the checklists
defined in AOP-013 document 04_AGENT_OS_V2_DESIGN.md Section 6:

  G1 Architecture Review Checklist (6 items):
    □ Confirm architectural classification of the requested actions
    □ Confirm appropriate EA class is assigned
    □ Identify any architectural preconditions not met
    □ Identify any architectural constraints on execution
    □ Confirm no architectural decision is bypassed
    □ Decision: APPROVED | DENIED | CONDITIONAL (with conditions)

  G2 Quality Review Checklist (5 items):
    □ Confirm authorized actions are traceable to acceptance criteria in the WP
    □ Confirm documentation is complete before execution is authorized
    □ Confirm acceptance criteria are sufficient and testable
    □ Confirm no documentation is deferred that should precede execution
    □ Decision: APPROVED | DENIED | CONDITIONAL

  G3 Security & Change Review Checklist (5 items):
    □ Assess security impact of authorized actions
    □ Confirm change impact is within acceptable scope
    □ Confirm rollback plan exists for the authorized actions
    □ Confirm recovery readiness is adequate
    □ Assess risk exposure; confirm within tolerance
    □ Decision: APPROVED | DENIED | CONDITIONAL

Reviews must be complete. No checklist items may be skipped or marked
not applicable without documented rationale.

---

5. CLASSIFICATION DISCIPLINE

All authority requests must be classified using the five classification
rules in AOP-013 document 05_AUTHORITY_CLASSIFICATION_STANDARD.md:

  Rule 1: Use the highest applicable class (round up)
  Rule 2: Classify by the riskiest action in the request
  Rule 3: Do not split risk across requests
  Rule 4: EA-6 is non-negotiable — production is always EA-6
  Rule 5: Uncertainty escalates — submit at the higher class

If G1 corrects the submitted classification during review, the register
entry is flagged with:

  Reclassified     : Yes — submitted as EA-{N}, confirmed as EA-{M}

The original submitted class is preserved alongside the confirmed class.
This prevents corrected entries from being read as authoritative correct
precedents in future calibration exercises (G3-OBS-003 resolution).

---

6. ADVISORY MODE OPERATION

During the WP-03 and WP-04 pilot window, all authority decisions carry
Mode: Advisory. The following rules apply:

  a. A1 issues advisory decisions following the formats above.
  b. D2 does NOT wait for advisory decisions before executing.
  c. D2 does NOT reference advisory authority IDs as execution gates.
  d. D2 proceeds under v1.0 Human Sponsor approval flow.
  e. After execution, A1 records the outcome against the advisory decision.
  f. Accuracy is assessed retrospectively at each WP closure.

VC-3 ADVISORY MODE HANDLING (G2-OBS-003 resolution):

  Validation criterion VC-3 (D2 Executes Under Authority, requiring D2 to
  reference authority IDs in execution records) cannot be satisfied in advisory
  mode by design. This is expected and correct behaviour for the pilot phase.

  During the pilot, M-06 (Advisory Decision Accuracy Rate) in the Success
  Metrics Dashboard is the operative proxy for VC-3. M-06 measures whether
  advisory GRANT decisions retrospectively align with successful execution
  outcomes.

  Full VC-3 compliance — D2 referencing authority IDs as execution gates —
  is deferred to binding mode activation, which requires a separate Sponsor
  decision after pilot GRADUATE outcome.

  A Pilot Validation Report reviewer must not score VC-3 as FAIL based solely
  on D2's absence of authority ID references during the advisory pilot.

---

A1 acknowledges that deviation from any of the above standards during the
advisory pilot is a governance breach reportable to the Human Sponsor and
may trigger Rollback Trigger T-01 (Critical Governance Violation).
```

---

## Entry 003 — G3 Remediation Verification

```
Entry Number  : 003
Date          : 2026-06-25
Event Type    : ACKNOWLEDGEMENT
Authority     : G3 Security & Change Governance
Decision File : enhancements/AOP-013/phase-b/G3_VERIFICATION_DECISION.md

Event         : G3 REMEDIATION VERIFICATION — CONFIRMED

G3-CON-001    : CONFIRMED — 7/7 checklist items PASS
               Mode field present in Section 2, all entries (001/002 Pre-Pilot,
               003 Advisory), and Section 8 template. Value definitions clear.
               Document 07 incremented to v1.1.

G3-CON-002    : CONFIRMED — 8/8 checklist items PASS
               AUTHORITY_DECISION_LOG.md Entry 002 contains all six required
               sections: GRANT/DENY/REVOKE formats, governance review checklists,
               classification discipline (incl. Reclassified flag), and advisory
               mode operating rules including VC-3 handling.

Observation   : OBS-G3-VER-001 (non-blocking) — G3 checklist in Entry 002
               Section 4 is labelled "(5 items)" but contains 6 bullet points.
               Content is correct. Correct at next routine document revision.

Phase B Status: COMPLETE PASS — all blocking conditions resolved
Pilot Gate    : CLEARED — pending Sponsor activation instruction
```

---

## Entry 004 — Phase C Pilot Activation by Sponsor

```
Entry Number  : 004
Date          : 2026-06-25
Event Type    : ACTIVATION
Authority     : Human Sponsor (Pilot Activation Instruction)
Sponsor Ref   : Phase C Activation Instruction (post Phase B COMPLETE PASS)

Event         : PHASE C — NADF PILOT ACTIVATED BY SPONSOR

Decision      : Phase B is accepted. Activate Phase C — NADF Pilot.

Operating Mode: Advisory. Not Binding.

Sponsor Instructions (verbatim):
  1. Deploy EXECUTION_AUTHORITY_REGISTER.md to NADF.
  2. Begin issuing advisory authority decisions.
  3. Apply authority classification to: WP-03 retrospective review,
     WP-04 HR Core, Subsequent NADF work packages.
  4. Record GRANTED/DENIED/REVOKED decisions using approved formats.
  5. Collect all metrics defined in the Success Metrics Dashboard.
  6. Follow Rollback Procedure if any trigger condition occurs.
  7. Produce periodic pilot status reports.

Constraint    : NADF delivery remains governed under Agent OS v1.
                AOP-013 operates in observation and measurement mode only.
                No binding authority decisions are permitted during the pilot.

A1 Action     : EXECUTION_AUTHORITY_REGISTER.md deployed to /nadf_erp root.
                WP-03 retrospective advisory authority decisions to be issued
                in Entries 005–008 below.
```

---

## Entry 005 — Advisory GRANT: EA-NADF-WP03-001 (EA-1 Documentation)

```
Entry Number  : 005
Date          : 2026-06-25
Event Type    : GRANT
Authority     : A1-NADF Master Orchestrator
Register Ref  : EA-NADF-WP03-001 (EXECUTION_AUTHORITY_REGISTER.md Entry 003)

  EXECUTION AUTHORITY GRANTED

  Authority ID:        EA-NADF-WP03-001
  Authority Class:     EA-1 — Documentation Authority
  Project:             NADF
  Work Package:        WP-03 — Procurement Core
  Authorized Actions:
    - Create DEC-WP03-001 in docs/DECISION_LOG.md (vendor compliance mechanism)
    - Create DEC-CONTRACT-001 in docs/DECISION_LOG.md (OCA contract evaluation)
    - Update IMPLEMENTATION_HISTORY.md with WP-03 delivery record
    - Update CHANGELOG.md with WP-03 changelog entry
    - Document WP03-07 BLOCKED status in IMPLEMENTATION_HISTORY.md
  Approvals:
    G1: Approved — documentation artifacts are low-risk; traceable to D-WP03-02,
        D-WP03-07; no architectural concerns
    G2: Approved (optional) — DEC-WP03-001 and DEC-CONTRACT-001 are mandatory
        WP-03 deliverables; documentation plan complete
    G3: N/A — optional for EA-1
  Validity:            WP-03 only
  Issued:              2026-06-25
  Mode:                Advisory
  Status:              Active

  Advisory Note: This decision is non-binding during the AOP-013 pilot.
  D2 proceeds under v1.0 Human Sponsor approval. This grant is logged
  for accuracy validation against execution outcomes.
```

---

## Entry 006 — Advisory GRANT: EA-NADF-WP03-002 (EA-2 Repository)

```
Entry Number  : 006
Date          : 2026-06-25
Event Type    : GRANT
Authority     : A1-NADF Master Orchestrator
Register Ref  : EA-NADF-WP03-002 (EXECUTION_AUTHORITY_REGISTER.md Entry 004)

  EXECUTION AUTHORITY GRANTED

  Authority ID:        EA-NADF-WP03-002
  Authority Class:     EA-2 — Repository Authority
  Project:             NADF
  Work Package:        WP-03 — Procurement Core
  Authorized Actions:
    - Branch feat/wp-03-procurement-core from main@e58e15c
      (already created per Go/No-Go PASS 2026-06-25)
    - Commit WP-03 deliverables to feat/wp-03-procurement-core
    - Raise PR: feat/wp-03-procurement-core → main using NADF PR template
  Approvals:
    G1: Approved — branch already created from protected main@e58e15c per
        Go/No-Go PASS; naming convention correct (feat/wp-XX-name)
    G2: Approved — PR will use NADF PR template; commits will follow
        conventional commits format; documentation completeness gate at PR review
    G3: N/A — optional for EA-2
  Validity:            WP-03 only
  Issued:              2026-06-25
  Mode:                Advisory
  Status:              Active

  Advisory Note: This decision is non-binding during the AOP-013 pilot.
  D2 proceeds under v1.0 Human Sponsor approval. This grant is logged
  for accuracy validation against execution outcomes.
```

---

## Entry 007 — Advisory GRANT: EA-NADF-WP03-003 (EA-3 Configuration)

```
Entry Number  : 007
Date          : 2026-06-25
Event Type    : GRANT
Authority     : A1-NADF Master Orchestrator
Register Ref  : EA-NADF-WP03-003 (EXECUTION_AUTHORITY_REGISTER.md Entry 005)

  EXECUTION AUTHORITY GRANTED

  Authority ID:        EA-NADF-WP03-003
  Authority Class:     EA-3 — Configuration Authority
  Project:             NADF
  Work Package:        WP-03 — Procurement Core
  Authorized Actions:
    - Configure purchase_request: set default picking_type_id to "Receipts"
      (NADF Main Warehouse)
    - Configure Procurement Officer group as approver for purchase_request
    - Test purchase_request state machine: draft → to_approve → approved →
      in_progress → done
    - Verify Call for Tender requisition type approval workflow
      (requisition → RFQ → award → PO)
    - Test goods receipt flow: test PO → confirm → validate receipt in
      NADF Main Warehouse
    - Verify mail.thread audit trail on purchase.request and purchase.order
      after state transitions
  Approvals:
    G1: Approved — CE-native module configuration; no new modules; picking_type
        assignment is correct platform approach; no architectural concerns;
        consistent with WP-03 Go/No-Go G1 verdict
    G2: Approved — all configuration actions traceable to AC-WP03-02/03/04/05/06;
        documentation requirements defined in WP-03 deliverable set
    G3: Approved — 4 Procurement user groups confirmed existing from WP-01;
        no new privilege grants; ₦500K PO threshold write-protected until B-03
        client confirmation per R-WP03-03; configuration reversible via Odoo
        Settings; no security risk in scope
  Validity:            WP-03 only
  Issued:              2026-06-25
  Mode:                Advisory
  Status:              Active

  Advisory Note: This decision is non-binding during the AOP-013 pilot.
  D2 proceeds under v1.0 Human Sponsor approval. This grant is logged
  for accuracy validation against execution outcomes.
```

---

## Entry 008 — Advisory GRANT (Conditional): EA-NADF-WP03-004 (EA-5 DB Mutation)

```
Entry Number  : 008
Date          : 2026-06-25
Event Type    : GRANT
Authority     : A1-NADF Master Orchestrator
Register Ref  : EA-NADF-WP03-004 (EXECUTION_AUTHORITY_REGISTER.md Entry 006)

  EXECUTION AUTHORITY GRANTED

  Authority ID:        EA-NADF-WP03-004
  Authority Class:     EA-5 — Database Mutation Authority
  Project:             NADF
  Work Package:        WP-03 — Procurement Core
  Authorized Actions:
    - Create x_compliance_status selection field on res.partner via Odoo shell
      (ir.model.fields create; values: compliant / non_compliant / pending)
    - Tag minimum 2 existing vendors (supplier_rank > 0) with
      x_compliance_status = 'compliant'
    - Create purchase.requisition.type record: 'Call for Tender'
      (exclusive=True, quantity_copy='copy') via Odoo shell
  Approvals:
    G1: Approved — x_compliance_status via ir.model.fields shell command is
        Phase 1 acceptable approach (confirmed in G1 Go/No-Go verdict §8);
        requisition type record creation is a standard data operation;
        R-WP03-01 acknowledged (creation command to be documented in
        IMPLEMENTATION_HISTORY.md)
    G2: Approved — traceable to D-WP03-01 (compliance field), D-WP03-02
        (DEC-WP03-001), D-WP03-05 (Call for Tender); R-WP03-01 mitigation
        documented (creation command in IMPLEMENTATION_HISTORY)
    G3: CONDITIONAL — G3-WP03-CON-001: D2 must execute scripts/backup_nadf.sh
        and confirm new backup file exists before executing any shell write
        command. Latest backup (nadf_20260624_160329) predates WP-01 execution.
        New backup required. Condition is pre-acknowledged in WP-03 Go/No-Go §3.
  Validity:            WP-03 only
  Conditions:          G3-WP03-CON-001 — new backup before first shell mutation.
                       Once backup confirmed, G3 condition is satisfied; no
                       further G3 review required.
  Issued:              2026-06-25
  Mode:                Advisory
  Status:              Active

  Advisory Note: This decision is non-binding during the AOP-013 pilot.
  D2 proceeds under v1.0 Human Sponsor approval. Conditional grant — D2 must
  take new backup before executing shell mutations. Grant accuracy assessed
  after WP-03 execution against actual outcome.
```

---

## Entry 009 — WP-04 Prospective Entries Logged (Pending Review)

```
Entry Number  : 009
Date          : 2026-06-25
Event Type    : ACKNOWLEDGEMENT
Authority     : A1-NADF Master Orchestrator

Event         : WP-04 PROSPECTIVE AUTHORITY ENTRIES STAGED IN REGISTER

Per Sponsor Phase C instruction: "Apply authority classification to WP-04 HR Core."

WP-04 work package definition does not yet exist in docs/work_packages/.
Three prospective entries have been staged in EXECUTION_AUTHORITY_REGISTER.md
(Entries 007–009 in the register) covering expected HR Core scope:

  EA-NADF-WP04-001 — EA-1 Documentation (prospective, pending WP-04 definition)
  EA-NADF-WP04-002 — EA-2 Repository Authority (prospective)
  EA-NADF-WP04-003 — EA-3 Configuration Authority (prospective — HR departments,
                     hr_holidays leave types, accrual plans, security groups,
                     employee record validation, work schedules)

Status        : All three entries are Pending Review. G1/G2/G3 reviews will be
                conducted once WP-04 work package document is created and the
                Go/No-Go checkpoint is initiated. Prospective entries will be
                updated to GRANTED or DENIED at that time.

Note          : No EA-4 (module installation) anticipated for WP-04 — hr and
                hr_holidays modules already installed (legacy Phase 3/4).
                No EA-5 (database mutation) anticipated — HR Core is configuration
                and ratification of existing employee data, not schema mutation.
                This assessment is subject to revision when WP-04 is formally defined.
```

---

*Authority Decision Log — NADF Project Pod*
*Maintained by A1-NADF Master Orchestrator*
*Software Factory Governance Authority — 2026-06-25*
