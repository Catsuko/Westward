import pyxel


class BlockDrawStrategy:

    def __init__(self, resolution, env):
        self.resolution = resolution
        self.scale = max(self.resolution) + 1
        self.env = env

    def draw(self, x, y, description, time):
        color = self.env.color(description)
        for px in self.resolution:
            for py in self.resolution:
                pyxel.pset(12 + px + x * self.scale, 12 + py + y * self.scale, color)
