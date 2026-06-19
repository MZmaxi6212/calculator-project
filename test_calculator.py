import unittest
from calculator import (
    addiere,
    subtrahiere,
    multipliziere,
    dividiere
)


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addiere(5, 3), 8)

    def test_subtraktion(self):
        self.assertEqual(subtrahiere(10, 4), 6)

    def test_multiplikation(self):
        self.assertEqual(multipliziere(2, 4), 8)

    def test_division(self):
        self.assertEqual(dividiere(12, 3), 4)

    def test_division_durch_null(self):
        with self.assertRaises(ValueError):
            dividiere(5, 0)


if __name__ == "__main__":
    unittest.main()