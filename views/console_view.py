class ConsoleView:

    def __init__(self, contents={}):
        self.contents = contents

    def render(self):
        print("\n%s\n" % self)

    def with_area(self, area):
        return area.print_to(self)

    def with_open_space(self, x, y):
        return self.__with_character(x, y, ".")

    def with_wall(self, x, y):
        return self.__with_character(x, y, "T")

    def with_actor(self, x, y, key):
        return self.__with_character(x, y, key[0])

    def with_ledge(self, x, y):
        return self.__with_character(x, y, "_")

    def with_door(self, x, y):
        return self.__with_character(x, y, "D")

    def __with_character(self, x, y, character):
        next_contents = self.contents.copy()
        next_contents[(x, y)] = character
        return ConsoleView(next_contents)

    def __str__(self):
        x_coords = [point[0] for point in self.contents.keys()]
        y_coords = [point[1] for point in self.contents.keys()]
        x_min = min(x_coords)
        x_max = max(x_coords)
        y_min = min(y_coords)
        y_max = max(y_coords)
        contents_str = ''
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                contents_str = contents_str + (self.contents[(x, y)] if (x, y) in self.contents else ' ')
            contents_str = contents_str + '\n'
        return contents_str

