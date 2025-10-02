def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Division by zero error"
    return result

try:
    numerator = float(input("numerator: "))
    denominator = float(input("denominator: "))
    result = safe_divide(numerator, denominator)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")

