# Uses python3
import sys
import random


def dp_get_edit_distance(string_1, string_2):
    # generating empty matrix
    number_of_operations = []
    for i in range(len(string_1) + 1):
        number_of_operations.append([])
        for j in range(len(string_2) + 1):
            number_of_operations[i].append(0)

    for i in range(1, len(string_2) + 1):
        number_of_operations[0][i] = number_of_operations[0][i - 1] + 1

    for i in range(1, len(string_1) + 1):
        number_of_operations[i][0] = number_of_operations[i - 1][0] + 1

    for i in range(1, len(string_1) + 1):
        for j in range(1, len(string_2) + 1):
            deletion = number_of_operations[i][j - 1] + 1
            insertion = number_of_operations[i - 1][j] + 1
            if string_1[i - 1] != string_2[j - 1]:
                change = number_of_operations[i - 1][j - 1] + 1
            else:
                change = number_of_operations[i - 1][j - 1]
            number_of_operations[i][j] = min(deletion, insertion, change)

    return number_of_operations[len(string_1)][len(string_2)]


with sys.stdin as f:
    string1 = str(f.readline())
    string2 = str(f.readline())
    number_of_operations = dp_get_edit_distance(string1, string2)
    print(number_of_operations)

# n = random.randint(1, 10)
# m = random.randint(1, 10)
# print("Test data: " + str(n) + " " + str(m))
# string_1 = "editing"
# string_2 = "distance"
# number_of_operations = dp_get_edit_distance(string_1, string_2)
# print("number of operations: " + str(number_of_operations))
