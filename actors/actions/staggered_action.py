from actors.actions.action import Action


class StaggeredAction(Action):

    def __init__(self, action, waiting=True):
        self.action = action
        self.waiting = waiting

    def on(self, actor, tile, root):
        action = self.action
        if not self.waiting:
            root, action = self.action.on(actor, tile, root)
        return root, StaggeredAction(action, not self.waiting)
