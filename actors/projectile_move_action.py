class ProjectileMoveAction:

    def __init__(self, x_dir, y_dir):
        self.x_dir = x_dir
        self.y_dir = y_dir

    def on(self, actor, tile, root):
        destination = tile.neighbour(self.x_dir, self.y_dir, root)
        root_without_projectile = tile.leave(actor, root)
        origin = tile.neighbour(0, 0, root_without_projectile)
        return destination.enter(actor, origin, root_without_projectile)

    def redirect(self, x_dir, y_dir):
        return ProjectileMoveAction(x_dir, y_dir)
