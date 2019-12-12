class OccupiedSpace:

    def __init__(self, occupant):
        self.occupant = occupant

    def enter(self, actor, origin, tile, root):
        return root

    def leave(self, actor, tile, root):
        from .open_space import OpenSpace
        return root.with_tile(tile.with_space(OpenSpace())) if actor == self.occupant else root

    def update(self, tile, root):
        return self.occupant.act(tile, root)

    def print_to(self, x, y, media):
        return self.occupant.print_to(x, y, media)
