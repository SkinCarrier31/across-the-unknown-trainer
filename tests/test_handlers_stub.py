"""Stub test - handlers can be imported without a live game."""
from handlers import HANDLER_REGISTRY


def test_registry_not_empty():
    assert len(HANDLER_REGISTRY) >= 3


def test_registry_keys_unique():
    keys = list(HANDLER_REGISTRY.keys())
    assert len(keys) == len(set(keys))
</final>