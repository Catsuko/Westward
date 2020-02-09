class SpawnEffect:

    def __init__(self, actor, spawn_points):
        self.actor = actor
        self.spawn_points = spawn_points

    def affect(self, area):
        for pos in self.spawn_points:
            tile = area.tile(*pos)
            area = tile.enter(self.actor.unique(), tile, area)
        return area.without_effect(self)

