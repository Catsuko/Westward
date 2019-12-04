class Area:

    def __init__(self, tiles=[]):
        self.tiles = tiles

    def update(self):
        area = self
        for tile in self.tiles:
            area = area.with_tiles(tile.update(area))
        return area

    def with_tiles(self, tiles):
        return Area([next((new_tile for new_tile in tiles
                           if tile.same_position_as(new_tile)), tile)
                     for tile in self.tiles])

    def print_to(self, media):
        return media.print_area(self.tiles)
