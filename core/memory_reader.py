"""Typed memory reads against the game process."""
import struct
from core.process_attach import GameProcess


class MemoryReader:
    def __init__(self, proc: GameProcess):
        self.proc = proc

    def read_int32(self, address: int) -> int:
        return struct.unpack("<i", self.proc.read(address, 4))[0]

    def read_float(self, address: int) -> float:
        return struct.unpack("<f", self.proc.read(address, 4))[0]

    def read_qword(self, address: int) -> int:
        return struct.unpack("<Q", self.proc.read(address, 8))[0]

    def resolve_pointer(self, base: int, offsets: list[int]) -> int:
        addr = base
        for off in offsets[:-1]:
            addr = self.read_qword(addr) + off
        return addr + offsets[-1]