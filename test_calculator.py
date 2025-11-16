# https://github.com/juanroseroacosta-ufl/lab10-JR-RG
# Partner 1: Juan Rosero Acosta
# Partner 2: Rohan Grewal

import unittest
import math
from calculator import add, subtract, mul, div, logarithm, exp

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1),-2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(4, 7), 28)
        self.assertEqual(mul(9, -10), -90)
        self.assertEqual(mul(49, 30), 1470)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(7, 70), 10)
        self.assertAlmostEqual(div(7, -8), -1.14285714285714)
        self.assertEqual(div(2, 45), 22.5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(math.e, math.e ** 3), 3.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(10, -5)
        with self.assertRaises(ValueError):
            logarithm(10, 1)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 9), 9.486832980505138)
        self.assertAlmostEqual(hypotenuse(3, 3), 4.242640687119285)
        self.assertAlmostEqual(hypotenuse(9, 5), 10.295630140987)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-49)
        
        self.assertEqual(square_root(25), 5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
