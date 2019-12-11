class BlockedSpace:

    def enter(self, actor, origin, tile, world):
        return [origin]

    def leave(self, actor, tile, area):
        return []

    def update(self, tile, area):
        return []

    def print_to(self, x, y, media):
        return media.with_wall(x, y)
