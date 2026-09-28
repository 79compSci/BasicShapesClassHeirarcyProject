"""Test runtime polymorphism through the BasicShape interface."""
import math
import unittest
from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle
from square import Square


class TestPolymorphism(unittest.TestCase):
    def test_common_shape_interface(self):
        shapes = [Circle(0, 0, 2), Rectangle(3, 4), Square(5)]
        expected_areas = [math.pi * 4, 12, 25]

        for shape, expected_area in zip(shapes, expected_areas):
            self.assertIsInstance(shape, BasicShape)
            self.assertIsInstance(shape.name, str)
            self.assertAlmostEqual(shape.area, expected_area)


if __name__ == "__main__":
    unittest.main()
