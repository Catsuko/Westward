from .occupied_space import *


class OpenSpace:

    def enter(self, actor, origin, tile, root):
        return root.with_tile(tile.with_space(OccupiedSpace(actor)))

    def leave(self, actor, tile, root):
        return root

    def update(self, tile, root):
        return root

    def with_space(self, space):
        return space

    def print_to(self, x, y, media):
        return media.with_open_space(x, y)
