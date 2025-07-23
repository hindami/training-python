import re


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")


# z = re.findall("[a-c]", txt)
# print(z)


# xi = re.search("a", txt)
# print(xi.start())

# xii = re.search("\s", txt)
# print(xii.start())

# the findall()

xiii = re.findall("ai", txt)
print(xiii)  # return a list of all match

xiv = re.findall("portugal", txt)
print(xiv)  # return [] if no match was found

# the search()
# search the string for a match, and return match objects if there is a match
# if no match, return None
xv = re.search("\s", txt)
print(xv)

xy = re.search("portugal", txt)
print(xy)
