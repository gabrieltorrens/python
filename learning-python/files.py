def main():
    myFile = open("textfile.txt", "w+") #w+ write mode and create if does not exist
    for i in range(10):
        myFile.write("This is new text\n")
    myFile.close()

    myFile = open("textfile.txt", "a+")
    for i in range(10):
        myFile.write("This is new text\n")
    myFile.close()

def backup():
    myFile = open("textfile.txt", "r")
    if myFile.mode == 'r':
        content = myFile.read()
        print(content)
        
        fileLines = myFile.readlines() #sends lines to a list
        for i in fileLines:
            print(i)

main()
backup()