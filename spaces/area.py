class Area:

    def __init__(self, tiles=[]):
        self.tiles = tiles

    # Find the origin tile in the areas tiles and enter the actor.
    def enter(self, actor, origin):
        pass

    def print_to(self, media):
        [tile.print_to(media) for tile in self.tiles]

    def update(self):
        [tile.update(self) for tile in self.tiles]
