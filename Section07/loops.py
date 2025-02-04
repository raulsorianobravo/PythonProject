temps = [9.1,8.8,7.6]

print(round(temps[0]))
print(round(temps[1]))
print(round(temps[2]))

for temp in temps:
    print(round(temp))
    print("Done")

for lettet in "hello":
    print(lettet.title())

#---------------------------------------------
#exercises

colors= [11,34,98,43,45,54,54]

for color in colors:
    print(color)

for color in colors:
    if color>50:
        print(color)
    #(color>50) ? print(color) ;print("nop")

colors= [11,34.1,98,43,45,54,54]
for color in colors:
    if type(color) == int:
        print(color)

colors= [11,34.1,98,43,45,54,54]
for color in colors:
    if type(color) == int and color> 50:
        print(color)
#---------------------------------------------

st = {"M":9.1,"Sim":8.8,"john":7.5}
for i in st.items():
    print(i)

#   ('M', 9.1)
#   ('Sim', 8.8)
#   ('john', 7.5)

for i in st.values():
    print(i)

# 9.1
# 8.8
# 7.5

for i in st.keys():
    print(i)

# M
# Sim
# john

#---------------------------------------------

phone_numbers = {"John": "+37682929928", "Marry": "+423998200919"}
 
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")

# John has as phone number +37682929928
# Marry has as phone number +423998200919

for key, value in phone_numbers.items():
    print(f"{key} has as phone number {value}")

# John has as phone number +37682929928
# Marry has as phone number +423998200919

#---------------------------------------------
#Exercises

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print(f"{pair[0]}: {pair[1]}")

#---------------------------------------------

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for i in phone_numbers.values():
    print(i.replace("+","00"))

#---------------------------------------------
#While

#infinite loop
a= 3
while a > 0:
    print(a)

#---------------------------------------------

username = ""
while (username != "mm"):
    username = input("Name:" )

#---------------------------------------------

while True:
    username = input("Name:" )
    if username == "mm":
        break
    else:
        continue

