from .open_tile import *


class OccupiedTile:

    def __init__(self, x, y, occupant):
        self.x = x
        self.y = y
        self.occupant = occupant

    def enter(self, actor, origin):
        return origin

    def leave(self, actor):
        return OpenTile(self.x, self.y) if actor == self.occupant else self

    def update(self, area):
        return self.occupant.act(area, self)

    def is_at(self, other_tile):
        other_tile.at_position(self.x, self.y)

    def at_position(self, x, y):
        print("%s, %s == %s, %s" % (x, y, self.x, self.y))
        return x == self.x and y == self.y

    def print_to(self, media):
        self.occupant.print_to(media)
