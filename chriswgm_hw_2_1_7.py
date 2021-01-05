"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/22/2020
Homework Problem: #7
Description:

A program that iterates over a given range, using a loop and printing its value
of each iteration that meets a conditional validation based of any iteration
index that can divide a given number x.

Directions:

‘for loop’ as a ‘while loop’: 

for i in range(1, x + 1):

    if x % i == 0:
        print(i)

"""


# Performing assignment of x with a given number
x = 20

# Performing a `while` for iterating over a range from 1 to a given number and
# printing the iteration index value if meets the conditional requirement
# validation.
i = 1
while i <= x:

    if x % i == 0:
        print(i)

    i += 1
