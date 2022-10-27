def gcd(a,b):
    while (b != 0):
        t = a
        a = b
        b = t % b #mod of a/b, loop stops if no remainder
    return a

print(gcd(20,8))