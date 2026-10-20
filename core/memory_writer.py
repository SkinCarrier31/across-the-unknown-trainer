"""Guarded memory writes - refuses to write unless signature matches."""
import struct
from core.process_attach import GameProcess
from utils.logger import get_logger

log = get_logger(__name__)


class MemoryWriter:
    def __init__(self, proc: GameProcess, dry_run: bool = False):
        self.proc = proc
        self.dry_run = dry_run
        self._guard: dict[int, bytes] = {}

    def guard(self, address: int, expected: bytes) -> None:
        self._guard[address] = expected

    def write_int32(self, address: int, value: int) -> None:
        if address in self._guard:
            current = self.proc.read(address, len(self._guard[address]))
            if current != self._guard[address]:
                log.warning("Guard mismatch at 0x{:X}; skipping write", address)
                return
        if self.dry_run:
            log.debug("[dry-run] write int32 @0x{:X} = {}", address, value)
            return
        self.proc.write(address, struct.pack("<i", value))

    def write_float(self, address: int, value: float) -> None:
        if self.dry_run:
            log.debug("[dry-run] write float @0x{:X} = {}", address, value)
            return
        self.proc.write(address, struct.pack("<f", value))