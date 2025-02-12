
# Dictionary Lists Sum
# Implement a function that takes a dictionary of lists as parameter and returns the sum of all items of all lists.

# For example, if input is {'a': [1, 2], 'b': [3, 4]} the output would be 10.

def foo(mydict):
    lst = []
    for key, value in mydict.items():
        lst = lst + value
    return sum(lst)