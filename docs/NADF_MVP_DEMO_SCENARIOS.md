# NADF ERP MVP — Demo Scenarios Walkthrough
**Date:** 2026-06-04 | **URL:** http://localhost:8071 | **DB:** NADF

This document is the presenter's guide for the four live demo scenarios.
All data is pre-loaded in the system. Follow the steps in sequence.

---

## Pre-Demo Checklist
- [ ] Odoo running on http://localhost:8071
- [ ] Browser open, logged out (ready for login as different users)
- [ ] This document visible on second screen or printed

---

## Scenario 1 — Laptop Purchase (Mid-Value PO, Tier 2 Approval)
**Story:** Procurement Officer submits a purchase order for 5 laptops (₦2,418,750). The amount exceeds the ₦500K threshold — system automatically escalates to Director Corporate Services.

**Pre-loaded state:** PO P00007 is confirmed and awaiting Director CS approval.

### Steps
1. Log in as **Procurement Officer** (`procurement.officer` / `admin`)
2. Go to **Purchase → Orders → Purchase Orders**
3. Open **P00007** — show: vendor (TechLink ICT Solutions), 5 laptops × ₦450,000, status `To Approve`
4. Point out the **Chatter** — automation rule has already notified Director CS
5. Log out → log in as **Director Corporate Services** (`director.cs` / `admin`)
6. Open **Activities** (clock icon, top bar) — show the `PO Approval Required` activity
7. Open P00007 → click **Approve Order** → status changes to `Purchase Order`
8. Show chatter log — approval recorded with timestamp

**Key message:** The system enforces the approval tier automatically — no manual routing needed.

---

## Scenario 4 — Consultancy Contract (High-Value PO, Tier 3 Approval)
**Story:** A ₦8,062,500 capacity-building contract exceeds ₦5M — escalates to both Director CS AND Executive Secretary simultaneously.

**Pre-loaded state:** PO P00008 confirmed; both Director CS and Executive Secretary have approval activities.

### Steps
1. Log in as **Executive Secretary** (`executive.secretary` / `admin`)
2. Open **Activities** → show two PO activities: one for P00008 (ES) + FYI notification to Director CS
3. Open P00008 — show: ProLearn Training Institute, 50 person-days × ₦150,000, Notes reference `NADF/TRAINING/2026/001`
4. Click **Approve Order** as Executive Secretary
5. Log in as **Director Corporate Services** → show the FYI activity (informational, not blocking)
6. Mark the FYI activity as Done

**Key message:** Tiered escalation — low-value goes to Director CS, high-value goes all the way to Executive Secretary with Director CS kept in the loop.

---

## Scenario 2 — Annual Leave Request (HR Approval Workflow)
**Story:** Suleiman Yusuf (Finance Officer) submits 5 days' annual leave. It routes to Head of HR for approval.

**Pre-loaded state:** Leave request submitted and awaiting Head HR approval (state = `confirm`).

### Steps
1. Log in as **Suleiman Yusuf** (`finance.officer` / `admin`)
2. Go to **Time Off** → show the pending leave request (2026-07-01 to 2026-07-05, Annual Leave)
3. Log out → log in as **Head HR** (`head.hr` / `admin`)
4. Go to **Time Off → Managers → All Time Off**
5. Open Suleiman Yusuf's request → click **Approve**
6. Log back in as `finance.officer` → show leave status changed to `Approved`
7. Show the leave balance updated in the employee record

**Key message:** HR workflows are self-service — employees submit, managers approve, balances update automatically.

---

## Scenario 3 — Vendor Invoice with Finance Approval (Tier 2 Trigger)
**Story:** A ₦3,650,000 vendor bill for office furniture arrives. Finance Officer validates it — the amount (₦1M–₦10M range) automatically creates a Director CS approval activity.

**Pre-loaded state:** BILL/2026/06/0001 in **Draft** — Finance Officer must post it during the demo.

### Steps
1. Log in as **Finance Officer** (`finance.officer` / `admin`)
2. Go to **Invoicing → Vendors → Bills**
3. Open **BILL/2026/06/0001** — show: Abuja Office Supplies Ltd, 3 line items, total ₦3,650,000, ref `DEMO-S3-INV-2026-0147`
4. Click **Confirm** (post the invoice) → status changes to `Posted`
5. Show the **Chatter** — automation rule fires and creates a Director CS activity
6. Log out → log in as **Director Corporate Services** (`director.cs` / `admin`)
7. Open **Activities** → show `Invoice Escalation` activity for the bill
8. Open the bill → mark activity as Done (or schedule a payment)

**Key message:** Finance controls are built in — no invoice above ₦1M goes unreviewed by senior management.

---

## User Login Reference

| Role | Username | Password |
|------|----------|----------|
| Administrator | admin | admin |
| Executive Secretary | executive.secretary | admin |
| Director Corporate Services | director.cs | admin |
| Head of Finance | head.finance | admin |
| Finance Officer | finance.officer | admin |
| Head of Procurement | head.procurement | admin |
| Procurement Officer | procurement.officer | admin |
| Head of HR | head.hr | admin |
| HR Officer | hr.officer | admin |

---

## Demo Data Reference

| Item | Reference | Amount | Status |
|------|-----------|--------|--------|
| Laptop Purchase PO | P00007 | ₦2,418,750 | To Approve (Dir CS) |
| Consultancy PO | P00008 | ₦8,062,500 | To Approve (Exec Sec) |
| Annual Leave | Suleiman Yusuf | 5 days | Awaiting Head HR |
| Vendor Invoice | BILL/2026/06/0001 | ₦3,650,000 | Draft (post during demo) |

---

*Generated: 2026-06-04 | NADF ERP MVP Phase 6*
