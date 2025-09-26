FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Temperature Conversion Tool")
    choice = input("Convert from (1) Fahrenheit to Celsius or (2) Celsius to Fahrenheit? Enter 1 or 2: ").strip()
    if choice == '1':
        fahrenheit = float(input("Enter the temperature to convert in Fahrenheit: "))
        celsius = FAHRENHEIT_TO_CELSIUS_FACTOR(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
    elif choice == '2':
        celsius = float(input("Enter the temperature to convert in Celsius: "))
        fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    else:
        print("Invalid choice. Please select 1 or 2.")