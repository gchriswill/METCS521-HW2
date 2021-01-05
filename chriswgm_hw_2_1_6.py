"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/22/2020
Homework Problem: #6
Description:

A program that calculate and prints the leaps years from 1900 to 2020
inclusively, using both, a `for` loop and `while` loop, separated from each
other processes and outputs.

Notes:

A leap year is exactly divisible by 4 except for century years.
The century year is a leap year only if it is perfectly divisible by 400.

"""


# IMPORTANT NOTE:
# This implementation is redundant because the range() function can achieve this
# the requirements. Example: `range(1900, 2020, 4)`
#
# Also, the Calendar library can detect if a given year is leap.
# Example calendar.isleap()


# Performing a function for calculating if a given year is leap and returning
# the result as boolean
def leap_year(y):

    # Performing first requirement of manual leap calculation
    first_leap_req = y % 4 == 0

    # Performing the second requirement of manual leap calculation
    second_leap_req = y % 100 != 0

    # Performing the third requirement of a manual leap calculation
    third_leap_req = y % 400 == 0

    # Performing all the requirements in conditional validation and returning
    # the results
    return (first_leap_req and second_leap_req) or third_leap_req


# Performing `for` loop for iteration against inclusive range
for i in range(1900, 2020+1):

    if leap_year(i):
        print(i)


# Performing `while` loop for iteration against inclusive condition
i = 1900
while i <= 2020:

    if leap_year(i):
        print(i)

    i += 1
