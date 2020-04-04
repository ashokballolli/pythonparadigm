


# list comprehension

def onlyNumbers(inList):
    new_list = [item for item in inList if isinstance(item, str) == False]
    return new_list

def onlyPositiveNumners(inList):
    new_list = [item for item in inList if isinstance(item, str) == False and item > 0]
    return new_list

print(onlyNumbers([34, 56, "dsfsf", 45, 4.43, -435, -34.65]))
print(onlyPositiveNumners([34, 56, "dsfsf", 45, 4.43, -435, -34.65]))

# if you want only numbers and if there is -9999 then replace it with 0

def onlyNumbersv2(inList):
    new_list = [item/10 if item != -9999 else 0 for item in inList]
    return new_list

print(onlyNumbersv2([34, 56, -9999, 45, 49.43, -435, -34.65]))


# define a function which takes the list which containes both int and strings and returns the list with the same int and 0 instead of the strings
def replaceStringWithZero(inList):
    new_list = [item if isinstance(item, int) else 0 for item in inList]
    return new_list

print(replaceStringWithZero([34, 56, "dsfsf", 45, 4, -435, -34]))

# Define a function which returns the sum of the list and input list containes the numbers in string format
def sumOfList(inList):
    new_list = [float(item) for item in inList]
    return sum(new_list)

# Default/non default parameters and keyword and non-keyword arguments
def area01(a, b):
    return a * b

print(area01(2, 3))
print(area01(a=2, b=3))
print(area01(b=3, a=2))

def area02(a, b=4):
    return a * b;

print(area02(2))
print(area02(2, 3))

# default arguments should follow the non-default arguments
# can not define the following function
# def area03(a=4, b):
#     return a * b;

# defince a function which takes any number of arguments like print(1, 3, 5, 2, "sdf")

def nArgFun(*args):
    return sum(args)

print(nArgFun(1, 3, 4))
print(nArgFun(1, 3, 4, 5, 2, 5))

def nParameter(*args):
    new_list = [item.upper() for item in args]
    print(new_list)
    return sorted(new_list)

print(nParameter("snow", "glacier", "iceberg"))

# Indefinete number of keyword arguments
def find_sum(**kwargs):
    return sum(kwargs.values())

print(find_sum(a=3, b=4, c=2))