# Mean of List Extraction (Complex)
# Calculate and print out the mean of all items at a step of two. In other words, filter the list to have only items 1, 6, 9, 7, and so on, 
# and print out the average of those numbers. Note that you're not being asked to define a function here. Your code should print out the required output using a print() function.


numbers = [1, 4, 6, 8, 9, 6, 7, 8, 9, 3, 44, 55, 6, 77, 88, 997, 7, 6, 7, 7, 8, 9, 8, 8, 8, 9, 8, 8, 0, 9, 0, 9, 8, 9, 8, 8, 8, 9, 9, 9, 9, 0, 1, 3, 5, 6, 7, 8, 7, 7, 7, 8, 7, 7, 5, 4, 5, 6, 5, 56, 4, 3, 4, 5, 6, 6, 7, 8, 8, 9]

every2 = numbers[::2]
print(sum(every2) / len(every2))