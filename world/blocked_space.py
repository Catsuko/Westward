class BlockedSpace:

    def enter(self, actor, origin, tile, root):
        return root.with_area(origin)

    def leave(self, actor, tile, root):
        return root

    def update(self, tile, root):
        return root

    def update_actor(self, actor, tile, root):
        return root

    def replace_actor(self, actor, tile, root):
        return root

    def print_to(self, x, y, media):
        return media.with_wall(x, y)
