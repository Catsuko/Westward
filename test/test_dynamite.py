import unittest

from ddt import ddt, data

from actors.actions.damage_action import DamageAction
from actors.actions.delayed_action import DelayedAction
from actors.actions.null_action import NullAction
from actors.actor import Actor
from actors.actor_query import ActorQuery
from actors.components.components import Components
from actors.components.health import Health
from actors.interactions.null_interaction import NullInteraction
from actors.projectile import Projectile
from world.area_builder import AreaBuilder


@ddt
class DynamiteTests(unittest.TestCase):

    @data(1, 3, 5)
    def test_dynamite_does_not_detonate_before_delay(self, detonation_delay):
        dynamite = self.__create_dynamite(detonation_delay)
        area = AreaBuilder().rectangle(2, 2).with_actor(dynamite, 0, 0).to_area()
        for _ in range(detonation_delay):
            area = area.update()
        query = self.__create_query()
        self.assertTrue(area.print_to(query).found())

    @data(2, 4, 6)
    def test_dynamite_detonates_after_delay(self, detonation_delay):
        dynamite = self.__create_dynamite(detonation_delay)
        area = AreaBuilder().rectangle(2, 2).with_actor(dynamite, 0, 0).to_area()
        for _ in range(detonation_delay + 1):
            area = area.update()
        query = self.__create_query()
        self.assertFalse(area.print_to(query).found())

    @data((1, 2), (2, 1), (0, 2), (2, 0), (1, 1), (3, 3))
    def test_detonation_damages_nearby_actor(self, actor_position):
        dynamite = self.__create_dynamite(1, 2)
        nearby_actor = Actor(NullAction(), NullInteraction(), "n", Components(frozenset([Health(1, 1)])))
        area = AreaBuilder().rectangle(5, 5)\
                            .with_actor(dynamite, 2, 2)\
                            .with_actor(nearby_actor, *actor_position).to_area()
        self.assertFalse(area.update().update().print_to(self.__create_query()).found())

    @data((0, 0), (6, 6), (0, 3), (6, 3), (3, 0), (3, 6), (2, 1), (5, 4))
    def test_detonation_does_not_damage_outside_range(self, actor_position):
        dynamite = self.__create_dynamite(1, 2)
        actor_key = "n"
        nearby_actor = Actor(NullAction(), NullInteraction(), actor_key, Components(frozenset([Health(1, 1)])))
        area = AreaBuilder().rectangle(7, 7) \
            .with_actor(dynamite, 3, 3) \
            .with_actor(nearby_actor, *actor_position).to_area()
        query = self.__create_query(lambda x, y, actor: actor is actor_key)
        self.assertTrue(area.update().update().print_to(query).found())

    def test_dynamite_detonates_early_when_damaged(self):
        dynamite = self.__create_dynamite(5, 5)
        projectile = Projectile((1, 0), "*")
        area = AreaBuilder().rectangle(5, 5)\
                            .with_actor(projectile, 1, 2)\
                            .with_actor(dynamite, 2, 2)\
                            .to_area()
        self.assertFalse(area.update().print_to(self.__create_query()).found())

    def __create_query(self, matcher=lambda x, y, actor: True):
        return ActorQuery(matcher)

    def __create_dynamite(self, detonation_delay=3, detonation_range=3):
        action = DelayedAction(DamageAction(), detonation_delay)
        components = Components(frozenset([Health(1, 1)]))
        return Actor(action, NullInteraction(), "d", components)


if __name__ == '__main__':
    unittest.main()
