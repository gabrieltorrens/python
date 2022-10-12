from collections import UserString


def palindromeCheck(testString):
    if testString == testString[::-1]:
        return True
    else:
        return False

runningState = True

while (runningState==True):
    userString = input("Enter your string or type 'exit':")
    if userString == "exit":
        break

    #format string
    formattedString = ""
    userString = userString.lower()
    for i in userString: #removes non-alphanumeric chars
        if i.isalnum():
            formattedString += i
    
    if palindromeCheck(formattedString):
        print("it's a palindrome")
    else:
        print("not a palindrome")