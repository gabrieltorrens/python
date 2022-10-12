try:
    x=10/0
except:
    print("exception triggered")


try:
    answer = input("What should I divide 10 by")
    num = int(answer)
    print(10/num)
except ZeroDivisionError as exception:
    print("You can't div by zero")
except ValueError as exception:
    print("invalid input. please try again.")
    print(exception)
finally:
    print("'finally' code will always run")