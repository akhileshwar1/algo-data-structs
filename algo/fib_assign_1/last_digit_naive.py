# using python3
from stress_test import algo_number_general


def fib_digit_naive(n):
    prev = 0
    current = 1
    if(n <= 1):
        return n
    for i in range(n-1):
        prev, current = current, prev + current

    return current % 10


# n = int(input())
# print(algo_number_general(n, 0, 10**7, fib_digit_naive))
