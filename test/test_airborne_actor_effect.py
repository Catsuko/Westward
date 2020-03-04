import unittest

from actors.actions.null_action import NullAction
from actors.actor import Actor
from actors.actor_query import ActorQuery
from actors.components.components import Components
from actors.interactions.null_interaction import NullInteraction
from world.area_builder import AreaBuilder
from world.effects.airborne_actor_effect import AirborneActorEffect
from world.effects.effect_query import EffectQuery


class AirborneActorEffectTests(unittest.TestCase):

    def test_effect_adds_at_shadow_at_starting_position(self):
        area = self.__create_area_with_effect((1, 0), (1, 0), 5)
        effect_query = EffectQuery(lambda x, y, effect: effect is "shadow")
        self.assertTrue(area.print_to(effect_query).found_at(1, 0))

    def test_shadow_moves_towards_destination_as_area_updates(self):
        area = self.__create_area_with_effect((0, 0), (1, 0), 2)
        effect_query = EffectQuery(lambda x, y, effect: effect is "shadow")
        self.assertTrue(area.update().print_to(effect_query).found_at(1, 0))

    def test_effect_triggers_once_destination_has_been_reached(self):
        area = self.__create_area_with_effect((0, 0), (1, 0), 2)
        actor_query = ActorQuery(lambda x, y, actor: True)
        self.assertTrue(area.update().update().update().print_to(actor_query).found_at(2, 0))

    def __create_area_with_effect(self, start_position, direction, turns_airborne):
        actor = Actor(NullAction(), NullInteraction(), "d", Components())
        airborne_effect = AirborneActorEffect(actor, start_position, direction, turns_airborne)
        return AreaBuilder().rectangle(5, 5).to_area().with_effect(airborne_effect)


if __name__ == '__main__':
    unittest.main()
