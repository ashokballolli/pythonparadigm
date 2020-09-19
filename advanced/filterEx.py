
# filter(function_which_returns_bool, seq)

input_list = [1, 2, 3, 4, 5, 6]
print("input_list : ", input_list)

list_even = filter(lambda x: x%2==0, input_list)
print("even_numbers : ", list_even)
print("even_numbers : ", list(list_even))


# using list comprehension
list_even02 = [x for x in input_list if x%2 == 0]
print("even_numbers 02 : ", list(list_even02))


# intersection of 2 lists
list01 = [1, 3, 4, 5, 7]
list02 = [2, 3, 5, 6]

common_list = filter(lambda x: x in list01, list02)
print("intersection list: ", list(common_list))