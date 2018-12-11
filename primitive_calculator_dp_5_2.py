# Uses python3
import sys
import random


def dp_get_number_of_operations(n):
    number_of_operations = []
    prev_value_for_every_position = []
    number_of_operations.append(0)
    number_of_operations.append(0)
    prev_value_for_every_position.append(1)
    prev_value_for_every_position.append(1)
    if n == 1:
        return number_of_operations[n - 1], prev_value_for_every_position[n - 1]
    for i in range(2, n + 1):
        options = [[int(i / 2), 10000000], [int(i / 3), 10000000], [i - 1, 10000000]]
        if i % 2 == 0:
            options[0][1] = number_of_operations[int(i / 2)] + 1
        if i % 3 == 0:
            options[1][1] = number_of_operations[int(i / 3)] + 1
        options[2][1] = number_of_operations[i - 1] + 1
        options.sort(key=lambda x: x[1])
        number_of_operations.append(options[0][1])
        prev_value_for_every_position.append(options[0][0])
    # Computation of the path
    path = []
    pointer = n
    while pointer > 1:
        path.append(prev_value_for_every_position[pointer])
        pointer = prev_value_for_every_position[pointer]
    path.sort()
    path.append(n)
    return number_of_operations[n], ' '.join([str(item) for item in path])


with sys.stdin as f:
    n = int(f.readline())
    number_of_operations, path = dp_get_number_of_operations(n)
    print(number_of_operations)
    print(path)

# while True:
#     n = random.randint(1, 100)
#     print("Test data: " + str(n))
#
#     number_of_operations, path = dp_get_number_of_operations(n)
#     print("number of operations: " + str(number_of_operations))
#     print("path: " + str(path))
    # if my_algorithm_result != optimal_algorithm_result:
    #     raise ValueError("Problem")
