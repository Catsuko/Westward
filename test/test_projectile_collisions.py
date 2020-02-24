import unittest

from actors.actor_target import ActorTarget
from actors.projectile import Projectile
from world.area_builder import AreaBuilder


class MyTestCase(unittest.TestCase):

    def test_two_projectiles_destroy_each_other(self):
        key = "*"
        right_projectile = Projectile((-1, 0), key)
        left_projectile = Projectile((1, 0), key)
        area = AreaBuilder().rectangle(10, 10)\
                            .with_actor(right_projectile, 5, 5)\
                            .with_actor(left_projectile, 4, 5)\
                            .to_area()
        area = area.update()
        self.assertFalse(area.print_to(ActorTarget(key)).found(), "Both projectiles were not destroyed.")


if __name__ == '__main__':
    unittest.main()
