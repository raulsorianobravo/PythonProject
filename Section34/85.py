
# Banned "xxx" Lists
# Implement a function that

# (1) takes a list as parameter

# (2) returns all the items that contain "xxx"

# The list can contain any type of objects so make sure your code doesn't break when the list has non-string items.

def foo(mylist):
    return [string for string in mylist if isinstance(string, str) and "xxx" in string ]