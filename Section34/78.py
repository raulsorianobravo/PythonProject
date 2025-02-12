
# X Every Y
# The function you see further below takes a list as argument and returns five items every seven items.

# Alter the function so that instead of returning five items every eight items the it returns x items every y items. In other words, 
# x and  should be provided as function arguments along with the list. This will make the function more future-proof.

# import itertools

# def foo(mylist, x, y):
#     list_of_lists = [mylist[i:i+5] for i in range(0, len(mylist),7)]
#     return list(itertools.chain.from_iterable(list_of_lists))

import itertools

def foo(mylist, x, y):
    list_of_lists = [mylist[i:i+x] for i in range(0, len(mylist),y)]
    return list(itertools.chain.from_iterable(list_of_lists))