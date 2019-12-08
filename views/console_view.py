from functools import reduce


class ConsoleView:

    def __init__(self, contents=""):
        self.contents = contents

    def print_area(self, tiles):
        impression = reduce(lambda m, t: t.print_to(m), tiles, self)
        print(impression)
        return impression

    def with_open_space(self, x, y):
        return self.with_character(x, y, "0")

    def with_wall(self, x, y):
        return self.with_character(x, y, "#")

    def with_actor(self, x, y, key):
        return self.with_character(x, y, key)

    def with_character(self, x, y, character):
        rows = self.contents.split("\n")
        width = len(rows[0])
        height = len(rows)
        rows.extend([" " for i in range(max((y-height)+1, 0))])
        rows = [row + (" " * max(x - width, 0)) for row in rows]
        rows[y] = (rows[y][:x] + character + rows[y][x+1:])
        return ConsoleView("\n".join(rows))

    def __str__(self):
        return '\n'.join([s.lstrip() for s in self.contents.split('\n')])
