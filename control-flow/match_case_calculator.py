first = 0
second = 0
number = first
number = second

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
operation = input("Choose the operation (+ , - , * , /): ")

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