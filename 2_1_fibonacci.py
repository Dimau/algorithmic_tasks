# Uses python3
import sys
import random


# Naive algorithm
def naive_calc_fib(n):
    if n <= 1:
        return n
    return naive_calc_fib(n - 1) + naive_calc_fib(n - 2)


def get_fibonacci_number(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    pre_result = 1
    pre_pre_result = 0
    result = 0
    for i in range(n - 1):
        result = pre_pre_result + pre_result
        pre_pre_result = pre_result
        pre_result = result
    return result


with sys.stdin as f:
    input_value = int(f.readline())
    my_algorithm_result = get_fibonacci_number(input_value)
    print(my_algorithm_result)

# while True:
#     n = random.randint(0, 7)
#     print("Test data: " + str(n))
#
#     my_algorithm_result = get_fibonacci_number(n)
#     naive_algorithm_result = naive_calc_fib(n)
#     print("Result my algorithm: " + str(my_algorithm_result))
#     print("Result naive algorithm: " + str(naive_algorithm_result))
#     if my_algorithm_result != naive_algorithm_result:
#         raise ValueError("Problem")
