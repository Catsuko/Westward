class LedgeSpace:

    def __init__(self, space):
        self.space = space

    def enter(self, actor, origin, tile, root):
        blocked = origin.above(tile)
        return root.with_tile(origin) if blocked else self.space.enter(actor, origin, tile, root)

    def leave(self, actor, tile, root):
        return self.space.leave(actor, tile, root)

    def update(self, tile, root):
        return self.space.update(tile, root)

    def with_space(self, space):
        return LedgeSpace(space)

    def print_to(self, x, y, media):
        return media.with_ledge(x, y)

