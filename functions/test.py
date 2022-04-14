from faker import Faker

from functions.spcalendar.spdate import SPDate
from spcalendar.spcalendar import is_leap
from spcalendar.spcalendar import number_of_days_in_month
from spcalendar.spcalendar import odd_days_in_month
from spcalendar.spcalendar import odd_days_in_century
from spcalendar.spcalendar import decode_month
from spcalendar.spcalendar import decode_day_str
from spcalendar.spcalendar import decode_day_int

import random

fake = Faker()


def generate_random_date():
    random_fake_date = fake.date_between(start_date='today', end_date='+30y')
    spdate = SPDate(random_fake_date.year, random_fake_date.month, random_fake_date.day)
    return spdate


century = random.randrange(1, 22) * 100
dt = generate_random_date()

# TODO: Print pretty formatted spdate
print(f"Date: {dt} | type : {type(dt)}")

print(f"Is {dt.year} leap? {is_leap(dt.year)}")
print(f'Max Days in {decode_month(dt.month)}: {number_of_days_in_month(dt.month, dt.year)}')
print(f'Odd days in {decode_month(dt.month)}: {odd_days_in_month(dt.month, dt.year)}')
print(f'Century under test: {century}')
print(f'Odd days in {century} century: {odd_days_in_century(century)}')

print(f"Decode Month to string: {decode_month(dt.month)}")

# TODO: Implement isoweekday logic
print(f"isoweekday :  {dt.isoweekday()}")
print(f"weekday as string :  {decode_day_str(dt.isoweekday())}")
print(f"weekday as integer :  {decode_day_int(decode_day_str(dt.isoweekday()))}")


