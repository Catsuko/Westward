class Tile:

    def __init__(self, x, y, space):
        self.x = x
        self.y = y
        self.space = space

    def update(self, root):
        return self.space.update(self, root)

    def with_tile(self, tile):
        return tile if tile.surrounds(self.x, self.y) else self

    def tile(self, x, y):
        return self

    def surrounds(self, x, y):
        return abs(x - self.x) < 1 and abs(y - self.y) < 1

    def enclosed_by(self, area):
        return area.surrounds(self.x, self.y)

    def print_to(self, media):
        return self.space.print_to(self.x, self.y, media)

    def enter(self, actor, origin, area):
        return self.space.enter(actor, origin, self, area)

    def leave(self, actor, area):
        return self.space.leave(actor, self, area)

    def to(self, other_tile):
        from_dir = other_tile.direction_from(self.x, self.y)
        return -from_dir[0], -from_dir[1]

    def direction_from(self, x, y):
        return x - self.x, y - self.y

    def neighbour(self, x_offset, y_offset, root):
        return root.tile(self.x + x_offset, self.y + y_offset)

    def with_space(self, space):
        return Tile(self.x, self.y, space)

    def __str__(self):
        return "%s Tile (%d, %d)" % (self.space.__class__.__name__, self.x, self.y)