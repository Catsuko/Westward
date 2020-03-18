import pyxel



class PyxelRenderer:

    def __init__(self, resolution, offset=(0, 0), queued_offset=None, tiles=set(), actors=set(), effects=set()):
        self.offset = offset
        self.queued_offset = queued_offset
        self.resolution = resolution
        self.scale = max(self.resolution) + 1
        self.tiles = tiles
        self.actors = actors
        self.effects = effects
        self.queued_tiles = set()
        self.queued_actors = set()
        self.queued_effects = set()

    def queue_actor(self, x, y, description):
        self.queued_actors.add((x, y, description))
        self.__take_min_coords(x, y)

    def queue_tile(self, x, y, description):
        self.queued_tiles.add((x, y, description))
        self.__take_min_coords(x, y)

    def queue_effect(self, x, y, description):
        self.queued_effects.add((x, y, description))
        self.__take_min_coords(x, y)

    def next(self):
        return PyxelRenderer(self.resolution, self.queued_offset, None, self.queued_tiles, self.queued_actors, self.queued_effects)

    def draw(self, tile_shader, effect_shader, actor_shader, time):
        pyxel.cls(col=0)
        for x, y, description in self.tiles:
            self.__draw(x, y, description, tile_shader, time)
        for x, y, description in self.effects:
            self.__draw(x, y, description, effect_shader, time)
        for x, y, description in self.actors:
            self.__draw(x, y, description, actor_shader, time)

    def __draw(self, x, y, description, shader, time):
        offset_x, offset_y = self.offset
        for px in self.resolution:
            for py in self.resolution:
                screen_x = 12 + px + (x * self.scale)
                screen_y = 12 + py + (y * self.scale)
                shader.color(lambda color: pyxel.pset(screen_x - (offset_x * self.scale), screen_y - (offset_y * self.scale), color), (x, y, screen_x, screen_y), description, time)

    def __take_min_coords(self, x, y):
        self.queued_offset = (x, y) if self.queued_offset is None else (min(self.queued_offset[0], x), min(self.queued_offset[1], y))

