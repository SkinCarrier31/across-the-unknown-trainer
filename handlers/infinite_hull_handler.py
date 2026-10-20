"""Infinite hull - keeps the Voyager's hull integrity pinned."""
from handlers.base_handler import BaseHandler
from signatures import loader


class InfiniteHullHandler(BaseHandler):
    name = "infinite_hull"

    def __init__(self, reader, writer, settings):
        super().__init__(reader, writer, settings)
        self.offsets = loader.load("infinite_hull")

    def tick(self) -> None:
        if not self.enabled:
            return
        addr = self.reader.resolve_pointer(
            self.offsets["base"], self.offsets["chain"]
        )
        hull = self.reader.read_float(addr)
        max_hull = 1000.0
        if hull < max_hull:
            self.writer.write_float(addr, max_hull)