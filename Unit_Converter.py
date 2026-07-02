# unit_converter.py

def length_converter():
    print("\nLength Converter")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Miles to Kilometers")
    print("4. Kilometers to Miles")
    print("5. Feet to Meters")
    print("6. Meters to Feet")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} m = {value / 1000} km")
    elif choice == 2:
        print(f"{value} km = {value * 1000} m")
    elif choice == 3:
        print(f"{value} miles = {value * 1.60934:.4f} km")
    elif choice == 4:
        print(f"{value} km = {value / 1.60934:.4f} miles")
    elif choice == 5:
        print(f"{value} ft = {value * 0.3048:.4f} m")
    elif choice == 6:
        print(f"{value} m = {value / 0.3048:.4f} ft")
    else:
        print("Invalid choice")


def weight_converter():
    print("\nWeight Converter")
    print("1. Grams to Kilograms")
    print("2. Kilograms to Grams")
    print("3. Kilograms to Pounds")
    print("4. Pounds to Kilograms")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value} g = {value / 1000} kg")
    elif choice == 2:
        print(f"{value} kg = {value * 1000} g")
    elif choice == 3:
        print(f"{value} kg = {value * 2.20462:.4f} lb")
    elif choice == 4:
        print(f"{value} lb = {value / 2.20462:.4f} kg")
    else:
        print("Invalid choice")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = int(input("Enter your choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print(f"{value}°C = {(value * 9/5) + 32:.2f}°F")
    elif choice == 2:
        print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
    elif choice == 3:
        print(f"{value}°C = {value + 273.15:.2f} K")
    elif choice == 4:
        print(f"{value} K = {value - 273.15:.2f}°C")
    else:
        print("Invalid choice")


def main():
    while True:
        print("\n===== UNIT CONVERTER =====")
        print("1. Length Converter")
        print("2. Weight Converter")
        print("3. Temperature Converter")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Thank you for using Unit Converter!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()