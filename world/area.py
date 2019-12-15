from functools import reduce

from world.blocked_space import BlockedSpace
from world.tile import Tile


class Area:

    def __init__(self, sub_areas=[]):
        self.sub_areas = sub_areas

    def update(self, root=None):
        return reduce(lambda root_area, sub_area: sub_area.update(root_area), self.sub_areas, root or self)

    def with_tile(self, tile):
        return Area([area.with_tile(tile) if tile.enclosed_by(area) else area for area in self.sub_areas])

    def tile(self, x, y):
        out_of_bounds = Tile(x, y, BlockedSpace())
        return next((sub_area.tile(x, y) for sub_area in self.sub_areas if sub_area.surrounds(x, y)), out_of_bounds)

    def surrounds(self, x, y):
        return any([sub_area.surrounds(x, y) for sub_area in self.sub_areas])

    def enclosed_by(self, area):
        return all([sub_area.enclosed_by(area) for sub_area in self.sub_areas])

    def print_to(self, media):
        return media.with_tiles(self.sub_areas)

    def __str__(self):
        return "Area (%d sub areas)" % len(self.sub_areas)


