
# Five Every Seven
# In the previous exercise you created a function that returned the 1st item of the input list, the 8th item, the 15th, and so on every item at a step of 7. In this exercise you should create a similar function but instead of returning 1 item at a step of 7, you should return 5 items at a step of 7.

# So, the function should return the 1st item, 2nd, 3rd, 4th, 5th, 8th, 9th,10th, 11th,12th, 15th, 16th, 17th, 18th, 19th, 22nd, 23rd, and so on.

# For example, if I called your function with

# foo(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon'])

# I would get as output this list:

# ['mon', 'tue', 'wed', 'thu', 'fri', 'mon', 'tue', 'wed', 'thu', 'fri', 'mon', 'tue', 'wed', 'thu', 'fri', 'mon'].

import itertools

def foo(mylist):
    list_of_lists = [mylist[i:i+5] for i in range(0, len(mylist),7)]
    return list(itertools.chain.from_iterable(list_of_lists))
