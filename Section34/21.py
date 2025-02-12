# Multiple Keyword Arguments
# Implement a function that takes an indefinite number of keyword arguments and returns a dictionary containing all the argument names and the argument values.

# For example, if I called your function like below:

# foo(a = 1, c = 5, d = 109)

# The output should be:

# {"a": 1, "c": 5, "d": 109}

# a, c, and d are the argument names, and 1, 5, and 109 are the argument values.

def foo(**kwargs):
    
    return kwargs

print(foo(a = 1, c = 5, d = 109)

)