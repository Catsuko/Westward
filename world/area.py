from functools import reduce
from world.blocked_space import BlockedSpace
from world.bounds import Bounds
from world.tile import Tile


class Area(Bounds):

    def __init__(self, sub_areas=[], effects=[]):
        self.sub_areas = sub_areas
        self.effects = effects

    def update(self, root=None):
        area_after_effects = reduce(lambda area, effect: effect.affect(area), self.effects, self)
        root = (root or self).with_area(area_after_effects)
        return reduce(lambda root_area, sub_area: sub_area.update(root_area), self.sub_areas, root)

    def update_actor(self, actor, update_delegate, root=None):
        root = root or self
        return reduce(lambda result, area: area.update_actor(actor, update_delegate, result), self.sub_areas, root)

    def with_area(self, area):
        if area == self:
            return area
        return self.__replace_area(area) if area in self.sub_areas else self.__replace_in_sub_area(area)

    def tile(self, x, y):
        out_of_bounds = Tile(x, y, BlockedSpace())
        return next((sub_area.tile(x, y) for sub_area in self.sub_areas if sub_area.surrounds(x, y)), out_of_bounds)

    def surrounds(self, x, y):
        return any([sub_area.surrounds(x, y) for sub_area in self.sub_areas])

    def enclosed_by(self, bounds):
        return all([sub_area.enclosed_by(bounds) for sub_area in self.sub_areas])

    def with_effect(self, effect):
        return Area(self.sub_areas, self.effects + [effect])

    def without_effect(self, effect):
        return Area(self.sub_areas, [e for e in self.effects if e is not effect])

    def replace_effect(self, old, new):
        return Area(self.sub_areas, [new if e is old else e for e in self.effects])

    def print_to(self, media):
        return reduce(lambda m, obj: obj.print_to(m), self.sub_areas + self.effects, media)

    def __replace_area(self, area):
        return Area([area if area == sub_area else sub_area for sub_area in self.sub_areas], self.effects)

    def __replace_in_sub_area(self, area):
        return next((self.with_area(sa.with_area(area)) for sa in self.sub_areas if area.enclosed_by(sa)), self)

    def __str__(self):
        return "Area (%d sub areas)" % len(self.sub_areas)


