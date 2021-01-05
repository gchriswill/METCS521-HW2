"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/22/2020
Homework Problem: #4
Description:

A 3 liner program that takes input and prints the results, resulting with
an output of 1 or 0, being 0 for even and 1 for odd.

Line Strict Directions/Requirements:
(1) prompts for a number
(2) converts the input to an integer
(3) prints the number 0 if the user input is even and the number 1 if the
user input is odd. 

"""


# Performs the gathering of input
input_int = input("Please enter a number:")

# Performing casting the input into integer and storing it
int_val = int(input_int)

# Performs the output with modulus operator for satisfying requirement #3
print(int_val % 2)
