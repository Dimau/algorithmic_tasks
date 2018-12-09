# Uses python3
import sys
import random
import math


def naive_extract_majority_element(unsorted_array):
    for i in range(len(unsorted_array)):
        counter = 1
        for j in range(i + 1, len(unsorted_array)):
            if unsorted_array[j] == unsorted_array[i]:
                counter += 1
        if counter > math.floor(len(unsorted_array) / 2):
            return 1
    return 0


def extract_majority_element(unsorted_array):
    l = 0
    r = len(unsorted_array) - 1
    half_of_array = math.floor(len(unsorted_array) / 2)
    return adaptive_quick_sort(unsorted_array, l, r, half_of_array)


def adaptive_quick_sort(unsorted_array, l, r, half_of_array):
    if l > r:
        return 0
    m1, m2 = partition3(unsorted_array, l, r)
    if (m2 - m1 + 1) > half_of_array:
        return 1
    res1 = adaptive_quick_sort(unsorted_array, l, m1 - 1, half_of_array)
    res2 = adaptive_quick_sort(unsorted_array, m2 + 1, r, half_of_array)
    return res1 + res2


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
            unsorted_array[m2 + 1], unsorted_array[m1], unsorted_array[i] = unsorted_array[m1], unsorted_array[i], unsorted_array[m2 + 1]
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
    result = extract_majority_element(input_array)
    print(result)

# while True:
#     n = random.randint(1, 100)
#     input_array = []
#     for _ in range(n):
#         input_array.append(random.randint(1, 3))
#     input_array_string = " ".join([str(item) for item in input_array])
#     print("n = " + str(n) + " input_array: " + input_array_string)
#     naive_result = naive_extract_majority_element(input_array)
#     my_result = extract_majority_element(input_array)
#     print('naive_result = ' + str(naive_result) + " my_result = " + str(my_result))
#     if naive_result != my_result:
#         raise ValueError("Problem")

# unsorted_array = [4, 6, 4, 2, 4, 4, 7, 4, 0, 4]
# print(extract_majority_element(unsorted_array))
