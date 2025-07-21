import datetime


x = datetime.datetime.now()

# date output

print(x)
print(x.year)
print(x.strftime("%A"))  # display day full

# create date objects
y = datetime.datetime(2020, 5, 17)
print(y)

# the strftime method
r = datetime.datetime(2018, 6, 1)
print(r.strftime("%B"))  # display month full
