"""

Student: Christopher W Gonzalez Melendez
Class: CS 521 - Summer 2
Date: 07/22/2020
Homework Problem: #5
Description:

An interactive program within that executes in the Python console, that gathers
weight and height input with Metric format, validates this input in
PRE/POST stages, extract the needed values from this input and use these values
to perform a calculation using BMI formula, and outputs the formula results.

BMI Formula format: weight / (height^2)

"""

import re

input_msg = "Enter your weight and height using Metric format (kg,cm):"
SUCC = "\033[94m"
FAIL = "\033[91m"
ENDC = "\033[0m"

err_msg_no_value = "No value was provided!"
err_msg_needs_kg = "Ensure you're including \"kg\" Metrics acronyms"
err_msg_needs_cm = "Ensure you're including \"cm\" Metrics acronyms"
err_msg_order = "Values are not following formatting order: \"kg\" then \"cm\""
err_msg_no_numbers = "Please enter the weight and height numeric values!"
err_msg_too_many_numbers = "Please enter no more than weight and height values!"

err_msg_w_format = "Ensure you're including \"kg\" " + \
                   "(Metrics wight acronym) left side next its value: " + \
                   "\"<your weight>kg\""

err_msg_h_format = "Ensure you're including \"cm\" " + \
                   "(Metrics height acronym) left side next its value: " + \
                   "\"<your height>cm\""


# Print function for printing error with error formatting
def print_err(msg):
    print("\n\t" + FAIL + msg + ENDC + "\n")


# Input function for repeating operation when error occurs
def input_caller(msg_param):
    input_val = input(str(msg_param))
    return input_parser(input_val)


def input_pre_validator(input_param):

    # Validation for if no value was provided
    if input_param is "":
        print_err(err_msg_no_value)
        return None

    # Validation for if no Weight/height acronyms values were provided
    if not input_param.__contains__("kg"):
        print_err(err_msg_needs_kg)
        return None

    if not input_param.__contains__("cm"):
        print_err(err_msg_needs_cm)
        return None

    # Validation for if the order of the values does not match BMI formula
    if input_param.find("kg") > input_param.find("cm"):
        print_err(err_msg_order)
        return None

    # Returns string with verified value
    return input_param


def input_extractor(input_param):

    # Search for numbers in string, group these in collection and stores
    # them in property for easy and convenient access
    raw_values = [str(s) for s in re.findall(r"-?\d+\.?\d*", input_param)]

    # Check if the collection is empty
    if len(raw_values) <= 1:
        print_err(err_msg_no_numbers)
        return None

    # Check if the collection contains more than to items
    if len(raw_values) >= 3:
        print_err(err_msg_too_many_numbers)
        return None

    # Returns list with verified values
    return raw_values


def input_post_validator(input_values, input_full_value):

    # Storage of individual items from collection for easy access
    weight_val = input_values[0]
    height_val = input_values[1]

    # Checking if integer or float from string and casting to the correct
    # number type
    if weight_val.isnumeric():
        weight_val = int(weight_val)
    else:
        if weight_val.isdecimal():
            weight_val = float(weight_val)

    if height_val.isnumeric():
        height_val = int(height_val)
    else:
        if height_val.isdecimal():
            height_val = float(height_val)

    # Validates for specific Metrics format alongside values
    chk_w_format = input_full_value.__contains__("{}kg".format(weight_val))
    chk_h_format = input_full_value.__contains__("{}cm".format(height_val))

    # Performs check validation for specific weight Metrics format
    if not chk_w_format:
        print_err(err_msg_w_format)

        return None

    # Performs check validation for specific height Metrics format
    if not chk_h_format:
        print_err(err_msg_h_format)

        return None

    # Returns dictionary with verified values
    return {"height": height_val, "weight": weight_val}


def input_parser(input_param):

    # Performing pre-validation for input and storing result
    input_val = input_pre_validator(input_param)

    # Forwarding None is pre-validation fails
    if input_val is None:
        return input_val

    # Performing extraction from input and storing result
    raw_values = input_extractor(input_val)

    # Forwarding None is extraction fails
    if raw_values is None:
        return raw_values

    # Performing post-validation for extracted values and storing result
    inputs_col = input_post_validator(raw_values, input_val)

    # Forwarding None is post-validation fails
    if inputs_col is None:
        return inputs_col

    # Returns dictionary with verified and parsed values
    return inputs_col


def bmi(wh_param):

    # Storing to local scoped variable for mutability
    wh_values = wh_param

    if wh_values is None:
        wh_values = input_caller(input_msg)
        bmi(wh_values)

    # Storage of individual items from collection for easy access
    w_val = wh_values["weight"]
    h_val = wh_values["height"]

    # Performing conversion of "centimeters to meters" and stores it
    height_meters_val = h_val / 100

    # Performing BMI operation
    bmi_ops = w_val / (height_meters_val ** 2)

    # Performs the output with BIM results
    print("\n\t" + SUCC + "Your BMI is: {}".format(bmi_ops) + ENDC + "\n")

    # Restarting BMI program to initial step
    wh_values = input_caller(input_msg)
    bmi(wh_values)


# Performs the gathering of input and starting point of BMI process flow
bmi(input_caller(input_msg))
