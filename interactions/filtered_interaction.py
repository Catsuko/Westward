class FilteredInteraction:

    def __init__(self, interaction, allowed_keys=[]):
        self.interaction = interaction
        self.allowed_keys = allowed_keys

    def between(self, initiator, origin, receiver, destination, root):
        allowed = any([initiator.identifies_with(key) for key in self.allowed_keys])
        return self.interaction.between(initiator, origin, receiver, destination, root) if allowed else root
