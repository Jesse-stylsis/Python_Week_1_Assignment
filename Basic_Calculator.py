# Basic Calculator Program

def calculator():
    # Welcome message for the user
    print("Welcome to the Basic Calculator!")
    try:
        # Prompt the user to enter the first number and convert it to a float
        num1 = float(input("Enter the first number: "))
        
        # Prompt the user to input the mathematical operation
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Prompt the user to enter the second number and convert it to a float
        num2 = float(input("Enter the second number: "))
        
        # Perform the selected operation
        if operation == '+':
            # Addition
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            # Subtraction
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            # Multiplication
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            # Division
            if num2 != 0:
                # Ensure the denominator is not zero
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                # Handle division by zero
                print("Error: Division by zero is not allowed.")
        else:
            # Handle invalid operation input
            print("Invalid operation. Please choose +, -, *, or /.")
    except ValueError:
        # Handle non-numeric inputs
        print("Invalid input. Please enter numbers only.")

# Run the calculator function
calculator()
