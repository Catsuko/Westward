class OccupiedSpace:

    def __init__(self, occupant):
        self.occupant = occupant

    def enter(self, actor, origin, tile, root):
        return root if actor == self.occupant else self.__interaction(actor, origin, tile, root)

    def leave(self, actor, tile, root):
        from .open_space import OpenSpace
        return root.with_tile(tile.with_space(OpenSpace())) if actor == self.occupant else root

    def update(self, tile, root):
        return root.update_actor(self.occupant, root)

    def update_actor(self, actor, tile, root):
        return self.occupant.act(tile, root) if actor == self.occupant else root

    def replace_actor(self, actor, tile, root):
        return root.with_tile(tile.with_space(OccupiedSpace(actor))) if actor == self.occupant else root

    def print_to(self, x, y, media):
        return self.occupant.print_to(x, y, media)

    def __replace(self, occupant, tile, root):
        return root.with_tile(tile.with_space(OccupiedSpace(occupant)))

    def __interaction(self, other, origin, tile, root):
        return other.interact_with(self.occupant, origin, tile, self.occupant.receive(other, origin, tile, root))
