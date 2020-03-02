class DamageAction:

    def on(self, actor, tile, root):
        return actor.attempt("damage", root, tile), self
