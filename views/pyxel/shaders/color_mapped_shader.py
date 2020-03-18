class ColorMappedShader:

    def __init__(self, color_map):
        self.color_map = color_map

    def color(self, renderer, pos, key, time):
        renderer(self.color_map.color(key))
