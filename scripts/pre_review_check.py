#!/usr/bin/env python3
"""
Pre-review static checker for NADF ERP custom addons.

Run before `gov review` to catch Odoo 16→17 incompatibilities and common issues
before they consume expensive G1/G2/G3 review cycles.

Exit code 0 = clean; 1 = issues found.

Usage:
    python3 scripts/pre_review_check.py
    make pre-review
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ADDONS = ROOT / 'custom_addons'
ISSUES = []

ODOO16_PATTERNS = [
    (re.compile(r'portal\.portal_my_home_entry'), 'portal.portal_my_home_entry does not exist in Odoo 17 — use portal.portal_docs_entry'),
    (re.compile(r'inherit_id\s*=\s*["\']portal\.portal_my_home_entry["\']'), 'inherit_id="portal.portal_my_home_entry" is non-existent in Odoo 17 — use portal.portal_docs_entry'),
    (re.compile(r'<tree[\s>]'), 'Odoo 17 uses <list> not <tree> for list views'),
    (re.compile(r'//tree\b'), 'XPath //tree targets list views — use //list in Odoo 17'),
    (re.compile(r'fields\.Boolean\.convert_to_cache'), 'fields.Boolean.convert_to_cache was removed in Odoo 17'),
    (re.compile(r'\bimport openerp\b|from openerp\b'), 'openerp import is Odoo 8/9 era — not valid in Odoo 17'),
]


def issue(filepath, line_no, msg):
    ISSUES.append(f'  [{filepath.relative_to(ROOT)}:{line_no}] {msg}')


def _changed_files():
    """Return git-diff-scoped file set; falls back to full custom_addons scan."""
    cmds = [
        ['git', 'diff', '--name-only', 'main...HEAD'],
        ['git', 'diff', '--cached', '--name-only'],
        ['git', 'diff', '--name-only', 'HEAD'],
    ]
    paths = set()
    git_available = False
    for cmd in cmds:
        try:
            out = subprocess.check_output(cmd, cwd=ROOT, text=True, stderr=subprocess.DEVNULL)
            git_available = True
            paths.update(ROOT / p.strip() for p in out.splitlines() if p.strip())
        except Exception:
            pass
    if git_available and paths:
        return paths
    result = set()
    if ADDONS.exists():
        result.update(ADDONS.rglob('*.py'))
        result.update(ADDONS.rglob('*.xml'))
    return result


# ── 1. Manifest validation ───────────────────────────────────────────────────
def check_manifests():
    import ast
    allowed_licenses = {'LGPL-3', 'AGPL-3', 'GPL-3', 'OPL-1', 'Other OSI approved licence'}
    for mf in sorted(ADDONS.glob('*/__manifest__.py')):
        try:
            tree = ast.parse(mf.read_text(encoding='utf-8'))
            d = next((ast.literal_eval(n) for n in ast.walk(tree) if isinstance(n, ast.Dict)), None)
            if not d:
                raise ValueError('no manifest dict found')
            missing = {'name', 'depends', 'license'} - set(d)
            if missing:
                raise ValueError(f'missing keys: {sorted(missing)}')
            if d['license'] not in allowed_licenses:
                raise ValueError(f'non-permitted license {d["license"]!r}')
        except Exception as e:
            issue(mf, 1, f'Manifest error: {e}')


# ── 2. XML well-formedness ───────────────────────────────────────────────────
def check_xml():
    import xml.etree.ElementTree as ET
    for xml_path in ADDONS.rglob('*.xml'):
        try:
            ET.parse(str(xml_path))
        except ET.ParseError as e:
            issue(xml_path, 1, f'XML parse error: {e}')


# ── 3. No hardcoded passwords ────────────────────────────────────────────────
SECRET_PATTERN = re.compile(
    r'(password\s*=\s*["\'][^"\']{6,}["\']'
    r'|admin_passwd\s*=\s*(?!CHANGE_ME)[^\s#]{6,})',
    re.IGNORECASE,
)


def check_no_secrets():
    try:
        ignored = set(subprocess.check_output(
            ['git', 'ls-files', '--ignored', '--exclude-standard', '-o'],
            cwd=ROOT, text=True,
        ).splitlines())
    except Exception:
        ignored = set()
    skip_dirs = {'.git', '__pycache__', 'specs', 'backups', 'docs', 'tests'}
    for path in ROOT.rglob('*'):
        if any(d in path.parts for d in skip_dirs):
            continue
        if str(path.relative_to(ROOT)) in ignored:
            continue
        if path.suffix not in ('.py', '.xml', '.json', '.conf', '.cfg', '.env'):
            continue
        if path.name.endswith('.example'):
            continue
        try:
            text = path.read_text(errors='ignore')
        except (OSError, IsADirectoryError):
            continue
        for m in SECRET_PATTERN.finditer(text):
            lineno = text[:m.start()].count('\n') + 1
            issue(path, lineno, f'Possible hardcoded secret: {m.group()[:60]!r}')


# ── 4. Odoo 16→17 compat patterns (diff-scoped) ─────────────────────────────
def check_odoo17_compat():
    self_path = Path(__file__).resolve()
    for path in _changed_files():
        if path.suffix not in ('.py', '.xml'):
            continue
        if not path.exists():
            continue
        if path.resolve() == self_path:
            continue
        try:
            lines = path.read_text(errors='ignore').splitlines()
        except (OSError, IsADirectoryError):
            continue
        for i, line in enumerate(lines, 1):
            for pattern, msg in ODOO16_PATTERNS:
                if pattern.search(line):
                    issue(path, i, f'Odoo 17 compat: {msg}')


# ── Run all checks ───────────────────────────────────────────────────────────
check_manifests()
check_xml()
check_no_secrets()
check_odoo17_compat()

if ISSUES:
    print(f'Pre-review: {len(ISSUES)} issue(s) found — fix before gov review:\n')
    for msg in ISSUES:
        print(msg)
    sys.exit(1)
else:
    print('Pre-review: clean. Safe to run gov review.')
    sys.exit(0)
