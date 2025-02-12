# Random Range
# Implement a function that:

# (1) returns a list of 1000 random integers

# (2) the integer values should be between 1 and 10, including 1 and 10.

import random
def foo():
    return [random.randint(1,10) for i in range(1000)]