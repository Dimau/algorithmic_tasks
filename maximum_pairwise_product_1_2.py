# Uses python3
import sys
import random
import copy


def get_max_pairwise_product(list_of_items):
    inner_list_of_items = copy.copy(list_of_items)
    index_max = 0
    max_value = inner_list_of_items[0]
    for i in range(len(inner_list_of_items)):
        if inner_list_of_items[i] > max_value:
            max_value = inner_list_of_items[i]
            index_max = i
    del inner_list_of_items[index_max]

    pre_max_value = inner_list_of_items[0]
    for i in range(len(inner_list_of_items)):
        if inner_list_of_items[i] > pre_max_value:
            pre_max_value = inner_list_of_items[i]

    return max_value * pre_max_value


def naive_get_max_pairwise_product(list_of_items):
    product = 0
    for i in range(len(list_of_items)):
        for j in range(i + 1, len(list_of_items)):
            product = max(product, list_of_items[i] * list_of_items[j])
    return product


def generate_test_data(n, m):
    list_of_items = []
    for i in range(n):
        list_of_items.append(random.randint(0, m))
    return " ".join([str(item) for item in list_of_items])


with sys.stdin as f:
    number_of_values = f.readline()
    input_str = f.readline()
    list_of_items = [int(item) for item in input_str.split()]
    my_algorithm_result = get_max_pairwise_product(list_of_items)
    print(my_algorithm_result)


# while True:
#     n = random.randint(2, 10)
#     m = random.randint(10, 1000)
#     test_data = generate_test_data(n, m)
#     print("Test data: " + test_data)
#
#     list_of_items = [int(item) for item in test_data.split()]
#     my_algorithm_result = get_max_pairwise_product(list_of_items)
#     naive_algorithm_result = naive_get_max_pairwise_product(list_of_items)
#     print("Result my algorithm: " + str(my_algorithm_result))
#     print("Result naive algorithm: " + str(naive_algorithm_result))
#     if my_algorithm_result != naive_algorithm_result:
#         raise ValueError("Problem")
