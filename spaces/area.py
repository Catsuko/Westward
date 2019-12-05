from functools import reduce


class Area:

    def __init__(self, tiles=[]):
        self.tiles = tiles

    def update(self):
        return reduce(lambda area, tile: area.with_tiles(tile.update(area)), self.tiles, self)

    def with_tiles(self, tiles):
        return Area([self.__updated_or_current(tiles, tile) for tile in self.tiles])

    def tile(self, x, y, x_offset, y_offset):
        target_x = x + round(x_offset)
        target_y = y + round(y_offset)
        return next((tile for tile in self.tiles if tile.at_position(target_x, target_y)))

    def print_to(self, media):
        return media.print_area(self.tiles)

    def __updated_or_current(self, updates, current):
        return next((new_tile for new_tile in updates[::-1] if new_tile.same_position_as(current)), current)

