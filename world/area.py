from functools import reduce
from world.blocked_space import BlockedSpace
from world.bounds import Bounds
from world.tile import Tile


class Area(Bounds):

    def __init__(self, sub_areas=[]):
        self.sub_areas = sub_areas

    def update(self, root=None):
        return reduce(lambda root_area, sub_area: sub_area.update(root_area), self.sub_areas, root or self)

    def update_actor(self, actor, root=None):
        return reduce(lambda root_area, sub_area: sub_area.update_actor(actor, root_area), self.sub_areas, root or self)

    def replace_actor(self, actor, root=None):
        return reduce(lambda root_area, area: area.replace_actor(actor, root_area), self.sub_areas, root or self)

    def with_area(self, area):
        return self.__replace_area(area) if area in self.sub_areas else self.__replace_in_sub_area(area)

    def tile(self, x, y):
        out_of_bounds = Tile(x, y, BlockedSpace())
        return next((sub_area.tile(x, y) for sub_area in self.sub_areas if sub_area.surrounds(x, y)), out_of_bounds)

    def surrounds(self, x, y):
        return any([sub_area.surrounds(x, y) for sub_area in self.sub_areas])

    def enclosed_by(self, bounds):
        return all([sub_area.enclosed_by(bounds) for sub_area in self.sub_areas])

    def print_to(self, media):
        return reduce(lambda m, area: area.print_to(m), self.sub_areas, media)

    def __replace_area(self, area):
        return Area([area if area == sub_area else sub_area for sub_area in self.sub_areas])

    def __replace_in_sub_area(self, area):
        return next((self.with_area(sa.with_area(area)) for sa in self.sub_areas if area.enclosed_by(sa)), self)

    def __str__(self):
        return "Area (%d sub areas)" % len(self.sub_areas)


