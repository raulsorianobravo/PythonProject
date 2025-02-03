# USER Input
# ---------------------------------------------
def ambient(temp):
    if(temp > 7):
        return "warm"
    elif(temp<=7):
            return "cold"
temp=input("enter temp: ")
print(ambient(int(temp)))

# enter temp: 2
# cold
# enter temp: 22
# warm

#---------------------------------------------

def inputName():
     user_input = input("Enter your name: ")
     hi = "Hi %s" % user_input
     hi = f"Hello {user_input}"
     return hi

def inputName2():
     user_input = input("Enter your name: ")
     hi = f"Hello {user_input}"
     return hi

print(inputName())
print(inputName2())

#---------------------------------------------

def inputName():
    user_input = input("Enter your name: ")
    user_input2 = input("Enter your surname: ")

    hi = "Hi %s %s" % (user_input, user_input2)
    #hi = f"Hello {user_input} . Hello {user_input2}"

    return hi 

print(inputName())

#---------------------------------------------

def inputName():
    user_input = input("Enter your name: ")
    user_input2 = input("Enter your surname: ")

    hi = "Hi {} - {}".format(user_input,user_input2)
    #hi = f"Hello {user_input} . Hello {user_input2}"

    return hi 

print(inputName())

#---------------------------------------------
#Exercixe

def name3(text):    
    message = "Hi %s" %user
    #message2 = f"Hello {user}"
    return message

user = input("enter your name:")
print(name3(user))

def name4(text):    
    message = "Hi %s" %user.capitalize
    #message2 = f"Hello {user}"
    return message

user = input("enter your name:")
print(name3(user))