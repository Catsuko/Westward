class SpawnEffect:

    def __init__(self, actor, spawn_points, death_trigger=None):
        self.actor = actor
        self.spawn_points = spawn_points
        self.death_trigger = death_trigger

    def affect(self, area):
        death_trigger = self.death_trigger
        for pos in self.spawn_points:
            tile = area.tile(*pos)
            actor = self.actor.unique()
            if death_trigger is not None:
                death_trigger = death_trigger.watch(actor)
            area = tile.enter(actor, tile, area)
        return area.without_effect(self) if death_trigger is None else area.replace_effect(self, death_trigger)
