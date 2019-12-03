from .occupied_tile import *


class OpenTile:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def enter(self, actor, origin):
        return OccupiedTile(self.x, self.y, actor)

    def leave(self, actor):
        return self

    def update(self, area):
        return [self]

    def is_at(self, other_tile):
        return other_tile.at_position(self.x, self.y)

    def at_position(self, x, y):
        return x == self.x and y == self.y

    def print_to(self, media):
        media.print_open_space(self.x, self.y)

