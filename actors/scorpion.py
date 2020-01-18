class Scorpion:

    def __init__(self, target, movement):
        self.target = target
        self.movement = movement

    def act(self, tile, root):
        updated_target = self.target.with_area(root)
        target_direction = updated_target.direction_to(tile)
        if target_direction[0] is not 0 and target_direction[1] is not 0:
            target_direction = (target_direction[0], 0)
        return self.movement.redirect(*target_direction).on(self, tile, root)

    def interact_with(self, actor, origin, tile, root):
        return root.with_tile(origin)

    def print_to(self, x, y, media):
        return media.with_actor(x, y, "s")

    def identifies_with(self, key):
        return key == "s"

    def matches(self, other_actor):
        return other_actor.identifies_with("s")

    def __str__(self):
        return "Scorpion"
