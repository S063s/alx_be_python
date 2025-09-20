first = 0
second = 0
number = first
number = second

operation = input("Enter operation (+/ -/ */ / /): ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

match operation:
    case "+":
        result = first + second
    case "-":
        result = first - second
    case "*":
        result = first * second
    case "/":
        result = first / second
    case _:
        result = None

if result is not None:
    print(f"The result is: {result}")
else:
    print("Invalid operation.")