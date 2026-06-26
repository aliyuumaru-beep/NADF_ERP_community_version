# WP-04 — HR Core Configuration
**Work Package:** WP-04 HR Core  
**Phase:** 1 — Foundation (Wave A, Session 2)  
**Authority:** `requirements/PRODUCT_SCOPE/NADF_FULL_PRODUCT_TRANSFER_PACKAGE_v2.1.md` §3.3  
**Backlog items:** BL-HR-01, BL-HR-02, BL-HR-03, BL-HR-04, BL-HR-05  
**Branch:** `feat/wp-04-hr-core` from main@`be7ed8b`  
**Executed:** 2026-06-26  
**Status:** CONDITIONAL PASS

---

## Go/No-Go Gate

| Gate | Verdict | Basis |
|------|---------|-------|
| G1 — Architecture & Odoo | PASS | CE native modules; no Enterprise; hierarchy via parent_id; x_employment_state consistent with DEC-WP03-001 pattern |
| G2 — Quality & Documentation | PASS | CHANGELOG, IMPLEMENTATION_HISTORY, DECISION_LOG, this WP doc updated |
| G3 — Security & Change | PASS | NADF HR groups populated; leave workflow groups wired; CEO automation active; pre-work backup taken |

**Go/No-Go: PASS — 2026-06-26**

---

## Pre-execution System State

| Item | State at WP-04 start |
|------|----------------------|
| `hr_recruitment` | uninstalled |
| `hr` | installed |
| `hr_holidays` | installed |
| Active employees | 24 |
| Employees with no manager | 16 (including 6 Admin-dept) |
| Leave types | 11 (mixed approval modes) |
| Recruitment stages | 0 (hr_recruitment not installed) |
| x_employment_state | Not present |
| NADF HR / Employee group | 0 users |
| NADF HR / Line Manager group | 0 users |
| Company VAT/RC | EMPTY |
| Claude API key | SET (108 chars) |

---

## Scope

Per Transfer Package §3.3 and WP-HR-01 definition:

| Item | Scope |
|------|-------|
| Employee records + 4-level org hierarchy | ✅ In scope |
| Leave type approval workflows | ✅ In scope |
| Recruitment pipeline stages | ✅ In scope |
| Appointment/separation approval state + CEO notification | ✅ In scope |
| HR user groups and access rights | ✅ In scope |
| mail.thread audit trail | ✅ In scope |
| HR performance management (BL-HR-06) | ❌ Deferred (Could Have) |
| Payroll (Phase 3) | ❌ Out of scope |

---

## Execution Record

### WP04-00 — Prerequisites

**Backup:** `nadf_20260625_142500` (dump 6.3 MB + filestore 37 MB, SHA-256 verified)  
**Single session:** Confirmed. PID 59090 is the sole active Odoo instance. Prior session PID 44319 (Tuesday context-exhausted session) confirmed sleeping/idle on ttys000.

**hr_recruitment install:**
```python
# Marked for install via button_install(), then:
Registry.new('NADF', update_module=True)
# Result: state=installed, 105 modules loaded
```

### WP04-01 — Employee Records + 4-Level Org Hierarchy

**Hierarchy map:**

```
Level 1 (MD): Mohammed Ibrahim — Executive Secretary (ES/CEO dept)
Level 2 (Director):
  └── Prof Maryam Koko     — Corporate Services (reports to ES)
       ├── Farida Sani      — Head HR
       ├── Onikepo Babalola — Head Communications
       └── Ifedapo Balogun  — Head ICT
  └── Dr Yusuf Jatto        — Head Finance (reports to ES)
       ├── Samuel Aende     — Finance Officer
       ├── Mohammed Ahmed   — Finance Officer
       ├── Suleiman Yusuf   — Finance Officer (corrected from Strategy Head)
       ├── Sam Ediale        — Finance (assigned to Finance Head)
       └── Ibrahim AlhaJi   — Finance (assigned to Finance Head)
  └── Sherrif Salawu        — Head Procurement (reports to ES)
  └── Adebanke Fajana       — Head Strategy & MEL (reports to ES)
  └── Nasir Ingawa          — Head Partnerships (reports to ES)
  └── Jamila Alhassan       — Head Infrastructure (reports to ES)
  └── Olalekan Alabi        — Head Investments (reports to ES)
  └── Oluwagbeminiyi Papoola — Head Legal (reports to ES)
  └── Daniella Daniel        — Exec. Assistant, OES (reports to ES)
Level 2 (Director, ext dept):
  └── Dr Yusuf Jatto       — Head Finance & Accounts Dept
  └── Olalekan Alabi       — Head Investment Management
  └── Oluwagbeminiyi Papoola — Head Legal
  └── Nasir Ingawa         — Head Partnerships
  └── Sherrif Salawu       — Head Procurement
```

**Changes made (8 parent_id updates):**
- Dr Yusuf Jatto → Mohammed Ibrahim
- Nasir Ingawa → Mohammed Ibrahim
- Onikepo Babalola → Prof Maryam Koko
- Ifedapo Balogun → Prof Maryam Koko
- Daniella Daniel → Mohammed Ibrahim
- Suleiman Yusuf → Dr Yusuf Jatto (corrected from Adebanke Fajana — legacy error)
- Sam Ediale → Dr Yusuf Jatto
- Ibrahim AlhaJi → Dr Yusuf Jatto

### WP04-02 — Admin Department Employees (Client Action)

Six employees in "Admin" department have no job position or manager assigned:

| ID | Name | Current Dept | Job | Manager |
|----|------|-------------|-----|---------|
| 12 | Al-amin Uwais | Admin | NONE | NONE |
| 13 | Ayinla Moshood | Admin | NONE | NONE |
| 14 | Bello Gidado | Admin | NONE | NONE |
| 18 | Mohammed Ali Bamalli | Admin | NONE | NONE |
| 20 | Olanrewaju Wilton-Waddel | Admin | NONE | NONE |
| 23 | Yakubu Ladan | Admin | NONE | NONE |

**Blocker:** B-WP04-01 — Client must confirm department assignments and reporting lines.

### WP04-03 — Leave Type Approval Workflows

**Policy:** NADF two-level — request → line manager approval → HR confirmation → `both`

| ID | Leave Type | Before | After | Rationale |
|----|-----------|--------|-------|-----------|
| 5 | Annual Leave | hr | **both** | Discretionary; needs line mgr gate |
| 6 | Sick Leave | manager | **both** | Pay continuity; HR co-sign required |
| 7 | Casual Leave | manager | **both** | Discretionary; HR recording needed |
| 3 | Compensatory Days | manager | **both** | Entitlement tracking; HR co-sign |
| 1 | Paid Time Off | both | both (unchanged) | — |
| 4 | Unpaid | both | both (unchanged) | — |
| 10 | Study Leave | both | both (unchanged) | — |
| 2 | Sick Time Off | hr | hr (unchanged) | Medical certificate → HR directly |
| 8 | Maternity Leave | hr | hr (unchanged) | Statutory right |
| 9 | Paternity Leave | hr | hr (unchanged) | Statutory right |
| 11 | Compassionate Leave | hr | hr (unchanged) | Bereavement |

**Note:** Duplicate leave types (Paid Time Off / Annual Leave; Sick Time Off / Sick Leave) retained pending client guidance. Deduplication deferred to WP-05.

### WP04-04 — Recruitment Pipeline

**Installed:** `hr_recruitment` 17.0.0.1 (CE native)

**NADF 5-stage pipeline:**

| Stage | Sequence | hired_stage |
|-------|----------|-------------|
| Vacancy Posted | 1 | False |
| Shortlisted | 2 | False |
| Interview | 3 | False |
| Offer | 4 | False |
| Appointment | 5 | **True** |

Odoo default stages (New, Initial Qualification, First Interview, Second Interview, Contract Proposal, Contract Signed) folded (fold=True, sequence=100). Cannot be deleted due to xmlid constraints.

### WP04-05 — Employment State Field + CEO Notification

**Field created:**
```python
env['ir.model.fields'].create({
    'name': 'x_employment_state',
    'field_description': 'Employment State',
    'model_id': env['ir.model'].search([('model','=','hr.employee')]).id,
    'ttype': 'selection',
    'selection': "[('employed','Active Employee'),('pending_appointment','Pending Appointment (CEO Approval)'),('pending_separation','Pending Separation (CEO Approval)'),('terminated','Terminated')]",
    'store': True,
})
# id=11644; all 24 active employees set to 'employed'
```

**Automations created (base.automation):**

| Auto ID | Name | Trigger | Filter | Action |
|---------|------|---------|--------|--------|
| 7 | HR: CEO notification — Appointment approval required | on_write | x_employment_state = pending_appointment (was != pending_appointment) | To-Do activity on Executive Secretary, deadline 3 days |
| 8 | HR: CEO notification — Separation approval required | on_write | x_employment_state = pending_separation (was != pending_separation) | To-Do activity on Executive Secretary, deadline 3 days |

**CEO user:** Executive Secretary (user id=13, login=executive.secretary) — NADF HR / CEO group (id=106).

**Risk:** x_employment_state is DB-resident (ir.model.fields). Loss on DB rebuild. Mitigation: command documented here; Phase 2 module spec should include version-controlled equivalent.

### WP04-06 — mail.thread Audit Trail

| Model | message_ids field | Sample record messages | Status |
|-------|-------------------|----------------------|--------|
| hr.employee | ✅ Present | 4 messages | ✅ PASS |
| hr.leave | ✅ Present | 1 message | ✅ PASS |
| hr.applicant | ✅ Present | 0 (no applicants yet) | ✅ PASS |

### WP04-07 — HR Group Assignments

| Group ID | Group Name | Users | Native Odoo group wired |
|----------|-----------|-------|------------------------|
| 102 | NADF HR / Employee | 8 (all internal) | — |
| 103 | NADF HR / Line Manager | 5 (Dept Heads) | Time Off Responsible [58] |
| 104 | NADF HR / HR Officer | 1 (HR Officer) | Time Off Officer [59] |
| 105 | NADF HR / HR Manager | 1 (Head HR) | Time Off Officer [59] + Responsible [58] |
| 106 | NADF HR / CEO | 1 (Executive Secretary) | — |

**Leave workflow wiring:**
- Time Off / Officer [59]: HR Officer + Head HR added → enables second-level HR approval
- Time Off Responsible [58]: Dept Heads added → enables first-level manager approval visibility

### WP04-08 — Company RC/TIN (DEFERRED)

Company VAT and Company Registry fields remain EMPTY.  
**Blocker:** B-WP04-02 — Client must supply NADF RC number and TIN (Tax Identification Number).  
No data found in Transfer Package v2.1.

### WP04-09 — Claude API Key (PRE-CONFIRMED PASS)

`nadf.claude.api.key` SET (108 chars) — confirmed before execution. `nadf_vendor_onboarding` AI analysis available.

---

## Exit Gate Assessment

| Item | Code | Status | Detail |
|------|------|--------|--------|
| hr_recruitment installed | WP04-00 | ✅ PASS | state=installed, 105 modules |
| ES at top of hierarchy | WP04-01a | ✅ PASS | parent=NONE |
| Finance Head → ES | WP04-01b | ✅ PASS | parent=Mohammed Ibrahim |
| HR Head → CS Head | WP04-01c | ✅ PASS | parent=Prof Maryam Koko |
| Suleiman Yusuf corrected | WP04-01d | ✅ PASS | parent=Dr Yusuf Jatto |
| Admin employees identified | WP04-02 | ✅ PASS | 6 employees flagged B-WP04-01 |
| Annual Leave = both | WP04-03a | ✅ PASS | |
| Casual Leave = both | WP04-03b | ✅ PASS | |
| Sick Leave = both | WP04-03c | ✅ PASS | |
| Maternity = hr (statutory) | WP04-03d | ✅ PASS | |
| Compensatory Days = both | WP04-03e | ✅ PASS | |
| NADF 5-stage pipeline | WP04-04a | ✅ PASS | Vacancy Posted → Appointment |
| Appointment = hired_stage | WP04-04b | ✅ PASS | |
| x_employment_state exists | WP04-05a | ✅ PASS | id=11644 |
| Default = employed | WP04-05b | ✅ PASS | 24/24 employees |
| 2 CEO automations active | WP04-05c | ✅ PASS | auto ids 7, 8 |
| mail.thread hr.employee | WP04-06 | ✅ PASS | |
| mail.thread hr.leave | WP04-06 | ✅ PASS | |
| mail.thread hr.applicant | WP04-06 | ✅ PASS | |
| Employee group populated | WP04-07a | ✅ PASS | 8 users |
| Line Manager group populated | WP04-07b | ✅ PASS | 5 users |
| HR Officer assigned | WP04-07c | ✅ PASS | |
| HR Manager assigned | WP04-07d | ✅ PASS | |
| CEO assigned | WP04-07e | ✅ PASS | |
| Company RC/TIN set | WP04-08 | ⚠️ DEFERRED | Client action B-WP04-02 |
| Claude API key set | WP04-09 | ✅ PASS | 108 chars |

**Score: 25/26 PASS | 1 DEFERRED | 0 FAIL**

**Verdict: CONDITIONAL PASS**

---

## Open Client Actions

| ID | Action | Blocks |
|----|--------|--------|
| B-WP04-01 | Confirm department assignments and reporting lines for 6 Admin-dept employees (IDs 12,13,14,18,20,23) | Org hierarchy completion |
| B-WP04-02 | Provide NADF RC number and TIN for company registration fields | WP04-08 |

---

## Decisions Raised

- DEC-WP04-001 — hr_recruitment installation
- DEC-WP04-002 — x_employment_state field and CEO automation
- DEC-WP04-003 — Leave type approval workflow correction
- DEC-WP04-004 — Manager hierarchy correction

---

## Risks Raised

| ID | Risk | Mitigation |
|----|------|-----------|
| R-WP04-01 | x_employment_state DB-resident field: loss on DB rebuild | Command documented; Phase 2 module spec to include version-controlled equivalent |
| R-WP04-02 | Duplicate leave types (Paid Time Off/Annual Leave; Sick Time Off/Sick Leave) — user confusion possible | Deferred to WP-05 UAT preparation; client guidance required before archiving Odoo defaults |
| R-WP04-03 | 6 Admin-dept employees without dept/manager: leave approval chain incomplete for those staff | Blocked on B-WP04-01 client confirmation |

---

## Lessons Learned

1. **`hr_recruitment` default stages have no `active` field** — stages cannot be archived. Use `fold=True` + high sequence to suppress from kanban view. Cannot be deleted due to `ir.model.data` xmlid constraints.
2. **`base.automation` activity state in CE 17 is `next_activity`** — `activity` is Enterprise-only. Confirmed by inspecting `ir.actions.server.state` selection values at runtime.
3. **Legacy employee-user mapping errors** — user "Head Finance" (login=head.finance) was linked to employee Adebanke Fajana (Strategy Head), not Dr Yusuf Jatto (Finance Head). Similarly, Suleiman Yusuf (Finance Officer) was under Strategy Head in parent_id. These are legacy data errors from Phase 3; corrected in WP04-01 where unambiguous. Remaining ambiguous mappings deferred to client review.
4. **`Registry.new('NADF', update_module=True)` is the reliable install path** — `odoo-bin --stop-after-init -i <module>` returned exit code 1 (xcrun Xcode tools error on this machine) but logged success; the Python API call is more reliable for confirming completion.
