from .blocked_tile import BlockedTile


class OpenTile:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def enter(self, actor, origin):
        return BlockedTile(self.x, self.y, actor)

    def print_to(self, media):
        media.print_space("open")

    def update(self, area):
        pass
