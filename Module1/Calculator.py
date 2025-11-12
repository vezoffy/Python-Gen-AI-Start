choice = -1

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("You chose to add.")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 + num2
            print(f"The sum of {num1} and {num2} is {result}.")
        case 2:
            print("You chose to subtract.")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 - num2
            print(f"The difference of {num1} and {num2} is {result}.")
        case 3:
            print("You chose to multiply.")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 * num2
            print(f"The product of {num1} and {num2} is {result}.")
        case 4:
            print("You chose to divide.")
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            if num2 == 0:
                print("Error: Division by zero!")
            else:
                result = num1 / num2
                print(f"The quotient of {num1} and {num2} is {result}.")
        case 0:
            print("Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
