
# Integers of non Empty Lists
# Loop through the elements list and print out the first item of each list if the item is an integer.

elements = [
    [1, 4, 6, 7],
    [4, 5, 6],
    [6, 7, 8],
    [],
    ["nodata", "nodata"],
    [1, 3]
            ]

for i in elements:
    try:
        if type(i[0]) == int:
            print(i[0])
    except:
        continue