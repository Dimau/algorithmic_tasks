# Uses python3
import sys
import random


# Naive algorithm
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_my(n, m):
    source_list = calculate_source_list(n, m)
    length_of_sequence = find_length_of_sequence(source_list)
    result = source_list[n % length_of_sequence]
    return result


def calculate_source_list(n, m):
    result_list = [0, 1]
    pre_result = 1
    pre_pre_result = 0
    for i in range(10000):
        current_value = pre_pre_result + pre_result
        pre_pre_result = pre_result
        pre_result = current_value
        result_list.append(current_value % m)
    return result_list


def find_length_of_sequence(source_list):
    for i in range(2, 10000):
        for j in range(i):
            if source_list[j] != source_list[j + i]:
                break
        else:
            return i
    return False


with sys.stdin as f:
    input_list = f.readline().split()
    a = int(input_list[0])
    b = int(input_list[1])
    my_algorithm_result = get_fibonacci_huge_my(a, b)
    print(my_algorithm_result)

# while True:
#     n = random.randint(1, 100)
#     m = random.randint(2, 1000)
#     n = 2816213588
#     m = 239
#     print("Test data: " + str(n) + " " + str(m))
#
#     my_algorithm_result = get_fibonacci_huge_my(n, m)
#     naive_algorithm_result = get_fibonacci_huge_naive(n, m)
#     print("Result my algorithm: " + str(my_algorithm_result))
#     print("Result naive algorithm: " + str(naive_algorithm_result))
#     if my_algorithm_result != naive_algorithm_result:
#         raise ValueError("Problem")
