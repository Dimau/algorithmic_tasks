# Uses python3
import sys
import random


def dp_get_number_of_coins(m):
    set_of_coins_for_change = [1, 3, 4]
    number_of_coins = []
    coins_value_for_every_position = []
    number_of_coins.append(0)
    coins_value_for_every_position.append(0)
    for i in range(1, m + 1):
        coins = {}
        for coin in set_of_coins_for_change:
            if i - coin < 0:
                continue
            coins[coin] = number_of_coins[i - coin] + 1
        min_amount_of_coins = min(coins.values())
        number_of_coins.append(min_amount_of_coins)
        # This is for tracing of adding coins
        # for key, value in coins.items():
        #     if value == min_amount_of_coins:
        #         coins_value_for_every_position.append(key)
        #         break
    # test
    # sum = m
    # while sum > 0:
    #     print(coins_value_for_every_position[sum])
    #     sum -= coins_value_for_every_position[sum]
    return number_of_coins[m]


def optimal_get_number_of_coins(m):
    number_4 = m // 4
    residue = m - number_4 * 4
    number_3 = residue // 3
    residue = residue - number_3 * 3
    number_1 = residue
    return number_4 + number_3 + number_1


with sys.stdin as f:
    m = int(f.readline())
    my_algorithm_result = dp_get_number_of_coins(m)
    print(my_algorithm_result)

# while True:
#     m = random.randint(1, 100)
#     m = 50
#     print("Test data: " + str(m))
#
#     my_algorithm_result = dp_get_number_of_coins(m)
#     optimal_algorithm_result = optimal_get_number_of_coins(m)
#     print("Result dp algorithm: " + str(my_algorithm_result))
#     print("Result optimal algorithm: " + str(optimal_algorithm_result))
#     if my_algorithm_result != optimal_algorithm_result:
#         raise ValueError("Problem")
