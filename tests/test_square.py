"""Unit tests for Square and its dimension invariant."""
import unittest
from square import Square


class TestSquare(unittest.TestCase):
    def test_valid_construction(self):
        square = Square(5)
        self.assertEqual(square.side, 5)
        self.assertEqual(square.length, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.area, 25)

    def test_side_change_preserves_invariant(self):
        square = Square(5)
        square.side = 8
        self.assertEqual(square.side, 8)
        self.assertEqual(square.length, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.area, 64)

    def test_length_change_preserves_invariant(self):
        square = Square(5)
        square.length = 7
        self.assertEqual(square.side, 7)
        self.assertEqual(square.length, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.area, 49)

    def test_width_change_preserves_invariant(self):
        square = Square(5)
        square.width = 9
        self.assertEqual(square.side, 9)
        self.assertEqual(square.length, 9)
        self.assertEqual(square.width, 9)
        self.assertEqual(square.area, 81)

    def test_invalid_side_values(self):
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-2)
        with self.assertRaises(TypeError):
            Square("five")

    def test_failed_assignment_preserves_state(self):
        square = Square(5)
        with self.assertRaises(ValueError):
            square.side = -1
        self.assertEqual((square.side, square.length, square.width, square.area), (5, 5, 5, 25))


if __name__ == "__main__":
    unittest.main()
