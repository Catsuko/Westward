import unittest

from actors.actions.move_action import MoveAction
from actors.actor import Actor
from actors.actor_query import ActorQuery
from actors.components.components import Components
from actors.interactions.null_interaction import NullInteraction
from world.area_builder import AreaBuilder


class ActorMovementTests(unittest.TestCase):

    def test_actor_moves_into_open_space(self):
        actor, actor_query = self.__create_actor_moving_in_direction((1, 0))
        area = AreaBuilder().rectangle(5, 5).with_actor(actor, 0, 0).to_area()
        self.assertTrue(area.update().print_to(actor_query).found_at(1, 0))

    def test_actor_cannot_move_out_of_bounds(self):
        actor, actor_query = self.__create_actor_moving_in_direction((-1, 0))
        area = AreaBuilder().rectangle(5, 5).with_actor(actor, 0, 0).to_area()
        self.assertTrue(area.update().print_to(actor_query).found_at(0, 0))

    def test_actor_cannot_move_into_another_actor(self):
        other_position = (1, 0)
        actor, actor_query = self.__create_actor_moving_in_direction(other_position)
        other_actor, _ = self.__create_actor_moving_in_direction((0, 0), "o")
        area = AreaBuilder().rectangle(5, 5).with_actor(actor, 0, 0).with_actor(other_actor, *other_position).to_area()
        self.assertTrue(area.update().print_to(actor_query).found_at(0, 0))

    def __create_actor_moving_in_direction(self, move_dir, key="d"):
        query = ActorQuery(lambda x, y, actor: actor[0] is key)
        return Actor(MoveAction(*move_dir), NullInteraction(), key, Components()), query


if __name__ == '__main__':
    unittest.main()
