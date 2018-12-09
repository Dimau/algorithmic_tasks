# Uses python3
import sys
import random


# Naive algorithm
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd(a, b):
    current_gcd = 1
    current_min = min(a, b)
    current_max = max(a, b)
    residue = 1
    while residue != 0:
        residue = current_max % current_min
        current_max = current_min
        current_min = residue
    return current_max


with sys.stdin as f:
    input_list = f.readline().split()
    a = int(input_list[0])
    b = int(input_list[1])
    my_algorithm_result = gcd(a, b)
    print(my_algorithm_result)

# while True:
#     a = random.randint(1, 1000)
#     b = random.randint(1, 1000)
#     a = 28851538
#     b = 1183019
#     print("Test data: " + str(a) + " " + str(b))
#
#     my_algorithm_result = gcd(a, b)
#     # naive_algorithm_result = gcd_naive(a, b)
#     print("Result my algorithm: " + str(my_algorithm_result))
#     # print("Result naive algorithm: " + str(naive_algorithm_result))
#     # if my_algorithm_result != naive_algorithm_result:
#     #     raise ValueError("Problem")
