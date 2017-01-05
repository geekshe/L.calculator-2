"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

vars = raw_input("Enter operation you'd like and that numbers to use: \n")


def calculator(operator, num1, num2):
    """Calculate numbers"""

    if operator == "+":
        print add(num1, num2)
    elif operator == "-":
        print subtract(num1, num2)
    elif operator == "*":
        print multiply(num1, num2)
    elif operator == "/":
        print divide(num1, num2)
    elif operator == "square":
        print square(num1)
    elif operator == "cube":
        print cube(num1)
    elif operator == "pow":
        print power(num1, num2)
    elif operator == "mod":
        print mod(num1, num2)
    else:
        print "Bye"

while vars != "q":

    calcs = vars.split(" ")
    print calcs
    operator = calcs[0]
    num1 = int(calcs[1])
    if len(calcs) == 2:
        num2 = 1
    calculator(operator, num1, num2)
    vars = raw_input("Enter another calculation or q to quit: \n")
