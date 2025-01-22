#More Operations
print(dir(list))

temp = [9.5, 9.4, 2.2]
temp.append(6.5)
print(temp)

temp.clear()
print(temp)

temp = [9.5, 9.4, 2.2]
print(temp.index(9.5))

try:
    print(temp.index(9.5, 1, 2))
except:
    print("error")
#Traceback (most recent call last):
#   File "d:\Source\Repos\Python\PythonCourse\OperationWithList2.py", line 12, in <module>
#     print(temp.index(9.5, 1, 2))
# ValueError: 9.5 is not in list

#Exercise
seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)
print(seconds)

seconds.remove(1.23)
print(seconds)

seconds.remove(1.45)
seconds.remove(1.02)
print(seconds)

#-----------------------------------
#Access items
seconds = [1.23, 1.45, 1.02]
seconds.__getitem__(1)
print(seconds[1])

#Exercises
# -----------------------------------
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[0], serials[2], serials[5])

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)

#Slicing

serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[1:3])
#['AA899819A', 'XYSA9099400']

print(serials[0:2])
print(serials[:2])
print(serials[3:])

#last item
print(serials[-1])
#KOC9889482

print(serials[-3])
#OOP8988459

print(serials[-2:])
#['EEO8904882', 'KOC9889482']

print(serials[-2:-4])
#[]
print(serials[-4:-2])
#['XYSA9099400', 'OOP8988459']

#Slicing Strings
text = "Hello"
print(text[1])
print(text[-1])
print(text[:3])
# e
# o
# Hel

stringList = ["Monday", 4, "Tuesday"]
print(stringList[0][:3])
#Mon

#Exercises
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[:3])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[4:])