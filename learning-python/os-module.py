import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    #print(os.name)
    print(path.exists(r"learning-python\textfile.txt"))
    print(path.isfile(r"learning-python\textfile.txt"))
    print(path.isdir(r"learning-python\textfile.txt"))

    #get full paths
    print(path.realpath(r"learning-python\textfile.txt"))
    print(path.split(path.realpath(r"learning-python\textfile.txt)"))) #splits path and file name

    #get modified time
    t = time.ctime(path.getmtime(r"learning-python\textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime(r"learning-python\textfile.txt")))

    #get how long ago time was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(r"learning-python\textfile.txt"))
    print(td)
    print(td.total_seconds())
    
if __name__ == "__main__":
    main()
