"""Unit tests for Rectangle."""
import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_valid_construction(self):
        rectangle = Rectangle(10, 20)
        self.assertEqual(rectangle.length, 10)
        self.assertEqual(rectangle.width, 20)
        self.assertEqual(rectangle.area, 200)

    def test_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 4)
        with self.assertRaises(ValueError):
            Rectangle(4, -1)
        with self.assertRaises(TypeError):
            Rectangle("four", 5)

    def test_length_recalculates_area(self):
        rectangle = Rectangle(10, 5)
        rectangle.length = 12
        self.assertEqual(rectangle.area, 60)

    def test_width_recalculates_area(self):
        rectangle = Rectangle(10, 5)
        rectangle.width = 8
        self.assertEqual(rectangle.area, 80)

    def test_failed_assignment_preserves_state(self):
        rectangle = Rectangle(10, 5)
        old_length = rectangle.length
        old_area = rectangle.area
        with self.assertRaises(ValueError):
            rectangle.length = -3
        self.assertEqual(rectangle.length, old_length)
        self.assertEqual(rectangle.area, old_area)


if __name__ == "__main__":
    unittest.main()
