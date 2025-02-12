# True if All
# Implement a function that

# (1) takes an indefinite number of lists as arguments

# (2) returns True if all lists have at least one item

# (3) returns False if one or more lists are empty.

# For example, if I called the function you have to define it would behave like below:

# foo([1, 2, 3], [0, 3], ['a']) -> True

# foo([1, 2, 3], [], ['a']) -> False

def foo(*args):
    for i in args:
        if i == None:
            return False
        return True
        
print(foo([1, 2, 3], [0, 3], ['a']))

print(foo([1, 2, 3], [], ['a']))



def foo(*args):
    return all(args)

print(foo([1, 2, 3], [0, 3], ['a']))

print(foo([1, 2, 3], [], ['a']))