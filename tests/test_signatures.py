"""Smoke tests - ensure every signature file parses."""
import json
from pathlib import Path

SIG_DIR = Path(__file__).resolve().parent.parent / "signatures"


def test_all_json_signatures_parse():
    files = [p for p in SIG_DIR.glob("*.json")]
    assert files, "no signature files found"
    for p in files:
        data = json.loads(p.read_text(encoding="utf-8"))
        assert "build" in data
        assert "base" in data or "crew_array_base" in data


def test_version_present():
    v = (SIG_DIR / "version.txt").read_text(encoding="utf-8").strip()
    assert v.startswith("v")