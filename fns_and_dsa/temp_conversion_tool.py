def fahrenheit_to_celsius_factor(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit_factor(celsius):
    return (celsius * 9/5) + 32

def main():
    print("Temperature Conversion Tool")
    choice = input("Convert from (1) Fahrenheit to Celsius or (2) Celsius to Fahrenheit? Enter 1 or 2: ").strip()
    if choice == '1':
        fahrenheit = float(input("Enter the temperature to convert in Fahrenheit: "))
        celsius = fahrenheit_to_celsius_factor(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C")
    elif choice == '2':
        celsius = float(input("Enter the temperature to convert in Celsius: "))
        fahrenheit = celsius_to_fahrenheit_factor(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F")
    else:
        print("Invalid choice. Please select 1 or 2.")