from py_compile import main


def perform_operation():
	print("Arithmetic Operations")
	num1 = float(input("Enter first number: "))
	num2 = float(input("Enter second number: "))
	operation = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()

	if operation == "add":
		result = num1 + num2
	elif operation == "subtract":
		result = num1 - num2
	elif operation == "multiply":
		result = num1 * num2
	elif operation == "divide":
		if num2 != 0:
			result = num1 / num2
		else:
			result = "Error: Division by zero is not allowed."
	else:
		result = "Invalid operation selected."

	print(f"The result is: {result}")
	
if __name__ == "__main__":
    main()
