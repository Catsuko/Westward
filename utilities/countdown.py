class Countdown:

    def __init__(self, counter, duration):
        self.counter = counter
        self.duration = duration

    def is_finished(self):
        return self.counter == 0

    def tick(self):
        return self if self.is_finished() else Countdown(self.counter - 1, self.duration)

    def reset(self):
        return Countdown(self.duration, self.duration)
