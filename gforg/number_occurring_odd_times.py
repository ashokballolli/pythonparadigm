"""
Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times. Find the number in O(n) time & constant space.
Examples :

Input : arr = {1, 2, 3, 2, 3, 1, 3}
Output : 3

Input : arr = {5, 7, 2, 7, 5, 2, 5}
Output : 5

https://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
"""
from functools import reduce

def method01(arr):
    l = len(arr)

    for i in range(l):
        count = 0
        for j in range(l):
            if arr[i] == arr[j]:
                count += 1
        if count % 2 != 0:
            return arr[i]


def method02(arr):
    #  Time complexity of this solution is O(n). But it requires extra space for dict/map/hashing.
    l = len(arr)
    no_count_map = dict()
    # for i in range(l):
    #     no_count_map[arr[i]] = no_count_map.get(arr[i], 0) + 1
    for ele in arr:
        no_count_map[ele] = no_count_map.get(ele, 0)+1
    # for i in range(l):
    #     if no_count_map[arr[i]] % 2 !=0:
    #         return arr[i]

    for k, v in no_count_map.items():
        if v % 2 != 0:
            return k

def method03(arr):
    # The Best Solution is to do bitwise XOR of all the elements. XOR of all elements gives us odd occurring element.
    # Please note that XOR of two elements is 0 if both elements are same and XOR of a number x with 0 is x.
    res = 0
    for ele in arr:
        res = res ^ ele

    return res

def method04(arr):
    # using Lambda expression and reduce function
    return reduce(lambda x, y: x^ y, arr)

arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
print(method01(arr))
print(method02(arr))
print(method03(arr))
print(method04(arr))