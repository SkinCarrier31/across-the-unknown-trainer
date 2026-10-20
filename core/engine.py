"""Trainer engine - owns the tick loop and dispatches to handlers."""
import time
from typing import Dict, List

from core.process_attach import GameProcess
from core.memory_reader import MemoryReader
from core.memory_writer import MemoryWriter
from handlers.base_handler import BaseHandler
from handlers import HANDLER_REGISTRY
from utils.logger import get_logger

log = get_logger(__name__)


class TrainerEngine:
    def __init__(self, proc: GameProcess, settings, dry_run: bool = False):
        self.proc = proc
        self.settings = settings
        self.dry_run = dry_run
        self.reader = MemoryReader(proc)
        self.writer = MemoryWriter(proc, dry_run=dry_run)
        self.handlers: List[BaseHandler] = []
        self._running = False

    def _load_handlers(self) -> None:
        for name, cls in HANDLER_REGISTRY.items():
            enabled = self.settings.handlers.get(name, True)
            if not enabled:
                log.info("Handler '{}' disabled in config", name)
                continue
            self.handlers.append(cls(self.reader, self.writer, self.settings))
            log.info("Loaded handler: {}", name)

    def start(self) -> None:
        self._load_handlers()
        self._running = True
        log.info("Engine online with {} handlers", len(self.handlers))
        tick = 1.0 / max(1, self.settings.tick_hz)
        try:
            while self._running:
                for h in self.handlers:
                    h.tick()
                time.sleep(tick)
        except KeyboardInterrupt:
            log.info("Interrupt received, shutting down")
        finally:
            self.stop()

    def stop(self) -> None:
        self._running = False
        for h in self.handlers:
            h.on_shutdown()