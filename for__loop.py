fruits = ["apple", "banana", "cherry"]
adj = ["red", "big", "tasty"]

for x in fruits:
    print(x)

# looping Through a String

for y in "banana":
    print(y)

# the break statement

for x in fruits:
    print(x)
    if x == "banana":
        break

for x in fruits:
    if x == "banana":
        break
    print(x)

# the continue statement
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range
for x in range(6):  # 0,1,2,3,4,5
    print(x)

for x in range(2, 6):  # 2,3,4,5
    print(x)

for x in range(2, 30, 3):  # 2,5,8,11,14,17,20,23,26,29
    print(x)

# Else in For Loop

for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")
# else block will not executed if there is break in loop


# nested loops
for x in adj:
    for y in fruits:
        print(x, y)

# pass statement
for x in [0, 1, 2]:
    pass

# if you want to pass the loop without return value
# or with empty value
