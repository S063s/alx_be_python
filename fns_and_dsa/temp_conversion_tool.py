FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 #for F to C
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 #for C to F

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Temperature Conversion Tool")
    choice = input("is the temperature in Fahrenheit or Celsius? (F/C): ").strip().upper()
    if choice == 'F':
        fahrenheit = float(input("Enter the temperature to convert in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
    elif choice == 'C':
        celsius = float(input("Enter the temperature to convert in Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    else:
        print("Invalid choice. Please select F or C.")

if __name__ == "__main__":
    main()