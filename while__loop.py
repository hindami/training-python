I = 1

while I < 6:
    print(I)
    I += 1


# the break statement
while I < 6:
    print(I)
    if I == 3:
        break
    I += 1


# the continue statement
X = 0

while X < 6:
    X += 1
    if X == 3:
        continue
    print(X)

Z = 0

while Z < 6:
    print(Z)
    Z += 1
else:
    print("Z is no longer less than 6")
