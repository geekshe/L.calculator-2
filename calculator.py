"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

raw_list = raw_input("Enter operation you'd like and that numbers to use: \n")


def calculator(operator, nums_only):
    """Calculate numbers"""

    if operator == "+":
        print reduce(add, nums_only)
    elif operator == "-":
        print reduce(subtract, nums_only)
    elif operator == "*":
        print reduce(multiply, nums_only)
    elif operator == "/":
        print reduce(divide, nums_only)
    elif operator == "square":
        print square(num1)
    elif operator == "cube":
        print cube(num1)
    elif operator == "pow":
        print reduce(power, nums_only)
    elif operator == "mod":
        print reduce(mod, nums_only)
    else:
        print "Bye"

while raw_list != "q":

    calcs = raw_list.split(" ")
    print calcs
    operator = calcs[0]
    print "Operator: {}".format(operator)
    nums_only = calcs[1:]
    print "Still strings: {}".format(nums_only)
    nums_only = map(int, nums_only)
    print type(nums_only[0])

    # num1 = int(calcs[1])
    # if len(calcs) == 2:
    #     num2 = 1
    if (operator == "cube" or operator == "square") and len(nums_only) > 1:
        print "You can't use that calculation with more than one number."
    else:
        calculator(operator, nums_only)
    raw_list = raw_input("Enter another calculation or q to quit: \n")
