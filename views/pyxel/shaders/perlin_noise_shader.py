import noise
import numpy as np


class PerlinNoiseShader:

    # TODO: Refactor noise out of this shader, instead pass in noise pre-generated.
    def __init__(self, noise_size=256, noise_scale=500.0, grass_threshold=0.05):
        shape = (noise_size, noise_size)
        octaves = 6
        persistence = 0.5
        lacunarity = 2.0
        self.grass_threshold = grass_threshold
        self.noise_scale = noise_size
        self.noise = np.zeros(shape)
        for i in range(shape[0]):
            for j in range(shape[1]):
                self.noise[i][j] = noise.pnoise2(i / noise_scale,
                                                 j / noise_scale,
                                                 octaves=octaves,
                                                 persistence=persistence,
                                                 lacunarity=lacunarity,
                                                 repeatx=noise_size,
                                                 repeaty=noise_size,
                                                 base=0)

    def color(self, renderer, position, description, time):
        x, y, screen_x, screen_y = position
        nx = screen_x % self.noise_scale
        ny = screen_y % self.noise_scale
        color = 15
        if self.noise[nx][ny] < self.grass_threshold:
            color = 11
        elif self.noise[nx][ny] < self.grass_threshold + 0.01:
            color = 9
        renderer(color)
