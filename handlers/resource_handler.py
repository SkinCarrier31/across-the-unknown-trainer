"""Resource handler - latinum, dilithium, replicator rations."""
from handlers.base_handler import BaseHandler
from signatures import loader


class ResourceHandler(BaseHandler):
    name = "resources"

    def __init__(self, reader, writer, settings):
        super().__init__(reader, writer, settings)
        self.offsets = loader.load("resources")
        self.target = settings.resource_target

    def tick(self) -> None:
        if not self.enabled:
            return
        for key, chain in self.offsets["chains"].items():
            addr = self.reader.resolve_pointer(self.offsets["base"], chain)
            self.writer.write_int32(addr, self.target)