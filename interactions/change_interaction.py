class ChangeInteraction:

    def __init__(self, next_interaction):
        self.next_interaction = next_interaction

    def between(self, initiator, origin, receiver, destination, root):
        return destination.enter(receiver.with_interaction(self.next_interaction), destination, root)
