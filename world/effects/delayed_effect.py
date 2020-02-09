class DelayedEffect:

    def __init__(self, effect, delay_count):
        self.effect = effect
        self.delay_count = delay_count

    def affect(self, area):
        delay = max(0, self.delay_count - 1)
        return area.replace_effect(self, self.effect if delay is 0 else DelayedEffect(self.effect, delay))
