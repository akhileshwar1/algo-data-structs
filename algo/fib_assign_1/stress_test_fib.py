# uses python3

from assign_1_opt import calc_fib_opt
from assign_1 import calc_fib
from stress_test import stress_gen

stress_gen(calc_fib, calc_fib_opt, 10, 1)
