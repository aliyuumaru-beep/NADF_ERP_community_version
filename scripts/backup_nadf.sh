#!/usr/bin/env bash
# NADF database + filestore backup — Software Factory POD-NADF
# Produces: <BACKUP_ROOT>/nadf_<TS>/{<DB>_<TS>.dump (pg_dump -F c), filestore_<DB>_<TS>.tar.gz, MANIFEST.txt, SHA256SUMS.txt}
# Read-safe: does not modify the live database.
set -euo pipefail

DB="${NADF_DB:-NADF}"
PGUSER="${PGUSER:-odoo}"
PGHOST="${PGHOST:-localhost}"
export PGPASSWORD="${PGPASSWORD:-odoo}"
FILESTORE="${NADF_FILESTORE:-$HOME/Library/Application Support/Odoo/filestore/$DB}"
BACKUP_ROOT="${NADF_BACKUP_ROOT:-$HOME/odoo_backups}"
TS="$(date +%Y%m%d_%H%M%S)"
DEST="$BACKUP_ROOT/nadf_${TS}"

mkdir -p "$DEST"
echo "[backup] db=$DB host=$PGHOST dest=$DEST"

# 1. Database dump (custom format → pg_restore compatible)
pg_dump -U "$PGUSER" -h "$PGHOST" -F c -f "$DEST/${DB}_${TS}.dump" "$DB"

# 2. Filestore archive (if present)
if [ -d "$FILESTORE" ]; then
  tar -czf "$DEST/filestore_${DB}_${TS}.tar.gz" -C "$(dirname "$FILESTORE")" "$(basename "$FILESTORE")"
else
  echo "[backup] WARNING: filestore not found at $FILESTORE"
fi

# 3. Manifest + checksums
{
  echo "NADF backup manifest"
  echo "timestamp:  $TS"
  echo "database:   $DB"
  echo "db_dump:    ${DB}_${TS}.dump"
  echo "filestore:  filestore_${DB}_${TS}.tar.gz"
  echo "pg_dump:    $(pg_dump --version)"
} > "$DEST/MANIFEST.txt"
( cd "$DEST" && shasum -a 256 ./*.dump ./*.tar.gz > SHA256SUMS.txt 2>/dev/null || true )

echo "[backup] complete: $DEST"
echo "$DEST"
