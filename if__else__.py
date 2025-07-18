"""Module providing a function printing python version."""

import sys

A = 33
B = 200
C = 500

if B > A:
    print("b is greater than a.")

# elif a.k.a else if
if A > B:
    print("a is greater than b.")
elif A == B:
    print("a and b are equal.")


# else
if A > B:
    print("a is greater than b.")
elif A == B:
    print("a and b are equal.")
else:
    print("b is greater than a")


# short hand if
# if A > B: print("a is greater than b")

# short hand if ... else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
# print("A") if a > b else print("B")

# ternary operator
# print("A") if a > v else print("=") if a == b else print("B")

# combine if with logical operator

# AND
if A > B and B < C:
    print("Why not both")

# OR
if A > B or B < C:
    print("At least one of the conditions is True")

# NOT
if not A > B:
    print("a is NOT greater than b")


# nested if
X = 41
if X > 10:
    print("Above ten")
    if X > 20:
        print("Above twenty")
    else:
        print("Below twenty")


# pass statement
# if statement cannot be empty, if you want to pass, add pass to exec code
Y = 33
M = 200

if M > Y:
    pass
