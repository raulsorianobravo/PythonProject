
# Try and Except
# Built a try and except block under the existing code.

# Print out the sum of x and y under try and print out the sum of the integer version of x and integer version of y under except.


x = 1
y = '2'
try:
    print(x + y)
except TypeError: # Better to be specific about the error you expect
    print(int(x) + int(y))



# Find Questions
# Extract and print out all the questions from the file2.txt file.

# Expected output:

# ['And what if others do?', 'What characterizes an addiction?', 'Why should we be addicted to thinking?']

import re
with open("file2.txt") as file:
    content = file.read()
    print(re.findall("[A-Z][a-z ',]*\?", content))


# John Smith
# Change line 4 in the code so it prints out Welcome John Smith to our shop! or any other first and last name that variables firstname and lastname may contain.

firstname = "John"
lastname = "Smith"

print("Welcome {} {} to our shop!".format(firstname, lastname))



# Andy Smith
# Fill in the parenthesis in format() so that the output of the code is Welcome Andy Smith to our shop!

names = {"firstname" : "Andy", "lastname": "Smith"}
print("Welcome {firstname} {lastname} to our shop!".format(**names))



# A.S
# Fill in the two {} brackets so that the output of the code is Welcome A.S to our shop!

firstname = "Andy"
lastname = "Smith"
print("Welcome {:.1}.{:.1} to our shop!".format(firstname, lastname))



# Number of Characters
# Complete the foo function so that it returns the number of characters of mystring wtihout the period (.) characters.

mystring = "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient python, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus."

def foo(mystring):
    return len(mystring.replace(".", ""))


# Similarity Between Texts
# Try to implement a function that takes two strings as parameters and outputs the similarity between them.For example, If I called your function with print(foo("tell me the time", "what time is it")) I would expect to get 0.3870967741935484 back.

# Make use of SequenceMatcher to build your function. It works like this:

# import difflib
# print(difflib.SequenceMatcher(None, "tell me the time", "what time is it").ratio())
# The above outputs 0.3870967741935484 which indicates some degree of similarity between the two given strings. 0 means no similarity at all. 1 means identical strings.

import difflib

def foo(string1, string2):
    return difflib.SequenceMatcher(None,string1, string2).ratio()


# Naive Robot
# Create a Robot class with two methods, an __init__, and a speak method. You can write whatever you want inside the methods, or just write pass. As long as the Robot class has the correct syntax and those two methods, the exercise will be correct.


class Robot:

    def __init__(self):
        pass

    def speak(self):
        pass

# Polite Robot
# Change the speak method so that if I was to use your robot like this:

# robot = Robot()
# print(robot.speak("hi robot"))
# The output of that would be:

# 'hi human'

class Robot:

    def __init__(self):
        pass

    def speak(self, query):
        if query == 'hi robot':
            return 'hi human'
        

# Smart Robot
# Change the speak method so that if I was to use your robot like this:

# robot = Robot()
# print(robot.speak("hi robot"))
# The output of that would be:

# 'hi human'

# For queries different from 'hi robot', the robot should return:

# I don't know

class Robot:

    def __init__(self):
        pass

    def speak(self, query):
        if query == 'hi robot':
            return 'hi human'
        else:
            return "I don't know"
        
# Genius Robot
# Alter the speak method so that it returns the sum of numbers for queries containing the word "sum" and two integers.

# Examples of usage:

# robot = Robot()
# print(robot.speak("what is the sum of 1 and 2"))
# print(robot.speak("what is the sum of 8 and 10"))
# The output of that would be:

# 3

# 18

import re

class Robot:

    def __init__(self):
        pass

    def speak(self, query):
        if 'sum' in query:
            numbers = re.findall(r'\b\d+\b', query)
            numbers = [float(item) for item in numbers]
            return sum(numbers)
        

# Robot and Mind
# As the program grows, you might want to make more objects to separate the concerns so that every object does something very specific.

# In the exercise body below you can see a Mind object with a think() method. The think()method takes a string query and returns the sum of the numbers contained in that string. So, Mind's role is only to think and return a decision (i.e. the sum). We can choose to do different things with that decision, like print it out or write it inside a file.

# That's why we also have a Robot object which has a print_out method to print out any text spitted out by the Mind and we also have a write_down method to write any text inside a text file. I have only implemented the print_out method. Using the same logic you need to implement the write_down. The write_method should create a .txt file with any name you like and write the number (e.g. 8.0) inside that file.

# For example, if I was to use your robot it should behave like below:

# robot = Robot()
# robot.print_out("What's the sum of 3 and 5?")
# robot.write_down("What's the sum of 3 and 5?")     
# That would print out 8.0 in the command line and it would also create a text file that contains the text 8.0 inside.


import re

class Mind:

    def __init__(self):
        pass
    
    
    def think(self, query):
        if 'sum' in query: # Check if string 'sum' is in query
            numbers = re.findall(r'\b\d+\b', query) # Extract the numbers. E.g. ['1', '2']
            numbers = [float(item) for item in numbers] # Convert the numbers into floats [1.0, 2.0]
            return sum(numbers) # Return the sum of the numbers
            
class Robot:

    def __init__(self):
        self.mind = Mind() # When Robot is initialized with Robot(), that will also initialize Mind
    
    def print_out(self, query):
        self.mind = Mind() # When Robot is initialized with Robot(), that will also initialize Mind
        print(self.mind.think(query)) # Prints out the output returned by mind.think(query) 
    def write_down(self, query):
        self.mind = Mind() # When Robot is initialized with Robot(), that will also initialize Mind

        with open("new.txt", "w") as file:
            file.write(str(self.mind.think(query)))


# Object and Attribute
# Print out the list of all attributes of int.

# Note: Attributes of an objects are all the object's methods (e.g. int.to_bytes()) and its properties(e.g. int.denominator).
# 

print(dir(int))            



# Object and Magic Attributes
# Implement a function that takes any Python object as parameter and returns a list of all attributes of that object except magic attributes.

# For example, if I called your function with foo(int), I expect to get this as output:

# ['bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

# As you can see, magic attributes (attributes that start and end with a double-underscore) are not in the output list.


import re

def foo(obj):
    all_attributes = dir(obj)
    normal_attributes = [attribute \
    for attribute in all_attributes \
        if not re.compile("__[a-z0-9A-Z_]*__").search(attribute)]
    return normal_attributes



# Object Identity
# Implement a function that takes any Python object as parameter and returns the object's id number.

def foo(obj):
    return id(obj)