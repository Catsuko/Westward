class BlockedTile:

    def __init__(self, x, y, occupant=None):
        self.x = x
        self.y = y
        self.occupant = occupant

    def enter(self, actor, origin):
        return origin

    def print_to(self, media):
        self.occupant.print_to(media)

    # How will a blocked tile revert back to an open tile?
    def update(self, area):
        if self.occupant is not None:
            self.occupant.act(area, self)
