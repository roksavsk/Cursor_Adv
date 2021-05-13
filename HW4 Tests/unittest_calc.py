# 1. Create tests for class Calculator (functions_to_test.py)
#     a. Using unittest lib
#     b. Using pytest lib
# 2.* Create tests for class Employee (employee.py) and mock response from "https://company.com"
from calc import Calculator
import unittest


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(5, 2), 7)
        self.assertEqual(Calculator.add(-7, -3), -10)
        self.assertEqual(Calculator.add(20.4, 0), 20.4)
        self.assertNotEqual(Calculator.add(5, 4), 0)
        self.assertNotEqual(Calculator.add(7, 33), 50)
        self.assertRaises(TypeError, Calculator.add, "a", 1)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(7, 3), 4)
        self.assertEqual(Calculator.subtract(2, 9), -7)
        self.assertEqual(Calculator.subtract(-5, 3), -8)
        self.assertNotEqual(Calculator.subtract(10, 20), 30)
        self.assertNotEqual(Calculator.subtract(10, 20), 30)
        self.assertRaises(TypeError, Calculator.subtract, 100, "c")

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(7, 5), 35)
        self.assertEqual(Calculator.multiply(9, 9), 81)
        self.assertEqual(Calculator.multiply(-5, 11), -55)
        self.assertNotEqual(Calculator.multiply(2, 2), 5)
        self.assertNotEqual(Calculator.multiply(22, 5), 100)
        self.assertRaises(TypeError, Calculator.multiply, "v", "x")

    def test_divide(self):
        self.assertEqual(Calculator.divide(9, 3), 3)
        self.assertEqual(Calculator.divide(99, 11), 9)
        self.assertEqual(Calculator.divide(100, -5), -20)
        self.assertNotEqual(Calculator.divide(2, 2), 5)
        self.assertNotEqual(Calculator.divide(22, 5), 100)
        self.assertRaises(ValueError, Calculator.divide, 5, 0)


if __name__ == '__main__':
    unittest.main()
