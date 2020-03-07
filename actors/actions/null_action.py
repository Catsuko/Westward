from actors.actions.action import Action


class NullAction(Action):

    def on(self, actor, tile, root):
        return root, self
