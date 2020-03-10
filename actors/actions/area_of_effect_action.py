from actors.actions.action import Action
from functools import reduce


class AreaOfEffectAction(Action):

    def __init__(self, radius=1, effect_description='danger'):
        self.radius = radius
        self.effect_description = effect_description

    def on(self, actor, tile, root):
        for x, y in self.__affected_positions():
            root = tile.neighbour(x, y, root).attempt("damage", root)
        return root

    def print_to(self, x, y, media):
        positions = self.__affected_positions(x, y)
        return reduce(lambda m, pos: m.with_effect(*pos, self.effect_description), positions, media)

    def __affected_positions(self, x_offset=0, y_offset=0):
        blast_range = range(-self.radius, self.radius+1)
        return ((x + x_offset, y + y_offset) for x in blast_range for y in blast_range if self.__in_range(x, y))

    def __in_range(self, x, y):
        return abs(x) + abs(y) <= self.radius
