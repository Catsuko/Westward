class FlickerShader:

    def __init__(self, shader, frequency_mod):
        self.shader = shader
        self.frequency_mod = frequency_mod

    def draw(self, x, y, description, time):
        if time % self.frequency_mod == 0:
            self.strategy.draw(x, y, description, time)
