# Project: Simple Calculator
# Objective: Create a simple calculator that performs basic arithmetic operations (addition, subtraction, multiplication, and division) based on user input.

# Requirements:

# Prompt the user to enter two numbers.
# Prompt the user to choose an arithmetic operation (addition, subtraction, multiplication, or division).
# Perform the chosen operation on the two numbers.
# Display the result to the user.
# Instructions:

# Get user input for the two numbers and the desired operation.
# Use conditional statements to determine which operation to perform based on the user’s choice.
# Use appropriate operators to compute the result.
# Handle division by zero gracefully.

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operations = input("Enter operation (+, -, *, /): ")

# Perform the operation based on user input
if operations == "+":
    print("The result is:", num1 + num2)
    
elif operations == "-":
    print("The result is:", num1 - num2)
    
elif operations == "*":
    print("The result is:", num1 * num2)
    
elif operations == "/":
    if num2 != 0:
        print("The result is:", num1 / num2)
    else:
        print("Error: Division by zero")
        
else:
    print("Error: Invalid operation")




