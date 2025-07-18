# normal function
from os import error


def my_function():
    print("Hello world!")


# call the function
my_function()


# add argument aka args
def my_function_a(fname):
    print(fname + " Refsnes")


my_function_a("Bobi")

# * function must be called by the correct args
# * no more, no less
# * it will be error


# Arbitrary Arguments, *args


def my_function_c(*kids):
    print("The youngest child is " + kids[2])


# * add '*' in front of the args if you don't know
# * how many argument you want to pass

my_function_c("Emil", "Tobias", "Linus")


# Keyword args
def my_function_x(child3, child2, child1):
    print("The youngest child is " + child3)


my_function_x(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword Arguments, **kwargs
# * add '**' before param name
# * if you don't know how many keys argument you want pass
def my_function_kid(**kid):
    print("His last name is " + kid["lname"])


my_function_kid(fname="Tobias", lname="Refsnes")

# def example(a, b, c) -> None:
#     print(a, b, c)

# or

# def example(*, a=None, b=None, c=None):
# use a, b, c
#     print(a, b, c)


# params = {"a": 1, "b": 2, "c": 3}


# example(**params)


# default value
def my_def_value(country="indonesia"):
    print("i am from " + country)


my_def_value()
my_def_value("swiss")


# Passing a List as an Argument
def my_food(food):
    print(food)
    for x in food:
        print(x)


food = ["bonteng", "wortel", "kemiri"]

my_food(food)

# return values


def return_value(x):
    return 5 * x


print(return_value(20))

# the pass statement


def pass_statement():
    pass


pass_statement()

# * if you don't want to return any content for some reason
# * you can add pass inside the function to avoid error


# Positional-Only Arguments
def positional_only(x, /):
    print(x)


# * if there is a function with two argument, but the function only use one
# * replace the unused argument to "/"

# not error
# def my_function(x):
#   print(x)

# my_function(x = 3)

# error
# def my_function(x,/):
#   print(x)

# my_function(x = 3)

# not error
# def my_function(x,/):
#   print(x)

# my_function(3)
