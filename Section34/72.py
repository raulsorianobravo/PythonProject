# Number Info
# Implement a function that:

# (1) takes a number as a parameter

# (2) returns a dictionary that has information about the sign ('negative', 'positive', or 'zero') and the parity ('odd', 'even', or 'non integer') of the input number.



# For example, if I called your function as below it would return:

# foo(10) -> {'sign': 'positive', 'parity': 'even' }

# foo(-2) -> {'sign': 'negative', 'parity': 'even'}

# foo(-3) -> {'sign': 'negative', 'parity': 'odd'}

# foo(5.1) -> {'sign': 'positive', 'parity': 'non integer'}

# foo(5.1) -> {'sign': 'negative, ', 'parity': 'non integer'}

# foo(0) -> {'sign': 'zero', 'parity': 'even'}

def foo(i):
    if i > 0:
        sign = "positive"
    elif i<0:
        sign = "negative"
    else:
        sign = "zero"
    par = "odd" if i % 2 == 1 else ("even" if i % 2 == 0 else "non integer") 
    result = {"sign":sign,"parity":par}
    return result
print(foo(10))

def foo(number):
    return dict(sign = "positive" if number > 0 else
        ("negative" if number < 0 else "zero"),
        parity = "odd" if number % 2 == 1 else 
        ("even" if number % 2 == 0 else "non integer"))