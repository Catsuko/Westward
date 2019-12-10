from world.area import Area
from world.occupied_space import OccupiedSpace
from world.open_space import OpenSpace
from world.tile import Tile


class AreaBuilder:

    def __init__(self, x=0, y=0, tiles=[]):
        self.x = x
        self.y = y
        self.tiles = tiles

    def with_actor(self, actor, x, y):
        new_tile = Tile(x + self.x, y + self.y, OccupiedSpace(actor))
        return AreaBuilder(self.x, self.y, [new_tile if new_tile.same_position_as(tile) else tile for tile in self.tiles])

    def rectangle(self, width, height):
        open_space = OpenSpace()
        return AreaBuilder(self.x, self.y, [Tile(x + self.x, y + self.y, open_space) for x in range(width) for y in range(height)])

    def starting_from(self, x, y):
        return AreaBuilder(x, y, self.tiles)

    def to_area(self):
        return Area(self.tiles)

