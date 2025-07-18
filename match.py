"""Module providing a function printing python version."""

import sys


def print_python_version():
    print(sys.version)


# syntax

# match expression:
#     case x:
#         code block
#     case y:
#         code block
#     case z:
#         code block

DAY = 10
match DAY:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# default
DAY_D = 4
match DAY_D:
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

    # use _ for block when there are not other matches
    case _:
        print("looking forward to the weekend")

# combined
DAY_C = 7
match DAY_C:
    case 1 | 2 | 3 | 4 | 5:
        print("It's weekday")
    case 6 | 7:
        print("I love weekend")


# if statement as guard
MONTH_G = 5
DAY_G = 1
match DAY_G:
    case 1 | 2 | 3 | 4 | 5 if MONTH_G == 4:
        print("A week in April")
    case 1 | 2 | 3 | 4 | 5 if MONTH_G == 5:
        print("A week in May")
    case _:
        print("No match")
