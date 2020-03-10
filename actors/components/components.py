from actors.components.component import Component
from functools import reduce


class Components(Component):

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

    def print_to(self, x, y, media):
        return reduce(lambda m, c: c.print_to(x, y, media), self.components, media)

    def __swallow_attempt(self, actor, root, *args):
        return root
