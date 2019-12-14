from functools import reduce


class Area:

    def __init__(self, sub_areas=[]):
        self.sub_areas = sub_areas

    def update(self, root=None):
        return reduce(lambda area, sub_area: sub_area.update(area), self.sub_areas, root or self)

    def with_tile(self, tile):
        return Area([sub_area.with_tile(tile) if tile.enclosed_by(sub_area) else sub_area for sub_area in self.sub_areas])

    # TODO: Return out of bounds tile when tile is not found.
    def tile(self, x, y):
        return next((sub_area.tile(x, y) for sub_area in self.sub_areas if sub_area.surrounds(x, y)), None)

    def surrounds(self, x, y):
        return any([sub_area.surrounds(x, y) for sub_area in self.sub_areas])

    def enclosed_by(self, area):
        return all([sub_area.enclosed_by(area) for sub_area in self.sub_areas])

    def print_to(self, media):
        return media.print_area(self.sub_areas)

