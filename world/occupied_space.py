class OccupiedSpace:

    def __init__(self, occupant):
        self.occupant = occupant

    def enter(self, actor, origin, tile, root):
        return root if actor == self.occupant else self.__interaction(actor, origin, tile, root)

    def leave(self, actor, tile, root):
        from .open_space import OpenSpace
        return root.with_area(tile.with_space(OpenSpace())) if actor == self.occupant else root

    def update(self, tile, root):
        return root.update_actor(self.occupant, self.__update_occupant)

    def update_actor(self, actor, update_delegate, tile, root):
        return update_delegate(self.occupant, tile, root) if self.occupant == actor else root

    def print_to(self, x, y, media):
        return self.occupant.print_to(x, y, media)

    def __update_occupant(self, actor, tile, root):
        return actor.act(tile, root)

    def __replace(self, occupant, tile, root):
        return root.with_area(tile.with_space(OccupiedSpace(occupant)))

    def __interaction(self, other, origin, tile, root):
        return other.interact_with(self.occupant, origin, tile, self.occupant.receive(other, origin, tile, root))
