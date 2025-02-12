
# The Inside of a List
# Implement a function that takes a list as parameter and returns a list with all but the first and the last item of the input list.

# For instance, if I was to call your function with foo([2, 19, 99, 101]) the output should be [19, 99].

def foo(lst:list):
    return lst[1:len(lst)-1]

print(foo([2, 19, 99, 101]))

print((1,2,3)*2)


def foo(mylist):
    return mylist[1:-1]