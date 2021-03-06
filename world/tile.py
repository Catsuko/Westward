from world.bounds import Bounds


class Tile(Bounds):

    def __init__(self, x, y, space):
        self.x = x
        self.y = y
        self.space = space

    def update(self, root):
        return self.space.update(self, root)

    def update_actor(self, actor, update_delegate, root):
        return self.space.update_actor(actor, update_delegate, self, root)

    def attempt(self, action, root, *args):
        args = args + (self,)
        return self.space.attempt(action, root, *args)

    # TODO: How can we refactor tile and find_in, these methods feel weird!
    def tile(self, x, y):
        return self

    def find_in(self, area):
        return area.tile(self.x, self.y)

    def surrounds(self, x, y):
        return abs(x - self.x) < 1 and abs(y - self.y) < 1

    def enclosed_by(self, bounds):
        return bounds.surrounds(self.x, self.y)

    def print_to(self, media):
        return self.space.print_to(self.x, self.y, media)

    def enter(self, actor, origin, root):
        return self.space.enter(actor, origin, self, root)

    def leave(self, actor, root):
        return self.space.leave(actor, self, root)

    def to(self, other_tile, normalize=True):
        x, y = other_tile.direction_from(self.x, self.y, normalize)
        return -x, -y

    def direction_from(self, x, y, normalize=True):
        x = x - self.x
        y = y - self.y
        if normalize:
            x = min(max(x, -1), 1)
            y = min(max(y, -1), 1)
        return x, y

    def neighbour(self, x_offset, y_offset, root):
        return root.tile(self.x + x_offset, self.y + y_offset)

    def with_space(self, space):
        return Tile(self.x, self.y, space)

    def __str__(self):
        return "%s Tile (%d, %d)" % (self.space.__class__.__name__, self.x, self.y)
