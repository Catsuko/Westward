class Health:

    def __init__(self, current, total):
        self.current = current
        self.total = total

    def update(self):
        return self

    def damage(self, actor, root, tile):
        health_left = Health(self.current - 1, self.total)
        return actor.replace(self, health_left, root) if health_left.alive() else tile.leave(actor, root)

    def heal(self, actor, root, tile):
        return actor.replace(self, Health(self.current + 1, self.total), root)

    def alive(self):
        return self.current > 0

