from menu import print_show
from operations import add, subtract, multiply, divide


def get_two_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numbers only.")


while True:

    print_show()

    choice = input("Enter your choice: ")

    if choice == "1":
        num1, num2 = get_two_numbers()
        result = add(num1, num2)
        print(f"The result of adding {num1} and {num2} is {result}")

    elif choice == "2":
        num1, num2 = get_two_numbers()
        result = subtract(num1, num2)
        print(f"The result of subtracting {num2} from {num1} is {result}")

    elif choice == "3":
        num1, num2 = get_two_numbers()
        result = multiply(num1, num2)
        print(f"The result of multiplying {num1} and {num2} is {result}")

    elif choice == "4":
        num1, num2 = get_two_numbers()
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = divide(num1, num2)
            print(f"The result of dividing {num1} by {num2} is {result}")

    elif choice == "5":
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice.")
        continue

    again = input("\nDo you want another calculation? (yes/no): ").lower()

    if again == "no":
        print("Thank you for using the calculator!")
        break