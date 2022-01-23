# using python3
from stress_test import algo_number_general


def fib_digit(n):
    prev = 0
    current = 1
    if(n <= 1):
        return n
    for i in range(n-1):
        prev, current = current, prev % 10 + current % 10

    return current


n = int(input())
print(algo_number_general(n, 10**7, 0, fib_digit))
