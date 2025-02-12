
# Mean of All Files
# The two text files have some numbers. Calculate and print out the mean value of all the values of all the text files.


import glob
import re

text_files = glob.glob("*.txt")
lists =[]
for text_file in text_files:
    with open(text_file) as file:
        lists.append(file.readlines())

all_lines = sum(lists, [])

matches = [re.compile("[0-9]+\.*[0-9]*").search(line) for line in all_lines]

numbers = [float(match.group(0)) for match in matches if match]
print(sum(numbers)/len(numbers))