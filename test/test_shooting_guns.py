import unittest

from actors.actions.null_action import NullAction
from actors.actions.use_action import UseAction
from actors.actor import Actor
from actors.actor_query import ActorQuery
from actors.actor_target import ActorTarget
from actors.components.components import Components
from actors.components.health import Health
from actors.components.inventory import Inventory
from actors.interactions.null_interaction import NullInteraction
from actors.projectile import Projectile
from items.gun import Gun
from world.area_builder import AreaBuilder


class ShootingGunsTests(unittest.TestCase):

    def test_gun_can_be_aimed_up(self):
        bullet_source, bullet_query = self.__create_bullet_source()
        shooter = self.__create_shooter(Gun(bullet_source), (0, 1))
        area = AreaBuilder().rectangle(5, 5).with_actor(shooter, 2, 2).to_area()
        self.assertTrue(area.update().print_to(bullet_query).found_at(2, 4))

    def test_gun_can_be_aimed_down(self):
        bullet_source, bullet_query = self.__create_bullet_source()
        shooter = self.__create_shooter(Gun(bullet_source), (0, -1))
        area = AreaBuilder().rectangle(5, 5).with_actor(shooter, 2, 2).to_area()
        self.assertTrue(area.update().print_to(bullet_query).found_at(2, 0))

    def test_gun_can_be_aimed_right(self):
        bullet_source, bullet_query = self.__create_bullet_source()
        shooter = self.__create_shooter(Gun(bullet_source), (1, 0))
        area = AreaBuilder().rectangle(5, 5).with_actor(shooter, 2, 2).to_area()
        self.assertTrue(area.update().print_to(bullet_query).found_at(4, 2))

    def test_gun_can_be_aimed_left(self):
        bullet_source, bullet_query = self.__create_bullet_source()
        shooter = self.__create_shooter(Gun(bullet_source), (-1, 0))
        area = AreaBuilder().rectangle(5, 5).with_actor(shooter, 2, 2).to_area()
        self.assertTrue(area.update().print_to(bullet_query).found_at(0, 2))

    def test_gun_takes_a_turn_to_reload(self):
        bullet_source, bullet_query = self.__create_bullet_source()
        shooter = self.__create_shooter(Gun(bullet_source))
        area = AreaBuilder().rectangle(10, 1).with_actor(shooter, 0, 0).to_area()
        expected_shots = 2
        for _ in range(expected_shots * 2):
            area = area.update()
        self.assertEqual(expected_shots, area.print_to(bullet_query).match_count())

    def test_gun_reload_duration_can_be_made_slower(self):
        bullet_source, bullet_query = self.__create_bullet_source()
        reload_duration = 4
        shooter = self.__create_shooter(Gun(bullet_source, reload_duration))
        area = AreaBuilder().rectangle(10, 1).with_actor(shooter, 0, 0).to_area()
        for _ in range(reload_duration):
            area = area.update()
        self.assertEqual(1, area.print_to(bullet_query).match_count())

    def test_gun_can_be_fired_at_point_blank_range(self):
        bullet_source, _ = self.__create_bullet_source()
        shooter = self.__create_shooter(Gun(bullet_source))
        dummy_key = "d"
        health = Health(1, 1)
        dummy = Actor(NullAction(), NullInteraction(), dummy_key, Components(frozenset([health])))
        dummy_target = ActorTarget(dummy_key)
        area = AreaBuilder().rectangle(2, 1)\
                            .with_actor(shooter, 0, 0)\
                            .with_actor(dummy, 1, 0)\
                            .to_area()
        self.assertFalse(area.update().print_to(dummy_target).found())

    def __create_bullet_source(self):
        bullet_key = "*"
        return lambda aim_dir: Projectile(aim_dir, bullet_key), ActorQuery(lambda x, y, actor: actor[0] is bullet_key)

    def __create_shooter(self, gun, aim_dir=(1, 0)):
        inventory = Inventory(frozenset([gun]))
        shooter = Actor(UseAction(*aim_dir), NullInteraction(), "s", Components(frozenset([inventory])))
        return shooter


if __name__ == '__main__':
    unittest.main()
