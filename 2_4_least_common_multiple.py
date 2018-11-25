# Uses python3
import sys
import random


# Naive algorithm
def naive_lcm(a, b):
    current_lcm = max(a, b)
    while True:
        if current_lcm % a == 0 and current_lcm % b == 0:
            return current_lcm
        current_lcm += 1


def lcm(a, b):
    current_lcm = max(a, b)
    step = max(a, b)
    while True:
        if current_lcm % a == 0 and current_lcm % b == 0:
            return current_lcm
        current_lcm += step


with sys.stdin as f:
    input_list = f.readline().split()
    a = int(input_list[0])
    b = int(input_list[1])
    my_algorithm_result = lcm(a, b)
    print(my_algorithm_result)

# while True:
#     a = random.randint(1, 1000)
#     b = random.randint(1, 1000)
#     a = 28851538
#     b = 1183019
#     print("Test data: " + str(a) + " " + str(b))
#
#     my_algorithm_result = lcm(a, b)
#     # naive_algorithm_result = naive_lcm(a, b)
#     print("Result my algorithm: " + str(my_algorithm_result))
#     # print("Result naive algorithm: " + str(naive_algorithm_result))
#     # if my_algorithm_result != naive_algorithm_result:
#     #     raise ValueError("Problem")
