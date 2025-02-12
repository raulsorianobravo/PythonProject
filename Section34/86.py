mylist = ["a", "b", "c", "c"]
print(set(mylist))

# Dictionary Sum
# Implement a function that takes a dictionary as parameter and returns the sum of the dictionary values.

# For example if the input is {'a' : 1, 'b' : 3, 'c' : 6} the function output should be 10.

def foo(mydict):
    return sum(mydict.values())