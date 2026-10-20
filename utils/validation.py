"""Sanity checks on offsets before we trust them."""
def plausible_pointer(addr: int) -> bool:
    return 0x10000 <= addr <= 0x7FFFFFFFFFFF


def plausible_hull(value: float) -> bool:
    return 0.0 <= value <= 100000.0


def clamp(value: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, value))