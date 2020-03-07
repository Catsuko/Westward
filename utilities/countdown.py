class Countdown:

    def __init__(self, duration, counter=None):
        self.duration = duration
        self.counter = duration if counter is None else counter

    def is_finished(self):
        return self.counter == 0

    def tick(self):
        return self if self.is_finished() else Countdown(self.duration, self.counter - 1)

    def reset(self):
        return Countdown(self.duration, self.duration)
