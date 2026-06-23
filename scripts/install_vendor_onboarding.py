#!/usr/bin/env python3
"""
NADF ERP — Install nadf_vendor_onboarding module
Run: python3 scripts/install_vendor_onboarding.py
"""

import xmlrpc.client, sys, time

URL, DB = 'http://localhost:8071', 'NADF'
ADMIN_PASS = 'admin'

common = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common')
uid = common.authenticate(DB, 'admin', ADMIN_PASS, {})
if not uid:
    print("ERROR: Authentication failed"); sys.exit(1)

m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, ADMIN_PASS, model, method, args, kw or {})

print("=" * 60)
print("  NADF ERP — Install nadf_vendor_onboarding")
print("=" * 60)

# 1. Update module list so Odoo discovers the new module
print("\n[1/3] Updating module list...")
x('ir.module.module', 'update_list', [])
print("  Module list updated.")

# 2. Find the module record
print("\n[2/3] Locating module record...")
mod_ids = x('ir.module.module', 'search', [[['name', '=', 'nadf_vendor_onboarding']]])
if not mod_ids:
    print("  ERROR: Module 'nadf_vendor_onboarding' not found.")
    print("  Make sure /Users/mac/odoo17/custom_addons/nadf_vendor_onboarding/ exists")
    print("  and the addons_path in nadf.conf includes /Users/mac/odoo17/custom_addons/")
    sys.exit(1)

mod_info = x('ir.module.module', 'read', [mod_ids], {'fields': ['name', 'state', 'summary']})
print(f"  Found: {mod_info[0]['name']} (state: {mod_info[0]['state']})")

state = mod_info[0]['state']
if state == 'installed':
    print("\n  Module is already installed. Upgrading instead...")
    x('ir.module.module', 'button_upgrade', [mod_ids])
elif state in ('uninstalled', 'to install'):
    print("\n[3/3] Installing module (this may take 15–30 seconds)...")
    x('ir.module.module', 'button_install', [mod_ids])
else:
    print(f"\n  Module state is '{state}'. Attempting install anyway...")
    x('ir.module.module', 'button_install', [mod_ids])

# 3. Wait for installation to complete
print("  Waiting for installation...")
for i in range(30):
    time.sleep(2)
    result = x('ir.module.module', 'read', [mod_ids], {'fields': ['state']})
    current_state = result[0]['state']
    if current_state == 'installed':
        print(f"  Installed successfully after {(i+1)*2}s")
        break
    print(f"  ... still installing (state: {current_state})")
else:
    print("  WARNING: Timed out waiting for installation. Check Odoo logs.")

# 4. Verify models exist
print("\n[4/4] Verifying installation...")
app_count = x('nadf.vendor.application', 'search_count', [[]])
print(f"  nadf.vendor.application: accessible ({app_count} records)")

# 5. Confirm portal route
print("\n  Portal URL: http://localhost:8071/vendor/register")
print("  Backend:    http://localhost:8071/odoo/vendor-onboarding (approx)")

print("\n" + "=" * 60)
print("  nadf_vendor_onboarding — INSTALLED")
print("=" * 60)
print("""
Next steps:
  1. Set the Claude API key:
     Odoo → Settings → Technical → System Parameters
     Key: nadf.claude.api.key
     Value: sk-ant-api03-…

  2. Assign 'Vendor Manager' group to procurement staff:
     Odoo → Settings → Users → [select user] → Vendor Onboarding

  3. Test portal at: http://localhost:8071/vendor/register
""")
