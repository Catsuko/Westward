from itertools import chain
from world.blocked_space import BlockedSpace
from world.tile import Tile


class Area:

    def __init__(self, sub_areas=[]):
        self.sub_areas = sub_areas

    def update(self):
        return list(chain.from_iterable([tile.update(self) for tile in self.sub_areas]))

    def with_tiles(self, tiles):
        return Area([self.__updated_or_current(tiles, tile) for tile in self.sub_areas])

    def tile(self, x, y):
        target_x = round(x)
        target_y = round(y)
        out_of_bounds = Tile(target_x, target_y, BlockedSpace())
        return next((tile for tile in self.sub_areas if tile.at_position(target_x, target_y)), out_of_bounds)

    def surrounds(self, x, y):
        return any([sub_area.surrounds(x, y) for sub_area in self.sub_areas])

    def print_to(self, media):
        return media.print_area(self.sub_areas)

    def __updated_or_current(self, updates, current):
        return next((new_tile for new_tile in updates[::-1] if new_tile.same_position_as(current)), current)

