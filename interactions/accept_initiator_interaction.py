class AcceptInitiatorInteraction:

    def between(self, initiator, origin, receiver, destination, root):
        return destination.leave(receiver, root).find(destination).enter(initiator, origin, root)
