"""Unit tests for Circle."""
import math
import unittest
from circle import Circle


class TestCircle(unittest.TestCase):
    def test_valid_circle(self):
        circle = Circle(0, 0, 4)
        self.assertEqual(circle.radius, 4)
        self.assertAlmostEqual(circle.area, math.pi * 16)

    def test_invalid_radius_values(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, 0)
        with self.assertRaises(ValueError):
            Circle(0, 0, -2)
        with self.assertRaises(TypeError):
            Circle(0, 0, "invalid")

    def test_radius_recalculates_area(self):
        circle = Circle(0, 0, 4)
        circle.radius = 8
        self.assertAlmostEqual(circle.area, math.pi * 64)

    def test_coordinates_do_not_change_area(self):
        circle = Circle(0, 0, 4)
        original_area = circle.area
        circle.x_center = -10
        circle.y_center = 15
        self.assertAlmostEqual(circle.area, original_area)

    def test_names(self):
        self.assertEqual(Circle(0, 0, 1).name, "Circle")
        self.assertEqual(Circle(0, 0, 1, "Wheel").name, "Wheel")


if __name__ == "__main__":
    unittest.main()
