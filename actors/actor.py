class Actor:

    def __init__(self, engine, key="@"):
        self.key = key
        self.engine = engine

    def act(self, area, origin):
        target_dir = self.engine.pick_movement_direction(area, origin)
        target = origin.neighbour(area, target_dir[0], target_dir[1])
        return [origin.leave(self), target.enter(self, origin)]

    def print_to(self, x, y, media):
        return media.with_character(x, y, self.key)
