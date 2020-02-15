class Components:

    def __init__(self, components=frozenset()):
        self.components = components

    def update(self):
        components = self
        for component in self.components:
            updated_component = component.update()
            if component is not updated_component:
                components = components.replace(component, updated_component)
        return components

    def attempt(self, action, actor, root, *args):
        handler = next((getattr(c, action) for c in self.components if hasattr(c, action)), self.__swallow_attempt)
        return handler(actor, root, *args)

    def replace(self, old, new):
        return Components(self.components - frozenset([old]) | frozenset([new]))

    def __swallow_attempt(self, actor, root, *args):
        return root
