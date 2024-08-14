# . Basic Operations
# Question 1: Create a tuple with 5 elements. Access the third element of the tuple and print it.

my_tuple = (1 , 7, 8 , 9, 4)
print(my_tuple[3])



# Question 2: Given the tuple (10, 20, 30, 40, 50), slice it to get the last three elements and print the result.

my_tuple2 = (10, 20, 30, 40, 50)
print(my_tuple2[-3:])





# Question 3: Concatenate two tuples (1, 2, 3) and (4, 5, 6) and print the resulting tuple.

my_tuple3 = (1, 2, 3)
my_tuple4 = (4, 5, 6) 

concatnate = my_tuple3 + my_tuple4
print(concatnate)




# Question 4: Repeat the tuple (7, 8) three times and print the result.
my_tuple5 = (7, 8)

result= print(my_tuple5 *3) 


# 2. Tuple Methods
# Question 5: Create a tuple with the following elements: (5, 8, 5, 9, 5). Use the count method to find out how many times the number 5 appears in the tuple.




my_tuple6 = (5, 8, 5, 9, 5)
result = my_tuple6.count(5)
print(result)

# Question 6: Create a tuple with the elements (12, 15, 18, 20). Use the index method to find the index of the element 18.

my_tuple7 = (12, 15, 18, 20)
result = my_tuple7.index(18)
print(result)


# 3. Tuple Unpacking
# Question 7: Given the tuple (4, 8, 15, 16, 23, 42), unpack the tuple into variables a, b, c, d, e, and f, and then print each variable.

a, b, c, d, e,f, = (4, 8, 15, 16, 23, 42)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# Question 8: Given the tuple ((1, 2), (3, 4), (5, 6)), unpack the first inner tuple into variables x and y, and the second inner tuple into z and w. Print all variables.

((a, b), (c, d), (e,f)) = ((1, 2), (3, 4), (5, 6))

print(a,b)
print(c,d)
print(e,f)




# 4. Nested Tuples
# Question 9: Create a nested tuple ((1, 2), (3, (4, 5))). Access and print the element 5 from this nested tuple.


my_tuple9 = ((a,b),(c,(d,e))) = ((1, 2), (3, (4, 5)))
result = my_tuple9[1][1][1]
print(result)


# 5. Tuple with Mutable Elements
# Question 10: Create a tuple with a list as one of its elements, like ([1, 2], 3). Modify the list inside the tuple and print the updated tuple.

my_tuple10 =  ([1, 2], 3)
my_tuple10[0].append(55)
print(my_tuple10)


# Question 11: Create a tuple ((1, 2), [3, 4], (5, 6)). Change the list to [7, 8] and print the updated tuple.

my_tuple11 = ((1, 2), [3, 4], (5, 6))
my_tuple11[1][0] = 7
my_tuple11[1][1] = 8
print(my_tuple11)


# Question 12: Given a list of tuples [(1, 2), (3, 4), (5, 6)], convert it into a tuple of tuples and print the result.

list_of_tuples = [(1, 2), (3, 4), (5, 6)]

tuple_of_tuples = tuple(list_of_tuples)

print(tuple_of_tuples)


# 7. Miscellaneous
# Question 13: Given the tuple (1, 2, 3, 4, 5), create a new tuple where each element is squared.


original_Tuple = (1, 2, 3, 4, 5)
squared_Tuple = tuple(x**2 for x in original_Tuple)
print(squared_Tuple)

# Question 14: Create a tuple with the values (1, 2, 3, 4, 5). Find the maximum and minimum values in the tuple and print them.

my_tuple = (1, 2, 3, 4, 5)

max_value = max(my_tuple)
min_value = min(my_tuple)


print(f"Maximum: {max_value}")  
print(f"Minimum: {min_value}")  




# Question 15: Create a tuple ('apple', 'banana', 'cherry'). Convert this tuple to a string with each element separated by a comma and print the result.

fruits = ('apple', 'banana', 'cherry')

fruits_string = ', '.join(fruits)
print(fruits_string)




