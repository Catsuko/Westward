class DoorSpace:

    def __init__(self, exit_x, exit_y):
        self.exit_x = exit_x
        self.exit_y = exit_y

    def enter(self, actor, origin, tile, root):
        exit = root.tile(self.exit_x, self.exit_y)
        return exit.enter(actor, origin, root)

    def leave(self, actor, tile, root):
        return root

    def update(self, tile, root):
        return root

    def print_to(self, x, y, media):
        return media.with_character(x, y, '_')