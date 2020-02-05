class Actor:

    def __init__(self, action, interaction, key, components):
        self.action = action
        self.interaction = interaction
        self.key = key
        self.components = components

    def act(self, tile, root):
        root, action = self.action.on(self, tile, root)
        return root.replace_actor(Actor(action, self.interaction, self.key, self.components))
    
    def interact_with(self, other, origin, tile, root):
        root, interaction = self.interaction.interact_with(self, origin, other, tile, root)
        return root.replace_actor(Actor(self.action, interaction, self.key, self.components))

    def receive(self, other, origin, tile, root):
        return root.with_area(origin)

    def replace(self, old, new, tile, root):
        updated_components = self.components.replace(old, new)
        return tile.replace_actor(Actor(self.action, self.interaction, self.key, updated_components), root)

    def attempt(self, action, root, *args):
        return self.components.attempt(action, self, root, *args)

    def print_to(self, x, y, media):
        return media.with_actor(x, y, self.key)

    def identifies_with(self, key):
        return self.key == key

    def __eq__(self, other):
        return isinstance(other, Actor) and other.identifies_with(self.key)

    def __str__(self):
        return "Actor %s" % self.key
