# Variables
# Create a variable named character  and assign the value "Jon Snow"  to that variable.

# Don't forget that everything in Python is case sensitive, which means character  is considered different from Character.

# Jon  is considered different from jon. And so on. 

# The solution is in this link.

 

# Essential points on how to solve these types of exercises:

# Write your code solution in the area down below and then click on Check Solution

# If your solution is incorrect, try to understand the error message you get, modify your solution, and click on Check Solution again. 

# Repeat the process above until you get the correct solution or skip if you want to surrender.

character = "Jon Snow"


# Get Variable Value
# 1. Create a variable named price and assign it a value of 10.

# 2. In the next line print the value of the variable price. Make sure you use the print function.

# The solution can be found in this link.

print(10)

price = 10
print(price)


# Math Operators
# Calculate the product (multiplication) of x  and y , raise the product to the power of z  and divide everything by 8. You should print the output using the print function.

# Please add your code below the existing code.

# Tip: You can either create a variable first, store the math expression in the variable, and then print out the variable, or you can simply put the expression inside the print() function directly. Either way is correct.

# View Solution


x = 1
y = 2
z = 3

print(((x*y)**z)/8)


# Simple Sum
# Complete the script by calculating the sum of a and b and use the print function to print the integer version of the sum.

# View Solution

a = 1.0
b = 2

print(int(a+b))

# Lists
# Assign a list of three items to mylist. The items can be any type of data.

# View Solution

mylist = [2,"re",8.0] 

# Indexing
# Insert the index of the character 'h'  inside the square brackets.

# View Solution

name = "John"
print(name[name.index('h')])

# Slicing
# Fill the empty square brackets so that the slice 'hn'  is printed.

# View Solution

name = "John Smith"
print(name[2:4])

# More on Indexing
# Fill in the square brackets so that item 'y'  is printed.

# View Solution

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[letters.index('y')])


# More on Slicing
# Fill in the empty square brackets so the script prints 'xy' .

# View Solution

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-3:-1])

# List Indexing
# Complete the print() function to print the 18th item from mylist using list indexing.

# View Solution

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(mylist[17:18])
print(mylist[17])

# Append to List
# Add another line under the existing line that appends the string "John"  to list mylist.

# View Solution

mylist = ["Marry", "Jack"]
mylist.append("John")



# Remove from List
# Add another line under the existing line where you remove "John"  from list mylist.

# View Solution

mylist = ["Marry", "Jack", "John"]
mylist.remove("John")


# Append from List to List
# Append the last item of list1  to list2 .

# View Solution

list1 = [1.2323442655, 1.4534345567, 1.023458894]
list2 = [1.9934332091]

list2.append(list1[-1])

# Concatenate List Items
# Concatenate the first item with the last item of mylist and store the output in a variable named c. Make sure to use list indexing to solve this exercise.

# View Solution

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

c = mylist[0] + mylist[-1]

# Create Dictionary
# Assign a dictionary made of two keys and two values to mydict. The keys and values can be anything.

# View Solution

mydict = {"key1":5, "key2":6}



# Create Function
# Define a function named hello_world  that has no parameters. The function should simply return the string "Hello World". Do not call the function, simply define the function and use return, and not print . You will understand when to use print  and when to use return  in the following video.

# View Solution

def hello_world():
    return "Hello World"

# Exponential Function
# Define a custom function using def  and name it power. The function should take one argument and return the argument raised to the power of 2.

# Example, take a  as argument and return a ** 2 .

# View Solution

def power(v):
    return v**2


# Sum up Function
# Complete the mysum  function so the function returns the sum of arguments a  and b . Don't call the function, simply define the function.

# View Solution

def mysum(a, b):
    return a+b

# Function Output
# Add another line under the existing code where you use the print function to print out the function call. The function call should take 10  and 20  as values for arguments a  and b  respectively. 

# View Solution

def mysum(a, b):
    return a + b
    
print(mysum(10,20))



# Function with Default Parameters
# Create a function named converter. The function should take two parameters, a non-default kg  and coef  parameter with a default value of 2.20462. The function should return the product of kg  and coef .

#  View Solution

def converter(kg, coef=2.20462):
    return kg * coef