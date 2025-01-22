#https://docs.python.org/3/library/time.html
#https://docs.python.org/3/library/os.html
#https://pandas.pydata.org/docs/

#https://pypi.org/project/pandas/
#pip install pandas

import time
import os
import pandas

while True:
    if os.path.exists("Section11/test.txt"):
        data = pandas.read_csv("Section11/1.csv")
        print(data.read())
    else:
        print("not exist")
    time.sleep(3)