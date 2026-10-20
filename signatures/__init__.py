"""Signature loader - reads JSON offset maps per game build."""
import json
from pathlib import Path

_CACHE: dict[str, dict] = {}
_ROOT = Path(__file__).parent


def load(name: str) -> dict:
    if name in _CACHE:
        return _CACHE[name]
    path = _ROOT / f"{name}.json"
    if not path.exists():
        raise FileNotFoundError(f"Signature '{name}' missing at {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    _CACHE[name] = data
    return data


def game_version() -> str:
    return (_ROOT / "version.txt").read_text(encoding="utf-8").strip()