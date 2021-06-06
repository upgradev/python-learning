from datetime import date

my_date = date(year=1998, month=7, day=19)
print(f"Date is {my_date}")

print(date.today())

print(date.today().month)


# time class
from datetime import time

mytime = time(hour=12, minute=30, second=45)
print(mytime)

mytie = time(minute=15)
print(mytie)