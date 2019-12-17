class PointCamera:

    def __init__(self, x, y, size, media):
        self.x = x
        self.y = y
        self.size = size
        self.media = media

    def move_to(self, x, y):
        return PointCamera(x, y, self.size, self.media)

    def render(self):
        return self.media.render()

    def with_area(self, area):
        return area.print_to(self)

    def with_open_space(self, x, y):
        return self.__printed(self.media.with_open_space(x, y)) if self.__within_bounds(x, y) else self

    def with_wall(self, x, y):
        return self.__printed(self.media.with_wall(x, y)) if self.__within_bounds(x, y) else self

    def with_actor(self, x, y, key):
        return self.__printed(self.media.with_actor(x, y, key)) if self.__within_bounds(x, y) else self

    def with_ledge(self, x, y):
        return self.__printed(self.media.with_ledge(x, y)) if self.__within_bounds(x, y) else self

    def with_door(self, x, y):
        return self.__printed(self.media.with_door(x, y)) if self.__within_bounds(x, y) else self

    def __within_bounds(self, x, y):
        return abs(x - self.x) < self.size and abs(y - self.y) < self.size

    def __printed(self, media):
        return PointCamera(self.x, self.y, self.size, media)

    def __str__(self):
        return str(self.media)