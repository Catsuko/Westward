class Actor:

    def __init__(self, engine, key="@", area_listener=None):
        self.key = key
        self.engine = engine
        self.area_listener = area_listener

    def act(self, tile, area):
        target_dir = self.engine.pick_movement_direction(area, tile)
        target = tile.neighbour(area, target_dir[0], target_dir[1])
        return target.enter(self, tile, tile.leave(self, area))

    def survey(self, area):
        if self.area_listener is not None:
            self.area_listener(area)

    def print_to(self, x, y, media):
        return media.with_character(x, y, self.key)
