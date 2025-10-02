def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Division by zero error"
    return result

try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = safe_divide(numerator, denominator)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")

