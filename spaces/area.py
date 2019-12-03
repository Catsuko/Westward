class Area:

    def __init__(self, tiles=[]):
        self.tiles = tiles

    def update(self):
        area = self
        for tile in self.tiles:
            area = area.with_tiles(tile.update(area))
        return area

    # TODO: TEST THIS METHOD!
    def with_tiles(self, tiles):
        return Area([next((new_tile for new_tile in tiles if tile.is_at(new_tile)), tile) for tile in self.tiles])

    def print_to(self, media):
        [tile.print_to(media) for tile in self.tiles]
