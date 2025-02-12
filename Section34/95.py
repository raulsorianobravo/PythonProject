
# Nine Files
# Create nine empty text files with pathnames day1.txt, day2.txt ... day9.txt.

for number in range(1, 9+1):
    open("day{}.txt".format(number), "w").close()