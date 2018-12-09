# Uses python3
import sys
import random


def greedy_get_max_value(n, w, items_list):
    items_value_per_weight_and_weight_list = [[item[0]/item[1], item[1]] for item in items_list if item[1] != 0]
    items_value_per_weight_and_weight_list = sorted(items_value_per_weight_and_weight_list, key=lambda x: x[0], reverse=True)
    current_value = 0
    residue = w
    for value_per_weight, weight in items_value_per_weight_and_weight_list:
        taking_weight = min(residue, weight)
        current_value += taking_weight * value_per_weight
        residue -= taking_weight
        if residue == 0:
            break
    return round(current_value, 4)


with sys.stdin as f:
    input_list = f.readline().split()
    n = int(input_list[0])
    W = int(input_list[1])
    items_list = []
    for input_string in f:
        input_list = [int(i) for i in input_string.split()]
        items_list.append(input_list)
    my_algorithm_result = greedy_get_max_value(n, W, items_list)
    print(my_algorithm_result)

# while True:
#     n = random.randint(1, 1000)
#     W = random.randint(0, 2000000)
#     items = [[random.randint(0, 2000000), random.randint(0, 2000000)] for i in range(n)]
#     # m = 239
#     print("n = " + str(n) + " W = " + str(W))
#
#     my_algorithm_result = greedy_get_max_value(n, W, items)
#     print("Result greedy algorithm: " + str(my_algorithm_result))
#     # if my_algorithm_result != optimal_algorithm_result:
#     #     raise ValueError("Problem")
