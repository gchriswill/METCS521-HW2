"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/22/2020
Homework Problem: #2
Description:

A program that takes input and outputs this as a string, as integer,
and as floating-point value.

"""


# Performs the gathering of input
input_value = input("Please enter a value:")

# Performs validation for if no value was provided
if input_value != "":

    # Preforms output to console as string
    as_string = str(input_value)
    print(as_string)

    # Preforms output to console as integer
    if input_value.isnumeric():
        as_int = int(input_value)
        print(as_int)

    # Preforms output to console as float
    if input_value.isdecimal():
        as_float = float(input_value)
        print(as_float)

else:
    # Preforms output to console for invalid input message
    print("No value was provided!")

"""
Primitive and Collection types can be sent through input and be printed 
without generating any errors. 
"""
