
# Every Seven
# Implement a function that takes a list as parameter and returns the first item and then every subsequent 7th item of the input list.

# For example, if I called your function with

# foo(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon'])

# The output would be this list:

# ['mon', 'mon', 'mon', 'mon']. So, the output contains the 1st element, 8th, 15th, 22nd, and so every item at a step of 7.

def foo(mylist):
    return mylist[::7]