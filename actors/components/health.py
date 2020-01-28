class Health:

    def __init__(self, current=1, total=1):
        self.current = current
        self.total = total

    def damage(self, actor, tile, root):
        health_left = Health(self.current - 1, self.total)
        return actor.replace(self, health_left, tile, root) if health_left.alive() else tile.leave(actor, root)

    def heal(self, actor, tile, root):
        return actor.replace(self, Health(self.current + 1, self.total), tile, root)

    def alive(self):
        return self.current > 0

