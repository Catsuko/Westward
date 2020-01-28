class Inventory:

    def __init__(self, items=frozenset()):
        self.items = items

    def pick_up(self, item, actor, tile, root):
        return actor.replace(self, Inventory(self.items | frozenset(item)), tile, root)

    def use_primary(self, actor, target, tile, root):
        items_iterator = iter(self.items)
        return next(items_iterator).use(actor, tile, target, root) if any(items_iterator) else root
