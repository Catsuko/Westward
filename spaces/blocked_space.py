class BlockedSpace:

    def enter(self, actor):
        return self

    def leave(self, actor):
        return self

    def update(self, area, tile):
        return []

    def print_to(self, x, y, media):
        return media.with_wall(x, y)