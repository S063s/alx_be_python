import unittest
from simple_calculator import SimpleCalculator, add, subtract, multiply, divide

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.cal.add(2, 3), 5)
        self.assertEqual(self.cal.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.cal.subtract(5, 3), 2)
        self.assertEqual(self.cal.subtract(2, 2), 0)

    def test_multiplication(self):
        self.assertEqual(self.cal.multiply(2, 3), 6)
        self.assertEqual(self.cal.multiply(-1, 1), -1)

    def test_division(self):
        self.assertEqual(self.cal.divide(6, 3), 2)
        self.assertEqual(self.cal.divide(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            self.cal.divide(1, 0)

if __name__ == '__main__':
    unittest.main()
    
