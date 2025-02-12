# Remove if Too Big and Add New
# Implement a function that:

# (1) takes a list and an object as arguments

# (2) if the list has three items remove the first item of the list and append the object to the end of the list

# (3) return the modified list or return None if the list didn't have three items.

def foo(lst:list, obj):
    if len(lst) == 3:
        lst.remove(lst[0])
        lst.append(obj)
        return lst
    else: return None

print(foo([1,2,5],5))
print(foo([3,4,5],5))


def foo(lst, item):
    if len(lst) == 3:
        lst.pop(0)
        lst.append(item)
        return lst