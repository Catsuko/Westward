class Action:

    def on(self, actor, tile, root):
        raise NotImplementedError

    def print_to(self, media):
        return media

