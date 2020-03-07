from actors.actions.action import Action


class MoveAction(Action):

    def __init__(self, x_dir=0, y_dir=0):
        self.x_dir = x_dir
        self.y_dir = y_dir

    def on(self, actor, tile, root):
        return (root if self.__is_stationary() else self.__enter_next_tile(actor, tile, root)), self

    def redirect(self, x_dir, y_dir):
        return MoveAction(x_dir, y_dir)

    def __enter_next_tile(self, actor, tile, root):
        return tile.neighbour(self.x_dir, self.y_dir, root).enter(actor, tile, tile.leave(actor, root))

    def __is_stationary(self):
        return self.x_dir + self.y_dir == 0

