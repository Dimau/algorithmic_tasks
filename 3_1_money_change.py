# Uses python3
import sys
import random


def greedy_get_number_of_coins(m):
    number_of_coins = 0
    set_of_coins_for_change = [1, 10, 5]
    set_of_coins_for_change = sorted(set_of_coins_for_change, reverse=True)
    residue = m
    for i in range(len(set_of_coins_for_change)):
        number_of_coins_i = 0
        while residue >= set_of_coins_for_change[i]:
            number_of_coins_i += 1
            residue -= set_of_coins_for_change[i]
        number_of_coins += number_of_coins_i
    return number_of_coins


def optimal_get_number_of_coins(m):
    number_10 = m // 10
    residue = m - number_10 * 10
    number_5 = residue // 5
    residue = residue - number_5 * 5
    number_1 = residue
    return number_10 + number_5 + number_1


with sys.stdin as f:
    input_list = f.readline().split()
    m = int(input_list[0])
    my_algorithm_result = greedy_get_number_of_coins(m)
    print(my_algorithm_result)

# while True:
#     m = random.randint(1, 1000)
#     # m = 239
#     print("Test data: " + str(m))
#
#     my_algorithm_result = greedy_get_number_of_coins(m)
#     optimal_algorithm_result = optimal_get_number_of_coins(m)
#     print("Result greedy algorithm: " + str(my_algorithm_result))
#     print("Result optimal algorithm: " + str(optimal_algorithm_result))
#     if my_algorithm_result != optimal_algorithm_result:
#         raise ValueError("Problem")
