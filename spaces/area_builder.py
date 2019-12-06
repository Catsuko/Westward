from spaces.area import Area
from spaces.den_tile import DenTile
from spaces.occupied_space import OccupiedSpace
from spaces.open_space import OpenSpace
from spaces.tile import Tile


class AreaBuilder:

    def __init__(self, tiles=[]):
        self.tiles = tiles

    def with_actor(self, actor, x, y):
        new_tile = Tile(x, y, OccupiedSpace(actor))
        return AreaBuilder([new_tile if new_tile.same_position_as(tile) else tile for tile in self.tiles])

    def with_den(self, x, y, width, length):
        den = DenTile(x, y, width, length)
        return AreaBuilder([tile for tile in self.tiles if not tile.same_position_as(den)] + [den])

    def rectangle(self, width, height):
        open_space = OpenSpace()
        return AreaBuilder([Tile(x, y, open_space) for x in range(width) for y in range(height)])

    def to_area(self):
        return Area(self.tiles)

