# Uses python3
import sys
import random


def greedy_get_max_number_of_prizes(n):
    prizes_list = [1]
    residue = n - 1
    last_prize = 1
    while last_prize + 1 <= residue:
        last_prize += 1
        prizes_list.append(last_prize)
        residue -= last_prize
    else:
        prizes_list[len(prizes_list) - 1] += residue
    return len(prizes_list), prizes_list


# with sys.stdin as f:
#     n = int(f.readline())
#     my_algorithm_result_k, my_algorithm_result_prizes = greedy_get_max_number_of_prizes(n)
#     print(my_algorithm_result_k)
#     my_algorithm_result_prizes_string = [str(item) for item in my_algorithm_result_prizes]
#     print(" ".join(my_algorithm_result_prizes_string))

while True:
    n = random.randint(0, 1000000000)
    # n = 2
    print("n = " + str(n))
    my_algorithm_result_k, my_algorithm_result_prizes = greedy_get_max_number_of_prizes(n)
    print("Result greedy algorithm: " + str(my_algorithm_result_k) + " all prizes: " + str(my_algorithm_result_prizes))
