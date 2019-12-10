class BlockedSpace:

    def enter(self, actor, origin, tile, area):
        return area.with_tiles([origin])

    def leave(self, actor, tile, area):
        return area

    def update(self, tile, area):
        return area

    def print_to(self, x, y, media):
        return media.with_wall(x, y)
