# create module


import tr_module
from tr_module import person1

# import tr_module as mymodule
# * you create an alias when you import a module, by using the 'as' word
# * you can only import one thing from module

tr_module.greeting("John doe")  # mymodule.greeting("John doe")
a = tr_module.person1["age"]
b = person1["age"]  # when you can only person1

print(a, b)


# the dir function is the way to see a list what inside the module
print(dir(tr_module))
