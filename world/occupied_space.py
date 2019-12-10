class OccupiedSpace:

    def __init__(self, occupant):
        self.occupant = occupant

    def enter(self, actor, origin, tile, area):
        return area.with_tiles([origin])

    def leave(self, actor, tile, area):
        from .open_space import OpenSpace
        return area.with_tiles([tile.with_space(OpenSpace())]) if actor == self.occupant else area

    def update(self, tile, area):
        return self.occupant.act(tile, area)

    def print_to(self, x, y, media):
        return self.occupant.print_to(x, y, media)
