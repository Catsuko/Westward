from world.area import Area
from world.blocked_space import BlockedSpace
from world.ledge_space import LedgeSpace
from world.occupied_space import OccupiedSpace
from world.open_space import OpenSpace
from world.tile import Tile
from world.door_space import DoorSpace


class AreaBuilder:

    def __init__(self, x=0, y=0, tiles=[]):
        self.x = x
        self.y = y
        self.tiles = tiles

    def with_actor(self, actor, x, y):
        return self.with_tile(x, y, OccupiedSpace(actor))

    def with_door(self, x, y, exit_x, exit_y):
        return self.with_tile(x, y, DoorSpace(exit_x, exit_y))

    def with_ledge(self, x, y, allowed_direction=(0, -1)):
        return self.with_tile(x, y, LedgeSpace(allowed_direction))

    def with_wall(self, x, y):
        return self.with_tile(x, y, BlockedSpace())

    def with_tile(self, x, y, space):
        new_tile = Tile(self.x + x, self.y + y, space)
        return AreaBuilder(self.x, self.y, [new_tile if new_tile.enclosed_by(tile) else tile for tile in self.tiles])

    def rectangle(self, width, height):
        open_space = OpenSpace()
        return AreaBuilder(self.x, self.y, [Tile(x + self.x, y + self.y, open_space) for x in range(width) for y in range(height)])

    def starting_from(self, x, y):
        return AreaBuilder(x, y, self.tiles)

    def to_area(self):
        return Area(self.tiles)

