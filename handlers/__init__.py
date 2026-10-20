"""Handler registry - order matters for tick scheduling."""
from handlers.infinite_hull_handler import InfiniteHullHandler
from handlers.crew_stat_handler import CrewStatHandler
from handlers.resource_handler import ResourceHandler
from handlers.overlay_handler import OverlayHandler

HANDLER_REGISTRY = {
    "infinite_hull": InfiniteHullHandler,
    "crew_stats": CrewStatHandler,
    "resources": ResourceHandler,
    "overlay": OverlayHandler,
}