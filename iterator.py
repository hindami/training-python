# return iterator from tuple

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# return iterator from string

mystr = "banana"
mystrit = iter(mystr)

print(next(mystrit))
print(next(mystrit))
print(next(mystrit))
print(next(mystrit))
print(next(mystrit))
print(next(mystrit))

# looping through an iterator

for x in mytuple:
    print(x)

for x in mystr:
    print(x)


# create the iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myite = iter(myclass)


print(next(myite))
print(next(myite))
print(next(myite))
print(next(myite))
print(next(myite))
print(next(myite))
print(next(myite))


class MyNumbersWithBrake:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclassbrake = MyNumbersWithBrake()
myiterbrake = iter(myclassbrake)

for x in myiterbrake:
    print(x)
