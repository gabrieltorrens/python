from datetime import date, datetime

now = datetime.now()

print(now.strftime("The year is %Y")) #allows formatting codes
print(now.strftime("%a, %d, %B, %y")) #Fri, 14, October, 22

print(now.strftime("Locale date and time: %c"))
print(now.strftime("Locale date and time: %x %X"))

print(now.strftime("%I:%M %p")) #AM/PM
print(now.strftime("%H:%M")) #24 hour clock