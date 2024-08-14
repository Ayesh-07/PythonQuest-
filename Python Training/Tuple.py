""" Tuples """

""" Definition: """

#     An immutable, ordered collection of items.

"""Syntax """

#     python
#     Copy code
#     my_tuple = (element1, element2, ...)


""" Characteristics:"""

#     Immutable: Data cannot be changed after creation.
#     Ordered: Elements retain their order.
#     Allows duplicates: Multiple occurrences of the same value are allowed.


""" Use Cases """

#     Fixed collections of data (e.g., coordinates, RGB values).
#     Ensuring data integrity.

#--------------------------------------------------------------------------------------------------


"""   Creating Tuples """

# Tuples are created using parentheses () and can contain any number of elements, including other tuples.


my_tuple = (1, 2, 3)

# Creating a tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14, (1, 2))

# Creating a tuple with a single element (note the trailing comma)
single_element_tuple = (1,)

# -------------------------------------------------------------------------------------------------

""" Accessing Elements  """

# You access elements of a tuple using indexing, similar to lists. Indexing starts at 0.


# Accessing elements
print(my_tuple[0])  # Output: 1

# Accessing elements from the end
print(my_tuple[-1])  

# ----------------------------------------------------------------------------------------

""" Slicing Tuples """

# Slicing
print(my_tuple[1:3])  # Output: (2, 3)
print(my_tuple[:2])   # Output: (1, 2)
print(my_tuple[1:])   # Output: (2, 3)


#---------------------------------------------------------------------------------------

"""   Concatenation and Repetition  """



# Concatenation
new_tuple = my_tuple + (4, 5)
print(new_tuple)  # Output: (1, 2, 3, 4, 5)

# Repetition
repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

#----------------------------------------------------------------------------------------


"""  Tuple Methods  """

# Tuples have a limited set of methods compared to lists. They are:

# count(x): Returns the number of times x appears in the tuple.
# index(x): Returns the index of the first occurrence of x in the tuple. Raises ValueError if x is not found.


# Count
print(my_tuple.count(2))  # Output: 1

# Index
print(my_tuple.index(3))  # Output: 2


#----------------------------------------------------------------------------------------------------------



""" Immutability  """

#  Tuples are immutable, meaning that once they are created, their elements cannot be changed, added, or removed.
#  However, if a tuple contains mutable objects like lists, those objects can still be modified.


# Tuples are immutable
# my_tuple[0] = 10  # This will raise a TypeError

# Modifying elements of a tuple with a mutable object
mutable_tuple = ([1, 2], 3)
mutable_tuple[0].append(3)
print(mutable_tuple)  # Output: ([1, 2, 3], 3)


# -------------------------------------------------------------------------------------


""" Tuple Unpacking  """

# You can unpack a tuple into individual variables.

# Unpacking
a, b, c = (1, 2, 3)
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

# Unpacking with a nested tuple
x, (y, z) = (1, (2, 3))
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3

# -----------------------------------------------------------------------------------------------

""" Nested tuples """



nested_tuple = ((1, 2), (3, 4))
print(nested_tuple[0])  # Output: (1, 2)
print(nested_tuple[1][0])  # Output: 3


# -----------------------------------------------------------------------------------------------