class ChainedInteraction:

    def __init__(self, interactions):
        self.interactions = interactions

    def interact_with(self, actor, tile, other, origin, root):
        interactions = []
        result = root
        for interaction in self.interactions:
            result, updated_interaction = interaction.interact_with(actor, tile, other, origin, result)
            interactions << updated_interaction
        return result, ChainedInteraction(interactions)
