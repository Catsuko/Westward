class AreaOfEffectAction:

    def __init__(self, radius=1):
        self.radius = radius

    def on(self, actor, tile, root):
        size = self.radius * 2 + 1
        for x in range(size):
            for y in range(size):
                x_offset = x - self.radius
                y_offset = y - self.radius
                if abs(x_offset) + abs(y_offset) <= self.radius:
                    root = tile.neighbour(x_offset, y_offset, root).attempt("damage", root)
        return root
