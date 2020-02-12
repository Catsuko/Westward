class ShootAtAction:

    def __init__(self, target, action):
        self.target = target
        self.action = action

    def on(self, actor, tile, root):
        target = self.target.with_area(root)
        x, y = target.direction_to(tile)
        action = self
        if abs(x + y) is 1:
            root, action = self.action.redirect(x, y).on(actor, tile, root)
            action = ShootAtAction(self.target, action)
        return root, self


