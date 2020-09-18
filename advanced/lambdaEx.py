"""
Lambda Functions == Anonymous Functions
lambda arguments: expression

Being anonymous, lambda functions can be easily passed without being assigned to a variable.
Lambda functions are inline functions and thus execute comparatively faster.
Many times lambda functions make code much more readable by avoiding the logical jumps caused by function calls
"""
sqr = lambda x: x ** 2
reminder3 = lambda x: x % 3
sqr2 = lambda _: _ ** 2

def sort_examples():
    # Sort the 2d list based on their key / value / sum / diff / reverse etc
    points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
    print("original list : ", points2D)
    # based on the key
    points2D_sort_key = sorted(points2D)
    print("sort by key : ", points2D_sort_key)

    # based on the value
    points2D_sort_value = sorted(points2D, key=lambda x: x[1])  # x[1] indicates the end value in eacch tuple
    print("sort by value : ", points2D_sort_value)

    # based on the sum of the tuple
    points2D_sort_sum = sorted(points2D, key=lambda x: x[0] + x[1])
    print("sort by sum : ", points2D_sort_sum)

    points2D_sort_sum_v2 = sorted(points2D, key = lambda _: _[0] + _[1])
    print("sort by sum v2 : ", points2D_sort_sum_v2)

    # based on the diff of tuple values, in reverse order
    points2D_sort_diff_reverse = sorted(points2D, key=lambda x: abs(x[0] - x[1]), reverse=True)
    print("sort by diff in reverse order : ", points2D_sort_diff_reverse)

    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sort_even_first = sorted(nums, key= lambda x: x%2)
    print("sort even first : ", sort_even_first)

# Print powers using Anonymous Function in Python
def print_powers():
    num = 10
    print(list(map(lambda x: 2 ** x, range(num))))

def nested_lambda():
    square = lambda x: x ** 2
    product = lambda f, n: lambda x: f(x) * n

    ans = product(square, 2)(10)
    print(ans)

print(sqr(5))
print(reminder3(11))
print(sqr2(7))
sort_examples()
print_powers()
nested_lambda()