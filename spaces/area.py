from functools import reduce


class Area:

    def __init__(self, tiles=[]):
        self.tiles = tiles

    def update(self):
        return reduce(lambda area, tile: area.with_tiles(tile.update(area)), self.tiles, self)

    def with_tiles(self, tiles):
        return Area([self.updated_or_current(tiles, tile) for tile in self.tiles])

    def updated_or_current(self, updates, current):
        return next((new_tile for new_tile in updates[::-1] if new_tile.same_position_as(current)), current)

    def print_to(self, media):
        return media.print_area(self.tiles)
