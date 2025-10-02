def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Division by zero error"
    return result

try:
    num = float(input("numerator: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    

try:
    denom = float(input("denominator: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    
    