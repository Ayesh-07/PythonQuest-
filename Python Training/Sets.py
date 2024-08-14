

# Definition:
# A set is an unordered collection of unique elements.


# Characteristics:
# No duplicate elements
# Elements are unordered
# Mutable (you can add or remove elements)



# Creating Sets

# Syntax

my_set = {1, 2, 3}

# Using the set() function

my_set = set([1, 2, 3])



"""  Basic Operations """ 

# Adding Elements:
my_set.add(4)
my_set.add(4)

# Removing Elements:
my_set.remove(2)
my_set.discard(2)

# Clearing All Elements:
my_set.clear()

 
"""  Set Operations """ 


# Union:
# set1 | set2

# Intersection:
# set1 & set2


# Difference:
# set1 - set2

# Symmetric Difference:
# set1 ^ set2


""" Set Comprehensions """

squared = {x**2 for x in range(10)}



# Empty Data Structures

# Empty List: []
# Empty Set: set()
# Empty Dictionary: {}
# Empty Tuple: ()


# Summary
# List: []
# Set: {} or set()
# Dictionary: {} with key-value pairs
# Tuple: ()
# String: '' or ""