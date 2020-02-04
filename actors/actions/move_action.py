class MoveAction:

    def __init__(self, x_dir=0, y_dir=0):
        self.x_dir = x_dir
        self.y_dir = y_dir

    def on(self, actor, tile, root):
        destination = tile.neighbour(self.x_dir, self.y_dir, root)
        return destination.enter(actor, tile, tile.leave(actor, root)), self

    def redirect(self, x_dir, y_dir):
        return MoveAction(x_dir, y_dir)

