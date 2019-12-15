class Actor:

    def __init__(self, engine, key="p", area_listener=None):
        self.key = key
        self.engine = engine
        self.area_listener = area_listener

    def act(self, tile, root):
        target_dir = self.engine.pick_movement_direction(tile, root)
        target = tile.neighbour(target_dir[0], target_dir[1], root)
        return target.enter(self, tile, tile.leave(self, root))

    def survey(self, area):
        if self.area_listener is not None:
            self.area_listener(area)

    def print_to(self, x, y, media):
        return media.with_actor(x, y, self.key)
