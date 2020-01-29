class Inventory:

    def __init__(self, items=frozenset()):
        self.items = items

    def pick_up(self, actor, root, item, tile):
        return actor.replace(self, Inventory(self.items | frozenset(item)), tile, root)

    def use_primary(self, actor, root, target, tile):
        items_iterator = iter(self.items)
        return root if len(self.items) is 0 else next(items_iterator).use(actor, tile, target, root)
