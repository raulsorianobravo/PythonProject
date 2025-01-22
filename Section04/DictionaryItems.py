#Acces items to a Dictionary

student = {"A":8.8, "B":9.0, "C":10.0}
#print(student[1])

print(student["A"])
#8.8
print(student["A"], student["B"])
#8.8 9.0

#Error
# print(student["A":"B"])

#Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

#From tuple to list:

cool_tuple = (1, 2, 3)
cool_list = list(cool_tuple)
print(cool_list)
#[1, 2, 3]


#From list to tuple:

cool_list = [1, 2, 3]
cool_tuple = tuple(cool_list)
print(cool_tuple)
#(1, 2, 3)


#From string to list:

cool_string = "Hello"
cool_list = list(cool_string)
print(cool_list)
#['H', 'e', 'l', 'l', 'o']


#From list to string:

cool_list = ['H', 'e', 'l', 'l', 'o']
cool_string = str.join("", cool_list)
print(cool_string)
#'Hello'