size = int(input("Enter the size of the pattern: "))
symbol = input("Enter the symbol to use in the pattern: ")

for i in range(1, size + 1):
    j = 0
    while j in range(size - i):
        print(" ", end="")
        j += 1
    for k in range(i):
        print(symbol, end="")
    print()