from actors.actions.action import Action


class StdinDrivenAction(Action):

    def __init__(self, key_map):
        self.key_map = key_map

    def on(self, actor, tile, root):
        key = None
        while key not in self.key_map.keys():
            key = input()
        return self.key_map[key].on(actor, tile, root), self
