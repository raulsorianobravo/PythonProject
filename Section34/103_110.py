
# Seek and Delete
# Delete all the files that have the "xxx" or the "XXX" string.

import glob
import os

text_files = glob.glob("*.txt")

for text_file in text_files:
    with open(text_file) as file:
        content = file.read().lower()
        
    if "xxx" in content:
        os.remove(text_file)




# The Shortest Straw
# Print out the name of the file with the smallest file size.

import glob
import os

text_files = glob.glob("*.txt")

sizes = {text_file:os.path.getsize(text_file) for text_file in text_files}
print(min(sizes, key=sizes.get))




# Add Gold
# Add gold to file2.txt.

# In other words, your code should modify the file2.txt file so that the content of the file looks like below.

# Since you cannot copy the text in here, you can also find the gold data inside file3.txt to easily copy them.

# {"metals":

#     {

#         "steel":

#         {

#             "conductivity": 30.1,

#             "density": 0.284,

#             "heat": 0.122,

#             "melting point": 2570,

#             "thermal expansion": 6.7,

#             "yield strength": 255,

#             "tensile strength": 410,

#             "minimum impact energy": 20

#         },

#         "aluminium":

#         {

#             "conductivity": 19,

#             "density": 0.112,

#             "heat": 0.102,

#             "melting point": 1250,

#             "thermal expansion": 9.8,

#             "yield strength": 102,

#             "tensile strength": 109,

#             "minimum impact energy": 15

#         },

#         "gold":

#         {

#             "conductivity": 33.5,

#             "density": 0.255,

#             "heat": 0.129,

#             "melting point": 2171,

#             "thermal expansion": 4.7,

#             "yield strength": 288,

#             "tensile strength": 441,

#             "minimum impact energy": 22

#             }

#     }

# }

import json

with open("file2.txt") as json_file1:
    data = json.load(json_file1)
print("DATA", data)

data["metals"]["gold"] = {
    "conductivity": 33.5,
    "density": 0.255,
    "heat": 0.129,
    "melting point": 2171,
    "thermal expansion": 4.7,
    "yield strength": 288,
    "tensile strength": 441,
    "minimum impact energy": 22
    }
with open("file2.txt", "w") as json_file2:
    json.dump(data, json_file2)



# Double Dictionary Values
# (1) Load the JSON data from file2.txt to Python as a dictionary

# (2) calculate a new dictionary like the original one but with its values multiplied by two

# (3) Print out the result dictionary.

# Expected output:

# {'yield strength': 510.0, 'heat': 0.244, 'melting point': 5140.0, 'thermal expansion': 13.4, 'density': 0.568, 'conductivity': 60.2, 'minimum impact energy': 40.0, 'tensile strength': 820.0}

# The order of items doesn't matter.


import json

with open("file2.txt") as json_file:
    data = json.load(json_file)
print({key:float(value)*2 for key, value in data.items()})



# Get Density
# Load the file2.txt data into Python as a dictionary and print out the density of steel.

# Expected output:

# 0.284

import json

with open("file2.txt") as json_file:
    data = json.load(json_file)
    print(data["metals"]["steel"]["density"])



# Access JSON Property
# Implement a function that takes the metal, the property, and the filepath as parameters and returns the property value for that metal.

# For example, if I was to call your function with print(foo("steel", "density", "file2.txt")) the output would be 0.284.

import json

def foo(metal, property, filepath):
    with open(filepath) as json_file:
        data = json.load(json_file)
        return data["metals"][metal][property]


# Merge Them
# Merge all the files into one together.txt file.

# The content of together.txt should look like below:

# Life is really simple, but we insist on making it complicated.

# Don't take life so seriously. It's not like you're going to get out alive.

# There is only one big risk you should avoid at all costs, and that is the risk of doing nothing.


import glob

text_files = glob.glob("file*.txt")
print(text_files)
with open('together.txt', 'w') as outfile:
    for text_file in text_files:
        with open(text_file) as infile:
            for line in infile:
                outfile.write(line + "\n")


# Renaming Multiple Files
# In the panel on the left, you can see a list of 13 text files named file2.txt, file3.txt ... file10.txt. Your task is to write a script that renames all the 10 files by adding a dash before the number. In other words, your code should rename all the files to:

# file-1.txt

# file-3.txt

# ...

# file-10.txt

import os
 

directory_list = os.listdir("./")
 
for f in directory_list:
    src = f
    dst = f.replace('file','file-')
    replace_name = dst
    os.rename (src, dst)