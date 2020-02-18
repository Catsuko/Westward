import uuid


class Actor:

    def __init__(self, action, interaction, key, components):
        self.action = action
        self.interaction = interaction
        self.key = key
        self.components = components

    # TODO: Currently replacing the actor here is overriding potential changes made to the actor during the action.
    #       This is preventing items from being updated as their old selves are being put back into the world.
    def act(self, tile, root):
        root, action = self.action.on(self, tile, root)
        return root.update_actor(self, self.__replacer(Actor(action, self.interaction, self.key, self.components)))
    
    def interact_with(self, other, origin, tile, root):
        root, interaction = self.interaction.interact_with(self, origin, other, tile, root)
        return root.update_actor(self, self.__replacer(Actor(self.action, interaction, self.key, self.components)))

    def receive(self, other, origin, tile, root):
        return root.with_area(origin)

    def replace(self, old, new, root):
        components = self.components.replace(old, new)
        return root.update_actor(self, self.__replacer(Actor(self.action, self.interaction, self.key, components)))

    def attempt(self, action, root, *args):
        return self.components.attempt(action, self, root, *args)

    def print_to(self, x, y, media):
        return media.with_actor(x, y, self.key)

    def identifies_with(self, key):
        return self.key == key

    def unique(self):
        return Actor(self.action, self.interaction, self.key + str(uuid.uuid1()), self.components)

    def __replacer(self, actor_to_update):
        return lambda actor, tile, root: tile.find_in(tile.leave(actor, root)).enter(actor_to_update, tile, root)

    def __eq__(self, other):
        return isinstance(other, Actor) and other.identifies_with(self.key)

    def __str__(self):
        return "Actor %s" % self.key
