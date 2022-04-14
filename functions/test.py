from faker import Faker
from spcalendar.spcalendar import is_leap
from spcalendar.spcalendar import decode_month
from spcalendar.spcalendar import decode_day
import datetime
fake = Faker()

def generate_random_date():
    return fake.date_between(start_date='today', end_date='+30y')

dt = generate_random_date()
print(f"Date: {dt}")

print(f"Is leap year? - {is_leap(dt.year)}")

print(f"Decode Month to string :  - {decode_month(dt.month)}")

#print(f"the weekday is : - {dt.dayofweek}")