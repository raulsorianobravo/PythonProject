#Lists
grades = [9.1, 8.5, 9.6]
listDiff = [9, "Text",[9, 8.5, 9.6]]

print(grades)
print(listDiff)
#[9.1, 8.5, 9.6]
#[9, 'Text', [9, 8.5, 9.6]]

#operations
print(grades * 3) 
#[9.1, 8.5, 9.6, 9.1, 8.5, 9.6, 9.1, 8.5, 9.6]

print(grades + listDiff)
#[9.1, 8.5, 9.6, 9, 'Text', [9, 8.5, 9.6]]

listRange = range(0,11)
print (listRange)
#range(0, 11)

listRange = list(range(1,9))
print (listRange)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listRange = list(range(1,9,2))
print (listRange)
#[1, 3, 5, 7]

