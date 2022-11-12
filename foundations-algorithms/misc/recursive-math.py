def power(x, pow):
    if pow == 0: #starting with breaking condition
        return 1
    else:
        return x*power(x, pow-1)

#4! = 4*3*2*1
def factorial(x):
    if x==0:
        return 1
    else:
        return x * factorial(x-1)

print("{} to the power of {} is {}".format(4,3, power(4,3)))
print("{}! is {}".format(4,factorial(4)))