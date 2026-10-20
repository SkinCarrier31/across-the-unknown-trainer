"""Base class all trainer features inherit from."""
from abc import ABC, abstractmethod
from core.memory_reader import MemoryReader
from core.memory_writer import MemoryWriter


class BaseHandler(ABC):
    name: str = "base"

    def __init__(self, reader: MemoryReader, writer: MemoryWriter, settings):
        self.reader = reader
        self.writer = writer
        self.settings = settings
        self.enabled = True

    @abstractmethod
    def tick(self) -> None:
        """Called every engine tick."""

    def on_shutdown(self) -> None:
        """Optional cleanup hook."""