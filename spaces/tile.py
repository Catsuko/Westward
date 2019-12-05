class Tile:

    def __init__(self, x, y, space):
        self.x = x
        self.y = y
        self.space = space

    def enter(self, actor, origin):
        result = self.space.enter(actor)
        return origin if result == self.space else result

    def leave(self, actor):
        result = self.space.leave(actor)
        return self if result == self.space else result

    def update(self, area):
        return self.space.update(area, self)

    def same_position_as(self, other_tile):
        return other_tile.at_position(self.x, self.y)

    def at_position(self, x, y):
        return x == self.x and y == self.y

    def neighbour(self, area, x_offset, y_offset):
        return area.neighbour(self.x, self.y, x_offset, y_offset)

    def print_to(self, media):
        return self.space.print_to(self.x, self.y, media)
