class OccupiedSpace:

    def __init__(self, occupant):
        self.occupant = occupant

    def enter(self, actor, origin, tile, root):
        same_actor = actor.matches(self.occupant)
        return root.with_tile(tile.with_space(OccupiedSpace(actor))) if same_actor else self.occupant.interact_with(actor, origin, tile, root)

    def leave(self, actor, tile, root):
        from .open_space import OpenSpace
        return root.with_tile(tile.with_space(OpenSpace())) if actor.matches(self.occupant) else root

    def update(self, tile, root):
        return root.update_actor(self.occupant, root)

    def update_actor(self, actor, tile, root):
        return self.occupant.act(tile, root) if actor.matches(self.occupant) else root

    def print_to(self, x, y, media):
        return self.occupant.print_to(x, y, media)
