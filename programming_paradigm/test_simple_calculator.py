import unittest
from simple_calculator import SimpleCalculator, add, subtract, multiply, divide

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.cal.add)
        self.assertEqual(self.cal.add)

    def test_subtraction(self):
        self.assertEqual(self.cal.subtract)
        self.assertEqual(self.cal.subtract)

    def test_multiplication(self):
        self.assertEqual(self.cal.multiply)
        self.assertEqual(self.cal.multiply)

    def test_division(self):
        self.assertEqual(self.cal.divide)
        self.assertEqual(self.cal.divide)
        with self.assertRaises(ZeroDivisionError):
            self.cal.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
    
