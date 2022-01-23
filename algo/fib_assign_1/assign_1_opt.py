# using python3
from stress_test import algo_number_general


def calc_fib_opt(n):
    prev = 0
    current = 1
    if(n <= 1):
        return n
    for i in range(n-1):
        prev, current = current, current + prev

    return current


# n = int(input())
# print(algo_number_general(n, 45, 0, calc_fib_opt))
