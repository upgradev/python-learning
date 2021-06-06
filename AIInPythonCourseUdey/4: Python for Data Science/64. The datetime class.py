# datetime class contains information on both date and time

from datetime import datetime

a = datetime(year=1993, month=5, day=10)
print(a)

b = datetime(year=1993, month=5, day=10, hour=12, minute=43, second=43, microsecond=43213)
print(b)

print(b.minute)

today = datetime.now()
print(today)