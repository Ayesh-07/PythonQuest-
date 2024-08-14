
# 1. **Create a Dictionary:**
#    - Create a dictionary with the keys `"name"`, `"age"`, and `"city"`, and assign appropriate values 
#    to each key.


person = {
    "name": "Alice",
    "age": 30,
    "city": "Wonderland"
}
print(person)




# 2. **Access Values:**
#    - Given the dictionary `person = {"name": "Alice", "age": 30, "city": "Wonderland"}`, 
#     retrieve and print the value associated with the key `"city"`.

person = {"name": "Alice", "age": 30, "city": "Wonderland"}



# 3. **Add a New Key-Value Pair:**
#    - Add a new key-value pair `"email": "alice@example.com"` to the `person` dictionary.



person["email"] = "alice@example.com"
print(person)




# 4. **Modify an Existing Value:**
#    - Update the `"age"` value in the `person` dictionary to `31`.


person["age"] = 31
print(person)

# 5. **Remove a Key-Value Pair:**
#    - Remove the key `"city"` from the `person` dictionary.

person.pop("city") 
print(person)

# 6. **Check for Key Existence:**
#    - Write a function that checks if a given key exists in a dictionary and returns `True` or `False`.

def key_exists(person, key):
    return key in person
print(key_exists(person, 'country'))  


# 7. **Get Dictionary Keys and Values:**
#    - Given a dictionary, use methods to print all keys and values.


for key, value in person.items():
    print(key, value)

# ### Intermediate Questions

# 8. **Nested Dictionaries:**
#    - Create a dictionary representing a student with the following keys: `"name"`, `"age"`, `"subjects"`.
#    The `"subjects"` key should map to another dictionary with `"math"`, `"science"`, and `"english"` 
#    as subjects with respective grades.


students = {
    "student1": {"name": "Alice", "age": 25 },
    "student2": {"name": "Bob", "age": 22}
}




# 9. **Merge Two Dictionaries:**
#    - Given two dictionaries `dict1 = {"a": 1, "b": 2}` and `dict2 = {"c": 3, "d": 4}`, 
#     merge them into a new dictionary.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

new_dictionary = dict1 | dict2
print(new_dictionary)

# 10. **Update Dictionary with Another Dictionary:**
#     - Update a dictionary `person` with new information provided in another dictionary `updates`.



person["age"] = 31
person["name"] = "Ayesha"
person["city"] = "Pakistan"
print(person)


# ### Advanced Questions

# 13. **Dictionary Comprehensions:**
#     - Use a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 5
#      and the values are the squares of the keys.



squares_dict = {x: x**2 for x in range(1, 6)}

# Print the resulting dictionary
print(squares_dict)



