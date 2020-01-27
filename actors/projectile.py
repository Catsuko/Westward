class Projectile:

    def __init__(self, velocity, key):
        self.velocity = velocity
        self.key = key

    def act(self, tile, root):
        destination = tile.neighbour(*self.velocity, root)
        root_without_projectile = tile.leave(self, root)
        origin = tile.neighbour(0, 0, root_without_projectile)
        return destination.enter(self, origin, root_without_projectile)

    # TODO: Damage the other actor!
    def interact_with(self, other, origin, tile, root):
        return root

    def receive(self, other, origin, tile, root):
        return tile.find_in(tile.leave(self, root)).enter(other, origin, root)

    def print_to(self, x, y, media):
        return media.with_actor(x, y, self.key)

