class ColorMappedShader:

    def __init__(self, color_map):
        self.color_map = color_map

    def color(self, renderer, description, time):
        _, _, key = description
        renderer(self.color_map.color(key))
