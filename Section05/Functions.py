#Functions
#print(dir(__builtins__))

def mean(listValues):
    total = sum(listValues) / len(listValues)
    return total

print(mean([5,6,3]))
print(type(mean), type(sum))

#---------------------------------------------

def convert(amount):
    total = amount * 1.75
    return total

print(convert(10))

#---------------------------------------------
#Exercises
def foo(side):
    area=side*side
    return area

print(foo(7))

#---------------------------------------------

def foo2(fluid):
    eq = 29.57353
    mil = fluid*eq
    return mil

print(foo2(5))
#---------------------------------------------

#not return or None
def none():
    return None
#---------------------------------------------


