from .occupied_space import *


class OpenSpace:

    def enter(self, actor, origin, tile, area):
        return area.with_tiles([tile.with_space(OccupiedSpace(actor))])

    def leave(self, actor, tile, area):
        return area

    def update(self, tile, area):
        return area

    def print_to(self, x, y, media):
        return media.with_open_space(x, y)
