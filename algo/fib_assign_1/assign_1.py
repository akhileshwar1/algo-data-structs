# Uses python3
from stress_test import algo_number_general


def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


# n = int(input())
# print(algo_number_general(n, 45, 0, calc_fib))
