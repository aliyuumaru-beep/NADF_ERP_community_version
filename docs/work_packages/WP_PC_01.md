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
**Status:** PLANNED — awaiting WP-01 completion and G1/G2/G3 Go/No-Go clearance before implementation

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

## 8. Go/No-Go Checkpoint (required before implementation begins)

**This checkpoint must be passed before D2 Solution Builder executes a single configuration command.**

G1, G2, and G3 must each confirm:

| Check | G1 | G2 | G3 |
|-------|----|----|-----|
| WP-01 exit gate confirmed PASS | ☐ | ☐ | ☐ |
| CE `project` approach approved (no Gantt / Enterprise modules) | ☐ | ☐ | ☐ |
| Director-only milestone restriction approach confirmed | ☐ | ☐ | ☐ |
| Project Coordination user group list approved | ☐ | ☐ | ☐ |
| Branch created for WP-PC-01 implementation | ☐ | ☐ | ☐ |

**Go/No-Go decision:** ☐ GO  ☐ NO-GO (record reason and remediation action)

**Decision recorded by:** ______________________  **Date:** ____________

---

## 9. Implementation Notes (for D2 Solution Builder — not to be actioned before Go/No-Go)

- **Task stages:** In CE `project`, stages are on `project.task.type`. Create: Initiation, Planning, Execution, Monitoring & Control, Closure. Sequence matters for kanban ordering.
- **Milestones:** CE `project.milestone` model (Odoo 17 CE native). Link milestones to projects; set `deadline` date. Restricting `is_reached` to Director: use `ir.rule` on `project.milestone` with domain `[('project_id.user_id', 'in', [user.id])]` OR use a group-level record rule — confirm with G1 the least-invasive CE-native approach.
- **Kanban status:** CE `project.project` has a `last_update_status` field (off_track, at_risk, on_track) — use this for kanban grouping, not a custom field.
- **User groups:** Prefix all PC groups with `nadf_` in the technical name. PCU Head group should inherit Project Manager group permissions.
- **Legacy `project` tasks:** The legacy Phase 8 build used CE `project` for the ICT helpdesk workaround. After `helpdesk_mgmt` is installed under WP-ADM-01, review any legacy helpdesk-type tasks in `project` and ensure they are migrated or archived before configuring the PCU project structure.

---

*This work package definition is a planning document only. Implementation does not begin until §8 Go/No-Go passes and WP-01 exit gate is confirmed. Authority: PEG-6 approval 2026-06-24 · Transfer Package v2.1.*
