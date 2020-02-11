class EnterTriggerEffect:

    def __init__(self, effect, center, radius, entered_count=0):
        self.effect = effect
        self.center = center
        self.radius = radius
        self.entered_count = entered_count

    def affect(self, area):
        return area.replace_effect(self, self.effect) if area.print_to(self).entered() else area

    def entered(self):
        return self.entered_count > 0

    def with_open_space(self, x, y):
        return self

    def with_wall(self, x, y):
        return self

    def with_actor(self, x, y, key):
        center_x, center_y = self.center
        return self if abs(center_x - x) > self.radius or abs(center_y - y) > self.radius else self.__up_count()

    def with_ledge(self, x, y):
        return self

    def with_door(self, x, y):
        return self

    def __up_count(self):
        return EnterTriggerEffect(self.effect, self.center, self.radius, self.entered_count + 1)
