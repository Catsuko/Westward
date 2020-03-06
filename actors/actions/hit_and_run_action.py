import random


# TODO: Tidy this mess up. Refactor conditional behaviour and use a move action
class HitAndRunAction:

    def __init__(self, target, action, target_distance, run_duration, run_counter=0):
        self.target = target
        self.action = action
        self.target_distance = target_distance
        self.run_duration = run_duration
        self.run_counter = run_counter

    def on(self, actor, tile, root):
        action = self
        target_x, target_y = self.target.with_area(root).direction_to(tile, normalize=False)
        distance = abs(target_x) + abs(target_y)
        if self.run_counter == 0 and distance == self.target_distance:
            root, action = self.action.on(actor, tile, root)
            action = HitAndRunAction(self.target, action, self.target_distance, self.run_duration, self.run_duration)
        else:
            if self.run_counter > 0:
                action = self.__tick_run_counter()
            move_x, move_y = self.__pick_move_direction(target_x, target_y, distance)
            if move_x + move_y != 0:
                move_target = tile.neighbour(move_x, move_y, root)
                root = move_target.enter(actor, tile, tile.leave(actor, root))
        return root, action

    def __at_target_distance(self, x, y):
        return self.target_distance == abs(x) + abs(y)

    def __tick_run_counter(self):
        return HitAndRunAction(self.target, self.action, self.target_distance, self.run_duration, self.run_counter - 1)

    def __normalize(self, n):
        return max(-1, min(1, n))

    def __pick_move_direction(self, target_x, target_y, distance):
        move_along_x = target_y == 0 or (target_x != 0 and random.randint(0, 1) == 0)
        move_away = distance < self.target_distance or self.run_counter > 0
        if move_away:
            target_x = target_x * -1
            target_y = target_y * -1
        return (self.__normalize(target_x), 0) if move_along_x else (0, self.__normalize(target_y))



