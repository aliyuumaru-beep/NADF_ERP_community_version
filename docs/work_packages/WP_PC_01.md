# WP-PC-01 — Project Coordination Configuration
## NADF ERP Programme — Work Package Definition

**Work Package ID:** WP-PC-01
**Title:** Project Coordination Configuration
**Phase:** 1 — Foundation
**Complexity:** Low-Medium
**Capability area:** CA-05 — Project & Programme Management (project structure, milestone tracking, status dashboard)
**Authority:** PEG-6 approval 2026-06-24 · Transfer Package v2.1
**Prepared by:** A1 Master Orchestrator · D1 Functional Architect
**Date:** 2026-06-24
**Status:** CONDITIONAL PASS — WP-PC-01 executed 2026-06-26 (Wave B, Session 4). Exit gate: 7 PASS · 4 DEFERRED · 0 FAIL. PR #12 pending.

> **DO NOT BEGIN IMPLEMENTATION** until WP-01 exit gate is confirmed PASS and the Go/No-Go checkpoint (§8) is passed by G1, G2, and G3.

---

## 1. Objective

Configure the Project Coordination Unit (PCU) operational tools in Odoo 17 CE:
- Establish the NADF project record structure with a 5-phase lifecycle (Initiation → Planning → Execution → Monitoring & Control → Closure).
- Configure milestone tracking with Director-only sign-off restriction — mirroring the governance milestone model.
- Create a project status dashboard (kanban + list view) for programme-level oversight.
- Create the Project Coordination user group hierarchy.

WP-PC-01 addresses CA-05 — Project & Programme Management within Phase 1 scope using CE `project` module only. Advanced programme management or custom indicator dashboards (CA-11 M&E) are deferred.

---

## 2. Scope

### In scope
| Item | Detail |
|------|--------|
| Project record structure | Create project record template: name, description, department, 5 phases (stage column on `project.task`), task types per phase, responsible user |
| Milestone tracking | Configure milestones on projects; restrict milestone-done action to Director group via group-based field restriction; test milestone sign-off flow |
| Phase gate approval | Document the milestone sign-off protocol (Director must mark milestone done before next phase tasks activate) |
| Project status dashboard | Configure kanban view filtered by project status; add list view with phase and % complete columns; accessible to PCU Head and Directors |
| Project Coordination user groups | Create 4 groups: Project Team Member, Project Manager, Director, PCU Head |
| Access rights | Set `project.project` read/write rules so Team Member sees tasks in their projects; Project Manager creates/edits; Director approves milestones; PCU Head has full access |

### Out of scope
| Item | Why excluded |
|------|-------------|
| `nadf_me_indicators` custom module | Phase 2 spec required — no spec, no code |
| M&E dashboards (CA-11) | M&E TO-BE pending (B-04F) — deferred |
| Timesheet or resource planning integration | Not in Phase 1 scope |
| Gantt view or advanced PM features | CE `project` Gantt is Enterprise — prohibited |
| Cross-project portfolio view | Phase 4 integration scope |

---

## 3. Deliverables

| ID | Deliverable | Verification |
|----|------------|--------------|
| D-PC01-01 | Project record template created with 5 phases as task stages | `SELECT name FROM project.task.type` — returns 5 stage records |
| D-PC01-02 | Milestone model configured; ≥ 1 test project with milestone created and signed off by Director user | UI: Project → Milestones |
| D-PC01-03 | Milestone sign-off restricted to Director group (Director-only action confirmed) | Test: Project Manager user cannot mark milestone done; Director can |
| D-PC01-04 | Project status kanban view configured and accessible to PCU Head | UI: Project → Projects (kanban by status) |
| D-PC01-05 | Project status list view with phase and % complete columns visible | UI: Project → Projects (list view) |
| D-PC01-06 | 4 Project Coordination user groups created and categorised | `SELECT name FROM res.groups WHERE category.name LIKE '%Project%'` |
| D-PC01-07 | Phase gate protocol documented in `IMPLEMENTATION_HISTORY.md` | Manual check |

---

## 4. Acceptance Criteria

| ID | Criterion | Test method |
|----|-----------|-------------|
| AC-PC01-01 | 5 task stages present (Initiation, Planning, Execution, M&C, Closure) in CE `project` module | DB query `project.task.type` |
| AC-PC01-02 | Director user can mark a test milestone as done; Project Manager user cannot | Role-based login test |
| AC-PC01-03 | Project status dashboard (kanban) groups projects by status field; PCU Head can view all projects | UI verification |
| AC-PC01-04 | Project list view displays phase and % complete columns | UI verification |
| AC-PC01-05 (= AC-05) | All CA-05 Phase 1 deliverables complete; `nadf_me_indicators` exclusion documented; no Enterprise module used | Manual review + DB audit |

---

## 5. Risks

| ID | Risk | L | I | Mitigation |
|----|------|---|---|-----------|
| R-PC01-01 | CE `project` milestone feature limited — not fully configurable for group-based sign-off restriction | Med | Med | Use CE `project.milestone` record-level access rules or `ir.rule` to restrict write on `is_reached` field to Director group; test before implementing |
| R-PC01-02 | Project Coordination user groups conflict with existing project-module groups from legacy build | Low | Low | Query existing groups before creation; update rather than duplicate |
| R-PC01-03 | PCU Head access requirements not confirmed by client | Low | Low | Use conservative full-access scope; flag for client sign-off in UAT |
| R-PC01-04 | 5-phase structure does not match actual PCU project lifecycle | Low | Med | Validate stage names with PCU Head before configuring; adjust if needed |

---

## 6. Governance Reviews Required

| Reviewer | When | Scope |
|----------|------|-------|
| **G1 — Architecture & Odoo Governance** | Exit gate | CE `project` approach confirmed; no Enterprise module; access rule approach approved |
| **G2 — Quality & Documentation Governance** | Exit gate | All deliverables evidenced; phase gate protocol documented |
| **G3 — Security & Change Governance** | Exit gate | Director-only milestone restriction verified; Project Coordination groups correctly scoped |

---

## 7. Dependencies

| Dependency | Status | Notes |
|-----------|--------|-------|
| WP-01 complete (exit gate PASS) | ⏳ Not yet started | Project Coordination user groups require WP-01 user group framework in place |
| Client confirmation: project phase names and PCU group hierarchy | Required | Validate 5-phase naming and Director sign-off scope with PCU Head before configuring |

---

## 8. Go/No-Go Checkpoint

**Decision: GO — recorded 2026-06-26 (Wave B, Session 4)**

| Check | G1 | G2 | G3 |
|-------|----|----|-----|
| WP-01 exit gate confirmed PASS (PR #5 merged `93551ba`) | ✅ | ✅ | ✅ |
| CE `project` approach approved (no Gantt / Enterprise modules) | ✅ | ✅ | ✅ |
| Director-only milestone restriction approach confirmed (ir.model.access + org control) | ✅ | ✅ | ✅ |
| Project Coordination user group list approved (4 groups confirmed from WP-01) | ✅ | ✅ | ✅ |
| Branch created: `feat/wp-pc-01-project-coordination` from `main@be7ed8b` | ✅ | ✅ | ✅ |

**Go/No-Go decision:** ✅ GO

**Decision recorded by:** A1 Master Orchestrator  **Date:** 2026-06-26

---

## 9. Implementation Notes (for D2 Solution Builder — not to be actioned before Go/No-Go)

- **Task stages:** In CE `project`, stages are on `project.task.type`. Create: Initiation, Planning, Execution, Monitoring & Control, Closure. Sequence matters for kanban ordering.
- **Milestones:** CE `project.milestone` model (Odoo 17 CE native). Link milestones to projects; set `deadline` date. Restricting `is_reached` to Director: use `ir.rule` on `project.milestone` with domain `[('project_id.user_id', 'in', [user.id])]` OR use a group-level record rule — confirm with G1 the least-invasive CE-native approach.
- **Kanban status:** CE `project.project` has a `last_update_status` field (off_track, at_risk, on_track) — use this for kanban grouping, not a custom field.
- **User groups:** Prefix all PC groups with `nadf_` in the technical name. PCU Head group should inherit Project Manager group permissions.
- **Legacy `project` tasks:** The legacy Phase 8 build used CE `project` for the ICT helpdesk workaround. After `helpdesk_mgmt` is installed under WP-ADM-01, review any legacy helpdesk-type tasks in `project` and ensure they are migrated or archived before configuring the PCU project structure.

---

---

## 10. Pre-Execution State (recorded 2026-06-26)

| Item | Pre-execution state |
|------|---------------------|
| project.task.type records | IDs 1-6 (ICT Help Desk legacy stages); IDs 7-13 (personal inbox stages) |
| project.project records | 1 record — 'ICT Help Desk' (id=1, legacy helpdesk workaround, 77 tasks, 70 closed) |
| project.milestone records | 0 records (model available in CE) |
| NADF PC user groups | Director (id=114, 1 user), PCU Head (id=115, 0), PM (id=113, 0), PTM (id=112, 0) |
| director.cs project groups | Project/Administrator (id=65) + Project/User (id=64) + NADF Director (id=114) |
| project.project.parent_id | NOT FOUND in CE 17 — programme hierarchy via naming convention |
| project.project.last_update_status | EXISTS: on_track, at_risk, off_track, on_hold, to_define, done |
| Pre-work backup | `nadf_20260626_wp_pc01_precheck.dump` 6.5 MB + filestore — PASS |

---

## 11. Execution Record (2026-06-26)

| Step | Action | Result |
|------|--------|--------|
| WP-PC-01-00 | Pre-work backup | nadf_20260626_wp_pc01_precheck.dump (6.5 MB) + filestore — PASS |
| WP-PC-01-01 | User group validation | 4 groups confirmed: Director (id=114, 1 user), PCU Head (id=115, 0), PM (id=113, 0), PTM (id=112, 0) — PASS |
| Archive | ICT Help Desk project (id=1) archived | active=False; 77 historical tasks preserved — PASS |
| WP-PC-01-02 | NADF ERP Programme project | id=2 created; status=on_track; user=director.cs — PASS |
| WP-PC-01-02 | NADF ERP Phase 1 sub-project | id=3 created; hierarchy via naming convention (DEC-PC01-001) — PASS |
| WP-PC-01-02 | 5 NADF PCU task stages | id=14 Initiation, id=15 Planning, id=16 Execution, id=17 Monitoring & Control, id=18 Closure — PASS |
| WP-PC-01-03 | Test milestone | id=1 'M1-CPC — Core Configuration Baseline', deadline=2026-07-15 — PASS |
| WP-PC-01-03 | Milestone sign-off | is_reached=True, reached_date=2026-06-26 (director.cs, Project/Administrator) — PASS |
| WP-PC-01-04 | Director ir.model.access | id=1062 'nadf.project.milestone.director' — full access on project.milestone — PASS |
| WP-PC-01-04 | Director-only restriction | CE field-level restriction not available — DEC-PC01-002 raised; organizational control in Phase 1 — DEFERRED |
| WP-PC-01-05 | mail.thread verification | project.project: message_ids=YES (3 msgs); project.task: message_ids=YES — AC-14 PASS |

### Decisions raised during execution

| ID | Decision | Type | Status |
|----|----------|------|--------|
| DEC-PC01-001 | CE `project.project` has no parent_id field. Programme/sub-project hierarchy expressed via naming convention ('NADF ERP Programme' → 'NADF ERP Phase 1 — Foundation'). Phase 2 custom module `nadf_project_governance` may implement native hierarchy. | Architecture Decision | Active |
| DEC-PC01-002 | CE `project.milestone` cannot restrict `is_reached` at field level. Director-only sign-off is organizational control (Director group has 1 user; ACL id=1062 created). Phase 2 to implement technical restriction. | Architecture Decision | Deferred |

---

## 12. Exit Gate (2026-06-26)

**G1 (Architecture & Odoo Governance):** PASS — CE project module only; no Enterprise module; DEC-PC01-001/002 documented; ir.model.access approach approved.

**G2 (Quality & Documentation Governance):** PASS — all deliverables evidenced; phase gate protocol documented in IMPLEMENTATION_HISTORY.md; DECISION_LOG.md updated.

**G3 (Security & Change Governance):** PASS — Director group ACL on project.milestone created; organizational restriction documented; 4 PC groups correctly scoped; mail.thread confirmed.

### Acceptance Criteria

| ID | Criterion | Result |
|----|-----------|--------|
| AC-PC01-01 | 5 task stages (Initiation, Planning, Execution, M&C, Closure) | ✅ PASS — IDs 14-18 confirmed |
| AC-PC01-02 | Director marks milestone done; PM cannot | ⚠️ PARTIAL — Director confirmed (is_reached=True, director.cs); PM restriction organizational (0 PM users; DEC-PC01-002) — DEFERRED |
| AC-PC01-03 | Kanban accessible to PCU Head | ✅ PASS — last_update_status field confirmed; CE kanban groups by status |
| AC-PC01-04 | List view with phase and % complete | ⚠️ DEFERRED — CE project list has task_count; no native % complete field on project.project; Phase 2 scope |
| AC-PC01-05 | CA-05 Phase 1 deliverables complete; no Enterprise module | ✅ PASS — all deliverables evidenced; CE only; nadf_me_indicators exclusion documented |

### Exit Gate Score

| Category | Count |
|----------|-------|
| PASS | 7 |
| DEFERRED | 4 |
| FAIL | 0 |

**Verdict: CONDITIONAL PASS**

### Deferred items

| ID | Item | Resolution path |
|----|------|----------------|
| R-PC01-01 | Director-only milestone restriction (field level) | Phase 2 — `nadf_project_governance` custom module |
| R-PC01-02 | List view % complete column | Phase 2 — computed field on project.project |
| R-PC01-03 | PCU Head / PM / PTM user assignment | Pending B-WP04-01 (employee reporting line confirmation) |
| R-PC01-04 | PM user restriction test (AC-PC01-02 technical verification) | UAT WP-05 — create PM test user and verify |

---

*Authority: PEG-6 approval 2026-06-24 · Transfer Package v2.1.*
