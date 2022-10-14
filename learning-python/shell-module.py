import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    myFile = open("textfile.txt", "w+") #w+ write mode and create if does not exist
    myFile.close()

    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt")
        dest = src + ".bak"
        shutil.copy(src, dest)

        #rename file
        os.rename("textfile.txt", "newfile.txt")

        #make a zip folder
        # if path.exists("textfile.txt.bak"):
        #     root_dir, tail = path.split(src)
        #     shutil.make_archive("archive", "zip", root_dir)

        #zip with select files
        with ZipFile("testzip.zip", "w") as newzip: #no need to file.close when using 'with'
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")

main()