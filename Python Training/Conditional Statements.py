"""  Introduction  """

# Conditional statements control the flow of execution based on certain conditions. 
# They allow you to execute specific code blocks when certain criteria are met.



#---------------------------------------------------------------------------------------
"""
Syntax

"""
#--------------------------------------------------------------------------------------




#          if condition:
#              # Code to execute if condition is True
             
             
#          if condition1:
#              # Code to execute if condition1 is True
#          elif condition2:
#              # Code to execute if condition1 is False and condition2 is True
             
             
#          if condition1:
#              # Code to execute if condition1 is True
#          elif condition2:
#              # Code to execute if condition1 is False and condition2 is True
#          else:
#              # Code to execute if none of the above conditions are True

""" Conditional Expressions """
           
#   Also known as the ternary operator for inline conditional assignments:


#--------------------------------------------------------------------------------------------------------------
"""

Practice Questions 
  
"""
#--------------------------------------------------------------------------------------------------------------


# Write a Python program that checks if a number is positive.
# If it is positive, print "The number is positive". If it is not, print "The number is not positive".

number = float(input("Enter your Number."))
if number > 0 :
    print("The number is positive.")
    
else:
   
    print("The number is not positive.") 
    
#-------------------------------------------------------------------------------------------------------------

# Create a Python program that takes a variable score and prints the corresponding grade based on the
# following criteria:

# 90 or above: "A"
# 80 to 89: "B"
# 70 to 79: "C"
# Below 70: "F"



grades = float(input("Enter your grades."))

if grades >= 90:
    
    print ("your Grade is :  A")
    
elif grades >= 80:
    print ("your Grade is :  B")
    
elif grades >= 70:
    print ("your Grade is :  C")
    
elif grades <= 70:
    print ("your Grade is :  B")
    
else:
    
    print ("This is Invailed Grades.")
    
    
#-------------------------------------------------------------------------------------------------------


# Write a Python program that checks if a person is eligible to vote. A person is eligible 
# if they are at least 18 years old and a citizen.
# Use logical operators to determine eligibility.


age = 20
is_citizen = True

if age  >= 18 and is_citizen :
    
    print ("You are Eligible.")
else:
    
    print("You are not Eligible.")
    

# ---------------------------------------------------------------------------------------------------


# Create a Python program that checks if a given fruit is in a predefined list of fruits. Print "Fruit found"
# if it is in the list and "Fruit not found" if it isn't.

fruits = ["apple", "banana", "cherry"]
fruit = "banana"

if fruit in fruits:
    print("Fruit found")

else:
    
    print("Fruit not found")
    
    
# ------------------------------------------------------------------------------------------------


# Write a Python program that compares two variables to check if they are the same object in memory. 
# Print "Same object" if they are, and "Different objects" if they are not.


num1 = float(input("Enter you First Number :  "))
num2 = float(input("Enter you Second Number : "))

result = print( num1 is num2)


# ---------------------------------------------------------------------------------------------


""" Conditional Expressions """
           
#   Also known as the ternary operator for inline conditional assignments:

# value_if_true if condition else value_if_false


# Write a Python program that uses a conditional expression to assign a message
# based on whether a number is even or odd. Print the message.



user_input = input("Enter a fruit: ").strip()

# Check if the input fruit is "mango"
message = "Yes! Mango is the king of fruits." if user_input.lower() == "mango" else "This fruit is not the king of fruits."

print(message)



# -----------------------------------------------------------------------------------------------------------------------------



 
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


