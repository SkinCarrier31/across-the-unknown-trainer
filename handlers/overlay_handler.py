"""In-game overlay - draws trainer status via pygame."""
import pygame
from handlers.base_handler import BaseHandler


class OverlayHandler(BaseHandler):
    name = "overlay"

    def __init__(self, reader, writer, settings):
        super().__init__(reader, writer, settings)
        self._initialized = False
        self._surface = None
        self._font = None

    def _init_overlay(self) -> None:
        pygame.init()
        pygame.font.init()
        self._surface = pygame.display.set_mode(
            (320, 120), pygame.NOFRAME | pygame.SRCALPHA
        )
        self._font = pygame.font.SysFont("Consolas", 14)
        self._initialized = True

    def tick(self) -> None:
        if not self.enabled:
            return
        if not self._initialized:
            self._init_overlay()
        self._surface.fill((0, 0, 0, 0))
        text = self._font.render(
            "AcrossTheUnknown Trainer | ACTIVE", True, (0, 255, 180)
        )
        self._surface.blit(text, (8, 8))

    def on_shutdown(self) -> None:
        if self._initialized:
            pygame.quit()