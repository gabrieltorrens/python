import calendar

#create a text calendar
cal = calendar.TextCalendar(calendar.SUNDAY) #create a calendar where the week begins on Sunday
calstr = cal.formatmonth(2022, 1, 0, 0)
print(calstr)
#print(cal.formatmonth(2022, 1, 0, 0)) # calendar as text string

htmlCal = calendar.HTMLCalendar(calendar.SUNDAY)
calstr = htmlCal.formatmonth(2011, 1)
print(calstr)

for i in cal.itermonthdates(2022,8): #returns each day in the month as a date
    print(i)

for i in cal.itermonthdays(2022,8): #returns each day in the month as a number
    print(i)

for name in calendar.month_name: #prints all months based off locale
    print(name)

for day in calendar.day_name: #prints all days based off locale
    print(day)

#find first friday of each month

for month in range(1,12): #months 1 to 12
    cal = calendar.monthcalendar(2022, month)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0: #if Friday value = 0 then the first Friday is in week 2
        meetingday = weekone[calendar.FRIDAY]
    else:
        meetingday = weektwo[calendar.FRIDAY]

    print(calendar.month_name[month], meetingday)