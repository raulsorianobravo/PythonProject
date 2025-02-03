a = 1
b= "2"
print(int(2.5))

#print(a+b)

# 2
# Traceback (most recent call last):
#   File "d:\Source\Repos\Python\PythonCourse\Section17\exceptions.py", line 4, in <module>
#     print(a+b)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# PS D:\Source\Repos\Python\PythonCourse> 

print(a+float(b))

#OR

print(str(a)+b)


#print(c)

# Traceback (most recent call last):
#   File "d:\Source\Repos\Python\PythonCourse\Section17\exceptions.py", line 20, in <module>
#     print(c)
# NameError: name 'c' is not defined

c=3
print(c)

#Exercises
# mydict = ["name":"John", "surname":"Smith"] 

# print(mydict)

# mylist = [John, Jack, Jim] 

# print(mylist) 