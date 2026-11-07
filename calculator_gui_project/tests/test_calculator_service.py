import unittest
from services.calculator_service import CalculatorService, CalculatorError

class CalculatorServiceTests(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculatorService()

    def test_addition(self):
        self.assertEqual(self.calculator.calculate("2+3"), 5)

    def test_precedence_and_parentheses(self):
        self.assertEqual(self.calculator.calculate("(2+3)*4"), 20)

    def test_division(self):
        self.assertEqual(self.calculator.calculate("8/2"), 4)

    def test_division_by_zero(self):
        with self.assertRaises(CalculatorError):
            self.calculator.calculate("5/0")

    def test_rejects_unsupported_expression(self):
        with self.assertRaises(CalculatorError):
            self.calculator.calculate("__import__('os').system('whoami')")

if __name__ == "__main__":
    unittest.main()
