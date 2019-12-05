class OccupiedSpace:

    def __init__(self, occupant):
        self.occupant = occupant

    def enter(self, actor):
        return self

    def leave(self, actor):
        from .open_space import OpenSpace
        return OpenSpace() if actor == self.occupant else self

    def update(self, area, tile):
        return self.occupant.act(area, tile)

    def print_to(self, x, y, media):
        return self.occupant.print_to(x, y, media)
