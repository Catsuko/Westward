class ActorTarget:

    def __init__(self, target_key, target_position=None):
        self.target_key = target_key
        self.target_position = target_position

    def with_area(self, area):
        return area.print_to(self)

    def with_open_space(self, x, y):
        return self

    def with_wall(self, x, y):
        return self

    def with_actor(self, x, y, key):
        return ActorTarget(self.target_key, (x, y)) if key == self.target_key else self

    def with_ledge(self, x, y):
        return self

    def with_door(self, x, y):
        return self

    def direction_to(self, origin):
        return (0, 0) if self.target_position is None else origin.direction_from(*self.target_position)