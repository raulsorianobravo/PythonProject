# Sequence Last Item
# Implement a function that takes a list as parameter and returns the last item of the list.

def lastItem(l:list):
    elements = len(l)
    
    return l[elements-1]

l = [0,4,2,4,5,3,2,1,"dds"]

print(lastItem(l))