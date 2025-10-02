def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Division by zero error"
    except ValueError:
        return "Invalid input: Please provide numeric values."
    return result
