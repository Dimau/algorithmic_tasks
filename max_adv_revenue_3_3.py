# Uses python3
import sys
import random


def naive_get_max_revenue(n, profit_per_click, clicks_per_day):
    result_sum = 0
    for i in range(n):
        max_permutation = -10000000000
        i_max_permutation = -1
        j_max_permutation = -1
        for profit in profit_per_click:
            for clicks_number in clicks_per_day:
                permutation = profit * clicks_number
                if ((profit >= 0 and clicks_number >= 0) or (profit <= 0 and clicks_number <= 0)) and permutation > max_permutation:
                    i_max_permutation = profit
                    j_max_permutation = clicks_number
                    max_permutation = permutation
                if ((profit > 0 and clicks_number < 0) or (profit < 0 and clicks_number > 0)) and permutation < max_permutation:
                    i_max_permutation = profit
                    j_max_permutation = clicks_number
                    max_permutation = permutation
        profit_per_click.remove(i_max_permutation)
        clicks_per_day.remove(j_max_permutation)
        result_sum += max_permutation
    return result_sum


def optimal_get_max_revenue(n, profit_per_click, clicks_per_day):
    profit_per_click = sorted(profit_per_click, reverse=True)
    clicks_per_day = sorted(clicks_per_day, reverse=True)
    result_sum = 0
    for i in range(n):
        result_sum += profit_per_click[i] * clicks_per_day[i]
    return result_sum


with sys.stdin as f:
    n = int(f.readline())
    profit_per_click = [int(item) for item in f.readline().split()]
    clicks_per_day = [int(item) for item in f.readline().split()]
    my_algorithm_result = optimal_get_max_revenue(n, profit_per_click, clicks_per_day)
    print(my_algorithm_result)

# while True:
#     n = random.randint(1, 3)
#     profit_per_click = [random.randint(0, 1000) - 500 for i in range(n)]
#     clicks_per_day = [random.randint(0, 1000) - 500 for i in range(n)]
#     profit_per_click = [-48, -460]
#     clicks_per_day = [151, 338]
#     n = 2
#     print("n = " + str(n) + " profit_per_click: " + str(profit_per_click) + " clicks_per_day: " + str(clicks_per_day))
#
#     my_algorithm_result = optimal_get_max_revenue(n, profit_per_click, clicks_per_day)
#     print("Result optimal algorithm: " + str(my_algorithm_result))
#     naive_algorithm_result = naive_get_max_revenue(n, profit_per_click, clicks_per_day)
#     print("Result naive algorithm: " + str(naive_algorithm_result))
#     if my_algorithm_result != naive_algorithm_result:
#         raise ValueError("Problem")
