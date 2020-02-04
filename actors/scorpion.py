class Scorpion:

    def __init__(self, target, movement, components, waiting=True):
        self.target = target
        self.movement = movement
        self.components = components
        self.waiting = waiting

    def act(self, tile, root):
        wait_flipped_scorpion = Scorpion(self.target, self.movement, self.components, not self.waiting)
        root = tile.replace_actor(wait_flipped_scorpion, root)
        if not self.waiting:
            target = self.target.with_area(root)
            target_direction = target.direction_to(tile)
            if target_direction[0] is not 0 and target_direction[1] is not 0:
                target_direction = (target_direction[0], 0)
            root = self.movement.redirect(*target_direction).on(wait_flipped_scorpion, tile.find_in(root), root)
        return root

    def interact_with(self, other, origin, tile, root):
        return other.attempt("damage", root, tile)

    def replace(self, old, new, tile, root):
        updated = Scorpion(self.target, self.movement, self.components.replace(old, new), self.waiting)
        return tile.replace_actor(updated, root)

    def attempt(self, action, root, *args):
        return self.components.attempt(action, self, root, *args)

    def receive(self, other, origin, tile, root):
        return root.with_tile(origin)

    def print_to(self, x, y, media):
        return media.with_actor(x, y, "s")

    def identifies_with(self, key):
        return key == "s"

    def matches(self, other_actor):
        return other_actor.identifies_with("s")

    def __eq__(self, other):
        return isinstance(other, Scorpion)

    def __str__(self):
        return "Scorpion"
