

# Second Element of Every Tuple
# Create a for loop below the existing code where you loop through all the tuples of elements and print out the second element of each tuple in the loop.

elements = (
    (1, 4),
    (4, 5),
    (6, 7),
    (1, 3)
            )

x = [i[1] for i in elements ]

print(x)

#OR

for i in elements:
    print(i[1])