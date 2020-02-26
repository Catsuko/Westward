import unittest

from actors.actions.chase_action import ChaseAction
from actors.actions.move_action import MoveAction
from actors.actions.null_action import NullAction
from actors.actions.staggered_action import StaggeredAction
from actors.actor import Actor
from actors.actor_target import ActorTarget
from actors.components.components import Components
from actors.interactions.null_interaction import NullInteraction
from world.area_builder import AreaBuilder


class MyTestCase(unittest.TestCase):

    def test_chases_target(self):
        dummy, dummy_target = self.__create_target()
        chaser_key = "c"
        chaser = Actor(ChaseAction(dummy_target, MoveAction()), NullInteraction(), chaser_key, Components())
        area = AreaBuilder().rectangle(1, 10)\
                            .with_actor(chaser, 0, 0)\
                            .with_actor(dummy, 0, 9)\
                            .to_area()
        self.assertTrue(area.update().print_to(ActorTarget(chaser_key)).found_at(0, 1))

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

    def __create_target(self):
        target_key = "t"
        return Actor(NullAction(), NullInteraction(), target_key, Components()), ActorTarget(target_key)


if __name__ == '__main__':
    unittest.main()
