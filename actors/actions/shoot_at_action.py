from actors.actions.action import Action


class ShootAtAction(Action):

    def __init__(self, target, action):
        self.target = target
        self.action = action

    def on(self, actor, tile, root):
        target = self.target.with_area(root)
        x, y = target.direction_to(tile)
        if abs(x + y) == 1:
            root, _ = self.action.redirect(x, y).on(actor, tile, root)
        return root, self


