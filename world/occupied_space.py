class OccupiedSpace:

    def __init__(self, occupant):
        self.occupant = occupant

    def enter(self, actor, origin, tile, world):
        return [origin]

    def leave(self, actor, tile, world):
        from .open_space import OpenSpace
        return [tile.with_space(OpenSpace()) if actor == self.occupant else self]

    def update(self, tile, world):
        return self.occupant.act(tile, world)

    def print_to(self, x, y, media):
        return self.occupant.print_to(x, y, media)
