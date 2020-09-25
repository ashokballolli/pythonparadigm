"""
reduce(function, seq)
reduce is available as part of the module functools
reduce() works by calling the function we passed for the first two items in the sequence.
The result returned by the function is used in another call to function alongside with the next (third in this case), element.
"""
from functools import reduce

input_list = [1, 2, 3, 4]
print("input_list : ", input_list)

mult = reduce(lambda x,y: x*y, input_list)
sum = reduce(lambda x, y: x+y, input_list)
print("mult : ", mult)
print("sum : ", sum)


# Find the Number Occurring Odd Number of Times using Lambda expression and reduce function
arr = [1, 2, 3, 2, 3, 1, 3]

res = reduce(lambda a, b: a ^ b, arr)
print(res)