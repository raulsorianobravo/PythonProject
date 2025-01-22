#Functions
print(isinstance("abc",str))

#Calculate area
def area(a,b):
    print(a, b)
    return(a*b)

print(area(4,5))

#Exercises
def concatenateF(text1, text2):
    return(text1+text2)
    
print(concatenateF("hi", "John"))

#-----------------------------

print(area(a = 4, b = 5))
print(area(b = 4, a = 5))


def area2(a,b=6):
    print(a, b)
    return(a*b)

print(area2(4))

#-----------------------------
#many arguments
def preMean(*args):
    return args

print(preMean(1,4,5))
#Tuple (1, 4, 5)

def mean(*args):
    return sum(args)/ len(args)

print(mean(1,4,5))
#3.3333333333333335

#-----------------------------

#Exercises
def foo(*args):
    return sum(args)/len(args)
print(foo(10, 20, 30, 40))

def foo(*args):
    args = [arg.upper() for arg in args]
    return sorted(args)

print(foo("snow", "glacier", "iceberg"))
#['GLACIER', 'ICEBERG', 'SNOW']
#-----------------------------

def mean(**kwargs):
    return kwargs

print(mean(a=1,b=4,c=5))
#{'a': 1, 'b': 4, 'c': 5}

#-----------------------------
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=4,b=5))