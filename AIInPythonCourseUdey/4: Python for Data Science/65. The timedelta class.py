# timedelta is used calculating differences in date and  is used for date manipulations in python

from datetime import datetime, timedelta

todays_date = datetime.now()
dateafter_months = todays_date+timedelta(days=90)
print(dateafter_months)

datebefore_months = todays_date-timedelta(days=90)
print(datebefore_months)
