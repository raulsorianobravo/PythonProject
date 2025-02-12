
# Sequence First and Last
# Implement a function that takes a list as parameter and returns the first and the last item of the list.

def lastItem(l:list):
    elements = len(l)
    
    result = [l[0],l[elements-1]]
    return result

l = [0,4,2,4,5,3,2,1,"dds"]

print(lastItem(l))