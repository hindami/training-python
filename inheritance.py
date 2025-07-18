# create parent class


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("Hindami", "Muhammad")
x.printname()


# create child class
class Student(Person):
    pass


# * use pass if you don't want to add any properties or methods class

y = Student("Karina", "Kapur")
y.printname()


# __init__
class Studentone(Person):
    def __init__(self, fname, lname):
        pass
        # add properties here


# * add __init__ on child class will override __init__ func parent class


class Studenttwo(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        # add properties here


# * if you want to inherit __init__ parent funct, follow codes above


y = Studenttwo("Mike", "Olsen")

y.printname()


# use super to make child class inherit all object property  and methods from
# it's parent
class Studentthree(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


# add properties
class Studentfour(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


x = Studentfour("Mike", "Olsen")
print(x.graduationyear)


# or
class Studentfive(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


xi = Studentfive("Mike", "Olsen", 2019)
xi.graduationyear


# add method
class Studentsix(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduatioinyear = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduatioinyear,
        )


xix = Studentsix("Mike", "Olsen", 2019)
xix.welcome()
