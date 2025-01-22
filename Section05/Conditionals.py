#Conditionals
def mean(vals):
    if type(vals) == list:
        total = sum(vals) / len(vals)
    #isinstance instead type
    elif isinstance(vals, dict):
         total = sum(vals.values()) /len(vals)
    return total

student = {"A":9.1,"B":8.8,"C":7.5}
temps = [5,6,3]
print("Dict",mean(student))
print("List",mean(temps))




#---------------------------------------------
def ambient(temp):
    if(temp > 7):
        return "warm"
    elif(temp<=7):
            return "cold"

print(ambient(4))

#---------------------------------------------
def function(text):
    if(len(list(text))<8):
        return False
    elif(len(list(text))>=8):
        return True

print(function("mypass"))
print(function("mylongpassword"))

#---------------------------------------------

x = -10
if x * 2 > x:
    print("Greater")
else:
    print("Less or Equal")

#---------------------------------------------

def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))

#---------------------------------------------

def function2(temp):
    if(temp > 25):
        return "Hot"
    elif(temp>=15) and temp<=25:
        return "warm"
    else:
        return "Cold"

print(function2(10))
print(function2(15))
print(function2(16))
print(function2(25))
print(function2(26))

#---------------------------------------------
def function3(temp):
    if(temp > 7):
        return "warm"
    elif(temp<=7):
            return "cold"

value3 = float(input("Enter Temperature:"))
print(function3(value3))