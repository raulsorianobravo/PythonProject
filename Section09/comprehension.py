temps = [221,234,340,230]

new_temps = []
for temp in temps:
    new_temps.append(temp/10)
print(new_temps)
# [22.1, 23.4, 34.0, 23.0]

new_temps = [temp/10 for temp in temps]
print(new_temps)
# [22.1, 23.4, 34.0, 23.0]

#---------------------------------------------

temps = [221,234,340,230, -9999]

new_temps = [temp/10 for temp in temps if temp!=-9999]

#---------------------------------------------
#Exercises

def foo(datas):
    processData = [data for data in datas if type(data) == int]
    return processData

print(foo([99, 'no data', 95, 94, 'no data']))
# [99, 95, 94]

#---------------------------------------------

def foo(datas):
    numbers = [data for data in datas if data>0]
    return numbers
    
print(foo([-5, 3, -1, 101]))
# [3, 101]
#---------------------------------------------

temps = [221,234,340,230,-9999]

new_temps = [temp/10 if temp!= -9999 else 0 for temp in temps ] 

print(new_temps)
# [22.1, 23.4, 34.0, 23.0, 0]

#---------------------------------------------
#Exercises
def foo(datas):
    numbers = [data if type(data)!= str else 0 for data in datas]
    return numbers
    
print(foo([99, 'no data', 95, 94, 'no data']))

#---------------------------------------------

def foo(datas):
    numbers = [float(data) for data in datas]
    
    return sum(numbers)
    
print(foo(['1.2', '2.6', '3.3']))