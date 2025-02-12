
# Nine Mindful Files
# Create nine empty files with pathnames file1.txt, file2.txt ... file9.txt . Do not overwrite them if they exist already.

for number in range(1, 9+1):
    open("file{}.txt".format(number), "a").close()