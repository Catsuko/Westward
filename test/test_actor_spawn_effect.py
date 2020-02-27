import unittest

from actors.actions.null_action import NullAction
from actors.actor import Actor
from actors.actor_query import ActorQuery
from actors.actor_target import ActorTarget
from actors.components.components import Components
from actors.interactions.null_interaction import NullInteraction
from world.area_builder import AreaBuilder
from world.effects.spawn_effect import SpawnEffect


class ActorSpawnEffectTests(unittest.TestCase):

    def test_spawn_effect_adds_actor_to_area(self):
        dummy, dummy_query = self.__create_dummy()
        spawn_effect = SpawnEffect(dummy, [(0, 0)])
        area = AreaBuilder().rectangle(10, 10).to_area().with_effect(spawn_effect)
        self.assertTrue(area.update().print_to(dummy_query).found())

    def __create_dummy(self):
        key = "d"
        query = ActorQuery(lambda x, y, actor: actor[0] is key)
        return Actor(NullAction(), NullInteraction(), key, Components()), query

if __name__ == '__main__':
    unittest.main()
