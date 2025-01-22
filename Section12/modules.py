import time
import os

while True:
    if os.path.exists("Section11/test.txt"):
        with open("Section11/test.txt") as file:
            print(file.read())
    else:
        print("not exist")
    time.sleep(3)