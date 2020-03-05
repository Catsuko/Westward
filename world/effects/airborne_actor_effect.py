class AirborneActorEffect:

    def __init__(self, actor, position, velocity, duration):
        self.actor = actor
        self.position = position
        self.velocity = velocity
        self.duration = duration

    def affect(self, area):
        if self.duration > 0:
            return area.replace_effect(self, self.__move_position())
        else:
            target_tile = area.tile(*self.position)
            return target_tile.enter(self.actor, target_tile, area).without_effect(self)

    def print_to(self, media):
        return media.with_effect(*self.position, "shadow")

    def __move_position(self):
        x, y = self.position
        x_dir, y_dir = self.velocity
        return AirborneActorEffect(self.actor, (x+x_dir, y+y_dir), self.velocity, self.duration - 1)
