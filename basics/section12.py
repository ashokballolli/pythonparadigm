import os
import time
import pandas

# using python standard modules

filePath = "../data/fruits.txt"
while True:
    if os.path.exists(filePath):
        with open(filePath) as dataFile:
            content = dataFile.read()
            print(content)
    else:
        print(os.path.curdir)
        print("file doesn't exists")

    time.sleep(5)