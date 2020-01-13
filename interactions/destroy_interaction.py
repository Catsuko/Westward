class DestroyInteraction:

    def between(self, initiator, origin, receiver, destination, root):
        return destination.leave(receiver, root)
