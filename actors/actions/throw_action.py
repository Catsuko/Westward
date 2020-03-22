from actors.actions.action import Action


class ThrowAction(Action):

    def __init__(self, target, effect):
        self.target = target
        self.effect = effect

    def on(self, actor, tile, root):
        return root.with_effect(self.effect.starting_from(tile, self.target.with_area(root))), self
