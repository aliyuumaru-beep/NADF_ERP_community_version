#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 4 HR Configuration
Configures: departments, job positions, sample employees, leave types
Run: python3 scripts/phase4_hr_configuration.py
"""

import xmlrpc.client, sys

URL, DB = 'http://localhost:8071', 'NADF'
ADMIN_PASS = 'admin'
uid = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common').authenticate(DB, 'admin', ADMIN_PASS, {})
if not uid:
    print("ERROR: Auth failed"); sys.exit(1)
m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, ADMIN_PASS, model, method, args, kw or {})

def find(model, domain):
    res = x(model, 'search', [domain], {'limit': 1})
    return res[0] if res else None

print("=" * 60)
print("  NADF ERP MVP — Phase 4 HR Configuration")
print("=" * 60)

# ── 1. Departments ────────────────────────────────────────────────────────────
print("\n[1/4] Creating departments...")

departments = {}
dept_defs = [
    ('Executive Office',  None),
    ('Finance',           None),
    ('Procurement',       None),
    ('Human Resources',   None),
    ('Administration',    None),
]
for dname, parent in dept_defs:
    existing = x('hr.department', 'search', [[['name','=',dname],['company_id','=',1]]])
    if existing:
        departments[dname] = existing[0]
        print(f"  SKIP (exists): {dname}")
        continue
    vals = {'name': dname, 'company_id': 1}
    if parent:
        vals['parent_id'] = departments.get(parent)
    did = x('hr.department', 'create', [vals])
    departments[dname] = did
    print(f"  Created: {dname}")

# ── 2. Job Positions ──────────────────────────────────────────────────────────
print("\n[2/4] Creating job positions...")

positions = {}
pos_defs = [
    # (title,                    department,         no_of_recruitment)
    ('Executive Secretary',      'Executive Office', 1),
    ('Director Corporate Services','Executive Office',1),
    ('Head of Finance',          'Finance',          1),
    ('Finance Officer',          'Finance',          2),
    ('Senior Finance Officer',   'Finance',          1),
    ('Head of Procurement',      'Procurement',      1),
    ('Procurement Officer',      'Procurement',      2),
    ('Senior Procurement Officer','Procurement',     1),
    ('Head of HR',               'Human Resources',  1),
    ('HR Officer',               'Human Resources',  2),
    ('Senior HR Officer',        'Human Resources',  1),
    ('Admin Officer',            'Administration',   2),
    ('ICT Officer',              'Administration',   1),
]
for title, dept, recruitment in pos_defs:
    dept_id = departments.get(dept)
    existing = x('hr.job', 'search', [[['name','=',title],['department_id','=',dept_id]]])
    if existing:
        positions[title] = existing[0]
        print(f"  SKIP (exists): {title}")
        continue
    jid = x('hr.job', 'create', [{
        'name':              title,
        'department_id':     dept_id,
        'no_of_recruitment': recruitment,
        'company_id':        1,
    }])
    positions[jid] = jid
    positions[title] = jid
    print(f"  Created: {title} ({dept})")

# ── 3. Sample Employees ───────────────────────────────────────────────────────
print("\n[3/4] Creating sample employees...")

# Link Odoo users to employees where applicable
def get_user_id(login):
    res = x('res.users', 'search_read', [[['login','=',login]]], {'fields': ['id','name']})
    return res[0]['id'] if res else None

employees = [
    {
        'name':         'Maryam Koko',
        'job_title':    'Executive Secretary',
        'job_id':       positions.get('Executive Secretary'),
        'department_id':departments.get('Executive Office'),
        'work_email':   'maryamkoko@nadf.gov.ng',
        'employee_type':'employee',
        'user_id':      get_user_id('executive.secretary'),
        'emp_no':       'NADF-001',
    },
    {
        'name':         'Nasir Ingawa',
        'job_title':    'Director Corporate Services',
        'job_id':       positions.get('Director Corporate Services'),
        'department_id':departments.get('Executive Office'),
        'work_email':   'n.ingawa@nadf.gov.ng',
        'employee_type':'employee',
        'user_id':      get_user_id('director.cs'),
        'emp_no':       'NADF-002',
    },
    {
        'name':         'Adebanke Fajana',
        'job_title':    'Head of Finance',
        'job_id':       positions.get('Head of Finance'),
        'department_id':departments.get('Finance'),
        'work_email':   'a.fajana@nadf.gov.ng',
        'employee_type':'employee',
        'user_id':      get_user_id('head.finance'),
        'emp_no':       'NADF-003',
    },
    {
        'name':         'Suleiman Yusuf',
        'job_title':    'Finance Officer',
        'job_id':       positions.get('Finance Officer'),
        'department_id':departments.get('Finance'),
        'work_email':   'S.Ibrahim@nadf.gov.ng',
        'employee_type':'employee',
        'user_id':      get_user_id('finance.officer'),
        'emp_no':       'NADF-004',
    },
    {
        'name':         'Kabir Abdulkadir',
        'job_title':    'Head of Procurement',
        'job_id':       positions.get('Head of Procurement'),
        'department_id':departments.get('Procurement'),
        'work_email':   'k.abdulkadir@nadf.gov.ng',
        'employee_type':'employee',
        'user_id':      get_user_id('head.procurement'),
        'emp_no':       'NADF-005',
    },
    {
        'name':         'Jamila Alhassan',
        'job_title':    'Procurement Officer',
        'job_id':       positions.get('Procurement Officer'),
        'department_id':departments.get('Procurement'),
        'work_email':   'J.alhassan@nadf.gov.ng',
        'employee_type':'employee',
        'user_id':      get_user_id('procurement.officer'),
        'emp_no':       'NADF-006',
    },
    {
        'name':         'Kabir Haruna',
        'job_title':    'Head of HR',
        'job_id':       positions.get('Head of HR'),
        'department_id':departments.get('Human Resources'),
        'work_email':   'K.haruna@nadf.gov.ng',
        'employee_type':'employee',
        'user_id':      get_user_id('head.hr'),
        'emp_no':       'NADF-007',
    },
    {
        'name':         'Daniella Daniel',
        'job_title':    'HR Officer',
        'job_id':       positions.get('HR Officer'),
        'department_id':departments.get('Human Resources'),
        'work_email':   'D.Daniel@nadf.gov.ng',
        'employee_type':'employee',
        'user_id':      get_user_id('hr.officer'),
        'emp_no':       'NADF-008',
    },
    {
        'name':         'Samuel Aende',
        'job_title':    'Admin Officer',
        'job_id':       positions.get('Admin Officer'),
        'department_id':departments.get('Administration'),
        'work_email':   'S.Aende@nadf.gov.ng',
        'employee_type':'employee',
        'emp_no':       'NADF-009',
    },
    {
        'name':         'Mohammed Ahmed',
        'job_title':    'ICT Officer',
        'job_id':       positions.get('ICT Officer'),
        'department_id':departments.get('Administration'),
        'work_email':   'M.ahmed@nadf.gov.ng',
        'employee_type':'employee',
        'emp_no':       'NADF-010',
    },
]

emp_ids = {}
for e in employees:
    existing = x('hr.employee', 'search', [[['name','=',e['name']],['company_id','=',1]]])
    if existing:
        emp_ids[e['name']] = existing[0]
        print(f"  SKIP (exists): {e['name']}")
        continue
    vals = {
        'name':          e['name'],
        'job_title':     e['job_title'],
        'department_id': e['department_id'],
        'work_email':    e['work_email'],
        'employee_type': e['employee_type'],
        'company_id':    1,
    }
    if e.get('job_id'):
        vals['job_id'] = e['job_id']
    if e.get('user_id'):
        vals['user_id'] = e['user_id']
    eid = x('hr.employee', 'create', [vals])
    emp_ids[e['name']] = eid
    print(f"  Created: [{e['emp_no']}] {e['name']} — {e['job_title']}")

# Set manager relationships
def set_manager(emp_name, manager_name):
    emp_id = emp_ids.get(emp_name)
    mgr_id = emp_ids.get(manager_name)
    if emp_id and mgr_id:
        x('hr.employee', 'write', [[emp_id], {'parent_id': mgr_id}])

print("\n  Setting reporting lines...")
set_manager('Nasir Ingawa',      'Maryam Koko')
set_manager('Adebanke Fajana',   'Nasir Ingawa')
set_manager('Kabir Abdulkadir',  'Nasir Ingawa')
set_manager('Kabir Haruna',      'Nasir Ingawa')
set_manager('Suleiman Yusuf',    'Adebanke Fajana')
set_manager('Jamila Alhassan',   'Kabir Abdulkadir')
set_manager('Daniella Daniel',   'Kabir Haruna')
set_manager('Samuel Aende',      'Nasir Ingawa')
set_manager('Mohammed Ahmed',    'Nasir Ingawa')
print("  Reporting lines configured")

# ── 4. Leave Types ────────────────────────────────────────────────────────────
print("\n[4/4] Configuring leave types...")

leave_types = [
    ('Annual Leave',        'hr',      10, False),
    ('Sick Leave',          'manager',  1, True),
    ('Casual Leave',        'manager',  4, False),
    ('Maternity Leave',     'hr',       6, True),
    ('Paternity Leave',     'hr',       2, True),
    ('Study Leave',         'both',     8, True),
    ('Compassionate Leave', 'hr',       3, False),
]

for name, validation, color, doc in leave_types:
    existing = x('hr.leave.type', 'search', [[['name','=',name]]])
    if existing:
        print(f"  SKIP (exists): {name}")
        continue
    lid = x('hr.leave.type', 'create', [{
        'name':                  name,
        'requires_allocation':   'no',
        'leave_validation_type': validation,
        'employee_requests':     'yes',
        'request_unit':          'day',
        'color':                 color,
        'support_document':      doc,
        'time_type':             'leave',
        'company_id':            1,
    }])
    print(f"  Created: {name:25s} — approval: {validation}")

# ── Summary ───────────────────────────────────────────────────────────────────
total_depts    = x('hr.department', 'search_count', [[['company_id','=',1]]])
total_positions= x('hr.job',        'search_count', [[['company_id','=',1]]])
total_employees= x('hr.employee',   'search_count', [[['company_id','=',1],['active','=',True]]])
total_leaves   = x('hr.leave.type', 'search_count', [[['company_id','in',[1,False]]]])

print("\n" + "=" * 60)
print("  Phase 4 HR Configuration — COMPLETE")
print("=" * 60)
print(f"  Departments   : {total_depts}")
print(f"  Job positions : {total_positions}")
print(f"  Employees     : {total_employees}")
print(f"  Leave types   : {total_leaves}")
print("\n  Next: Phase 5 — Approval Workflow Configuration")
