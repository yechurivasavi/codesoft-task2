def calculator():
    print("Welcome to the Simple Calculator!")

    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    print("\nSelect operation:")
    print(" +  Addition")
    print(" -  Subtraction")
    print(" *  Multiplication")
    print(" /  Division")

    operation = input("Enter operation (+, -, *, /): ")

    # Perform calculation
    if operation == '+':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid operation selected.")

# Run the calculator
calculator()
