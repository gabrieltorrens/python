def main():
    myFile = open("textfile.txt", "w+") #w+ write mode and create if does not exist
    for i in range(10):
        myFile.write("This is new text\n")
    myFile.close()