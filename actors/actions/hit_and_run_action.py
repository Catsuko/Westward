from actors.actions.action import Action
import random


# TODO: Tidy this mess up. Refactor conditional behaviour and use a move action
class HitAndRunAction(Action):

    def __init__(self, target, action, movement, target_distance, run_countdown):
        self.target = target
        self.action = action
        self.movement = movement
        self.target_distance = target_distance
        self.run_countdown = run_countdown

    def on(self, actor, tile, root):
        target_x, target_y = self.target.with_area(root).direction_to(tile, normalize=False)
        distance = abs(target_x) + abs(target_y)
        if self.run_countdown.is_finished() and distance == self.target_distance:
            root, action = self.action.on(actor, tile, root)
            countdown = self.run_countdown.reset()
            action = HitAndRunAction(self.target, action, self.movement, self.target_distance, countdown)
        else:
            countdown = self.run_countdown.tick()
            action = HitAndRunAction(self.target, self.action, self.movement, self.target_distance, countdown)
            move_x, move_y = self.__pick_move_direction(target_x, target_y, distance)
            root, _ = self.movement.redirect(move_x, move_y).on(actor, tile, root)
        return root, action

    def __at_target_distance(self, x, y):
        return self.target_distance == abs(x) + abs(y)

    def __normalize(self, n):
        return max(-1, min(1, n))

    def __pick_move_direction(self, target_x, target_y, distance):
        move_along_x = target_y == 0 or (target_x != 0 and random.randint(0, 1) == 0)
        move_away = distance < self.target_distance or (not self.run_countdown.is_finished())
        if move_away:
            target_x = target_x * -1
            target_y = target_y * -1
        return (self.__normalize(target_x), 0) if move_along_x else (0, self.__normalize(target_y))
