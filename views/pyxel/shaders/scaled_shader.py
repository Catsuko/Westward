# TODO: Perlin noise ground textures
# TODO: Reduce size of actors
# TODO: Reduce size of bullets


class ScaledShader:

    def __init__(self, shader, resolution):
        self.shader = shader
        self.resolution = resolution
        self.scale = max(self.resolution) + 1

    def draw(self, x, y, description, time):
        for px in self.resolution:
            for py in self.resolution:
                self.shader.draw(12 + px + x * self.scale, 12 + py + y * self.scale, description, time)
