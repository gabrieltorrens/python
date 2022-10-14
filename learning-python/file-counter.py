import os
from os import path

#gets working dir, writes titles and total size in bytes to a txt file

myPath = os.getcwd()
print(myPath)

myFiles = os.listdir(myPath)
print(myFiles)

results = open("results.txt", "w+")
size = 0
for i in myFiles:
    results.write(i + "\n")
    size = size + os.path.getsize(i)
results.write(f"Total size: {size}")
results.close()