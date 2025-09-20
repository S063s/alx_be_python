length = int(input("Enter the length of the pattern: "))
symbol = input("Enter the symbol to use in the pattern: ")

for i in range(1, length + 1):
    for j in range(length - i):
        print(" ", end="")
    for k in range(i):
        print(symbol, end="")
    print()
    