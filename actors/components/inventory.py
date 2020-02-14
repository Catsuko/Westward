class Inventory:

    def __init__(self, items=frozenset()):
        self.items = items

    def use_primary(self, actor, root, target, tile):
        if len(self.items) is 0:
            return root
        primary_item = next(iter(self.items))
        root, updated_item = primary_item.use(actor, tile, target, root)
        updated_items = [updated_item if item is primary_item else item for item in self.items]
        return actor.replace(self, Inventory(frozenset(updated_items)), root)
