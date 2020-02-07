class MappedInteraction:

    def __init__(self, lookup, default_interaction):
        self.lookup = lookup
        self.default_interaction = default_interaction

    def interact_with(self, actor, tile, other, origin, root):
        root, _ = other.print_to(0, 0, self).interact_with(actor, tile, other, origin, root)
        return root, self

    # TODO: Make actor key a descriptive object that encapsulates the actor's UUID
    def with_actor(self, x, y, key):
        key = key[0]
        return self.lookup[key] if key in self.lookup else self.default_interaction
