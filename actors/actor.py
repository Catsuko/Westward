class Actor:

    def __init__(self, engine, key="p"):
        self.key = key
        self.engine = engine

    def act(self, tile, root):
        target_dir = self.engine.pick_movement_direction(tile, root)
        target = tile.neighbour(target_dir[0], target_dir[1], root)
        return target.enter(self, tile, tile.leave(self, root))

    def print_to(self, x, y, media):
        return media.with_actor(x, y, self.key)

    def __str__(self):
        return "Actor %s" % self.key
