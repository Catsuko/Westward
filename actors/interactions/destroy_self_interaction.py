class DestroySelfInteraction:

    def interact_with(self, actor, tile, other, origin, root):
        return origin.leave(actor, root), self
