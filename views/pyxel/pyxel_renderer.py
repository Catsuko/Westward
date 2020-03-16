import pyxel
import math



class PyxelRenderer:

    def __init__(self, offset, queued_rect, resolution, tiles=set(), actors=set(), effects=set()):
        self.offset = offset
        self.queued_rect = queued_rect
        self.tiles = tiles
        self.actors = actors
        self.effects = effects
        self.queued_tiles = set()
        self.queued_actors = set()
        self.queued_effects = set()

    def queue_actor(self, x, y, description):
        pass

    def queue_tile(self, x, y, description):
        pass

    def queue_effect(self, x, y, description):

    def next(self):
        x_offset = self.__center(self.queued_rect[0], self.queued_rect[1])
        y_offset = self.__center(self.queued_rect[2], self.queued_rect[3])
        return PyxelRenderer(self.queued_rect, (0, 0, 0, 0), self.queued_tiles, self.queued_actors, self.queued_tiles)

    def draw(self, x, y, color):
        pyxel.pset(x + self.h_margin, y + self.v_margin, color)

    def __updated_rect(self, x, y):
        self.queued_rect[0] = min(self.queued_rect[0], x)
        self.queued_rect[1] = max(self.queued_rect[1], x)
        self.queued_rect[2] = min(self.queued_rect[2], y)
        self.queued_rect[3] = max(self.queued_rect[3], y)

    def __center(self, a, b):
        return a + math.floor((b - a) * 0.5)
