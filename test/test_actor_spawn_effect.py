import unittest

from actors.actions.null_action import NullAction
from actors.actor import Actor
from actors.actor_query import ActorQuery
from actors.components.components import Components
from actors.interactions.null_interaction import NullInteraction
from actors.projectile import Projectile
from world.area_builder import AreaBuilder
from world.effects.death_trigger_effect import DeathTriggerEffect
from world.effects.delayed_effect import DelayedEffect
from world.effects.spawn_effect import SpawnEffect


class ActorSpawnEffectTests(unittest.TestCase):

    def test_spawn_effect_adds_actor_to_area(self):
        dummy, dummy_query = self.__create_dummy()
        spawn_effect = SpawnEffect(dummy, [(0, 0)])
        area = AreaBuilder().rectangle(10, 10).to_area().with_effect(spawn_effect)
        self.assertTrue(area.update().print_to(dummy_query).found())

    def test_delayed_spawn_effect_does_not_spawn_on_first_update(self):
        dummy, dummy_query = self.__create_dummy()
        spawn_effect = SpawnEffect(dummy, [(0, 0)])
        delayed_spawn_effect = DelayedEffect(spawn_effect, 1)
        area = AreaBuilder().rectangle(10, 10).to_area().with_effect(delayed_spawn_effect)
        self.assertFalse(area.update().print_to(dummy_query).found())

    def test_delayed_spawn_effect_spawns_after_delay(self):
        dummy, dummy_query = self.__create_dummy()
        spawn_effect = SpawnEffect(dummy, [(0, 0)])
        delayed_spawn_effect = DelayedEffect(spawn_effect, 1)
        area = AreaBuilder().rectangle(10, 10).to_area().with_effect(delayed_spawn_effect)
        self.assertTrue(area.update().update().print_to(dummy_query).found())

    def test_death_effect_triggers_after_spawned_actor_has_been_removed(self):
        dummy, dummy_query = self.__create_dummy()
        spawn_effect = SpawnEffect(dummy, [(0, 0)])
        death_trigger_effect = DeathTriggerEffect(spawn_effect)
        first_spawn_effect = SpawnEffect(Projectile((0, -1), "*"), [(0, 0)], death_trigger_effect)
        area = AreaBuilder().rectangle(2, 2).to_area().with_effect(first_spawn_effect)
        area_with_first_spawn = area.update()
        area_with_first_spawn_updated = area_with_first_spawn.update()
        area_without_first_spawn = area_with_first_spawn_updated.update()
        area_with_death_trigger_spawn = area_without_first_spawn.update()
        self.assertTrue(area_with_death_trigger_spawn.print_to(dummy_query).found())


    def __create_dummy(self):
        key = "d"
        query = ActorQuery(lambda x, y, actor: actor[0] is key)
        return Actor(NullAction(), NullInteraction(), key, Components()), query

if __name__ == '__main__':
    unittest.main()
