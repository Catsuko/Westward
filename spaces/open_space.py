from .occupied_space import *


class OpenSpace:

    def enter(self, actor):
        return OccupiedSpace(actor)

    def leave(self, actor):
        return self

    def update(self, area, tile):
        return []

    def print_to(self, x, y, media):
        return media.with_open_space(x, y)
