"""Entry point for Across the Unknown Trainer."""
import sys
import argparse
from pathlib import Path

from core.engine import TrainerEngine
from core.process_attach import GameProcess
from utils.logger import setup_logger
from config.settings import load_settings


def main() -> int:
    parser = argparse.ArgumentParser(prog="across-the-unknown-trainer")
    parser.add_argument("--process", default="AcrossTheUnknown.exe")
    parser.add_argument("--config", default="config/default.toml")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    log = setup_logger()
    settings = load_settings(Path(args.config))
    log.info("Trainer starting | game={} dry_run={}", args.process, args.dry_run)

    try:
        proc = GameProcess.attach(args.process)
    except GameProcess.NotFound:
        log.error("Game process '{}' not found. Launch the game first.", args.process)
        return 1

    engine = TrainerEngine(proc, settings, dry_run=args.dry_run)
    engine.start()
    return 0


if __name__ == "__main__":
    sys.exit(main())