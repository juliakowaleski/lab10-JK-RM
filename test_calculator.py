# https://github.com/juliakowaleski/lab10-JK-RM.git

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2,3), 6)
        self.assertEqual(mul(-2,3), -6)
        self.assertEqual(mul(0, 3), 0)
        self.assertEqual(mul(-1, -3), 3)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,4), 2)
        self.assertEqual(div(2,10), 5)
        self.assertEqual(div(0, 30), 'Division by zero')


    def test_log_invalid_argument(self): # 1 assertion
        self.assertEqual(logarithm(0,1), 'logarithm failed')
        self.assertEqual(logarithm(10,1), 0)
        self.assertAlmostEqual(logarithm(5,10), 1.4306765580733933)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(5,12),13)
        self.assertEqual(hypotenuse(12,35), 37)


    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(-5), 'value error')
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(64), 8)


    def test_add(self):  # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(-1, 2), -3)
        self.assertEqual(subtract(0, 0), 0)


    def test_divide_by_zero(self):  # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        self.assertEqual(div(0, 5), "Division by zero")

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(10, 1), 0)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(4, 16), 2)

    def test_log_invalid_base(self):  # 1 assertion
        # use same technique from test_divide_by_zero
        self.assertEqual(logarithm(0, 1), "logarithm failed")


# Do not touch this
if __name__ == "__main__":
    unittest.main()

