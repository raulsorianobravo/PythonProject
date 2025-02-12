
# Sequence Last Item If Last Item
# Implement a function that:

# (1) takes a list as a parameter

# (2) returns the last item of the list

# (2) returns the string "Empty List" if the input list has no items.


def check(lst:list):
    if all(lst):
        return "Empty List"
    else: 
        return lst[(len(lst)-1)]
    

print(check([]))
print(check([3,4]))
