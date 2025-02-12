# Pregunta 1:
# What would be the content of fillme if you ran the following code. Please try to answer it mentally, without running the code on your Python interpreter.


data = [1, 2, 3, None]
fillme = []
if data:
    for item in data:
        if item:
            fillme.append(item)

print(fillme)