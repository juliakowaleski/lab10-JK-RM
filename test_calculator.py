#https://github.com/juliakowaleski/lab10-JK-RM.git

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

if __name__ == "__main__":
    unittest.main()