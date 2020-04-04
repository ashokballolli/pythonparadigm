import datetime as datetime

currentDateTime = datetime.datetime.now()

print("current date time is ", currentDateTime)

x=10
y="10"
z=10.2
m='10'

print(type(x), type(y), type(z), type(m))

# Lists
ranks = [10, 43, 23]

# Range
list01 = list(range(1, 10))
list02 = list(range(1, 10, 3))

print(list01)
print(list02)

temperatures = [10.23, 43, "bang"]
print(temperatures)

list04 = [3, 4, 5]
rainfall = [34.23, 98, "name", list04]
print(rainfall)

print(dir(list))  # what are all the things you can do with the list
# >>> help(str.upper) # detail of the function like unix command's man page

#  all the builtins functions we can use can be seen by using
print(dir(__builtins__))


username = "Python3"
print(username.lower())

# tuples
ranks_tuples = (10, 43, 23)
print(ranks_tuples)

#  List are mutable but tuples are not
# Tuples are bit faster than the list

