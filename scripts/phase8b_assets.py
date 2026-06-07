#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 8b: Asset Register Upload
Reads NADF ASSET REGISTER EXCEL.xlsx and loads:
  - maintenance.equipment records (physical tracking — location, category)
  - account.asset.asset records (accounting — depreciation, book value)
Vehicles (rows 48-52) are skipped here — handled by phase8c_fleet.py
"""
import xmlrpc.client, zipfile, xml.etree.ElementTree as ET, sys
from datetime import datetime

URL, DB, PW  = 'http://localhost:8071', 'NADF', 'admin'
EXCEL        = '/Users/mac/Documents/Aliyu/NADF/Digital Transformation/Client Data/NADF ASSET REGISTER EXCEL.xlsx'

uid = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common').authenticate(DB, 'admin', PW, {})
if not uid: print("ERROR: Auth failed"); sys.exit(1)
m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, PW, model, method, args, kw or {})

def get_cat_id(model, name):
    ids = x(model, 'search', [[['name','=',name]]])
    return ids[0] if ids else None

def parse_date(s):
    s = str(s).strip()
    for fmt in ('%d-%m-%Y','%Y-%m-%d','%m/%d/%Y'):
        try:
            return datetime.strptime(s, fmt).strftime('%Y-%m-%d')
        except: pass
    # Excel serial date
    try:
        n = float(s)
        if n > 40000:
            from datetime import timedelta
            return (datetime(1899,12,30) + timedelta(days=n)).strftime('%Y-%m-%d')
    except: pass
    return '2024-01-14'  # default acquisition date

print("=" * 60)
print("  Phase 8b — Asset Register Upload")
print("=" * 60)

# ── Read Excel ─────────────────────────────────────────────────────────────────
with zipfile.ZipFile(EXCEL) as z:
    strings = []
    if 'xl/sharedStrings.xml' in z.namelist():
        ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
        for si in ET.parse(z.open('xl/sharedStrings.xml')).getroot().iter(f'{ns}si'):
            strings.append(''.join(n.text or '' for n in si.iter(f'{ns}t')))
    sf = sorted([n for n in z.namelist() if n.startswith('xl/worksheets/sheet') and n.endswith('.xml')])[0]
    ns = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    raw = []
    for row in ET.parse(z.open(sf)).getroot().iter(f'{ns}row'):
        cells = []
        for c in row.iter(f'{ns}c'):
            t, v = c.get('t',''), c.find(f'{ns}v')
            val = v.text if v is not None else ''
            if t == 's' and val:
                try: val = strings[int(val)]
                except: pass
            cells.append(str(val).strip())
        raw.append(cells)

# Parse: skip title row (0) and header row (1), stop at empty
assets = []
for row in raw[2:]:
    if not row or not row[0].strip() or not row[0].strip().isdigit():
        continue
    sno = int(row[0])
    # Pad row to 7 columns
    while len(row) < 7: row.append('')

    # Some rows have shifted columns (missing location)
    item = row[1].strip()
    qty_raw = row[2].strip()
    date_raw = row[3].strip()
    loc_raw  = row[4].strip()
    price_raw = row[5].strip()
    amount_raw = row[6].strip()

    # Detect shifted columns (date in col4, price in col4, etc.)
    # If loc_raw looks like a number and price_raw is empty → columns shifted left
    def is_num(s):
        try: float(s.replace(',','')); return True
        except: return False

    if is_num(date_raw) and not is_num(loc_raw) and is_num(price_raw):
        pass  # normal
    elif is_num(qty_raw) and is_num(date_raw) and not loc_raw and is_num(price_raw):
        pass  # normal but no location
    elif not is_num(qty_raw) and is_num(date_raw):
        # qty missing, date in col2, location in col3, price in col4
        qty_raw, date_raw, loc_raw, price_raw, amount_raw = '1', qty_raw, date_raw, loc_raw, price_raw

    try: qty = int(float(qty_raw)) if qty_raw else 1
    except: qty = 1
    try: unit_price = float(price_raw.replace(',','')) if price_raw else 0.0
    except: unit_price = 0.0
    try: total = float(amount_raw.replace(',','')) if amount_raw else unit_price * qty
    except: total = unit_price * qty

    acq_date = parse_date(date_raw if date_raw else '46027')
    # Fix known wrong year
    if acq_date == '2014-01-14':
        acq_date = '2024-01-14'

    assets.append({
        'sno': sno, 'item': item, 'qty': qty,
        'date': acq_date, 'location': loc_raw,
        'unit_price': unit_price, 'total': total,
    })

print(f"  {len(assets)} assets parsed from register")

# ── Categorize ────────────────────────────────────────────────────────────────
VEHICLES = {48, 49, 50, 51, 52}  # go to fleet

def categorize(sno, item):
    item_u = item.upper()
    if sno in VEHICLES:                              return 'VEHICLE'
    if any(w in item_u for w in ['LAPTOP','COMPUTER','PRINTER','PROJECTOR',
        'SCREEN','PHOTOCOPIER','SHREDDER','SCANNER','HARD','SWITCH',
        'PABX','CCTV','ACCESS POINT','IP PHONE','MONITOR','TELEVISION',
        'TV','KEYBOARD','DRAGON']):                  return 'IT Equipment'
    if any(w in item_u for w in ['A/C','AIR CON','GENERATOR','STABILIZER',
        'INVERTER','GEN.','GEN SET','GENSET','STANDING A/C']):
                                                     return 'A/C & Power Equipment'
    if any(w in item_u for w in ['FRIDGE','REFRIGERATOR','MICROWAVE','KETTLE',
        'COFFEE','DISPENSER','WATER','CANTEEN','KITCHEN','DUSTBIN',
        'WASTE BIN','STOOL','DININ']):               return 'Office Appliances'
    if any(w in item_u for w in ['TABLE','CHAIR','SOFA','SETTEE','DESK',
        'WORKSTATION','WORK STATION','CABINET','FILING','SHELVE','SHELF',
        'BOOKSHELF','BOOK SHELVE','RUG','CONSOLE','RECEPTIONIST',
        'BOARDROOM','CONFERENCE','SIDE BOARD','HANGER','SUIT']):
                                                     return 'Office Furniture & Fittings'
    return 'Office Appliances'  # fallback

# ── Load maintenance.equipment ────────────────────────────────────────────────
print("\n[1] Loading into maintenance.equipment (physical tracking)...")

maint_cat_ids = {
    'IT Equipment':           get_cat_id('maintenance.equipment.category', 'IT Equipment'),
    'Office Furniture & Fittings': get_cat_id('maintenance.equipment.category', 'Office Furniture & Fittings'),
    'A/C & Power Equipment':  get_cat_id('maintenance.equipment.category', 'A/C & Power Equipment'),
    'Office Appliances':      get_cat_id('maintenance.equipment.category', 'Office Appliances'),
    'ICT Infrastructure':     get_cat_id('maintenance.equipment.category', 'ICT Infrastructure'),
}

maint_created = maint_skipped = 0
for a in assets:
    cat = categorize(a['sno'], a['item'])
    if cat == 'VEHICLE':
        continue

    # For qty > 1, create one equipment record per unit
    count = a['qty'] if a['qty'] and a['qty'] > 0 else 1
    for i in range(1, count + 1):
        name = a['item'] if count == 1 else f"{a['item']} #{i}"
        existing = x('maintenance.equipment', 'search',
                     [[['name','=',name]]], {'limit':1})
        if existing:
            maint_skipped += 1
            continue
        vals = {
            'name':        name,
            'category_id': maint_cat_ids.get(cat),
            'location':    a['location'] or 'NADF Office',
            'cost':        a['unit_price'],
            'assign_date': a['date'],
        }
        x('maintenance.equipment', 'create', [vals])
        maint_created += 1

print(f"  Created: {maint_created}  |  Skipped (exists): {maint_skipped}")

# ── Load account.asset.asset (accounting / depreciation) ─────────────────────
print("\n[2] Loading into account.asset.asset (accounting)...")

acct_cat_ids = {
    'IT Equipment':           get_cat_id('account.asset.category', 'IT Equipment'),
    'Office Furniture & Fittings': get_cat_id('account.asset.category', 'Office Furniture & Fittings'),
    'A/C & Power Equipment':  get_cat_id('account.asset.category', 'A/C & Power Equipment'),
    'Office Appliances':      get_cat_id('account.asset.category', 'Office Appliances'),
}

acct_created = acct_skipped = acct_zero = 0
for a in assets:
    cat = categorize(a['sno'], a['item'])
    if cat == 'VEHICLE':
        continue
    if a['total'] <= 0:
        acct_zero += 1
        continue   # no value — skip accounting record

    cat_id = acct_cat_ids.get(cat)
    if not cat_id:
        continue

    name = a['item']
    existing = x('account.asset.asset', 'search',
                 [[['name','=',name]]], {'limit':1})
    if existing:
        acct_skipped += 1
        continue

    x('account.asset.asset', 'create', [{
        'name':              name,
        'category_id':       cat_id,
        'date':              a['date'],
        'value':             a['total'],
        'method':            'linear',
        'method_time':       'number',
        'method_period':     1,
        'type':              'purchase',
    }])
    acct_created += 1

print(f"  Created: {acct_created}  |  Skipped (exists): {acct_skipped}  |  Zero-value skipped: {acct_zero}")

# ── Summary ───────────────────────────────────────────────────────────────────
total_eq   = x('maintenance.equipment', 'search_count', [[]])
total_asset = x('account.asset.asset', 'search_count', [[]])
print(f"\n  Total equipment records:  {total_eq}")
print(f"  Total accounting assets:  {total_asset}")
print("  Vehicles → handled by phase8c_fleet.py")
