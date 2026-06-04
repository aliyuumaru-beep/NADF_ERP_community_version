#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 3 Procurement Configuration
Configures: warehouse, stores, product categories, products,
            purchase approval settings
Run: python3 scripts/phase3_procurement_configuration.py
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

def find(model, domain, field='id'):
    res = x(model, 'search_read', [domain], {'fields': [field], 'limit': 1})
    return res[0][field] if res else None

print("=" * 60)
print("  NADF ERP MVP — Phase 3 Procurement Configuration")
print("=" * 60)

# ── 1. Rename warehouse to NADF ───────────────────────────────────────────────
print("\n[1/5] Configuring warehouse...")

x('stock.warehouse', 'write', [[1], {
    'name': 'NADF Main Warehouse',
    'code': 'NADF',
}])
print("  Renamed: NADF Main Warehouse (code: NADF)")

# Get the parent physical location for NADF
# WH/Stock is ID 8 from inspection — find the parent (WH)
wh_view_loc = x('stock.location', 'search_read',
    [[['complete_name','=','NADF Main Warehouse']]], {'fields': ['id','name','complete_name']})
if not wh_view_loc:
    wh_view_loc = x('stock.location', 'search_read',
        [[['usage','=','view'],['active','=',True]]], {'fields': ['id','name','complete_name']})

# Get the stock location (now renamed)
stock_loc = x('stock.location', 'search_read',
    [[['usage','=','internal'],['active','=',True]]], {'fields': ['id','name','complete_name','location_id']})
print(f"  Stock locations found: {[l['complete_name'] for l in stock_loc]}")

# Find the main warehouse stock location (parent for sub-stores)
main_stock_id = stock_loc[0]['id'] if stock_loc else None
main_stock_parent = stock_loc[0]['location_id'][0] if stock_loc else None

# ── 2. Create Store Locations ─────────────────────────────────────────────────
print("\n[2/5] Creating store locations...")

stores = [
    ('Main Store',         'Main Store — general goods and office supplies'),
    ('ICT Store',          'ICT Store — computers, equipment, accessories'),
    ('Consumables Store',  'Consumables Store — toner, stationery, small items'),
]

store_ids = {}
for store_name, note in stores:
    existing = x('stock.location', 'search', [[['name','=',store_name],['usage','=','internal']]])
    if existing:
        store_ids[store_name] = existing[0]
        print(f"  SKIP (exists): {store_name}")
        continue
    loc_id = x('stock.location', 'create', [{
        'name':        store_name,
        'usage':       'internal',
        'location_id': main_stock_parent or 5,  # parent = WH view location
        'comment':     note,
        'active':      True,
    }])
    store_ids[store_name] = loc_id
    print(f"  Created: {store_name}")

# ── 3. Product Categories ─────────────────────────────────────────────────────
print("\n[3/5] Creating product categories...")

# Get 'All' root category
all_cat = x('product.category', 'search', [[['name','=','All'],['parent_id','=',False]]])
all_cat_id = all_cat[0] if all_cat else 1

def ensure_category(name, parent_id, parent_name=''):
    existing = x('product.category', 'search', [[['name','=',name],['parent_id','=',parent_id]]])
    if existing:
        print(f"  SKIP (exists): {parent_name}/{name}" if parent_name else f"  SKIP: {name}")
        return existing[0]
    cid = x('product.category', 'create', [{'name': name, 'parent_id': parent_id}])
    print(f"  Created: {parent_name}/{name}" if parent_name else f"  Created: {name}")
    return cid

# Top-level NADF procurement categories
office_cat  = ensure_category('Office Supplies', all_cat_id)
ict_cat     = ensure_category('ICT',             all_cat_id)
ops_cat     = ensure_category('Operations',      all_cat_id)
services_cat = ensure_category('Services',       all_cat_id)

# Sub-categories
ensure_category('Stationery',   office_cat, 'Office Supplies')
ensure_category('Printing',     office_cat, 'Office Supplies')
ensure_category('Furniture',    office_cat, 'Office Supplies')
ensure_category('Computers',    ict_cat,    'ICT')
ensure_category('Software',     ict_cat,    'ICT')
ensure_category('Accessories',  ict_cat,    'ICT')
ensure_category('Consultancy',  ops_cat,    'Operations')
ensure_category('Logistics',    ops_cat,    'Operations')
ensure_category('Training',     services_cat, 'Services')
ensure_category('Utilities',    services_cat, 'Services')

# ── 4. Sample Products ────────────────────────────────────────────────────────
print("\n[4/5] Creating sample products...")

# Get COA accounts for stock valuation
stock_val_acc  = find('account.account', [['code','=','110100']])
stock_in_acc   = find('account.account', [['code','=','110200']])
stock_out_acc  = find('account.account', [['code','=','110300']])
expense_acc    = find('account.account', [['code','=','634000']])  # Office & Admin
ict_expense    = find('account.account', [['code','=','611000']])  # Purchase of Equipments

# Get category IDs freshly
ict_cat_id     = find('product.category', [['name','=','ICT']])
office_cat_id  = find('product.category', [['name','=','Office Supplies']])
services_id    = find('product.category', [['name','=','Services']])
stationery_id  = find('product.category', [['name','=','Stationery']])
computers_id   = find('product.category', [['name','=','Computers']])
furniture_id   = find('product.category', [['name','=','Furniture']])

products = [
    {
        'name':           'Laptop (15" Business)',
        'type':           'product',       # storable
        'categ_id':       computers_id or ict_cat_id,
        'uom_id':         1,               # Unit
        'uom_po_id':      1,
        'standard_price': 450000.0,        # ₦450,000
        'purchase_ok':    True,
        'sale_ok':        False,
        'default_code':   'ICT-LAP-001',
        'description_purchase': 'Standard business laptop for office use',
    },
    {
        'name':           'Printer (LaserJet A4)',
        'type':           'product',
        'categ_id':       computers_id or ict_cat_id,
        'uom_id':         1,
        'uom_po_id':      1,
        'standard_price': 185000.0,        # ₦185,000
        'purchase_ok':    True,
        'sale_ok':        False,
        'default_code':   'ICT-PRN-001',
        'description_purchase': 'LaserJet A4 office printer',
    },
    {
        'name':           'Toner Cartridge',
        'type':           'product',
        'categ_id':       stationery_id or office_cat_id,
        'uom_id':         1,
        'uom_po_id':      1,
        'standard_price': 22000.0,         # ₦22,000
        'purchase_ok':    True,
        'sale_ok':        False,
        'default_code':   'OFC-TON-001',
        'description_purchase': 'Compatible toner cartridge',
    },
    {
        'name':           'Office Chair (Executive)',
        'type':           'product',
        'categ_id':       furniture_id or office_cat_id,
        'uom_id':         1,
        'uom_po_id':      1,
        'standard_price': 75000.0,         # ₦75,000
        'purchase_ok':    True,
        'sale_ok':        False,
        'default_code':   'OFC-CHR-001',
        'description_purchase': 'Executive ergonomic office chair',
    },
    {
        'name':           'Internet Subscription (Monthly)',
        'type':           'service',
        'categ_id':       services_id,
        'uom_id':         1,
        'uom_po_id':      1,
        'standard_price': 85000.0,         # ₦85,000/month
        'purchase_ok':    True,
        'sale_ok':        False,
        'default_code':   'ICT-NET-001',
        'description_purchase': 'Monthly internet connectivity subscription',
    },
    {
        'name':           'A4 Paper (Ream)',
        'type':           'product',
        'categ_id':       stationery_id or office_cat_id,
        'uom_id':         1,
        'uom_po_id':      1,
        'standard_price': 4500.0,          # ₦4,500/ream
        'purchase_ok':    True,
        'sale_ok':        False,
        'default_code':   'OFC-PAP-001',
        'description_purchase': 'A4 80gsm photocopier paper — ream of 500 sheets',
    },
    {
        'name':           'Consultancy Services (Per Day)',
        'type':           'service',
        'categ_id':       services_id,
        'uom_id':         1,
        'uom_po_id':      1,
        'standard_price': 150000.0,        # ₦150,000/day
        'purchase_ok':    True,
        'sale_ok':        False,
        'default_code':   'SVC-CON-001',
        'description_purchase': 'Professional consultancy services — daily rate',
    },
]

for p in products:
    existing = x('product.template', 'search', [[['default_code','=',p['default_code']]]])
    if existing:
        print(f"  SKIP (exists): {p['name']}")
        continue
    pid = x('product.template', 'create', [p])
    print(f"  Created: [{p['default_code']}] {p['name']} — ₦{p['standard_price']:,.0f}")

# ── 5. Purchase Approval Settings ─────────────────────────────────────────────
print("\n[5/5] Configuring purchase approval settings...")

# Enable purchase order approval at ₦500,000 threshold (NADF tier-1)
x('res.config.settings', 'create', [{}])
try:
    x('res.config.settings', 'execute', [])
except Exception:
    pass

# Set via ir.config_parameter (direct approach for purchase approval)
# purchase.purchase_order_approval → True
# purchase.purchase_order_approval_min_amount → 500000

def set_param(key, value):
    existing = x('ir.config_parameter', 'search', [[['key','=',key]]])
    if existing:
        x('ir.config_parameter', 'write', [existing, {'value': str(value)}])
    else:
        x('ir.config_parameter', 'create', [{'key': key, 'value': str(value)}])

set_param('purchase.purchase_order_approval', 'True')
set_param('purchase.purchase_order_approval_min_amount', '500000.0')
print("  Purchase order approval: ENABLED")
print("  Approval threshold      : ₦500,000 (Head Procurement level)")
print("  Amounts > ₦500K require Manager approval before PO confirmation")

# Verify
threshold = x('ir.config_parameter', 'search_read',
    [[['key','=','purchase.purchase_order_approval_min_amount']]],
    {'fields': ['value']})
approval  = x('ir.config_parameter', 'search_read',
    [[['key','=','purchase.purchase_order_approval']]],
    {'fields': ['value']})
print(f"\n  Verified approval flag   : {approval[0]['value'] if approval else 'not set'}")
print(f"  Verified threshold value : {threshold[0]['value'] if threshold else 'not set'}")

# ── Summary ───────────────────────────────────────────────────────────────────
total_products  = x('product.template', 'search_count', [[['purchase_ok','=',True]]])
total_cats      = x('product.category', 'search_count', [[]])
total_locations = x('stock.location',   'search_count', [[['usage','=','internal'],['active','=',True]]])

print("\n" + "=" * 60)
print("  Phase 3 Procurement Configuration — COMPLETE")
print("=" * 60)
print(f"  Warehouse       : NADF Main Warehouse (code: NADF)")
print(f"  Store locations : {total_locations} internal locations")
print(f"  Product categories: {total_cats}")
print(f"  Products (purchasable): {total_products}")
print(f"  Purchase approval: ₦500,000 threshold ACTIVE")
print("\n  Next: Phase 4 — HR Configuration")
