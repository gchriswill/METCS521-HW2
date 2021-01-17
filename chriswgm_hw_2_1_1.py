"""


Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/22/2020
Homework Problem: #1
Description:

A program that takes input as number to perform sum,
multiplication, subtraction, and division operations for demonstrating the
use of operators. It checks whether the input matches entry value against a
final result, and also prints this result alongside a descriptive message.

"""


# Imports Copy Library
import copy


# Performs the gathering of input
input_str = input("Please enter a number:")

# Performs validation for if no value was provided
if input_str != "":

    # Performs validation for a multiple number types
    if input_str.isnumeric() or input_str.isdecimal():

        # Performs Cast input to float for better precision
        entry = float(input_str)

        # Performs Copy the entry value for performing math operations
        ops = copy.deepcopy(entry)

        # Performs Sum and Assigment operation
        ops += 2

        # Performs Multiplication and Assigment operation
        ops *= 3

        # Performs Subtraction and Assignment operation
        ops -= 6

        # Perform Division and Assignment operation
        ops /= 3

        # Performs conditional check and stores it in variable
        matching = entry == ops

        # Performs storing long string in variable
        msg = "Chris's results - HW 2.1.1: Entry Value == result Value: "

        # Performs validation of conditional check
        # This IF statement is redundant, just following homework instructions
        if matching:

            # Preforms output to console for message and matching check
            print(msg, matching)
        else:

            # Preforms output to console for message and matching check
            print(msg, matching)
    else:

        # Preforms output to console for invalid input message
        print("The value has to be a number!")
else:

    # Preforms output to console for invalid input message
    print("No value was provided!")
