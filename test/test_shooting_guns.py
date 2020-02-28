import unittest

from actors.actions.use_action import UseAction
from actors.actor import Actor
from actors.actor_query import ActorQuery
from actors.components.components import Components
from actors.components.inventory import Inventory
from actors.interactions.null_interaction import NullInteraction
from actors.projectile import Projectile
from items.gun import Gun
from world.area_builder import AreaBuilder


class ShootingGunsTests(unittest.TestCase):

    def test_gun_takes_a_turn_to_reload(self):
        shooter, bullet_query = self.__create_shooter()
        area = AreaBuilder().rectangle(10, 1).with_actor(shooter, 0, 0).to_area()
        expected_shots = 2
        for _ in range(expected_shots * 2):
            area = area.update()
        self.assertEqual(expected_shots, area.print_to(bullet_query).match_count())

    def __create_shooter(self):
        bullet_key = "*"
        gun = Gun(lambda aim_dir: Projectile(aim_dir, bullet_key))
        inventory = Inventory(frozenset([gun]))
        shooter = Actor(UseAction(1, 0), NullInteraction(), "s", Components(frozenset([inventory])))
        return shooter, ActorQuery(lambda x, y, actor: actor[0] is bullet_key)


if __name__ == '__main__':
    unittest.main()
