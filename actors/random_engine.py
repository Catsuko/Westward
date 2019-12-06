import random


class RandomEngine:

    def pick_movement_direction(self, area, origin):
        magnitude = random.uniform(-1, 1)
        direction = random.randint(0, 1)
        return (magnitude, 0) if direction is 0 else (0, magnitude)