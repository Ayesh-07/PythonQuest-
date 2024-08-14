#------------------------------------------------------------------------------------------ 

# for printing statement in python 

#--------------------------------------------------------------------------------------------



#The print() function is used to display output to the console. 
# It can handle various types of data, including strings, numbers, and other objects.
#You can pass multiple arguments to print(), which will be separated by spaces by default.

# Using Separator and End Parameters

# sep: Defines the separator between values.
# end: Defines what is printed at the end of the output (default is a newline).


#----------------------------------------------------------------------------------------

print("Hello World");

print("Hi i'm Ayesha");

print("Hello,", "World!")

print("Hello", "World", sep="---", end="!!!")

#-----------------------------------------------------------------------------------------------


# Formatted Strings
# You can use formatted strings (f-strings) for more complex formatting.


name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")


#----------------------------------------------------------------------------------------------------

# Comments  in python

#----------------------------------------------------------------------------------------------------


# Comments are used to explain and annotate code. They are not executed 
# by the interpreter and are intended to make the code more understandable to humans.


# Single-Line Comments

# Single-line comments start with the # symbol.
# print("Hello World");
#print("Hi i'm Ayesha");

#----------------------------------------------------------------------------------------------------

#Multi-Line Comments

""" Python does not have a distinct multi-line comment syntax, but multi-line comments 
are often achieved using multi-line strings (triple quotes). Although these are technically 
string literals,they are not assigned to any variable and thus are ignored by the interpreter."""

"""
This is a multi-line comment.
It can span multiple lines.
"""
print("Hello, World!")


#--------------------------------------------------------------------------------------------

# Practice Question 

#-------------------------------------------------------------------------------------------


# Create variables to store your name and age.
# Use the print() function to display your name and age in the format provided.
# Ensure the output message uses the variables to personalize the message.



name = "ayesha";
age = "49"
result = print(f"Hi! I'm {name} and i am {age} years old.")



