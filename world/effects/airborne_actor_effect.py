# TODO: Implement -> Move for x turns and then create the actor!
class AirborneActorEffect:

    def __init__(self, actor, start, velocity, duration):
        self.actor = actor
        self.start = start
        self.velocity = velocity
        self.duration = duration

    def affect(self, area):
        return area
