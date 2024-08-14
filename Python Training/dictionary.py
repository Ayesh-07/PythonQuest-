# A dictionary is a collection of key-value pairs.
# Each key is unique and maps to a value.

 
""" Use Cases:  """

# Storing user information.
# Representing data in key-value format.
# Efficient lookups.



my_dict = {"name": "Alice", "age": 25, "city": "New York"}


# Unordered: The items in a dictionary do not have a specific order.
# Mutable: Dictionaries can be changed after creation.
# Key-Value Pairs: Data is stored in pairs, with each key linked to a value.


# ---------------------------------------------------------------------------------------------------


# Creating a Dictionary

my_dict = {
    "key1": "value1",
    "key2": "value2",
   
}


person = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}




# ---------------------------------------------------------------------------------------------------


""" Accessing Values  """


# Using Keys to Access Values
person = {"name": "Alice", "age": 30}
print(person["name"])  

# Using the get Method
print(person.get("age")) 


# ---------------------------------------------------------------------------------------------------


"""  Adding and Modifying Items  """


# Adding Items
person["email"] = "alice@example.com"


# Modifying Items
person["age"] = 31



# ---------------------------------------------------------------------------------------------------


"""  Removing Items """

# Using del:

del person["email"]

# Using pop:

age = person.pop("age")

# Using popitem:

last_item = person.popitem()


# ------------------------------------------------------------------------------------------------------

""" Dictionary Methods  """

# Common Methods:

# keys(): Returns a view of all keys.
# values(): Returns a view of all values.
# items(): Returns a view of all key-value pairs.


print(person.keys())   # Output: dict_keys(['name', 'age'])
print(person.values()) # Output: dict_values(['Alice', 31])


# -------------------------------------------------------------------------------------------------------


"""  Iterating Over a Dictionary """

 # Looping Through Keys:

for key in person:
    print(key, person[key])


for key, value in person.items():
    print(key, value)
    
    
# ----------------------------------------------------------------------------------------------------


"""  Nested Dictionaries  """


# Definition: Dictionaries inside other dictionarie

students = {
    "student1": {"name": "Alice", "age": 25},
    "student2": {"name": "Bob", "age": 22}
}


# -----------------------------------------------------------------------------------------------

""" Accessing Nested Values:  """


print(students["student1"]["name"])  


# ----------------------------------------------------------------------------------------------

