
# Create a List:
# - Create a list containing the integers from 1 to 5. Print the list.



my_list = [1,2,3,4,5]
print(my_list)


# Access Elements 
# - Given the list `colors = ['red', 'green', 'blue']`, print the first and last elements.



colors = ['red', 'green', 'blue']
print(colors[0])
print(colors[-1])



# Modify a List
 
# - Given the list `numbers = [1, 2, 3]`, append the number 4 to the list and print it.

numbers = [1, 2, 3]
numbers.append(4)
print(numbers)


# 4. **Insert an Element**:
#    - Insert the number 10 at index 1 in the list `my_list = [1, 2, 3, 4]`. Print the updated list.

my_list = [1, 2, 3, 4]
my_list.insert(1,10)
print(my_list)

# 5. **Remove an Element**:
#    - Remove the element 'apple' from the list `fruits = ['banana', 'apple', 'cherry']`. Print the updated list.

fruits = ['banana', 'apple', 'cherry']
fruits.remove('apple')
print(fruits)



# 6. **List Slicing**:
#    - Given the list `data = [10, 20, 30, 40, 50]`, print the sublist containing the second and third elements.

data = [10, 20, 30, 40, 50]
sublist = data[1:3]
print(sublist)

# 7. **List Comprehension**:
#    - Create a list of squares of numbers from 1 to 5 using list comprehension. Print the list.

my_list =[1 ,2 ,3,4,5]
res=[x**2 for x in my_list]
print(res)

# 8. **Count Occurrences**:
#    - Given the list `letters = ['a', 'b', 'a', 'c', 'a']`, count how many times 'a' appears in the list.
letters = ['a', 'b', 'a', 'c', 'a']
res = letters.count('a')
print(res)


# 9. **Find Index**:
#    - Given the list `items = ['apple', 'banana', 'cherry']`, find and print the index of 'banana'.

items = ['apple', 'banana', 'cherry']
res = items.index('banana')
print(res)


# 10. **Reverse a List**:
#     - Reverse the list `numbers = [1, 2, 3, 4, 5]` and print the reversed list.

numbers = [1, 2, 3, 4, 5]
numbers.reverse()  # Reverse the list in place
print(numbers)     # Print the reversed list

numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]  # Create a new list that is the reversed version of the original
print(reversed_numbers)          # Print the reversed list


# 11. **Nested Lists**:
#     - Create a 2x2 matrix `matrix = [[1, 2], [3, 4]]`. Print the element in the second row, first column.

matrix = [[1, 2], [3, 4]]
res = matrix[1][0]
print(res)


# 12. **Extend a List**:
#     - Given the list `base = [1, 2]`, extend it by adding `[3, 4, 5]`. Print the updated list.

base = [1, 2]
base.extend([3, 4, 5])
print(base)

# 13. **List Manipulation**:
#     - Given the list `elements = [5, 10, 15, 20]`, use slicing to create a new list containing only the last 
#       two elements. Print the new list.

elements = [5, 10, 15, 20]
new_List = elements[2:]
print(new_List)




# 14. **Remove by Index**:
#     - Remove the element at index 1 from the list `data = [100, 200, 300, 400]`. Print the updated list.

data = [100, 200, 300, 400]
data.pop(1)  # Remove and return the element at index 1
print(data)  # Print the updated list

data = [100, 200, 300, 400]
del data[1]  # Remove the element at index 1
print(data)  # Print the updated list



# 15. **Flatten a Nested List**:
#     - Given the nested list `nested_list = [[1, 2], [3, 4], [5, 6]]`, flatten it into a single list.
#      Print the flattened list.

nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)





# 16. **Find Duplicates**:
#     - Write a function that takes a list and returns a new list containing only the unique elements 
#       (i.e., remove duplicates).

my_list = [1, 2, 2, 3, 4, 4, 5]

print(list(set(my_list)))

# 17. **Sort a List**:
#     - Given the list `numbers = [5, 3, 8, 1, 2]`, sort the list in descending order and print it.
 
numbers = [5, 3, 8, 1, 2]
numbers.sort(reverse=True)
print(numbers)
 

# 18. **Combine Two Lists**:
#     - Given `list1 = [1, 2, 3]` and `list2 = ['a', 'b', 'c']`, 
#      create a new list that combines these two lists by alternating elements from each.


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = list1 + list2
print(combined)


# 19. **Nested List Comprehension**:
#     - Create a list of lists where each inner list contains numbers from 1 to 3. Use list comprehension.

nested_list = [[x for x in range(1, 4)] for _ in range(3)]
print(nested_list)

# 20. **Find Maximum and Minimum**:
#     - Given the list `numbers = [4, 7, 1, 8, 3]`, find and print the maximum and minimum values.

numbers = [4, 7, 1, 8, 3]
max_value = max(numbers)
min_value = min(numbers)

print(f"Maximum: {max_value}")  
print(f"Minimum: {min_value}")  
