from spaces.area import Area
from spaces.occupied_space import OccupiedSpace
from spaces.open_space import OpenSpace
from spaces.tile import Tile


class AreaBuilder:

    def __init__(self, tiles=[]):
        self.tiles = tiles

    def with_actor(self, actor, x, y):
        tiles = [row[:] for row in self.tiles]
        tiles[y][x] = Tile(x, y, OccupiedSpace(actor))
        return AreaBuilder(tiles)

    def rectangle(self, width, height):
        open_space = OpenSpace()
        return AreaBuilder([[Tile(x, y, open_space) for x in range(width)] for y in range(height)])

    def to_area(self):
        return Area([tile for tile_row in self.tiles for tile in tile_row])
