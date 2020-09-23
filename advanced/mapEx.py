# map(func, seq)

input_list = [1, 2, 3, 4, 5]
print("input_list : ", input_list)
# get a list by multiplieng eacch element by 2

result1 = map(lambda x: x*2, input_list)
print("result1 : ", result1)
print("result1 : ", list(result1))

# using list comprehension
result2 = [x*2 for x in input_list]
print("result2 : ", result2)
