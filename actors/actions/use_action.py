class UseAction:

    def __init__(self, x_dir=0, y_dir=0):
        self.x_dir = x_dir
        self.y_dir = y_dir

    def on(self, actor, tile, root):
        target = tile.neighbour(self.x_dir, self.y_dir, root)
        return actor.attempt("use_primary", root, target, tile), self

    def redirect(self, x_dir, y_dir):
        return UseAction(x_dir, y_dir)
