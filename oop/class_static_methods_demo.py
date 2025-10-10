class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @classmethod
    def multiply(cls, a, b):
        return a * b

    @classmethod
    def divide(cls, a, b):
        if b != 0:
            return a / b
        return "Division by zero error"


class CalculationType:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def is_odd(number):
        return number % 2 != 0

    @classmethod
    def is_positive(cls, number):
        return number > 0

    @classmethod
    def is_negative(cls, number):
        return number < 0        

