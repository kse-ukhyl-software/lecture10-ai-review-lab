"""Sanity tests so students can confirm the app runs before reviewing it."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import app  # noqa: E402


def test_app_imports():
    assert app is not None


def test_export_route_registered():
    rules = {r.rule for r in app.url_map.iter_rules()}
    assert "/admin/export" in rules
    assert "/login" in rules
    assert "/orders/<order_id>" in rules
