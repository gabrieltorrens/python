from datetime import date
from datetime import time
from datetime import datetime

#date object
today = date.today()
print(today)
print(today.day, today.month, today.year)

print(f"Today's weekday number is: {today.weekday()}")
days = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]
print(f"that is a {days[today.weekday()]}")

#datetime object
now = datetime.now()
print(now) #current date and time is

t = datetime.time(datetime.now())
print(t) #current time is

