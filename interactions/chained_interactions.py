class ChainedInteractions:

    def __init__(self, interactions):
        self.interactions = interactions

    def between(self, initiator, origin, receiver, destination, root):
        for interaction in self.interactions:
            root = interaction.between(initiator, origin, receiver, destination, root)
        return root

