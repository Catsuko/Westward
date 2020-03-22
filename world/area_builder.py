from world.area import Area
from world.occupied_space import OccupiedSpace
from world.open_space import OpenSpace
from world.tile import Tile
from world.door_space import DoorSpace
from functools import reduce


class AreaBuilder:

    def __init__(self, x=0, y=0, tiles=[]):
        self.x = x
        self.y = y
        self.tiles = tiles

    def with_actor(self, actor, x, y):
        return self.with_tile(x, y, OccupiedSpace(actor))

    def with_open_space(self, x, y):
        return self.with_tile(x, y, OpenSpace())

    def with_door(self, x, y, exit_x, exit_y):
        return self.with_tile(x, y, DoorSpace(exit_x, exit_y))

    def with_tile(self, x, y, space):
        return AreaBuilder(self.x, self.y, self.__tiles_with(self.__tile(x, y, space)))

    def rectangle(self, width, height):
        open_space = OpenSpace()
        points = [(x, y) for x in range(width) for y in range(height)]
        return reduce(lambda builder, point: builder.with_tile(*point, open_space), points, self)

    def reposition(self, x, y):
        return AreaBuilder(x, y, self.tiles)

    def nudge(self, x_offset, y_offset):
        return AreaBuilder(self.x + x_offset, self.y + y_offset, self.tiles)

    def to_area(self):
        return Area(self.tiles)

    def __tiles_with(self, new_tile):
        is_new = any([new_tile.enclosed_by(tile) for tile in self.tiles])
        return [new_tile if new_tile.enclosed_by(tile) else tile for tile in self.tiles] if is_new else self.tiles + [new_tile]

    def __tile(self, x, y, space):
        return Tile(x + self.x, y + self.y, space)

