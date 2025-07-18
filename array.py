cars = ["toyota", "honda", "suzuki"]
x = cars[0]

print(x)

print(len(cars))

for x in cars:
    print(x)

# adding data and put it on the last element
cars.append("BYD")
cars.append("BYD")
cars.append("BYD")

print(cars)

# delete specified data on array
cars.pop(1)  # delete data on index 2

print(cars)

cars.remove("BYD")

# can delete with specified value
# but if there is multiple data with the same value,
# only one data will removed (first occurence)
print(cars)
