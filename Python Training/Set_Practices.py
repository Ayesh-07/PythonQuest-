
# 1. **Removing Duplicates:**
#    - **Question:** You have a list of names: `["Alice", "Bob", "Alice", "Charlie", "Bob"]`.
#      Write a code snippet to remove duplicates and print the unique names.




my_set = set(["Alice", "Bob", "Alice", "Charlie", "Bob"])
print(my_set)




# 2. **Set Operations:**
#    - **Question:** Given two sets, `set_x = {5, 10, 15, 20}` and `set_y = {15, 20, 25, 30}`,
#     write a code snippet to find the union, intersection, and difference between the two sets.

set_x = {5, 10, 15, 20}
set_y = {15, 20, 25, 30}

print(set_x | set_y)



# 3. **Set Comprehensions:**
#    - **Question:** Create a set comprehension to generate a set of cubes of all odd numbers between 1 and 10.


my_set2 = {x**3 for x in range(1, 11) if x % 2 != 0}
print(my_set2)




# 4. **Checking Membership:**
#    - **Question:** You have a set of cities: `{"New York", "Los Angeles", "Chicago", "Houston"}`. 
#      Write a code snippet to check if the city "San Francisco" is in the set and print a message accordingly.


cities = {"New York", "Los Angeles", "Chicago", "Houston"}

my_set3 = "San Francisco" in cities
print(my_set3)


# 5. **Set Operations on Strings:**
#    - **Question:** Given two strings, `str_a = "data"` and `str_b = "science"`, write a code snippet to 
#        find the characters that are in `str_b` but not in `str_a` using sets.

str_a = "data"
str_b = "science"

my_set4 = str_a in str_b

print(my_set4)


# 6. **Adding and Removing Elements:**
#    - **Question:** Start with an empty set and perform the following operations: add the elements `2`, `4`, and `6`, 
#    then remove `4`. Write a code snippet to perform these operations and print the final set.


# Syntax: {} (curly braces) for non-empty sets or set() for creating an empty set.

my_set5 = set()
my_set5.update([2,4,6])
my_set5.remove(4)
print(my_set5)


# ### Intermediate Set Operations

# 7. **Set Intersection with Lists:**
#    - **Question:** You have two lists, `list_1 = [1, 2, 3, 4, 5]` and `list_2 = [4, 5, 6, 7, 8]`. 
#    Convert them to sets and find the common elements.

list_1 = set([1, 2, 3, 4, 5])
list_2 = set([4, 5, 6, 7, 8])

res = list_1 & list_2
print(res)



# 8. **Symmetric Difference:**
#    - **Question:** Given two sets, `set_m = {7, 8, 9}` and `set_n = {8, 9, 10}`,
#    write a code snippet to find the symmetric difference between the two sets.

set_m = {7, 8, 9}
set_n = {8, 9, 10}
res = set_m ^ set_n
print(res)



# 9. **Set Operations with Mixed Data Types:**
#    - **Question:** Create a set with mixed data types (integers and strings) and perform operations like
#     union and intersection with another set containing only integers.


mixed_set = {1, 'apple', 3, 'banana', 5}
int_set = {3, 4, 5, 6}

res = mixed_set & int_set
res2 = mixed_set | int_set
print(res)
print(res2)




# 10. **Set with Nested Lists:**
#     - **Question:** You have a list of lists: `[[1, 2], [3, 4], [1, 2]]`. Convert it to a set of tuples and print the result.

list_of_lists = [[1, 2], [3, 4], [1, 2]]
set_of_tuples = set(tuple(lst) for lst in list_of_lists)
print(set_of_tuples)


# 11. **Filtering with Sets:**
#     - **Question:** You have a list of numbers: `[10, 20, 30, 40, 50, 60]` and a set of multiples of 20: `{20, 40, 60}`. 
#     Write a code snippet to filter the list to include only numbers that are also in the set.

numbers = [10, 20, 30, 40, 50, 60]

multiples = {20, 40, 60}

numbers_set = set(numbers)

res = numbers_set & multiples

result = list(res)
print(result)


# 12. **Set of Sets:**
#     - **Question:** Create a set containing other sets (as frozen sets) and perform a union operation with another set of frozen sets.


# Create sets of frozensets
set_of_frozensets1 = {frozenset([1, 2]), frozenset([3, 4]), frozenset([5, 6])}
set_of_frozensets2 = {frozenset([3, 4]), frozenset([7, 8])}

# Perform the union operation
union_result = set_of_frozensets1 | set_of_frozensets2

print("Union:", union_result)




# 13. **Finding Unique Words in a Sentence:**
#     - **Question:** Given the sentence `"the quick brown fox jumps over the lazy dog"`, find the unique words in the sentence using sets.

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
new = set(words)
print(new)

  


# 14. **Comparing Sets:**
#     - **Question:** Given three sets, `set_p = {1, 2, 3, 4}`, `set_q = {3, 4, 5, 6}`, and `set_r = {1, 5, 7}`,
#     write a code snippet to find which elements are unique to each set and not in any other set.

set_p = {1, 2, 3, 4}

set_q = {3, 4, 5, 6}

set_r = {1, 5, 7}

unique_to_p = set_p - (set_q | set_r)
unique_to_q = set_q - (set_p | set_r)
unique_to_r = set_r - (set_p | set_q)

# Combine the unique elements
unique_elements = unique_to_p | unique_to_q | unique_to_r

print(unique_elements)



# 15. **Using Sets for Membership Testing:**
#     - **Question:** You have a large list of user IDs. Convert this list to a set and write a code snippet
#     to test if a particular user ID exists in the set quickly.



user_ids_list = [
    101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 
    111, 112, 113, 114, 115, 116, 117, 118, 119, 120
]

user_ids = set(user_ids_list)

test_id = 105

exists = test_id in user_ids

print(f"User ID {test_id} exists: {exists}")

