
"""  Lists """


""" Definition: """

# Ordered collection of items

""" Syntax: """

# list_name = [item1, item2, ...]


""" Characteristics:  """

#   Ordered
#   Mutable
#   Allows duplicates
  

""" Use Cases: """

#  Storing sequences
#  Dynamic data manipulation


""" Indexing """

#   Zero-based indexing: my_list[0]
#   Negative indexing: my_list[-1]


""" Slicing """

# Access sublists: my_list[1:4]

""" Basic Operations """

#   Appending: my_list.append('banana')
#   Inserting: my_list.insert(2, 'orange')
#   Removing: my_list.remove('apple')
#   Popping: item = my_list.pop()
#   Clearing: my_list.clear()

""" List Methods """

#   count(x): Count occurrences of x
#   extend(iterable): Add elements from iterable
#   index(x): Find index of first occurrence of x
#   reverse(): Reverse the list
#   sort(key=None, reverse=False): Sort the list


"""  List Comprehensions """

#   Basic: [x**2 for x in range(10)]
#   Conditional: [x**2 for x in range(10) if x % 2 == 0]

"""  Nested Lists """

#    Example: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#    Access: matrix[0][1]


"""  Iterating Through Lists """

#   For Loop: for item in my_list: print(item)
#   With Indexes: for i in range(len(my_list)): print(my_list[i])
#   List Operations


"""  List Operations """

#  Concatenation: combined = list1 + list2
#  Repetition: repeated = [1, 2] * 3


""" List Copying """

#  Shallow Copy: list_copy = my_list.copy()
#  Deep Copy: import copy; deep_copy = copy.deepcopy(nested_list)