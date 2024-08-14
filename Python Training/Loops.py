
""" Python Loops Comprehensive Notes"""


# ------------------------------------------------------------------------------------------------------------------------------


""" for Loop """


# The for loop is used to iterate over elements of a sequence (like lists, tuples, strings)
# or other iterable objects.


"""  Syntax  """

# for variable in sequence:
#     # code block


""" Iterating Over a List:  """

# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)

"""  Using range() Function: """

# for i in range(5):  # Generates numbers 0 to 4
#     print(i)

"""  Iterating Over a String: """

# for char in "hello":
#     print(char)


"""  Basic Questions  """

# Simple Iteration:
# Write a for loop that prints all the elements in the list [10, 20, 30, 40, 50].

Numbers = [10, 20, 30, 40, 50]

for num in Numbers:
    print(num);



#  ----------------------------------------------------------------------------------------------------

# Range Function:
# Use a for loop to print all the numbers from 1 to 10 (inclusive) using the range() function.

for items in range (1 , 11):
    print(items)
    

# ---------------------------------------------------------------------------------------------------


# String Iteration:
# Write a for loop that prints each character of the string "Hello, World!" on a new line.

word = "Hello, World!"
for char in word:
    print(char)
    
# ----------------------------------------------------------------------------------------------------

# Sum of Numbers:
# Write a for loop to calculate the sum of all numbers from 1 to 100 and print the result.

total_Sum = 0

for numbers in range(1,100):
  total_Sum += numbers 
print(total_Sum)


# -------------------------------------------------------------------------------------------------------

# List Comprehension:
# Create a list of squares of numbers from 1 to 5 using a for loop and list comprehension.

square_list = []

for i in range(1,6):
    square_list.append (i * i)
print(square_list)



""" While Loop """

# The while loop repeats a block of code as long as a specified condition is True.

"""  Syntax """

# while condition:
    # code block
    
    
    
count = 0
while count < 5:
    print(count)
    count += 1  # Ensure the condition eventually becomes False
    
    
# --------------------------------------------------------------------------------------------------------


""" Practice Questions """

# ---------------------------------------------------------------------------------------------------

# Print Numbers from 1 to 20:
# Write a while loop that prints numbers from 1 to 20 (inclusive).

count = 1 
while  count <= 20 :
   print(count)
   count += 1
   
   
# ---------------------------------------------------------------------------------------------------------------

# Sum of Positive Numbers:

# Write a while loop to calculate the sum of positive numbers entered by the user.
# The loop should stop when the user enters a negative number, and print the final sum.


total_sum = 0
number = int(input("Enter a positive number (or a negative number to stop): "))

while number >= 0:
    total_sum += number
    number = int(input("Enter another positive number (or a negative number to stop): "))

print("The sum of positive numbers is:", total_sum)


# -------------------------------------------------------------------------------------------------

# Find the First Perfect Square Greater Than 100:
# Write a while loop to find and print the smallest perfect square number that is greater than 100.


number = 101  # Start checking from 101
while True:
    if (number ** 0.5).is_integer():
        print("The first perfect square greater than 100 is:", number)
        break
    number += 1

# ---------------------------------------------------------------------------------------------------------


# Count Down from 10 to 0:
# Write a while loop that counts down from 10 to 0 and prints each number.


count = 10
while count <= 1:
    print(count)
    count -= 1
    

# ----------------------------------------------------------------------------------------------------------

# Repeat Until User Inputs "quit":
# Write a while loop that continuously prompts the user to enter a word. 
# The loop should stop and print "Goodbye!" when the user inputs "quit".



user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter a word (type 'quit' to stop): ")
print("Goodbye!")



# --------------------------------------------------------------------------------------------



# Generate Fibonacci Sequence:
# Write a while loop to generate and print the first 15 numbers of the Fibonacci sequence.








# Factorial Calculation:
# Write a while loop to calculate the factorial of a user-inputted positive integer.

# Find the Smallest Power of 2 Greater Than 1000:
# Write a while loop to find and print the smallest power of 2 that is greater than 1000.

# Print Multiples of 3 Less Than 50:
# Write a while loop that prints all multiples of 3 that are less than 50.

multiple = 3
while multiple < 50:
 print(multiple) 
 multiple += 3
 

# --------------------------------------------------------------------------------------------------------


""" Infinite Loop """

# Be cautious with infinite loops, which occur when the condition is always True. 
# They can only be terminated by a break statement or by stopping the program.

while True:
    response = input("Type 'exit' to quit: ")
    if response == 'exit':
        break
    print(response)



# -----------------------------------------------------------------------------------------------------


"""  Loop Control Statements """

#    Python includes several control statements to modify the behavior of loops:
   
#    break      The break statement is used to exit the nearest enclosing loop prematurely.
   
#    continue    The continue statement skips the current iteration and proceeds to the next iteration of the loop.
   
#    else        An else block can be used with both for and while loops. 
#                It executes after the loop finishes normally (i.e., not terminated by a break statement).



for i in range(10):
    if i == 5:
        break
    print(i)



for i in range(5):
    if i % 2 == 0:
        continue
    print(i)


for i in range(5):
    print(i)
else:
    print("Loop completed.")


# -----------------------------------------------------------------------------------------------


"""  Practice Questions on infinite loop . loop control statements  """

# ----------------------------------------------------------------------------------------------


# Write a Python program that iterates over a list of numbers and prints each number. 
# If the number is greater than 10, break out of the loop.
# Ensure that you print a message when you break out of the loop.



input =  [3, 7, 10, 12, 15]

for i in input:
   if   i > 10:
    print("Number greater than 10 found. Exiting loop.")    
    break

# ------------------------------------------------------------------------------------------------------------------    

# Write a Python program that prints all the even numbers from 1 to 20. 
# Use the continue statement to skip the printing of odd numbers.


for i in range(1,21):
    if i % 2 != 0:
        print(i)
        continue
        
# -----------------------------------------------------------------------------------------------------------------


# Write a Python program that searches for the number 7 in a list of integers. If 7 is found, print "Number found." 
# If the loop completes without finding the number, print "Number not found." Use an else block with the loop.


Input = [1, 2, 3, 4, 5, 6, 8, 9]

for  i in Input:
    if i == 7:
        print("Number found")
        break 
    else:
        print(" Number not found. ")




