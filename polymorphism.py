class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

# because polymorphism, we can execute the same method for all three class


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Cars(Vehicle):
    pass


class Boats(Vehicle):
    def move(self):
        print("Sail!")


class Planes(Vehicle):
    def move(self):
        print("Fly!")


car2 = Cars("Ford", "Mustang")  # Create a Car object
boat2 = Boats("Ibiza", "Touring 20")  # Create a Boat object
plane2 = Planes("Boeing", "747")

for x in (car2, boat2, plane2):
    print(x.brand)
    print(x.model)
    x.move()
