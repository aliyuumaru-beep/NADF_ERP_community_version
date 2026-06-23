#!/usr/bin/env python3
"""NADF ERP CI validator — Gate B build verification.

Pure-stdlib checks (no third-party deps) so it runs identically locally and on
a GitHub Actions ubuntu runner:

  1. Manifest parse  — every custom_addons/*/__manifest__.py is a valid dict with
     required keys (name, depends, license) and license is not Enterprise.
  2. Python compile  — every module .py compiles (py_compile).
  3. XML well-formed — every module .xml parses (xml.etree).

Exit 0 = all pass; exit 1 = any failure (fails the CI job).
"""
import ast
import glob
import os
import py_compile
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADDONS = os.path.join(ROOT, "custom_addons")
ALLOWED_LICENSES = {"LGPL-3", "AGPL-3", "GPL-3", "OPL-1", "Other OSI approved licence"}

failures = []


def check_manifests():
    for mf in sorted(glob.glob(os.path.join(ADDONS, "*", "__manifest__.py"))):
        try:
            tree = ast.parse(open(mf, encoding="utf-8").read())
            d = next((ast.literal_eval(n) for n in ast.walk(tree) if isinstance(n, ast.Dict)), None)
            if not d:
                raise ValueError("no manifest dict found")
            missing = {"name", "depends", "license"} - set(d)
            if missing:
                raise ValueError(f"missing keys: {sorted(missing)}")
            if d["license"] not in ALLOWED_LICENSES:
                raise ValueError(f"non-permitted license {d['license']!r}")
            print(f"  OK manifest: {os.path.relpath(mf, ROOT)} ({d['license']})")
        except Exception as e:  # noqa: BLE001
            failures.append(f"manifest {os.path.relpath(mf, ROOT)}: {e}")


def check_python():
    for py in glob.glob(os.path.join(ADDONS, "**", "*.py"), recursive=True):
        if "__pycache__" in py:
            continue
        try:
            py_compile.compile(py, doraise=True)
        except py_compile.PyCompileError as e:
            failures.append(f"py_compile {os.path.relpath(py, ROOT)}: {e}")
    print("  OK python: all module .py compiled")


def check_xml():
    n = 0
    for x in glob.glob(os.path.join(ADDONS, "**", "*.xml"), recursive=True):
        if "__pycache__" in x:
            continue
        n += 1
        try:
            ET.parse(x)
        except ET.ParseError as e:
            failures.append(f"xml {os.path.relpath(x, ROOT)}: {e}")
    print(f"  OK xml: {n} files well-formed")


if __name__ == "__main__":
    print("NADF CI validation")
    check_manifests()
    check_python()
    check_xml()
    if failures:
        print("\nFAILURES:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print("\nAll CI checks passed.")
