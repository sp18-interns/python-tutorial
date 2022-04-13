def is_leap(year):
    """
    Description: Given an integer year in the input, it should return a boolean
    signifying whether the given year is a year or not.
    Input: year (integer)
    Ouput: boolean (leap or not)
    """
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
