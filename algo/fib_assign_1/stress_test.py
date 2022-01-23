# uses python3
# general skeleton for stress testing
import random


def stress_gen(naive, opt, high, low):
    while True:
        n = random.randint(low, high)
        print(n)
        naive_result = naive(n)
        opt_result = opt(n)

        if(naive_result != opt_result):
            print(f'invalid for input case {n}')


def algo_number_general(n, high, low, algo):
    if(n >= low and n <= high):
        return algo(n)
    else:
        return None
