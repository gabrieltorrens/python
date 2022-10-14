from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#date deltas
print(timedelta(days=365, hours=8, minutes=2)) #365 days, 8:02:00

now = datetime.now()
print(now)
print(now+timedelta(days=365)) #prints one year from now

print("In two weeks and three days it will be:", now+timedelta(weeks=2, days=3))

#time deltas
t = datetime.now() - timedelta(weeks=1)
print(t.strftime("One week ago it was %A %B %d %Y"))

#How many days until Halloween
today = date.today()
hallo = date(today.year, 10, 31)

print(today)
print(hallo)

if hallo < today:
    print("Halloween was", ((today-hallo).days), "days ago")
    hallo = hallo.replace(year= today.year+1)
    daysToNextHallo = hallo - today
    print("Next Halloween is", daysToNextHallo.days, "days from now")
else:
    print("Halloween is",((hallo-today).days), "days from now")