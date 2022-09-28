def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('you cant div by zero')

print(div42by(2))
print(div42by(0))
print(div42by(1))

print('how many cats?')
numCats = input()

if int(numCats) >= 4:
    print('thats a lot of cats')
else:
    print('not a lot of cats')