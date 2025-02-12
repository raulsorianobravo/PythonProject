# Odd Lists
# Implement a function that takes a list as parameter and returns the middle item of the list.

# For example, if the input value for the function is [5, 8, 9] the function output would be 8.  Yes, you'd ask what happens if the input list is [5, 8, 9, 10]?

# Well, lets just pretend the universe has only odd lists for now. We'll implement a function for even lists in the next exercise.

def foo(mylist):
    middle_index = int(len(mylist)/2)
    return mylist[middle_index]