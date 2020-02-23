# TODO: When two bullets collide, they should destroy each other!
class Projectile:

    def __init__(self, velocity, key):
        self.velocity = velocity
        self.key = key

    def act(self, tile, root):
        destination = tile.neighbour(*self.velocity, root)
        root_without_projectile = tile.leave(self, root)
        origin = tile.neighbour(0, 0, root_without_projectile)
        return destination.enter(self, origin, root_without_projectile)

    def attempt(self, action, root, *args):
        return root

    def interact_with(self, other, origin, tile, root):
        return origin.leave(self, other.attempt("damage", root, tile))

    def receive(self, other, origin, tile, root):
        root = tile.find_in(tile.leave(self, root)).enter(other, origin, root)
        return self.interact_with(other, origin.find_in(root), tile.find_in(root), root)

    def identifies_with(self, key):
        return key is self.key

    def print_to(self, x, y, media):
        return media.with_actor(x, y, self.key)


