#------------------------------------------------------------------------------------------------------

""" Variables in Python  """

#-----------------------------------------------------------------------------------------------------


"""  Definition:  """   

# Containers for storing data values.


"""  Naming Rules:  """

# Must start with a letter (a-z, A-Z) or an underscore (_).
# Followed by letters, numbers (0-9), or underscores.
# Case-sensitive (e.g., age and Age are different).


"""  Dynamic Typing: """ 

# No need to declare data types explicitly. Python infers the type based on the value assigned.


#------------------------------------------------------------------------------------------------------



name = "Alice"   # String variable
age = 30         # Integer variable
height = 5.6     # Float variable



#-----------------------------------------------------------------------------------------------------


"""Basic Data Types in Python """

# ----------------------------------------------------------------------------------------------------

# - Integer (`int`): Whole numbers.
# - Float (`float`): Numbers with decimal points.
# - String (`str`):  Sequence of characters.
# - Boolean (`bool`): Represents `True` or `False`.
# - List (`list`):  Ordered, mutable collection of items.
# - Tuple (`tuple`): Ordered, immutable collection of items.
# - Set (`set`): Unordered collection of unique items.
# - Dictionary (`dict`):  Collection of key-value pairs.


#------------------------------------------------------------------------------------------------------


age = 25
print(type(age))

height = 5.9
print(type(height))

name = "Alice"
print(type(name))

is_student = True
print(type(is_student))

numbers = [1, 2, 3]
print(type(numbers))

coordinates = (10, 20)
print(type(coordinates))

fruits = {"apple", "banana"}
print(type(fruits))

person = {"name": "Alice", "age": 25}
print(type(person))


#---------------------------------------------------------------------------------------------------
"""

Type Conversion

"""

#-------------------------------------------------------------------------------------------------
""" Explicit Conversion: """
    
# Converting one data type to another using built-in functions.

""" Implicit Conversion:  """

# Automatic type conversion by Python.


#------------------------------------------------------------------------------------------------

num_str = "10"
num_int = int(num_str)  # Convert string to integer   (Explicit)


result = 10 + 5.5  # Integer 10 is implicitly converted to float   (implicit)


#-------------------------------------------------------------------------------------------------------

"""
Practice Question

"""

#------------------------------------------------------------------------------------------------------


# Create three variables:

# An integer variable num with a value of 5.
# A float variable decimal with a value of 3.14.
# A string variable text with a value of "Number".
# Convert the float variable decimal to an integer and store the result in a new variable decimal_to_int.

# Concatenate the string variable text with the integer variable num (convert num to a string before concatenation) and store the result in a new variable combined_text.

# Print the values of decimal_to_int and combined_text.



num = 5
decimal = 3.14
text = "Number"
result = print(int(decimal))
combined_text = print (str(num) + text)