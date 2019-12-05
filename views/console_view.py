from functools import reduce


class ConsoleView:

    def __init__(self, contents=[]):
        self.contents = contents

    def print_area(self, tiles):
        impression = reduce(lambda m, t: t.print_to(m), tiles, self)
        print(impression)
        return impression

    def with_open_space(self, x, y):
        return self.with_character(x, y, "0")

    def with_wall(self, x, y):
        return self.with_character(x, y, "#")

    def with_character(self, x, y, character):
        return ConsoleView(self.contents + [character])

    def __str__(self):
        return ''.join(self.contents)
