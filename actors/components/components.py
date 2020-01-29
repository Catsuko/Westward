class Components:

    def __init__(self, components=frozenset()):
        self.components = components

    def attempt(self, action, actor, root, *args):
        handler = next((getattr(c, action) for c in self.components if hasattr(c, action)), self.__swallow_attempt)
        return handler(actor, root, *args)

    def replace(self, old, new):
        return Components(self.components - frozenset([old]) | frozenset([new]))

    def __swallow_attempt(self, actor, root, *args):
        return root

