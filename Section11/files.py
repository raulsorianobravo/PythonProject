#Files
file = open("D:\Source\Repos\Python\PythonCourse\Section11\\test.txt")
print(file.read())

#----------------------------------------
content = file.read()
print(content)

file.close()

#---------------------------------------------
#better than close
with open("D:\Source\Repos\Python\PythonCourse\Section11\\test.txt") as seconFile:
    content2 = seconFile.read()

print(content)

#-----------------------------------------------
#paths
with open("Section11/test.txt") as seconFile:
    content2 = seconFile.read()

print(content)

#-----------------------------------------------
with open("Section11/test2.txt","w") as seconFile:
    seconFile.write("8888")
    seconFile.write("8888\n999")

print(content)

#-----------------------------------------------------
#Exercises
with open("Section11/test.txt") as textFile:
    content = textFile.read()[0:90]
print(content)

#-----------------------------------------------------
def getCharacter(char, path):
    with open(path) as textFile:
        result = textFile.read().count(char)
    return result
    
print(getCharacter('e',"Section11/test.txt"))

#-----------------------------------------------------
with open("file.txt","w") as seconFile:
    seconFile.write("snail")

#-----------------------------------------------------

with open("bear.txt") as textFile:
    content = textFile.read()[0:90]
print(content)

with open("first.txt","w") as firstFile:
    firstFile.write(content)

#-----------------------------------------------------
#Appending
with open("Section11/test2.txt","a") as seconFile:
    seconFile.write("\n8888\n999")

print(content)

#append and read
with open("Section11/test2.txt","a+") as seconFile:
    seconFile.write("\n8888\n999")
    seconFile.seek(0)
    content = seconFile.read()

print(content)

#-----------------------------------------------------
#Exercises

with open("bear1.txt") as textFile:
    content = textFile.read()

with open("bear2.txt", "a") as secondFile:
    secondFile.write(content)
#-----------------------------------------------------
with open("data.txt","a+") as textFile:
    textFile.seek(0)
    content = textFile.read()
    textFile.seek(0)
    textFile.write(content)
    textFile.write(content)
