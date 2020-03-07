from actors.actions.action import Action


class DamageAction(Action):

    def on(self, actor, tile, root):
        return actor.attempt("damage", root, tile), self
