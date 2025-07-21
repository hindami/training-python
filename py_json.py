import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x
y = json.loads(x)

# result
print(y["age"])


# a Python object (dict):
z = {"name": "John", "age": 30, "city": "New York"}

zi = json.dumps(z)

print(zi)

d = x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

di = json.dumps(d, indent=4, separators=(". ", " = "), sort_keys=True)

print(di)
