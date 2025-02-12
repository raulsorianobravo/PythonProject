
lst = [4, 5, "er", 6.8]

def check(lista:list, obj):
    if(type(lista) == list):
        if(lista.count(obj) == 0):
            lista.append(obj)
    return lista

result = check(lst, "er")

print(result)