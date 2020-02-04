class UseAction:

    def __init__(self, x_dir, y_dir):
        self.x_dir = x_dir
        self.y_dir = y_dir

    def on(self, actor, tile, root):
        target = tile.neighbour(self.x_dir, self.y_dir, root)
        return actor.attempt("use_primary", root, target, tile), self

