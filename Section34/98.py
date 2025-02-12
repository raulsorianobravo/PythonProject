
# Mean and Write
# Calculate the mean of all the numbers of all the text files and write the value inside a new mean.txt file. Just so you know, the mean is 15.550769230769232.


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
mean = sum(numbers)/len(numbers)

with open("mean.txt", "w") as file:
    file.write(str(mean))