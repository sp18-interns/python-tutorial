from faker import Faker
from spcalendar.spcalendar import is_leap
from spcalendar.spcalendar import number_of_days_in_month
from spcalendar.spcalendar import odd_days_in_month
from spcalendar.spcalendar import odd_days_in_century
from spcalendar.spcalendar import decode_month
from spcalendar.spcalendar import decode_day
import datetime

import random

fake = Faker()


def generate_random_date():
    return fake.date_between(start_date='today', end_date='+30y')


century = random.randrange(1, 22)*100
dt = generate_random_date()
print(f"Date: {dt}")

print(f"Is leap year? - {is_leap(dt.year)}")
print(
    f'The number of days in the month is- {number_of_days_in_month(dt.year,dt.month)}')
print(f'Total odd days in month {dt.month} is {odd_days_in_month(dt.month)}')
print(f'The century is {century}')
print(f'The no. of odd days in {century} is {odd_days_in_century(century)}')

print(f"Decode Month to string :  - {decode_month(dt.month)}")

print()