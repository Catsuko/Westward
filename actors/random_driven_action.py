import random


class RandomDrivenAction:

    def __init__(self, actions=[]):
        self.actions = actions

    def on(self, actor, tile, root):
        return self.__on_random_action(actor, tile, root) if len(self.actions) > 0 else root

    def __on_random_action(self, actor, tile, root):
        return self.actions[random.randint(0, len(self.actions) - 1)].on(actor, tile, root)
