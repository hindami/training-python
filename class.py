# create a Class


class MyClass:
    x = 5


print(MyClass)
# * <class '__main__.MyClass'>

# create object

p1 = MyClass()

print(p1.x)
# * 5


# __init__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# * __init__(self) always there when initialize class and called automatically


# __str__(self)


class Personstr:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p2 = Personstr("John", 36)
print(p2)


# object methods


class Personmet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p3 = Personmet("John", 36)

print(p3.myfunc())

# * self param is the way to access the variable belong to the class
# * you can named self whatever you want, but
# * it has to be the first parameter of any func in the class


# Self parameter
class Personself:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(nany):
        print(f"{nany.name}({nany.age})")

    # * you can change name 'self' but linter cannot allow that


p4 = Personself("John", 36)


p4.myfunc()


# Modify object properties
p4.age = 40
p4.myfunc()

# delete object properties
del p4.age

p4.myfunc()

# delete objects
del p4

p4.myfunc()

# pass statement
# * class cannot be empty, but for some reason the class should be empty
# * you can use pass


class Personpass:
    pass


p5 = Personpass()

print(p5)
