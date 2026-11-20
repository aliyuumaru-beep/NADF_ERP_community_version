"""
Unit tests for scripts/pre_review_check.py.

Imports ODOO16_PATTERNS and SECRET_PATTERN directly from the production module
so tests cover the actual constants, not copies.

Run with:  python3 -m pytest scripts/tests/ -v
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / 'scripts'))

import pre_review_check as prc  # noqa: E402


# ── Odoo 16→17 compat pattern tests ─────────────────────────────────────────

@pytest.mark.parametrize('bad_line,expected_match', [
    ("<field name='inherit_id' ref='portal.portal_my_home_entry'/>", 'portal.portal_my_home_entry'),
    ('    <tree string="Contracts">', '<tree'),
    ("        xpath = '//tree[@string]'", '//tree'),
    ('    res = fields.Boolean.convert_to_cache(self, v)', 'convert_to_cache'),
    ('import openerp', 'openerp'),
])
def test_odoo16_pattern_matches_bad_line(bad_line, expected_match):
    hits = [msg for regex, msg in prc.ODOO16_PATTERNS if regex.search(bad_line)]
    assert hits, f"Expected a pattern to match {bad_line!r} (looking for {expected_match!r}); none did"


@pytest.mark.parametrize('clean_line', [
    "<field name='inherit_id' ref='portal.portal_docs_entry'/>",
    '    <list string="Contracts">',
    "        xpath = '//list[@string]'",
    '    res = super().create(vals)',
    'from odoo import models',
])
def test_odoo16_pattern_does_not_match_clean_line(clean_line):
    hits = [msg for regex, msg in prc.ODOO16_PATTERNS if regex.search(clean_line)]
    assert not hits, f"Pattern(s) incorrectly matched clean line {clean_line!r}: {hits}"


# ── Secret pattern tests ─────────────────────────────────────────────────────

def test_secret_pattern_catches_hardcoded_password():
    assert prc.SECRET_PATTERN.search("password = 'hunter2x'")


def test_secret_pattern_ignores_change_me():
    assert not prc.SECRET_PATTERN.search("admin_passwd = CHANGE_ME")


def test_secret_pattern_ignores_short_value():
    assert not prc.SECRET_PATTERN.search("password = 'x'")


# ── XML well-formedness ──────────────────────────────────────────────────────

def test_valid_xml_passes(tmp_path):
    p = tmp_path / 'good.xml'
    p.write_text('<odoo><data/></odoo>')
    ET.parse(str(p))  # should not raise


def test_malformed_xml_fails(tmp_path):
    p = tmp_path / 'bad.xml'
    p.write_text('<odoo><data></odoo>')
    with pytest.raises(ET.ParseError):
        ET.parse(str(p))


# ── Manifest validation ──────────────────────────────────────────────────────

def test_valid_manifest_passes(tmp_path):
    import ast
    p = tmp_path / '__manifest__.py'
    p.write_text("{'name': 'Test', 'depends': ['base'], 'license': 'LGPL-3'}")
    allowed = {'LGPL-3', 'AGPL-3', 'GPL-3', 'OPL-1', 'Other OSI approved licence'}
    tree = ast.parse(p.read_text())
    d = next((ast.literal_eval(n) for n in ast.walk(tree) if isinstance(n, ast.Dict)), None)
    assert d is not None
    assert d['license'] in allowed


def test_manifest_missing_license_flagged(tmp_path):
    import ast
    p = tmp_path / '__manifest__.py'
    p.write_text("{'name': 'Test', 'depends': ['base']}")
    tree = ast.parse(p.read_text())
    d = next((ast.literal_eval(n) for n in ast.walk(tree) if isinstance(n, ast.Dict)), None)
    missing = {'name', 'depends', 'license'} - set(d)
    assert 'license' in missing
