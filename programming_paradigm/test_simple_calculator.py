import unittest
from simple_calculator import SimpleCalculator, add, subtract, multiply, divide

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add)
        self.assertEqual(self.calc.add)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract)
        self.assertEqual(self.calc.subtract)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply)
        self.assertEqual(self.calc.multiply)

    def test_division(self):
        self.assertEqual(self.calc.divide)
        self.assertEqual(self.calc.divide)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
    
