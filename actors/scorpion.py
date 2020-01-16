class Scorpion:

    def act(self, tile, root):
        # 1. Find the position of the target in this area
        #       - Print area (root) to a target location obj
        #       - later this target could be given a point camera
        #         to restrict vision!
        # 2. Move to the closest neighbouring tile
        # 3. Once the scorpion moves into the player, the interaction will perform an attack.
        #       - Will need to plan how damaging will work
        #           - will all actors implement take_damage?
        #           - will there be a messaging system
        pass

    def interact_with(self, actor, origin, tile, root):
        pass

    def print_to(self, x, y, media):
        pass

    def identifies_with(self, key):
        pass

    def matches(self, other_actor):
        pass

    def __str__(self):
        return "Scorpion"
