# Uses python3
import sys
import random
import math
import copy


def select_sort(unsorted_array):
    for i in range(len(unsorted_array)):
        min_value = unsorted_array[i]
        for j in range(i + 1, len(unsorted_array)):
            if unsorted_array[j] < min_value:
                min_value = unsorted_array[j]
                unsorted_array[i], unsorted_array[j] = unsorted_array[j], unsorted_array[i]


def quick_sort(unsorted_array, l, r):
    if l >= r:
        return
    m1, m2 = partition3(unsorted_array, l, r)
    quick_sort(unsorted_array, l, m1 - 1)
    quick_sort(unsorted_array, m2 + 1, r)


def partition3(unsorted_array, l, r):
    middle_value_index = find_middle_value_index(unsorted_array, l, r)
    unsorted_array[l], unsorted_array[middle_value_index] = unsorted_array[middle_value_index], unsorted_array[l]
    pivot = unsorted_array[l]
    m1 = m2 = l
    for i in range(l + 1, r + 1):
        if unsorted_array[i] == pivot:
            unsorted_array[m2 + 1], unsorted_array[i] = unsorted_array[i], unsorted_array[m2 + 1]
            m2 += 1
        elif unsorted_array[i] < pivot:
            unsorted_array[m2 + 1], unsorted_array[i] = unsorted_array[i], unsorted_array[m2 + 1]
            unsorted_array[m2 + 1], unsorted_array[m1] = unsorted_array[m1], unsorted_array[m2 + 1]
            m1 += 1
            m2 += 1
    return m1, m2


def find_middle_value_index(unsorted_array, l, r):
    if l == r:
        return l
    mapping = [[l, unsorted_array[l]], [math.floor((l + r) / 2), unsorted_array[math.floor((l + r) / 2)]], [r, unsorted_array[r]]]
    sorted_array = sorted(mapping, key=lambda x: x[1])
    return sorted_array[1][0]


with sys.stdin as f:
    f.readline()
    input_array = [int(i) for i in f.readline().split()]
    quick_sort(input_array, 0, len(input_array) - 1)
    result_string = " ".join([str(item) for item in input_array])
    print(result_string)

# while True:
#     n = random.randint(1, 100)
#     input_array = []
#     for _ in range(n):
#         input_array.append(random.randint(1, 3))
#     input_array_string = " ".join([str(item) for item in input_array])
#     print("n = " + str(n) + " input_array: " + input_array_string)
#     input_array_1 = copy.copy(input_array)
#     select_sort(input_array_1)
#     input_array_2 = copy.copy(input_array)
#     quick_sort(input_array_2, 0, len(input_array_2) - 1)
#     if input_array_1 != input_array_2:
#         raise ValueError("Problem")

# unsorted_array = [2, 3, 9, 2, 9]
# quick_sort(unsorted_array, 0, len(unsorted_array) - 1)
# print(unsorted_array)
