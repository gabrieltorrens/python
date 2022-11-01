def countdown(a):
    if a == 0:
        print("DONE")
        return
    else:
        print(a)
        countdown(a-1)
        print("this still prints because the call stack is unwound after 'return'")

countdown(5)