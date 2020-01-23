class AcceptInitiatorInteraction:

    def between(self, initiator, origin, receiver, destination, root):
        return destination.find_in(destination.leave(receiver, root)).enter(initiator, origin, root)
