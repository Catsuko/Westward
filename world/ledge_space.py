class LedgeSpace:

    def __init__(self, allowed_direction):
        self.allowed_direction = allowed_direction

    def enter(self, actor, origin, tile, root):
        move = origin.to(tile)
        allowed = move == self.allowed_direction
        return tile.neighbour(*move, root).enter(actor, origin, root) if allowed else root.with_area(origin)

    def leave(self, actor, tile, root):
        return root

    def update(self, tile, root):
        return root

    def update_actor(self, actor, update_delegate, tile, root):
        return root

    def attempt(self, action, root, *args):
        return root

    def print_to(self, x, y, media):
        return media.with_ledge(x, y)
