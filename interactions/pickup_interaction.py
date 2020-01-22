class PickupInteraction:

    def __init__(self, item):
        self.item = item

    def between(self, initiator, origin, receiver, destination, root):
        return origin.enter(initiator.pick_up(self.item), origin, root)
