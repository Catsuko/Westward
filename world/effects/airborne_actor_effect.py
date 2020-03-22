class AirborneActorEffect:

    def __init__(self, actor, countdown, position=(0,0), velocity=(0,0)):
        self.actor = actor
        self.countdown = countdown
        self.position = position
        self.velocity = velocity

    def affect(self, area):
        if self.countdown.is_finished():
            target_tile = area.tile(*self.position)
            return target_tile.enter(self.actor, target_tile, area).without_effect(self)
        else:
            return area.replace_effect(self, self.__move_position())

    # TODO: Implement this method, tests first!
    def starting_from(self, origin, target):
        return self

    def print_to(self, media):
        return media.with_effect(*self.position, "shadow")

    def __move_position(self):
        x, y = self.position
        x_dir, y_dir = self.velocity
        return AirborneActorEffect(self.actor, self.countdown.tick(), (x+x_dir, y+y_dir), self.velocity)
