def function1():
    print("this is a function.")

function1()
print(function1()) #runs function and also returns None because there is no return value

def argfunction(arg1, arg2):
    print(arg1," ", arg2)

argfunction("Hello", "World")

def cube(x):
    return x * x * x #returns a value

print(cube(2))

def power(base, exponent=1): #exponent is set as a default value
    result = 1;
    for i in range(exponent):
        result = result * base
    return result

print(power(2))
print(power(2,3))

def multi_add(*args): #variable number of arguments
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(1,12,3))
