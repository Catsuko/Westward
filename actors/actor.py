class Actor:

    def __init__(self, engine, key="@", area_listener=None):
        self.key = key
        self.engine = engine
        self.area_listener = area_listener

    def act(self, area, origin):
        target_dir = self.engine.pick_movement_direction(area, origin)
        target = origin.neighbour(area, target_dir[0], target_dir[1])
        return [origin.leave(self), target.enter(self, origin)]

    def survey(self, area):
        if self.area_listener is not None:
            self.area_listener(area)

    def print_to(self, x, y, media):
        return media.with_character(x, y, self.key)
