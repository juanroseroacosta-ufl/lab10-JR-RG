# https://github.com/juanroseroacosta-ufl/lab10-JR-RG
# Partner 1: Juan Rosero Acosta
# Partner 2: Rohan Grewal

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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