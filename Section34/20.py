
# Multiple Arguments Function Definition
# Implement a function that takes an indefinite number of arguments and returns a list containing all the argument values.

# For example, if I called the function you have to define it would behave like below:

# foo(1, "a", 5, "c")

# Expected output:

# [1, "a", 5, "c"]


def foo(*args):
    lst = [i for i in args]
    return lst

print(foo(1, "a", 5, "c"))