# Nested Directory Structure
# Create the following directory structure with Python. In other words, use Python code to create 50 empty folders named 1 to 50 and each of those folder should contain five empty subfolders named mon to fri:

# /1

#     /mon

#     /tue

#    /wed

#    /thu

#    /fri

# /2

#     /mon

#     /tue

#    /wed

#    /thu

#    /fri

# ...

# /50

#     /mon

#     /tue

#    /wed

#    /thu

#    /fri


import os

for folder in range(1, 50+1):
    os.makedirs(str(folder))

for folder in range(1, 50+1):
    for subfolder in ["mon", "tue", "wed", "thu", "fri"]:
        os.makedirs(str(folder) + "/" + str(subfolder))

