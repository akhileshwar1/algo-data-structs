# uses python3

from last_digit import fib_digit
from last_digit_naive import fib_digit_naive
from stress_test import stress_gen

stress_gen(fib_digit_naive, fib_digit, 100, 0)
