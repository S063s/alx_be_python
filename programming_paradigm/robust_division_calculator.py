def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except ValueError:
        return "Invalid input: Please provide numeric values."
    return result
