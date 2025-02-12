
# What Day is Today?
# Implement a function that takes a date in the form of 'YYYY-MM-DD' as parameter and returns the day for that date.

# For example, if I called your function with print(foo('2019-6-17')) it should return 'Monday'.

import datetime

def foo(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    