def division(a,b):
    try:
        return a/b
    except:
        return "ZeroDivide"

print(division(1,0))


def division2(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "ZeroDivide"

print(division2(1,0))

