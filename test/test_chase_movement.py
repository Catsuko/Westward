import unittest

from actors.actions.chase_action import ChaseAction
from actors.actions.move_action import MoveAction
from actors.actions.null_action import NullAction
from actors.actions.staggered_action import StaggeredAction
from actors.actor import Actor
from actors.actor_target import ActorTarget
from actors.components.components import Components
from actors.interactions.null_interaction import NullInteraction
from actors.projectile import Projectile
from world.area_builder import AreaBuilder


class ChaseMovementTests(unittest.TestCase):

    def test_chases_target(self):
        dummy, dummy_target = self.__create_target()
        chaser, chaser_target = self.__create_chaser(dummy_target)
        area = AreaBuilder().rectangle(1, 10)\
                            .with_actor(chaser, 0, 0)\
                            .with_actor(dummy, 0, 9)\
                            .to_area()
        self.assertTrue(area.update().print_to(chaser_target).found_at(0, 1))

    def test_chases_target_slowly(self):
        dummy, dummy_target = self.__create_target()
        chaser_key = "c"
        slow_chase_action = StaggeredAction(ChaseAction(dummy_target, MoveAction()))
        chaser = Actor(slow_chase_action, NullInteraction(), chaser_key, Components())
        area = AreaBuilder().rectangle(1, 10)\
                            .with_actor(chaser, 0, 0)\
                            .with_actor(dummy, 0, 9)\
                            .to_area()
        self.assertTrue(area.update().update().print_to(ActorTarget(chaser_key)).found_at(0, 1))

    def test_stays_still_when_target_is_not_found(self):
        target = ActorTarget("?")
        chaser, chaser_target = self.__create_chaser(target)
        area = AreaBuilder().rectangle(3, 3).with_actor(chaser, 1, 1).to_area()
        self.assertTrue(area.update().print_to(chaser_target).found_at(1, 1))

    def test_moves_into_target_when_beside(self):
        dummy_key = "t"
        dummy = Projectile((0, 0), dummy_key)
        dummy_target = ActorTarget(dummy_key)
        chaser, chaser_target = self.__create_chaser(dummy_target)
        area = AreaBuilder().rectangle(3, 3).with_actor(chaser, 1, 0).with_actor(dummy, 1, 1).to_area()
        self.assertTrue(area.update().print_to(chaser_target).found_at(1, 1))

    def __create_target(self):
        target_key = "t"
        return Actor(NullAction(), NullInteraction(), target_key, Components()), ActorTarget(target_key)

    def __create_chaser(self, target):
        chaser_key = "c"
        chaser = Actor(ChaseAction(target, MoveAction()), NullInteraction(), chaser_key, Components())
        return chaser, ActorTarget(chaser_key)


if __name__ == '__main__':
    unittest.main()
