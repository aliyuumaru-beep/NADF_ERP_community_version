#!/usr/bin/env python3
"""
NADF ERP MVP — Phase 8c: Fleet Vehicles
Loads 5 NADF vehicles from the asset register into fleet.vehicle.
Creates Toyota brand and specific models first.
"""
import xmlrpc.client, sys

URL, DB, PW = 'http://localhost:8071', 'NADF', 'admin'
uid = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/common').authenticate(DB, 'admin', PW, {})
if not uid: print("ERROR: Auth failed"); sys.exit(1)
m = xmlrpc.client.ServerProxy(f'{URL}/xmlrpc/2/object')

def x(model, method, args, kw=None):
    return m.execute_kw(DB, uid, PW, model, method, args, kw or {})

def find_or_create(model, domain, vals):
    ids = x(model, 'search', [domain])
    return (ids[0], False) if ids else (x(model, 'create', [vals]), True)

print("=" * 60)
print("  Phase 8c — Fleet Vehicles")
print("=" * 60)

# ── Brand ──────────────────────────────────────────────────────────────────────
toyota_id, _ = find_or_create('fleet.vehicle.model.brand',
    [['name','=','Toyota']], {'name': 'Toyota'})
print(f"\n  Toyota brand id={toyota_id}")

# ── Models ────────────────────────────────────────────────────────────────────
def get_model(name):
    mid, created = find_or_create('fleet.vehicle.model',
        [['name','=',name],['brand_id','=',toyota_id]],
        {'name': name, 'brand_id': toyota_id})
    print(f"  {'Created' if created else 'Exists'} model: Toyota {name} (id={mid})")
    return mid

lc_id   = get_model('Land Cruiser')
cor_id  = get_model('Corolla')
hil_id  = get_model('Hilux')
hia_id  = get_model('Hiace')

# ── Vehicles ──────────────────────────────────────────────────────────────────
# (item, model_id, acquisition_date, cost, seats, fuel_type, location, notes)
VEHICLES = [
    ('Toyota Land Cruiser (2023) SUV',    lc_id,  '2024-01-14', 255325000, 7,  'gasoline', 'Office of the ES',  'Executive vehicle'),
    ('Toyota Corolla (2023) Sedan',       cor_id, '2024-01-14', 41280000,  5,  'gasoline', 'Office of the ES',  'Official sedan'),
    ('Toyota Hilux DC (Black) 2023',      hil_id, '2024-01-14', 57712500,  5,  'diesel',   'Project Vehicle',   'Project pickup'),
    ('Toyota Hilux DC (White) 2023',      hil_id, '2024-01-14', 65830000,  5,  'diesel',   'Project Vehicle',   'Project pickup'),
    ('Toyota Hiace Bus 2023',             hia_id, '2024-01-14', 85125000,  14, 'diesel',   'Pool Vehicle',      'Pool bus'),
]

print("\n  Loading vehicles...")
v_created = v_skipped = 0
for name, model_id, acq_date, cost, seats, fuel, location, note in VEHICLES:
    existing = x('fleet.vehicle', 'search', [[['name','=',name]]])
    if existing:
        print(f"  EXISTS : {name}")
        v_skipped += 1
        continue
    vid = x('fleet.vehicle', 'create', [{
        'name':             name,
        'model_id':         model_id,
        'acquisition_date': acq_date,
        'seats':            seats,
        'fuel_type':        fuel,
    }])
    # Log a note in chatter
    x('fleet.vehicle', 'message_post', [[vid]], {
        'body': f'Asset Register value: ₦{cost:,.0f} | Location: {location} | {note}'
    })
    print(f"  Created: {name} (id={vid}) ₦{cost:,.0f}")
    v_created += 1

print(f"\n  Vehicles created: {v_created}  |  Skipped: {v_skipped}")
total = x('fleet.vehicle', 'search_count', [[]])
print(f"  Total fleet vehicles: {total}")
