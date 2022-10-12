str = "This is text"
list = [0, "uno", 2, 3.14, False]
tuple = (0, 1, 2)
dict = {"keyOne" : 1, "keyTwo" : 2}

print(str)
print(list)
print(tuple)
print(dict)

#accessing lists, tuples, dictionaries
print(list[3])
print(tuple[0])
print(dict["keyOne"])

print(list[1:5]) #slices
print(list[1:5:2]) #with step value

print(list[::-1]) #reverses sequence


# Global and local variables
def myFunction():
    #global str #imports global variable
    str = "new value"
    print(str)

myFunction()
print(f"str's global value is '{str}'")