"""Crew stat editor - pins Janeway/Chakotay/Tuvok skill values."""
from handlers.base_handler import BaseHandler
from signatures import loader


class CrewStatHandler(BaseHandler):
    name = "crew_stats"

    def __init__(self, reader, writer, settings):
        super().__init__(reader, writer, settings)
        self.offsets = loader.load("crew_stats")
        self._pinned = self.settings.crew_pinned_stats

    def tick(self) -> None:
        if not self.enabled or not self._pinned:
            return
        base = self.offsets["crew_array_base"]
        for idx, value in self._pinned.items():
            addr = self.reader.resolve_pointer(
                base, [idx * self.offsets["stride"], self.offsets["stat_off"]]
            )
            self.writer.write_int32(addr, value)