# Uses python3
import sys
import random


def greedy_get_min_amount_of_visits(n, time_segments):
    time_segments = sorted(time_segments, key=lambda x: x[1])
    visits = []
    for segment in time_segments:
        if len(visits) == 0:
            visits.append(segment[1])
            continue
        for visit in reversed(visits):
            if visit >= segment[0] and visit <= segment[1]:
                break
            if visit < segment[0]:
                visits.append(segment[1])
                break
    return len(visits), visits


with sys.stdin as f:
    n = int(f.readline())
    time_segments = []
    for input_string in f:
        input_list = [int(i) for i in input_string.split()]
        time_segments.append(input_list)
    my_algorithm_result_m, my_algorithm_result_visits = greedy_get_min_amount_of_visits(n, time_segments)
    print(my_algorithm_result_m)
    my_algorithm_result_visits_string = [str(item) for item in my_algorithm_result_visits]
    print(" ".join(my_algorithm_result_visits_string))

# while True:
#     n = random.randint(1, 100)
#     time_segments = []
#     for i in range(n):
#         begin_time = random.randint(0, 1000000000)
#         duration = random.randint(0, 1000000000)
#         time_segments.append([begin_time, min(begin_time + duration, 1000000000)])
#     print("n = " + str(n) + " time_segments: " + str(time_segments))
#
#     my_algorithm_result_m, my_algorithm_result_visits = greedy_get_min_amount_of_visits(n, time_segments)
#     print("Result greedy algorithm: " + str(my_algorithm_result_m) + " all visits: " + str(my_algorithm_result_visits))
