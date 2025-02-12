
# Function of Function
# Define another function below the foo function. That other function should return the foo function.

# Note that I said the foo function, not the foo function call.

def foo():
    return "Hello"

def foo2():
    return foo

print(foo2)
