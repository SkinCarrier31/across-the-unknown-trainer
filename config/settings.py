"""Config loader - pydantic models + TOML read."""
from pathlib import Path
import tomllib
from pydantic import BaseModel, Field


class TrainerSettings(BaseModel):
    tick_hz: int = 20
    resource_target: int = 99999
    crew_pinned_stats: dict[int, int] = Field(default_factory=dict)
    handlers: dict[str, bool] = Field(default_factory=dict)
    overlay_alpha: int = 200


def load_settings(path: Path) -> TrainerSettings:
    if not path.exists():
        return TrainerSettings()
    with path.open("rb") as fh:
        raw = tomllib.load(fh)
    return TrainerSettings(**raw.get("trainer", {}))