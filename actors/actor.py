# TODO: Refactor input into an Engine responsible for dictating actions.
# TODO: Introduce an actor that roams around the map randomly.


class Actor:

    def __init__(self, key="@"):
        self.key = key
        self.keys_table = {
            'w': (0, -1), 's': (0, 1),
            'a': (-1, 0), 'd': (1, 0)
        }

    def act(self, area, origin):
        inp = input()
        while inp not in self.keys_table.keys():
            inp = input()
        target_dir = self.keys_table[inp]
        target = origin.neighbour(area, target_dir[0], target_dir[1])
        return [origin.leave(self), target.enter(self, origin)]

    def print_to(self, x, y, media):
        return media.with_character(x, y, self.key)
