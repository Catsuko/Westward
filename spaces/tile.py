class Tile:

    def __init__(self, x, y, space):
        self.x = x
        self.y = y
        self.space = space

    def enter(self, actor, origin):
        return Tile(self.x, self.y, self.space.enter(actor, origin))

    def leave(self, actor):
        return Tile(self.x, self.y, self.space.leave(actor))

    def update(self, area):
        return self.space.update(area, self)

    def same_position_as(self, other_tile):
        return other_tile.at_position(self.x, self.y)

    def at_position(self, x, y):
        return x == self.x and y == self.y

    def print_to(self, media):
        return self.space.print_to(self.x, self.y, media)
