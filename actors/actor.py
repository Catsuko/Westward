class Actor:

    def __init__(self, action, interaction, key, inventory=[]):
        self.action = action
        self.interaction = interaction
        self.key = key
        self.inventory = inventory

    def act(self, tile, root):
        return self.action.on(self, tile, root)
    
    def interact_with(self, actor, origin, tile, root):
        return self.interaction.between(actor, origin, self, tile, root)

    def pick_up(self, item, tile, root):
        return tile.enter(self.__with_item(item), tile, root)

    def with_interaction(self, interaction):
        return Actor(self.action, interaction, self.key, self.inventory)

    def use(self, tile, target, root):
        return self.inventory[0].use(self, tile, target, root) if len(self.inventory) > 0 else root

    def print_to(self, x, y, media):
        return media.with_actor(x, y, self.key)

    def identifies_with(self, key):
        return self.key == key

    # TODO: Refactor into an equality override.
    def matches(self, other_actor):
        return other_actor.identifies_with(self.key)

    def __with_item(self, item):
        return Actor(self.action, self.interaction, self.key, self.inventory + [item])

    def __str__(self):
        return "Actor %s (Inventory: %d)" % (self.key, len(self.inventory))
