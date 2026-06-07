#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 8e: HR Update
1. Updates work_email on 10 existing employees from M365 credentials
2. Adds 14 missing staff as HR employees with real @nadf.gov.ng emails
"""
import xmlrpc.client, sys

URL, DB, PW = 'http://localhost:8071', 'NADF', 'admin'
uid = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common').authenticate(DB, 'admin', PW, {})
if not uid: print("ERROR: Auth failed"); sys.exit(1)
m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, PW, model, method, args, kw or {})

print("=" * 60)
print("  Phase 8e — HR Update (Emails + Missing Staff)")
print("=" * 60)

# ── Step 1: Update emails on existing employees ───────────────────────────────
# From users_credentials.csv — match by display name to Odoo employee name
EXISTING_EMAILS = {
    'Adebanke Fajana':     'a.fajana@nadf.gov.ng',
    'Daniella Daniel':     'D.Daniel@nadf.gov.ng',
    'Jamila Alhassan':     'J.alhassan@nadf.gov.ng',
    'Kabir Haruna':        'K.haruna@nadf.gov.ng',
    'Kabir Abdulkadir':    'k.abdulkadir@nadf.gov.ng',
    'Maryam Koko':         'maryamkoko@nadf.gov.ng',
    'Mohammed Ahmed':      'M.ahmed@nadf.gov.ng',
    'Nasir Ingawa':        'n.ingawa@nadf.gov.ng',
    'Samuel Aende':        'S.Aende@nadf.gov.ng',
    'Suleiman Yusuf':      'S.Ibrahim@nadf.gov.ng',
}

print("\n[1] Updating existing employee emails...")
for name, email in EXISTING_EMAILS.items():
    emps = x('hr.employee', 'search_read', [[['name','ilike',name]]],
             {'fields':['id','name','work_email']})
    if not emps:
        print(f"  NOT FOUND: {name}")
        continue
    emp = emps[0]
    x('hr.employee', 'write', [[emp['id']], {'work_email': email}])
    print(f"  Updated: {emp['name']} → {email}")

# ── Step 2: Add 14 missing staff as employees ─────────────────────────────────
# These are in M365 but not yet in Odoo HR.
# Department mapping is inferred from role context — left as Administration if unknown.
NEW_STAFF = [
    # (full_name, email, job_title, department_name)
    ('Al-amin Uwais',         'A.Uwais@nadf.gov.ng',        'Staff',                  'Administration'),
    ('Ayinla Moshood',        't.ayinla@nadf.gov.ng',       'Staff',                  'Administration'),
    ('Bello Gidado',          'b.gidado@nadf.gov.ng',       'Staff',                  'Administration'),
    ('Sonny Nwarisi',         's.mwarisi@nadf.gov.ng',      'Director',               'Executive Office'),
    ('Enenede Idusuyi',       'E.Idusuyi@nadf.gov.ng',      'Staff',                  'Administration'),
    ('Ibrahim AlhaJi',        'I.muazualhagi@nadf.gov.ng',  'Staff',                  'Finance'),
    ('Mohammed Ali Bamalli',  'M.bamalli@nadf.gov.ng',      'Staff',                  'Administration'),
    ('Mohammed Ibrahim',      'm.ibrahim@nadf.gov.ng',      'Staff',                  'Administration'),
    ('Olanrewaju Wilton-Waddel', 'Owwaddell@nadf.gov.ng',  'Staff',                  'Administration'),
    ('Osayuki Innocent',      'O.innocent@nadf.gov.ng',     'Staff',                  'Administration'),
    ('Sam Ediale',            'S.ediale@nadf.gov.ng',       'Staff',                  'Finance'),
    ('Yakubu Ladan',          'Y.Ladan@nadf.gov.ng',        'Staff',                  'Administration'),
    ('Yusuf Jatto',           'y.jatto@nadf.gov.ng',        'Staff',                  'Administration'),
    ('Kabir Kabiir',          'admin@nadfgovng.onmicrosoft.com', 'ICT Administrator', 'Administration'),
]

print("\n[2] Adding 14 missing staff as employees...")

def get_dept(name):
    ids = x('hr.department', 'search', [[['name','=',name]]])
    return ids[0] if ids else None

created = skipped = 0
for full_name, email, job_title, dept_name in NEW_STAFF:
    existing = x('hr.employee', 'search', [[['name','ilike',full_name]]])
    if existing:
        print(f"  EXISTS : {full_name}")
        skipped += 1
        continue
    dept_id = get_dept(dept_name)
    emp_id = x('hr.employee', 'create', [{
        'name':          full_name,
        'work_email':    email,
        'job_title':     job_title,
        'department_id': dept_id,
    }])
    print(f"  Created: {full_name} | {email} | {dept_name} (id={emp_id})")
    created += 1

print(f"\n  Added: {created}  |  Skipped (exists): {skipped}")

# ── Summary ───────────────────────────────────────────────────────────────────
total_emp = x('hr.employee', 'search_count', [[['active','=',True]]])
print(f"\n  Total active employees: {total_emp}")
print("  Done.")
