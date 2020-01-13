class ReturnInitiatorInteraction:

    def between(self, initiator, origin, receiver, destination, root):
        return root.with_tile(origin)
