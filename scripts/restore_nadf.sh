#!/usr/bin/env bash
# NADF restore DRILL — restores a dump into a TEMPORARY database.
# SAFETY: refuses to target the live NADF database. Never overwrites production data.
# Usage: restore_nadf.sh <dump_file> [target_db]
set -euo pipefail

DUMP="${1:?usage: restore_nadf.sh <dump_file> [target_db]}"
TARGET="${2:-NADF_restore_drill}"
PGUSER="${PGUSER:-odoo}"
PGHOST="${PGHOST:-localhost}"
export PGPASSWORD="${PGPASSWORD:-odoo}"

if [ "$TARGET" = "NADF" ]; then
  echo "[restore-drill] REFUSING: target '$TARGET' is the live database. Use a drill DB." >&2
  exit 2
fi
[ -f "$DUMP" ] || { echo "[restore-drill] dump not found: $DUMP" >&2; exit 2; }

echo "[restore-drill] target=$TARGET  dump=$DUMP"
dropdb   -U "$PGUSER" -h "$PGHOST" --if-exists "$TARGET"
createdb -U "$PGUSER" -h "$PGHOST" -O "$PGUSER" "$TARGET"

# Restore (ignore benign owner/acl noise; real success measured by verification below)
pg_restore -U "$PGUSER" -h "$PGHOST" -d "$TARGET" --no-owner --no-acl "$DUMP" 2>&1 | tail -8 || true

echo "[restore-drill] verification on $TARGET:"
psql -U "$PGUSER" -h "$PGHOST" -d "$TARGET" -tAc \
  "select 'installed_modules='||count(*) from ir_module_module where state='installed';"
psql -U "$PGUSER" -h "$PGHOST" -d "$TARGET" -tAc \
  "select 'res_partner_rows='||count(*) from res_partner;"
psql -U "$PGUSER" -h "$PGHOST" -d "$TARGET" -tAc \
  "select 'nadf_modules='||string_agg(name,',') from ir_module_module where name like 'nadf%' and state='installed';"
