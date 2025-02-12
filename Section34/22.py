
# Concatenate Lists Indefinite
# Implement a function that takes an indefinite number of lists and returns the concatenated list.

# For example, if I called your function like foo([1, 2], [3, 5, 7, 8], [1]) it should return [1, 2, 3, 5, 7, 8, 1].

def foo2(*args):
    result = [x for x in args]
    return result

print(foo2([1, 2], [3, 5, 7, 8], [1]))

def foo(*args):
    lst = []
    for i in args:
        lst = lst + i
    return lst

print(foo([1, 2], [3, 5, 7, 8], [1]))
