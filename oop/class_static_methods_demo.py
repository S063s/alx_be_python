class Calculator:
   calculation_type = "Arithmetic Operations"

   @staticmethod
   def add(a, b):
       return a + b

   @classmethod
   def subtract(cls, a, b):
    print(f"Calculation type: {cls.calculation_type}")
       return a - b

   @classmethod
   def multiply(cls, a, b):
       print(f"Calculation type: {cls.calculation_type}")
       return a * b
        

   @classmethod
   def divide(cls, a, b):
       if b != 0:
           return a / b
       return "Division by zero error"

