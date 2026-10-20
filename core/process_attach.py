"""Attach to the AcrossTheUnknown.exe process and expose a handle."""
from dataclasses import dataclass
from typing import Optional
import pymem

from utils.logger import get_logger

log = get_logger(__name__)


class GameProcess:
    class NotFound(Exception):
        pass

    def __init__(self, handle: pymem.Pymem, base_address: int, pid: int):
        self.handle = handle
        self.base = base_address
        self.pid = pid

    @classmethod
    def attach(cls, name: str) -> "GameProcess":
        try:
            pm = pymem.Pymem(name)
        except pymem.exception.ProcessNotFound as exc:
            raise cls.NotFound(name) from exc
        base = pm.base_address
        log.info("Attached to {} pid={} base=0x{:X}", name, pm.process_id, base)
        return cls(pm, base, pm.process_id)

    def read(self, address: int, size: int) -> bytes:
        return self.handle.read_bytes(address, size)

    def write(self, address: int, data: bytes) -> None:
        self.handle.write_bytes(address, data)

    def module_base(self, module: str) -> Optional[int]:
        try:
            mod = self.handle.read_module(module)
            return mod.lpBaseOfDll
        except Exception:
            return None