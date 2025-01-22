#Tuples
#inmutables
day_temp = (4.4, 7.9, 4.5)
try:
    day_temp.append(0,0)
except:
    print("error")

#List are mutables
day_temp2 = [4.4, 7.9, 4.5]

day_temp2.append(0.0)

print(day_temp)
print(day_temp2)

#Exercises
#------------------------------------------------------
c1 = ("red", 1,0,0)
c2 = ("green", 0,0,1)
c3 = ("blue", 0,1,0)

color_codes = (c1, c2, c3)
print(color_codes)

#------------------------------------------------------
day_temp = ({"morning":(4.4, 7.9, 4.5), "noon":(4.4, 7.9, 4.5),"evening":(4.4, 7.9, 4.5)})
print(day_temp)