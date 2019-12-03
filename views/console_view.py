# TODO: MAKE IMMUTABLE!
# TODO: Print tiles in order
# TODO: Maybe create a large rect and place tiles
#       inside of it?


class ConsoleView:

    def __init__(self):
        self.output = [""]

    def print_open_space(self, x, y):
        print("0")

    def print_wall(self, x, y):
        print("#")
