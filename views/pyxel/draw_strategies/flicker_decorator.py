class FlickerDecorator:

    def __init__(self, strategy, frequency_mod):
        self.strategy = strategy
        self.frequency_mod = frequency_mod

    def draw(self, x, y, description, time):
        if time % self.frequency_mod == 0:
            self.strategy.draw(x, y, description, time)
