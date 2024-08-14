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