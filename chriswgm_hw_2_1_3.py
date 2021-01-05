"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/22/2020
Homework Problem: #3
Description:

A program that take an integer input, computes its value with the
provided formula and prints the the formula with its result to the console.
Math Formula format: n + n*n + n*n*n + n*n*n*n = ?

"""


# Performs the gathering of input
input_int = input("Please enter a number:")

# Performs validation for if no value was provided
if input_int != "":

    # Performs validation for integer type
    if input_int.isnumeric():

        # Performing casting the input into integer and storing it
        i_val = int(input_int)

        # Performing formula programmatically and storing the results
        computed_value = i_val + (i_val ** 2) + (i_val ** 3) + (i_val ** 4)

        # Performing grouping math operators for building the formula in string
        math_ops = "+*+**+***="

        # Performing the initialization of string storage for further use in
        # building the formula in a string format
        formula_str = ""

        # Performing process for building the formula in string value by
        # concatenating each operator with the value of input.
        for c in math_ops:

            # Performing concatenation
            formula_str += "{}{}".format(i_val, c)

            # Performing check for last character and ensures that last
            # character meets the requirements for to be the "="
            if c is math_ops[-1] and c is "=":
                formula_str += "{}".format(computed_value)

        # Performs the output for formula and result to console as string
        print(formula_str)

    else:

        # Preforms output to console for invalid input message
        print("The value has to be a number!")

else:

    # Preforms output to console for invalid input message
    print("No value was provided!")
