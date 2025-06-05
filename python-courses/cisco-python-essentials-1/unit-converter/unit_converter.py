def display_menu():
    print("\nUnit Converter Menu:")
    print("1. Length (meters <-> feet)")
    print("2. Weight (kilograms <-> pounds)")
    print("3. Temperature (Celsius <-> Fahrenheit)")
    print("4. Exit")

def length_converter():
    print("\nLength Conversion:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    choice = input("Choose conversion (1-2): ").strip()
    try:
        value = float(input("Enter the value: "))
        if choice == "1":
            print(f"{value} meters = {value * 3.28084:.2f} feet")
        elif choice == "2":
            print(f"{value} feet = {value / 3.28084:.2f} meters")
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter a valid number.")

def weight_converter():
    print("\nWeight Conversion:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    choice = input("Choose conversion (1-2): ").strip()
    try:
        value = float(input("Enter the value: "))
        if choice == "1":
            print(f"{value} kg = {value * 2.20462:.2f} lbs")
        elif choice == "2":
            print(f"{value} lbs = {value / 2.20462:.2f} kg")
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter a valid number.")

def temperature_converter():
    print("\nTemperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose conversion (1-2): ").strip()
    try:
        value = float(input("Enter the value: "))
        if choice == "1":
            print(f"{value}°C = {(value * 9/5) + 32:.2f}°F")
        elif choice == "2":
            print(f"{value}°F = {(value - 32) * 5/9:.2f}°C")
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
