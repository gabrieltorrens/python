import calendar

day = int(input("""What day of the week do you want to count?
0: Monday
1: Tuesday
2: Wednesday
3: Thursday
4: Friday
5: Saturday
6: Sunday
"""))

year = int(input("What year?"))
month = int(input("What month?"))

cal = calendar.monthcalendar(year, month) #returns weeks as lists

count=0
for week in cal:
    if week[day]!=0: #if week[4 for Friday] is not 0, then there's a Friday in the week's list
        count += 1

print(f"There are {count} of that day")