"""Loguru wrapper with rotating file sink."""
import sys
from pathlib import Path
from loguru import logger

_LOGGED = False


def setup_logger() -> "logger.__class__":
    global _LOGGED
    if _LOGGED:
        return logger
    log_dir = Path.home() / "AppData" / "Roaming" / "AcrossTheUnknownTrainer"
    log_dir.mkdir(parents=True, exist_ok=True)
    logger.remove()
    logger.add(sys.stderr, level="INFO", colorize=True)
    logger.add(
        log_dir / "trainer.log",
        rotation="5 MB",
        retention=3,
        level="DEBUG",
    )
    _LOGGED = True
    return logger


def get_logger(name: str):
    setup_logger()
    return logger.bind(module=name)