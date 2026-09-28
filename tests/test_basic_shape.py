"""Test the BasicShape abstract base class and common interface."""

import unittest

from basic_shape import BasicShape
from circle import Circle
from rectangle import Rectangle


class TestBasicShape(unittest.TestCase):
    """Verify abstract-class behavior and inherited common properties."""

    def test_cannot_instantiate_basic_shape(self):
        with self.assertRaises(TypeError):
            BasicShape("Shape")

    def test_concrete_classes_inherit_interface(self):
        shapes = [Circle(0, 0, 2), Rectangle(3, 4)]
        for shape in shapes:
            self.assertIsInstance(shape, BasicShape)
            self.assertIsInstance(shape.name, str)
            self.assertGreater(shape.area, 0)

    def test_invalid_name_type_rejected(self):
        with self.assertRaises(TypeError):
            Circle(0, 0, 2, 123)

    def test_empty_name_rejected(self):
        with self.assertRaises(ValueError):
            Rectangle(3, 4, "   ")

    def test_area_is_read_only(self):
        circle = Circle(0, 0, 2)
        with self.assertRaises(AttributeError):
            circle.area = 50


if __name__ == "__main__":
    unittest.main()
