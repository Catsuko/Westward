class UseAction:

    def __init__(self, x_dir, y_dir):
        self.x_dir = x_dir
        self.y_dir = y_dir

    def on(self, actor, tile, root):
        return actor.use(tile, tile.neighbour(self.x_dir, self.y_dir, root), root)
