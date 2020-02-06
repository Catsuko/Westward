class SpawnEffect:

    def __init__(self, actor, spawn_points):
        self.actor = actor
        self.spawn_points = spawn_points

    def affect(self, root):
        for pos in self.spawn_points:
            tile = root.tile(*pos)
            root = tile.enter(self.actor.unique(), tile, root)
        return root
