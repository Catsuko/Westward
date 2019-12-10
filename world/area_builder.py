from environment.area import Area
from environment.den_tile import DenTile
from environment.door_tile import DoorTile
from environment.occupied_space import OccupiedSpace
from environment.open_space import OpenSpace
from environment.tile import Tile


class AreaBuilder:

    def __init__(self, x=0, y=0, tiles=[]):
        self.x = x
        self.y = y
        self.tiles = tiles

    def with_actor(self, actor, x, y):
        new_tile = Tile(x + self.x, y + self.y, OccupiedSpace(actor))
        return AreaBuilder(self.x, self.y, [new_tile if new_tile.same_position_as(tile) else tile for tile in self.tiles])

    def with_door(self, x, y, area):
        return AreaBuilder(self.x, self.y, self.tiles + [DoorTile(x + self.x, y + self.y, area)])

    def with_den(self, x, y, width, length):
        den = DenTile(x + self.x, y + self.y, width, length)
        return AreaBuilder(self.x, self.y, [tile for tile in self.tiles if not tile.same_position_as(den)] + [den])

    def rectangle(self, width, height):
        open_space = OpenSpace()
        return AreaBuilder(self.x, self.y, [Tile(x + self.x, y + self.y, open_space) for x in range(width) for y in range(height)])

    def starting_from(self, x, y):
        return AreaBuilder(x, y, self.tiles)

    def to_area(self):
        return Area(self.tiles)

