
# Directory Structure
# Create 50 empty folders named 1 to 50:

# /1

# /2

# ...

# /50

import os

for i in range(1, 50+1):
    os.makedirs(str(i))