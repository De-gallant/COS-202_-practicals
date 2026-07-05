# MATHEMATICAL CALCULATOR (MC)

print("=" * 40)
print("     MATHEMATICAL CALCULATOR (MC)")
print("=" * 40)

while True:
    print("\nSelect an Operation:")
    print("+  : Addition")
    print("-  : Subtraction")
    print("*  : Multiplication")
    print("/  : Division")
    print("\\  : Floor Division")
    print("^  : Power")
    print("%  : Modulus")
    print("C  : Clear Screen")
    print("OFF: Exit Calculator")

    choice = input("\nEnter your choice: ").upper()

    if choice == "OFF":
        print("\nCalculator is now OFF.")
        break

    elif choice == "C":
        print("\n" * 50)
        print("Calculator Cleared!")
        continue

    elif choice in ["+", "-", "*", "/", "\\", "^", "%"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "+":
                result = num1 + num2

            elif choice == "-":
                result = num1 - num2

            elif choice == "*":
                result = num1 * num2

            elif choice == "/":
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                    continue
                result = num1 / num2

            elif choice == "\\":
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                    continue
                result = num1 // num2

            elif choice == "^":
                result = num1 ** num2

            elif choice == "%":
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                    continue
                result = num1 % num2

            print(f"\nResult = {result}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    else:
        print("Invalid operation! Please try again.")