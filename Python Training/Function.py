"""  Basic Function Definition  """

#---------------------------------------------------------------------------------------------------------


# In Python, you define a function using the def keyword. 


#        def function_name(parameters):
#            """
#            Optional docstring
#            """
#            # Function body
#            statement(s)
#            return value  # Optional


#       function_name is the name of your function.
#       parameters are inputs to the function (can be empty).
#       return statement is optional and is used to return a value from the function.



"""  Basic Function Definition  """

#---------------------------------------------------------------------------------------------------------


# Define a function in Python that takes two numbers as arguments and returns their sum.

def numbers( a , b):
 return a + b

numbers( 5 , 9)


#---------------------------------------------------------------------------------------------------------


# What is the purpose of the return statement in a function?

# Answer: The return statement is used to exit a function and pass a value back to the caller.


# --------------------------------------------------------------------------------------------------


# How do you call a function in Python?

# Answer: You call a function by using its name followed by parentheses, e.g., function_name().


# --------------------------------------------------------------------------------------------------

# Write a function that takes a list of numbers and returns the maximum number.
num = [ 4 ,6 ,9,44,2,5]

def find_max(num):
    return max(num)

# ------------------------------------------------------------------------------------------------

# What is the purpose of *args and **kwargs in function definitions?

#  *args allows a function to accept a variable number of positional arguments, 
# while **kwargs allows a function to accept a variable number of keyword arguments.





