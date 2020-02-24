import unittest

from world.area import Area
from world.area_builder import AreaBuilder
from world.open_space import OpenSpace
from world.tile import Tile


class AreaBoundsTests(unittest.TestCase):

    def test_area_surrounds_point_in_tiles(self):
        x, y = (3, 3)
        area = AreaBuilder().rectangle(10, 10).reposition(x, y).to_area()
        self.assertTrue(area.surrounds(x, y))

    def test_area_surrounds_point_with_single_tile(self):
        x, y = (2, 5)
        area = AreaBuilder().reposition(x, y).rectangle(1, 1).to_area()
        self.assertTrue(area.surrounds(x, y))

    def test_area_surrounds_point_in_sub_areas(self):
        x, y = (10, 10)
        root = Area([
            AreaBuilder().rectangle(5, 5).to_area(),
            AreaBuilder().reposition(x, y).rectangle(5, 5).to_area()
        ])
        self.assertTrue(root.surrounds(x, y))

    def test_area_does_not_surround_point_outside_tiles(self):
        x, y = (3, 3)
        area = AreaBuilder().rectangle(2, 2).reposition(-x, -y).to_area()
        self.assertFalse(area.surrounds(x, y))

    def test_area_is_enclosed_by_itself(self):
        area = AreaBuilder().rectangle(5, 5).to_area()
        self.assertTrue(area.enclosed_by(area))

    def test_area_with_single_tile_is_enclosed_by_tile(self):
        tile = Tile(10, 10, OpenSpace())
        area = Area([tile])
        self.assertTrue(area.enclosed_by(tile))

    def test_area_is_enclosed_by_larger_area(self):
        smaller_area = AreaBuilder().rectangle(2, 2).to_area()
        larger_area = AreaBuilder().rectangle(10, 10).to_area()
        self.assertTrue(smaller_area.enclosed_by(larger_area))

    def test_area_is_not_enclosed_by_smaller_area(self):
        smaller_area = AreaBuilder().rectangle(2, 2).to_area()
        larger_area = AreaBuilder().rectangle(10, 10).to_area()
        self.assertFalse(larger_area.enclosed_by(smaller_area))

    def test_area_with_multiple_tiles_is_not_enclosed_by_single_tile(self):
        tile = Tile(2, 2, OpenSpace())
        area = AreaBuilder().rectangle(10, 10).to_area()
        self.assertFalse(area.enclosed_by(tile))


if __name__ == '__main__':
    unittest.main()
