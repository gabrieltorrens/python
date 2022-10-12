def main():
    x = 0

    while(x<5):
        print(x)
        x = x+1

    for i in range(5,10): #stops when x=10
        print(i)

    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for day in days:
        print(day)


    #break and continue statements
    for i in range(5,10): #stops when x=10
        # if i == 7:
        #     break
        if i % 2 == 0:
            continue #returns to begining of loop if number is even
        print(i)

    #enumerate function
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i, day in enumerate(days): #enumerate function returns index number and item
        print(i,day)

if __name__ == "__main__":
    main()