class Actor:

    def __init__(self, action, key, components):
        self.action = action
        self.key = key
        self.components = components

    def act(self, tile, root):
        return self.action.on(self, tile, root)
    
    def interact_with(self, other, origin, tile, root):
        return root

    def receive(self, other, origin, tile, root):
        return root.with_tile(origin)

    def replace(self, old, new, tile, root):
        return tile.enter(Actor(self.action, self.key, self.components.replace(old, new)), tile, root)

    def attempt(self, action, root, *args):
        return self.components.attempt(action, self, root, *args)

    def print_to(self, x, y, media):
        return media.with_actor(x, y, self.key)

    def identifies_with(self, key):
        return self.key == key

    def __eq__(self, other):
        return isinstance(other, Actor) and other.identifies_with(self.key)

    def __str__(self):
        return "Actor %s (Inventory: %d)" % (self.key, len(self.inventory))
