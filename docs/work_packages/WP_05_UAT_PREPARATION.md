# WP-05 — User Acceptance Testing (UAT) Preparation
## NADF ERP Programme — Phase 1 Foundation

---

**Document ID:** WP-05-UAT-PREP-001
**Document Type:** Work Package Definition + Test Plan
**Project Pod:** POD-NADF
**Work Package:** WP-05 — Phase 1 UAT / Operational Readiness
**Wave:** Wave C (preparation); Wave D (execution, pending client availability)
**Author:** A1 Master Orchestrator — Wave C
**Created:** 2026-06-29
**Status:** In Preparation — test plan authored; execution pending client scheduling

---

## 1. Purpose

WP-05 is the final Phase 1 Work Package. Its purpose is to verify that all 6 Phase 1 departmental configurations work correctly from a user perspective, that known gaps are pre-logged and accepted, and that the system is operationally ready for Phase 1 hand-over to NADF staff.

WP-05 does not develop new features. It tests what was delivered in WP-01 through WP-PC-01.

---

## 2. Scope

### 2.1 In Scope (Phase 1 UAT)

| Department | Work Package | UAT Coverage |
|------------|-------------|--------------|
| Finance | WP-02 | Chart of Accounts; vendor bills; payment workflow; analytic cost centres; budget positions; FY2026 budget |
| Procurement | WP-03 | Purchase request workflow; Call for Tender; goods receipt; vendor compliance status |
| Human Resources | WP-04 | Employee records; leave application and approval; recruitment pipeline; org chart |
| Administration | WP-ADM-01 | Fleet management; asset register; ICT helpdesk ticket lifecycle |
| Project Coordination | WP-PC-01 | NADF Programme project; Phase 1 sub-project; task stages; PCU milestone |
| ICT / Platform | WP-01 | TOTP 2FA enrollment; user login with roles; OCA module access |

### 2.2 Out of Scope (Phase 2+)

- `nadf_vendor_onboarding` portal UAT (requires live public URL)
- `nadf_facilities_management` UAT (unratified module — pending Phase 2 spec gate)
- `mis_builder` KPI dashboard (WP02-08 — blocked on client KPI sign-off)
- Multi-level procurement approval (WP03-07 — blocked on B-02/B-03)
- Payroll, legal contract, investment modules (Phase 2/3 development)

---

## 3. Pre-Conditions

| Pre-Condition | Status | Notes |
|--------------|--------|-------|
| All 6 Phase 1 WPs CONDITIONAL PASS | ✅ MET | M1-CPC CONDITIONAL PASS 2026-06-29 |
| NADF DB accessible (port 8071) | ✅ | Odoo 17 CE running |
| Wave C PR merged to main | ⏳ Pending | PR to be raised after WP-05 document complete |
| NADF client UAT participants identified | ⏳ Pending | Client scheduling required |
| NADF client has TOTP 2FA enrolled | ⏳ Pending | Each participant must complete TOTP setup |
| Known gaps pre-logged in defect register | ✅ MET (below §6) | All known gaps documented as pre-logged items |

---

## 4. UAT Test Plan

### 4.1 Test Environment

- **URL:** `http://localhost:8071`
- **Database:** `NADF`
- **Platform:** Odoo 17.0 Community Edition (106 modules)
- **Backup taken before UAT session:** mandatory (using `scripts/backup_nadf.sh`)

### 4.2 Test User Accounts

| Odoo Login | Role | Department |
|-----------|------|------------|
| `admin` | System Administrator | Platform |
| `director.cs` | Director Corporate Services (interim ICT/Fleet/Asset/Project Manager) | Multi-dept |
| Finance Officer account | Finance Officer | Finance |
| Finance Manager account | Finance Manager / CFO | Finance |
| Procurement Officer account | Procurement Officer | Procurement |
| Head of Procurement account | Head of Procurement | Procurement |
| HR Officer account | HR Officer | HR |
| Head HR account | Head HR / Time Off Officer | HR |

> Note: Each participant must complete TOTP enrollment (QR code scan) on first login. TOTP policy = `required`.

### 4.3 Test Scenarios by Department

---

#### TC-FIN-01: Vendor Bill Workflow

**Role:** Finance Officer → Finance Manager
**Steps:**
1. Finance Officer: Vendors → Create vendor bill (any supplier); add 1 line item; Save
2. Finance Officer: Confirm bill (Draft → Posted state)
3. Finance Manager: Review bill in accounting list; verify amount
4. Finance Officer: Register payment (Bank journal)
5. Verify payment status = In Payment / Paid
**Expected:** Bill posts cleanly; payment registers without error
**Known gap:** Payment is advisory-controlled (no hard block between roles) — DEC-WP02-001

---

#### TC-FIN-02: Budget View

**Role:** Finance Manager
**Steps:**
1. Accounting → Budgets → Budgets
2. Open "NADF FY2026 Budget" (id=1; state=confirm)
3. Verify 3 budget lines: Personnel Cost (₦495M), Operating Expenses (₦5M), Capital Expenditure (₦106.8B)
4. Verify budget state = Confirmed
5. Verify 3 Budgetary Positions exist under Configuration
**Expected:** Budget visible and confirmed; 3 positions map to correct CoA accounts
**Blocker:** mis_builder dashboard not yet built (WP02-08 pending client KPI sign-off)

---

#### TC-FIN-03: Analytic Cost Centres

**Role:** Finance Manager
**Steps:**
1. Accounting → Configuration → Analytic Accounts
2. Verify 5 accounts: CC-ADM, CC-EXE, CC-FIN, CC-HR, CC-PRO
3. Post a vendor bill and tag it to CC-FIN analytic account
4. Run Accounting → Reporting → Analytic Items
**Expected:** Analytic items show against correct cost centre

---

#### TC-PROC-01: Purchase Request Workflow

**Role:** Procurement Officer → Head of Procurement
**Steps:**
1. Procurement Officer: Purchase → Purchase Requests → New
2. Fill in request description, product, quantity; Submit for Approval
3. Head of Procurement: Approve the request
4. Verify request state = Approved
**Expected:** State machine transitions correctly; mail thread shows approval log

---

#### TC-PROC-02: Call for Tender

**Role:** Head of Procurement
**Steps:**
1. Purchase → Agreements → New → Type = "Call for Tender"
2. Add 2+ products; confirm agreement
3. Create 2 RFQs from agreement (Generate Alternatives)
4. Send RFQ to each vendor; compare; award one PO
5. Cancel losing RFQ; close agreement
**Expected:** Full tender cycle completes; awarded PO in purchase order list

---

#### TC-PROC-03: Goods Receipt

**Role:** Procurement Officer
**Steps:**
1. Confirm a purchase order (product in stock)
2. Navigate to Receipt (Inventory → Receipts)
3. Validate receipt (Done quantities = ordered quantities)
4. Verify stock move state = Done
**Expected:** Goods receipt posted; inventory updated

---

#### TC-HR-01: Leave Application

**Role:** Employee → Line Manager → Head HR
**Steps:**
1. Employee: Time Off → New → Annual Leave; select dates; confirm
2. Line Manager: Approve (first level)
3. Head HR (Time Off Officer): Approve (second level)
4. Verify leave state = Validated
**Expected:** Two-level approval works; email notifications sent

---

#### TC-HR-02: Recruitment Pipeline

**Role:** HR Officer
**Steps:**
1. Recruitment → Job Positions → Create vacancy
2. Create applicant; move through stages: Vacancy Posted → Shortlisted → Interview → Offer → Appointment
3. Mark hired (hired_stage = True on Appointment stage)
**Expected:** Applicant progresses through 5-stage pipeline; hired flag set

---

#### TC-HR-03: Employee Record & Org Chart

**Role:** HR Manager
**Steps:**
1. Employees → View employee list
2. Verify manager hierarchy for 3 employees (parent_id set)
3. Check employment state field (x_employment_state = employed)
4. Navigate Employees → Reporting → Org Chart (if CE provides one)
**Expected:** Manager chain visible; employment state populated for all 24 employees

---

#### TC-ADM-01: Fleet Management

**Role:** Director CS (Fleet Manager)
**Steps:**
1. Fleet → Vehicles → Verify 5 Toyota vehicles registered
2. Open one vehicle; verify model year, odometer reading, and service log
3. Add a new service record (Fuel Refueling type)
**Expected:** Vehicles appear; service record saves correctly

---

#### TC-ADM-02: Asset Register

**Role:** Director CS (Asset Manager)
**Steps:**
1. Accounting → Assets → Assets
2. Verify 61 total assets; open one validated asset
3. Confirm state = Open; check depreciation schedule active
**Expected:** Validated assets show running depreciation; asset count correct
**Known gap:** Motor Vehicles GL account mapping (DEC-ADM01-002) — correction deferred to Finance review

---

#### TC-ADM-03: ICT Helpdesk Ticket

**Role:** Any user → IT Manager (director.cs)
**Steps:**
1. Helpdesk → Tickets → New
2. Select ticket category (Hardware / Software / Network / Access / Service Outage)
3. Set priority; save
4. Assign to IT Manager team; mark resolved (stage = Done)
5. Verify mail thread shows 3+ messages
**Expected:** Ticket lifecycle completes; team assignment works
**Known gap:** No SLA model in helpdesk_mgmt (DEC-ADM01-001) — priority + stage timestamp as proxy

---

#### TC-PCU-01: Project and Task Management

**Role:** Director CS (Project Manager)
**Steps:**
1. Project → Projects → Verify "NADF ERP Programme" (id=2) and "NADF ERP Phase 1 — Foundation" (id=3)
2. Open Phase 1 project → Tasks → Verify 5 stages: Initiation / Planning / Execution / Monitoring & Control / Closure
3. Create a test task; move through stages
4. Project → Milestones → Verify "M1-CPC — Core Configuration Baseline" (is_reached=True)
**Expected:** Projects visible; stages work; milestone accessible to Director group
**Known gap:** Programme hierarchy is naming convention only (no parent_id in CE) — DEC-PC01-001

---

#### TC-ICT-01: TOTP 2FA Enrollment and Login

**Role:** Any participant
**Steps:**
1. Navigate to `http://localhost:8071/web/login`
2. Log in with credentials; system prompts TOTP enrollment (if not yet enrolled)
3. Scan QR code with authenticator app; enter TOTP token
4. Confirm login succeeds
**Expected:** TOTP enforced for all users; no bypass available without TOTP code

---

### 4.4 UAT Exit Criteria

| Criterion | Target |
|-----------|--------|
| Test scenarios executed | All 11 (TC-FIN-01/02/03, TC-PROC-01/02/03, TC-HR-01/02/03, TC-ADM-01/02/03, TC-PCU-01, TC-ICT-01) |
| Critical defects (blocker) | 0 |
| Known/pre-logged items | All pre-logged items from §6 accepted by client |
| Client sign-off | Business Sponsor signature on UAT completion record |

---

## 5. Known Defects — Pre-Logged (Accepted Before UAT)

These items are **pre-logged** and accepted as conditions of the CONDITIONAL PASS. They are not UAT failures.

| Defect ID | Description | Classification | Resolution Path |
|-----------|-------------|----------------|-----------------|
| KD-WP02-001 | Payment advisory-only (no hard block between Finance Officer and Finance Manager) | Accepted — Phase 2 | `nadf_approvals` custom module Phase 2 |
| KD-WP02-005 | mis_builder KPI dashboard not built (WP02-08 blocked) | Deferred — client sign-off | WP02-08 client session |
| KD-WP03-007 | Multi-level procurement approval thresholds not configured (WP03-07 blocked) | Deferred — B-02/B-03 | Client review session |
| KD-ADM01-001 | Helpdesk_mgmt has no SLA model; priority + stage timestamp proxy | Accepted — Phase 2 | `nadf_ict_helpdesk` Phase 2 |
| KD-ADM01-002 | Motor Vehicles GL account mapped to Earth Moving Equipment (legacy error) | Deferred — Finance review | Finance-owned correction |
| KD-ADM01-003 | Driver (107) and IT Officer (110) groups empty; Admin-dept users have no Odoo logins | Blocked — B-WP04-01 + user creation | NADF Client |
| KD-WP04-008 | Company RC/TIN not set | Blocked — B-WP04-02 | NADF Client |
| KD-PC01-001 | Programme hierarchy via naming convention only (no parent_id in CE) | Accepted — architectural | Phase 2 optional |
| KD-PC01-002 | project.milestone.is_reached not restricted at field level to Director group | Accepted — organizational control | Phase 2 nadf_project_governance |
| KD-HR-001 | Duplicate leave types (Paid Time Off/Annual Leave; Sick Time Off/Sick Leave) | Deferred — client guidance | Client review session |

---

## 6. UAT Defect Register Template

To be completed during UAT execution:

| Defect ID | Test Case | Description | Severity | Assigned To | Status | Resolution |
|-----------|-----------|-------------|----------|-------------|--------|------------|
| UAT-001 | | | | | Open | |

**Severity levels:** Critical (blocks go-live) / High (major function broken) / Medium (workaround available) / Low (cosmetic / minor)

---

## 7. WP-05 Exit Gate Criteria

| AC | Criterion | Evidence Required |
|----|-----------|-------------------|
| AC-UAT-01 | All 11 test scenarios executed | UAT session log / screenshots |
| AC-UAT-02 | Zero critical defects outstanding | Defect register reviewed |
| AC-UAT-03 | All pre-logged items accepted by client | Client sign-off on KD list |
| AC-UAT-04 | TOTP 2FA verified for all UAT participants | TC-ICT-01 PASS |
| AC-UAT-05 | Client Business Sponsor sign-off received | Sign-off record in this document |

---

## 8. Post-UAT Deliverables

Upon WP-05 PASS, the following documents are updated:

- `MILESTONE_TRACKER.md` — WP-05 PASS recorded; M1 milestone closure assessment triggered
- `IMPLEMENTATION_HISTORY.md` — WP-05 block added
- `CHANGELOG.md` — WP-05 section added
- `docs/governance/GOVERNANCE_APPROVAL_REGISTER.md` — WP-05 exit gate update
- `PROJECT_STATE.md` — updated to M1 closure assessment

M1 full closure requires WP-05 PASS + all client-dependent items resolved + human sponsor approval.

---

*WP-05 UAT Preparation — NADF ERP Programme*
*Document ID: WP-05-UAT-PREP-001 · Created: 2026-06-29*
*Produced by A1 Master Orchestrator — Wave C*
