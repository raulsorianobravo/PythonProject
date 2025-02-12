
# Tuple to Dictionary
# customer is a tuple of tuples, but it is not the best data structure to store such data. Use Python to convert the tuple into a dictionary and print out the dictionary. 

# Expected output:

# {'rented_books': 3, 'name': 'marry', 'id': '98698761', 'surname': 'smith'}

# Note: The order of the dictionary items doesn't matter.

customer = (
    ('id','98698761'), 
    ('name', 'marry'), 
    ('surname', 'smith'), 
    ('rented_books', 3 )
    )

customerDict = dict(customer)
print(type(customerDict))
print(customerDict)