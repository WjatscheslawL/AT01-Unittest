import unittest

from main import add, subtract, multiply, divide
from main import check, divide_0, restfromdiv


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)


class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))
        self.assertTrue(not check(1))
        self.assertTrue(not check(3))
        self.assertTrue(not check(57))


class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(70, 2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide_0, 6, 0)

    def test_rest_from_divide(self):
        self.assertEqual(ValueError, restfromdiv(6, 4), 2)
        self.assertEqual(ValueError, restfromdiv(10, 3), 1)
        self.assertNotEqual(ValueError, restfromdiv(10, 3), 2)
        self.assertRaises(ValueError, restfromdiv(5, 0))


if __name__ == '__main__':
    unittest.main()
