class ChaseAction:

    def __init__(self, target, movement):
        self.target = target
        self.movement = movement

    def on(self, actor, tile, root):
        target = self.target.with_area(root)
        x, y = target.direction_to(tile)
        if x is not 0 and y is not 0:
            y = 0
        root, action = self.movement.redirect(x, y).on(actor, tile, root)
        return root, ChaseAction(self.target, action)
