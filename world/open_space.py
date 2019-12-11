from .occupied_space import *


class OpenSpace:

    def enter(self, actor, origin, tile, area):
        return [tile.with_space(OccupiedSpace(actor))]

    def leave(self, actor, tile, area):
        return []

    def update(self, tile, area):
        return []

    def print_to(self, x, y, media):
        return media.with_open_space(x, y)
