
# Filter Dictionary
# Implement a function that:

# (1) takes a dictionary as parameter

# (2) returns a dictionary containing only the pairs whose values are greater than 4.

# For example, if I called your function with

# foo({'a': 5, 'b': 3, 'c': 10})

# the output should be

# {'a': 5, 'c': 10}


def foo(mydict):
    return dict((key, value) for key, value in mydict.items() if value > 4)