class FlickerShader:

    def __init__(self, shader, frequency_mod):
        self.shader = shader
        self.frequency_mod = frequency_mod

    def color(self, renderer, description, time):
        if time % self.frequency_mod == 0:
            self.shader.color(renderer, description, time)
