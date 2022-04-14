from calendar import monthrange


def is_leap(year):
    """
    Description: Given an integer year in the input, it should return a boolean
    signifying whether the given year is a leap year or not.
    Input: year (integer)
    Ouput: boolean (leap or not)
    """
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


def number_of_days_in_month(year=0, month=0):
    return monthrange(year, month)[1]


def odd_days_in_month(month=0):
    """
    Description: Given an integer month in input,it should return an integer 
    signifying the total no. of odd days in the month.
    Input: month(integer)
    Output: integer(total no of odd days)
    """
    count_odd = 0
    for day in month:
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
    for year in century:
        if is_leap(year) == True:
            count_leap += 1
    total_days = 36500 + count_leap
    for day in total_days:
        if day % 2 != 0:
            count_odd += 1

    return count_odd
