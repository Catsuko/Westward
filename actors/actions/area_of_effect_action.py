from actors.actions.action import Action
from functools import reduce


class AreaOfEffectAction(Action):

    def __init__(self, radius=1, effect_description='danger'):
        self.radius = radius
        self.effect_description = effect_description

    def on(self, actor, tile, root):
        for x, y in self.__affected_positions():
            x_offset = x - self.radius
            y_offset = y - self.radius
            if abs(x_offset) + abs(y_offset) <= self.radius:
                root = tile.neighbour(x_offset, y_offset, root).attempt("damage", root)
        return root

    def print_to(self, media):
        return reduce(self.__print_effect_description, self.__affected_positions(), media)

    def __print_effect_description(self, media, position):
        return media.with_effect(*position, self.effect_description)

    def __affected_positions(self):
        size = self.radius * 2 + 1
        return ((x, y) for x in range(size) for y in range(size))
