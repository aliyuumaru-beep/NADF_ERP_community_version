"""
Unit tests for scripts/pre_review_check.py.

Run with:  python3 -m pytest scripts/tests/ -v
"""
import re
import sys
import tempfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(REPO_ROOT / 'scripts'))


# ── Helpers ──────────────────────────────────────────────────────────────────

def _file(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content)
    return p


# ── Odoo 16→17 compat pattern tests ─────────────────────────────────────────

ODOO16_PATTERNS = [
    (re.compile(r'portal\.portal_my_home_entry'), 'portal.portal_my_home_entry does not exist in Odoo 17'),
    (re.compile(r'<tree[\s>]'), 'Odoo 17 uses <list> not <tree>'),
    (re.compile(r'//tree\b'), 'XPath //tree targets list views'),
    (re.compile(r'fields\.Boolean\.convert_to_cache'), 'fields.Boolean.convert_to_cache was removed'),
    (re.compile(r'\bimport openerp\b|from openerp\b'), 'openerp import is not valid in Odoo 17'),
]


@pytest.mark.parametrize('pattern,bad_line', [
    (ODOO16_PATTERNS[0], "<field name='inherit_id' ref='portal.portal_my_home_entry'/>"),
    (ODOO16_PATTERNS[1], '    <tree string="Contracts">'),
    (ODOO16_PATTERNS[2], "        xpath = '//tree[@string]'"),
    (ODOO16_PATTERNS[3], '    res = fields.Boolean.convert_to_cache(self, value)'),
    (ODOO16_PATTERNS[4], 'import openerp'),
])
def test_odoo16_pattern_matches_bad_line(pattern, bad_line):
    regex, _ = pattern
    assert regex.search(bad_line), f"Pattern should match: {bad_line!r}"


@pytest.mark.parametrize('pattern,clean_line', [
    (ODOO16_PATTERNS[0], "<field name='inherit_id' ref='portal.portal_docs_entry'/>"),
    (ODOO16_PATTERNS[1], '    <list string="Contracts">'),
    (ODOO16_PATTERNS[2], "        xpath = '//list[@string]'"),
    (ODOO16_PATTERNS[3], '    res = fields.Boolean._convert_to_cache(self, value)'),
    (ODOO16_PATTERNS[4], 'from odoo import models'),
])
def test_odoo16_pattern_does_not_match_clean_line(pattern, clean_line):
    regex, _ = pattern
    assert not regex.search(clean_line), f"Pattern should NOT match: {clean_line!r}"


# ── Secret pattern test ──────────────────────────────────────────────────────

SECRET_PATTERN = re.compile(
    r'(password\s*=\s*["\'][^"\']{6,}["\']'
    r'|admin_passwd\s*=\s*(?!CHANGE_ME)[^\s#]{6,})',
    re.IGNORECASE,
)


def test_secret_pattern_catches_hardcoded_password():
    assert SECRET_PATTERN.search("password = 'secret123'")


def test_secret_pattern_ignores_change_me():
    assert not SECRET_PATTERN.search("admin_passwd = CHANGE_ME")


def test_secret_pattern_ignores_short_value():
    assert not SECRET_PATTERN.search("password = 'x'")


# ── XML well-formedness ──────────────────────────────────────────────────────

def test_valid_xml_passes(tmp_path):
    xml_file = _file(tmp_path, 'good.xml', '<odoo><data/></odoo>')
    import xml.etree.ElementTree as ET
    ET.parse(str(xml_file))  # should not raise


def test_malformed_xml_fails(tmp_path):
    import xml.etree.ElementTree as ET
    xml_file = _file(tmp_path, 'bad.xml', '<odoo><data></odoo>')
    with pytest.raises(ET.ParseError):
        ET.parse(str(xml_file))


# ── Manifest validation ──────────────────────────────────────────────────────

def test_valid_manifest_passes(tmp_path):
    mf = _file(tmp_path, '__manifest__.py', "{'name': 'Test', 'depends': ['base'], 'license': 'LGPL-3'}")
    import ast
    allowed_licenses = {'LGPL-3', 'AGPL-3', 'GPL-3', 'OPL-1', 'Other OSI approved licence'}
    tree = ast.parse(mf.read_text())
    d = next((ast.literal_eval(n) for n in ast.walk(tree) if isinstance(n, ast.Dict)), None)
    assert d is not None
    assert d['license'] in allowed_licenses


def test_manifest_missing_license_flagged(tmp_path):
    mf = _file(tmp_path, '__manifest__.py', "{'name': 'Test', 'depends': ['base']}")
    import ast
    tree = ast.parse(mf.read_text())
    d = next((ast.literal_eval(n) for n in ast.walk(tree) if isinstance(n, ast.Dict)), None)
    missing = {'name', 'depends', 'license'} - set(d)
    assert 'license' in missing
