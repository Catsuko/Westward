from views.area_media import AreaMedia


class ActorTarget(AreaMedia):

    def __init__(self, target_key, target_position=None):
        self.target_key = target_key
        self.target_position = target_position

    def with_area(self, area):
        return area.print_to(self)

    def with_actor(self, x, y, key):
        return ActorTarget(self.target_key, (x, y)) if key == self.target_key else self

    def direction_to(self, origin, normalize=True):
        return (0, 0) if self.target_position is None else origin.direction_from(*self.target_position, normalize)

    def found(self):
        return self.target_position is not None

    def found_at(self, x, y):
        target_x, target_y = self.target_position
        return target_x is x and target_y is y
