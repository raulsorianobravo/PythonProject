
# Even Lists
# Implement a function that:

# (1) takes a list as parameter

# (2) returns the middle item of the list

# (2) returns the string "Bad List" if the input list has no items or it has an even number of items


def foo(mylist):
    if len(mylist) > 0 and len(mylist) % 2 != 0:
        middle_index = int(len(mylist)/2)
        return mylist[middle_index]
    else:
        return "Bad List"