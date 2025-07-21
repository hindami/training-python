# scope
# a variable is only available from inside function it is created
# this is called scope


# local scope
def myfunc():
    x = 300
    print(x)


myfunc()
# ** x only can be accessed inside myfunc


def myfunc2():
    x = 300

    def myinnerfunc():
        print(x)

    myinnerfunc()


myfunc2()

# ** x can be accessed by myinnerfunc because myinnerfunc inside myfunc2
# ** or myinnerfunc is on the same location with x

# global scope

z = 100


def myfunz():
    print(z)


myfunz()

print(z)

# ** a variable created outside the function can be accessed by anyone

# naming variable
# * if there is a variable created outside the function with name 'P'
# * and there ist a variable create inside the function with name 'P'
# * python will threat them as two separate variable.

y = 500


def myfux():
    y = 400
    print(y)


myfux()
print(y)

# global keyword

# * if you need to create a global variable, but are stuck in the local scope.
# * you can use the global keyword.
# * the global keyword make the variable global


def myfnd():
    global w
    w = 7575


myfnd()
print(w)
