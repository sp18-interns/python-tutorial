from calendar import monthrange
import datetime
import re


def is_leap(year):
    """
    Description: Given an integer year in the input, it should return a boolean
    signifying whether the given year is a leap year or not.
    Input: year (integer)
    Ouput: boolean (leap or not)
    """
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


def number_of_days_in_month(month=0, year=0):
    if month <= 0 or year <= 0:
        print("ERROR: month/year invalid. Please send positive values for month and year.")
        return -1

    dic = {1: ['January', 31], 2: ['February', 28], 3: ['March', 31], 4: ['April', 30], 5: ['May', 31], 6: ['June', 30], 7: [
        'July', 31], 8: ['August', 31], 9: ['September', 30], 10: ['October', 31], 11: ['November', 30], 12: ['December', 31]}

    if is_leap(year) and month == 2:
        return dic[2][1] + 1

    return dic[month][1]


# def number_of_days_in_month(month, year):
#     """
#     Description: Given an integer month and year as input, return the days in that month of that year.
#     Do consider that if the year is leap, it should return 29 days for February.
#     """
#     if month <= 0 or year <= 0:
#         print("ERROR: month/year invalid. Please send positive values for month and year.")
#         return -1
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     elif month in (4, 6, 9, 11):
#         return 30
#     elif month == 2:
#         if is_leap(year):
#             return 29
#         return 28
#     else:
#         print(
#             "ERROR: month invalid. Out of bound value for month. Valid range [1-12].")


def odd_days_in_month(month=0,year=0):
    """
    Description: Given an integer month in input,it should return an integer
    signifying the total no. of odd days in the month.
    Input: month(integer)
    Output: integer(total no of odd days)
    """
    no_of_days_in_month = number_of_days_in_month(month,year)
    count_odd = 0
    for day in range(1, no_of_days_in_month + 1):
        if day % 2 != 0:
            count_odd += 1
    return count_odd


def odd_days_in_century(century=0):
    """
    Description: Given an integer century in input,it should return an integer
    signifying the total no. of odd days in a century.
    Input: century(ineger)
    Output: integer(total no of odd days in a century)
    """
    count_odd = 0
    count_leap = 0
    for year in range(century - 100, century):
        if is_leap(year) == True:
            count_leap += 1
    total_days = 36500 + count_leap
    for day in range(1, total_days + 1):
        if day % 2 != 0:
            count_odd += 1

    return count_odd


def decode_month(month=0):
    """
<<<<<<< HEAD
    DESCRIPTION : Decode month number to convert to string.
    INPUT : Month generated by using random generator function.
    OUTPUT: Month Name is displayed by using month number.
=======
    DESCRIPTION : Decode month --> number to convert to string
    INPUT : Month generated by using random generator function
    OUTPUT: Month Name is displayed by using month number
>>>>>>> 1f738f773c40a6186b20a9cd5d0324aca5f2ca37
    """
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"

    # return (z, ":", calendar.month_name[z.month])


def decode_day_int(isoweekday=''):
    """
    DESCRIPTION - Convert weekday into int
    INPUT - Weekday given/generated as input
    OUTPUT - Convert weekday into integer
    """

    if isoweekday == "Monday":
        return 1
    elif isoweekday == "Tuesday":
        return 2
    elif isoweekday == "Wednesday":
        return 3
    elif isoweekday == "Thursday":
        return 4
    elif isoweekday == "Friday":
        return 5
    elif isoweekday == "Saturday":
        return 6
    elif isoweekday == "Sunday":
        return 7


def decode_day_str(isoweekday=0):
    """
    DESCRIPTION - Convert weekday into int
    INPUT - Weekday given/generated as input
    OUTPUT - Convert weekday into integer
    """

    if isoweekday == 1:
        return "Monday"
    elif isoweekday == 2:
        return "Tuesday"
    elif isoweekday == 3:
        return "Wednesday"
    elif isoweekday == 4:
        return "Thursday"
    elif isoweekday == 5:
        return "Friday"
    elif isoweekday == 6:
        return "Saturday"
    elif isoweekday == 7:
        return "Sunday"
