import pyxel


class ColorMappedShader:

    def __init__(self, color_map):
        self.color_map = color_map

    def draw(self, x, y, description, time):
        pyxel.pset(x, y, self.color_map.color(description))
