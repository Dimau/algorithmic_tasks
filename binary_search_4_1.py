# Uses python3
import sys
import random
import math


def binary_search(b, sorted_array):
    l = 0  # start index of current segment of array
    r = len(sorted_array) - 1  # end index of current segment of array
    while l <= r:
        m = math.floor(l + (r - l) / 2)
        if b == sorted_array[m]:
            return m
        elif b > sorted_array[m]:
            l = m + 1
        else:
            r = m - 1
    return -1


def linear_search(b, sorted_array):
    for i in range(len(sorted_array)):
        if b == sorted_array[i]:
            return i
    return -1


with sys.stdin as f:
    input_array = [int(i) for i in sys.stdin.readline().split()]
    del(input_array[0])
    search_goals_array = [int(i) for i in sys.stdin.readline().split()]
    del(search_goals_array[0])
    result_array = []
    for search_goal in search_goals_array:
        binary_result = binary_search(search_goal, input_array)
        result_array.append(binary_result)
    result_array_string = [str(item) for item in result_array]
    print(" ".join(result_array_string))

# while True:
#     b = random.randint(1, 1000)
#     input_array = []
#     for _ in range(100):
#         input_array.append(random.randint(1, 10))
#     input_array.sort()
#     input_array_string = " ".join([str(item) for item in input_array])
#     print("b = " + str(b) + " input_array: " + input_array_string)
#     linear_result = linear_search(b, input_array)
#     binary_result = binary_search(b, input_array)
#     print('linear_result = ' + str(linear_result) + " binary_result = " + str(binary_result))
#     if linear_result != -1 and binary_result != -1 and input_array[linear_result] != input_array[binary_result]:
#         raise ValueError("Problem")
