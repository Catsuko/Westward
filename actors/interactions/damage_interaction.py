class DamageInteraction:

    def interact_with(self, actor, origin, other, tile, root):
        return other.attempt("damage", root, tile), self
