import random


class RandomEngine:

    def pick_movement_direction(self, origin, world):
        move_vertically = random.randint(0, 1)
        direction = random.randint(0, 1) * 2 - 1
        return (0, direction) if move_vertically is 0 else (direction, 0)
